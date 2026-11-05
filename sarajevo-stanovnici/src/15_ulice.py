"""Pristup autom: uske i strme ulice po H3 polju.

Ulaz:  raw/Sarajewo.osm.gz (mreža), interim/zgrade.gpkg (otisci zgrada), out/polja_h3.gpkg,
       Copernicus DEM (kao 10_teren.py)
Izlaz: out/ulice_h3.csv        pokazatelji pristupa autom i ocjena 0–100 po polju
       out/ulice_dionice.gpkg  dionice ulica s procijenjenom širinom koridora i nagibom

Širina: OSM gotovo nema oznaku width (29 od 6.650 stambenih ulica), pa se procjenjuje
koridor između zgrada: s polovine svake dionice pruža se okomica lijevo i desno do 20 m
i mjeri udaljenost do najbliže zgrade. Koridor < 6 m = vrlo uska ulica (jedna traka,
nema mimoilaženja), 6–9 m = uska. Ograde i zidovi nisu u OSM-u, pa je ovo gornja granica
stvarne širine. Uske su i ulice s lanes=1, living_street i track.
Nagib: visina čvorova iz DEM-a. Copernicus je model površine (krovovi), pa se najprije
uzima najniža tačka u prozoru 90 m (ceste su na tlu), zatim izglađuje (~45 m). Mostovi i
tuneli se ne računaju (DEM vidi dolinu ispod mosta ili brdo iznad tunela).
Nagib se mjeri na 100 m (duž ulice i duž puta): DEM od 30 m na ulicama koje idu poprijeko
padine daje lažne nagibe na kratkim dionicama.

Put polja: od čvora najbližeg središtu polja najkraćim putem autom do najbliže glavne
ceste (tercijarna ili viša). Na tom putu: najveći nagib, dužina strmih (> 12%) i uskih
dionica, makadam. U polju: udio dužine ulica koje su strme ili uske.

Ocjena 0–100 (KAZNE ispod): 100 minus kazne za najveći nagib puta, uske dionice,
udio strmih ulica u polju i makadam.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
import shapely
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components, dijkstra
from scipy.spatial import cKDTree

from common import OSM_IME
from common import CRS_M, CRS_WGS, INTERIM, OUT, RAW

_s = importlib.util.spec_from_file_location("dost", Path(__file__).with_name("08_dostupnost.py"))
dost = importlib.util.module_from_spec(_s)
_s.loader.exec_module(dost)

GLAVNE = {"motorway", "motorway_link", "trunk", "trunk_link", "primary", "primary_link",
          "secondary", "secondary_link", "tertiary", "tertiary_link"}
USKE_KLASE = {"living_street", "track"}
MAKADAM = {"unpaved", "gravel", "dirt", "ground", "compacted", "fine_gravel", "earth", "mud", "grass"}
ZRAKA_M = 20.0
VRLO_USKO, USKO = 6.0, 9.0
STRMO = 0.12
PROZOR_M = 100.0

KAZNE = {
    "nagib": (0.08, 0.20, 40),   # najveći nagib puta: 0 do 8%, linearno do -40 na 20%+
    "usko_m": (10.0, 30),        # -1 bod na svakih 10 m uskog puta, najviše -30
    "strmo_udio": 20,            # udio strmih ulica u polju × 20
    "makadam_m": (20.0, 10),     # -1 na svakih 20 m makadama, najviše -10
}


def koridor(a: np.ndarray, b: np.ndarray, zgrade: gpd.GeoSeries) -> np.ndarray:
    """Širina koridora (m) na polovini dionica a->b: zbir udaljenosti do zgrada lijevo i desno."""
    m = (a + b) / 2
    v = b - a
    n = np.c_[-v[:, 1], v[:, 0]] / np.maximum(np.hypot(v[:, 0], v[:, 1]), 1e-9)[:, None]
    tree = shapely.STRtree(zgrade.to_numpy())
    geoms = zgrade.to_numpy()
    sirina = np.zeros(len(a))
    for znak in (1, -1):
        kraj = m + znak * n * ZRAKA_M
        poc = m + znak * n * 0.5
        zrake = shapely.linestrings(np.stack([poc, kraj], axis=1))
        ri, gi = tree.query(zrake, predicate="intersects")
        d = np.full(len(a), ZRAKA_M)
        if len(ri):
            dist = shapely.distance(shapely.points(m[ri]), geoms[gi])
            np.minimum.at(d, ri, dist)
        sirina += d
    return sirina


def main() -> None:
    polja = gpd.read_file(OUT / "polja_h3.gpkg")
    nodes, ways, _ = dost.ucitaj_mrezu(RAW / OSM_IME)
    used = sorted({n for _, nds in ways for n in nds if n in nodes})
    idx = {n: k for k, n in enumerate(used)}
    pts = gpd.GeoSeries(gpd.points_from_xy(*zip(*[nodes[n] for n in used])), crs=CRS_WGS).to_crs(CRS_M)
    xy = np.c_[pts.x, pts.y]
    ll = np.array([nodes[n] for n in used])
    z = dost.visine_cvorova(ll[:, 0], ll[:, 1], sigma=1.5, tlo=True)

    # dionice za automobil (isti filter kao 08, graf 'auto')
    rows = []
    for t, nds in ways:
        hw = t["highway"]
        v = dost.brzina(t) * dost.FAKTOR_GRADSKE_VOZNJE
        if v <= 0 or t.get("motor_vehicle") == "no" or t.get("access") in ("no", "private"):
            continue
        ow = t.get("oneway")
        jedno = 1 if ow in ("yes", "1", "true") or (t.get("junction") == "roundabout" and ow != "no") \
            else (-1 if ow == "-1" else 0)
        usk = hw in USKE_KLASE or t.get("lanes") == "1"
        mak = t.get("surface") in MAKADAM or (hw == "track" and "surface" not in t)
        most = t.get("bridge", "no") != "no" or t.get("tunnel", "no") != "no"
        k_ = [idx[n] for n in nds if n in idx]
        if len(k_) >= 2:
            cdw = np.r_[0, np.cumsum(np.hypot(*(xy[k_[1:]] - xy[k_[:-1]]).T))]
            zw = z[k_]
            if cdw[-1] > 0:
                h = PROZOR_M / 2
                sredina = (cdw[1:] + cdw[:-1]) / 2
                a_ = np.clip(sredina - h, 0, cdw[-1])
                b_ = np.clip(sredina + h, 0, cdw[-1])
                nag_way = np.abs(np.interp(b_, cdw, zw) - np.interp(a_, cdw, zw)) / np.maximum(b_ - a_, 1)
            else:
                nag_way = np.zeros(len(k_) - 1)
            nag_map = {(k_[q], k_[q + 1]): nag_way[q] for q in range(len(k_) - 1)}
        else:
            nag_map = {}
        sir_tag = pd.to_numeric(str(t.get("width", "")).replace("m", "").replace(",", "."), errors="coerce")
        for a, b in zip(nds[:-1], nds[1:]):
            if a in idx and b in idx:
                rows.append((idx[a], idx[b], v, jedno, hw, usk, mak, sir_tag, most,
                             nag_map.get((idx[a], idx[b]), 0.0)))
    e = pd.DataFrame(rows, columns=["i", "j", "v", "jedno", "klasa", "usk", "mak", "sir_tag", "most", "nag_way"])
    e["d"] = np.hypot(*(xy[e.i] - xy[e.j]).T)
    e = e[e.d > 0].reset_index(drop=True)
    e["glavna"] = e.klasa.isin(GLAVNE)

    # koridor samo za dionice unutar okvira općina (ostalo: otvoreno)
    x0, y0, x1, y1 = polja.total_bounds
    mid = (xy[e.i] + xy[e.j]) / 2
    u = (mid[:, 0] >= x0) & (mid[:, 0] <= x1) & (mid[:, 1] >= y0) & (mid[:, 1] <= y1) & ~e.glavna.to_numpy()
    zg = gpd.read_file(INTERIM / "zgrade.gpkg").geometry
    e["koridor"] = 2 * ZRAKA_M
    e.loc[u, "koridor"] = koridor(xy[e.i[u]], xy[e.j[u]], zg)
    e.loc[e.sir_tag.notna(), "koridor"] = e.sir_tag + 4  # širina kolovoza + ~2 m sa svake strane
    e["uska"] = (e.koridor < USKO) | e.usk
    e["vrlo_uska"] = (e.koridor < VRLO_USKO)
    e["nagib"] = e.nag_way  # nagib na 100 m duž iste ulice (kraće dionice su šum DEM-a od 30 m)
    e.loc[e.most, "nagib"] = 0.0  # most/tunel: DEM vidi dolinu ili brdo, ne kolovoz

    # graf (minute), oba smjera po pravilima jednosmjernih
    w = e.d / 1000 / e.v * 60
    fw = e.jedno >= 0
    bw = e.jedno <= 0
    r = np.r_[e.i[fw], e.j[bw]]
    c = np.r_[e.j[fw], e.i[bw]]
    eid = np.r_[e.index[fw], e.index[bw]]
    N = len(xy)
    G = coo_matrix((np.r_[w[fw], w[bw]], (r, c)), shape=(N, N)).tocsr()
    kljuc = pd.Series(eid, index=r.astype(np.int64) * N + c)
    kljuc = kljuc[~kljuc.index.duplicated()]

    _, lab = connected_components(G, directed=True, connection="strong")
    ok = np.where(lab == np.bincount(lab).argmax())[0]
    izvori = np.unique(np.r_[e.i[e.glavna], e.j[e.glavna]])
    izvori = izvori[np.isin(izvori, ok)]
    D, pred, _ = dijkstra(G.T.tocsr(), indices=izvori, min_only=True, return_predecessors=True)

    cen = polja.geometry.centroid
    tree = cKDTree(xy[ok])
    _, ic = tree.query(np.c_[cen.x, cen.y])
    start = ok[ic]

    rez = []
    for s in start:
        put = [s]
        while pred[put[-1]] >= 0 and len(put) < 5000:
            put.append(pred[put[-1]])
        p = np.array(put)
        if len(p) < 2:
            rez.append((0, 0.0, 0, 0, 0, 2 * ZRAKA_M))
            continue
        ids = kljuc.reindex(p[:-1].astype(np.int64) * N + p[1:]).to_numpy()
        ids = ids[~np.isnan(ids)].astype(int)
        seg = e.loc[ids]
        cd = np.r_[0, np.cumsum(np.hypot(*(xy[p[1:]] - xy[p[:-1]]).T))]
        zz = z[p].astype(float).copy()
        mm = np.zeros(len(p), bool)
        if len(seg) == len(p) - 1:
            mm[1:-1] = seg.most.to_numpy()[1:] | seg.most.to_numpy()[:-1]
        if mm.any() and (~mm).sum() >= 2:
            zz[mm] = np.interp(cd[mm], cd[~mm], zz[~mm])
        j = np.searchsorted(cd, cd + PROZOR_M)
        okj = j < len(cd)
        nag = np.abs(zz[j[okj]] - zz[okj]) / np.maximum(cd[j[okj]] - cd[okj], 1)
        max_nag = float(nag.max()) if len(nag) else float(np.abs(zz[-1] - zz[0]) / max(cd[-1], 1))
        strmo_m = float(seg.d[seg.nagib > STRMO].sum())
        usko_m = float(seg.d[seg.uska & ~seg.glavna].sum())
        mak_m = float(seg.d[seg.mak].sum())
        min_kor = float(seg.koridor[~seg.glavna].min()) if (~seg.glavna).any() else 2 * ZRAKA_M
        rez.append((cd[-1], max_nag, strmo_m, usko_m, mak_m, min_kor))
    out = pd.DataFrame(rez, columns=["put_m", "put_max_nagib", "put_strmo_m", "put_usko_m", "put_makadam_m",
                                     "put_min_koridor_m"])
    out.insert(0, "h3_id", polja.h3_id.to_numpy())

    # u polju: udio dužine ulica (ne glavnih) koje su strme / uske
    eg = gpd.GeoDataFrame(e[~e.glavna], geometry=gpd.points_from_xy(mid[~e.glavna, 0], mid[~e.glavna, 1]), crs=CRS_M)
    j = gpd.sjoin(eg, polja[["h3_id", "geometry"]], predicate="within")
    g = j.groupby("h3_id")
    uk = g.d.sum()
    out = out.set_index("h3_id")
    out["ulice_m"] = uk.reindex(out.index).fillna(0).round(0)
    out["udio_strmo"] = (j[j.nagib > STRMO].groupby("h3_id").d.sum() / uk).reindex(out.index).fillna(0).round(2)
    out["udio_usko"] = (j[j.uska].groupby("h3_id").d.sum() / uk).reindex(out.index).fillna(0).round(2)

    k = KAZNE
    kn = np.clip((out.put_max_nagib - k["nagib"][0]) / (k["nagib"][1] - k["nagib"][0]), 0, 1) * k["nagib"][2]
    ku = np.minimum(out.put_usko_m / k["usko_m"][0], k["usko_m"][1])
    ks = out.udio_strmo * k["strmo_udio"]
    km = np.minimum(out.put_makadam_m / k["makadam_m"][0], k["makadam_m"][1])
    out["ocjena_pristupa"] = np.clip(100 - kn - ku - ks - km, 0, 100).round(0).astype(int)
    out["put_max_nagib"] = (out.put_max_nagib * 100).round(1)
    for c_ in ("put_m", "put_strmo_m", "put_usko_m", "put_makadam_m", "put_min_koridor_m"):
        out[c_] = out[c_].round(0).astype(int)
    out.reset_index().to_csv(OUT / "ulice_h3.csv", index=False)

    lin = gpd.GeoDataFrame(e[["klasa", "koridor", "nagib", "uska", "vrlo_uska", "mak"]].assign(
        nagib=lambda d: (d.nagib * 100).round(1), koridor=lambda d: d.koridor.round(1)),
        geometry=shapely.linestrings(np.stack([xy[e.i], xy[e.j]], axis=1)), crs=CRS_M)
    lin = lin[u | e.glavna.to_numpy()]
    lin.to_file(OUT / "ulice_dionice.gpkg", driver="GPKG")

    j2 = out.join(polja.set_index("h3_id")[["opcina", "mz", "stanovnici"]])
    nas = j2[j2.stanovnici > 0]
    wv = nas.stanovnici
    print(f"Dionica za auto: {len(e)}, od toga uskih (koridor < {USKO:.0f} m ili klasa): {e.uska.sum()}, "
          f"vrlo uskih (< {VRLO_USKO:.0f} m): {e.vrlo_uska.sum()}")
    print("Stanovnici po najvećem nagibu puta do glavne ceste: " + ", ".join(
        f"{a}–{b}%: {wv[(nas.put_max_nagib >= a) & (nas.put_max_nagib < b)].sum():,.0f}"
        for a, b in ((0, 8), (8, 12), (12, 16), (16, 20), (20, 100))))
    print(f"Stanovnici s > 100 m uskog puta do glavne ceste: {wv[nas.put_usko_m > 100].sum():,.0f}")
    print("\nOcjena pristupa po općini (prosjek po stanovniku):")
    print(nas.groupby("opcina").apply(lambda g: np.average(g.ocjena_pristupa, weights=g.stanovnici),
                                      include_groups=False).round(0).to_string())
    mz = nas.dropna(subset=["mz"]).groupby(["opcina", "mz"]).apply(
        lambda g: pd.Series({"st": g.stanovnici.sum(),
                             "ocjena": np.average(g.ocjena_pristupa, weights=g.stanovnici),
                             "max_nagib": np.average(g.put_max_nagib, weights=g.stanovnici),
                             "usko_m": np.average(g.put_usko_m, weights=g.stanovnici)}), include_groups=False)
    print("\nNajteži pristup (MZ):")
    print(mz.sort_values("ocjena").round(0).head(10).to_string())


if __name__ == "__main__":
    main()
