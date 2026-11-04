"""Koraci 4, 5, 7 i 8: težine, kontrolni zbirovi, starosne grupe, raspon.

Ulaz:  interim/dijelovi.gpkg (ili dijelovi_03.gpkg ako 04 nije pokrenut),
       interim/zgrade.gpkg, interim/polja.gpkg, data/*.csv
       data/stari_grad_graf3.csv  (TEK nakon potvrde naziva MZ s Grafa 3:
                                   kolone mz, stanovnici)
Izlaz: out/polja_h3.gpkg, out/polja_h3.geojson, out/mz_zbirovi.csv,
       interim/raspodjela_dijelovi.gpkg (po dijelu: glavni scenarij, bez MZ ograničenja)
"""
from __future__ import annotations

import importlib.util
import json

import geopandas as gpd
import numpy as np
import pandas as pd

from common import (ALFA_OPCINA, GUSTINA_NISKA_OPCINA, GUSTINA_NISKA, PRAG_BLOK, ALFA, ALFE_SCENARIJI, BETA_NOVI_GRAD, C_PRAG_WORLDPOP, CRS_M, CRS_WGS,
                    DATA, INTERIM, MATICNE_MZ_NOVI_GRAD, OUT, SPRAT_POMAK_SCENARIJI,
                    VELIKA_ZGRADA, najveci_ostatak, normaliziraj, opcine_ukupno)

_spec = importlib.util.spec_from_file_location("zgrade", __file__.replace("05_raspodjela.py", "02_zgrade.py"))
_zg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_zg)
zapremina = _zg.zapremina

SG, NG = "Stari Grad Sarajevo", "Novi Grad Sarajevo"


# ------------------------------------------------------------ zgrade -> dijelovi

def zgrade_u_dijelove(z: gpd.GeoDataFrame, d: gpd.GeoDataFrame) -> pd.DataFrame:
    """Tabela (zgrada, dio, udio). Male zgrade po centroidu, velike po presjeku."""
    d = d[["geometry"]].copy()
    d["dio"] = np.arange(len(d))
    z = z[["geometry"]].copy()
    z["zgrada"] = np.arange(len(z))
    velika = z.area > VELIKA_ZGRADA

    c = z[~velika].copy()
    c["geometry"] = c.representative_point()
    j = gpd.sjoin(c, d, predicate="within")[["zgrada", "dio"]].drop_duplicates("zgrada")
    j["udio"] = 1.0

    v = z[velika]
    ov = gpd.overlay(v.assign(_a=v.area), d, how="intersection", keep_geom_type=True)
    ov["udio"] = ov.area / ov._a
    return pd.concat([j, ov[["zgrada", "dio", "udio"]]], ignore_index=True)


# ------------------------------------------------------------ model

def tezine(B: np.ndarray, P: np.ndarray, C: np.ndarray, zona: np.ndarray, alfa_ulaz) -> np.ndarray:
    """alfa_ulaz: broj (isti za sve zone) ili rječnik općina -> α."""
    W = np.zeros(len(B))
    for zz in np.unique(zona):
        m = zona == zz
        b, p, c = B[m], P[m], C[m]
        sb, sp = b.sum(), p.sum()
        if sb > 0 and sp > 0:
            alfa = alfa_ulaz[str(zz).split("|")[0]] if isinstance(alfa_ulaz, dict) else alfa_ulaz
            w = alfa * b / sb + (1 - alfa) * p / sp
            w[c] = p[c] / sp  # nedostaju zgrade: samo WorldPop
        elif sb > 0:
            w = b / sb
        elif sp > 0:
            w = p / sp
        else:
            w = np.ones(m.sum()) / m.sum()
        W[m] = w
    return W


def rasporedi(T: dict, W: np.ndarray, zona: np.ndarray) -> np.ndarray:
    out = np.zeros(len(W))
    for zz, t in T.items():
        m = zona == zz
        s = W[m].sum()
        out[m] = t * W[m] / s if s > 0 else t / m.sum()
    return out


