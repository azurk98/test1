"""Dostupnost i atraktivnost lokacije po H3 polju (ne mijenja procjenu stanovnika).

Ulaz:  raw/Sarajewo.osm.gz (cestovna mreža, stanice javnog prevoza),
       raw/osm_grad.json (POI), out/polja_h3.gpkg (stanovnici po polju)
Izlaz: out/dostupnost_h3.gpkg, out/dostupnost_h3.csv

Pokazatelji po polju:
  pjesice_5/10/15   stanovnici dostupni pješice za 5/10/15 min (mreža ulica i staza; 4,8 km/h na
                    ravnom, nagib po Toblerovoj formuli: sporije uzbrdo i strmo nizbrdo)
  auto_5/10/15      stanovnici dostupni autom za 5/10/15 min (jednosmjerne ulice, ograničenja brzine)
  poi_10min         trgovine/usluge (shop, amenity, office) dostupne pješice za 10 min
  stanica_m         udaljenost do najbliže stanice javnog prevoza (m)
  stanica_tip       tip najbliže stanice (tramvaj, trolejbus, autobus)
  stanice_400m      broj stanica u krugu 400 m; tramvaj_400m posebno
  glavna_cesta_m    udaljenost do primarne/sekundarne/magistralne ceste (m)
  ulice_km_km2      gustina ulica (km po km²)
  raskrsnice_km2    broj raskrsnica (čvorovi s ≥ 3 ulice) po km²
  atraktivnost      0–100, ponderisani zbir percentilnih rangova (TEZINE ispod)

Dostupni stanovnici računaju se samo iz šest modeliranih općina; kod rubova
prema Ilidži, Vogošći i Istočnom Sarajevu potcijenjeni su (rubni efekat).
Vremena autom: ograničenje brzine (ili tipična brzina klase ceste) × 0,65; javni prevoz je samo blizina
stanica, bez voznog reda.
"""
from __future__ import annotations

import gzip
import re
import xml.etree.ElementTree as ET

import geopandas as gpd
import numpy as np
import pandas as pd
from pathlib import Path

from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components, dijkstra
from scipy.spatial import cKDTree
from shapely.geometry import LineString

from common import OSM_IME
from common import CRS_M, CRS_WGS, OUT, RAW, overpass_u_gdf

PJESACKA_BRZINA = 4.8  # km/h
# stvarna gradska brzina vožnje ≈ 65% ograničenja (semafori, raskrsnice, gužva);
# uobičajena aproksimacija bez podataka o saobraćaju
FAKTOR_GRADSKE_VOZNJE = 0.65
PRAGOVI_MIN = (5, 10, 15)

# km/h po klasi ceste kad maxspeed nije upisan (gradska vožnja bez gužve)
BRZINA_AUTO = {
    "motorway": 80, "motorway_link": 50, "trunk": 60, "trunk_link": 40,
    "primary": 50, "primary_link": 35, "secondary": 45, "secondary_link": 30,
    "tertiary": 40, "tertiary_link": 30, "unclassified": 30, "residential": 30,
    "living_street": 10, "service": 15, "track": 10, "road": 25,
}
NEPJESACKE = {"motorway", "motorway_link", "trunk_link", "construction", "proposed",
              "raceway", "bus_guideway", "services", "via_ferrata", "corridor", "elevator"}
GLAVNE = {"motorway", "trunk", "primary", "secondary"}

# Ponderi atraktivnosti (zbir 1). Svaki pokazatelj se pretvara u percentilni rang
# među naseljenim poljima; za udaljenosti manje je bolje.
TEZINE = {
    "pjesice_10": 0.20,      # pješačka masa potencijalnih kupaca
    "auto_10": 0.15,         # automobilski doseg
    "poi_10min": 0.20,       # postojeća ponuda / prolaznost
    "stanice_400m": 0.15,    # javni prevoz u blizini
    "stanica_m": 0.10,       # (manje = bolje)
    "glavna_cesta_m": 0.10,  # vidljivost / pristup s glavne ceste (manje = bolje)
    "raskrsnice_km2": 0.10,  # povezanost ulične mreže
}
MANJE_JE_BOLJE = {"stanica_m", "glavna_cesta_m"}


def brzina(tags: dict) -> float:
    m = re.match(r"\s*(\d+)", tags.get("maxspeed", ""))
    if m:
        return float(m.group(1))
    return float(BRZINA_AUTO.get(tags["highway"], 0))


