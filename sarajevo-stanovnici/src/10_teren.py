"""Topografija: sjenčenje reljefa, izohipse i nagib po H3 polju.

Ulaz:  raw/cop_dem_n43e018.tif (Copernicus GLO-30 DEM, 30 m; preuzima se ako ne postoji),
       out/polja_h3.gpkg
Izlaz: out/teren_okvir.json        stvarni okvir slika (lon/lat)
       out/teren_h3.csv           visina (m n.v.) i nagib (%) po polju
       out/teren_reljef.png       sjenčenje + hipsometrijske boje, okvir u TEREN_OKVIR
       out/teren_sjena.png        samo sjenčenje (sivo), za preklapanje preko satelita
       out/teren_izohipse.geojson izohipse svakih 50 m (glavne svakih 250 m)

Copernicus DEM: © DLR e.V. 2010-2014 i © Airbus Defence and Space GmbH 2014-2018,
licenca Copernicus programa (slobodna upotreba uz navođenje izvora).
"""
from __future__ import annotations

import json

import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio
import requests
from rasterio.windows import from_bounds

from common import OUT, RAW

DEM_URL = ("https://copernicus-dem-30m.s3.amazonaws.com/Copernicus_DSM_COG_10_N43_00_E018_00_DEM/"
           "Copernicus_DSM_COG_10_N43_00_E018_00_DEM.tif")
TEREN_OKVIR = (18.2352, 43.8089, 18.53, 43.9783)  # isti okvir kao satelitska podloga
IZOHIPSE_M = 50
GLAVNE_M = 250


def dem() -> tuple[np.ndarray, rasterio.Affine]:
    f = RAW / "cop_dem_n43e018.tif"
    if not f.exists():
        r = requests.get(DEM_URL, timeout=600)
        r.raise_for_status()
        f.write_bytes(r.content)
    with rasterio.open(f) as src:
        win = from_bounds(*TEREN_OKVIR, transform=src.transform).round_offsets().round_lengths()
        z = src.read(1, window=win).astype(float)
        return z, src.window_transform(win)


def nagib_i_sjena(z, t, lat0):
    dy = abs(t.e) * 111_320
    dx = t.a * 111_320 * np.cos(np.radians(lat0))
    gy, gx = np.gradient(z, dy, dx)   # gy: prema jugu (red raste), gx: prema istoku
    nagib = np.hypot(gx, gy)
    # višesmjerno sjenčenje (315°, 270°, 0°, 225°), visina sunca 45°
    alt = np.radians(45)
    asp = np.arctan2(-gy, gx)  # smjer pada nagiba (matematički ugao)
    slope = np.arctan(nagib)
    sj = np.zeros_like(z)
    for az, w in ((315, 0.4), (270, 0.2), (0, 0.2), (225, 0.2)):
        a = np.radians(90 - az)
        sj += w * (np.sin(alt) * np.cos(slope) + np.cos(alt) * np.sin(slope) * np.cos(a - asp))
    return nagib * 100, np.clip(sj, 0, 1)


def hipsometrija(z):
    """Boja po visini: dolina zelenkasta -> brda oker -> vrhovi svijetli."""
    stops = [(400, (0.62, 0.74, 0.58)), (600, (0.80, 0.82, 0.62)), (800, (0.86, 0.78, 0.58)),
             (1000, (0.78, 0.66, 0.52)), (1300, (0.90, 0.88, 0.86))]
    zz = np.clip(z, stops[0][0], stops[-1][0])
    out = np.zeros(z.shape + (3,))
    for (z0, c0), (z1, c1) in zip(stops[:-1], stops[1:]):
        m = (zz >= z0) & (zz <= z1)
        f = ((zz - z0) / (z1 - z0))[m][:, None]
        out[m] = np.array(c0) * (1 - f) + np.array(c1) * f
    return out


def main() -> None:
    from PIL import Image

    z, t = dem()
    # Copernicus je model površine (DSM): uključuje krovove i krošnje. Izglađivanje
    # (~60 m) uklanja zgrade kao lažne nagibe, a zadržava oblik terena.
    from scipy.ndimage import gaussian_filter
    z = gaussian_filter(z, sigma=2)
    lat0 = (TEREN_OKVIR[1] + TEREN_OKVIR[3]) / 2
    nag, sj = nagib_i_sjena(z, t, lat0)

    ny, nx = z.shape
    (OUT / "teren_okvir.json").write_text(json.dumps(
        {"x0": t.c, "y1": t.f, "x1": t.c + nx * t.a, "y0": t.f + ny * t.e}))
    rel = hipsometrija(z) * (0.35 + 0.75 * sj[..., None])
    Image.fromarray((np.clip(rel, 0, 1) * 255).astype(np.uint8)).save(OUT / "teren_reljef.png", optimize=True)
    Image.fromarray((sj * 255).astype(np.uint8), mode="L").save(OUT / "teren_sjena.png", optimize=True)

    # izohipse
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    ny, nx = z.shape
    xs = t.c + t.a * (np.arange(nx) + 0.5)
    ys = t.f + t.e * (np.arange(ny) + 0.5)
    nivoi = np.arange(np.ceil(z.min() / IZOHIPSE_M) * IZOHIPSE_M, z.max(), IZOHIPSE_M)
    cs = plt.contour(xs, ys, z, levels=nivoi)
    feats = []
    for lvl, segs in zip(cs.levels, cs.allsegs):
        for seg in segs:
            if len(seg) < 8:
                continue
            seg = seg[::2] if len(seg) > 40 else seg
            feats.append({"type": "Feature", "properties": {"m": int(lvl), "glavna": int(lvl) % GLAVNE_M == 0},
                          "geometry": {"type": "LineString",
                                       "coordinates": [[round(float(a), 5), round(float(b), 5)] for a, b in seg]}})
    plt.close("all")
    (OUT / "teren_izohipse.geojson").write_text(json.dumps({"type": "FeatureCollection", "features": feats}))

    # po polju: srednja/min/max visina i srednji nagib
    p = gpd.read_file(OUT / "polja_h3.gpkg").to_crs(4326)
    from rasterio.features import rasterize
    lab = rasterize(((g, i + 1) for i, g in enumerate(p.geometry)), out_shape=z.shape, transform=t, fill=0)
    df = pd.DataFrame({"lab": lab.ravel(), "z": z.ravel(), "n": nag.ravel()})
    df = df[df.lab > 0]
    agg = df.groupby("lab").agg(visina_m=("z", "mean"), visina_min=("z", "min"), visina_max=("z", "max"),
                                nagib_pct=("n", "mean"))
    agg.index = p.h3_id.to_numpy()[agg.index - 1]
    agg.index.name = "h3_id"
    agg = agg.round(0).astype(int)
    agg.reset_index().to_csv(OUT / "teren_h3.csv", index=False)

    st = p.set_index("h3_id").stanovnici
    j = agg.join(st)
    w = j[j.stanovnici > 0]
    print(f"DEM {z.shape}, visina {z.min():.0f}–{z.max():.0f} m; izohipsi: {len(feats)}")
    print(f"Stanovnici po nagibu polja: "
          + ", ".join(f"{a}–{b}%: {w[(w.nagib_pct >= a) & (w.nagib_pct < b)].stanovnici.sum():,.0f}"
                      for a, b in ((0, 5), (5, 10), (10, 20), (20, 100))))
    print(f"Stanovnici iznad 700 m n.v.: {w[w.visina_m > 700].stanovnici.sum():,.0f}")


if __name__ == "__main__":
    main()
