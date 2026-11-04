"""Koraci 1 i 3: H3 mreža, dijelovi polja (polje ∩ općina ∩ MZ) i WorldPop.

Ulaz:  raw/granice.json, raw/worldpop_2026.tif
Izlaz: interim/polja.gpkg (H3 heksagoni), interim/dijelovi_03.gpkg, interim/mz_granice.gpkg

MZ iz OSM-a: Stari Grad (svih 16, rupe se pripajaju susjednoj MZ, jer je
MZ kontrolni zbir) i Novo Sarajevo (samo za izvještaj, rupe ostaju bez MZ,
npr. Dolac Malta). Novi Grad dobija MZ u koraku 04.
"""
from __future__ import annotations

import geopandas as gpd
import h3
import numpy as np
import pandas as pd
from shapely.geometry import Polygon, mapping

from common import (CRS_M, CRS_WGS, H3_RES, INTERIM, popuni_mz, ucitaj_granice,
                    worldpop_po_dijelu)


def h3_polja(geom_wgs) -> gpd.GeoDataFrame:
    shape = h3.geo_to_h3shape(mapping(geom_wgs))
    try:
        cells = h3.h3shape_to_cells_experimental(shape, H3_RES, contain="overlap")
    except Exception:  # starije h3 verzije
        cells = h3.h3shape_to_cells(h3.geo_to_h3shape(mapping(geom_wgs.buffer(0.003))), H3_RES)
    geoms = [Polygon([(lng, lat) for lat, lng in h3.cell_to_boundary(c)]) for c in cells]
    return gpd.GeoDataFrame({"h3_id": list(cells)}, geometry=geoms, crs=CRS_WGS)


def main() -> None:
    opcine, mz_osm = ucitaj_granice()
    print(f"Općine: {len(opcine)}/4, MZ poligona iz OSM-a: {len(mz_osm)}")
    if len(opcine) != 4:
        raise SystemExit("Nedostaju granice općina u raw/granice.json")

    unija = opcine.union_all()
    polja = h3_polja(gpd.GeoSeries([unija], crs=CRS_M).to_crs(CRS_WGS).iloc[0]).to_crs(CRS_M)
    polja = polja[polja.intersects(unija)].reset_index(drop=True)
    polja.to_file(INTERIM / "polja.gpkg", driver="GPKG")
    print(f"H3 res {H3_RES} polja: {len(polja)}")

    # MZ zone po općini
    mz_sve = []
    for _, o in opcine.iterrows():
        m = mz_osm[mz_osm.opcina == o.opcina]
        if m.empty:
            continue
        p = popuni_mz(o.geometry, m, popuni_rupe=(o.opcina == "Stari Grad Sarajevo"))
        p["opcina"] = o.opcina
        mz_sve.append(p)
        pokr = p.area.sum() / o.geometry.area
        print(f"  {o.opcina}: {len(p)} MZ, pokrivenost {pokr:.1%}")
    mz = gpd.GeoDataFrame(pd.concat(mz_sve, ignore_index=True), crs=CRS_M) if mz_sve else \
        gpd.GeoDataFrame({"opcina": [], "mz": []}, geometry=[], crs=CRS_M)
    mz.to_file(INTERIM / "mz_granice.gpkg", driver="GPKG")

    # polje ∩ općina
    d = gpd.overlay(polja, opcine, how="intersection", keep_geom_type=True)
    # ∩ MZ (gdje postoji)
    if len(mz):
        sa = gpd.overlay(d, mz.drop(columns="opcina"), how="intersection", keep_geom_type=True)
        # MZ mora biti iz iste općine kao dio
        mz_op = mz.set_index("mz").opcina
        sa = sa[sa.mz.map(mz_op) == sa.opcina]
        bez = gpd.overlay(d, mz[["geometry"]], how="difference", keep_geom_type=True)
        bez["mz"] = None
        d = pd.concat([sa, bez], ignore_index=True)
    else:
        d["mz"] = None
    d = gpd.GeoDataFrame(d, geometry="geometry", crs=CRS_M).explode(ignore_index=True)
    d["mz"] = d.mz.fillna("")
    d = d[d.area > 1].dissolve(by=["h3_id", "opcina", "mz"], as_index=False)
    d["mz"] = d.mz.replace("", None)
    d["povrsina"] = d.area
    d["P"] = worldpop_po_dijelu(d)
    d = d[["h3_id", "opcina", "mz", "povrsina", "P", "geometry"]]
    d.to_file(INTERIM / "dijelovi_03.gpkg", driver="GPKG")
    print(f"Dijelova polja: {len(d)}, WorldPop ukupno: {d.P.sum():,.0f}")
    print(d.groupby("opcina").P.sum().round(0).to_string())


if __name__ == "__main__":
    main()
