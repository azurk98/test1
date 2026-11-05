"""Kvalitet života po H3 polju: pješačka dostupnost svakodnevnih sadržaja.

Ulaz:  raw/Sarajewo.osm.gz (mreža, sadržaji, parkovi), out/polja_h3.gpkg,
       out/supermarket_trgovine.csv (09), out/putevi.geojson (11), out/teren_h3.csv (10),
       interim/landuse.gpkg (02)
Izlaz: out/kvalitet_zivota_h3.csv  minute hoda do najbližeg sadržaja po kategoriji, bodovi, indeks
       out/sadrzaji.geojson        lokacije sadržaja (OSM) za kartu

Vrijeme hoda: OSM mreža ulica i staza, nagib po Toblerovoj formuli (kao 08), od polja
do najbližeg sadržaja svake kategorije. Bodovi po kategoriji: 1 / (1 + (t / t50)²), gdje je
t50 vrijeme na kojem sadržaj vrijedi pola (npr. škola 12 min). Indeks 0–100 je ponderisani
zbir bodova (KATEGORIJE) umanjen za buku uz autoput/magistralu/primarnu cestu, industriju
u polju, vrlo strm teren i težak pristup autom (uske i strme ulice, 15_ulice.py; pokrenuti
prije ovog koraka). Ponderi i pragovi su procjena, ne kalibracija; mijenjaju se ovdje.
Sadržaji izvan šest općina (Hadžići, Ilijaš, Istočno Sarajevo...) se računaju, jer ih stanovnici koriste.
"""
from __future__ import annotations

import gzip
import importlib.util
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
from scipy.sparse.csgraph import connected_components, dijkstra
from scipy.spatial import cKDTree
from shapely.geometry import Point, Polygon

from common import OSM_IME
from common import CRS_M, CRS_WGS, INTERIM, OUT, RAW
from common import _rel_geom

_s = importlib.util.spec_from_file_location("dost", Path(__file__).with_name("08_dostupnost.py"))
dost = importlib.util.module_from_spec(_s)
_s.loader.exec_module(dost)

# kategorija: (t50 u minutama, ponder, opis)
KATEGORIJE = {
    "trgovina": (8, 0.15, "trgovina namirnica"),
    "stanica": (5, 0.15, "stanica javnog prevoza"),
    "osnovna_skola": (12, 0.15, "osnovna škola"),
    "ambulanta": (12, 0.12, "ambulanta, dom zdravlja, poliklinika"),
    "park": (8, 0.12, "park"),
    "vrtic": (10, 0.08, "vrtić"),
    "apoteka": (8, 0.07, "apoteka"),
    "igraliste": (8, 0.06, "dječije igralište"),
    "bolnica": (25, 0.05, "bolnica"),
    "sport": (12, 0.05, "sportski teren ili centar"),
}
KAZNA_BUKA = {75: 10, 150: 5}       # m od autoputa/magistrale/primarne ceste -> oduzeti bodovi
KAZNA_INDUSTRIJA = (0.25, 10)       # udio industrijskog zemljišta u polju > 25% -> -10
KAZNA_STRMO = (20, 5)               # srednji nagib polja > 20% -> -5
KAZNA_PRISTUP = 0.15                # (100 - ocjena pristupa autom iz 15_ulice.py) × 0,15 -> do -15
MAX_MIN = 60

NIJE_OSNOVNA = re.compile(r"(srednj|gimnaz|tehni[cč]k|medicinsk|ekonomsk|škola za|jezi|keramik|français|umjetni|"
                          r"institut|centar za|crveni kri|muzi[cč]k|baletsk|fakultet|univerzit)", re.I)


def kategorija(t: dict) -> str | None:
    a, h, l = t.get("amenity"), t.get("healthcare"), t.get("leisure")
    if a == "hospital" or h == "hospital":
        return "bolnica"
    if a in ("clinic", "doctors") or h in ("clinic", "doctor", "centre"):
        return "ambulanta"
    if a == "pharmacy" or h == "pharmacy":
        return "apoteka"
    if a == "kindergarten":
        return "vrtic"
    if a == "school":
        ime = t.get("name", "")
        return None if (not ime or NIJE_OSNOVNA.search(ime)) else "osnovna_skola"
    if l == "park":
        return "park"
    if l == "playground":
        return "igraliste"
    if l in ("sports_centre", "pitch", "fitness_centre"):
        return "sport"
    return None


