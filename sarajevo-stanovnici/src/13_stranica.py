"""Interaktivna stranica (claude.ai artifact) -> out/stranica.html

Sastavlja jednu samostalnu HTML stranicu iz izlaza koraka 05–11 i šablona
src/stranica_sablon.html: H3 polja (stanovnici, dostupnost, supermarket, teren),
granice, postojeće trgovine i predložene lokacije, satelitsku podlogu
(Sentinel-2 cloudless 2016, EOX, CC BY 4.0), reljef i izohipse (10_teren.py)
i mrežu puteva (11_putevi.py). Slike i podaci su ugrađeni, jer stranica ne
smije učitavati sadržaj s drugih servera.

Zamjene u šablonu: __DATA__, __SAT__, __X0__/__Y0__/__X1__/__Y1__, __TEREN__, __ROADS__.
"""
from __future__ import annotations

import base64
import io
import json

import geopandas as gpd
import h3
import numpy as np
import pandas as pd
import requests
from PIL import Image
from shapely.geometry import LineString, mapping

from common import DATA, INTERIM, OUT, RAW, ucitaj_granice

KZ_KAT = ["trgovina", "stanica", "osnovna_skola", "ambulanta", "park", "vrtic", "apoteka", "igraliste",
          "bolnica", "sport"]
POI_KAT = ["osnovna_skola", "vrtic", "ambulanta", "bolnica", "apoteka", "park", "igraliste", "sport"]
OP = ["Centar Sarajevo", "Novi Grad Sarajevo", "Novo Sarajevo", "Stari Grad Sarajevo"]
SAT_OKVIR = (18.2352, 43.8089, 18.53, 43.9783)
SAT_SIRINA = 2400
SAT_URL = ("https://tiles.maps.eox.at/wms?service=WMS&version=1.1.1&request=GetMap&layers=s2cloudless"
           "&styles=&srs=EPSG:4326&bbox={},{},{},{}&width={}&height={}&format=image/jpeg")
SABLON = OUT.parent / "src" / "stranica_sablon.html"


def rnd(g):
    def f(c):
        if isinstance(c[0], (list, tuple)):
            return [f(x) for x in c]
        return [round(c[0], 5), round(c[1], 5)]
    m = mapping(g)
    return {"type": m["type"], "coordinates": f(m["coordinates"])}


