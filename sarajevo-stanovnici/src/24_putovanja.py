"""Model putovanja autom kroz dan, kalibriran na brojače Direkcije za puteve KS.

Ulaz:  raw/Sarajewo.osm.gz, raw/worldpop_2026.tif, out/polja_h3.gpkg, out/radna_mjesta_h3.csv,
       data/radna_mjesta_opcine.csv, data/brojaci_2025*.csv
Izlaz: out/model_dionice.geojson   dnevni promet po dionici (oba smjera i jači smjer), kapacitet
       out/model_brojaci.csv        izbrojano / model po brojaču: faza 1, faza 2, unakrsna provjera
       out/model_info.json          parametri i pokazatelji slaganja

Zone: H3 rezolucija 8 (~0,7 km²) na cijelom području mreže (i Ilidža, Vogošća, Istočno Sarajevo).
  stanovnici: u četiri općine iz modela stanovništva, izvan iz WorldPop-a
  zaposleni stanovnici: udio po općini (ZIS KS 07/2025), izvan 0,32 (kao Ilidža)
  radna mjesta: u četiri općine iz 23_radna_mjesta.py, izvan 0,30 po stanovniku
  ulazi u područje: čvorovi magistralnih, primarnih i sekundarnih cesta na rubu mreže

Putovanja (dnevna, autom, svako putovanje i povratak):
  posao (HBW):  dvostruko ograničen gravitacioni model, exp(-β·t), β = 0,08/min
  ostalo (OTH): izvor stanovnici, cilj radna mjesta + 0,3·stanovnici, β = 0,15/min
  izvana (EXT): s ulaza prema zonama, cilj radna mjesta + 0,5·stanovnici, β = 0,04/min
Dodjela: najbrži put (vrijeme vožnje kao u 08, 65% ograničenja), 5 iteracija MSA s BPR
  zastojem na vršnom satu (8% dnevnog prometa). Faza 1: putovanja na posao fiksno (40% zaposlenih autom,
  tamo i nazad); ostala po stanovniku i izvana po ulazu iz najmanjih kvadrata na brojačima.
  Šest brojača broji samo jedan smjer (SMJER_BROJANJA) i porede se samo s tim smjerom.
  Faza 2: lokalna korekcija: na ulici brojača (isti naziv, do 2,5 km, u smjeru brojanja) tok se
  množi omjerom brojač/model najbližeg brojača, pa se model na brojačima poklapa; ostale ceste
  ostaju na modelu putovanja. (Procjena matrice iz brojanja, ODME, je isprobana i odbačena: na
  izostavljenom brojaču bila je lošija od faze 1.) Unakrsna provjera: svaki brojač izostavljen
  i procijenjen iz modela i ostalih brojača (koliko vrijedi tamo gdje nema brojača).
"""
from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path

import geopandas as gpd
import h3
import numpy as np
import pandas as pd
import rasterio
from rasterio.features import geometry_mask
from scipy.optimize import nnls
from scipy.sparse import coo_matrix, csr_matrix, identity
from scipy.sparse.csgraph import connected_components, dijkstra
from scipy.sparse.linalg import spsolve_triangular
from scipy.spatial import cKDTree
from shapely.geometry import LineString, Point, box

from common import CRS_M, CRS_WGS, DATA, OUT, RAW, ucitaj_granice


def _uvezi(ime, fajl):
    s = importlib.util.spec_from_file_location(ime, Path(__file__).with_name(fajl))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


dost = _uvezi("dost", "08_dostupnost.py")
guz = _uvezi("guz", "22_guzva.py")

OKVIR = (18.242, 43.768, 18.515, 43.935)   # granice OSM ekstrakta
H3Z = 8
BETA = {"hbw": 0.08, "oth": 0.15, "ext": 0.04}
UDIO_VRSNOG_SATA = 0.08
KAP_TRAKA = {"motorway": 1800, "motorway_link": 1200, "trunk": 1000, "trunk_link": 800}
KAP_GRAD = 800
KAP_LOKALNA = 500
GLAVNE = {"motorway", "trunk", "primary", "secondary", "tertiary", "motorway_link", "trunk_link",
          "primary_link", "secondary_link", "tertiary_link"}
