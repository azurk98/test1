"""Provjera trase linije S (28_sjeverna_linija.py) za midibus 8–9 m: nagibi, krivine, širina, ulice.

Ulaz:  out/sjeverna_linija.geojson, raw/cop_dem_n43e018.tif (preko 10_teren), out/ulice_dionice.gpkg
       (15_ulice: koridor = razmak između zgrada), raw/Sarajewo.osm.gz (oznake ulica)
Izlaz: out/provjera_trase_50m.csv      dionice od 50 m s pokazateljima i ocjenom
       out/provjera_trase_tacke.csv    mjesta za provjeru na terenu (spojene uzastopne dionice)
       out/provjera_trase.geojson      dionice (za kartu)

Pragovi za midibus (pretpostavke, provjeriti s prevoznikom):
  nagib na 50 m: 10–15% provjeriti (zima), > 15% problem; na 100 m > 12% problem
  koridor (razmak zgrada): < 5,5 m problem (nema mimoilaženja), 5,5–8 m provjeriti
  skretanje (ugao na ±10 m): > 120° serpentina (problem), 90–120° provjeriti; obično skretanje
  na raskrsnici (~90°) nije problem
  povratak istim putem (skretanje > 150° na 20 m): greška trase, ispraviti ručno
  stanica: 20 m s nagibom ≤ 4% i koridorom ≥ 8 m
Visine: FGU model reljefa FBiH (DEM_2012, ~5 m, tlo, cijeli metri; javni ArcGIS servis geoportala
katastar.ba, upit svakih 15 m, keš raw/fgu/visine_trase.json): nagib na 100 m ~±1%, na 50 m ~±2%.
Bez mreže/keša: VISINE=cop koristi Copernicus GLO-30 (30 m): nagib na 100 m ±3–4%. Koridor ne zna za ograde, zidove i parkirana auta.
"""
from __future__ import annotations

import gzip
import importlib.util
import xml.etree.ElementTree as ET
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
from scipy.ndimage import gaussian_filter, grey_opening, map_coordinates
from scipy.spatial import cKDTree
from shapely.geometry import LineString, Point

from common import OSM_IME
from common import CRS_M, CRS_WGS, OUT, RAW


def _uvezi(ime, fajl):
    s = importlib.util.spec_from_file_location(ime, Path(__file__).with_name(fajl))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


import os
KORAK = 10.0
VISINE = os.environ.get("VISINE", "cop")   # "fgu" (FGU DEM FBiH, ~5 m; traži dozvolu za upite) ili "cop" (Copernicus 30 m)
DIONICA = 50.0


def visine_fgu(s_m, korak=15.0):
    """Visina tla iz FGU modela reljefa FBiH (DEM_2012, ~5 m, cijeli metri) duž trase, upitom
    'identify' na javnom ArcGIS servisu geoportala katastar.ba (1 upit u sekundi, keš u raw/fgu/)."""
    import json
    import time
    import requests
    from pyproj import Transformer
    keš = RAW / "fgu" / "visine_trase.json"
    c = json.loads(keš.read_text()) if keš.exists() else {}
    tr = Transformer.from_crs(CRS_M, 31276, always_xy=True)
    dd = np.arange(0, s_m.length, korak)
    url = "https://static.katastar.ba/arcgis/rest/services/DEM_2012/MapServer/identify"
    zz = []
    for i, x in enumerate(dd):
        p = s_m.interpolate(x)
        X, Y = tr.transform(p.x, p.y)
        k = f"{X:.1f},{Y:.1f}"
        if k not in c:
            q = {"geometry": f"{X},{Y}", "geometryType": "esriGeometryPoint", "sr": 31276, "layers": "all:0",
                 "tolerance": 0, "mapExtent": f"{X-50},{Y-50},{X+50},{Y+50}", "imageDisplay": "100,100,96",
                 "returnGeometry": "false", "f": "json"}
            for pokusaj in range(3):
                try:
                    r = requests.get(url, params=q, timeout=60,
                                     headers={"User-Agent": "sarajevo-stanovnici research (non-commercial)"})
                    res = r.json().get("results", [])
                    c[k] = float(res[0]["attributes"]["Pixel Value"]) if res else None
                    break
                except Exception as ex:  # noqa: BLE001
                    print("  ponovo:", ex, flush=True); time.sleep(5)
            time.sleep(1.0)
            if i % 100 == 0:
                keš.parent.mkdir(parents=True, exist_ok=True)
                keš.write_text(json.dumps(c)); print(f"  FGU visine {i}/{len(dd)}", flush=True)
        zz.append(c.get(k))
    keš.write_text(json.dumps(c))
    zz = np.array([np.nan if v is None else v for v in zz], float)
    return dd, zz