def ucitaj_mrezu(xml_gz):
    nodes, ways, stops = {}, [], []
    with gzip.open(xml_gz, "rb") as f:
        for _, el in ET.iterparse(f):
            if el.tag == "node":
                i = int(el.get("id"))
                lat, lon = float(el.get("lat")), float(el.get("lon"))
                nodes[i] = (lon, lat)
                t = {c.get("k"): c.get("v") for c in el.findall("tag")}
                if t and (t.get("highway") == "bus_stop" or t.get("railway") == "tram_stop"
                          or t.get("public_transport") in ("platform", "stop_position")):
                    tip = ("tramvaj" if t.get("railway") == "tram_stop" or t.get("tram") == "yes"
                           else "trolejbus" if t.get("trolleybus") == "yes" else "autobus")
                    stops.append((lon, lat, tip, t.get("name", "")))
                el.clear()
            elif el.tag == "way":
                t = {c.get("k"): c.get("v") for c in el.findall("tag")}
                if "highway" in t:
                    ways.append((t, [int(n.get("ref")) for n in el.findall("nd")]))
                el.clear()
            elif el.tag == "relation":
                el.clear()
    return nodes, ways, stops


def tobler_kmh(nagib):
    """Toblerova brzina hoda (km/h) za nagib dz/dx, skalirana da je na ravnom PJESACKA_BRZINA.
    Najbrže na blagom nizbrdu (-5%); 10% uzbrdo ~3,4 km/h, 20% uzbrdo ~2,4 km/h."""
    return PJESACKA_BRZINA / np.exp(-3.5 * 0.05) * np.exp(-3.5 * np.abs(np.clip(nagib, -1, 1) + 0.05))


def visine_cvorova(lon, lat, sigma: float = 2, tlo: bool = False) -> np.ndarray:
    """Nadmorska visina čvorova iz Copernicus DEM-a (izglađenog ~60 m, kao u 10_teren.py)."""
    import importlib.util
    from scipy.ndimage import gaussian_filter
    sp = importlib.util.spec_from_file_location("teren", Path(__file__).with_name("10_teren.py"))
    ter = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(ter)
    z, t = ter.dem()
    if tlo:
        # DSM -> približno tlo: najniža tačka u prozoru 90 m (ceste su na tlu, krovovi nisu)
        from scipy.ndimage import grey_opening
        z = grey_opening(z, size=(3, 3))
    z = gaussian_filter(z, sigma=sigma)
    col = np.clip(((np.asarray(lon) - t.c) / t.a).astype(int), 0, z.shape[1] - 1)
    row = np.clip(((np.asarray(lat) - t.f) / t.e).astype(int), 0, z.shape[0] - 1)
    return z[row, col]


def graf(nodes, ways, xy, idx, mod: str, visine=None):
    """Rijetka matrica vremena (minute) između čvorova za 'pjesice' ili 'auto'.
    Uz visine (m po čvoru) pješačko vrijeme zavisi od nagiba i smjera (Tobler)."""
    r, c, w = [], [], []
    for t, nds in ways:
        hw = t["highway"]
        if mod == "pjesice":
            if hw in NEPJESACKE or t.get("foot") == "no" or t.get("access") == "no" and t.get("foot") != "yes":
                continue
            v = PJESACKA_BRZINA
            jedno = 0
        else:
            v = brzina(t) * FAKTOR_GRADSKE_VOZNJE
            if v <= 0 or t.get("motor_vehicle") == "no" or t.get("access") in ("no", "private"):
                continue
            ow = t.get("oneway")
            jedno = 1 if ow in ("yes", "1", "true") or (t.get("junction") == "roundabout" and ow != "no") \
                else (-1 if ow == "-1" else 0)
        for a, b in zip(nds[:-1], nds[1:]):
            if a not in idx or b not in idx:
                continue
            i, j = idx[a], idx[b]
            d = float(np.hypot(*(xy[i] - xy[j])))
            minute = d / 1000 / v * 60
            minute_nazad = minute
            if mod == "pjesice" and visine is not None and d > 0:
                nag = (visine[j] - visine[i]) / d
                minute = d / 1000 / tobler_kmh(nag) * 60
                minute_nazad = d / 1000 / tobler_kmh(-nag) * 60
            if jedno >= 0:
                r.append(i); c.append(j); w.append(minute)
            if jedno <= 0:
                r.append(j); c.append(i); w.append(minute_nazad)
    n = len(xy)
    return coo_matrix((w, (r, c)), shape=(n, n)).tocsr()


def dostupno(G, izvori, pop_cvor, poi_cvor, pragovi, ulaz_min):
    """Za svaki izvor: zbir stanovnika (i POI) u čvorovima dostupnim unutar praga."""
    lim = max(pragovi)
    pop = np.zeros((len(izvori), len(pragovi)))
    poi = np.zeros((len(izvori), len(pragovi)))
    cv_pop, w_pop = pop_cvor
    cv_poi, w_poi = poi_cvor
    for s in range(0, len(izvori), 64):
        blok = izvori[s:s + 64]
        D = dijkstra(G, indices=blok, limit=lim)
        Dp = D[:, cv_pop] + ulaz_min[s:s + 64, None]
        Dq = D[:, cv_poi] + ulaz_min[s:s + 64, None]
        for k, p in enumerate(pragovi):
            pop[s:s + len(blok), k] = (Dp <= p) @ w_pop
            poi[s:s + len(blok), k] = (Dq <= p) @ w_poi
    return pop, poi


