"""Magla i niski oblaci zimi: Butmir i kandidati za novi aerodrom (Nišići, Glasinac, Pazarić, Kiseljak).

Ulaz (preuzima se ako nema):
  raw/metar_lqsa.csv    METAR aerodroma Sarajevo 2016–2025 (arhiva Iowa Environmental Mesonet)
  raw/modis_zima/       MODIS Terra dnevni snimci (~10:30 lokalno), novembar–februar 2016/17–2025/26,
                        NASA GIBS: Corrected Reflectance pojasevi 7-2-1 i prave boje
Postupak:
  oblak/magla na tački = pojas 7 (2,1 µm) svijetao (>= 110) i prave boje svijetle (>= 150), prosjek 5×5
  piksela (~1 km). Snijeg je u pojasu 7 taman, pa se ne miješa s oblakom.
  Analiziraju se samo dani kad su planine (Bjelašnica, Igman, Trebević, Romanija) bez oblaka: tipična
  zimska inverzija, kad je magla u dolinama. Kalibracija na METAR-u Butmira (09–10 UTC, vidljivost < 1 km
  ili oblaci do 500 ft): test pogađa 76% jutara s maglom, a lažno javlja 18% jutara bez magle.
Izlaz: out/magla_lokacije.csv, ispis.
Ograničenja: satelit vidi vrh oblaka, pa dani s oblacima i iznad planina (frontalni sistemi) nisu ocijenjeni;
  jedan snimak dnevno (~10:30), a magla se ponekad digne ranije; tačke su ~1 km, a ne sama pista.
"""
from __future__ import annotations

import datetime as dt
import os
import time

import numpy as np
import pandas as pd
import requests
from PIL import Image

from common import OUT, RAW

MOD = RAW / "modis_zima"
GIBS = ("https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0"
        "&LAYERS={L}&CRS=EPSG:4326&BBOX=43.70,18.00,44.20,18.90&WIDTH=405&HEIGHT=225&FORMAT=image/png&TIME={d}")
METAR = ("https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?station=LQSA&data=vsby&data=wxcodes&data=skyc1"
         "&data=skyl1&year1=2016&month1=1&day1=1&year2=2026&month2=1&day2=1&tz=Etc/UTC&format=onlycomma&latlon=no"
         "&missing=M&trace=T&direct=no&report_type=3&report_type=4")
TACKE = {"Butmir (danas)": (18.33, 43.824), "Centar": (18.41, 43.857), "Kiseljak": (18.067, 43.957),
         "Pazarić / Tarčin": (18.10, 43.80), "Glasinac": (18.809, 43.894), "Nišići": (18.476, 44.078)}
PLANINE = {"Bjelašnica": (18.256, 43.715), "Igman": (18.25, 43.76), "Trebević": (18.45, 43.83), "Romanija": (18.72, 43.885)}
PRAG_7, PRAG_TC = 110, 150
UA = {"User-Agent": "sarajevo-stanovnici/1.0 (istrazivacki skript)"}


def preuzmi() -> None:
    if not (RAW / "metar_lqsa.csv").exists():
        (RAW / "metar_lqsa.csv").write_bytes(requests.get(METAR, headers=UA, timeout=600).content)
    MOD.mkdir(exist_ok=True)
    d = dt.date(2016, 11, 1)
    while d <= dt.date(2026, 2, 28):
        if d.month in (11, 12, 1, 2):
            for L, k in (("MODIS_Terra_CorrectedReflectance_Bands721", "721"),
                         ("MODIS_Terra_CorrectedReflectance_TrueColor", "tc")):
                f = MOD / f"{d}_{k}.png"
                if not f.exists():
                    r = requests.get(GIBS.format(L=L, d=d), headers=UA, timeout=60)
                    if r.ok and r.content[:4] == b"\x89PNG":
                        f.write_bytes(r.content)
                    time.sleep(0.4)
        d += dt.timedelta(1)


def piksel(a, x, y):
    i, j = int(round((x - 18) / 0.9 * 405)), int(round((44.2 - y) / 0.5 * 225))
    return a[max(j - 2, 0):j + 3, max(i - 2, 0):i + 3]


def main() -> None:
    preuzmi()
    met = pd.read_csv(RAW / "metar_lqsa.csv", na_values="M", low_memory=False)
    met["t"] = pd.to_datetime(met.valid)
    met = met[met.t.dt.hour.between(9, 10)]
    nisko = met.skyc1.isin(["BKN", "OVC", "VV"]) & (met.skyl1 <= 500)
    met["magla"] = (met.vsby * 1609.34 < 1000) | nisko
    bm = met.groupby(met.t.dt.strftime("%Y-%m-%d")).magla.max()
    rows = []
    for f in sorted(os.listdir(MOD)):
        if not f.endswith("_721.png") or not (MOD / f.replace("_721", "_tc")).exists():
            continue
        a = np.asarray(Image.open(MOD / f).convert("RGBA")).astype(float)
        t = np.asarray(Image.open(MOD / f.replace("_721", "_tc")).convert("RGB")).astype(float)
        if piksel(a, *TACKE["Butmir (danas)"])[..., 3].mean() < 200:
            continue                                   # bez snimka (praznina između prolaza)
        r = {"d": f[:10]}
        for n, (x, y) in {**TACKE, **PLANINE}.items():
            r[n] = bool(piksel(a, x, y)[..., 0].mean() >= PRAG_7 and piksel(t, x, y).mean() >= PRAG_TC)
        rows.append(r)
    d = pd.DataFrame(rows)
    d["butmir_metar"] = d.d.map(bm)
    vedro = d[list(PLANINE)].sum(axis=1) <= 1           # najviše jedna planina pod oblakom
    sez = len(d) / 120.6
    inv = d[vedro]
    bf = inv.butmir_metar == True                       # noqa: E712
    out = []
    for n in TACKE:
        out.append({"lokacija": n, "udio_inverzijskih_jutara_pod_niskim_oblakom_pct": round(inv[n].mean() * 100),
                    "kad_butmir_u_magli_pct": round(inv[n][bf].mean() * 100),
                    "kad_butmir_bez_magle_pct": round(inv[n][~bf & inv.butmir_metar.notna()].mean() * 100),
                    "jutara_po_zimi": round(inv[n].sum() / sez)})
    r = pd.DataFrame(out)
    r.to_csv(OUT / "magla_lokacije.csv", index=False)
    print(f"Zimskih dana sa snimkom: {len(d)}, od toga s vedrim planinama: {len(inv)}; Butmir u magli (METAR) {bf.sum()}")
    print(r.to_string(index=False))


if __name__ == "__main__":
    main()