def sadrzaji(xml_gz) -> gpd.GeoDataFrame:
    nodes, ways_xy, rows = {}, {}, []
    with gzip.open(xml_gz, "rb") as f:
        for _, el in ET.iterparse(f):
            if el.tag == "node":
                lon, lat = float(el.get("lon")), float(el.get("lat"))
                nodes[int(el.get("id"))] = (lon, lat)
                t = {c.get("k"): c.get("v") for c in el.findall("tag")}
                k = kategorija(t) if t else None
                if k:
                    rows.append({"kategorija": k, "ime": t.get("name", ""), "geometry": Point(lon, lat)})
                el.clear()
            elif el.tag == "way":
                t = {c.get("k"): c.get("v") for c in el.findall("tag")}
                pts = [nodes[int(n.get("ref"))] for n in el.findall("nd") if int(n.get("ref")) in nodes]
                ways_xy[int(el.get("id"))] = pts
                k = kategorija(t)
                if k and len(pts) >= 4 and pts[0] == pts[-1]:
                    rows.append({"kategorija": k, "ime": t.get("name", ""), "geometry": Polygon(pts)})
                el.clear()
            elif el.tag == "relation":
                t = {c.get("k"): c.get("v") for c in el.findall("tag")}
                k = kategorija(t)
                if k:
                    mem = [{"type": "way", "role": m.get("role") or "",
                            "geometry": [{"lon": x, "lat": y} for x, y in ways_xy.get(int(m.get("ref")), [])]}
                           for m in el.findall("member") if m.get("type") == "way"]
                    g = _rel_geom({"members": mem})
                    if g is not None:
                        rows.append({"kategorija": k, "ime": t.get("name", ""), "geometry": g})
                el.clear()
    g = gpd.GeoDataFrame(rows, crs=CRS_WGS).to_crs(CRS_M)
    g = g[g.is_valid & ~g.is_empty]
    # isti objekat kao tačka i kao poligon: zadrži poligon
    return g.reset_index(drop=True)


