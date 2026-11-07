"""Procjena radnih mjesta (mjesto rada) po H3 polju.

Ulaz:  interim/zgrade.gpkg (02), raw/overture_places.parquet, out/polja_h3.gpkg
       data/radna_mjesta_opcine.csv: prosječan broj zaposlenih po općini, 2024
       (FZS, Kanton Sarajevo u brojkama 2025, tabela 4.2; po mjestu rada) i zaposleni stanovnici
       31.07.2025 (ZIS KS, izvor Porezna uprava FBiH; po mjestu stanovanja)
Izlaz: out/radna_mjesta_h3.csv, out/radna_mjesta_mz.csv

Postupak (procjena):
  težina zgrade = poslovna površina / m² po radnom mjestu za vrstu zgrade
                  (poslovna površina = površina · spratnost · (1 − stambeni udio);
                   poslovno prizemlje stambene zgrade: 70% otiska, 40 m² po radnom mjestu)
                + 2 · broj firmi/objekata iz Overture u zgradi ili na ≤ 25 m (male firme u stanovima)
  radna mjesta u općini = FZS (kontrolni zbir), raspoređeno po težini.
  Ograničenja: FZS broji po sjedištu poslovne jedinice, pa dio radnika firmi sa sjedištem u
  Centru možda radi drugdje; m² po radnom mjestu su tipične vrijednosti, ne mjerenje;
  OSM često ne razlikuje poslovne i stambene zgrade.
"""
from __future__ import annotations

import geopandas as gpd
import numpy as np
import pandas as pd

from common import CRS_M, DATA, OUT, RAW, najveci_ostatak

M2_PO_RADNIKU = {
    "office": 25, "commercial": 30, "government": 25, "public": 30, "bank": 25, "civic": 30,
    "retail": 35, "supermarket": 45, "kiosk": 15, "hospital": 45, "clinic": 40,
    "school": 60, "kindergarten": 50, "college": 50, "university": 45, "hotel": 60,
    "industrial": 120, "manufacture": 120, "factory": 120, "warehouse": 200,
    "train_station": 150, "transportation": 150, "fire_station": 80, "police": 40,
}
BEZ_RADNIKA = {"garage", "garages", "parking", "roof", "ruins", "construction", "grandstand", "shed",
               "carport", "mosque", "church", "chapel", "religious", "house", "apartments", "residential",
               "terrace", "detached", "semidetached_house", "bungalow", "hut", "cabin", "bunker"}
MAX_OTISAK_M2 = 3000
M2_DEFAULT = 50          # nestambeni dio zgrade nepoznate vrste
M2_INDUSTRIJSKA_ZONA = 120
RADNIKA_PO_FIRMI = 2
OVERTURE_ISKLJUCI = ("park", "monument", "landmark", "church", "mosque", "religious", "bus_stop", "atm",
                     "parking", "residential", "apartment", "memorial", "mountain", "river", "lake",
                     "structure", "bridge", "public_plaza", "cemetery", "playground", "viewpoint",
                     "hiking", "neighborhood", "city", "town", "home", "housing")


