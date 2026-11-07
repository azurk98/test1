"""Dopuna za Ilidžu i Vogošću: granice, MZ i OSM objekti izvan okvira BBBike ekstrakta.

BBBike ekstrakt (raw/Sarajewo.osm.gz) pokriva 18,242–18,515 E, 43,768–43,935 N, pa mu nedostaju
sjever Vogošće i zapad i jug Ilidže. Overpass i Geofabrik nisu dostupni iz okruženja, pa se ti
dijelovi dopunjuju iz Overture Maps (izdanje u raw/overture/*.state), koji za zgrade i ceste
prenosi OSM podatke s istim vrstama (class = OSM building/highway).

Ulaz:  raw/Sarajewo.osm.gz, raw/overture/{building,segment,land_use,water,division_area,division}.parquet,
       raw/overture_places.parquet
Izlaz: raw/Sarajewo_sire.osm.gz  ekstrakt + dopuna (negativni id-jevi), isti XML oblik, pa ga ostali
                                 koraci čitaju kao i prije (common.OSM_IME)
       raw/osm_grad.json        ponovo iz proširenog ekstrakta (zgrade, POI, namjena zemljišta)
       raw/granice_dopuna.gpkg  općine Ilidža i Vogošća (OSM relacije 2528207, 2528291 preko Overture)
                                 i njihove MZ: Vogošća 21 OSM poligon (cijela općina); Ilidža 15 OSM
                                 poligona (38% površine, uglavnom ruralno), ostatak podijeljen oko
                                 Overture naziva naselja (Stup, Otes, Hrasnica ...; Voronoi, približno)
Pravila dopune:
  - samo objekti čija je reprezentativna tačka izvan okvira ekstrakta, a do 2 km od Ilidže/Vogošće
  - zgrade samo iz OSM izvora (Microsoft ML zgrade bi promijenile metodu u odnosu na ostale općine)
  - čvor ceste koji se poklapa (≤ 2 m) s čvorom iz ekstrakta dobija njegov id, pa je mreža povezana
  - mjesta (Overture places) samo kao opšti POI i sadržaji iz 14 (škola, vrtić, ambulanta ...);
    trgovine, autopraonice i restorani se i dalje uzimaju iz Overture direktno (09, 19, 20)
"""
from __future__ import annotations

import gzip
from xml.sax.saxutils import quoteattr

import geopandas as gpd
import numpy as np
import pandas as pd
from scipy.spatial import cKDTree
from shapely.geometry import MultiPoint, box
from shapely.ops import voronoi_diagram

from common import CRS_M, CRS_WGS, RAW
from osm_xml import konvertuj

OV = RAW / "overture"
OKVIR = (18.242, 43.768, 18.515, 43.935)
NOVE = {"Ilidža": "r2528207", "Vogošća": "r2528291"}
ILIDZA_NASELJA = ("locality", "macrohood", "neighborhood")
HIGHWAY_OK = {"motorway", "trunk", "primary", "secondary", "tertiary", "unclassified", "residential",
              "living_street", "service", "pedestrian", "track", "footway", "path", "steps", "cycleway",
              "bridleway"}
LANDUSE = {("developed", "commercial"): {"landuse": "commercial"}, ("developed", "industrial"): {"landuse": "industrial"},
           ("developed", "retail"): {"landuse": "retail"}, ("developed", "brownfield"): {"landuse": "brownfield"},
           ("construction", "construction"): {"landuse": "construction"}, ("residential", "residential"): {"landuse": "residential"},
           ("agriculture", "farmland"): {"landuse": "farmland"}, ("agriculture", "meadow"): {"landuse": "meadow"},
           ("cemetery", "cemetery"): {"landuse": "cemetery"}, ("park", "park"): {"leisure": "park"},
           ("recreation", "pitch"): {"leisure": "pitch"}, ("recreation", "playground"): {"leisure": "playground"},
           ("recreation", "stadium"): {"leisure": "sports_centre"}, ("education", "school"): {"amenity": "school"},
           ("education", "kindergarten"): {"amenity": "kindergarten"}, ("medical", "hospital"): {"amenity": "hospital"},
           ("medical", "clinic"): {"amenity": "clinic"}, ("resource_extraction", "quarry"): {"landuse": "quarry"}}
