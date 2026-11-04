"""Sati sunca zimi po H3 polju (zasjenjenje terenom).

Ulaz:  raw/cop_dem_n43e018.tif (Copernicus DEM, cijela pločica 43–44° N, 18–19° E), out/polja_h3.gpkg
Izlaz: out/sunce_h3.csv  sati direktnog sunca 21. decembra i 21. januara, izlazak i zalazak sunca
                         iza okolnih brda, i astronomski maksimum (ravan horizont)

Postupak: položaj sunca svakih 5 minuta (NOAA formule, lokalno vrijeme UTC+1). Za 7 tačaka po
polju (središta H3 polja rezolucije 10) prati se zraka prema suncu do 25 km i traži najveći
ugao horizonta (teren + zakrivljenost Zemlje uz refrakciju 0,13). Sunce je vidljivo kad je iznad
horizonta i više od 1°. Teren: DSM bez zgrada (najniža tačka u 90 m) i blago izglađen; posmatrač
2 m iznad tla. Računa se vedar dan: magla i oblaci (česti zimi u dolini) nisu uključeni.
"""
from __future__ import annotations

import datetime as dt

import geopandas as gpd
import h3
import numpy as np
import pandas as pd
import rasterio
from rasterio.windows import Window, from_bounds
from scipy.ndimage import gaussian_filter, grey_opening

from common import H3_RES, OUT, RAW

DATUMI = {"21dec": dt.date(2026, 12, 21), "21jan": dt.date(2027, 1, 21)}
KORAK_MIN = 5
DOMET_M = 25_000
VISINA_OKA = 2.0
MIN_UGAO = 1.0
R_ZEMLJE = 6_371_000.0
REFRAKCIJA = 0.13
UTC_POMAK = 1  # zimsko vrijeme, CET


def polozaj_sunca(lat: float, lon: float, datum: dt.date, minute_lokalno: np.ndarray):
    """Elevacija i azimut sunca (stepeni; azimut od sjevera u smjeru kazaljke) — NOAA aproksimacija."""
    n = datum.timetuple().tm_yday
    g = 2 * np.pi / 365 * (n - 1 + (minute_lokalno / 60 - UTC_POMAK - 12) / 24)
    eqt = 229.18 * (0.000075 + 0.001868 * np.cos(g) - 0.032077 * np.sin(g)
                    - 0.014615 * np.cos(2 * g) - 0.040849 * np.sin(2 * g))
    dekl = (0.006918 - 0.399912 * np.cos(g) + 0.070257 * np.sin(g) - 0.006758 * np.cos(2 * g)
            + 0.000907 * np.sin(2 * g) - 0.002697 * np.cos(3 * g) + 0.00148 * np.sin(3 * g))
    sun_vr = minute_lokalno + eqt + 4 * lon - 60 * UTC_POMAK
    ha = np.radians(sun_vr / 4 - 180)
    la = np.radians(lat)
    cz = np.sin(la) * np.sin(dekl) + np.cos(la) * np.cos(dekl) * np.cos(ha)
    zen = np.arccos(np.clip(cz, -1, 1))
    az = np.degrees(np.arctan2(np.sin(ha), np.cos(ha) * np.sin(la) - np.tan(dekl) * np.cos(la))) + 180
    return 90 - np.degrees(zen), az % 360


