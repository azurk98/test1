"""Brdska naselja: šta bi navelo ljude da na posao ne idu autom (isti model izbora kao 32).

Brdske zone: prosječna visina iznad dna doline ≥ 40 m (17_zrak). Danas su to naselja gdje je
auto skoro jedini razuman izbor (rijetke linije, strm hod, presjedanje).
Scenariji (samo za putovanja koja počinju ili završavaju u brdskoj zoni, osim B2 parkinga):
  B1  brdski midibusi: čekanje najviše 0,5 · 60 / 8 + 1 (8 polazaka/h, usklađeno), hod do stanice −40%
      (gušće stanice, kosi liftovi, prevoz na poziv), presjedanje 2 min (jedna karta, usklađeni polasci)
  B2  B1 + parking u centru (cilj u Centru, Starom Gradu, Novom Sarajevu): +5 min za auto
      (ekvivalent naplate i traženja mjesta)

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
Izlaz: out/brda_scenarij.json, ispis.
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
H_BRDO = 40.0


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

    zr = pd.read_csv(OUT / "zrak_h3.csv").set_index("h3_id").reindex(polja.h3_id)
    hz = pd.DataFrame({"z": polja.z, "w": w, "h": zr.iznad_dna_m.fillna(0).to_numpy() * w}).groupby("z").sum()
    brdo = ((hz.h / hz.w).reindex(Z.index).fillna(0).to_numpy() >= H_BRDO) & zz
    centar = opc.isin(["Centar Sarajevo", "Stari Grad Sarajevo", "Novo Sarajevo"]).to_numpy()
    print(f"Brdskih zona: {brdo.sum()} od {zz.sum()}, stanovnika {Z.stanovnici.to_numpy()[brdo].sum():,.0f}", flush=True)
    m_brdo = (brdo[:, None] | brdo[None, :])

    def t_javni(sc_=None):
        f = np.maximum(fz / 4, 0.5)
        cek = np.minimum(0.5 * 60 / f + 2, 30)
        hod_ = hod.copy()
        voz = D0 * 1.6
        pres = np.where(zrak > 3000, 5.0, 0)
        T = hod_[:, None] + cek[:, None] + voz + pres + hod_[None, :]
        if sc_ in ("B1", "B2"):
            cek_b = np.minimum(cek, 0.5 * 60 / 8 + 1)
            hod_b = np.where(brdo, hod * 0.6, hod)
            pres_b = np.where(zrak > 3000, 2.0, 0)
            T_b = hod_b[:, None] + cek_b[:, None] + voz + pres_b + hod_b[None, :]
            T = np.where(m_brdo, T_b, T)
        return T

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
    dt0 = t_javni(None) - t_auto
    lo, hi = -10.0, 10.0
    for _ in range(60):
        asc = (lo + hi) / 2
        P = 1 / (1 + np.exp(BETA * dt0 + asc))
        sve = Tauto / np.maximum(1 - P, 1e-3)
        udio = (sve * P)[m_int].sum() / sve[m_int].sum()
        lo, hi = (asc, hi) if udio > S0 else (lo, asc)
    P0 = P
    sve0 = Tauto / np.maximum(1 - P0, 1e-3)
    mb = m_int & (brdo[:, None] & ~brdo[None, :])                  # iz brda u dolinu (tipično na posao)
    for sc_ in ("B1", "B2"):
        t_a = t_auto + (np.where(centar, 5.0, 0)[None, :] if sc_ == "B2" else 0)
        P1 = 1 / (1 + np.exp(BETA * (t_javni(sc_) - t_a) + asc))
        f_ = np.where(m_int, (1 - P1) / np.maximum(1 - P0, 1e-3), 1.0)
        rez[sc_] = {"udio_brdo_dolina_danas": float((sve0 * P0)[mb].sum() / sve0[mb].sum()),
                    "udio_brdo_dolina_poslije": float((sve0 * P1)[mb].sum() / sve0[mb].sum()),
                    "auto_iz_brda_promjena_pct": float(((Tauto * f_)[mb].sum() / Tauto[mb].sum() - 1) * 100),
                    "udio_grad_danas": float((sve0 * P0)[m_int].sum() / sve0[m_int].sum()),
                    "udio_grad_poslije": float((sve0 * P1)[m_int].sum() / sve0[m_int].sum()),
                    "auto_grad_promjena_pct": float(((Tauto * f_)[m_int].sum() / Tauto[m_int].sum() - 1) * 100),
                    "faktor": f_}
        r = rez[sc_]
        print(f"{sc_}: brdo → dolina javnim {r['udio_brdo_dolina_danas']:.0%} → {r['udio_brdo_dolina_poslije']:.0%}, "
              f"autom iz brda {r['auto_iz_brda_promjena_pct']:+.0f}%; cijeli grad javnim {r['udio_grad_danas']:.0%} → "
              f"{r['udio_grad_poslije']:.0%}, autom {r['auto_grad_promjena_pct']:+.0f}%", flush=True)

    vh = {}
    pres_all = {}
    eime = e.w.map(lambda q: wmeta[q]["ime"]).to_numpy()
    mid = (xy[e.u] + xy[e.v]) / 2
    eid = csr_matrix((np.arange(1, len(e) + 1), (e.u, e.v)), shape=(n, n))

    def m_xy(lon, lat):
        p = gpd.GeoSeries(gpd.points_from_xy([lon], [lat]), crs=CRS_WGS).to_crs(CRS_M)[0]
        return np.array([p.x, p.y])

    vh["0"] = float((tok0 * t0_).sum() / 60)
    for sc_ in ("B1", "B2"):
        tok1, t1_, _, _ = dodjela(rez[sc_]["faktor"])
        vh[sc_] = float((tok1 * t1_).sum() / 60)
        pres = {}
        for nz, ul, lon, lat in sc.PRESJECI:
            p = m_xy(lon, lat)
            sel = np.where((np.hypot(*(mid - p).T) < 400) & np.array([ul.lower() in s_.lower() for s_ in eime]))[0]
            if not len(sel):
                continue
            j = sel[np.argmax(tok0[sel])]
            rev = eid[e.v[j], e.u[j]]
            v0 = tok0[j] + (tok0[int(rev) - 1] if rev else 0); v1 = tok1[j] + (tok1[int(rev) - 1] if rev else 0)
            if v0 > 0:
                pres[nz] = round(float((v1 / v0 - 1) * 100), 1)
        pres_all[sc_] = pres
        print(f"{sc_}: vozilo-sati {vh['0']:,.0f} → {vh[sc_]:,.0f}; presjeci {pres}", flush=True)
    out = {"brdskih_zona": int(brdo.sum()), "stanovnika_brdo": float(Z.stanovnici.to_numpy()[brdo].sum()),
           "rez": {k: {kk_: round(v, 3) for kk_, v in r.items() if kk_ != "faktor"} for k, r in rez.items()},
           "vozilo_sati": vh, "presjeci": pres_all}
    json.dump(out, open(OUT / "brda_scenarij.json", "w"), ensure_ascii=False, indent=1)
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