def pristupne_tacke(g: gpd.GeoDataFrame) -> pd.DataFrame:
    """Tačke iz kojih se sadržaj doseže: tačka; za parkove rub svakih 40 m; za ostale poligone tačka unutar."""
    rows = []
    for k, geom in zip(g.kategorija, g.geometry):
        if geom.geom_type == "Point":
            rows.append((k, geom.x, geom.y))
        elif k == "park":
            if geom.area < 1000:
                continue
            ring = geom.exterior if geom.geom_type == "Polygon" else max(geom.geoms, key=lambda p: p.area).exterior
            n = max(int(ring.length // 40), 4)
            for d in np.linspace(0, ring.length, n, endpoint=False):
                p = ring.interpolate(d)
                rows.append((k, p.x, p.y))
        else:
            p = geom.representative_point()
            rows.append((k, p.x, p.y))
    return pd.DataFrame(rows, columns=["kategorija", "x", "y"])


def main() -> None:
    polja = gpd.read_file(OUT / "polja_h3.gpkg")
    nodes, ways, stops = dost.ucitaj_mrezu(RAW / OSM_IME)
    used = sorted({n for _, nds in ways for n in nds if n in nodes})
    idx = {n: k for k, n in enumerate(used)}
    pts = gpd.GeoSeries(gpd.points_from_xy(*zip(*[nodes[n] for n in used])), crs=CRS_WGS).to_crs(CRS_M)
    xy = np.c_[pts.x, pts.y]
    ll = np.array([nodes[n] for n in used])
    G = dost.graf(nodes, ways, xy, idx, "pjesice", visine=dost.visine_cvorova(ll[:, 0], ll[:, 1]))
    _, lab = connected_components(G, directed=True, connection="weak")
    ok = np.where(lab == np.bincount(lab).argmax())[0]
    tree = cKDTree(xy[ok])
    hod = lambda d: d / 1000 / dost.PJESACKA_BRZINA * 60  # noqa: E731

    s = sadrzaji(RAW / OSM_IME)
    print("Sadržaji (OSM):", s.kategorija.value_counts().to_dict())
    tacke = pristupne_tacke(s)
    # trgovine namirnica iz 09 (OSM + Overture, i Google ako je svjež) i stanice javnog prevoza
    tr = pd.read_csv(OUT / "supermarket_trgovine.csv")
    tr = gpd.GeoDataFrame(tr, geometry=gpd.points_from_xy(tr.lon, tr.lat), crs=CRS_WGS).to_crs(CRS_M)
    st = gpd.GeoSeries(gpd.points_from_xy([a[0] for a in stops], [a[1] for a in stops]), crs=CRS_WGS).to_crs(CRS_M)
    tacke = pd.concat([tacke,
                       pd.DataFrame({"kategorija": "trgovina", "x": tr.geometry.x, "y": tr.geometry.y}),
                       pd.DataFrame({"kategorija": "stanica", "x": st.x, "y": st.y})], ignore_index=True)

    cen = polja.geometry.centroid
    dc, ic = tree.query(np.c_[cen.x, cen.y])
    cvor_polja = ok[ic]
    GT = G.T.tocsr()  # vrijeme OD polja DO sadržaja = najkraći put u obrnutom grafu od sadržaja
    rez = pd.DataFrame({"h3_id": polja.h3_id})
    for k in KATEGORIJE:
        t = tacke[tacke.kategorija == k]
        if t.empty:
            rez[f"min_{k}"] = MAX_MIN
            continue
        dt, it = tree.query(np.c_[t.x, t.y])
        izvori = np.unique(ok[it][dt <= 150])
        D = dijkstra(GT, indices=izvori, min_only=True, limit=MAX_MIN)
        m = D[cvor_polja] + hod(dc)
        rez[f"min_{k}"] = np.round(np.minimum(m, MAX_MIN), 1)

    # bodovi i indeks
    skor = np.zeros(len(rez))
    for k, (t50, w, _) in KATEGORIJE.items():
        b = 1 / (1 + (rez[f"min_{k}"] / t50) ** 2)
        rez[f"bod_{k}"] = b.round(2)
        skor += w * b
    rez["indeks_bez_kazni"] = (skor * 100).round(1)

    pu = gpd.read_file(OUT / "putevi.geojson").to_crs(CRS_M)
    bucne = pu[pu.klasa.isin(["autoput", "magistrala", "primarna"])].union_all()
    d_buka = cen.distance(bucne).to_numpy()
    kazna = np.zeros(len(rez))
    for prag, b in sorted(KAZNA_BUKA.items(), reverse=True):
        kazna = np.where(d_buka <= prag, b, kazna)
    rez["buka_m"] = d_buka.round(0).astype(int)
    lu = gpd.read_file(INTERIM / "landuse.gpkg")
    ind = lu[lu.vrsta == "landuse=industrial"].union_all()
    udio_ind = polja.geometry.intersection(ind).area / polja.area
    rez["industrija_udio"] = udio_ind.round(2).to_numpy()
    kazna += np.where(udio_ind > KAZNA_INDUSTRIJA[0], KAZNA_INDUSTRIJA[1], 0)
    ter = pd.read_csv(OUT / "teren_h3.csv").set_index("h3_id").nagib_pct.reindex(rez.h3_id).fillna(0).to_numpy()
    kazna += np.where(ter > KAZNA_STRMO[0], KAZNA_STRMO[1], 0)
    up = OUT / "ulice_h3.csv"
    if up.exists():
        pr = pd.read_csv(up).set_index("h3_id").ocjena_pristupa.reindex(rez.h3_id).fillna(100).to_numpy()
        rez["ocjena_pristupa"] = pr.astype(int)
        kazna += (100 - pr) * KAZNA_PRISTUP
    rez["kazne"] = kazna.round(1)
    rez["indeks"] = np.clip(rez.indeks_bez_kazni - kazna, 0, 100).round(0).astype(int)
    rez.to_csv(OUT / "kvalitet_zivota_h3.csv", index=False)

    out = s.copy()
    out["geometry"] = out.geometry.representative_point()
    out.to_crs(CRS_WGS).to_file(OUT / "sadrzaji.geojson", driver="GeoJSON")

    j = rez.merge(polja[["h3_id", "opcina", "mz", "stanovnici"]], on="h3_id")
    nas = j[j.stanovnici > 0]
    w = nas.stanovnici
    print("\nMedijan minuta (naseljena polja, ponderisano stanovnicima):")
    for k in KATEGORIJE:
        v = nas[f"min_{k}"].to_numpy()
        o = np.argsort(v)
        c = np.cumsum(w.to_numpy()[o])
        print(f"  {k:14s} {v[o][np.searchsorted(c, c[-1] / 2)]:5.1f} min;  "
              f"> 15 min: {w[nas[f'min_{k}'] > 15].sum():,.0f} stanovnika")
    print("\nIndeks po općini (prosjek po stanovniku):")
    print(nas.groupby("opcina").apply(lambda g: np.average(g.indeks, weights=g.stanovnici), include_groups=False)
          .round(0).to_string())
    print("\nNajbolja naseljena polja:")
    print(nas.sort_values("indeks", ascending=False)[["opcina", "mz", "stanovnici", "indeks"]].head(8).to_string(index=False))
    print("\nNajbolje MZ (prosjek po stanovniku, MZ s ≥ 1000 st.):")
    mz = nas.dropna(subset=["mz"]).groupby(["opcina", "mz"]).apply(
        lambda g: pd.Series({"st": g.stanovnici.sum(), "indeks": np.average(g.indeks, weights=g.stanovnici)}),
        include_groups=False)
    print(mz[mz.st >= 1000].sort_values("indeks", ascending=False).round(0).head(10).to_string())
    print(mz[mz.st >= 1000].sort_values("indeks").round(0).head(5).to_string())


if __name__ == "__main__":
    main()