def main() -> None:
    polja = gpd.read_file(OUT / "polja_h3.gpkg")
    nodes, ways, stops = ucitaj_mrezu(RAW / OSM_IME)
    print(f"Mreža: {len(ways)} cesta/staza, {len(stops)} oznaka stanica")

    used = sorted({n for _, nds in ways for n in nds if n in nodes})
    idx = {n: k for k, n in enumerate(used)}
    pts = gpd.GeoSeries(gpd.points_from_xy(*zip(*[nodes[n] for n in used])), crs=CRS_WGS).to_crs(CRS_M)
    xy = np.c_[pts.x, pts.y]
    ll = np.array([nodes[n] for n in used])
    vis = visine_cvorova(ll[:, 0], ll[:, 1])  # nagib u pješačkom vremenu (Tobler)

    # središte polja: težište stambene površine je bolje od geometrijskog, ali polje
    # bez zgrada nema ga; koristi se reprezentativna tačka heksagona
    cen = polja.geometry.centroid
    cxy = np.c_[cen.x, cen.y]
    st = polja.stanovnici.to_numpy(float)

    # POI tačke
    osm = overpass_u_gdf(RAW / "osm_grad.json")
    kol = [k for k in ("shop", "amenity", "office") if k in osm]
    poi = osm[(osm.geom_type == "Point") & osm[kol].notna().any(axis=1)].to_crs(CRS_M)
    if "amenity" in poi:  # klupe, kante i slično nisu ponuda
        poi = poi[~poi.amenity.isin(["bench", "waste_basket", "parking", "bicycle_parking",
                                     "recycling", "drinking_water", "parking_entrance", "vending_machine"])]
    pxy = np.c_[poi.geometry.x, poi.geometry.y]
    print(f"POI (trgovine, usluge, uredi): {len(poi)}")

    rez = pd.DataFrame({"h3_id": polja.h3_id})
    for mod in ("pjesice", "auto"):
        G = graf(nodes, ways, xy, idx, mod, visine=vis if mod == "pjesice" else None)
        # najveća (jako) povezana komponenta, da se ne snapuje na izolovane dijelove
        _, lab = connected_components(G, directed=True, connection="strong" if mod == "auto" else "weak")
        glavna = np.bincount(lab).argmax()
        ok = np.where(lab == glavna)[0]
        tree = cKDTree(xy[ok])
        d_c, i_c = tree.query(cxy)
        d_p, i_p = tree.query(pxy)
        cv_c = ok[i_c]
        ulaz = d_c / 1000 / PJESACKA_BRZINA * 60  # pješice do mreže
        # stanovnici i POI pridruženi čvorovima mreže
        pop_c = pd.Series(st).groupby(cv_c).sum()
        poi_c = pd.Series(1.0, index=range(len(pxy))).groupby(ok[i_p]).sum()
        izvori = np.arange(len(polja))
        cvorovi = cv_c[izvori]
        Gs = G
        pop, poin = dostupno(Gs, cvorovi, (pop_c.index.to_numpy(), pop_c.to_numpy()),
                             (poi_c.index.to_numpy(), poi_c.to_numpy()), PRAGOVI_MIN, ulaz)
        for k, p in enumerate(PRAGOVI_MIN):
            rez[f"{mod}_{p}"] = pop[:, k].round().astype(int)
        if mod == "pjesice":
            rez["poi_10min"] = poin[:, PRAGOVI_MIN.index(10)].round().astype(int)
        print(f"  {mod}: {G.nnz} veza, komponenta {len(ok)} čvorova")

    # stanice: spoji oznake bliže od 40 m (stub + peron iste stanice)
    s = gpd.GeoDataFrame(pd.DataFrame(stops, columns=["lon", "lat", "tip", "ime"]),
                         geometry=gpd.points_from_xy([a[0] for a in stops], [a[1] for a in stops]),
                         crs=CRS_WGS).to_crs(CRS_M)
    sxy = np.c_[s.geometry.x, s.geometry.y]
    grupa = -np.ones(len(s), int)
    t = cKDTree(sxy)
    for i in range(len(s)):
        if grupa[i] < 0:
            for j in t.query_ball_point(sxy[i], 40):
                if grupa[j] < 0:
                    grupa[j] = i
    prio = {"tramvaj": 0, "trolejbus": 1, "autobus": 2}
    s["g"] = grupa
    s["p"] = s.tip.map(prio)
    st_g = s.sort_values("p").groupby("g").agg(x=("geometry", lambda g: g.x.mean()),
                                                y=("geometry", lambda g: g.y.mean()), tip=("tip", "first"))
    gxy = st_g[["x", "y"]].to_numpy()
    print(f"Stanice nakon spajanja: {len(st_g)} ({st_g.tip.value_counts().to_dict()})")
    ts = cKDTree(gxy)
    d, i = ts.query(cxy)
    rez["stanica_m"] = d.round().astype(int)
    rez["stanica_tip"] = st_g.tip.to_numpy()[i]
    rez["stanice_400m"] = ts.query_ball_point(cxy, 400, return_length=True)
    tram = gxy[st_g.tip.to_numpy() == "tramvaj"]
    rez["tramvaj_400m"] = cKDTree(tram).query_ball_point(cxy, 400, return_length=True) if len(tram) else 0

    # ceste: udaljenost do glavne, gustina ulica, raskrsnice
    seg, glavne = [], []
    stepen = np.zeros(len(xy), int)
    for tg, nds in ways:
        if tg["highway"] in NEPJESACKE - {"motorway", "motorway_link"} or tg["highway"] in ("footway", "path", "steps", "cycleway", "track", "bridleway", "pedestrian"):
            continue
        k = [idx[n] for n in nds if n in idx]
        if len(k) < 2:
            continue
        ln = LineString(xy[k])
        seg.append(ln)
        if tg["highway"] in GLAVNE:
            glavne.append(ln)
        stepen[k[0]] += 1
        stepen[k[-1]] += 1
        stepen[k[1:-1]] += 2
    ulice = gpd.GeoDataFrame(geometry=seg, crs=CRS_M)
    import shapely
    rez["glavna_cesta_m"] = shapely.distance(cen.to_numpy(), shapely.union_all(glavne)).round().astype(int)
    pu = gpd.sjoin(ulice, polja[["h3_id", "geometry"]], predicate="intersects")
    hexg = polja.set_index("h3_id").geometry
    pu["l"] = shapely.length(shapely.intersection(pu.geometry.to_numpy(), hexg.reindex(pu.h3_id).to_numpy())) / 1000
    km = pu.groupby("h3_id").l.sum()
    povr = polja.set_index("h3_id").area / 1e6
    rez["ulice_km_km2"] = (km.reindex(rez.h3_id).fillna(0).to_numpy() / povr.reindex(rez.h3_id).to_numpy()).round(1)
    rask = gpd.GeoSeries(gpd.points_from_xy(*xy[stepen >= 3].T), crs=CRS_M)
    jr = gpd.sjoin(gpd.GeoDataFrame(geometry=rask), polja[["h3_id", "geometry"]], predicate="within")
    rez["raskrsnice_km2"] = (jr.h3_id.value_counts().reindex(rez.h3_id).fillna(0).to_numpy()
                             / povr.reindex(rez.h3_id).to_numpy()).round(0).astype(int)

    # atraktivnost: percentilni rang među naseljenim poljima
    nas = polja.stanovnici.to_numpy() > 0
    skor = np.zeros(len(rez))
    for k, w in TEZINE.items():
        v = rez[k].astype(float)
        if k in MANJE_JE_BOLJE:
            v = -v
        rang = v[nas].rank(pct=True)
        r = np.zeros(len(rez))
        r[nas] = rang.to_numpy()
        r[~nas] = v[~nas].apply(lambda x: (v[nas] <= x).mean()).to_numpy()
        rez[f"rang_{k}"] = (r * 100).round(0).astype(int)
        skor += w * r
    rez["atraktivnost"] = (skor * 100).round(0).astype(int)

    out = polja[["h3_id", "opcina", "mz", "stanovnici", "geometry"]].merge(rez, on="h3_id")
    out.to_file(OUT / "dostupnost_h3.gpkg", driver="GPKG")
    out.drop(columns="geometry").to_csv(OUT / "dostupnost_h3.csv", index=False)
    print("\nNaseljena polja, medijan:")
    print(out[nas][["pjesice_10", "auto_10", "poi_10min", "stanica_m", "stanice_400m",
                    "glavna_cesta_m", "ulice_km_km2", "raskrsnice_km2", "atraktivnost"]].median().to_string())
    print("\nNajatraktivnija polja:")
    print(out.sort_values("atraktivnost", ascending=False)[["opcina", "mz", "stanovnici", "pjesice_10",
          "auto_10", "poi_10min", "stanica_m", "atraktivnost"]].head(10).to_string(index=False))


if __name__ == "__main__":
    main()