def main() -> None:
    kz = pd.read_csv(DATA / "radna_mjesta_opcine.csv").set_index("opcina")
    z = gpd.read_file(INTERIM_ZGRADE)
    # model spratnosti je učen na stambenim zgradama: velikim poslovnim otiscima (hale, tržni centri)
    # s procijenjenom spratnošću ograniči visinu
    sprat = z.spratnost.clip(lower=1).where(~((z.spratnost_izvor == "model") & (z.povrsina > MAX_OTISAK_M2)
                                               & (z.stambeni_udio < 1)), lambda x: x.clip(upper=3))
    z["pod"] = z.povrsina * sprat
    tip = z.tip.str.split(";").str[0]
    m2 = tip.map(M2_PO_RADNIKU)
    m2 = m2.where(m2.notna(), np.where(z.landuse.isin(["industrial"]), M2_INDUSTRIJSKA_ZONA, M2_DEFAULT))
    nes = z.pod * (1 - z.stambeni_udio)
    w = np.where(tip.isin(BEZ_RADNIKA) & z.tip.ne("yes"), 0, nes / m2)
    w = w + np.where(z.poslovno_prizemlje & (z.stambeni_udio > 0.5), 0.7 * z.povrsina / 40, 0)
    z["w_zgrada"] = w

    o = gpd.read_parquet(RAW / "overture_places.parquet")
    o["kat"] = o.taxonomy.apply(lambda t: t.get("primary") if t is not None else None).fillna("")
    o = o[(o.confidence >= 0.4) & ~o.kat.str.contains("|".join(OVERTURE_ISKLJUCI))]
    if "operating_status" in o:
        o = o[o.operating_status.fillna("open").ne("permanently_closed")]
    o = o.to_crs(CRS_M)
    o["geometry"] = o.geometry.representative_point()
    j = gpd.sjoin_nearest(o[["geometry"]], z[["geometry"]], max_distance=25, how="left")
    j = j[~j.index.duplicated()]
    firme = j.index_right.dropna().astype(int).value_counts()
    z["firme"] = firme.reindex(z.index).fillna(0).to_numpy()
    z["w"] = z.w_zgrada + RADNIKA_PO_FIRMI * z.firme
    print(f"Overture objekata s radnicima: {len(o):,}, u zgradi ili ≤ 25 m: {firme.sum():,.0f}")

    polja = gpd.read_file(OUT / "polja_h3.gpkg")
    zc = z[["opcina", "w", "w_zgrada", "firme", "geometry"]].copy()
    zc["geometry"] = zc.representative_point()
    zc = gpd.sjoin(zc, polja[["h3_id", "geometry"]], predicate="within")
    zc = zc[zc.opcina.isin(kz.index)]
    rows = []
    for op, g in zc.groupby("opcina"):
        cilj = int(kz.loc[op, "radna_mjesta_2024"])
        if g.w.sum() <= 0:
            continue
        rows.append(g.assign(rm=g.w / g.w.sum() * cilj))
        print(f"{op}: {cilj:,} radnih mjesta; udio iz zgrada {g.w_zgrada.sum() / g.w.sum():.0%}, "
              f"iz firmi {RADNIKA_PO_FIRMI * g.firme.sum() / g.w.sum():.0%}")
    zc = pd.concat(rows)
    po_polju = zc.groupby(["h3_id", "opcina"]).rm.sum().reset_index()
    # cijeli brojevi: najveći ostatak po općini
    po_polju["radna_mjesta"] = 0
    for op, g in po_polju.groupby("opcina"):
        po_polju.loc[g.index, "radna_mjesta"] = najveci_ostatak(g.rm.to_numpy(), int(kz.loc[op, "radna_mjesta_2024"]))
    rm = po_polju.groupby("h3_id").radna_mjesta.sum()
    out = polja[["h3_id", "opcina", "mz", "stanovnici"]].copy()
    out["radna_mjesta"] = rm.reindex(out.h3_id).fillna(0).astype(int).to_numpy()
    out["po_km2"] = (out.radna_mjesta / (polja.area / 1e6)).round(0)
    out.drop(columns=["opcina", "mz", "stanovnici"]).to_csv(OUT / "radna_mjesta_h3.csv", index=False)

    mz = out.dropna(subset=["mz"]).groupby(["opcina", "mz"]).agg(radna_mjesta=("radna_mjesta", "sum"),
                                                                  stanovnici=("stanovnici", "sum")).reset_index()
    mz["rm_na_100_stanovnika"] = (100 * mz.radna_mjesta / mz.stanovnici.clip(lower=1)).round(0)
    mz.sort_values("radna_mjesta", ascending=False).to_csv(OUT / "radna_mjesta_mz.csv", index=False)
    print("\nOpćine: radna mjesta / zaposleni stanovnici")
    print(kz.assign(omjer=(kz.radna_mjesta_2024 / kz.zaposleni_stanovnici_2025).round(2)).to_string())
    print("\nNajviše radnih mjesta (MZ):")
    print(mz.sort_values("radna_mjesta", ascending=False).head(15).to_string(index=False))
    print("\nNajgušća polja:")
    print(out.sort_values("radna_mjesta", ascending=False).head(10).to_string(index=False))


INTERIM_ZGRADE = OUT.parent / "interim" / "zgrade.gpkg"

if __name__ == "__main__":
    main()
