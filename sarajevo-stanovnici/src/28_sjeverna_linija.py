"""Ocjena prijedloga: sjeverna brdska linija (trasa preko brda, ne dolinom) Stup – Zabrđe – Briješće – Sokolje – Buća Potok –
Pofalići – Velešići – Željeznička stanica (u poređenju s P1 Zabrđe – Alipašin Most).

Izlaz: out/sjeverna_linija.geojson (trasa s dionicama), ispis pokazatelja.
Pokazatelji: dužina, vožnja (autom · 1,4), stanovnici/radna mjesta do 400 m, stanovnici danas
> 8 min od stanice, putovanja dnevno između zona uz trasu (model 24, sva putovanja; linija ih
vozi bez presjedanja), najveći nagib na 100 m, dužina uskih ulica (15_ulice: koridor < 6 m),
postojeće linije po dionici (portal Ministarstva).
"""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

import geopandas as gpd
import h3
import numpy as np
import pandas as pd
from scipy.sparse.csgraph import connected_components, dijkstra
from scipy.spatial import cKDTree
from shapely.geometry import LineString, Point

from common import CRS_M, CRS_WGS, DATA, OUT


def _uvezi(ime, fajl):
    s = importlib.util.spec_from_file_location(ime, Path(__file__).with_name(fajl))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


mp = _uvezi("mp", "24_putovanja.py")

TACKE = [("Stup", None), ("Zabrđe", "Novi Grad Sarajevo"), ("Briješće", "Novi Grad Sarajevo"),
         ("Naselje heroja Sokolje", "Novi Grad Sarajevo"), ("Buća Potok", "Novi Grad Sarajevo"),
         ("Pofalići II", "Novo Sarajevo"), ("Velešići", "Novo Sarajevo"), ("Željeznička stanica", None)]
PREKO_BRDA = True      # trasa preko brda: ceste niže od H_DOLINA iznad dna doline su KAZNA_DOLINA puta "skuplje"
H_DOLINA = 40.0
KAZNA_DOLINA = 6.0
IZUZETAK_M = 800       # oko Stupa i Željezničke (krajevi su u dolini)
FIKSNE = {"Stup": (18.3317, 43.8460), "Željeznička stanica": (18.3998, 43.8590)}


