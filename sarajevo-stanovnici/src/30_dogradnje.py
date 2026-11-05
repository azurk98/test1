"""Nove trase javnog prevoza uz male dogradnje: kratki novi spojevi između ulica (analiza, ne projekat).

Ideja: u brdima se dvije ulice (često slijepe) gotovo dodiruju, a cestom su udaljene kilometrima.
Kratka nova dionica (≤ MAX_SPOJ_M, nagib ≤ MAX_NAGIB) omogućava poprečnu liniju kroz naselja sa
slabim prevozom.

Kandidati: parovi čvorova ulica (residential i veće) u četiri općine, 60–MAX_SPOJ_M zračno, cestom
≥ 3× duže i ≥ 800 m, nagib spoja ≤ MAX_NAGIB (Copernicus, tlo), spoj ne siječe zgrade (± 3 m);
prelaz preko rijeke se označava (treba most). Ocjena: stanovnici do 400 m od spoja koji su danas
> 8 min hoda od stanice ili u PTAL ≤ 1b, puta ušteda puta (km, do 3). Za najbolje spojeve trasa
linije: najbliža stanica tramvaja/trolejbusa/autobusa s jedne strane → spoj → s druge strane.
Izlaz: out/dogradnje_spojevi.csv, out/dogradnje_linije.csv, out/dogradnje.geojson
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
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components, dijkstra
from scipy.spatial import cKDTree
from shapely.geometry import LineString, Point

from common import CRS_M, CRS_WGS, DATA, INTERIM, OUT, RAW, ucitaj_granice


def _uvezi(ime, fajl):
    s = importlib.util.spec_from_file_location(ime, Path(__file__).with_name(fajl))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


mp = _uvezi("mp", "24_putovanja.py")

MAX_SPOJ_M = 400
MIN_SPOJ_M = 60
MAX_NAGIB = 0.10
MIN_ZAOBILAZAK = 3.0
MIN_CESTOM_M = 800
N_SPOJEVA = 10
ULICE = {"residential", "unclassified", "tertiary", "secondary", "primary", "trunk", "living_street",
         "tertiary_link", "secondary_link", "primary_link"}


def rijeke():
    nodes, out = {}, []
    with gzip.open(RAW / "Sarajewo.osm.gz", "rb") as f:
        for _, el in ET.iterparse(f):
            if el.tag == "node":
                nodes[int(el.get("id"))] = (float(el.get("lon")), float(el.get("lat")))
                el.clear()
            elif el.tag == "way":
                t = {c.get("k"): c.get("v") for c in el.findall("tag")}
                if t.get("waterway") in ("river", "stream", "canal") or t.get("railway") == "rail":
                    p = [nodes[int(n.get("ref"))] for n in el.findall("nd") if int(n.get("ref")) in nodes]
                    if len(p) >= 2:
                        out.append({"vrsta": "pruga" if t.get("railway") else t["waterway"], "geometry": LineString(p)})
                el.clear()
            elif el.tag == "relation":
                el.clear()
    return gpd.GeoDataFrame(out, crs=CRS_WGS).to_crs(CRS_M)


def main() -> None:
    wmeta, xy, ll, e, idx = mp.mreza()
    n = len(xy)
    ehw = e.w.map(lambda k: wmeta[k]["hw"]).to_numpy()
    # neusmjereni graf dužina (m) samo po ulicama; vrijeme autom iz e.t0
    duz = np.hypot(*(xy[e.u] - xy[e.v]).T)
    m_ul = np.isin(ehw, list(ULICE))
    Gd = csr_matrix((np.r_[duz[m_ul], duz[m_ul]], (np.r_[e.u[m_ul], e.v[m_ul]], np.r_[e.v[m_ul], e.u[m_ul]])), shape=(n, n))
    _, lab = connected_components(Gd, directed=False)
    glavna = lab == np.bincount(lab).argmax()
    cv = np.zeros(n, bool); cv[e.u[m_ul]] = True; cv[e.v[m_ul]] = True
    cv &= glavna

    polja = gpd.read_file(OUT / "polja_h3.gpkg")
    pv = pd.read_csv(OUT / "prevoz_h3.csv", dtype={"ptal": str}).set_index("h3_id").reindex(polja.h3_id)
    pc = polja.geometry.centroid
    pcx = np.c_[pc.x, pc.y]
    slabo = ((pv.stanica_min.to_numpy() > 8) | pv.ptal.isin(["0", "1a", "1b"]).to_numpy()) & (polja.stanovnici.to_numpy() > 0)
    tp = cKDTree(pcx)
    st = polja.stanovnici.to_numpy()

    op, _ = ucitaj_granice()
    cetiri = op.to_crs(CRS_M).union_all()
    u4 = np.array([cetiri.contains(Point(p)) for p in xy]) if False else gpd.GeoSeries(gpd.points_from_xy(xy[:, 0], xy[:, 1]), crs=CRS_M).within(cetiri).to_numpy()
    # čvorovi s potražnjom: u 4 općine i do 400 m od slabo pokrivenih stanovnika
    sl_pts = cKDTree(pcx[slabo])
    blizu = np.array([len(x) > 0 for x in sl_pts.query_ball_point(xy, 400)])
    kand = np.where(cv & u4 & blizu)[0]
    print(f"Čvorova kandidata: {len(kand)}", flush=True)

    vis = mp.dost.visine_cvorova(ll[:, 0], ll[:, 1], tlo=True)
    tk = cKDTree(xy[kand])
    parovi = tk.query_pairs(MAX_SPOJ_M, output_type="ndarray")
    a, b = kand[parovi[:, 0]], kand[parovi[:, 1]]
    L = np.hypot(*(xy[a] - xy[b]).T)
    ok = (L >= MIN_SPOJ_M) & (np.abs(vis[a] - vis[b]) / np.maximum(L, 1) <= MAX_NAGIB)
    a, b, L = a[ok], b[ok], L[ok]
    print(f"Parova do {MAX_SPOJ_M} m s nagibom ≤ {MAX_NAGIB:.0%}: {len(a):,}", flush=True)
    # mrežna udaljenost: dijkstra iz jedinstvenih krajeva, s limitom
    izv = np.unique(a)
    pos = {k: i for i, k in enumerate(izv)}
    D = np.empty(len(a))
    for s0 in range(0, len(izv), 200):
        blok = izv[s0:s0 + 200]
        Db = dijkstra(Gd, indices=blok, limit=6000)
        for k in range(len(blok)):
            sel = np.where(a == blok[k])[0]
            D[sel] = Db[k, b[sel]]
    D[~np.isfinite(D)] = 6000
    ok = (D >= MIN_ZAOBILAZAK * L) & (D >= MIN_CESTOM_M)
    a, b, L, D = a[ok], b[ok], L[ok], D[ok]
    print(f"Sa zaobilaskom ≥ {MIN_ZAOBILAZAK}× i ≥ {MIN_CESTOM_M} m: {len(a):,}", flush=True)

    # zgrade i rijeke/pruge
    z = gpd.read_file(INTERIM / "zgrade.gpkg", columns=["geometry"])
    zs = z.sindex
    rv = rijeke()
    rs = rv.sindex
    rows = []
    for u, v, l_, d_ in zip(a, b, L, D):
        g = LineString([xy[u], xy[v]])
        if len(zs.query(g.buffer(3), predicate="intersects")):
            continue
        prelaz = rv.vrsta.iloc[rs.query(g, predicate="intersects")].unique().tolist()
        mid = g.interpolate(0.5, normalized=True)
        u400 = tp.query_ball_point([mid.x, mid.y], 400)
        sl = float(st[u400][slabo[u400]].sum())
        if sl <= 0:
            continue
        rows.append({"u": int(u), "v": int(v), "spoj_m": round(l_), "cestom_m": round(d_), "usteda_km": round((d_ - l_) / 1000, 2),
                     "nagib_pct": round(abs(vis[u] - vis[v]) / l_ * 100, 1), "prelaz": ", ".join(prelaz) or "—",
                     "slabo_pokriveni_400m": int(sl), "ocjena": sl * min((d_ - l_) / 1000, 3.0), "geometry": g})
    S = gpd.GeoDataFrame(rows, crs=CRS_M)
    print(f"Bez zgrada na trasi: {len(S):,}", flush=True)
    # izbor: najbolja ocjena, najmanje 600 m od već izabranog
    S = S.sort_values("ocjena", ascending=False)
    izbor = []
    for r in S.itertuples():
        m_ = r.geometry.interpolate(0.5, normalized=True)
        if all(m_.distance(x.geometry.interpolate(0.5, normalized=True)) > 600 for x in izbor):
            izbor.append(r)
        if len(izbor) >= N_SPOJEVA:
            break
    S = gpd.GeoDataFrame([r._asdict() for r in izbor], crs=CRS_M).drop(columns="Index")

    # imena ulica na krajevima i naselje
    ime_cv = {}
    for k_, w in enumerate(wmeta):
        if w["ime"]:
            for nd in w["nds"]:
                ime_cv.setdefault(idx[nd], w["ime"])
    mz_tp = cKDTree(pcx)
    S["ulica_a"] = [ime_cv.get(u, "") for u in S.u]
    S["ulica_b"] = [ime_cv.get(v, "") for v in S.v]
    S["naselje"] = [f"{polja.mz.iat[mz_tp.query(xy[u])[1]]} / {polja.mz.iat[mz_tp.query(xy[v])[1]]}" for u, v in zip(S.u, S.v)]

    # linije kroz spoj: od najbliže stanice (portal) s jedne strane, kroz spoj, do najbliže s druge;
    # stanica mora biti na "svojoj" strani (bliža svom kraju spoja mrežom nego drugom)
    js = pd.read_csv(DATA / "jpks_stanice.csv")
    jsg = gpd.GeoDataFrame(js, geometry=gpd.points_from_xy(js.lon, js.lat), crs=CRS_WGS).to_crs(CRS_M)
    sxy = np.c_[jsg.geometry.x, jsg.geometry.y]
    tcv = cKDTree(xy[np.where(cv)[0]]); cvi = np.where(cv)[0]
    st_cv = cvi[tcv.query(sxy)[1]]
    jl = pd.read_csv(DATA / "jpks_linije.csv", dtype={"linija": str})
    jl["key"] = jl.vrsta + ":" + jl.linija.str.split().str[0]
    fq = jl.groupby("key").vrsni_sat_7_9.max()
    jaka = np.array([sum(fq.get(f"{v}:{k}", 0) for v, k in re.findall(r"(minibus|autobus|trolejbus|tramvaj):(\S+)", str(x)))
                     for x in js.linije])
    linije = []
    for i, r in enumerate(S.itertuples(), 1):
        Du, Pu = dijkstra(Gd, indices=[r.u], return_predecessors=True, limit=4000)
        Dv, Pv = dijkstra(Gd, indices=[r.v], return_predecessors=True, limit=4000)
        du, dv = Du[0][st_cv], Dv[0][st_cv]
        # stanica s polascima ≥ 4/h, na svojoj strani, najbliža
        def najbolja(dk, dd_):
            ok_ = (jaka >= 4) & np.isfinite(dk) & (dk < dd_)
            return int(np.argmin(np.where(ok_, dk, np.inf))) if ok_.any() else None
        sa, sb = najbolja(du, dv), najbolja(dv, du)
        if sa is None or sb is None:
            continue
        def put(P, src, t):
            p = [t]
            while p[-1] != src and p[-1] >= 0:
                p.append(P[0][p[-1]])
            return p[::-1]
        pa = put(Pu, r.u, st_cv[sa])[::-1]       # stanica A -> u
        pb = put(Pv, r.v, st_cv[sb])             # v -> stanica B
        cvorovi = pa + pb
        g = LineString([xy[k] for k in cvorovi])
        u400 = pc.within(g.buffer(400)).to_numpy()
        duzina = g.length
        prije = float(dijkstra(Gd, indices=[st_cv[sa]], limit=20000)[0][st_cv[sb]])
        linije.append({"id": f"D{i}", "od": js.naziv.iat[sa], "do": js.naziv.iat[sb], "spoj": f"{r.ulica_a or '?'} – {r.ulica_b or '?'}",
                       "naselje": r.naselje, "duzina_km": round(duzina / 1000, 1), "voznja_min": round(duzina / 1000 / 18 * 60),
                       "danas_cestom_km": round(prije / 1000, 1) if np.isfinite(prije) else None,
                       "stanovnici_400m": int(st[u400].sum()), "danas_slabo_pokriveni": int(st[u400 & slabo].sum()),
                       "spoj_m": r.spoj_m, "nagib_spoja_pct": r.nagib_pct, "prelaz": r.prelaz,
                       "geometry": g})
    Lg = gpd.GeoDataFrame(linije, crs=CRS_M)
    pd.set_option("display.width", 250); pd.set_option("display.max_colwidth", 50)
    print("\n== Kratki novi spojevi")
    print(S.drop(columns=["geometry", "u", "v", "ocjena"]).to_string(index=False))
    print("\n== Linije kroz spojeve")
    print(Lg.drop(columns="geometry").to_string(index=False))
    S.drop(columns=["geometry", "u", "v"]).to_csv(OUT / "dogradnje_spojevi.csv", index=False)
    Lg.drop(columns="geometry").to_csv(OUT / "dogradnje_linije.csv", index=False)
    out = pd.concat([S.assign(tip="spoj", id=[f"N{i}" for i in range(1, len(S) + 1)])[["tip", "id", "geometry"]],
                     Lg.assign(tip="linija")[["tip", "id", "geometry"]]], ignore_index=True)
    gpd.GeoDataFrame(out, crs=CRS_M).to_crs(CRS_WGS).to_file(OUT / "dogradnje.geojson", driver="GeoJSON", COORDINATE_PRECISION=5)


if __name__ == "__main__":
    main()