def main() -> None:
    polja = gpd.read_file(OUT / "polja_h3.gpkg")
    lat0, lon0 = 43.86, 18.41
    with rasterio.open(RAW / "cop_dem_n43e018.tif") as src:
        okvir = (lon0 - 0.45, lat0 - 0.33, lon0 + 0.45, lat0 + 0.33)  # ~ ±35 km
        win = from_bounds(*okvir, transform=src.transform).round_offsets().round_lengths()
        # okvir mora ostati unutar pločice (inače čitanje i transformacija ne odgovaraju jedno drugom);
        # zimi sunce dolazi s juga, a jug je cijeli unutar pločice
        win = win.intersection(Window(0, 0, src.width, src.height))
        z = src.read(1, window=win).astype(float)
        t = src.window_transform(win)
    z = gaussian_filter(grey_opening(z, size=(3, 3)), sigma=1)
    ny, nx = z.shape
    m_po_px_y = abs(t.e) * 111_320
    m_po_px_x = t.a * 111_320 * np.cos(np.radians(lat0))

    # tačke: na rezoluciji 9 sedam središta djece (rez. 10) po polju; na gušćoj mreži samo središte
    tacke, kome = [], []
    for i, h in enumerate(polja.h3_id):
        for c in (h3.cell_to_children(h, H3_RES + 1) if H3_RES <= 9 else [h]):
            la, lo = h3.cell_to_latlng(c)
            tacke.append((lo, la))
            kome.append(i)
    tacke = np.array(tacke)
    kome = np.array(kome)
    col0 = (tacke[:, 0] - t.c) / t.a
    row0 = (tacke[:, 1] - t.f) / t.e
    z0 = z[np.clip(row0.astype(int), 0, ny - 1), np.clip(col0.astype(int), 0, nx - 1)] + VISINA_OKA

    # udaljenosti uzorkovanja: gusto blizu, rjeđe daleko
    d = np.r_[np.arange(30, 2000, 30), np.arange(2000, 8000, 60), np.arange(8000, DOMET_M, 120)].astype(float)
    pad = d ** 2 / (2 * R_ZEMLJE) * (1 - REFRAKCIJA)
    horizont_cache: dict[int, np.ndarray] = {}

    def horizont(az_deg: float) -> np.ndarray:
        k = int(round(az_deg))  # 1° rezolucija azimuta
        if k in horizont_cache:
            return horizont_cache[k]
        a = np.radians(k)
        dc = np.sin(a) * d / m_po_px_x
        dr = -np.cos(a) * d / m_po_px_y
        out = np.full(len(tacke), -90.0)
        for s in range(0, len(tacke), 2000):
            r = np.clip((row0[s:s + 2000, None] + dr[None, :]).astype(int), 0, ny - 1)
            c = np.clip((col0[s:s + 2000, None] + dc[None, :]).astype(int), 0, nx - 1)
            ugao = np.degrees(np.arctan((z[r, c] - pad[None, :] - z0[s:s + 2000, None]) / d[None, :]))
            out[s:s + 2000] = ugao.max(axis=1)
        horizont_cache[k] = out
        return out

    rez = pd.DataFrame({"h3_id": polja.h3_id})
    for ime, datum in DATUMI.items():
        minute = np.arange(6 * 60, 18 * 60, KORAK_MIN, dtype=float)
        el, az = polozaj_sunca(lat0, lon0, datum, minute)
        iznad = el > 0
        astro = iznad.sum() * KORAK_MIN / 60
        vidi = np.zeros((len(tacke), iznad.sum()), bool)
        for j, (e, a) in enumerate(zip(el[iznad], az[iznad])):
            vidi[:, j] = e > np.maximum(horizont(a), MIN_UGAO)
        sati_t = vidi.sum(axis=1) * KORAK_MIN / 60
        mm = minute[iznad]
        prvi = np.where(vidi.any(axis=1), mm[np.argmax(vidi, axis=1)], np.nan)
        zadnji = np.where(vidi.any(axis=1), mm[len(mm) - 1 - np.argmax(vidi[:, ::-1], axis=1)], np.nan)
        df = pd.DataFrame({"i": kome, "sati": sati_t, "prvi": prvi, "zadnji": zadnji})
        g = df.groupby("i").agg(sati=("sati", "mean"), prvi=("prvi", "median"), zadnji=("zadnji", "median"))
        rez[f"sunce_{ime}_h"] = g.sati.reindex(range(len(polja))).round(1).to_numpy()
        hm = lambda v: "" if np.isnan(v) else f"{int(v // 60):02d}:{int(v % 60):02d}"  # noqa: E731
        rez[f"sunce_{ime}_od"] = [hm(v) for v in g.prvi.reindex(range(len(polja)))]
        rez[f"sunce_{ime}_do"] = [hm(v) for v in g.zadnji.reindex(range(len(polja)))]
        rez[f"astro_{ime}_h"] = round(astro, 1)
        print(f"{ime}: astronomski dan {astro:.1f} h (izlazak/zalazak bez brda "
              f"{hm(mm[0])}–{hm(mm[-1] + KORAK_MIN)})")
    rez.to_csv(OUT / "sunce_h3.csv", index=False)

    j = rez.merge(polja[["h3_id", "opcina", "mz", "stanovnici"]], on="h3_id")
    nas = j[j.stanovnici > 0]
    w = nas.stanovnici
    s = nas.sunce_21dec_h
    print("\nStanovnici po satima sunca 21. decembra: " + ", ".join(
        f"{a}–{b} h: {w[(s >= a) & (s < b)].sum():,.0f}" for a, b in ((0, 2), (2, 4), (4, 6), (6, 8), (8, 24))))
    mz = nas.dropna(subset=["mz"]).groupby(["opcina", "mz"]).apply(
        lambda g: pd.Series({"st": g.stanovnici.sum(), "dec": np.average(g.sunce_21dec_h, weights=g.stanovnici),
                             "jan": np.average(g.sunce_21jan_h, weights=g.stanovnici)}), include_groups=False)
    mz = mz[mz.st >= 500]
    print("\nNajsunčanije MZ (21. dec, sati):")
    print(mz.sort_values("dec", ascending=False).round(1).head(10).to_string())
    print("\nNajmanje sunca:")
    print(mz.sort_values("dec").round(1).head(10).to_string())


if __name__ == "__main__":
    main()