def mz_ciljevi(d: pd.DataFrame, W_op: np.ndarray, Topc: pd.Series, sg_graf3: pd.DataFrame | None,
               ng_2010: pd.DataFrame) -> tuple[np.ndarray, dict, dict]:
    """Vraća (zona po dijelu, T po zoni, info)."""
    zona = d.opcina.to_numpy().astype(object)
    T = {o: float(Topc[o]) for o in Topc.index}
    info = {}

    # Stari Grad: tvrdi udjeli iz Grafa 3 (samo ako su nazivi potvrđeni)
    if sg_graf3 is not None:
        m = (d.opcina == SG).to_numpy()
        mz_u_modelu = set(d.loc[m, "mz"].dropna())
        n = sg_graf3.set_index("mz").stanovnici
        if d.loc[m, "mz"].notna().all() and mz_u_modelu <= set(n.index):
            n = n[[x for x in n.index if x in mz_u_modelu]]
            T.pop(SG)
            for mz_, v in n.items():
                T[f"{SG}|{mz_}"] = Topc[SG] * v / n.sum()
            zona[m] = (SG + "|" + d.loc[m, "mz"]).to_numpy()
            info[SG] = "MZ zbirovi iz Grafa 3 (udjeli)"
        else:
            info[SG] = ("dio općine bez MZ ili nazivi MZ ne odgovaraju Grafu 3 "
                        f"({sorted(mz_u_modelu - set(n.index))}); samo zbir općine")
    else:
        info[SG] = "Graf 3 nije potvrđen; samo zbir općine"

    # Novi Grad: meko ograničenje 2010 + model
    m = (d.opcina == NG).to_numpy()
    if m.any() and d.loc[m, "mz"].notna().all():
        um = pd.Series(W_op[m], index=d.loc[m, "mz"].to_numpy()).groupby(level=0).sum()
        um = um / um.sum()
        n10 = ng_2010.assign(k=ng_2010.mz_danas.map(normaliziraj)).set_index("k").stanovnici
        kljuc = {mz_: normaliziraj(mz_) for mz_ in um.index}
        nove = [mz_ for mz_ in um.index if kljuc[mz_] not in n10.index]
        u10 = pd.Series(0.0, index=um.index)
        stare = [mz_ for mz_ in um.index if mz_ not in nove]
        u10[stare] = [n10[kljuc[x]] for x in stare]
        u10 = u10 / u10.sum()
        poznate = {n: p for n, p in MATICNE_MZ_NOVI_GRAD.items() if n in nove and p in stare}
        for nova, mat in poznate.items():
            grupa = [mat, nova]
            u10[grupa] = u10[mat] * um[grupa] / um[grupa].sum()
        nepoznate = [x for x in nove if x not in poznate]
        if nepoznate:
            ostatak = 1 - um[nepoznate].sum()
            ost = [x for x in um.index if x not in nepoznate]
            u10[ost] = u10[ost] / u10[ost].sum() * ostatak
            u10[nepoznate] = um[nepoznate]
        udio = BETA_NOVI_GRAD * u10 + (1 - BETA_NOVI_GRAD) * um
        T.pop(NG)
        for mz_, u in udio.items():
            T[f"{NG}|{mz_}"] = Topc[NG] * u
        zona[m] = (NG + "|" + d.loc[m, "mz"]).to_numpy()
        info[NG] = (f"MZ: β={BETA_NOVI_GRAD}·udio_2010 + (1−β)·udio_modela; "
                    f"nove MZ s matičnom: {poznate or 'nema'}; bez matične: {nepoznate or 'nema'}")
        info["ng_udjeli"] = pd.DataFrame({"udio_2010_prilagodjen": u10, "udio_modela": um,
                                          "udio_konacni": udio}).round(5).to_dict(orient="index")
    else:
        info[NG] = "MZ poligoni nisu dostupni; samo zbir općine"
    return zona, T, info


