"""Mreža puteva za prikaz na karti -> out/putevi.geojson

Iz OSM ekstrakta (raw/Sarajewo.osm.gz) uzima ceste i tramvajsku prugu u okviru
četiri općine (+ ~1 km), razvrstava ih u klase za prikaz i pojednostavljuje
geometriju (~5 m). Pješačke staze, stepenice i servisne ceste se ne crtaju.

klasa: autoput (motorway/trunk), glavna (primary), sekundarna (secondary),
       tercijarna (tertiary), ulica (residential/unclassified/living_street),
       tramvaj (railway=tram)
"""
from __future__ import annotations

import gzip
import json
import xml.etree.ElementTree as ET

import geopandas as gpd
from shapely.geometry import LineString, box

from common import CRS_WGS, OUT, RAW

KLASA = {
    "motorway": "autoput", "motorway_link": "autoput", "trunk": "autoput", "trunk_link": "autoput",
    "primary": "glavna", "primary_link": "glavna",
    "secondary": "sekundarna", "secondary_link": "sekundarna",
    "tertiary": "tercijarna", "tertiary_link": "tercijarna",
    "residential": "ulica", "unclassified": "ulica", "living_street": "ulica", "road": "ulica",
}


def main() -> None:
    polja = gpd.read_file(OUT / "polja_h3.gpkg").to_crs(CRS_WGS)
    x0, y0, x1, y1 = polja.total_bounds
    okvir = box(x0 - 0.012, y0 - 0.009, x1 + 0.012, y1 + 0.009)

    nodes, rows = {}, []
    with gzip.open(RAW / "Sarajewo.osm.gz", "rb") as f:
        for _, el in ET.iterparse(f):
            if el.tag == "node":
                nodes[int(el.get("id"))] = (float(el.get("lon")), float(el.get("lat")))
                el.clear()
            elif el.tag == "way":
                t = {c.get("k"): c.get("v") for c in el.findall("tag")}
                k = "tramvaj" if t.get("railway") == "tram" else KLASA.get(t.get("highway"))
                if k:
                    pts = [nodes[int(n.get("ref"))] for n in el.findall("nd") if int(n.get("ref")) in nodes]
                    if len(pts) >= 2:
                        rows.append({"klasa": k, "ime": t.get("name", ""), "geometry": LineString(pts)})
                el.clear()
            elif el.tag == "relation":
                el.clear()

    g = gpd.GeoDataFrame(rows, crs=CRS_WGS)
    g = g[g.intersects(okvir)].copy()
    g["geometry"] = g.geometry.intersection(okvir).simplify(0.00005)
    g = g[~g.geometry.is_empty]
    g = g.explode(ignore_index=True)
    g = g[g.geom_type == "LineString"]
    g.to_file(OUT / "putevi.geojson", driver="GeoJSON", COORDINATE_PRECISION=5)
    duz = g.to_crs(32634).assign(km=lambda d: d.length / 1000).groupby("klasa").km.sum().round(0)
    print(f"-> out/putevi.geojson ({len(g)} dionica)")
    print(duz.to_string())


if __name__ == "__main__":
    main()
