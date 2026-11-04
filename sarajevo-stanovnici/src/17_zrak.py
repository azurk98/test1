"""Smog i magla zimi: izloženost inverziji po H3 polju (relativni indeksi, ne mjerenje).

Ulaz:  raw/cop_dem_n43e018.tif, raw/osm_grad.json (zgrade), raw/Sarajewo.osm.gz (rijeke),
       out/putevi.geojson, out/polja_h3.gpkg
       Mjerenja: FHMZ, Godišnji izvještaj o kvalitetu zraka u FBiH za 2025 (raw/zrak/izvjestaj-2025.pdf,
       tabela 22/26): srednje godišnje PM2.5. Koordinate stanica nisu objavljene; ovdje su
       približne (± ~300 m), pa se model poredi s prosjekom kruga od 300 m oko stanice.
Izlaz: out/zrak_h3.csv, out/zrak_stanice.csv (izmjerene vrijednosti i indeks na lokaciji stanice)

Napomena o modelu: prva verzija je uključivala gustinu malih kuća kao znak grijanja na čvrsto
gorivo; na mjerenjima je dala obrnut odnos (r = -0,42): oko stanice Bjelave je mnogo malih
kuća, a zrak je najčišći, jer centar uglavnom grije plin. Bez podataka o gasnoj mreži taj
faktor je izbačen, a PM2.5 se ne procjenjuje po polju (5 stanica nije dovoljno).

Model (procjena, ne mjerenje):
  visina iznad dna doline h = z - (najniža tačka terena u krugu 3 km)
  inverzija E = 1 / (1 + exp((h - H50) / W))  — udio inverzionih dana kad je mjesto ispod
                gornje granice inverzije; H50 = 200 m, W = 50 m (tipično za kotline)
  izvori: gustina malih kuća (otisak 40–250 m², pojedinačno grijanje, često drva i ugalj),
          zaglađena ~500 m; saobraćaj: dužina glavnih cesta, zaglađena ~150 m
  smog S = E · (1 + B·saobraćaj), relativni indeks 0–100 (2.–98. percentil polja)
  magla M = E · (0,6 + 0,4 · exp(-udaljenost od rijeke / 500 m))
"""
from __future__ import annotations

import gzip
import json
import xml.etree.ElementTree as ET

import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio
from rasterio.features import rasterize
from rasterio.windows import Window, from_bounds
from scipy.ndimage import distance_transform_edt, gaussian_filter, grey_opening, minimum_filter
from shapely.geometry import LineString, shape

from common import OUT, RAW

OKVIR = (18.20, 43.78, 18.56, 43.98)
H50, W = 200.0, 50.0
B_SAOBRACAJ = 0.5
DNO_RADIJUS_M = 3000

# 2025, FHMZ (srednja godišnja PM2.5, µg/m³); koordinate približne
STANICE = {
    "Sarajevo Bjelave": (43.8675, 18.4232, 26),
    "Sarajevo Otoka": (43.8487, 18.3640, 35),
    "Sarajevo Saraj Polje": (43.8478, 18.3355, 61),
    "Ilidža": (43.8304, 18.3110, 29),
    "Vogošća": (43.9030, 18.3450, 26),
}