def main() -> None:
    p = INTERIM / "dijelovi.gpkg"
    if not p.exists():
        p = INTERIM / "dijelovi_03.gpkg"
        print("UPOZORENJE: interim/dijelovi.gpkg ne postoji (04 nije pokrenut); Novi Grad bez MZ.")
    d = gpd.read_file(p)
    z = gpd.read_file(INTERIM / "zgrade.gpkg")
    polja = gpd.read_file(INTERIM / "polja.gpkg")
    op = opcine_ukupno()
    Topc = op.stanovnici
    sg_path = DATA / "stari_grad_graf3.csv"
    sg_graf3 = pd.read_csv(sg_path).dropna(subset=["mz"]) if sg_path.exists() else None
    ng_2010 = pd.read_csv(DATA / "mz_novi_grad_2010.csv")

    veze = zgrade_u_dijelove(z, d)
    print(f"Zgrada pridruženo dijelovima: {veze.zgrada.nunique()} od {len(z)}")

    # težina zgrade = stambena površina × gustina stanovanja (kuće < blokovi)
    niska = z.opcina.map(GUSTINA_NISKA_OPCINA).fillna(GUSTINA_NISKA).to_numpy()
    gustina = np.where(z.spratnost.to_numpy() >= PRAG_BLOK, 1.0, niska)

    def B_za(pomak: int, fizicka: bool = False) -> np.ndarray:
        vol = zapremina(z, pomak).to_numpy() * (1.0 if fizicka else gustina)
        return np.bincount(veze.dio, weights=vol[veze.zgrada] * veze.udio, minlength=len(d))

    P = d.P.to_numpy()
    B0 = B_za(0)
    M0 = B_za(0, fizicka=True)  # stambeni m² (za provjeru gustine poda)
    C = (B0 == 0) & (P >= C_PRAG_WORLDPOP)
    print(f"Dijelova s oznakom C (WorldPop ≥ {C_PRAG_WORLDPOP}, zgrade = 0): {C.sum()}")

    zona_op = d.opcina.to_numpy()

    def model(alfa: float, pomak: int, mz_ogr: bool = True):
        B = B0 if pomak == 0 else B_za(pomak)
        W_op = tezine(B, P, C, zona_op, alfa)
        if not mz_ogr:
            return rasporedi({o: Topc[o] for o in Topc.index}, W_op, zona_op), None
        zona, T, info = mz_ciljevi(d, W_op, Topc, sg_graf3, ng_2010)
        W = tezine(B, P, C, zona, alfa)
        return rasporedi(T, W, zona), (zona, info)

    glavni, (zona, info) = model(ALFA_OPCINA, 0)
    bez_mz, _ = model(ALFA_OPCINA, 0, mz_ogr=False)
    scen = {}
    for a in ALFE_SCENARIJI:
        for s in SPRAT_POMAK_SCENARIJI:
            scen[f"a{a}_s{s:+d}"] = model(a, s)[0]
    S = np.column_stack(list(scen.values()))

    # cijeli brojevi: najveći ostatak po općini (tačan zbir)
    st = np.zeros(len(d), dtype=int)
    for o in Topc.index:
        m = (d.opcina == o).to_numpy()
        st[m] = najveci_ostatak(glavni[m], int(Topc[o]))

    # starosne grupe po dijelu
    grupe = ["d0_14", "d15_64", "d65plus"]
    G = np.zeros((len(d), 3), dtype=int)
    for i, (o, n) in enumerate(zip(d.opcina, st)):
        G[i] = najveci_ostatak(op.loc[o, grupe].to_numpy(float), int(n))

    zona_mz = np.array(["|" in str(x) for x in zona])
    pouz = np.where(C, "C", np.where(zona_mz & (B0 > 0), "A", "B"))

    dd = d.copy()
    dd["zona"] = zona
    dd["B"] = B0
    dd["m2"] = M0
    dd["C"] = C
    dd["pouzdanost"] = pouz
    dd["stanovnici_f"] = glavni
    dd["stanovnici"] = st
    dd["stanovnici_bez_mz"] = bez_mz
    dd["stanovnici_min"] = S.min(axis=1)
    dd["stanovnici_max"] = S.max(axis=1)
    dd[grupe] = G
    for k, v in scen.items():
        dd[f"sc_{k}"] = v
    dd.to_file(INTERIM / "raspodjela_dijelovi.gpkg", driver="GPKG")

    # ---- agregacija na polja
    def dominantna(g, kol):
        s = g.groupby(kol, dropna=True).stanovnici_f.sum()
        if s.empty:
            return None
        return s.idxmax() if s.max() > 0 else g.groupby(kol).povrsina.sum().idxmax()

    agg = dd.groupby("h3_id").agg(
        stanovnici=("stanovnici", "sum"), stanovnici_min=("stanovnici_min", "sum"),
        stanovnici_max=("stanovnici_max", "sum"), d0_14=("d0_14", "sum"),
        d15_64=("d15_64", "sum"), d65plus=("d65plus", "sum"), stambeni_m2=("m2", "sum"),
        worldpop=("P", "sum"))
    rows = []
    for h, g in dd.groupby("h3_id"):
        tot = g.stanovnici_f.sum()
        udio = {k: (g.loc[g.pouzdanost == k, "stanovnici_f"].sum() / tot if tot > 0 else
                    (g.pouzdanost == k).mean()) for k in "ABC"}
        pz = "C" if udio["C"] >= 0.5 else ("A" if udio["A"] >= 0.5 else "B")
        if udio["C"] >= 0.999:
            izv = "WorldPop (nema zgrada)"
        elif udio["C"] > 0:
            izv = f"zgrade+WorldPop (α={ALFA_OPCINA.get(dominantna(g, 'opcina'), ALFA)}); dio samo WorldPop"
        elif g.B.sum() > 0:
            izv = f"zgrade+WorldPop (α={ALFA_OPCINA.get(dominantna(g, 'opcina'), ALFA)})"
        else:
            izv = "WorldPop" if g.P.sum() > 0 else "nema težine"
        op_dom = dominantna(g, "opcina")
        rows.append({"h3_id": h, "opcina": op_dom, "mz": dominantna(g[g.opcina == op_dom], "mz"),
                     "pouzdanost": pz, "izvor_tezine": izv})
    meta = pd.DataFrame(rows).set_index("h3_id")
    out = polja.set_index("h3_id").join(meta, how="inner").join(agg)
    out["stanovnici_min"] = np.minimum(out.stanovnici_min, out.stanovnici).round().astype(int)
    out["stanovnici_max"] = np.maximum(out.stanovnici_max, out.stanovnici).round().astype(int)
    out = out.reset_index()[["h3_id", "opcina", "mz", "stanovnici", "stanovnici_min", "stanovnici_max",
                             "d0_14", "d15_64", "d65plus", "pouzdanost", "izvor_tezine",
                             "stambeni_m2", "worldpop", "geometry"]]
    out = gpd.GeoDataFrame(out, geometry="geometry", crs=CRS_M)
    out.to_file(OUT / "polja_h3.gpkg", driver="GPKG")
    gj = OUT / "polja_h3.geojson"
    gj.unlink(missing_ok=True)
    out.to_crs(CRS_WGS).to_file(gj, driver="GeoJSON")

    # ---- MZ zbirovi
    mzd = dd.assign(mz=dd.mz.fillna("(MZ nepoznata)"))
    sc_kol = [c for c in dd if c.startswith("sc_")]
    g = mzd.groupby(["opcina", "mz"])
    mzt = g[["stanovnici", "d0_14", "d15_64", "d65plus"]].sum()
    sct = g[sc_kol].sum()
    mzt["stanovnici_min"] = sct.min(axis=1).round().astype(int)
    mzt["stanovnici_max"] = sct.max(axis=1).round().astype(int)
    mzt["stanovnici_bez_mz_ogranicenja"] = g.stanovnici_bez_mz.sum().round().astype(int)
    mzt["kontrolni_zbir"] = g.zona.first().str.contains("|", regex=False).map(
        {True: "MZ", False: "samo općina"})
    mzt.reset_index().to_csv(OUT / "mz_zbirovi.csv", index=False)

    (INTERIM / "raspodjela_info.json").write_text(
        json.dumps({k: v for k, v in info.items()}, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8")
    print("\nZbir po općini:")
    print(dd.groupby("opcina").stanovnici.sum().to_frame().join(Topc.rename("FZS")).to_string())
    for k in (SG, NG):
        print(f"{k}: {info.get(k)}")
    print(f"\nPolja: {len(out)}; pouzdanost: {out.pouzdanost.value_counts().to_dict()}")


if __name__ == "__main__":
    main()
