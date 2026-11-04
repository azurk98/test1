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
    """Stambena zapremina (m² poda) uz pomak podrazumijevane spratnosti."""
    sprat = z.spratnost + np.where(z.spratnost_izvor == "podrazumijevano", pomak, 0)
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
    print(f"Zgrade u 4 općine: {ukupno_prije}, nakon filtra < {MIN_POVRSINA_ZGRADE} m²: {len(z)}")

    for kol in ("building:levels", "height", "addr:street", "addr:housenumber"):
        if kol not in z:
            z[kol] = None
    z["tip"] = z["building"].astype(str).str.strip().str.lower()

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
    if udio_nivoi < 0.30:
        if ghsl.exists():
            import rasterio
            with rasterio.open(ghsl) as src:
                m = z.spratnost.isna()
                pts = cent.loc[m].to_crs(src.crs)
                vals = np.array([v[0] for v in src.sample(zip(pts.x, pts.y))], float)
                vals[(vals <= 0) | (vals == src.nodata)] = np.nan
                z.loc[m, "spratnost"] = vals / 3.0
                z.loc[m & z.spratnost.notna(), "spratnost_izvor"] = "ghsl"
                ghsl_koristen = True
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