def main() -> None:
    wmeta, xy, ll, e, idx = mp.mreza()
    n = len(xy)
    G = mp.graf(e, n, e.t0.to_numpy())
    _, lab = connected_components(G, directed=True, connection="strong")
    ok = np.where(lab == np.bincount(lab).argmax())[0]
    tk = cKDTree(xy[ok])
    polja = gpd.read_file(OUT / "polja_h3.gpkg")
    pv = pd.read_csv(OUT / "prevoz_h3.csv").set_index("h3_id").reindex(polja.h3_id)
    rm = pd.read_csv(OUT / "radna_mjesta_h3.csv").set_index("h3_id").radna_mjesta.reindex(polja.h3_id).fillna(0).to_numpy()
    pc = polja.geometry.centroid
    pcw = pc.to_crs(CRS_WGS)
    daleko = (pv.stanica_min.to_numpy() > 8) & (polja.stanovnici.to_numpy() > 0)

    # visina iznad dna doline (kao 17_zrak.py): teren minus najniža tačka u krugu 3 km
    from scipy.ndimage import gaussian_filter, grey_opening, minimum_filter
    ter = _uvezi("ter", "10_teren.py")
    zr, tr = ter.dem()
    zr = gaussian_filter(grey_opening(zr, size=(3, 3)), 1)
    py_, px_ = abs(tr.e) * 111_320, tr.a * 111_320 * np.cos(np.radians(43.86))
    hr = zr - gaussian_filter(minimum_filter(zr, size=(int(6000 / py_), int(6000 / px_))), 15)

    def h_at(lon, lat):
        c = np.clip(((np.asarray(lon) - tr.c) / tr.a).astype(int), 0, hr.shape[1] - 1)
        r = np.clip(((np.asarray(lat) - tr.f) / tr.e).astype(int), 0, hr.shape[0] - 1)
        return hr[r, c]

    hn = h_at(ll[:, 0], ll[:, 1])
    hc = h_at(pcw.x.to_numpy(), pcw.y.to_numpy())
    he = (hn[e.u.to_numpy()] + hn[e.v.to_numpy()]) / 2
    dolina_e = he < H_DOLINA
    izuzeto = np.zeros(len(e), bool)
    for lon, lat in FIKSNE.values():
        p = gpd.GeoSeries([Point(lon, lat)], crs=CRS_WGS).to_crs(CRS_M)[0]
        mid = (xy[e.u.to_numpy()] + xy[e.v.to_numpy()]) / 2
        izuzeto |= np.hypot(mid[:, 0] - p.x, mid[:, 1] - p.y) < IZUZETAK_M
    G_brdo = mp.graf(e, n, e.t0.to_numpy() * np.where(dolina_e & ~izuzeto, KAZNA_DOLINA, 1.0))
    eid = {(u, v): k for k, (u, v) in enumerate(zip(e.u.to_numpy(), e.v.to_numpy()))}

    def tacka(ime, op):
        if ime in FIKSNE:
            return FIKSNE[ime]
        m = ((polja.mz == ime) & (polja.opcina == op)).to_numpy() & (polja.stanovnici.to_numpy() > 0)
        if (m & (hc >= H_DOLINA)).sum() >= 3:
            m &= hc >= H_DOLINA                           # brdski dio naselja (iznad dna doline)
        if (m & daleko).sum() >= 3:
            m &= daleko                                   # i daleko od stanice
        w = polja.stanovnici.to_numpy()[m]
        return float(np.average(pcw.x[m], weights=w)), float(np.average(pcw.y[m], weights=w))

    def cvor(lon, lat):
        p = gpd.GeoSeries([Point(lon, lat)], crs=CRS_WGS).to_crs(CRS_M)[0]
        return ok[tk.query([p.x, p.y])[1]]

    def trasa(tacke):
        cv = [cvor(*t) for t in tacke]
        put, dion, minute = [cv[0]], [], 0.0
        for a, b in zip(cv[:-1], cv[1:]):
            D, P = dijkstra(G_brdo if PREKO_BRDA else G, indices=[a], return_predecessors=True)
            seg = [b]
            while seg[-1] != a:
                seg.append(P[0, seg[-1]])
            dion.append(seg[::-1])
            put += seg[::-1][1:]
        ids = [eid[(u, v)] for u, v in zip(put[:-1], put[1:])]
        minute = float(e.t0.to_numpy()[ids].sum())
        trasa.dolina_km = float((np.hypot(*(xy[put[1:]] - xy[put[:-1]]).T) * dolina_e[ids]).sum() / 1000)
        return put, dion, minute

    vis = mp.dost.visine_cvorova(ll[:, 0], ll[:, 1], tlo=True)
    js = pd.read_csv(DATA / "jpks_stanice.csv")
    S = gpd.GeoDataFrame(js, geometry=gpd.points_from_xy(js.lon, js.lat), crs=CRS_WGS).to_crs(CRS_M)
    jl = pd.read_csv(DATA / "jpks_linije.csv", dtype={"linija": str})
    jl["key"] = jl.vrsta + ":" + jl.linija.str.split().str[0]
    fq = jl.groupby("key").vrsni_sat_7_9.max()
    uske = gpd.read_file(OUT / "ulice_dionice.gpkg")
    uske = uske[uske.uska.astype(bool)].to_crs(CRS_M) if "uska" in uske else uske.iloc[0:0]

    # zone i putovanja (model 24)
    Z = mp.zone(xy, ll, e, wmeta)
    cvz = Z.cvor.to_numpy()
    Dz = dijkstra(G, indices=cvz)[:, cvz]
    Dz[~np.isfinite(Dz)] = 1e3
    mats = mp.matrice(Z, Dz)
    T_sve = (mats["hbw"] + mats["oth"]) / 2
    czz = np.array([h3.cell_to_latlng(h) if t == "zona" else (ll[c][1], ll[c][0]) for h, t, c in zip(Z.index, Z.tip, cvz)])
    zpt = gpd.GeoSeries(gpd.points_from_xy(czz[:, 1], czz[:, 0]), crs=CRS_WGS).to_crs(CRS_M)

    def ocijeni(naziv, tacke):
        put, dion, minute = trasa(tacke)
        g = LineString([ll[i] for i in put])
        gm = gpd.GeoSeries([g], crs=CRS_WGS).to_crs(CRS_M)[0]
        u = pc.within(gm.buffer(400)).to_numpy()
        # nagib na prozoru ~100 m
        pxy = xy[put]
        dd = np.r_[0, np.cumsum(np.hypot(*np.diff(pxy, axis=0).T))]
        z = vis[put]
        nag = []
        for i in range(len(put)):
            j = np.searchsorted(dd, dd[i] + 100)
            if j < len(put) and dd[j] - dd[i] > 50:
                nag.append(abs(z[j] - z[i]) / (dd[j] - dd[i]))
        uska_m = float(uske.intersection(gm.buffer(8)).length.sum() / 2) if len(uske) else float("nan")
        uz = np.where((zpt.distance(gm) <= 600).to_numpy() & (Z.tip == "zona").to_numpy())[0]
        koridor = float(T_sve[np.ix_(uz, uz)].sum())
        rows = []
        for k, seg in enumerate(dion):
            sg = gpd.GeoSeries([LineString([ll[i] for i in seg])], crs=CRS_WGS).to_crs(CRS_M)[0]
            cnt = {}
            for l in S[S.distance(sg) <= 250].linije.dropna():
                for v, kk in re.findall(r"(minibus|autobus|trolejbus|tramvaj):(\S+)", l):
                    cnt[f"{v} {kk}"] = cnt.get(f"{v} {kk}", 0) + 1
            lst = sorted([x for x, c in cnt.items() if c >= 2 and fq.get(x.replace(" ", ":"), 0) > 0],
                         key=lambda x: -fq.get(x.replace(" ", ":"), 0))
            rows.append({"dionica": f"{tacke_imena[naziv][k]} – {tacke_imena[naziv][k + 1]}",
                         "km": round(sg.length / 1000, 1),
                         "postojece": ", ".join(f"{x} ({fq.get(x.replace(' ', ':'), 0):g}/h)" for x in lst[:4]) or "—"})
        rez = {"linija": naziv, "km": round(gm.length / 1000, 1), "voznja_min": round(minute * 1.4),
               "stanovnici_400m": int(polja.stanovnici[u].sum()), "radna_mjesta_400m": int(rm[u].sum()),
               "danas_>8min_od_stanice": int(polja.stanovnici[u & daleko].sum()),
               "putovanja_u_koridoru_dnevno": round(koridor), "zona_uz_trasu": len(uz),
               "max_nagib_100m_pct": round(100 * max(nag), 1) if nag else None,
               "nagib_>10pct_km": round(sum(1 for x in nag if x > 0.10) * float(np.mean(np.diff(dd))) / 1000, 1) if nag else 0,
               "uske_ulice_m": round(uska_m), "u_dolini_km": round(trasa.dolina_km, 1)}
        return rez, pd.DataFrame(rows), g

    tacke_s = [tacka(i, o) for i, o in TACKE]
    tacke_p1 = [tacka("Zabrđe", "Novi Grad Sarajevo"), tacka("Briješće", "Novi Grad Sarajevo"),
                tacka("Naselje heroja Sokolje", "Novi Grad Sarajevo"), (18.3475, 43.8480)]
    tacke_imena = {"Sjeverna (prijedlog)": [i for i, _ in TACKE],
                   "P1": ["Zabrđe", "Briješće", "Sokolje", "Alipašin Most"]}
    r1, d1, g1 = ocijeni("Sjeverna (prijedlog)", tacke_s)
    r2, d2, g2 = ocijeni("P1", tacke_p1)
    # varijante
    tacke_imena["Bez Stupa"] = [i for i, _ in TACKE[1:]]
    tacke_imena["Zapad"] = ["Zabrđe", "Briješće", "Sokolje", "Buća Potok", "Otoka (tramvaj)"]
    tacke_imena["Istok"] = ["Buća Potok", "Pofalići II", "Velešići", "Željeznička stanica"]
    rv1, dv1, gv1 = ocijeni("Bez Stupa", tacke_s[1:])
    rv2, dv2, gv2 = ocijeni("Zapad", tacke_s[1:5] + [(18.3640, 43.8487)])
    rv3, dv3, gv3 = ocijeni("Istok", tacke_s[4:])
    # zaobilaznost: cestom / zračno po dionici
    for k in range(len(tacke_s) - 1):
        a_, b_ = [gpd.GeoSeries([Point(*t)], crs=CRS_WGS).to_crs(CRS_M)[0] for t in tacke_s[k:k + 2]]
        print(f"{TACKE[k][0]} – {TACKE[k + 1][0]}: zračno {a_.distance(b_) / 1000:.1f} km, cestom {d1.km.iat[k]} km")
    pd.set_option("display.width", 250)
    print(pd.DataFrame([r1, rv1, rv2, rv3, r2]).set_index("linija").T.to_string())
    for nm, gg, rr in (("S_zapad", gv2, rv2), ("S_istok", gv3, rv3)):
        gpd.GeoDataFrame([{"id": nm, **{k: v for k, v in rr.items() if k != "linija"}}], geometry=[gg], crs=CRS_WGS).to_file(
            OUT / f"sjeverna_{nm.lower()}.geojson", driver="GeoJSON", COORDINATE_PRECISION=5)
    print("\nSjeverna – postojeće linije po dionici:\n" + d1.to_string(index=False))
    gpd.GeoDataFrame([{"id": "S", "naziv": "Stup – Zabrđe – Briješće – Sokolje – Buća Potok – Pofalići – Velešići – Željeznička",
                       **{k: v for k, v in r1.items() if k != "linija"}}], geometry=[g1], crs=CRS_WGS).to_file(
        OUT / "sjeverna_linija.geojson", driver="GeoJSON", COORDINATE_PRECISION=5)
    d1.to_csv(OUT / "sjeverna_linija_dionice.csv", index=False)


if __name__ == "__main__":
    main()
