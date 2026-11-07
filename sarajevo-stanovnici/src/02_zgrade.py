"""Korak 2: zgrade, spratnost i stambeni udio.

Ulaz:  raw/osm_grad.json, raw/granice.json, (opcionalno) raw/ghsl_built_h.tif
Izlaz: interim/zgrade.gpkg, interim/landuse.gpkg, interim/zgrade_statistika.json

Zapremina se ovdje NE računa konačno, jer scenariji (korak 8) mijenjaju
podrazumijevanu spratnost. Upisuju se sastojci:
  povrsina, spratnost, spratnost_izvor, poslovno_prizemlje, stambeni_udio
i osnovna zapremina za pomak 0.
"""
from __future__ import annotations

import json
import re

import geopandas as gpd
import numpy as np
import pandas as pd

from common import (CRS_M, INTERIM, MIN_POVRSINA_ZGRADE, NESTAMBENE,
                    PODRAZUMIJEVANA_SPRATNOST, RAW, STAMBENE, overpass_u_gdf,
                    poligoni, ucitaj_granice)


def broj(s):
    if s is None or (isinstance(s, float) and np.isnan(s)):
        return np.nan
    m = re.search(r"\d+(?:[.,]\d+)?", str(s))
    return float(m.group(0).replace(",", ".")) if m else np.nan