def podaci() -> dict:
    p = gpd.read_file(OUT / "polja_h3.gpkg")
    acc = pd.read_csv(OUT / "dostupnost_h3.csv").set_index("h3_id")
    sm = pd.read_csv(OUT / "supermarket_pokrivenost.csv").set_index("h3_id").supermarket_pjesice_min
    ter = pd.read_csv(OUT / "teren_h3.csv").set_index("h3_id")
    kz = pd.read_csv(OUT / "kvalitet_zivota_h3.csv").set_index("h3_id")
    kz_kol = ["indeks"] + [f"min_{k}" for k in KZ_KAT]
    ul = pd.read_csv(OUT / "ulice_h3.csv").set_index("h3_id")
    su = pd.read_csv(OUT / "sunce_h3.csv", keep_default_na=False).set_index("h3_id")
    zr = pd.read_csv(OUT / "zrak_h3.csv").set_index("h3_id")
    rmj = pd.read_csv(OUT / "radna_mjesta_h3.csv").set_index("h3_id").radna_mjesta
    ap = pd.read_csv(OUT / "autopraonica_pokrivenost.csv").set_index("h3_id").praonica_auto_min
    pv = pd.read_csv(OUT / "prevoz_h3.csv", dtype={"ptal": str}, keep_default_na=False).set_index("h3_id")
    cells = []
    for r in p.itertuples():
        cells.append(
            [r.h3_id, OP.index(r.opcina) if r.opcina in OP else -1, r.mz if isinstance(r.mz, str) else "",
             int(r.stanovnici), int(r.stanovnici_min), int(r.stanovnici_max), int(r.d0_14), int(r.d15_64),
             int(r.d65plus), r.pouzdanost, round(h3.cell_area(r.h3_id, "km^2"), 4)]
            + [int(acc.loc[r.h3_id, k]) if k != "stanica_tip" else acc.loc[r.h3_id, k]
               for k in ("atraktivnost", "pjesice_5", "pjesice_10", "pjesice_15", "auto_5", "auto_10", "auto_15",
                         "poi_10min", "stanica_m", "stanica_tip", "stanice_400m", "tramvaj_400m", "glavna_cesta_m")]
            + [None if pd.isna(sm.get(r.h3_id)) else round(float(sm.get(r.h3_id)), 1)]
            + ([int(ter.loc[r.h3_id, "visina_m"]), int(ter.loc[r.h3_id, "nagib_pct"])]
               if r.h3_id in ter.index else [None, None])
            + [int(round(float(kz.loc[r.h3_id, k]))) for k in kz_kol]
            + [int(ul.loc[r.h3_id, "ocjena_pristupa"]), float(ul.loc[r.h3_id, "put_max_nagib"]),
               int(ul.loc[r.h3_id, "put_usko_m"]), int(round(ul.loc[r.h3_id, "udio_usko"] * 100)),
               int(round(ul.loc[r.h3_id, "udio_strmo"] * 100)), int(ul.loc[r.h3_id, "put_min_koridor_m"])]
            + [float(su.loc[r.h3_id, "sunce_21dec_h"]), su.loc[r.h3_id, "sunce_21dec_od"],
               su.loc[r.h3_id, "sunce_21dec_do"], float(su.loc[r.h3_id, "sunce_21jan_h"]),
               float(su.loc[r.h3_id, "astro_21dec_h"])]
            + [int(zr.loc[r.h3_id, "iznad_dna_m"]), float(zr.loc[r.h3_id, "inverzija"]),
               int(zr.loc[r.h3_id, "smog_indeks"]), int(zr.loc[r.h3_id, "magla_indeks"])]
            + [int(kz.loc[r.h3_id, "buka_m"]), float(kz.loc[r.h3_id, "industrija_udio"])]
            + [float(pv.loc[r.h3_id, "ptal_ai"]), pv.loc[r.h3_id, "ptal"], pv.loc[r.h3_id, "linije"],
               int(pv.loc[r.h3_id, "polazaka_na_sat"]), float(pv.loc[r.h3_id, "stanica_min"])]
            + [None if pd.isna(ap.get(r.h3_id)) else round(float(ap.get(r.h3_id)), 1)]
            + [int(rmj.get(r.h3_id, 0))])

    op, _ = ucitaj_granice()
    op = op.set_index("opcina").loc[OP].reset_index()
    op["geometry"] = op.simplify(12)
    op = op.to_crs(4326)
    mz = gpd.read_file(INTERIM / "mz_granice.gpkg")
    sl = [mz[["opcina", "mz", "geometry"]]]
    if (INTERIM / "mz_novi_grad.gpkg").exists():
        sl.append(gpd.read_file(INTERIM / "mz_novi_grad.gpkg")[["opcina", "mz", "geometry"]])
    if (INTERIM / "mz_centar.gpkg").exists():
        sl.append(gpd.read_file(INTERIM / "mz_centar.gpkg")[["opcina", "mz", "geometry"]])
    mzall = gpd.GeoDataFrame(pd.concat(sl, ignore_index=True), crs=mz.crs)
    mzall["geometry"] = mzall.simplify(10)
    mzall = mzall.to_crs(4326)

    fzs = pd.read_csv(DATA / "opcine_procjena_2026.csv").set_index("opcina")
    d = gpd.read_file(INTERIM / "raspodjela_dijelovi.gpkg")
    summ = []
    for o in OP:
        dd = d[d.opcina == o]
        pz = dd.groupby("pouzdanost").stanovnici.sum()
        summ.append({"name": o, "total": int(fzs.loc[o, "stanovnici"]),
                     "ages": [int(fzs.loc[o, k]) for k in ("d0_14", "d15_64", "d65plus")],
                     "cells": int(dd.h3_id.nunique()), "abc": [int(pz.get(k, 0)) for k in "ABC"]})
    mzt = pd.read_csv(OUT / "mz_zbirovi.csv")
    mzrows = [[OP.index(r.opcina), r.mz, int(r.stanovnici), int(r.stanovnici_min), int(r.stanovnici_max),
               r.kontrolni_zbir] for r in mzt.itertuples()]

    st = pd.read_csv(OUT / "supermarket_trgovine.csv")
    st = st[st.tip.isin(["supermarket", "mall", "department_store"])]
    if "izvor" in st:  # Google Places se ne prikazuje na karti koja nije Google karta
        st = st[st.izvor != "google"]
    kd = pd.read_csv(OUT / "supermarket_kandidati.csv")
    sites = [[r.strategija, int(r.rang), r.h3_id, r.mz if isinstance(r.mz, str) else "", OP.index(r.opcina),
              int(r.kupci_procjena), int(r.stanovnici_10min_pjesice), int(r.od_toga_bez_supermarketa_10min),
              int(r.najblizi_supermarket_m), int(r.glavna_cesta_m), r.znakovi_zemljista, r.lon, r.lat]
             for r in kd.itertuples()]
    pr = pd.read_csv(OUT / "autopraonica_postojece.csv")
    praonice = [[round(r.lon, 5), round(r.lat, 5), r.ime if isinstance(r.ime, str) else "", r.vrsta]
                for r in pr.itertuples()]
    ak = pd.read_csv(OUT / "autopraonica_kandidati.csv")
    wsites = [[r.strategija, int(r.rang), r.h3_id, r.mz if isinstance(r.mz, str) else "", OP.index(r.opcina),
               int(r.pranja_mj), int(r.od_stanovnika), int(r.od_prolaza), int(r.stanovnici_10min_voznje),
               int(r.bez_praonice_5min), int(r.najbliza_praonica_m), int(r.najbliza_pumpa_m), r.cesta,
               r.znakovi_zemljista, r.lon, r.lat] for r in ak.itertuples()]
    biz = {}
    for k in ("dostava", "muzicka"):
        bk = pd.read_csv(OUT / f"biz_{k}_kandidati.csv")
        bp = pd.read_csv(OUT / f"biz_{k}_postojeci.csv")
        bc = pd.read_csv(OUT / f"biz_{k}_pokrivenost.csv").set_index("h3_id").reindex(p.h3_id)
        biz[k] = {
            "sites": [[r.strategija, int(r.rang), r.h3_id, r.mz if isinstance(r.mz, str) else "", OP.index(r.opcina),
                       float(r.procjena), int(r.potraznja_blizu), int(r.novo_pokriveno), int(r.najblizi_konkurent_m),
                       int(r.konkurenata_1500m), r.znakovi_zemljista, r.lon, r.lat] for r in bk.itertuples()],
            "places": [[round(r.lon, 5), round(r.lat, 5), r.ime if isinstance(r.ime, str) else "", r.vrsta]
                       for r in bp.itertuples()],
            "cov": [[None if pd.isna(m) else round(float(m), 1), None if pd.isna(n) else int(n)]
                    for m, n in zip(bc.min_do_najblizeg, bc.u_blizini)]}
    gz = gpd.read_file(OUT / "guzva_dionice.geojson")
    gp = json.load(open(OUT / "guzva_profili.json"))
    pk = list(gp["profili"])
    model = (OUT / "model_dionice.geojson").exists()
    if model:
        # tokovi iz modela putovanja (24_putovanja.py), profil sata s najbližeg brojača
        from scipy.spatial import cKDTree
        md = gpd.read_file(OUT / "model_dionice.geojson")
        bp = pd.read_csv(DATA / "brojaci_2025.csv").dropna(subset=["lat", "lon"])
        bp = bp[bp.brojac.isin(pk)]
        tk = cKDTree(np.c_[bp.lon * 0.72, bp.lat])
        c = md.geometry.interpolate(0.5, normalized=True)
        prof = bp.brojac.to_numpy()[tk.query(np.c_[c.x * 0.72, c.y])[1]]
        gz = gpd.GeoDataFrame({"pgds_smjer": md.jaci_smjer, "kapacitet": md.kap_smjer, "profil": prof,
                               "izvor": "model", "ime": md.ime, "brojac": ""}, geometry=md.geometry, crs=md.crs)
        mb = pd.read_csv(OUT / "model_brojaci.csv").set_index("brojac")
        mi = json.load(open(OUT / "model_info.json"))
    gimena = sorted({x for x in gz.ime if isinstance(x, str) and x})
    _op, _ = ucitaj_granice()
    unutra = gz.geometry.interpolate(0.5, normalized=True).within(_op.to_crs(gz.crs).union_all()).to_numpy()
    gbr = pd.read_csv(DATA / "brojaci_2025.csv").dropna(subset=["lat", "lon"])
    gbr = mb.reset_index()[["brojac", "lokacija", "lat", "lon", "pgds_2025"]] if model else gbr[gbr.brojac.isin(set(gz.brojac))]
    trf = {"prof": [gp["profili"][k] for k in pk], "day": gp["dan"], "names": gimena,
           "seg": [[round(float(r.pgds_smjer)), int(r.kapacitet), pk.index(r.profil), 0 if r.izvor in ("brojac", "model") else 1,
                    gimena.index(r.ime) if isinstance(r.ime, str) and r.ime else -1,
                    [round(c, 5) for xy in r.geometry.coords for c in xy], int(u)]
                   for r, u in zip(gz.itertuples(), unutra)],
           "cnt": [[r.brojac, r.lokacija, round(r.lat, 5), round(r.lon, 5), int(r.pgds_2025),
                    pk.index(r.brojac) if r.brojac in pk else -1,
                    int(mb.model.get(r.brojac, -1)) if model else -1,
                    int(mb.unakrsna.get(r.brojac, -1)) if model else -1,
                    int(mb.model_faza1.get(r.brojac, -1)) if model else -1,
                    int(bool(mb.korigovan.get(r.brojac, False))) if model else 0] for r in gbr.itertuples()],
           "model": mi if model else None}
    rmo = pd.read_csv(DATA / "radna_mjesta_opcine.csv")
    rmz = pd.read_csv(OUT / "radna_mjesta_mz.csv")
    jobs = {"op": [[OP.index(r.opcina), int(r.radna_mjesta_2024), int(r.zaposleni_stanovnici_2025)] for r in rmo.itertuples()],
            "mz": [[OP.index(r.opcina), r.mz, int(r.radna_mjesta), int(r.stanovnici)] for r in rmz.itertuples()]}
    sd = gpd.read_file(OUT / "sadrzaji.geojson")
    x0, y0, x1, y1 = SAT_OKVIR
    sd = sd[(sd.geometry.x.between(x0, x1)) & (sd.geometry.y.between(y0, y1))]
    poi = {k: [[round(g.x, 5), round(g.y, 5), (n if isinstance(n, str) else "")]
               for g, n in zip(sd[sd.kategorija == k].geometry, sd[sd.kategorija == k].ime)] for k in POI_KAT}
    dio = gpd.read_file(OUT / "ulice_dionice.gpkg")
    dio = dio[~dio.klasa.isin(["motorway", "motorway_link", "trunk", "trunk_link", "primary", "primary_link",
                               "secondary", "secondary_link", "tertiary", "tertiary_link"])]
    dio["kod"] = (dio.nagib > 12).astype(int) + 2 * dio.uska.astype(bool).astype(int)
    dio = dio[dio.kod > 0].to_crs(4326)
    acc = {}
    for kod, g in dio.groupby("kod"):
        acc[int(kod)] = [[round(c, 5) for xy in geom.coords for c in xy] for geom in g.geometry]
    zs = pd.read_csv(OUT / "zrak_stanice.csv")
    stanice = [[r.stanica, round(r.lat, 5), round(r.lon, 5), int(r.pm25)] for r in zs.itertuples()]
    li = gpd.read_file(OUT / "linije.geojson")
    li["geometry"] = li.to_crs(32634).simplify(8).to_crs(4326)
    linije = []
    for r in li.itertuples():
        parts = getattr(r.geometry, "geoms", [r.geometry])
        linije.append([r.mod, r.linija, r.ime, None if pd.isna(r.polazaka_na_sat) else float(r.polazaka_na_sat),
                       [[round(c, 5) for xy in p.coords for c in xy] for p in parts]])
    return {"lines": linije, "aq": stanice, "acc": acc, "poi": poi,
            "stores": [[round(a, 5), round(b, 5), (n if isinstance(n, str) else "")]
                       for a, b, n in zip(st.lon, st.lat, st.ime)],
            "sites": sites, "washes": praonice, "wsites": wsites, "biz": biz, "trf": trf, "jobs": jobs, "cells": cells, "summ": summ, "mz": mzrows,
            "op": [rnd(x) for x in op.geometry],
            "mzlines": [[OP.index(o) if o in OP else -1, n, rnd(x)]
                        for o, n, x in zip(mzall.opcina, mzall.mz, mzall.geometry)]}


