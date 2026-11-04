"""Interaktivna karta -> out/karta.html

Podloge: Esri World Imagery (satelit, zadano), OpenTopoMap, OpenStreetMap;
preko njih sjenčenje reljefa (Esri World Hillshade) i izohipse iz koraka 10.
Slojevi: stanovnici, MZ granice, a ako postoje rezultati koraka 08/09 i
atraktivnost lokacije, postojeći supermarketi i predložene lokacije.
Karta učitava podloge s njihovih servera (treba internet); Esri World Imagery
podliježe Esrijevim uslovima korištenja.
"""
from __future__ import annotations

import branca.colormap as cm
import folium
import geopandas as gpd
import numpy as np
import pandas as pd

from common import CRS_WGS, INTERIM, OUT


def main() -> None:
    p = gpd.read_file(OUT / "polja_h3.gpkg").to_crs(CRS_WGS)
    p = p[p.stanovnici > 0].copy()
    p["mz"] = p.mz.fillna("–")
    vmax = float(np.percentile(p.stanovnici, 98)) if len(p) else 1
    cmap = cm.LinearColormap(["#fff5eb", "#fdae6b", "#e6550d", "#7f2704"], vmin=0, vmax=vmax,
                             caption="Stanovnici po H3 polju (~0,1 km²)")

    c = p.geometry.union_all().centroid
    m = folium.Map(location=[c.y, c.x], zoom_start=13, tiles=None)
    folium.TileLayer(
        tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
        attr="Tiles © Esri — Source: Esri, Maxar, Earthstar Geographics, and the GIS User Community",
        name="Satelit (Esri)", max_zoom=19).add_to(m)
    folium.TileLayer("https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png", name="Topografska (OpenTopoMap)",
                     attr="Map data © OpenStreetMap contributors, SRTM | Style © OpenTopoMap (CC-BY-SA)",
                     max_zoom=17, show=False).add_to(m)
    folium.TileLayer("OpenStreetMap", name="OpenStreetMap", show=False).add_to(m)
    folium.TileLayer(
        tiles="https://server.arcgisonline.com/ArcGIS/rest/services/Elevation/World_Hillshade/MapServer/tile/{z}/{y}/{x}",
        attr="Hillshade © Esri", name="Sjenčenje reljefa (Esri)", overlay=True, show=True, opacity=0.7,
        max_zoom=16, className="sjencenje").add_to(m)
    m.get_root().header.add_child(folium.Element(
        "<style>.sjencenje{mix-blend-mode:multiply}</style>"))
    izo = OUT / "teren_izohipse.geojson"
    if izo.exists():
        folium.GeoJson(
            str(izo), name="Izohipse (50 m, Copernicus DEM)", show=True,
            style_function=lambda f: {"color": "#ffffff", "weight": 1.4 if f["properties"]["glavna"] else 0.6,
                                      "opacity": 0.8 if f["properties"]["glavna"] else 0.45},
            tooltip=folium.GeoJsonTooltip(fields=["m"], aliases=["Nadmorska visina (m)"]),
        ).add_to(m)
    folium.GeoJson(
        p[["h3_id", "opcina", "mz", "stanovnici", "stanovnici_min", "stanovnici_max",
           "d0_14", "d15_64", "d65plus", "pouzdanost", "izvor_tezine", "geometry"]],
        name="Stanovnici",
        style_function=lambda f: {
            "fillColor": cmap(min(f["properties"]["stanovnici"], vmax)),
            "color": "#fff", "weight": 0.3,
            "fillOpacity": 0.15 + 0.6 * min(f["properties"]["stanovnici"] / vmax, 1),
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
    pp = OUT / "putevi.geojson"
    if pp.exists():
        boje = {"autoput": ("#f4a259", 4), "glavna": ("#ffd166", 3), "sekundarna": ("#fff1a8", 2.2),
                "tercijarna": ("#ffffff", 1.6), "ulica": ("#ffffff", 0.8), "tramvaj": ("#e63946", 2)}
        folium.GeoJson(
            str(pp), name="Mreža puteva (OSM)", show=True,
            style_function=lambda f: {"color": boje[f["properties"]["klasa"]][0],
                                      "weight": boje[f["properties"]["klasa"]][1],
                                      "opacity": 0.6 if f["properties"]["klasa"] == "ulica" else 0.95,
                                      "dashArray": "6 4" if f["properties"]["klasa"] == "tramvaj" else None},
            tooltip=folium.GeoJsonTooltip(fields=["ime", "klasa"], aliases=["Naziv", "Klasa"]),
        ).add_to(m)
    dp = OUT / "dostupnost_h3.gpkg"
    if dp.exists():
        a = gpd.read_file(dp).to_crs(CRS_WGS)
        acm = cm.LinearColormap(["#f7fcb9", "#78c679", "#238443", "#004529"], vmin=0, vmax=100,
                                caption="Atraktivnost lokacije (0–100)")
        a["mz"] = a.mz.fillna("–")
        folium.GeoJson(
            a[["opcina", "mz", "atraktivnost", "pjesice_10", "auto_10", "poi_10min", "stanica_m", "geometry"]],
            name="Atraktivnost lokacije", show=False,
            style_function=lambda f: {"fillColor": acm(f["properties"]["atraktivnost"]), "color": "#fff",
                                      "weight": 0.3, "fillOpacity": 0.6},
            tooltip=folium.GeoJsonTooltip(
                fields=["opcina", "mz", "atraktivnost", "pjesice_10", "auto_10", "poi_10min", "stanica_m"],
                aliases=["Općina", "MZ", "Atraktivnost", "Stanovnici 10 min pješice",
                         "Stanovnici 10 min autom", "Trgovine/usluge 10 min", "Stanica (m)"], localize=True),
        ).add_to(m)
    tp = OUT / "supermarket_trgovine.csv"
    kp = OUT / "supermarket_kandidati.csv"
    if tp.exists() and kp.exists():
        fg = folium.FeatureGroup(name="Postojeći supermarketi", show=False)
        t = pd.read_csv(tp)
        if "izvor" in t:  # Google Places se ne smije prikazivati na karti koja nije Google karta
            t = t[t.izvor != "google"]
        for r in t[t.tip.isin(["supermarket", "mall", "department_store"])].itertuples():
            folium.CircleMarker([r.lat, r.lon], radius=3, color="#fff", weight=1, fill=True,
                                fill_color="#222", fill_opacity=0.9,
                                tooltip=f"{r.ime if isinstance(r.ime, str) else r.tip}").add_to(fg)
        fg.add_to(m)
        k = pd.read_csv(kp)
        for strat, ime, boja in (("bijela_mrlja", "Supermarket: bijele mrlje", "#d08a3c"),
                                 ("najveci_promet", "Supermarket: najveći promet", "#1d6b74")):
            fg = folium.FeatureGroup(name=ime, show=False)
            for r in k[k.strategija == strat].itertuples():
                folium.Marker(
                    [r.lat, r.lon],
                    icon=folium.DivIcon(html=f'<div style="width:22px;height:22px;border-radius:50%;background:{boja};'
                                             f'color:#fff;font:600 11px sans-serif;display:grid;place-items:center;'
                                             f'border:2px solid #fff">{r.rang}</div>', icon_anchor=(11, 11)),
                    tooltip=(f"#{r.rang} {r.mz} — kupaca ~{r.kupci_procjena:,}; 10 min pješice {r.stanovnici_10min_pjesice:,}; "
                             f"bez supermarketa {r.od_toga_bez_supermarketa_10min:,}; najbliži supermarket {r.najblizi_supermarket_m} m"
                             ).replace(",", "."),
                ).add_to(fg)
            fg.add_to(m)
    cmap.add_to(m)
    folium.LayerControl(collapsed=False).add_to(m)
    m.get_root().html.add_child(folium.Element(
        '<div style="position:fixed;bottom:10px;left:10px;z-index:9999;background:white;padding:6px 8px;'
        'font:12px sans-serif;border-radius:4px;max-width:320px">Procjena (model), ne mjerenje. '
        'Zbir po općini = FZS 30.06.2026. Pouzdanost: A = poznat zbir MZ, B = samo zbir općine, '
        'C = uglavnom WorldPop (isprekidano).</div>'))
    m.save(OUT / "karta.html")
    print(f"-> out/karta.html ({len(p)} polja)")


if __name__ == "__main__":
    main()