MJESTA = {"elementary_school": {"amenity": "school"}, "preschool": {"amenity": "kindergarten"},
          "kindergarten": {"amenity": "kindergarten"}, "hospital": {"amenity": "hospital"},
          "health_care": {"amenity": "clinic"}, "medical_center": {"amenity": "clinic"},
          "doctor": {"amenity": "doctors"}, "dental_clinic": {"amenity": "dentist"},
          "pharmacy_and_drug_store": {"amenity": "pharmacy"}, "pharmacy": {"amenity": "pharmacy"},
          "park": {"leisure": "park"}, "playground": {"leisure": "playground"},
          "gym": {"leisure": "fitness_centre"}, "sport_or_fitness_facility": {"leisure": "sports_centre"},
          "post_office": {"amenity": "post_office"}, "bank": {"amenity": "bank"}}


def ime(n):
    return (n or {}).get("primary") if isinstance(n, dict) else None


def izvor(s):
    return s[0]["record_id"].split("@")[0] if s is not None and len(s) else ""


def granice() -> gpd.GeoDataFrame:
    da = gpd.read_parquet(OV / "division_area.parquet").to_crs(CRS_M)
    da["src"] = da.sources.map(izvor)
    da["nm"] = da.names.map(ime)
    op = {k: da[da.src == v].geometry.union_all() for k, v in NOVE.items()}
    nb = da[da.subtype.isin(["neighborhood", "macrohood"])]
    rows = [{"vrsta": "opcina", "opcina": k, "mz": None, "izvor": f"OSM relacija {NOVE[k][1:]} (Overture)", "geometry": g}
            for k, g in op.items()]
    for k, g in op.items():
        m = nb[nb.intersection(g).area > 0.5 * nb.area]
        for r in m.itertuples():
            nm = r.nm.replace("MZ ", "").replace(" (FBiH)", "")
            rows.append({"vrsta": "mz", "opcina": k, "mz": nm, "izvor": f"OSM {r.src} (Overture)",
                         "geometry": r.geometry.intersection(g)})
        ostatak = g.difference(m.union_all()) if len(m) else g
        if ostatak.area < 1e5:
            continue
        # ostatak (gradski dio Ilidže): Voronoi oko naziva naselja koja nisu već MZ
        p = gpd.read_parquet(OV / "division.parquet").to_crs(CRS_M)
        p["nm"] = p.names.map(ime)
        vec = {x.lower() for x in m.nm.str.replace("MZ ", "")}
        p = p[p.subtype.isin(ILIDZA_NASELJA) & p.within(ostatak) & ~p.nm.str.lower().isin(vec)].drop_duplicates("nm")
        vor = gpd.GeoSeries(list(voronoi_diagram(MultiPoint(list(p.geometry)), envelope=g.envelope.buffer(5000)).geoms), crs=CRS_M)
        for c in vor:
            nm = p[p.within(c)].nm.iloc[0]
            gg = c.intersection(ostatak)
            if not gg.is_empty:
                rows.append({"vrsta": "mz", "opcina": k, "mz": nm, "izvor": "Voronoi oko naziva naselja (približno)", "geometry": gg})
    g = gpd.GeoDataFrame(rows, crs=CRS_M)
    # nazivi MZ moraju biti jedinstveni u svim općinama (npr. Vlakovo, Kobilja Glava postoje i drugdje)
    from common import DATA
    stari = set(pd.read_csv(DATA / "mz_lista.csv").mz)
    jm = g.vrsta == "mz"
    vise = g[jm].groupby("mz").opcina.nunique()
    dup = jm & (g.mz.isin(stari) | g.mz.map(vise).gt(1) | g[jm].duplicated("mz", keep=False).reindex(g.index, fill_value=False))
    g.loc[dup, "mz"] = g.mz[dup] + " (" + g.opcina[dup] + ")"
    g = g.dissolve(by=["vrsta", "opcina", "mz"], as_index=False, dropna=False, aggfunc="first") if g[jm].mz.duplicated().any() else g
    mz = g[g.vrsta == "mz"]
    for k in op:
        print(f"  {k}: {len(mz[mz.opcina == k])} MZ ({(mz[(mz.opcina == k) & mz.izvor.str.startswith('OSM')].area.sum() / op[k].area):.0%} iz OSM poligona)")
    return g


