"""Šta bi donijelo drastično unapređenje javnog prevoza: izbor auto/javni prevoz + dodjela autom.

Model izbora (binarni logit po paru zona, sva motorizovana putovanja):
  vrijeme autom  = vožnja sa zastojem (model 24/31) + parking (cilj u Centru/Starom Gradu 6 min,
                   Novo Sarajevo 3, ostalo 1)
  vrijeme javnim = hod do stanice (prosjek zone iz 18: stanica_min) + čekanje (0,5 · 60 / f + 2,
                   f = polasci na sat u dosegu / 4, najviše 30 min) + vožnja (vrijeme autom bez zastoja
                   · 1,6) + presjedanje (5 min ako je par dalje od 3 km)
  P(javni) = 1 / (1 + exp(β · (T_javni − T_auto) + ASC)), β = 0,07/min; ASC tako da je današnji
  udio javnog prevoza u motorizovanim putovanjima S0 (pretpostavka 45%; provjera 35% i 55%).
Unapređenje: polazaka 2× (čekanje upola), vožnja +25% brže (prioritet), hod do stanice −30% u
zonama gdje je danas > 6 min (brda), kazna za presjedanje upola.
Putovanja autom po paru se množe s (1 − P_novo) / (1 − P_danas); dodjela kao u 31_scenariji.py.
Ograničenja: nema ankete o načinu putovanja (S0 i β su pretpostavke); pješačenje i bicikl nisu
u modelu; nova potražnja (više putovanja zbog boljeg prevoza) nije uključena.
Izlaz: out/prevoz_scenarij.json, ispis.
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import geopandas as gpd
import h3
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
from scipy.spatial import cKDTree

from common import CRS_M, CRS_WGS, OUT


def _uvezi(ime, fajl):
    s = importlib.util.spec_from_file_location(ime, Path(__file__).with_name(fajl))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


mp = _uvezi("mp", "24_putovanja.py")
sc = _uvezi("sc", "31_scenariji.py")

BETA = 0.07
S0_SVE = (0.35, 0.45, 0.55)
S0 = 0.45
POBOLJ = {"frekvencija": 2.0, "brzina": 1.25, "hod_brda": 0.7, "presjedanje": 0.5}


def main() -> None:
    wmeta, xy, ll, e, idx = mp.mreza()
    n = len(xy)
    Z = mp.zone(xy, ll, e, wmeta)
    cv = Z.cvor.to_numpy()
    zz = (Z.tip == "zona").to_numpy()
    info = json.load(open(OUT / "model_info.json"))
    kk = (info["koef"]["posao_po_zaposlenom"], info["koef"]["ostalo_po_stanovniku"], info["koef"]["izvana_po_ulazu"])

    # atributi zona za javni prevoz (H3 10 -> zona H3 8, ponderisano stanovnicima)
    polja = gpd.read_file(OUT / "polja_h3.gpkg")
    pv = pd.read_csv(OUT / "prevoz_h3.csv").set_index("h3_id").reindex(polja.h3_id)
    polja["z"] = [h3.cell_to_parent(h, mp.H3Z) for h in polja.h3_id]
    w = polja.stanovnici.clip(lower=1)
    a = pd.DataFrame({"z": polja.z, "w": w, "hod": pv.stanica_min.clip(upper=20).to_numpy() * w,
                      "f": pv.polazaka_na_sat.to_numpy() * w}).groupby("z").sum()
    hod = (a.hod / a.w).reindex(Z.index).fillna(8.0).to_numpy()
    fz = (a.f / a.w).reindex(Z.index).fillna(8.0).to_numpy()
    opc = polja.groupby("z").opcina.agg(lambda s: s.mode().iat[0] if len(s.mode()) else None).reindex(Z.index)
    park = np.where(opc.isin(["Centar Sarajevo", "Stari Grad Sarajevo"]), 6.0, np.where(opc == "Novo Sarajevo", 3.0, 1.0))
    cz = np.array([h3.cell_to_latlng(h) if t == "zona" else (ll[c][1], ll[c][0]) for h, t, c in zip(Z.index, Z.tip, cv)])
    zp = gpd.GeoSeries(gpd.points_from_xy(cz[:, 1], cz[:, 0]), crs=CRS_WGS).to_crs(CRS_M)
    zxy = np.c_[zp.x, zp.y]
    zrak = np.hypot(zxy[:, None, 0] - zxy[None, :, 0], zxy[:, None, 1] - zxy[None, :, 1])

    D0 = dijkstra(mp.graf(e, n, e.t0.to_numpy()), indices=cv)[:, cv]
    D0[~np.isfinite(D0)] = 1e3

    def t_javni(pob=False):
        f = np.maximum(fz / 4, 0.5) * (POBOLJ["frekvencija"] if pob else 1)
        cek = np.minimum(0.5 * 60 / f + 2, 30)
        h_ = np.where(pob & (hod > 6), hod * POBOLJ["hod_brda"], hod) if pob else hod
        voz = D0 * 1.6 / (POBOLJ["brzina"] if pob else 1)
        pres = np.where(zrak > 3000, 5.0 * (POBOLJ["presjedanje"] if pob else 1), 0)
        return h_[:, None] + cek[:, None] + voz + pres + h_[None, :]

    def dodjela(faktor, rng_seed=7):
        """MSA kao u 31; matrica autom se množi faktorom (udio koji ostaje u autu)."""
        eid = csr_matrix((np.arange(1, len(e) + 1), (e.u, e.v)), shape=(n, n))
        rng = np.random.default_rng(rng_seed)
        t = e.t0.to_numpy().copy(); tok = np.zeros(len(e)); kap = e.kap.to_numpy(float)
        for it in range(1, sc.MSA + 1):
            D, _ = mp.stabla(mp.graf(e, n, t), cv)
            C = D[:, cv]; C[~np.isfinite(C)] = 1e3
            mats = mp.matrice(Z, C)
            T = sum(c * mats[q] for c, q in zip(kk, ("hbw", "oth", "ext"))) * faktor
            F = np.zeros(len(e))
            for _ in range(sc.RUTA):
                _, P = mp.stabla(mp.graf(e, n, t * rng.lognormal(0, mp.SIGMA_RUTA, len(t))), cv)
                F += mp.dodijeli(P, cv, [T], eid, n)[0] / sc.RUTA
            tok = F if it == 1 else tok + (F - tok) / it
            t = e.t0.to_numpy() * (1 + 0.15 * (tok * mp.UDIO_VRSNOG_SATA / kap) ** 4)
        Dz = dijkstra(mp.graf(e, n, t), indices=cv)[:, cv]; Dz[~np.isfinite(Dz)] = 1e3
        return tok, t, T, Dz

    # osnovno stanje: dodjela bez promjene, vrijeme autom sa zastojem
    tok0, t0_, T0, Dc = dodjela(1.0)
    Tauto = T0.copy()
    m_int = np.outer(zz, zz) & (zrak > 500)                       # unutar područja, ne kratka
    t_auto = Dc + park[None, :]
    rez = {}
    for s0 in S0_SVE:
        # ASC tako da je ponderisani udio javnog = s0 (ponder: sva motorizovana putovanja ≈ auto / (1 − P))
        dt = t_javni(False) - t_auto
        lo, hi = -10.0, 10.0
        for _ in range(60):
            asc = (lo + hi) / 2
            P = 1 / (1 + np.exp(BETA * dt + asc))
            sve = Tauto / np.maximum(1 - P, 1e-3)
            udio = (sve * P)[m_int].sum() / sve[m_int].sum()
            lo, hi = (asc, hi) if udio > s0 else (lo, asc)
        P0 = P
        P1 = 1 / (1 + np.exp(BETA * (t_javni(True) - t_auto) + asc))
        f_ = np.where(m_int, (1 - P1) / np.maximum(1 - P0, 1e-3), 1.0)
        sve = Tauto / np.maximum(1 - P0, 1e-3)
        rez[s0] = {"udio_danas": float((sve * P0)[m_int].sum() / sve[m_int].sum()),
                   "udio_poslije": float((sve * P1)[m_int].sum() / sve[m_int].sum()),
                   "auto_putovanja_promjena_pct": float(((Tauto * f_)[m_int].sum() / Tauto[m_int].sum() - 1) * 100),
                   "putnika_javni_promjena_pct": float(((sve * P1)[m_int].sum() / (sve * P0)[m_int].sum() - 1) * 100),
                   "faktor": f_}
        print(f"S0 = {s0:.0%}: udio javnog {rez[s0]['udio_danas']:.0%} → {rez[s0]['udio_poslije']:.0%}; "
              f"putovanja autom {rez[s0]['auto_putovanja_promjena_pct']:+.0f}%; putnika u javnom "
              f"{rez[s0]['putnika_javni_promjena_pct']:+.0f}%", flush=True)

    # dodjela za S0 (središnja pretpostavka)
    tok1, t1_, T1, Dc1 = dodjela(rez[S0]["faktor"])
    vh0, vh1 = float((tok0 * t0_).sum() / 60), float((tok1 * t1_).sum() / 60)
    # presjeci i vršni sat
    eime = e.w.map(lambda q: wmeta[q]["ime"]).to_numpy()
    mid = (xy[e.u] + xy[e.v]) / 2
    eid = csr_matrix((np.arange(1, len(e) + 1), (e.u, e.v)), shape=(n, n))

    def m_xy(lon, lat):
        p = gpd.GeoSeries(gpd.points_from_xy([lon], [lat]), crs=CRS_WGS).to_crs(CRS_M)[0]
        return np.array([p.x, p.y])

    pres = {}
    for nz, ul, lon, lat in sc.PRESJECI:
        p = m_xy(lon, lat)
        sel = np.where((np.hypot(*(mid - p).T) < 400) & np.array([ul.lower() in s.lower() for s in eime]))[0]
        if not len(sel):
            continue
        j = sel[np.argmax(tok0[sel])]
        rev = eid[e.v[j], e.u[j]]
        v0 = tok0[j] + (tok0[int(rev) - 1] if rev else 0); v1 = tok1[j] + (tok1[int(rev) - 1] if rev else 0)
        pres[nz] = [round(float(v0)), round(float(v1)), round(float((v1 / v0 - 1) * 100), 1)]
    kap = e.kap.to_numpy(float)
    preko = lambda tk: float((np.hypot(*(xy[e.u] - xy[e.v]).T) * (tk * mp.UDIO_VRSNOG_SATA / kap > 0.9)).sum() / 1000)  # noqa: E731
    sve_cv = np.unique(np.r_[e.u, e.v]); ta = cKDTree(xy[sve_cv])
    parovi = {}
    for nz, a_, b_ in sc.PAROVI:
        ca = sve_cv[ta.query(m_xy(*a_))[1]]; cb = sve_cv[ta.query(m_xy(*b_))[1]]
        parovi[nz] = [round(float(dijkstra(mp.graf(e, n, t0_), indices=[ca])[0, cb]), 1),
                      round(float(dijkstra(mp.graf(e, n, t1_), indices=[ca])[0, cb]), 1)]
    # vrijeme javnim prevozom za tipične parove (danas → poslije), zona do zone
    tz = cKDTree(zxy)
    pj = {}
    for nz, a_, b_ in sc.PAROVI:
        i = tz.query(m_xy(*a_))[1]; j = tz.query(m_xy(*b_))[1]
        pj[nz] = [round(float(t_javni(False)[i, j]), 0), round(float(t_javni(True)[i, j]), 0)]
    out = {"pretpostavke": {"beta": BETA, "S0": S0, "poboljsanje": POBOLJ},
           "osjetljivost": {f"{k:.2f}": {kk_: round(v, 3) for kk_, v in r.items() if kk_ != "faktor"} for k, r in rez.items()},
           "vozilo_sati": [round(vh0), round(vh1)], "km_preko_90pct_vrsni_sat": [round(preko(tok0), 1), round(preko(tok1), 1)],
           "presjeci": pres, "auto_min_vrsni": parovi, "javni_min": pj}
    json.dump(out, open(OUT / "prevoz_scenarij.json", "w"), ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != "pretpostavke"}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