def satelit() -> tuple[str, tuple]:
    f = RAW / "s2cloudless_2016.jpg"
    x0, y0, x1, y1 = SAT_OKVIR
    if not f.exists():
        import math
        h = round(SAT_SIRINA * (y1 - y0) / ((x1 - x0) * math.cos(math.radians((y0 + y1) / 2))))
        r = requests.get(SAT_URL.format(x0, y0, x1, y1, SAT_SIRINA, h), timeout=180)
        r.raise_for_status()
        f.write_bytes(r.content)
    return "data:image/jpeg;base64," + base64.b64encode(f.read_bytes()).decode(), SAT_OKVIR


def teren() -> dict:
    def jpg(path, mode, q):
        b = io.BytesIO()
        Image.open(OUT / path).convert(mode).save(b, "JPEG", quality=q, optimize=True)
        return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()

    gj = json.loads((OUT / "teren_izohipse.geojson").read_text())
    cont = []
    for f in gj["features"]:
        ln = LineString(f["geometry"]["coordinates"]).simplify(0.00015)
        if ln.length < 0.003:
            continue
        cont.append([f["properties"]["m"], 1 if f["properties"]["glavna"] else 0,
                     [round(c, 4) for xy in ln.coords for c in xy]])
    return {"rel": jpg("teren_reljef.png", "RGB", 82), "sj": jpg("teren_sjena.png", "L", 80),
            "cont": cont, "box": json.loads((OUT / "teren_okvir.json").read_text())}


def putevi() -> dict:
    gj = json.loads((OUT / "putevi.geojson").read_text())
    roads: dict[str, list] = {}
    for f in gj["features"]:
        k = f["properties"]["klasa"]
        nd = 4 if k in ("ulica", "pristupna", "pjesacka", "stepenice") else 5
        roads.setdefault(k, []).append([round(c, nd) for xy in f["geometry"]["coordinates"] for c in xy])
    return roads


def main() -> None:
    sat, (x0, y0, x1, y1) = satelit()
    t = SABLON.read_text(encoding="utf-8")
    t = (t.replace("__X0__", str(x0)).replace("__Y0__", str(y0)).replace("__X1__", str(x1)).replace("__Y1__", str(y1))
         .replace("__ROADS__", json.dumps(putevi(), separators=(",", ":")))
         .replace("__TEREN__", json.dumps(teren(), separators=(",", ":")))
         .replace("__DATA__", json.dumps(podaci(), ensure_ascii=False, separators=(",", ":")))
         .replace("__SAT__", sat))
    (OUT / "stranica.html").write_text(t, encoding="utf-8")
    print(f"-> out/stranica.html ({len(t) // 1024} KB)")


if __name__ == "__main__":
    main()
