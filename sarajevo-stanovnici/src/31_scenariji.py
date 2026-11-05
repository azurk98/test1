"""Scenariji novih cesta i tunela u modelu putovanja (24): ušteda vremena i rasterećenje uskih grla.

Za svaki scenarij se mreži dodaju nove dionice (ili se postojeće nadograde), pa se ista dnevna
matrica putovanja autom (faza 1 iz 24, koeficijenti iz model_info.json) dodijeli s MSA (zastoj, BPR)
i nekoliko ruta. Poređenje s osnovnim stanjem uz iste parametre i iste slučajne brojeve.
Pokazatelji: vozilo-sati dnevno, dnevni tok na mjernim presjecima (oba smjera), tok na novoj
dionici, vrijeme vožnje za izabrane parove (vršni sat, zastoj).
Ideje su koncepti za raspravu, ne projekti: trase, cijene, geologija i vlasništvo nisu provjereni.
Izlaz: out/scenariji.csv, out/scenariji_presjeci.csv, out/scenariji.geojson
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import geopandas as gpd
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

MSA = 3
RUTA = 2
GLAVNE = {"motorway", "trunk", "primary", "secondary", "tertiary", "motorway_link", "trunk_link",
          "primary_link", "secondary_link", "tertiary_link"}

# novi spojevi: (naziv, [(lon, lat), ...] tačke trase, brzina km/h, traka po smjeru)
SCENARIJI = {
    # A (tunel ispod Bistrika) odbačen na zahtjev korisnika; P je već planirani tunel (provjera efekta)
    "P": ("Planirani tunel Bentbaša – Koševo (ispod Bjelava, prema tunelu Ciglane)", [[(18.4380, 43.8590), (18.4140, 43.8665)]], 50, 2),
    "B": ("Sjeverna brdska veza: Zabrđe – Sokolje – Buća Potok – Pofalići – Velešići", "sjeverna", 40, 1),
    "C": ("Tunel ispod Mojmila: Alipašino Polje – Dobrinja", [[(18.3505, 43.8430), (18.3500, 43.8325)]], 50, 2),
    "C2": ("Tunel ispod Mojmila, istočnije: Alipašino Polje (istok) – Dobrinja I", [[(18.3590, 43.8440), (18.3600, 43.8305)]], 50, 2),
    "C3": ("Tunel Hrasno – istočna Dobrinja (prema Lukavici)", [[(18.3720, 43.8440), (18.3700, 43.8305)]], 50, 2),
    # pravci za putovanje na posao zapad -> centar
    "G": ("Produžetak Gradskog autoputa uz prugu: Drinska (Pofalići) – Željeznička – Marijin Dvor",
          [[(18.3826, 43.8579), (18.3920, 43.8590), (18.4000, 43.8585), (18.4085, 43.8565)]], 60, 2),
    "S": ("Sjeverna longitudinala: Put života (Pofalići) – Koševo", [[(18.3883, 43.8570), (18.3990, 43.8640), (18.4080, 43.8700)]], 50, 2),
    # planirane transverzale (trase približne, prema opisima u medijima)
    "T1": ("Prva transverzala: Pofalići (Ambasada SAD) – Željeznička – Koševsko brdo/Velešići – Kobilja Glava",
           [[(18.3890, 43.8556), (18.3990, 43.8590), (18.4025, 43.8680), (18.3985, 43.8790), (18.3940, 43.8845)]], 50, 2),
    "T6": ("Šesta transverzala: Hrasno – Čengić Vila – Buća Potok – Hotonj",
           [[(18.3745, 43.8445), (18.3705, 43.8515), (18.3715, 43.8580), (18.3725, 43.8650), (18.3760, 43.8760), (18.3770, 43.8850)]], 50, 2),
    "T16": ("Prva i Šesta transverzala zajedno",
            [[(18.3890, 43.8556), (18.3990, 43.8590), (18.4025, 43.8680), (18.3985, 43.8790), (18.3940, 43.8845)],
             [(18.3745, 43.8445), (18.3705, 43.8515), (18.3715, 43.8580), (18.3725, 43.8650), (18.3760, 43.8760), (18.3770, 43.8850)]], 50, 2),
    "SP": ("Sjeverni obilazak: Put života – Koševo + planirani tunel Koševo – Bentbaša",
           [[(18.3883, 43.8570), (18.3990, 43.8640), (18.4080, 43.8700)], [(18.4140, 43.8665), (18.4380, 43.8590)]], 50, 2),
}
# mjerni presjeci: (naziv, ulica u OSM-u, lon, lat)
PRESJECI = [("Obala Kulina bana", "Obala Kulina bana", 18.4160, 43.8566), ("Maršala Tita", "Maršala Tita", 18.4166, 43.8590),
            ("Zmaja od Bosne (Čengić Vila)", "Zmaja od Bosne", 18.3742, 43.8510),
            ("Bulevar Meše Selimovića", "Meše Selimovića", 18.3423, 43.8453), ("Alipašina", "Alipašina", 18.4076, 43.8705),
            ("Safeta Zajke", "Safeta Zajke", 18.3421, 43.8521), ("Džemala Bijedića", "Džemala Bijedića", 18.3600, 43.8470)]
PAROVI = [("Velešići → Zabrđe", (18.4015, 43.8655), (18.3097, 43.8741)),
          ("Dobrinja → Alipašino Polje", (18.3470, 43.8290), (18.3480, 43.8450)),
          ("Alipašin most → Bentbaša", (18.3475, 43.8480), (18.4380, 43.8586)),
          ("Koševo → Bentbaša", (18.4100, 43.8700), (18.4380, 43.8586)),
          ("Dobrinja I → Hrasno", (18.3600, 43.8300), (18.3720, 43.8450)),
          ("Alipašin most → Marijin Dvor", (18.3475, 43.8480), (18.4100, 43.8560)),
          ("Pale (ulaz) → Marijin Dvor", (18.5130, 43.8510), (18.4100, 43.8560))]


def main() -> None:
    wmeta, xy, ll, e0, idx = mp.mreza()
    n = len(xy)
    Z = mp.zone(xy, ll, e0, wmeta)
    cv = Z.cvor.to_numpy()
    info = json.load(open(OUT / "model_info.json"))
    k = info["koef"]
    kk = (k["posao_po_zaposlenom"], k["ostalo_po_stanovniku"], k["izvana_po_ulazu"])
    ehw = e0.w.map(lambda q: wmeta[q]["hw"]).to_numpy()
    eime = e0.w.map(lambda q: wmeta[q]["ime"]).to_numpy()
    glavni_cv = np.unique(np.r_[e0.u[np.isin(ehw, list(GLAVNE))], e0.v[np.isin(ehw, list(GLAVNE))]])
    tg = cKDTree(xy[glavni_cv])
    # samo čvorovi glavne jako povezane komponente (spojevi se ne smiju vezati za izolovane puteve)
    from scipy.sparse.csgraph import connected_components
    _, lab = connected_components(mp.graf(e0, n, e0.t0.to_numpy()), directed=True, connection="strong")
    sve_cv = np.where(lab == np.bincount(lab).argmax())[0]; ta = cKDTree(xy[sve_cv])
    glavni_cv = np.intersect1d(glavni_cv, sve_cv); tg = cKDTree(xy[glavni_cv])

    def m_xy(lon, lat):
        p = gpd.GeoSeries([Point(lon, lat)], crs=CRS_WGS).to_crs(CRS_M)[0]
        return np.array([p.x, p.y])

    def nove_dionice(sc):
        """Vrati DataFrame dodatnih grana (u, v, t0, w=-1, kap) i geometrije za kartu."""
        naziv, trase, v, trake = SCENARIJI[sc]
        rows, geoms = [], []
        if trase == "sjeverna":
            # nadogradnja: grane duž trase linije S dobiju brzinu v i 1 traku po smjeru; + spojevi N6, N4 iz 30
            g = gpd.read_file(OUT / "sjeverna_linija.geojson").to_crs(CRS_M).geometry.iloc[0]
            mid = (xy[e0.u] + xy[e0.v]) / 2
            uz = gpd.GeoSeries(gpd.points_from_xy(mid[:, 0], mid[:, 1]), crs=CRS_M).distance(g).to_numpy() < 8
            nadogr = np.where(uz)[0]
            dg = gpd.read_file(OUT / "dogradnje.geojson").to_crs(CRS_M)
            for nid in ("N6", "N4"):
                sel = dg[(dg.tip == "spoj") & (dg.id == nid)]
                if len(sel):
                    trase_n = [list(sel.geometry.iloc[0].coords)]
                    for t in trase_n:
                        a = sve_cv[ta.query(t[0])[1]]; b = sve_cv[ta.query(t[-1])[1]]
                        L = float(np.hypot(*(xy[a] - xy[b])))
                        tt = L / 1000 / (v * mp.dost.FAKTOR_GRADSKE_VOZNJE) * 60
                        rows += [(a, b, tt, -1, 800), (b, a, tt, -1, 800)]
                        geoms.append(LineString([xy[a], xy[b]]))
            geoms.append(g)
            return pd.DataFrame(rows, columns=["u", "v", "t0", "w", "kap"]), nadogr, geoms
        for t in trase:
            pts = [m_xy(*p) for p in t]
            cvs = [glavni_cv[tg.query(p)[1]] for p in pts]
            for a, b in zip(cvs[:-1], cvs[1:]):
                L = float(np.hypot(*(xy[a] - xy[b])))
                tt = L / 1000 / v * 60                       # tunel: bez semafora, puna brzina
                rows += [(a, b, tt, -1, trake * 1800), (b, a, tt, -1, trake * 1800)]
                geoms.append(LineString([xy[a], xy[b]]))
        return pd.DataFrame(rows, columns=["u", "v", "t0", "w", "kap"]), np.array([], int), geoms

    def pokreni(sc):
        e = e0.copy()
        dod, nadogr, geoms = (pd.DataFrame(columns=["u", "v", "t0", "w", "kap"]), np.array([], int), []) if sc == "0" else nove_dionice(sc)
        if len(nadogr):
            v = SCENARIJI[sc][2] * mp.dost.FAKTOR_GRADSKE_VOZNJE
            duz = np.hypot(*(xy[e.u.to_numpy()[nadogr]] - xy[e.v.to_numpy()[nadogr]]).T)
            e.loc[nadogr, "t0"] = np.minimum(e.t0.to_numpy()[nadogr], duz / 1000 / v * 60)
            e.loc[nadogr, "kap"] = np.maximum(e.kap.to_numpy()[nadogr], 800)
        nova0 = len(e)
        if len(dod):
            e = pd.concat([e, dod.astype({"u": int, "v": int})], ignore_index=True)
        from scipy.sparse import csr_matrix
        eid = csr_matrix((np.arange(1, len(e) + 1), (e.u, e.v)), shape=(n, n))
        rng = np.random.default_rng(7)
        t = e.t0.to_numpy().copy(); tok = np.zeros(len(e)); kap = e.kap.to_numpy(float)
        for it in range(1, MSA + 1):
            D, _ = mp.stabla(mp.graf(e, n, t), cv)
            C = D[:, cv]; C[~np.isfinite(C)] = 1e3
            mats = mp.matrice(Z, C)
            T = sum(c * mats[q] for c, q in zip(kk, ("hbw", "oth", "ext")))
            F = np.zeros(len(e))
            for _ in range(RUTA):
                _, P = mp.stabla(mp.graf(e, n, t * rng.lognormal(0, mp.SIGMA_RUTA, len(t))), cv)
                F += mp.dodijeli(P, cv, [T], eid, n)[0] / RUTA
            tok = F if it == 1 else tok + (F - tok) / it
            t = e.t0.to_numpy() * (1 + 0.15 * (tok * mp.UDIO_VRSNOG_SATA / kap) ** 4)
        vh = float((tok * t).sum() / 60)                                     # vozilo-sati dnevno
        # presjeci: max zbir oba smjera na grani te ulice do 150 m od tačke
        mid = (xy[e.u] + xy[e.v]) / 2
        ime_e = np.r_[eime, np.array([""] * (len(e) - len(eime)))]
        pres = {}
        for nz, ul, lon, lat in PRESJECI:
            p = m_xy(lon, lat)
            sel = np.where((np.hypot(*(mid - p).T) < 400) & np.array([ul.lower() in s.lower() for s in ime_e]))[0]
            if not len(sel):
                pres[nz] = np.nan; continue
            j = sel[np.argmax(tok[sel])]
            rev = eid[e.v[j], e.u[j]]
            pres[nz] = float(tok[j] + (tok[int(rev) - 1] if rev else 0))
        # vrijeme za parove (zastoj)
        G = mp.graf(e, n, t)
        vr = {}
        for nz, a, b in PAROVI:
            ca = sve_cv[ta.query(m_xy(*a))[1]]; cb = sve_cv[ta.query(m_xy(*b))[1]]
            vr[nz] = float(dijkstra(G, indices=[ca])[0, cb])
        na_novoj = float(tok[nova0:].max()) * 2 if len(e) > nova0 else np.nan
        return vh, pres, vr, na_novoj, geoms

    rez, pre, geo = [], [], []
    baza = None
    import os
    izbor = os.environ.get("SCEN", "0," + ",".join(SCENARIJI)).split(",")
    for sc in izbor:
        print(f"Scenarij {sc} ...", flush=True)
        vh, pres, vr, na_novoj, geoms = pokreni(sc)
        if sc == "0":
            baza = (vh, pres, vr)
        naziv = "Osnovno stanje" if sc == "0" else SCENARIJI[sc][0]
        rez.append({"scenarij": sc, "naziv": naziv, "vozilo_sati_dnevno": round(vh),
                    "usteda_vozilo_sati": round(baza[0] - vh), "na_novoj_dionici_dnevno": None if np.isnan(na_novoj) else round(na_novoj),
                    **{f"min: {q}": round(vr[q], 1) for q in vr}})
        for nz, val in pres.items():
            pre.append({"scenarij": sc, "presjek": nz, "dnevno": round(val) if np.isfinite(val) else None,
                        "promjena_pct": round((val / baza[1][nz] - 1) * 100, 1) if np.isfinite(val) and baza[1][nz] else None})
        for g in geoms:
            geo.append({"scenarij": sc, "naziv": naziv, "geometry": g})
        print(pd.DataFrame(rez).tail(1).to_string(index=False), flush=True)
    R = pd.DataFrame(rez); Pp = pd.DataFrame(pre)
    if os.environ.get("SCEN"):   # djelimično pokretanje: spoji s postojećim rezultatima (zamijeni iste scenarije)
        if (OUT / "scenariji.csv").exists():
            R0 = pd.read_csv(OUT / "scenariji.csv", dtype={"scenarij": str}); P0 = pd.read_csv(OUT / "scenariji_presjeci.csv", dtype={"scenarij": str})
            R = pd.concat([R0[~R0.scenarij.isin(R.scenarij)], R]).sort_values("scenarij")
            Pp = pd.concat([P0[~P0.scenarij.isin(Pp.scenarij)], Pp])
    R.to_csv(OUT / "scenariji.csv", index=False); Pp.to_csv(OUT / "scenariji_presjeci.csv", index=False)
    if geo:
        gpd.GeoDataFrame(geo, crs=CRS_M).to_crs(CRS_WGS).to_file(OUT / "scenariji.geojson", driver="GeoJSON", COORDINATE_PRECISION=5)
    pd.set_option("display.width", 250)
    print(R.to_string(index=False))
    print(Pp.pivot(index="presjek", columns="scenarij", values="promjena_pct").to_string())


if __name__ == "__main__":
    main()