def main() -> None:
    with rasterio.open(RAW / "cop_dem_n43e018.tif") as src:
        win = from_bounds(*OKVIR, transform=src.transform).round_offsets().round_lengths()
        win = win.intersection(Window(0, 0, src.width, src.height))
        dem = src.read(1, window=win).astype(float)
        t = src.window_transform(win)
    ny, nx = dem.shape
    lat0 = (OKVIR[1] + OKVIR[3]) / 2
    py, px = abs(t.e) * 111_320, t.a * 111_320 * np.cos(np.radians(lat0))
    z = gaussian_filter(grey_opening(dem, size=(3, 3)), 1)
    dno = gaussian_filter(minimum_filter(z, size=(int(2 * DNO_RADIJUS_M / py), int(2 * DNO_RADIJUS_M / px))), 15)
    h = z - dno
    E = 1 / (1 + np.exp((h - H50) / W))

    # male kuće (svi OSM objekti u ekstraktu, ne samo četiri općine)
    els = json.loads((RAW / "osm_grad.json").read_text())["elements"]
    pts = []
    for e in els:
        tg = e.get("tags", {})
        if e["type"] != "way" or "building" not in tg:
            continue
        if tg["building"] not in ("house", "detached", "yes", "residential", "semidetached_house", "terrace"):
            continue
        g = e.get("geometry") or []
        if len(g) < 4:
            continue
        lons = np.array([p["lon"] for p in g])
        lats = np.array([p["lat"] for p in g])
        povr = abs(np.sum(lons[:-1] * lats[1:] - lons[1:] * lats[:-1])) / 2 * px / t.a * py / abs(t.e)
        if 40 <= povr <= 250:
            pts.append((lons.mean(), lats.mean()))
    pts = np.array(pts)
    col = ((pts[:, 0] - t.c) / t.a).astype(int)
    row = ((pts[:, 1] - t.f) / t.e).astype(int)
    ok = (col >= 0) & (col < nx) & (row >= 0) & (row < ny)
    kuce = np.zeros((ny, nx))
    np.add.at(kuce, (row[ok], col[ok]), 1)
    kuce = gaussian_filter(kuce, sigma=(500 / py, 500 / px)) / (py * px / 1e6)  # kuća po km²
    pu = gpd.read_file(OUT / "putevi.geojson")
    tez = {"autoput": 1.0, "magistrala": 1.0, "primarna": 0.7, "sekundarna": 0.4}
    pu = pu[pu.klasa.isin(tez)]
    sao = rasterize(((g, tez[k]) for g, k in zip(pu.geometry, pu.klasa)), out_shape=(ny, nx), transform=t,
                    fill=0, all_touched=True, merge_alg=rasterio.enums.MergeAlg.add).astype(float)
    sao = gaussian_filter(sao, sigma=(150 / py, 150 / px))
    Kn = kuce / np.percentile(kuce[kuce > 0], 95)
    Tn = sao / np.percentile(sao[sao > 0], 95)
    S = E * (1 + B_SAOBRACAJ * Tn)

    # rijeke
    rijeke = []
    with gzip.open(RAW / "Sarajewo.osm.gz", "rb") as f:
        nodes = {}
        for _, el in ET.iterparse(f):
            if el.tag == "node":
                nodes[int(el.get("id"))] = (float(el.get("lon")), float(el.get("lat")))
                el.clear()
            elif el.tag == "way":
                tg = {c.get("k"): c.get("v") for c in el.findall("tag")}
                if tg.get("waterway") == "river":
                    p = [nodes[int(n.get("ref"))] for n in el.findall("nd") if int(n.get("ref")) in nodes]
                    if len(p) >= 2:
                        rijeke.append(LineString(p))
                el.clear()
            elif el.tag == "relation":
                el.clear()
    rr = rasterize(((g, 1) for g in rijeke), out_shape=(ny, nx), transform=t, fill=0, all_touched=True)
    d_rijeka = distance_transform_edt(rr == 0, sampling=(py, px))
    M = E * (0.6 + 0.4 * np.exp(-d_rijeka / 500))

    # kalibracija na stanice: prosjek kruga 300 m
    def krug(arr, la, lo, r=300):
        c0, r0 = (lo - t.c) / t.a, (la - t.f) / t.e
        yy, xx = np.mgrid[0:ny, 0:nx]
        m = ((yy - r0) * py) ** 2 + ((xx - c0) * px) ** 2 <= r * r
        return arr[m].mean()

    st = pd.DataFrame([(n, la, lo, pm, krug(S, la, lo), krug(E, la, lo), krug(h, la, lo), krug(Kn, la, lo),
                        krug(Tn, la, lo)) for n, (la, lo, pm) in STANICE.items()],
                      columns=["stanica", "lat", "lon", "pm25", "S", "E", "h", "kuce", "saobracaj"])
    from scipy.stats import spearmanr
    rho = spearmanr(st.S, st.pm25).statistic
    print(st.round(2).to_string(index=False))
    print(f"Spearman (indeks vs izmjereno PM2.5, 5 stanica): {rho:.2f}; bez Saraj Polja (66% obuhvat): "
          f"{spearmanr(st.S[st.stanica != 'Sarajevo Saraj Polje'], st.pm25[st.stanica != 'Sarajevo Saraj Polje']).statistic:.2f}")
    smin_st = None
    st.to_csv(OUT / "zrak_stanice.csv", index=False)

    # po polju
    polja = gpd.read_file(OUT / "polja_h3.gpkg").to_crs(4326)
    lab = rasterize(((g, i + 1) for i, g in enumerate(polja.geometry)), out_shape=(ny, nx), transform=t, fill=0)
    df = pd.DataFrame({"l": lab.ravel(), "h": h.ravel(), "E": E.ravel(), "S": S.ravel(), "M": M.ravel()})
    g = df[df.l > 0].groupby("l").mean()
    g.index = polja.h3_id.to_numpy()[g.index - 1]
    out = pd.DataFrame(index=polja.h3_id)
    out["iznad_dna_m"] = g.h.reindex(out.index).round(0)
    out["inverzija"] = g.E.reindex(out.index).round(2)
    smin, smax = np.percentile(g.S, [2, 98])
    out["smog_indeks"] = (100 * (g.S - smin) / (smax - smin)).clip(0, 100).reindex(out.index).round(0)
    out["magla_indeks"] = (100 * g.M / g.M.max()).reindex(out.index).round(0)
    out.reset_index().rename(columns={"index": "h3_id"}).to_csv(OUT / "zrak_h3.csv", index=False)

    j = out.join(polja.set_index("h3_id")[["opcina", "mz", "stanovnici"]])
    nas = j[j.stanovnici > 0]
    w = nas.stanovnici
    print("\nStanovnici po izloženosti inverziji: " + ", ".join(
        f"{a:.0%}–{b:.0%}: {w[(nas.inverzija >= a) & (nas.inverzija < b)].sum():,.0f}"
        for a, b in ((0, 0.25), (0.25, 0.5), (0.5, 0.75), (0.75, 0.9), (0.9, 1.01))))
    mz = nas.dropna(subset=["mz"]).groupby(["opcina", "mz"]).apply(
        lambda g_: pd.Series({"st": g_.stanovnici.sum(),
                              "smog": np.average(g_.smog_indeks, weights=g_.stanovnici),
                              "iznad_dna": np.average(g_.iznad_dna_m, weights=g_.stanovnici),
                              "inverzija": np.average(g_.inverzija, weights=g_.stanovnici),
                              "magla": np.average(g_.magla_indeks, weights=g_.stanovnici)}), include_groups=False)
    mz = mz[mz.st >= 500]
    print("\nNajčišći zrak (MZ):")
    print(mz.sort_values("smog").round(2).head(10).to_string())
    print("\nNajzagađenije (MZ):")
    print(mz.sort_values("smog", ascending=False).round(2).head(10).to_string())


if __name__ == "__main__":
    main()