def oznake_ulica(okvir):
    """OSM ceste u okviru: oznake važne za autobus."""
    nodes, rows = {}, []
    with gzip.open(RAW / OSM_IME, "rb") as f:
        for _, el in ET.iterparse(f):
            if el.tag == "node":
                nodes[int(el.get("id"))] = (float(el.get("lon")), float(el.get("lat")))
                el.clear()
            elif el.tag == "way":
                t = {c.get("k"): c.get("v") for c in el.findall("tag")}
                if "highway" in t:
                    p = [nodes[int(n.get("ref"))] for n in el.findall("nd") if int(n.get("ref")) in nodes]
                    if len(p) >= 2:
                        g = LineString(p)
                        if g.intersects(okvir):
                            rows.append({"highway": t["highway"], "ime": t.get("name", ""),
                                         "podloga": t.get("surface", ""), "sirina_osm": t.get("width", ""),
                                         "trake": t.get("lanes", ""), "jednosmjerna": t.get("oneway", ""),
                                         "trotoar": t.get("sidewalk", ""), "max_tezina": t.get("maxweight", ""),
                                         "geometry": g})
                el.clear()
            elif el.tag == "relation":
                el.clear()
    return gpd.GeoDataFrame(rows, crs=CRS_WGS).to_crs(CRS_M)