ULAZ_TEZINA = {"motorway": 1.0, "trunk": 1.0, "primary": 0.6, "secondary": 0.3}
import os
# brojači koji broje samo jedan kolovoz/smjer (publikacija: "pravac" i "profil saobraćajnice")
SMJER_BROJANJA = {"KSBS03": "E", "KSBS04": "W", "KSBS05": "W", "KSBS06": "E", "KSBS17": "E", "KSBS24": "E"}
# položaj: KSBS22 nema koordinate u publikaciji (približno, Džemala Bijedića kod "Žice");
# KSBS27 je na poprečnoj ulici bez naziva (XI transferzala), ne na Džemala Bijedića
TACKA = {"KSBS22": ("Džemala Bijedića", (43.8452, 18.3470)), "KSBS27": ("*", None)}
MSA_ITER = int(os.environ.get("MSA_ITER", 5))
ODME_ITER = 40
KOREKCIJA_M = 2500
NESIGURNA_LOKACIJA = {"KSBS22"}   # publikacija nema koordinate; tačka je približna
AUTOM_NA_POSAO = 0.4
R_RUTA = int(os.environ.get("R_RUTA", 4))
SIGMA_RUTA = 0.3


# ---------------------------------------------------------------- mreža
def mreza():
    nodes, ways, _ = dost.ucitaj_mrezu(RAW / "Sarajewo.osm.gz")
    rows = []
    wmeta = []
    for wi, (t, nds) in enumerate(ways):
        v = dost.brzina(t) * dost.FAKTOR_GRADSKE_VOZNJE
        if v <= 0 or t.get("motor_vehicle") == "no" or t.get("access") in ("no", "private"):
            continue
        if t.get("service") in ("parking_aisle", "driveway", "drive-through"):
            continue
        ow = t.get("oneway")
        jedno = 1 if ow in ("yes", "1", "true") or (t.get("junction") == "roundabout" and ow != "no") \
            or t["highway"] == "motorway" else (-1 if ow == "-1" else 0)
        m = re.match(r"\d+", t.get("lanes", ""))
        trake = int(m[0]) if m else None
        hw = t["highway"]
        if trake is None:
            trake = (2 if hw in ("motorway", "trunk", "primary") else 1) if jedno else \
                (4 if hw in ("motorway", "trunk", "primary") else 2)
        trake_smjer = max(1, trake if jedno else trake // 2)
        kap = trake_smjer * KAP_TRAKA.get(hw, KAP_GRAD if hw in GLAVNE else KAP_LOKALNA)
        nds = [n for n in nds if n in nodes]
        if len(nds) < 2:
            continue
        wmeta.append({"wi": wi, "hw": hw, "ime": t.get("name", ""), "jedno": jedno, "kap": kap,
                      "nds": nds, "v": v})
    used = sorted({n for w in wmeta for n in w["nds"]})
    idx = {n: k for k, n in enumerate(used)}
    ll = np.array([nodes[n] for n in used])
    pts = gpd.GeoSeries(gpd.points_from_xy(ll[:, 0], ll[:, 1]), crs=CRS_WGS).to_crs(CRS_M)
    xy = np.c_[pts.x, pts.y]
    eu, ev, et, ew, ek = [], [], [], [], []
    for k, w in enumerate(wmeta):
        for a, b in zip(w["nds"][:-1], w["nds"][1:]):
            i, j = idx[a], idx[b]
            if i == j:
                continue
            mins = float(np.hypot(*(xy[i] - xy[j]))) / 1000 / w["v"] * 60
            if w["jedno"] >= 0:
                eu.append(i); ev.append(j); et.append(mins); ew.append(k); ek.append(w["kap"])
            if w["jedno"] <= 0:
                eu.append(j); ev.append(i); et.append(mins); ew.append(k); ek.append(w["kap"])
    e = pd.DataFrame({"u": eu, "v": ev, "t0": et, "w": ew, "kap": ek})
    e = e.sort_values("t0").drop_duplicates(["u", "v"]).reset_index(drop=True)
    return wmeta, xy, ll, e, idx


def graf(e, n, t):
    return csr_matrix((t, (e.u.to_numpy(), e.v.to_numpy())), shape=(n, n))


# ---------------------------------------------------------------- zone
def zone(xy, ll, e, wmeta):
    polja = gpd.read_file(OUT / "polja_h3.gpkg")
    rm = pd.read_csv(OUT / "radna_mjesta_h3.csv").set_index("h3_id").radna_mjesta
    kz = pd.read_csv(DATA / "radna_mjesta_opcine.csv").set_index("opcina")
    pop_op = polja.groupby("opcina").stanovnici.sum()
    udio_zap = (kz.zaposleni_stanovnici_2025 / pop_op.reindex(kz.index)).to_dict()
    polja["z"] = [h3.cell_to_parent(h, H3Z) for h in polja.h3_id]
    polja["zap"] = polja.stanovnici * polja.opcina.map(udio_zap).fillna(0.32)
    polja["rm"] = rm.reindex(polja.h3_id).fillna(0).to_numpy()
    unutra = polja.groupby("z")[["stanovnici", "zap", "rm"]].sum()

    # WorldPop izvan četiri općine, u okviru mreže
    opcine, _ = ucitaj_granice()
    cetiri = opcine.to_crs(CRS_WGS).union_all()
    with rasterio.open(RAW / "worldpop_2026.tif") as s:
        win = rasterio.windows.from_bounds(*OKVIR, transform=s.transform).round_offsets().round_lengths()
        a = s.read(1, window=win).astype(float)
        tr = s.window_transform(win)
    a[a < 0] = 0
    m_in = ~geometry_mask([cetiri], out_shape=a.shape, transform=tr)
    a[m_in] = 0
    rr, cc = np.nonzero(a > 0)
    lon = tr.c + (cc + 0.5) * tr.a
    lat = tr.f + (rr + 0.5) * tr.e
    vani = pd.DataFrame({"z": [h3.latlng_to_cell(y, x, H3Z) for x, y in zip(lon, lat)], "stanovnici": a[rr, cc]})
    vani = vani.groupby("z").stanovnici.sum().to_frame()
    vani["zap"] = 0.32 * vani.stanovnici
    vani["rm"] = 0.30 * vani.stanovnici
    z = unutra.add(vani, fill_value=0)
    z = z[(z.stanovnici + z.rm) >= 30].copy()
    print(f"Zone: {len(z)} (H3 {H3Z}); stanovnici {z.stanovnici.sum():,.0f} (izvan 4 općine "
          f"{vani.stanovnici.sum():,.0f}), radna mjesta {z.rm.sum():,.0f}")

    # čvor zone: najbliži čvor ulice (residential ili veća) u glavnoj jako povezanoj komponenti
    n = len(xy)
    G = graf(e, n, e.t0.to_numpy())
    _, lab = connected_components(G, directed=True, connection="strong")
    glavna = lab == np.bincount(lab).argmax()
    ok_hw = {"residential", "unclassified", "living_street"} | GLAVNE
    cv_ok = np.zeros(n, bool)
    uvz = set(e.u[e.w.map(lambda k: wmeta[k]["hw"] in ok_hw)]) | set(e.v[e.w.map(lambda k: wmeta[k]["hw"] in ok_hw)])
    cv_ok[list(uvz)] = True
    cv_ok &= glavna
    kand = np.where(cv_ok)[0]
    tk = cKDTree(xy[kand])
    cz = np.array([h3.cell_to_latlng(h) for h in z.index])
    czm = gpd.GeoSeries(gpd.points_from_xy(cz[:, 1], cz[:, 0]), crs=CRS_WGS).to_crs(CRS_M)
    _, iz = tk.query(np.c_[czm.x, czm.y])
    z["cvor"] = kand[iz]
    z["tip"] = "zona"

    # ulazi: čvorovi glavnih cesta blizu ruba okvira
    x0, y0, x1, y1 = OKVIR
    rub = (np.minimum.reduce([ll[:, 0] - x0, x1 - ll[:, 0], ll[:, 1] - y0, y1 - ll[:, 1]]) < 0.004) & glavna
    ul = []
    ehw = e.w.map(lambda k: wmeta[k]["hw"])
    for cv, hw in zip(np.r_[e.u, e.v], np.r_[ehw, ehw]):
        if rub[cv] and hw in ULAZ_TEZINA:
            ul.append((cv, ULAZ_TEZINA[hw]))
    ul = pd.DataFrame(ul, columns=["cvor", "tez"]).groupby("cvor").tez.max().reset_index()
    # spoji ulaze bliže od 1,5 km (ista cesta)
    keep = []
    for r in ul.sort_values("tez", ascending=False).itertuples():
        if all(np.hypot(*(xy[r.cvor] - xy[k])) > 1500 for k, _ in keep):
            keep.append((r.cvor, r.tez))
    ulazi = pd.DataFrame(keep, columns=["cvor", "tez"])
    ulazi.index = [f"ulaz_{i}" for i in range(len(ulazi))]
    ulazi["tip"] = "ulaz"
    for c in ("stanovnici", "zap", "rm"):
        ulazi[c] = 0.0
    print(f"Ulazi u područje: {len(ulazi)}: " + ", ".join(
        f"{ll[c][1]:.3f},{ll[c][0]:.3f} ({t})" for c, t in zip(ulazi.cvor, ulazi.tez)))
    return pd.concat([z, ulazi])


# ---------------------------------------------------------------- matrice
def furness(f, P, A, it=30):
    T = f.copy()
    for _ in range(it):
        T *= (P / np.maximum(T.sum(axis=1), 1e-9))[:, None]
        T *= (A / np.maximum(T.sum(axis=0), 1e-9))[None, :]
    return T


def matrice(Z, C):
    """Jedinične matrice (po 1 putovanju po zaposlenom / stanovniku / jedinici ulaza), oba smjera."""
    zz = (Z.tip == "zona").to_numpy()
    uu = ~zz
    P_w, A_w = Z.zap.to_numpy() * zz, Z.rm.to_numpy() * zz
    A_w = A_w * P_w.sum() / A_w.sum()
    f = np.exp(-BETA["hbw"] * C) * np.outer(zz, zz)
    np.fill_diagonal(f, f.diagonal() * 0.5)
    Tw = furness(f, P_w, A_w)
    pop = Z.stanovnici.to_numpy() * zz
    Ao = (Z.rm.to_numpy() + 0.3 * pop) * zz
    fo = Ao[None, :] * np.exp(-BETA["oth"] * C) * np.outer(zz, zz)
    To = fo / np.maximum(fo.sum(axis=1, keepdims=True), 1e-12) * pop[:, None]
    Ae = (Z.rm.to_numpy() + 0.5 * pop) * zz
    fe = Ae[None, :] * np.exp(-BETA["ext"] * C) * np.outer(uu, zz)
    Te = fe / np.maximum(fe.sum(axis=1, keepdims=True), 1e-12) * Z.tez.fillna(0).to_numpy()[:, None]
    return {k: T + T.T for k, T in (("hbw", Tw), ("oth", To), ("ext", Te))}


# ---------------------------------------------------------------- dodjela
def stabla(G, izvori):
    return dijkstra(G, indices=izvori, return_predecessors=True)


def dubina(pred):
    """Broj grana od izvora do čvora (pointer doubling); nedostižni i izvor = 0."""
    n = len(pred)
    akt = pred >= 0
    jump = np.where(akt, pred, np.arange(n))
    d = akt.astype(np.int32)
    for _ in range(22):
        d = d + d[jump]
        jump = jump[jump]
    return d


def dodijeli(P, cv, Ts, eid, n):
    """Tokovi po granama (sve ili ništa) za listu matrica Ts po stablima P (red = izvor).
    Protok kroz granu pred(v)->v = potražnja u podstablu v; zbraja se po nivoima, od najdubljeg."""
    tok = np.zeros((eid.nnz + 1, len(Ts)))
    for o in range(P.shape[0]):
        pred = P[o]
        v = np.where(pred >= 0)[0]
        if not len(v):
            continue
        x = np.zeros((n, len(Ts)))
        for k, T in enumerate(Ts):
            np.add.at(x[:, k], cv, T[o])
        dub = dubina(pred)
        red = v[np.argsort(-dub[v], kind="stable")]
        dr = dub[red]
        granice = np.r_[0, np.nonzero(np.diff(dr))[0] + 1, len(red)]
        for a_, b_ in zip(granice[:-1], granice[1:]):
            sel = red[a_:b_]
            np.add.at(x, pred[sel], x[sel])
        ids = np.asarray(eid[pred[v], v]).ravel().astype(int)
        np.add.at(tok, ids, x[v])
    return [tok[1:, k] for k in range(len(Ts))]


def incidencija(P, cv, eid, e_brojac, nb):
    """inc[o, d, c] = put od zone o do zone d prolazi kroz brojač c."""
    nz = P.shape[0]
    inc = np.zeros((nz, nz, nb), bool)
    for o in range(nz):
        pred = P[o]
        v = np.where(pred >= 0)[0]
        cn = np.full(len(pred), -1)
        ids = np.asarray(eid[pred[v], v]).ravel().astype(int) - 1
        cn[v] = e_brojac[ids]
        cur = cv.copy()
        dd = np.arange(nz)
        akt = pred[cur] >= 0
        while akt.any():
            c = cn[cur[akt]]
            h = c >= 0
            inc[o, dd[akt][h], c[h]] = True
            cur = np.where(akt, pred[np.maximum(cur, 0)], cur)
            akt = akt & (cur >= 0)
            akt[akt] = pred[cur[akt]] >= 0
    return inc


def main() -> None:
    wmeta, xy, ll, e, idx = mreza()
    n = len(xy)
    print(f"Mreža: {n:,} čvorova, {len(e):,} grana")
    Z = zone(xy, ll, e, wmeta)
    cv = Z.cvor.to_numpy()
    eid = csr_matrix((np.arange(1, len(e) + 1), (e.u, e.v)), shape=(n, n))

    # brojači -> grane
    br = pd.read_csv(DATA / "brojaci_2025.csv")
    for k_, (_, p) in list(guz.ULICA.items()) + list(TACKA.items()):
        if p:
            br.loc[br.brojac == k_, ["lat", "lon"]] = p
    br = br.dropna(subset=["lat", "lon"])
    br = br[(br.lon.between(OKVIR[0], OKVIR[2])) & (br.lat.between(OKVIR[1], OKVIR[3]))].reset_index(drop=True)
    bxy = gpd.GeoSeries(gpd.points_from_xy(br.lon, br.lat), crs=CRS_WGS).to_crs(CRS_M)
    mid = (xy[e.u] + xy[e.v]) / 2
    ehw = e.w.map(lambda k: wmeta[k]["hw"]).to_numpy()
    eime = e.w.map(lambda k: wmeta[k]["ime"]).to_numpy()
    # kandidati: grane iste ulice (ili glavne ceste) do 100 m od brojača; po smjeru se kasnije bira
    # grana s najvećim tokom (brojač broji cijeli presjek ceste, oba kolovoza)
    smjer = xy[e.v] - xy[e.u]
    smjer = smjer / np.maximum(np.linalg.norm(smjer, axis=1, keepdims=True), 1e-9)
    grane_br = []
    for i, r in br.iterrows():
        ul = TACKA.get(r.brojac, guz.ULICA.get(r.brojac, (None, None)))[0]
        p = np.array([bxy.x[i], bxy.y[i]])
        dist = np.hypot(*(mid - p).T)
        maska = np.isin(ehw, list(GLAVNE)) if ul != "*" else np.ones(len(e), bool)
        if ul and ul != "*":
            maska &= np.array([ul.lower() in s.lower() for s in eime])
        dist = np.where(maska, dist, np.inf)
        j = int(dist.argmin())
        if dist[j] > (600 if ul and ul != "*" else 150):
            print(f"{r.brojac}: nema grane ({dist[j]:.0f} m)"); grane_br.append(None); continue
        ista = (eime == eime[j]) if eime[j] else (ehw == ehw[j])
        kand = np.where(ista & (np.hypot(*(mid - mid[j]).T) <= 100))[0]
        sm = SMJER_BROJANJA.get(r.brojac)
        if sm:
            dx = smjer[kand, 0]
            grane_br.append((kand[dx > 0.3],) if sm == "E" else (kand[dx < -0.3],))
        else:
            cos = smjer[kand] @ smjer[j]
            grane_br.append((kand[cos > 0.3], kand[cos < -0.3]))
    br["grane"] = grane_br
    br["index_src"] = np.arange(len(br))
    bxy_m = bxy
    br = br[br.grane.notna()].reset_index(drop=True)
    kandidati = list(br.grane)
    y = br.pgds_2025.to_numpy(float)
    print(f"Brojači u modelu: {len(br)}")

    # ---- MSA s fazom 1; svaka iteracija = R dodjela sa slučajno izmijenjenim vremenima (više ruta)
    rng = np.random.default_rng(1)
    t = e.t0.to_numpy().copy()
    tok = np.zeros(len(e))
    kap = e.kap.to_numpy(float)
    K3 = ("hbw", "oth", "ext")
    for it in range(1, MSA_ITER + 1):
        D, _ = stabla(graf(e, n, t), cv)
        C = D[:, cv]
        C[~np.isfinite(C)] = 1e3
        mats = matrice(Z, C)
        Ps, F = [], {k: 0 for k in K3}
        for _ in range(R_RUTA):
            _, P = stabla(graf(e, n, t * rng.lognormal(0, SIGMA_RUTA, len(t))), cv)
            Ps.append(P)
            for k, f_ in zip(K3, dodijeli(P, cv, [mats[k] for k in K3], eid, n)):
                F[k] = F[k] + f_ / R_RUTA
        if it == 1:
            # brojač: po smjeru grana s najvećim tokom među kandidatima
            br["grane"] = [sorted({int(g[np.argmax(F["oth"][g])]) for g in kk if len(g)}) for kk in kandidati]
        X = np.c_[[[F[k][g].sum() for k in K3] for g in br.grane]]
        w = 1 / np.sqrt(y)
        # posao i ostalo imaju skoro isti prostorni raspored (kolinearni), pa se posao ne procjenjuje:
        # AUTOM_NA_POSAO zaposlenih ide autom (tamo i nazad), ostalo i izvana iz brojača
        yr = y - AUTOM_NA_POSAO * X[:, 0]
        k2, _ = nnls(X[:, 1:] * w[:, None], yr * w)
        koef = np.r_[AUTOM_NA_POSAO, k2]
        novi = sum(c * F[k] for c, k in zip(koef, K3))
        tok = novi if it == 1 else tok + (novi - tok) / it
        t = e.t0.to_numpy() * (1 + 0.15 * (tok * UDIO_VRSNOG_SATA / kap) ** 4)
        m1 = X @ koef
        if os.environ.get("DIJAG"):
            print(pd.DataFrame(X.round(0), columns=list(K3)).assign(
                brojac=br.brojac, izbrojano=y, model=m1.round()).to_string(index=False))
        print(f"MSA {it}: koef posao {koef[0]:.2f}/zaposlenom, ostalo {koef[1]:.2f}/stanovniku, "
              f"izvana {koef[2]:,.0f}/ulaz; R² {1 - ((y - m1) ** 2).sum() / ((y - y.mean()) ** 2).sum():.2f}")
    m_faza1 = np.array([tok[g].sum() for g in br.grane])
    T = sum(c * mats[k] for c, k in zip(koef, K3))

    # ---- faza 2: lokalna korekcija uz brojače. Procjena matrice iz brojanja (ODME) je isprobana
    # (6 jačina): poklapa brojače, ali unakrsna provjera na izostavljenom brojaču bila je lošija nego
    # bez nje (medijan 42–50% prema 28%), pa se ne koristi. Umjesto toga: tok na ulici brojača
    # (isti naziv, do KOREKCIJA_M, u smjeru koji brojač broji) množi se omjerom brojač/model
    # najbližeg brojača; ostale ceste ostaju na modelu putovanja.
    omjer = y / np.maximum(m_faza1, 1)
    bpt = np.c_[bxy_m.x, bxy_m.y][br.index_src.to_numpy()]
    faktor = np.ones(len(e))
    dmin = np.full(len(e), np.inf)
    vlasnik = np.full(len(e), -1)
    ulice = []
    for c, g in enumerate(br.grane):
        ime = eime[g[0]]
        dist = np.hypot(*(mid - bpt[c]).T)
        sel = (eime == ime) & (dist <= KOREKCIJA_M) if ime else (ehw == ehw[g[0]]) & (dist <= 300)
        sm = SMJER_BROJANJA.get(br.brojac[c])
        if sm:
            sel &= (smjer[:, 0] > 0.3) if sm == "E" else (smjer[:, 0] < -0.3)
        sel[g] = True
        ulice.append(sel)
    def faktori(aktivni):
        f_ = np.ones(len(e)); dm = np.full(len(e), np.inf); vl = np.full(len(e), -1)
        for c, sel in enumerate(ulice):
            if not aktivni[c]:
                continue
            dist = np.hypot(*(mid - bpt[c]).T)
            bolje = sel & (dist < dm)
            f_[bolje], dm[bolje], vl[bolje] = omjer[c], dist[bolje], c
        return f_, vl
    aktivni = ~br.brojac.isin(NESIGURNA_LOKACIJA).to_numpy()
    faktor, vlasnik = faktori(aktivni)
    tok_kon = tok * faktor
    m_faza2 = np.array([tok_kon[g].sum() for g in br.grane])
    loo = np.zeros(len(br))
    for c in range(len(br)):
        a_ = aktivni.copy(); a_[c] = False
        f_, _ = faktori(a_)
        loo[c] = (tok * f_)[br.grane[c]].sum()

    def pok(m):
        gre = (m - y) / y
        geh = np.sqrt(2 * (m / 24 - y / 24) ** 2 / (m / 24 + y / 24))
        return {"R2": round(float(1 - ((y - m) ** 2).sum() / ((y - y.mean()) ** 2).sum()), 3),
                "srednja_aps_greska_pct": round(float(np.abs(gre).mean() * 100), 1),
                "medijan_aps_greska_pct": round(float(np.median(np.abs(gre)) * 100), 1),
                "GEH_satni_<5_udio": round(float((geh < 5).mean()), 2)}

    info = {"odme_odbacen": "procjena matrice iz brojanja: unakrsni medijan 42–50% (lošije od faze 1)",
            "faza1": pok(m_faza1), "faza2": pok(m_faza2), "unakrsna": pok(loo),
            "koef": dict(zip(("posao_po_zaposlenom", "ostalo_po_stanovniku", "izvana_po_ulazu"),
                             map(float, koef))),
            "putovanja_dnevno": {"posao": float((koef[0] * mats["hbw"]).sum() / 2),
                                 "ostalo": float((koef[1] * mats["oth"]).sum() / 2),
                                 "izvana": float((koef[2] * mats["ext"]).sum() / 2),
                                 }}
    print(json.dumps(info, indent=1, ensure_ascii=False))
    br_out = br[["brojac", "lokacija", "lat", "lon", "pgds_2025"]].assign(
        model_faza1=m_faza1.round(), model=m_faza2.round(), unakrsna=loo.round(),
        korigovan=aktivni)
    br_out.to_csv(OUT / "model_brojaci.csv", index=False)
    print(br_out.drop(columns=["lat", "lon"]).to_string(index=False))
    json.dump(info, open(OUT / "model_info.json", "w"), ensure_ascii=False, indent=1)

    # po dionici (OSM way): oba smjera i jači smjer
    e["tok"] = tok_kon
    e["smjer"] = np.where(e.u < e.v, 0, 1)
    pw = e.groupby(["w", "smjer"]).tok.mean().unstack(fill_value=0)
    rows = []
    for k_, r in pw.iterrows():
        w = wmeta[k_]
        uk = float(r.sum())
        if w["hw"] not in GLAVNE and uk < 1500:
            continue
        rows.append({"klasa": guz.KLASA.get(w["hw"], "ulica"), "ime": w["ime"], "dnevno": round(uk),
                     "jaci_smjer": round(float(r.max())), "jednosmjerna": bool(w["jedno"]),
                     "kap_smjer": w["kap"], "geometry": LineString([ll[idx[nd]] for nd in w["nds"]])})
    out = gpd.GeoDataFrame(rows, crs=CRS_WGS)
    out["geometry"] = out.to_crs(CRS_M).simplify(4).to_crs(CRS_WGS)
    out.to_file(OUT / "model_dionice.geojson", driver="GeoJSON", COORDINATE_PRECISION=5)
    print(f"-> out/model_dionice.geojson ({len(out)} dionica)")


if __name__ == "__main__":
    main()