def main() -> None:
    print("Granice i MZ (Overture / OSM)")
    g = granice()
    g.to_crs(CRS_WGS).to_file(RAW / "granice_dopuna.gpkg", driver="GPKG")
    zona = g[g.vrsta == "opcina"].union_all().buffer(2000)
    okvir = gpd.GeoSeries([box(*OKVIR)], crs=CRS_WGS).to_crs(CRS_M).iloc[0]
    region = zona.difference(okvir)

    def unutra(gs: gpd.GeoSeries) -> np.ndarray:
        gm = gs.to_crs(CRS_M)
        rp = gm.representative_point() if (gm.geom_type != "Point").any() else gm
        return rp.within(region).to_numpy()

    # čvorovi ekstrakta (za spajanje mreže)
    print("Čvorovi ekstrakta ...")
    ids, ll = [], []
    with gzip.open(RAW / "Sarajewo.osm.gz", "rt", encoding="utf-8") as f:
        for line in f:
            s = line.lstrip()
            if s.startswith("<node"):
                a = s.split('id="', 1)[1]; i = int(a.split('"', 1)[0])
                lat = float(s.split('lat="', 1)[1].split('"', 1)[0]); lon = float(s.split('lon="', 1)[1].split('"', 1)[0])
                ids.append(i); ll.append((lon, lat))
            elif s.startswith("<way"):
                break
    ll = np.array(ll)
    kx = np.cos(np.radians(43.85)) * 111320
    stablo = cKDTree(np.c_[ll[:, 0] * kx, ll[:, 1] * 111320])
    nodes: dict[tuple, int] = {}
    novi_cvor: list[tuple[int, float, float, dict]] = []
    ways: list[tuple[list[int], dict]] = []
    nid = [-1]

    def cvor(lon, lat, tags=None, spoji=False):
        k = (round(lon, 7), round(lat, 7))
        if k in nodes and not tags:
            return nodes[k]
        if spoji:
            d, j = stablo.query((lon * kx, lat * 111320))
            if d <= 2:
                nodes[k] = ids[j]
                return ids[j]
        i = nid[0]; nid[0] -= 1
        novi_cvor.append((i, lat, lon, tags or {}))
        if not tags:
            nodes[k] = i
        return i

    def put(coords, tags, spoji=False):
        refs = [cvor(x, y, spoji=spoji) for x, y in coords]
        refs = [r for k, r in enumerate(refs) if k == 0 or r != refs[k - 1]]
        if len(refs) >= 2:
            ways.append((refs, tags))

    def prstenovi(geom):
        for p in getattr(geom, "geoms", [geom]):
            if p.geom_type == "Polygon":
                yield list(p.exterior.coords)

    # zgrade (samo OSM izvor)
    b = gpd.read_parquet(OV / "building.parquet").rename(columns={"class": "klasa"})
    b = b[b.sources.map(lambda s: s[0]["dataset"] == "OpenStreetMap")]
    b = b[unutra(b.geometry.set_crs(CRS_WGS, allow_override=True))]
    for r in b.itertuples():
        t = {"building": r.klasa if isinstance(r.klasa, str) else "yes", "source": "overture"}
        if pd.notna(r.num_floors):
            t["building:levels"] = str(int(r.num_floors))
        if pd.notna(r.height):
            t["height"] = f"{r.height:g}"
        for ring in prstenovi(r.geometry):
            put(ring, t)
    print(f"  zgrade: {len(b)}")

    # ceste i pruge
    s = gpd.read_parquet(OV / "segment.parquet").rename(columns={"class": "klasa"})
    s = s[s.subtype.isin(["road", "rail"]) & unutra(s.geometry.set_crs(CRS_WGS, allow_override=True))]
    n_c = 0
    for r in s.itertuples():
        t = {"source": "overture"}
        if r.subtype == "road":
            t["highway"] = r.klasa if r.klasa in HIGHWAY_OK else "road"
            if (r.road_flags is not None and len(r.road_flags)
                    and any("is_bridge" in (f.get("values") or []) for f in r.road_flags)):
                t["bridge"] = "yes"
            if r.access_restrictions is not None:
                for a in r.access_restrictions:
                    if a.get("access_type") == "denied" and (a.get("when") or {}).get("heading") == "backward":
                        t["oneway"] = "yes"
            if r.speed_limits is not None and len(r.speed_limits):
                mx = r.speed_limits[0].get("max_speed")
                if mx:
                    t["maxspeed"] = str(int(mx["value"]))
        else:
            t["railway"] = {"tram": "tram", "standard_gauge": "rail"}.get(r.klasa, r.klasa or "rail")
        nm = ime(r.names)
        if nm:
            t["name"] = nm
        put(list(r.geometry.coords), t, spoji=True)
        n_c += 1
    print(f"  ceste i pruge: {n_c}")

    # namjena zemljišta
    lu = gpd.read_parquet(OV / "land_use.parquet").rename(columns={"class": "klasa"})
    lu = lu[lu.geometry.geom_type.isin(["Polygon", "MultiPolygon"]) & unutra(lu.geometry.set_crs(CRS_WGS, allow_override=True))]
    n_l = 0
    for r in lu.itertuples():
        t = LANDUSE.get((r.subtype, r.klasa))
        if not t:
            continue
        for ring in prstenovi(r.geometry):
            put(ring, {**t, "source": "overture"}); n_l += 1
    print(f"  namjena zemljišta: {n_l}")

    # rijeke
    w = gpd.read_parquet(OV / "water.parquet")
    w = w[(w.subtype == "river") & (w.geometry.geom_type == "LineString") & unutra(w.geometry.set_crs(CRS_WGS, allow_override=True))]
    for r in w.itertuples():
        put(list(r.geometry.coords), {"waterway": "river", "name": ime(r.names) or "", "source": "overture"})
    print(f"  rijeke: {len(w)}")

    # mjesta: sadržaji i opšti POI
    p = gpd.read_parquet(RAW / "overture_places.parquet")
    p = p[unutra(p.geometry.set_crs(CRS_WGS, allow_override=True))]
    for r in p.itertuples():
        tax = r.taxonomy if r.taxonomy is not None else {}
        kat = tax.get("primary") or ""
        hij = list(tax.get("hierarchy") if tax.get("hierarchy") is not None else [])
        t = MJESTA.get(kat) or ({"shop": "yes"} if hij[:1] == ["shopping"] else {"office": "yes"} if hij else None)
        if t:
            cvor(r.geometry.x, r.geometry.y, {**t, "name": ime(r.names) or "", "source": "overture"})
    print(f"  mjesta: {len(p)}")

    # spajanje: čvorovi dopune prije prvog <way>, putevi dopune prije prve <relation>
    print("Pisanje raw/Sarajewo_sire.osm.gz ...")
    tg = lambda t: "".join(f"\n    <tag k={quoteattr(k)} v={quoteattr(str(v))}/>" for k, v in t.items() if v != "")
    wid = -1
    with gzip.open(RAW / "Sarajewo.osm.gz", "rt", encoding="utf-8") as f, \
            gzip.open(RAW / "Sarajewo_sire.osm.gz", "wt", encoding="utf-8", compresslevel=4) as o:
        n_ok = w_ok = False
        for line in f:
            s_ = line.lstrip()
            if not n_ok and s_.startswith("<way"):
                for i, lat, lon, t in novi_cvor:
                    o.write(f'  <node id="{i}" lat="{lat:.7f}" lon="{lon:.7f}"' + (f">{tg(t)}\n  </node>\n" if t else "/>\n"))
                n_ok = True
            if not w_ok and (s_.startswith("<relation") or s_.startswith("</osm")):
                for refs, t in ways:
                    o.write(f'  <way id="{wid}">' + "".join(f'\n    <nd ref="{r}"/>' for r in refs) + tg(t) + "\n  </way>\n")
                    wid -= 1
                w_ok = True
            if s_.startswith("<bounds"):
                line = '  <bounds minlat="43.72" minlon="18.13" maxlat="44.02" maxlon="18.515"/>\n'
            o.write(line)
    print(f"  dopuna: {len(novi_cvor)} čvorova, {len(ways)} puteva")
    print("raw/osm_grad.json iz proširenog ekstrakta ...")
    info = konvertuj(RAW / "Sarajewo_sire.osm.gz", set(), RAW / "granice_x.json", RAW / "osm_grad.json")
    (RAW / "granice_x.json").unlink(missing_ok=True)
    print(f"  {info}")


if __name__ == "__main__":
    main()
