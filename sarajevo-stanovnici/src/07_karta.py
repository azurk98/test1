"""Interaktivna karta -> out/karta.html"""
from __future__ import annotations

import branca.colormap as cm
import folium
import geopandas as gpd
import numpy as np

from common import CRS_WGS, INTERIM, OUT


def main() -> None:
    p = gpd.read_file(OUT / "polja_h3.gpkg").to_crs(CRS_WGS)
    p = p[p.stanovnici > 0].copy()
    p["mz"] = p.mz.fillna("–")
    vmax = float(np.percentile(p.stanovnici, 98)) if len(p) else 1
    cmap = cm.LinearColormap(["#fff5eb", "#fdae6b", "#e6550d", "#7f2704"], vmin=0, vmax=vmax,
                             caption="Stanovnici po H3 polju (~0,1 km²)")

    c = p.geometry.union_all().centroid
    m = folium.Map(location=[c.y, c.x], zoom_start=13, tiles="CartoDB positron")
    folium.GeoJson(
        p[["h3_id", "opcina", "mz", "stanovnici", "stanovnici_min", "stanovnici_max",
           "d0_14", "d15_64", "d65plus", "pouzdanost", "izvor_tezine", "geometry"]],
        name="Stanovnici",
        style_function=lambda f: {
            "fillColor": cmap(min(f["properties"]["stanovnici"], vmax)),
            "color": "#555", "weight": 0.2, "fillOpacity": 0.75,
            "dashArray": "3" if f["properties"]["pouzdanost"] == "C" else None},
        tooltip=folium.GeoJsonTooltip(
            fields=["opcina", "mz", "stanovnici", "stanovnici_min", "stanovnici_max",
                    "d0_14", "d15_64", "d65plus", "pouzdanost", "izvor_tezine"],
            aliases=["Općina", "MZ", "Stanovnici", "Min", "Max", "0–14", "15–64", "65+",
                     "Pouzdanost", "Izvor težine"], localize=True),
    ).add_to(m)

    for ime, f in (("MZ granice", INTERIM / "mz_granice.gpkg"),
                   ("MZ Novi Grad (iz adresa)", INTERIM / "mz_novi_grad.gpkg")):
        if f.exists():
            g = gpd.read_file(f).to_crs(CRS_WGS)
            folium.GeoJson(g[["mz", "geometry"]], name=ime, show=False,
                           style_function=lambda _: {"fill": False, "color": "#225ea8", "weight": 1.5},
                           tooltip=folium.GeoJsonTooltip(fields=["mz"], aliases=["MZ"])).add_to(m)
    cmap.add_to(m)
    folium.LayerControl().add_to(m)
    m.get_root().html.add_child(folium.Element(
        '<div style="position:fixed;bottom:10px;left:10px;z-index:9999;background:white;padding:6px 8px;'
        'font:12px sans-serif;border-radius:4px;max-width:320px">Procjena (model), ne mjerenje. '
        'Zbir po općini = FZS 30.06.2026. Pouzdanost: A = poznat zbir MZ, B = samo zbir općine, '
        'C = uglavnom WorldPop (isprekidano).</div>'))
    m.save(OUT / "karta.html")
    print(f"-> out/karta.html ({len(p)} polja)")


if __name__ == "__main__":
    main()