def main() -> None:
    s = gpd.read_file(OUT / "sjeverna_linija.geojson").to_crs(CRS_M).geometry.iloc[0]
    L = s.length
    d = np.arange(0, L, KORAK)
    pts = [s.interpolate(x) for x in d]
    xy = np.array([[p.x, p.y] for p in pts])
    ll = gpd.GeoSeries(pts, crs=CRS_M).to_crs(CRS_WGS)

    # visine (tlo: najniža tačka u prozoru 3×3, blago zaglađeno), bilinearno
    ter = _uvezi("ter", "10_teren.py")
    z, t = ter.dem()
    z = gaussian_filter(grey_opening(z, size=(3, 3)), 0.7)
    col = (ll.x.to_numpy() - t.c) / t.a - 0.5
    row = (ll.y.to_numpy() - t.f) / t.e - 0.5
    h = map_coordinates(z, [row, col], order=1)
    izvor_visina = "Copernicus GLO-30"
    if VISINE == "fgu":
        dd_f, z_f = visine_fgu(s)
        ok_ = np.isfinite(z_f)
        if ok_.sum() > 10:
            # cijeli metri: blago zagladi (prosjek 3 susjedne tačke) pa interpoliraj na korak 10 m
            zs = pd.Series(z_f).interpolate(limit_direction="both").rolling(3, center=True, min_periods=1).mean().to_numpy()
            h_cop = h.copy()
            h = np.interp(d, dd_f, zs)
            izvor_visina = "FGU DEM FBiH (~5 m)"
            print(f"FGU visine: {ok_.sum()} tačaka; razlika prema Copernicusu: medijan "
                  f"{np.median(np.abs(h - h_cop)):.1f} m, 90. percentil {np.percentile(np.abs(h - h_cop), 90):.1f} m")

    def nagib(win):
        k = int(round(win / 2 / KORAK))
        out = np.full(len(d), np.nan)
        out[k:len(d) - k] = (h[2 * k:] - h[:len(d) - 2 * k]) / (2 * k * KORAK)
        return np.abs(out)

    n20, n50, n100 = nagib(20), nagib(50), nagib(100)

    # krivine: polumjer kružnice kroz tačke na −10, 0, +10 m; povratak = skretanje > 150°
    R = np.full(len(d), np.inf)
    okret = np.zeros(len(d), bool)
    for i in range(1, len(d) - 1):
        a, b, c = xy[i - 1], xy[i], xy[i + 1]
        ab, bc, ca = np.linalg.norm(b - a), np.linalg.norm(c - b), np.linalg.norm(a - c)
        cross = abs((b - a)[0] * (c - a)[1] - (b - a)[1] * (c - a)[0])
        if cross > 1e-6:
            R[i] = ab * bc * ca / (2 * cross)
        v1, v2 = b - a, c - b
        cosang = v1 @ v2 / max(np.linalg.norm(v1) * np.linalg.norm(v2), 1e-9)
        okret[i] = cosang < np.cos(np.radians(150))

    # koridor (razmak zgrada) iz 15_ulice
    ud = gpd.read_file(OUT / "ulice_dionice.gpkg").to_crs(CRS_M)
    ud = ud[ud.intersects(s.buffer(30))]
    j = gpd.sjoin_nearest(gpd.GeoDataFrame(geometry=pts, crs=CRS_M), ud[["koridor", "mak", "geometry"]],
                          max_distance=10, how="left")
    j = j[~j.index.duplicated()]
    koridor = j.koridor.to_numpy(float)
    mak = j.mak.fillna(False).astype(bool).to_numpy()

    os_ = oznake_ulica(gpd.GeoSeries([s], crs=CRS_M).to_crs(CRS_WGS)[0].buffer(0.0005))
    jo = gpd.sjoin_nearest(gpd.GeoDataFrame(geometry=pts, crs=CRS_M), os_, max_distance=8, how="left")
    jo = jo[~jo.index.duplicated()]

    # tačka po tačka: ocjena 0 ok, 1 provjeriti, 2 problem; razlozi
    raz = [[] for _ in d]
    sev = np.zeros(len(d), int)

    def oznaci(m, ocjena, tekst):
        for i in np.where(m)[0]:
            raz[i].append(tekst)
            sev[i] = max(sev[i], ocjena)

    oznaci(n50 > 0.15, 2, "nagib > 15% (50 m)")
    oznaci((n50 > 0.10) & (n50 <= 0.15), 1, "nagib 10–15% (50 m, zima)")
    oznaci(n100 > 0.12, 2, "nagib > 12% (100 m)")
    oznaci(koridor < 5.5, 2, "razmak zgrada < 5,5 m")
    oznaci((koridor >= 5.5) & (koridor < 8), 1, "razmak zgrada 5,5–8 m")
    # ugao skretanja na ±10 m: obično skretanje na raskrsnici je ~90°; serpentina > 120°
    ug = np.zeros(len(d))
    for i in range(1, len(d) - 1):
        v1, v2 = xy[i] - xy[i - 1], xy[i + 1] - xy[i]
        ug[i] = np.degrees(np.arccos(np.clip(v1 @ v2 / max(np.linalg.norm(v1) * np.linalg.norm(v2), 1e-9), -1, 1)))
    oznaci((ug > 120) & ~okret, 2, "serpentina (skretanje > 120°)")
    oznaci((ug > 90) & (ug <= 120), 1, "oštro skretanje 90–120°")
    oznaci(okret, 2, "trasa se vraća istim putem (ispraviti)")
    oznaci(mak, 1, "makadam")
    pod = jo.podloga.fillna("").to_numpy()
    oznaci(np.isin(pod, ["unpaved", "gravel", "dirt", "ground", "compacted", "fine_gravel"]), 1, "neasfaltirano (OSM)")
    oznaci(jo.highway.fillna("").isin(["track", "service", "living_street", "pedestrian"]).to_numpy(), 1,
           "pristupni put / stambena zona (OSM)")
    oznaci(jo.jednosmjerna.fillna("").isin(["yes", "-1"]).to_numpy(), 1, "jednosmjerna (povratak drugom ulicom)")
    stanica_ok = (n20 <= 0.04) & (np.nan_to_num(koridor, nan=99) >= 8)

    # dionice od 50 m
    k = int(DIONICA / KORAK)
    rows = []
    for a in range(0, len(d), k):
        b = min(a + k, len(d))
        sl = slice(a, b)
        rz = sorted({x for lst in raz[a:b] for x in lst})
        imena = [x for x in jo.ime.fillna("").iloc[a:b] if x]
        rows.append({"od_m": int(d[a]), "do_m": int(d[b - 1] + KORAK), "ulica": max(set(imena), key=imena.count) if imena else "",
                     "visina_m": round(float(np.nanmean(h[sl]))), "nagib_50m_max_pct": round(float(np.nanmax(n50[sl]) * 100), 1)
                     if np.isfinite(n50[sl]).any() else None,
                     "nagib_100m_max_pct": round(float(np.nanmax(n100[sl]) * 100), 1) if np.isfinite(n100[sl]).any() else None,
                     "skretanje_max_stepeni": round(float(np.max(ug[sl]))),
                     "koridor_min_m": round(float(np.nanmin(koridor[sl])), 1) if np.isfinite(koridor[sl]).any() else None,
                     "podloga_osm": ",".join(sorted({x for x in pod[sl] if x})), "moguca_stanica": bool(stanica_ok[sl].any()),
                     "ocjena": int(sev[sl].max()), "razlozi": "; ".join(rz),
                     "lon": round(float(ll.x.iloc[(a + b) // 2]), 5), "lat": round(float(ll.y.iloc[(a + b) // 2]), 5),
                     "geometry": LineString(xy[a:b + 1] if b < len(d) else xy[a:b]) if b - a >= 2 else Point(xy[a])})
    seg = gpd.GeoDataFrame(rows, crs=CRS_M)
    seg.drop(columns="geometry").to_csv(OUT / "provjera_trase_50m.csv", index=False)
    seg[seg.geometry.geom_type == "LineString"].to_crs(CRS_WGS).to_file(OUT / "provjera_trase.geojson", driver="GeoJSON",
                                                                         COORDINATE_PRECISION=5)
    # mjesta za provjeru: uzastopne dionice s ocjenom ≥ 1
    mj, cur = [], None
    for r in seg.itertuples():
        if r.ocjena >= 1:
            if cur and r.od_m - cur["do_m"] <= 0:
                cur["do_m"] = r.do_m; cur["ocjena"] = max(cur["ocjena"], r.ocjena)
                cur["razlozi"] |= set(r.razlozi.split("; ")); cur["ulice"].add(r.ulica)
            else:
                if cur:
                    mj.append(cur)
                cur = {"od_m": r.od_m, "do_m": r.do_m, "ocjena": r.ocjena, "razlozi": set(r.razlozi.split("; ")),
                       "ulice": {r.ulica}, "lon": r.lon, "lat": r.lat}
        elif cur:
            mj.append(cur); cur = None
    if cur:
        mj.append(cur)
    tm = pd.DataFrame([{"mjesto": i + 1, "od_km": round(m["od_m"] / 1000, 2), "duzina_m": m["do_m"] - m["od_m"],
                        "ocjena": "problem" if m["ocjena"] == 2 else "provjeriti",
                        "ulica": ", ".join(sorted(x for x in m["ulice"] if x)) or "(bez naziva)",
                        "razlozi": "; ".join(sorted(m["razlozi"])), "lat": m["lat"], "lon": m["lon"]} for i, m in enumerate(mj)])
    tm.to_csv(OUT / "provjera_trase_tacke.csv", index=False)

    duz = seg.do_m - seg.od_m
    print(f"Visine: {izvor_visina}")
    print(f"Trasa {L / 1000:.1f} km: ok {duz[seg.ocjena == 0].sum() / 1000:.1f} km, provjeriti "
          f"{duz[seg.ocjena == 1].sum() / 1000:.1f} km, problem {duz[seg.ocjena == 2].sum() / 1000:.1f} km")
    print(f"Mjesta za provjeru: {len(tm)} (problem {int((tm.ocjena == 'problem').sum())}); "
          f"dionica s mogućom stanicom: {int(seg.moguca_stanica.sum())} od {len(seg)}")
    vsi = {}
    for lst in raz:
        for x in lst:
            vsi[x] = vsi.get(x, 0) + KORAK
    print("Po razlogu (m trase):", {k_: int(v) for k_, v in sorted(vsi.items(), key=lambda x: -x[1])})
    pd.set_option("display.width", 250); pd.set_option("display.max_colwidth", 80)
    print(tm.drop(columns=["lat", "lon"]).head(40).to_string(index=False))


if __name__ == "__main__":
    main()