def procjena_spratnosti(z: gpd.GeoDataFrame, cent: gpd.GeoDataFrame) -> tuple[np.ndarray, dict]:
    """Gradient boosting na zgradama s building:levels. Ulazi: površina i oblik
    otiska, tip, gustina i veličina okolnih zgrada, GHSL visina. Vraća procjenu
    za sve zgrade i rezultat prostorne unakrsne provjere (blokovi 500 m)."""
    from scipy.spatial import cKDTree
    from sklearn.ensemble import GradientBoostingRegressor
    from sklearn.model_selection import GroupKFold

    xy = np.c_[cent.geometry.x, cent.geometry.y]
    tree = cKDTree(xy)
    _, idx = tree.query(xy, k=min(16, len(z)))
    X = pd.DataFrame({
        "log_povrsina": np.log(z.povrsina.to_numpy()),
        "oblik": (z.length / np.sqrt(z.povrsina)).to_numpy(),
        "ghsl_m": z["ghsl_m"].fillna(0).to_numpy(),
        "susjedi_povrsina": np.log(np.median(z.povrsina.to_numpy()[idx[:, 1:]], axis=1)),
        "gustina_100m": tree.query_ball_point(xy, r=100, return_length=True),
        "stambena_visoka": z.tip.isin(["apartments", "residential"]).astype(int).to_numpy(),
        "kuca": z.tip.isin(["house", "detached", "semidetached_house", "terrace", "bungalow"]).astype(int).to_numpy(),
    })
    lab = (z.spratnost_izvor == "building:levels").to_numpy()
    y = z.spratnost.to_numpy(float)
    blok = (xy[:, 0] // 500).astype(int) * 100000 + (xy[:, 1] // 500).astype(int)

    def gbm():
        return GradientBoostingRegressor(n_estimators=300, max_depth=3, learning_rate=0.05,
                                         subsample=0.8, random_state=0)

    cv = np.zeros(lab.sum())
    for tr, te in GroupKFold(5).split(X[lab], y[lab], blok[lab]):
        cv[te] = gbm().fit(X[lab].iloc[tr], y[lab][tr]).predict(X[lab].iloc[te])
    g = np.maximum(np.round(X.ghsl_m[lab] / 3), 1)
    info = {"n_ucenje": int(lab.sum()),
            "model_mae": round(float(np.mean(np.abs(cv - y[lab]))), 2),
            "model_r": round(float(np.corrcoef(cv, y[lab])[0, 1]), 2),
            "ghsl_mae": round(float(np.mean(np.abs(g - y[lab]))), 2),
            "ghsl_r": round(float(np.corrcoef(g, y[lab])[0, 1]), 2)}
    pred = gbm().fit(X[lab], y[lab]).predict(X)
    return np.clip(np.round(pred), 1, None), info


def stambeni_udio(tip: str, landuse: str | None) -> float:
    if tip in STAMBENE:
        return 1.0
    if tip in NESTAMBENE:
        return 0.0
    if tip == "yes" or tip not in STAMBENE | NESTAMBENE:
        # netipizirane (i nepoznati tipovi) po namjeni zemljišta
        if landuse == "residential":
            return 1.0
        if landuse in ("commercial", "retail"):
            return 0.3
        if landuse == "industrial":
            return 0.0
        return 0.7
    return 0.0


def zapremina(z: pd.DataFrame, pomak: int = 0) -> pd.Series:
    """Stambena zapremina (m² poda) uz pomak procijenjene spratnosti
    (podrazumijevana po tipu i model; izmjerena OSM spratnost se ne mijenja)."""
    sprat = z.spratnost + np.where(z.spratnost_izvor.isin(["podrazumijevano", "model"]), pomak, 0)
    sprat = np.maximum(sprat, 1)
    stambeni = np.maximum(sprat - z.poslovno_prizemlje.astype(int), 0)
    return z.povrsina * stambeni * z.stambeni_udio


def main() -> None:
    osm = overpass_u_gdf(RAW / "osm_grad.json")
    opcine, _ = ucitaj_granice()
    print(f"OSM elemenata: {len(osm)}")

    # --- zgrade
    z = poligoni(osm[osm.get("building").notna()]).to_crs(CRS_M)
    z = gpd.clip(z, opcine.union_all()) if len(z) else z
    z = z[z.geom_type.isin(["Polygon", "MultiPolygon"])]
    z["povrsina"] = z.area
    ukupno_prije = len(z)
    z = z[z.povrsina >= MIN_POVRSINA_ZGRADE].copy()
    print(f"Zgrade u modeliranim općinama: {ukupno_prije}, nakon filtra < {MIN_POVRSINA_ZGRADE} m²: {len(z)}")

    for kol in ("building:levels", "height", "addr:street", "addr:housenumber"):
        if kol not in z:
            z[kol] = None
    z["tip"] = z["building"].astype(str).str.strip().str.lower()

    # adresne tačke (čvorovi s addr:*) unutar zgrade bez adrese -> adresa zgrade
    if "addr:housenumber" in osm and "addr:street" in osm:
        at = osm[(osm.geom_type == "Point") & osm["addr:housenumber"].notna()
                 & osm["addr:street"].notna()][["addr:street", "addr:housenumber", "geometry"]].to_crs(CRS_M)
        bez = z["addr:street"].isna() | z["addr:housenumber"].isna()
        hit = gpd.sjoin(at, z.loc[bez, ["geometry"]], predicate="within").drop_duplicates("index_right")
        z.loc[hit.index_right, "addr:street"] = hit["addr:street"].to_numpy()
        z.loc[hit.index_right, "addr:housenumber"] = hit["addr:housenumber"].to_numpy()
        print(f"Adresa preuzeta iz adresnih tačaka: {len(hit)} zgrada")

    # --- landuse
    lu = poligoni(osm[osm.get("landuse").notna()]).to_crs(CRS_M)[["landuse", "geometry"]]
    prioritet = {"industrial": 0, "commercial": 1, "retail": 1, "residential": 2}
    lu["prio"] = lu.landuse.map(prioritet).fillna(3)
    cent = z[["geometry"]].copy()
    cent["geometry"] = z.representative_point()
    j = gpd.sjoin(cent, lu, how="left", predicate="within").sort_values("prio")
    z["landuse"] = j[~j.index.duplicated()].landuse.reindex(z.index)

    # --- spratnost
    nivoi = z["building:levels"].map(broj)
    visina = z["height"].map(broj) / 3.0
    z["spratnost"] = nivoi
    z["spratnost_izvor"] = np.where(nivoi.notna(), "building:levels", None)
    m = z.spratnost.isna() & visina.notna()
    z.loc[m, "spratnost"] = visina[m]
    z.loc[m, "spratnost_izvor"] = "height"

    udio_nivoi = float(nivoi.notna().mean()) if len(z) else 0.0
    ghsl = RAW / "ghsl_built_h.tif"
    ghsl_koristen = False
    model_cv = None
    if udio_nivoi < 0.30:
        if ghsl.exists():
            import rasterio
            with rasterio.open(ghsl) as src:
                pts = cent.to_crs(src.crs)
                vals = np.array([v[0] for v in src.sample(zip(pts.geometry.x, pts.geometry.y))], float)
                vals[(vals <= 0) | (vals == src.nodata)] = np.nan
            z["ghsl_m"] = vals
            ghsl_koristen = True
            # GHSL (prosjek 100 m ćelije) slabo razlikuje zgrade (provjera na zgradama
            # s building:levels: r ≈ 0.13). Zato se spratnost procjenjuje modelom
            # naučenim na zgradama s poznatom spratnošću; GHSL je jedan od ulaza.
            pred, model_cv = procjena_spratnosti(z, cent)
            m = z.spratnost.isna()
            z.loc[m, "spratnost"] = pred[m.to_numpy()]
            z.loc[m, "spratnost_izvor"] = "model"
            print(f"Spratnost procijenjena modelom za {int(m.sum())} zgrada; "
                  f"prostorna unakrsna provjera: {model_cv}")
        else:
            print("UPOZORENJE: < 30% zgrada ima building:levels, a raw/ghsl_built_h.tif ne postoji.")

    m = z.spratnost.isna()
    z.loc[m, "spratnost"] = z.loc[m, "tip"].map(PODRAZUMIJEVANA_SPRATNOST).fillna(3)
    z.loc[m, "spratnost_izvor"] = "podrazumijevano"
    z["spratnost"] = z.spratnost.clip(lower=1).round()

    # --- stambeni udio
    z["stambeni_udio"] = [stambeni_udio(t, l) for t, l in zip(z.tip, z.landuse)]

    # --- poslovno prizemlje: POI tačka unutar stambene zgrade
    poi_kol = [c for c in ("shop", "amenity", "office") if c in osm]
    poi = osm[(osm.geom_type == "Point") & osm[poi_kol].notna().any(axis=1)].to_crs(CRS_M)
    hit = gpd.sjoin(poi[["geometry"]], z[["geometry"]], predicate="within")
    z["poslovno_prizemlje"] = z.index.isin(hit.index_right) & (z.stambeni_udio > 0)

    z["zapremina"] = zapremina(z, 0)

    # --- opcina zgrade (po centroidu)
    jo = gpd.sjoin(cent, opcine, how="left", predicate="within")
    z["opcina"] = jo[~jo.index.duplicated()].opcina.reindex(z.index)

    # --- statistika (kontrolna tačka prije koraka 5)
    adresa = z["addr:street"].notna() & z["addr:housenumber"].notna()
    stambene = z.zapremina > 0

    def tabela(maska):
        g = z[maska].groupby("opcina")
        return pd.DataFrame({
            "zgrada": g.size(),
            "sa_spratnoscu_pct": g["building:levels"].apply(lambda s: s.map(broj).notna().mean() * 100),
            "sa_adresom_pct": g.apply(lambda d: (d["addr:street"].notna() & d["addr:housenumber"].notna()).mean() * 100,
                                      include_groups=False),
        }).round(1)

    stat = {
        "zgrada_ukupno": int(len(z)),
        "zgrada_stambenih": int(stambene.sum()),
        "sa_building_levels": int(nivoi.notna().sum()),
        "sa_building_levels_pct": round(udio_nivoi * 100, 1),
        "sa_height_pct": round(float(z["height"].notna().mean() * 100), 1),
        "sa_adresom": int(adresa.sum()),
        "sa_adresom_pct": round(float(adresa.mean() * 100), 1),
        "stambene_sa_adresom_pct": round(float(adresa[stambene].mean() * 100), 1) if stambene.any() else 0,
        "izvor_spratnosti": z.spratnost_izvor.value_counts().to_dict(),
        "ghsl_koristen": ghsl_koristen,
        "model_spratnosti_cv": model_cv,
        "po_tipu": z.tip.value_counts().head(20).to_dict(),
        "po_opcini_sve": tabela(np.ones(len(z), bool)).to_dict(orient="index"),
        "po_opcini_stambene": tabela(stambene.values).to_dict(orient="index"),
    }
    (INTERIM / "zgrade_statistika.json").write_text(
        json.dumps(stat, ensure_ascii=False, indent=2), encoding="utf-8")

    print("\n=== KONTROLNA TAČKA (prije koraka 5) ===")
    print(f"Zgrada: {stat['zgrada_ukupno']}, stambenih (zapremina > 0): {stat['zgrada_stambenih']}")
    print(f"Sa building:levels: {stat['sa_building_levels']} ({stat['sa_building_levels_pct']}%)")
    print(f"Sa adresom (addr:street + addr:housenumber): {stat['sa_adresom']} ({stat['sa_adresom_pct']}%)")
    print("Po općini (sve zgrade):")
    print(tabela(np.ones(len(z), bool)).to_string())
    print("Po općini (stambene):")
    print(tabela(stambene.values).to_string())

    kol = ["osm_id", "tip", "opcina", "landuse", "povrsina", "spratnost", "spratnost_izvor",
           "stambeni_udio", "poslovno_prizemlje", "zapremina", "addr:street", "addr:housenumber",
           "geometry"]
    z = z[kol].rename(columns={"addr:street": "addr_street", "addr:housenumber": "addr_housenumber"})
    z.to_file(INTERIM / "zgrade.gpkg", driver="GPKG")

    # landuse, parkovi, aerodrom za provjeru
    ost = osm.copy()
    ost["vrsta"] = None
    if "landuse" in ost:
        ost.loc[ost.landuse.notna(), "vrsta"] = "landuse=" + ost.landuse.astype(str)
    if "leisure" in ost:
        ost.loc[ost.leisure == "park", "vrsta"] = "park"
    if "aeroway" in ost:
        ost.loc[ost.aeroway == "aerodrome", "vrsta"] = "aerodrom"
    ost = poligoni(ost[ost.vrsta.notna()]).to_crs(CRS_M)[["vrsta", "geometry"]]
    ost.to_file(INTERIM / "landuse.gpkg", driver="GPKG")
    print(f"\nZapisano: interim/zgrade.gpkg ({len(z)}), interim/landuse.gpkg ({len(ost)})")


if __name__ == "__main__":
    main()
