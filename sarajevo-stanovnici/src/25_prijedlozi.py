"""Prijedlozi: nove linije javnog prevoza i novi cestovni spojevi (analiza, ne projekat).

Ulaz:  mreža, zone i matrice iz 24_putovanja.py (model_info.json za koeficijente),
       out/linije.geojson, out/prevoz_h3.csv, out/polja_h3.gpkg, out/radna_mjesta_h3.csv,
       out/model_dionice.geojson, out/teren_h3.csv
Izlaz: out/prijedlozi_prevoz.csv, out/prijedlozi_ceste.csv, out/prijedlozi.geojson

Javni prevoz
  1. Pravci: parovi zona (sva putovanja: posao + ostalo, sve vrste prevoza) udaljeni > 2,5 km,
     grupisani u šire područje (H3 7, ~5 km²), gdje bar jedan kraj nije na tramvaju/trolejbusu
     (≤ 600 m). Rang po broju putovanja dnevno; trasa = najkraći put cestom.
  2. Brdska naselja: MZ s najviše stanovnika > 8 min hoda do stanice (prevoz_h3), uz nagib.
  Napomena: OSM ima sve tramvajske i trolejbuske linije, ali mali dio autobuskih, pa je
  "nema linije" pouzdano samo za tramvaj/trolejbus.
Ceste
  1. Najopterećeniji pravci u vršnom satu (model, četiri općine).
  2. Nedostajući spojevi: parovi zona blizu zračnom linijom (< 2 km), a daleko cestom; za svaki
     par najbliži par čvorova ulica (≤ 900 m) postaje kandidat za novu dionicu (30 km/h). Kandidat se
     ocjenjuje ukupnom uštedom vremena svih putovanja autom (model) i nagibom (≤ 12%).
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import geopandas as gpd
import h3
import numpy as np
import pandas as pd
from scipy.sparse.csgraph import dijkstra
from scipy.spatial import cKDTree
from shapely.geometry import LineString, Point

from common import CRS_M, CRS_WGS, OUT


def _uvezi(ime, fajl):
    s = importlib.util.spec_from_file_location(ime, Path(__file__).with_name(fajl))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


mp = _uvezi("mp", "24_putovanja.py")
dost = mp.dost

MIN_DUZINA_M = 2500
TRUNK_M = 600
N_PRAVACA = 8
N_KAND = 25
N_CESTA = 8


def main() -> None:
    wmeta, xy, ll, e, idx = mp.mreza()
    n = len(xy)
    Z = mp.zone(xy, ll, e, wmeta)
    cv = Z.cvor.to_numpy()
    zz = (Z.tip == "zona").to_numpy()
    G = mp.graf(e, n, e.t0.to_numpy())
    D = dijkstra(G, indices=cv)[:, cv]
    print("matrica vremena ok", flush=True)
    D[~np.isfinite(D)] = 1e3
    mats = mp.matrice(Z, D)
    info = json.load(open(OUT / "model_info.json"))
    k = info["koef"]
    T_auto = (k["posao_po_zaposlenom"] * mats["hbw"] + k["ostalo_po_stanovniku"] * mats["oth"]
              + k["izvana_po_ulazu"] * mats["ext"]) / 2       # jednosmjerna putovanja autom dnevno
    T_sve = (mats["hbw"] + mats["oth"]) / 2                     # sva putovanja (svi načini), gruba mjera

    cz = np.array([h3.cell_to_latlng(h) if t == "zona" else (ll[c][1], ll[c][0])
                   for h, t, c in zip(Z.index, Z.tip, cv)])
    zpt = gpd.GeoSeries(gpd.points_from_xy(cz[:, 1], cz[:, 0]), crs=CRS_WGS).to_crs(CRS_M)
    zxy = np.c_[zpt.x, zpt.y]
    zrak = np.hypot(zxy[:, None, 0] - zxy[None, :, 0], zxy[:, None, 1] - zxy[None, :, 1])

    polja = gpd.read_file(OUT / "polja_h3.gpkg")
    pv = pd.read_csv(OUT / "prevoz_h3.csv").set_index("h3_id").reindex(polja.h3_id)
    rm = pd.read_csv(OUT / "radna_mjesta_h3.csv").set_index("h3_id").radna_mjesta.reindex(polja.h3_id).fillna(0)
    ter = pd.read_csv(OUT / "teren_h3.csv").set_index("h3_id").reindex(polja.h3_id)
    pc = polja.geometry.centroid
    # naziv zone: MZ s najviše stanovnika
    polja["z"] = [h3.cell_to_parent(h, mp.H3Z) for h in polja.h3_id]
    naziv = polja.sort_values("stanovnici").groupby("z").mz.last()
    opn = polja.sort_values("stanovnici").groupby("z").opcina.last()
    def ime_zone(i):
        h = Z.index[i]
        if Z.tip.iat[i] != "zona":
            return f"ulaz ({cz[i][0]:.3f}, {cz[i][1]:.3f})"
        m = naziv.get(h)
        return m if isinstance(m, str) else f"izvan 4 općine ({cz[i][0]:.3f}, {cz[i][1]:.3f})"

    # ------------------------------------------------ javni prevoz: pravci
    li = gpd.read_file(OUT / "linije.geojson").to_crs(CRS_M)
    trunk = li[li["mod"].isin(["tram", "trolleybus"])].union_all()
    na_trunku = np.array([Point(p).distance(trunk) <= TRUNK_M for p in zxy])
    sve_linije_buf = li.union_all().buffer(500)
    print("linije ok", flush=True)
    z7 = np.array([h3.cell_to_parent(h, 7) if t == "zona" else f"u{i}" for i, (h, t) in enumerate(zip(Z.index, Z.tip))])
    rows = []
    for o in range(len(Z)):
        if not zz[o]:
            continue
        for d in range(o + 1, len(Z)):
            if not zz[d] or zrak[o, d] < MIN_DUZINA_M or (na_trunku[o] and na_trunku[d]):
                continue
            rows.append((z7[o], z7[d], o, d, T_sve[o, d] + T_sve[d, o]))
    od = pd.DataFrame(rows, columns=["a7", "b7", "o", "d", "put"])
    od["par"] = [tuple(sorted(x)) for x in zip(od.a7, od.b7)]
    od = od[od.a7 != od.b7]
    gr = od.groupby("par").agg(put=("put", "sum")).sort_values("put", ascending=False)
    # najjača zona na svakom kraju para
    pravci = []
    vec = set()
    pop_z = Z.stanovnici.to_numpy() + Z.rm.to_numpy()
    for par, r in gr.iterrows():
        if len(pravci) >= N_PRAVACA:
            break
        if par[0] in vec and par[1] in vec:
            continue
        sel = od[od.par == par]
        za = sel.groupby("o").put.sum().idxmax() if True else None
        oa = [i for i in range(len(Z)) if z7[i] == par[0]]
        ob = [i for i in range(len(Z)) if z7[i] == par[1]]
        a = max(oa, key=lambda i: pop_z[i]); b = max(ob, key=lambda i: pop_z[i])
        # trasa cestom
        _, P = dijkstra(G, indices=[cv[a]], return_predecessors=True)
        put = [cv[b]]
        while put[-1] != cv[a] and put[-1] >= 0:
            put.append(P[0][put[-1]])
        if put[-1] < 0:
            continue
        geom = LineString([ll[i] for i in put[::-1]])
        gm = gpd.GeoSeries([geom], crs=CRS_WGS).to_crs(CRS_M)[0]
        buf = gm.buffer(400)
        u400 = pc.within(buf).to_numpy()
        postoji_bus = sve_linije_buf.contains(Point(zxy[a])) and sve_linije_buf.contains(Point(zxy[b]))
        pravci.append({"tip": "pravac", "od": ime_zone(a), "do": ime_zone(b),
                       "putovanja_dnevno": round(r.put), "duzina_km": round(gm.length / 1000, 1),
                       "stanovnici_400m": int(polja.stanovnici[u400].sum()), "radna_mjesta_400m": int(rm[u400].sum()),
                       "udio_na_tramvaju_trolejbusu": round(gm.intersection(trunk.buffer(60)).length / gm.length, 2),
                       "osm_bus_blizu_oba_kraja": bool(postoji_bus), "geometry": geom})
        vec |= set(par)
    pravci = gpd.GeoDataFrame(pravci, crs=CRS_WGS)
    print("pravci ok", flush=True)

    # ------------------------------------------------ javni prevoz: brdska naselja
    daleko = (pv.stanica_min.to_numpy() > 8) & (polja.stanovnici.to_numpy() > 0)
    b = polja.assign(daleko=np.where(daleko, polja.stanovnici, 0), nagib=ter.nagib_pct.to_numpy(),
                     ptal=pv.ptal_ai.to_numpy(), min_st=pv.stanica_min.to_numpy())
    brdo = b.dropna(subset=["mz"]).groupby(["opcina", "mz"]).apply(lambda g: pd.Series({
        "stanovnici": g.stanovnici.sum(), "daleko_od_stanice": g.daleko.sum(),
        "prosj_min_do_stanice": np.average(g.min_st.fillna(99).clip(upper=30), weights=g.stanovnici.clip(lower=1)),
        "prosj_nagib_pct": np.average(g.nagib.fillna(0), weights=g.stanovnici.clip(lower=1))}),
        include_groups=False).reset_index()
    brdo = brdo[brdo.daleko_od_stanice >= 300].sort_values("daleko_od_stanice", ascending=False).head(12)

    # ------------------------------------------------ ceste: opterećenje
    md = gpd.read_file(OUT / "model_dionice.geojson")
    from common import ucitaj_granice
    op, _ = ucitaj_granice()
    md = md[md.geometry.interpolate(0.5, normalized=True).within(op.to_crs(CRS_WGS).union_all())]
    md["vc"] = md.jaci_smjer * mp.UDIO_VRSNOG_SATA / md.kap_smjer
    opt = (md[md.ime != ""].assign(km=md.to_crs(CRS_M).length / 1000)
           .groupby("ime").apply(lambda g: pd.Series({"max_vc": g.vc.max(), "dnevno": g.dnevno.max(),
                                                       "km_preko_90": g.km[g.vc > 0.9].sum()}), include_groups=False)
           .sort_values("km_preko_90", ascending=False))
    opt = opt[opt.km_preko_90 > 0].head(10)

    # ------------------------------------------------ ceste: nedostajući spojevi
    vis = dost.visine_cvorova(ll[:, 0], ll[:, 1], tlo=True)
    ok_hw = {"residential", "unclassified", "tertiary", "secondary", "primary", "trunk",
             "tertiary_link", "secondary_link", "primary_link", "living_street"}
    cv_ok = np.zeros(n, bool)
    ehw = e.w.map(lambda k_: wmeta[k_]["hw"]).to_numpy()
    m_ok = np.isin(ehw, list(ok_hw))
    cv_ok[e.u[m_ok]] = True; cv_ok[e.v[m_ok]] = True
    kn = np.where(cv_ok)[0]
    tk = cKDTree(xy[kn])
    # vrijeme cestom vs zračna linija (30 km/h, 65% -> ~19,5 km/h): kandidat ako je cestom > 3× sporije
    v_ref = 30 * dost.FAKTOR_GRADSKE_VOZNJE / 60 * 1000   # m/min
    tez = T_auto + T_auto.T
    kand = []
    for o in np.where(zz)[0]:
        for d in np.where(zz)[0]:
            if d <= o or not (400 < zrak[o, d] < 2000):
                continue
            omjer = D[o, d] / (zrak[o, d] / v_ref)
            if omjer > 2.5 and tez[o, d] > 5:
                kand.append((o, d, omjer, tez[o, d] * (D[o, d] - zrak[o, d] / v_ref)))
    kand = sorted(kand, key=lambda x: -x[3])[:N_KAND * 3]
    cand_links = []
    for o, d, omjer, pot in kand:
        ia = tk.query_ball_point(zxy[o], 700); ib = tk.query_ball_point(zxy[d], 700)
        if not ia or not ib:
            continue
        A = kn[ia]; B = kn[ib]
        dd = np.hypot(xy[A][:, None, 0] - xy[B][None, :, 0], xy[A][:, None, 1] - xy[B][None, :, 1])
        i, j = np.unravel_index(dd.argmin(), dd.shape)
        u, v = A[i], B[j]
        L = dd[i, j]
        if L < 60 or L > 900:
            continue
        nag = abs(vis[u] - vis[v]) / L
        if nag > 0.12:
            continue
        if any(np.hypot(*(xy[u] - xy[c[0]])) < 300 and np.hypot(*(xy[v] - xy[c[1]])) < 300 for c in cand_links):
            continue
        cand_links.append((u, v, L, nag, o, d))
        if len(cand_links) >= N_KAND:
            break
    print(f"Kandidati za nove spojeve: {len(cand_links)}", flush=True)
    # ocjena: ušteda vremena svih putovanja autom (zone do 6 km od spoja)
    from scipy.sparse import csr_matrix
    base = e.t0.to_numpy()
    ocj = []
    for u, v, L, nag, o, d in cand_links:
        t_l = L / 1000 / (30 * dost.FAKTOR_GRADSKE_VOZNJE) * 60
        mid = (xy[u] + xy[v]) / 2
        bliz = np.where(np.hypot(*(zxy - mid).T) < 4000)[0]
        G2 = csr_matrix((np.r_[base, t_l, t_l], (np.r_[e.u, u, v], np.r_[e.v, v, u])), shape=(n, n))
        D2 = dijkstra(G2, indices=cv[bliz], limit=40)[:, cv]
        D2 = np.where(np.isfinite(D2), D2, D[bliz])
        dt = np.clip(D[bliz] - D2, 0, None)
        ustedjeno = float((T_auto[bliz] * dt).sum() + (T_auto[:, bliz].T * dt).sum())   # min/dan (oba smjera)
        korist = int((T_auto[bliz] * (dt > 1)).sum() + (T_auto[:, bliz].T * (dt > 1)).sum())
        geom = LineString([ll[u], ll[v]])
        print(f"spoj {len(ocj)+1}/{len(cand_links)}: {ime_zone(o)} – {ime_zone(d)}, {ustedjeno/60:.0f} h/dan", flush=True)
        ocj.append({"tip": "spoj", "od": ime_zone(o), "do": ime_zone(d), "duzina_m": round(L),
                    "nagib_pct": round(nag * 100, 1), "usteda_sati_dnevno": round(ustedjeno / 60),
                    "putovanja_s_ustedom_1min": korist, "cestom_prije_min": round(float(D[o, d]), 1),
                    "cestom_poslije_min": round(float(D2[np.where(bliz == o)[0][0], d]) if o in bliz else np.nan, 1),
                    "geometry": geom})
    ceste = gpd.GeoDataFrame(ocj, crs=CRS_WGS).sort_values("usteda_sati_dnevno", ascending=False).head(N_CESTA)

    pd.set_option("display.width", 250); pd.set_option("display.max_colwidth", 40)
    print("\n== Pravci bez tramvaja/trolejbusa na bar jednom kraju (sva putovanja dnevno, gruba mjera)")
    print(pravci.drop(columns="geometry").to_string(index=False))
    print("\n== Naselja s najviše stanovnika > 8 min hoda do stanice")
    print(brdo.round(1).to_string(index=False))
    print("\n== Najopterećenije ulice (km iznad 90% kapaciteta u vršnom satu)")
    print(opt.round(2).to_string())
    print("\n== Novi cestovni spojevi (ušteda vremena putovanja autom, model)")
    print(ceste.drop(columns="geometry").to_string(index=False))
    pravci.drop(columns="geometry").to_csv(OUT / "prijedlozi_prevoz.csv", index=False)
    brdo.to_csv(OUT / "prijedlozi_brdska_naselja.csv", index=False)
    ceste.drop(columns="geometry").to_csv(OUT / "prijedlozi_ceste.csv", index=False)
    opt.to_csv(OUT / "prijedlozi_opterecenje.csv")
    gpd.GeoDataFrame(pd.concat([pravci, ceste], ignore_index=True), crs=CRS_WGS).to_file(
        OUT / "prijedlozi.geojson", driver="GeoJSON", COORDINATE_PRECISION=5)


if __name__ == "__main__":
    main()
