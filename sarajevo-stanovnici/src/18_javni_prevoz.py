"""Javni prevoz: linije, frekvencija i dostupnost (PTAL) po H3 polju.

Ulaz:  raw/Sarajewo.osm.gz (OSM rute tramvaja, trolejbusa i autobusa, stanice, mreža),
       data/linije_frekvencija.csv (polasci na sat po liniji; pravi se s pretpostavkama ako ne postoji),
       out/polja_h3.gpkg
Izlaz: out/prevoz_h3.csv   PTAL indeks (AI) i razred, linije u dosegu, polasci na sat, najbliža stanica
       out/linije.geojson  trase linija (oba smjera spojena) s frekvencijom

Metoda: PTAL (Public Transport Accessibility Level, Transport for London, 2010):
  - stanice u dosegu pješice: autobus/trolejbus ≤ 8 min, tramvaj ≤ 12 min (hod uz nagib, Tobler, kao 08)
  - za svaku liniju samo najpristupačnija stanica; čekanje = 0,5 × interval + pouzdanost
    (2 min autobus/trolejbus, 0,75 min tramvaj)
  - EDF = 30 / (hod + čekanje); po vrsti prevoza AI = najbolji EDF + 0,5 × zbir ostalih
  - razredi: 0, 1a ≤ 2,5, 1b ≤ 5, 2 ≤ 10, 3 ≤ 15, 4 ≤ 20, 5 ≤ 25, 6a ≤ 40, 6b > 40

Ako postoje data/jpks_*.csv (27_javniprevozks.py, portal Ministarstva saobraćaja KS), koriste se
stvarne stanice i polasci (7–9 h radnim danom, jači smjer) za svih 117 linija, i ne treba
"nepoznata" linija. Inače:
Frekvencija: GTFS za Sarajevo ne postoji (Mobility Database), a stranica GRAS-a ne dozvoljava
automatski pristup. Zato su polasci u data/linije_frekvencija.csv pretpostavke po vrsti linije
(kolona izvor = "pretpostavka") dok se ne upišu stvarni podaci iz voznog reda.
OSM sadrži sve tramvajske i trolejbuske linije, ali samo dio autobuskih: stanice kroz koje ne
prolazi nijedna OSM linija računaju se kao jedna nepoznata autobuska linija (2 polaska na sat).
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
from shapely.geometry import LineString, MultiLineString
from shapely.ops import linemerge

from common import CRS_M, CRS_WGS, DATA, OUT, RAW

_s = importlib.util.spec_from_file_location("dost", Path(__file__).with_name("08_dostupnost.py"))
dost = importlib.util.module_from_spec(_s)
_s.loader.exec_module(dost)

DOSEG_MIN = {"tram": 12.0, "trolleybus": 8.0, "bus": 8.0}
POUZDANOST = {"tram": 0.75, "trolleybus": 2.0, "bus": 2.0}
NEPOZNATA_F = 2.0
JP_MOD = {"tramvaj": "tram", "trolejbus": "trolleybus", "autobus": "bus", "minibus": "bus"}
RAZREDI = [(0, "0"), (2.5, "1a"), (5, "1b"), (10, "2"), (15, "3"), (20, "4"), (25, "5"), (40, "6a"), (1e9, "6b")]

# pretpostavljeni polasci na sat u vršnom periodu, po smjeru (zamijeniti stvarnim voznim redom)
PRETPOSTAVKA = {("tram", "3"): 10, ("tram", "*"): 5, ("trolleybus", "103"): 6, ("trolleybus", "107"): 6,
                ("trolleybus", "*"): 4, ("bus", "31E"): 4, ("bus", "200E"): 2, ("bus", "*"): 3}


def ucitaj_rute(xml_gz):
    nodes, ways, rels = {}, {}, []
    stop_nodes = {}
    with gzip.open(xml_gz, "rb") as f:
        for _, el in ET.iterparse(f):
            if el.tag == "node":
                nodes[int(el.get("id"))] = (float(el.get("lon")), float(el.get("lat")))
                el.clear()
            elif el.tag == "way":
                ways[int(el.get("id"))] = [int(n.get("ref")) for n in el.findall("nd")]
                el.clear()
            elif el.tag == "relation":
                t = {c.get("k"): c.get("v") for c in el.findall("tag")}
                if t.get("type") == "route" and t.get("route") in ("bus", "tram", "trolleybus", "minibus"):
                    ref = t.get("ref", "")
                    if not ref or re.match(r"^[A-Z]{1,2}\d{3,}", ref) or "flixbus" in t.get("name", "").lower():
                        el.clear()
                        continue
                    mem = [(m.get("type"), int(m.get("ref")), m.get("role") or "") for m in el.findall("member")]
                    rels.append({"mod": "bus" if t["route"] == "minibus" else t["route"], "ref": ref,
                                 "ime": t.get("name", ""), "mem": mem})
                el.clear()
    out = []
    for r in rels:
        linije = [LineString([nodes[n] for n in ways[w] if n in nodes]) for typ, w, role in r["mem"]
                  if typ == "way" and role in ("", "forward", "backward") and w in ways
                  and sum(n in nodes for n in ways[w]) >= 2]
        stanice = [nodes[n] for typ, n, role in r["mem"] if typ == "node" and n in nodes
                   and (role.startswith("stop") or role.startswith("platform"))]
        if linije:
            out.append({**r, "geom": linemerge(MultiLineString(linije)), "stanice": stanice})
    return out


def main() -> None:
    rute = ucitaj_rute(RAW / "Sarajewo.osm.gz")
    lin = pd.DataFrame([(r["mod"], r["ref"]) for r in rute], columns=["mod", "linija"]).drop_duplicates()
    fp = DATA / "linije_frekvencija.csv"
    if fp.exists():
        fr = pd.read_csv(fp, dtype={"linija": str})
    else:
        fr = lin.assign(polazaka_na_sat=[PRETPOSTAVKA.get((m, l), PRETPOSTAVKA[(m, "*")]) for m, l in lin.values],
                        izvor="pretpostavka").sort_values(["mod", "linija"])
        fr.to_csv(fp, index=False)
        print(f"Napravljeno {fp.name} s pretpostavljenim frekvencijama ({len(fr)} linija) — upisati stvarne.")
    f_map = {(m, l): f for m, l, f in zip(fr["mod"], fr.linija, fr.polazaka_na_sat)}

    # stvarne linije, stanice i polasci s portala Ministarstva (27_javniprevozks.py), ako postoje
    jp = (DATA / "jpks_linije.csv").exists()
    nodes, ways, stops = dost.ucitaj_mrezu(RAW / "Sarajewo.osm.gz")
    if jp:
        jl = pd.read_csv(DATA / "jpks_linije.csv", dtype={"linija": str})
        js = pd.read_csv(DATA / "jpks_stanice.csv")
        jl["mod"] = jl.vrsta.map(JP_MOD)
        jl["lin"] = jl.linija.str.lower().str.replace(r"\s.*$", "", regex=True)
        # polasci na sat u vršnom periodu (7–9 h), jači smjer; ako ih nema, prosjek dnevnih (16 h)
        jf = jl.groupby(["mod", "lin"]).apply(lambda g: max(g.vrsni_sat_7_9.max(), g.polazaka_radni.max() / 16),
                                              include_groups=False)
        jf = jf[jf > 0]
        f_map = {k: float(v) for k, v in jf.items()}
        stops = [(r.lon, r.lat, "jpks", r.naziv) for r in js.itertuples()]
        print(f"Portal: {jf.size} linija s polascima, {len(js)} stanica")
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
    s["g"] = grupa
    st = s.groupby("g").agg(x=("geometry", lambda g: g.x.mean()), y=("geometry", lambda g: g.y.mean()),
                            ime=("ime", lambda v: next((x for x in v if x), "")))
    gxy = st[["x", "y"]].to_numpy()
    tst = cKDTree(gxy)

    # linije -> stanice (OSM članovi stop/platform; bez njih: stanice ≤ 25 m od trase)
    sluzi = {}  # (mod, linija) -> set indeksa stanica
    if jp:
        # stanice portala: kolona linije ("vrsta:kod ...") određuje koje linije staju na stanici
        gidx = dict(zip(range(len(s)), s.g))
        red = {g: k for k, g in enumerate(st.index)}
        for i, r in enumerate(js.itertuples()):
            for v, kod in re.findall(r"(minibus|autobus|trolejbus|tramvaj):(\S+)", str(r.linije)):
                key = (JP_MOD[v], kod.lower())
                if key in f_map:
                    sluzi.setdefault(key, set()).add(red[gidx[i]])
    rows = []
    for r in rute:
        key = (r["mod"], r["ref"])
        g = gpd.GeoSeries([r["geom"]], crs=CRS_WGS).to_crs(CRS_M).iloc[0]
        if r["stanice"]:
            p = gpd.GeoSeries(gpd.points_from_xy(*zip(*r["stanice"])), crs=CRS_WGS).to_crs(CRS_M)
            d, i = tst.query(np.c_[p.x, p.y])
            idx = set(i[d <= 50])
        else:
            near = tst.query_ball_point(np.c_[np.array(g.interpolate(np.arange(0, g.length, 20)).x) if False else
                                              [pt.x for pt in [g.interpolate(x) for x in np.arange(0, g.length, 20)]],
                                              [pt.y for pt in [g.interpolate(x) for x in np.arange(0, g.length, 20)]]], 25)
            idx = set(k for lst in near for k in lst)
        if not jp:
            sluzi.setdefault(key, set()).update(idx)
        rows.append({"mod": r["mod"], "linija": r["ref"], "ime": r["ime"], "geometry": r["geom"]})
    gl = gpd.GeoDataFrame(rows, crs=CRS_WGS)
    gl = gl.dissolve(by=["mod", "linija"], aggfunc={"ime": "first"}).reset_index()
    gl["polazaka_na_sat"] = [f_map.get((m, str(l).lower()), np.nan) for m, l in zip(gl["mod"], gl.linija)]
    gl["stanica"] = [len(sluzi.get((m, str(l).lower()), ())) for m, l in zip(gl["mod"], gl.linija)]
    gl.to_file(OUT / "linije.geojson", driver="GeoJSON")
    pokrivene = set().union(*sluzi.values()) if sluzi else set()
    nepoznate = [] if jp else [k for k in range(len(st)) if k not in pokrivene]
    print(f"Linija: {len(gl)} ({gl['mod'].value_counts().to_dict()}); stanica {len(st)}, "
          f"od toga bez OSM linije: {len(nepoznate)}")

    # vrijeme hoda od polja do stanica (obrnuti pješački graf, nagib)
    used = sorted({n for _, nds in ways for n in nds if n in nodes})
    idx = {n: k for k, n in enumerate(used)}
    pts = gpd.GeoSeries(gpd.points_from_xy(*zip(*[nodes[n] for n in used])), crs=CRS_WGS).to_crs(CRS_M)
    xy = np.c_[pts.x, pts.y]
    ll = np.array([nodes[n] for n in used])
    G = dost.graf(nodes, ways, xy, idx, "pjesice", visine=dost.visine_cvorova(ll[:, 0], ll[:, 1]))
    _, lab = connected_components(G, directed=True, connection="weak")
    ok = np.where(lab == np.bincount(lab).argmax())[0]
    tree = cKDTree(xy[ok])
    polja = gpd.read_file(OUT / "polja_h3.gpkg")
    cen = polja.geometry.centroid
    dc, ic = tree.query(np.c_[cen.x, cen.y])
    cvor_polja = ok[ic]
    ds, is_ = tree.query(gxy)
    cvor_st = ok[is_]
    hod = lambda d: d / 1000 / dost.PJESACKA_BRZINA * 60  # noqa: E731
    GT = G.T.tocsr()
    lim = max(DOSEG_MIN.values())
    Tst = np.full((len(st), len(polja)), np.inf, dtype=np.float32)
    for b in range(0, len(st), 40):
        D = dijkstra(GT, indices=cvor_st[b:b + 40], limit=lim)
        Tst[b:b + 40] = D[:, cvor_polja] + hod(dc)[None, :] + hod(ds[b:b + 40])[:, None]

    # PTAL
    if jp:
        linije = [(m, l, f, sorted(sluzi[(m, l)])) for (m, l), f in f_map.items() if sluzi.get((m, l))]
    else:
        linije = [(m, l, f_map.get((m, l), np.nan), sorted(sluzi.get((m, l), ()))) for m, l in gl[["mod", "linija"]].values]
        linije = [x for x in linije if x[3] and not np.isnan(x[2])]
        linije.append(("bus", "?", NEPOZNATA_F, nepoznate))
    edf = {m: [] for m in DOSEG_MIN}
    u_dosegu = [[] for _ in range(len(polja))]
    polasci = np.zeros(len(polja))
    for m, l, f, sts in linije:
        hodm = Tst[sts].min(axis=0)
        ok_ = hodm <= DOSEG_MIN[m]
        tat = hodm + 0.5 * 60 / f + POUZDANOST[m]
        e = np.where(ok_, 30 / tat, 0.0)
        edf[m].append(e)
        polasci += np.where(ok_, f, 0)
        for i in np.where(ok_)[0]:
            u_dosegu[i].append(l if l != "?" else "bus")
    ai = np.zeros(len(polja))
    for m, lst in edf.items():
        if not lst:
            continue
        E = np.vstack(lst)
        best = E.max(axis=0)
        ai += best + 0.5 * (E.sum(axis=0) - best)
    razred = [next(r for lim_, r in RAZREDI if a <= lim_) if a > 0 else "0" for a in ai]
    rez = pd.DataFrame({
        "h3_id": polja.h3_id, "ptal_ai": ai.round(1), "ptal": razred,
        "linije": [" ".join(sorted(set(x), key=lambda v: (len(v), v))) for x in u_dosegu],
        "broj_linija": [len(set(x) - {"bus"}) for x in u_dosegu],
        "polazaka_na_sat": polasci.round(0).astype(int),
        "stanica_min": np.round(np.minimum(Tst.min(axis=0), 99), 1),
    })
    rez.to_csv(OUT / "prevoz_h3.csv", index=False)

    j = rez.merge(polja[["h3_id", "opcina", "mz", "stanovnici"]], on="h3_id")
    nas = j[j.stanovnici > 0]
    w = nas.stanovnici
    print("\nStanovnici po PTAL razredu: " + ", ".join(
        f"{r}: {w[nas.ptal == r].sum():,.0f}" for r in ["0", "1a", "1b", "2", "3", "4", "5", "6a", "6b"]))
    mz = nas.dropna(subset=["mz"]).groupby(["opcina", "mz"]).apply(
        lambda g: pd.Series({"st": g.stanovnici.sum(), "ai": np.average(g.ptal_ai, weights=g.stanovnici),
                             "polazaka": np.average(g.polazaka_na_sat, weights=g.stanovnici)}), include_groups=False)
    mz = mz[mz.st >= 500]
    print("\nNajbolji javni prevoz (MZ):")
    print(mz.sort_values("ai", ascending=False).round(1).head(8).to_string())
    print("\nNajslabiji:")
    print(mz.sort_values("ai").round(1).head(8).to_string())


if __name__ == "__main__":
    main()
