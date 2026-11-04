"""Odjeljak 6: provjere -> out/validacija.md"""
from __future__ import annotations

import json

import geopandas as gpd
import numpy as np
import pandas as pd

from common import DATA, INTERIM, OUT, normaliziraj, opcine_ukupno

SG, NG = "Stari Grad Sarajevo", "Novi Grad Sarajevo"


def md_tabela(df: pd.DataFrame, n: int | None = None) -> str:
    df = df if n is None else df.head(n)
    if df.empty:
        return "_(nema)_\n"
    kol = list(df.columns)
    lin = ["| " + " | ".join(map(str, kol)) + " |", "|" + "---|" * len(kol)]
    for _, r in df.iterrows():
        lin.append("| " + " | ".join(f"{v:,.3f}" if isinstance(v, float) else str(v) for v in r) + " |")
    return "\n".join(lin) + "\n"


def main() -> None:
    d = gpd.read_file(INTERIM / "raspodjela_dijelovi.gpkg")
    p = gpd.read_file(OUT / "polja_h3.gpkg")
    Topc = opcine_ukupno().stanovnici
    info = json.loads((INTERIM / "raspodjela_info.json").read_text(encoding="utf-8"))
    r = ["# Validacija\n", "Sve ispod nivoa općine je model (raspodjela), ne mjerenje.\n"]
    ok_sve = True

    # 1. zbir po općini
    z = d.groupby("opcina").stanovnici.sum().to_frame("model").join(Topc.rename("FZS_2026"))
    z["razlika"] = z.model - z.FZS_2026
    ok = (z.razlika == 0).all()
    ok_sve &= ok
    r += ["\n## 1. Zbir po općini\n", f"**{'OK' if ok else 'GREŠKA'}**\n\n", md_tabela(z.reset_index())]

    # 2. Stari Grad bez MZ ograničenja vs Graf 3
    r.append("\n## 2. Stari Grad: model bez MZ ograničenja vs Graf 3 (udjeli)\n")
    gp = DATA / "stari_grad_graf3.csv"
    if gp.exists():
        g3 = pd.read_csv(gp).dropna(subset=["mz"]).set_index("mz").stanovnici
        m = d[d.opcina == SG].groupby("mz").stanovnici_bez_mz.sum()
        t = pd.DataFrame({"graf3_udio": g3 / g3.sum(), "model_udio": m / m.sum()}).dropna()
        t["rel_greska"] = (t.model_udio - t.graf3_udio).abs() / t.graf3_udio
        mape = t.rel_greska.mean() * 100
        r += [f"Graf 3 ukupno {int(g3.sum()):,}, FZS {int(Topc[SG]):,} (porede se udjeli).\n\n",
              f"**MAPE po MZ: {mape:.1f}%** (glavna mjera kvaliteta modela)\n\n",
              md_tabela(t.sort_values("rel_greska", ascending=False).reset_index())]
    else:
        r.append("**Nije izračunato**: nazivi MZ na Grafu 3 (Strategija 2024–2027, str. 16) još "
                 "nisu potvrđeni. Nakon čitanja grafikona spremiti `data/stari_grad_graf3.csv` "
                 "(kolone `mz`, `stanovnici`) i ponoviti korake 05–06.\n")

    # 3. Novi Grad vs 2010
    r.append("\n## 3. Novi Grad: model bez MZ ograničenja vs udjeli 2010\n")
    ng = d[d.opcina == NG]
    if ng.mz.notna().any():
        n10 = pd.read_csv(DATA / "mz_novi_grad_2010.csv")
        n10["k"] = n10.mz_danas.map(normaliziraj)
        m = ng.groupby("mz").stanovnici_bez_mz.sum()
        t = pd.DataFrame({"model_udio": m / m.sum()})
        t["k"] = t.index.map(normaliziraj)
        t = t.join(n10.set_index("k").stanovnici.rename("st_2010"), on="k")
        poz = t.st_2010.notna()
        t["udio_2010"] = np.where(poz, t.st_2010 / t.st_2010[poz].sum() * (1 - t.model_udio[~poz].sum()), np.nan)
        t["omjer"] = t.model_udio / t.udio_2010
        t["oznaka"] = np.select(
            [~poz, t.omjer > 1.3, t.omjer < 0.7],
            ["nova MZ (nema 2010)", "model > 2010 za >30%: nova gradnja?", "model < 2010 za >30%: provjeriti"], "")
        r += ["Udjeli 2010 preskalirani na dio općine bez novih MZ. Odstupanje > 30% je označeno; "
              "veće udjele u modelu obično objašnjava nova gradnja nakon 2010.\n\n",
              md_tabela(t.drop(columns=["k", "st_2010"]).sort_values("omjer").reset_index())]
        if "ng_udjeli" in info:
            r.append("\nKonačni udjeli korišteni kao meko ograničenje: vidi `interim/raspodjela_info.json`.\n")
    else:
        r.append("**Nije izračunato**: Novi Grad nema MZ poligone (korak 04 nije završen).\n")

    # 4. gustina poda
    p["m2_po_st"] = np.where(p.stanovnici > 0, p.stambeni_m2 / p.stanovnici.clip(lower=1), np.nan)
    sa_zgradama = (p.stanovnici >= 10) & (p.stambeni_m2 > 0)
    van = p[sa_zgradama & ((p.m2_po_st < 15) | (p.m2_po_st > 60))]
    bez_zgrada = int(((p.stanovnici >= 10) & (p.stambeni_m2 == 0)).sum())
    med = np.nanmedian(p.loc[sa_zgradama, "m2_po_st"])
    r += ["\n## 4. Gustina poda (stambeni m² po stanovniku, očekivano 15–60)\n",
          f"Medijan (polja s ≥ 10 st.): {med:.1f} m²/st. Polja izvan raspona: **{len(van)}** "
          f"od {int(sa_zgradama.sum())}. Polja sa stanovnicima a bez stambenih zgrada "
          f"(pouzdanost C, samo WorldPop): **{bez_zgrada}**.\n\n",
          md_tabela(van.sort_values("m2_po_st")[["h3_id", "opcina", "mz", "stanovnici", "stambeni_m2",
                                                 "m2_po_st", "pouzdanost"]].round(1))]

    # 5. vizuelno: industrija, parkovi, aerodrom; gusta naselja
    r.append("\n## 5. Vizuelna provjera\n")
    lu = gpd.read_file(INTERIM / "landuse.gpkg")
    lu = lu[lu.vrsta.isin(["landuse=industrial", "park", "aerodrom"])]
    if len(lu):
        dd = d[["stanovnici_f", "geometry"]].copy()
        dd["_a"] = dd.area
        ov = gpd.overlay(dd, lu, how="intersection", keep_geom_type=True)
        ov["st"] = ov.stanovnici_f * ov.area / ov._a
        t = ov.groupby("vrsta").st.sum().round(0).to_frame("procijenjeno_stanovnika (površinski)")
        r += ["Stanovnici u zonama gdje ih ne bi trebalo biti (aproksimacija: ravnomjerno po dijelu polja):\n\n",
              md_tabela(t.reset_index())]
    gust = d.dropna(subset=["mz"]).groupby(["opcina", "mz"]).agg(st=("stanovnici", "sum"), a=("povrsina", "sum"))
    gust["st_po_km2"] = (gust.st / gust.a * 1e6).round(0)
    gust = gust.sort_values("st_po_km2", ascending=False).reset_index()
    gust["rang"] = np.arange(1, len(gust) + 1)
    cilj = gust[gust.mz.str.contains("Dobrinja|Alipašino|Grbavica", regex=True)]
    r += [f"\nNajgušće MZ (od {len(gust)} sa poznatim granicama):\n\n",
          md_tabela(gust[["rang", "opcina", "mz", "st", "st_po_km2"]], 15),
          "\nDobrinja, Alipašino Polje, Grbavica (očekivano visoko):\n\n",
          md_tabela(cilj[["rang", "opcina", "mz", "st", "st_po_km2"]]),
          "\nKarta za vizuelni pregled: `out/karta.html`.\n"]

    # 6. starosne grupe
    zb = p.d0_14 + p.d15_64 + p.d65plus
    ok6 = bool((zb == p.stanovnici).all())
    ok_sve &= ok6
    gr = d.groupby("opcina")[["d0_14", "d15_64", "d65plus"]].sum()
    fzs = opcine_ukupno()[["d0_14", "d15_64", "d65plus"]]
    r += ["\n## 6. Starosne grupe\n",
          f"Zbir grupa = ukupno u svakom polju: **{'OK' if ok6 else 'GREŠKA'}** "
          f"({int((zb != p.stanovnici).sum())} polja odstupa).\n\n",
          "Odstupanje zbira grupa po općini od FZS-a (posljedica zaokruživanja po polju):\n\n",
          md_tabela((gr - fzs.loc[gr.index]).reset_index())]

    r += ["\n## Napomene o modelu\n"] + [f"- **{k}**: {v}\n" for k, v in info.items() if k != "ng_udjeli"]
    r.append(f"- Pouzdanost polja: {p.pouzdanost.value_counts().to_dict()}\n")
    (OUT / "validacija.md").write_text("".join(r), encoding="utf-8")
    print("".join(r[:6]))
    print(f"-> out/validacija.md ({'sve tvrde provjere OK' if ok_sve else 'IMA GREŠAKA'})")


if __name__ == "__main__":
    main()
