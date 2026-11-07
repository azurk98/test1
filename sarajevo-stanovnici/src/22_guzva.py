"""Gužva po satu na glavnim cestama: volumen s brojača Direkcije za puteve KS / kapacitet.

Ulaz:  data/brojaci_2025.csv, data/brojaci_2025_satno.csv, data/brojaci_2025_dnevno.csv
       (21_brojaci_saobracaja.py), raw/Sarajewo.osm.gz, out/polja_h3.gpkg
Izlaz: out/guzva_dionice.geojson   dionice s PGDS-om, kapacitetom i izvorom procjene
       out/guzva_profili.json       satni profili brojača i faktori dana (radni, subota, nedjelja)

Postupak (procjena, ne mjerenje gužve):
  1. Svaki brojač se veže za najbližu dionicu glavne ceste (s nazivom ulice iz publikacije, gdje je
     naveden), pa se njegov PGDS prenosi na dionice iste ulice do PROPAGACIJA_M; kod više brojača na
     istoj ulici svaka dionica uzima najbliži.
  2. Ostale dionice: PGDS_PRETPOSTAVKA po klasi (brojač bez naziva ulice važi samo za svoju dionicu).
  3. Jednosmjerne dionice dvosmjerne ulice (dva kolovoza) nose pola PGDS-a.
  4. Kapacitet: trake iz OSM-a (lanes), inače tipično po klasi; 800 voz/h po traci u gradu
     (semafori), 1.800 na autoputu.
  5. Satni volumen = PGDS · udio sata (profil najbližeg brojača) · faktor dana; gužva = volumen /
     kapacitet. Profil vrijedi za prosječan dan; vikendom je isti oblik, umanjen faktorom dana.
"""
from __future__ import annotations

import gzip
import json
import re
import xml.etree.ElementTree as ET

import geopandas as gpd
import numpy as np
import pandas as pd
from scipy.spatial import cKDTree
from shapely.geometry import LineString, Point, box

from common import OSM_IME
from common import CRS_M, CRS_WGS, DATA, OUT, RAW

KLASA = {"motorway": "autoput", "motorway_link": "autoput", "trunk": "magistrala", "trunk_link": "magistrala",
         "primary": "primarna", "primary_link": "primarna", "secondary": "sekundarna",
         "secondary_link": "sekundarna", "tertiary": "tercijarna", "tertiary_link": "tercijarna"}
TRAKE = {"autoput": (2, 4), "magistrala": (2, 4), "primarna": (2, 4), "sekundarna": (2, 2), "tercijarna": (1, 2)}
KAP_TRAKA = {"autoput": 1800}
KAP_TRAKA_GRAD = 800
# ceste bez brojača (brojači stoje na najprometnijim pravcima, pa medijan brojača precjenjuje ostale)
PGDS_PRETPOSTAVKA = {"autoput": 25000, "magistrala": 20000, "primarna": 12000, "sekundarna": 8000, "tercijarna": 4000}
PROPAGACIJA_M = 2500
# ulica iz publikacije i, gdje su koordinate u izvoru ponovljene ili ih nema, približna tačka
ULICA = {
    "KSBS03": ("Obala Kulina bana", None), "KSBS04": ("Maršala Tita", None),
    "KSBS05": ("Maršala Tita", (43.8582, 18.4130)), "KSBS10": ("Derviša Numića", None),
    "KSBS11": ("Hamdije Čemerlića", (43.8545, 18.3925)), "KSBS13": ("Put života", None),
    "KSBS14": ("Topal Osman", None), "KSBS15": ("Drinska", None), "KSBS16": ("Azize Šaćirbegović", None),
    "KSBS17": ("Zmaja od Bosne", None), "KSBS18": ("Džemala Bijedića", None), "KSBS21": ("Majdanska", None),
    "KSBS22": ("Džemala Bijedića", (43.8480, 18.3540)), "KSBS23": ("Ive Andrića", None),
    "KSBS24": ("Meše Selimovića", None), "KSBS25": ("Ante Babića", None), "KSBS26": ("Safeta Zajke", None),
    "KSBS29a": ("Rajlovačka", (43.8730, 18.3110)), "KSBS30": ("Kasindolska", None), "KSBS32": ("Bojnička", None),
}


def ucitaj_dionice(okvir):
    nodes, rows = {}, []
    with gzip.open(RAW / OSM_IME, "rb") as f:
        for _, el in ET.iterparse(f):
            if el.tag == "node":
                nodes[int(el.get("id"))] = (float(el.get("lon")), float(el.get("lat")))
                el.clear()
            elif el.tag == "way":
                t = {c.get("k"): c.get("v") for c in el.findall("tag")}
                k = KLASA.get(t.get("highway"))
                if k:
                    p = [nodes[int(n.get("ref"))] for n in el.findall("nd") if int(n.get("ref")) in nodes]
                    if len(p) >= 2:
                        m = re.match(r"\d+", t.get("lanes", ""))
                        jedno = t.get("oneway") in ("yes", "1", "-1") or t.get("junction") == "roundabout" \
                            or t.get("highway") == "motorway"
                        rows.append({"klasa": k, "ime": t.get("name", ""), "trake_osm": int(m[0]) if m else None,
                                     "jednosmjerna": jedno, "link": t["highway"].endswith("_link"),
                                     "geometry": LineString(p)})
                el.clear()
            elif el.tag == "relation":
                el.clear()
    g = gpd.GeoDataFrame(rows, crs=CRS_WGS)
    g = g[g.intersects(okvir)].copy()
    g["geometry"] = g.geometry.intersection(okvir)
    g = g.explode(ignore_index=True)
    return g[g.geom_type == "LineString"].to_crs(CRS_M).reset_index(drop=True)


def main() -> None:
    polja = gpd.read_file(OUT / "polja_h3.gpkg").to_crs(CRS_WGS)
    x0, y0, x1, y1 = polja.total_bounds
    g = ucitaj_dionice(box(x0 - 0.02, y0 - 0.015, x1 + 0.02, y1 + 0.015))
    br = pd.read_csv(DATA / "brojaci_2025.csv")
    sat = pd.read_csv(DATA / "brojaci_2025_satno.csv")
    dn = pd.read_csv(DATA / "brojaci_2025_dnevno.csv", parse_dates=["datum"])

    # tačke brojača
    for k, (_, xy) in ULICA.items():
        if xy:
            br.loc[br.brojac == k, ["lat", "lon"]] = xy
    br = br.dropna(subset=["lat", "lon"]).reset_index(drop=True)
    bg = gpd.GeoDataFrame(br, geometry=gpd.points_from_xy(br.lon, br.lat), crs=CRS_WGS).to_crs(CRS_M)

    mid = g.geometry.interpolate(0.5, normalized=True)
    g["pgds"] = np.nan
    g["izvor"] = ""
    g["brojac"] = ""
    vezano = []
    for r in bg.itertuples():
        ul = ULICA.get(r.brojac, (None, None))[0]
        kand = g[g.ime.str.contains(ul, case=False, regex=False)] if ul else g[~g.link]
        if kand.empty:
            print("nema ulice za", r.brojac, ul); continue
        d = kand.distance(r.geometry)
        if d.min() > (600 if ul else 150):
            print(f"{r.brojac}: najbliža dionica {d.min():.0f} m — preskočeno"); continue
        s = d.idxmin()
        ime = g.ime.at[s]
        vezano.append((r.brojac, s, ime or "", r.pgds_2025, r.geometry))
        print(f"{r.brojac} -> {ime or '(bez naziva)'} [{g.klasa.at[s]}], {d.min():.0f} m, PGDS {r.pgds_2025:,}")
    # propagacija po istoj ulici, najbliži brojač
    dmin = np.full(len(g), np.inf)
    for brojac, s, ime, pgds, pt in vezano:
        if ime and brojac in ULICA:
            ista = g.index[(g.ime == ime) & (mid.distance(pt) <= PROPAGACIJA_M)]
        else:
            ista = pd.Index([s])
        for i in ista:
            dist = mid.at[i].distance(pt)
            if dist < dmin[i]:
                g.at[i, "pgds"], g.at[i, "izvor"], g.at[i, "brojac"] = pgds, "brojac", brojac
                dmin[i] = dist
    # dvosmjerna ulica na dva kolovoza: jednosmjerna dionica ima istoimeni par u blizini
    tr = cKDTree(np.c_[mid.x, mid.y])
    par = np.zeros(len(g), bool)
    for i in np.where(g.jednosmjerna)[0]:
        for j in tr.query_ball_point((mid.x.iat[i], mid.y.iat[i]), 60):
            if j != i and g.jednosmjerna.iat[j] and g.ime.iat[j] == g.ime.iat[i] and g.klasa.iat[j] == g.klasa.iat[i] \
                    and g.geometry.iat[j].distance(g.geometry.iat[i]) > 5:
                par[i] = True; break
    g["par"] = par | (g.klasa == "autoput")
    for k, v in PGDS_PRETPOSTAVKA.items():
        sel = (g.izvor == "") & (g.klasa == k)
        g.loc[sel, "pgds"] = v
        g.loc[sel, "izvor"] = "pretpostavka"
    g.loc[g.link, "pgds"] = g.loc[g.link, "pgds"] * 0.3
    g["pgds_smjer"] = np.where(g.par, g.pgds / 2, g.pgds)
    tr_def = np.where(g.jednosmjerna, [TRAKE[k][0] for k in g.klasa], [TRAKE[k][1] for k in g.klasa])
    g["trake"] = g.trake_osm.fillna(pd.Series(tr_def, index=g.index)).clip(1, 6).astype(int)
    g.loc[g.link, "trake"] = 1
    g["kapacitet"] = g.trake * g.klasa.map(KAP_TRAKA).fillna(KAP_TRAKA_GRAD)
    # profil: najbliži brojač s profilom
    sa_prof = bg[bg.brojac.isin(sat.brojac.unique())]
    tp = cKDTree(np.c_[sa_prof.geometry.x, sa_prof.geometry.y])
    g["profil"] = np.where(g.brojac.isin(sa_prof.brojac), g.brojac,
                           sa_prof.brojac.to_numpy()[tp.query(np.c_[mid.x, mid.y])[1]])

    # profili i faktori dana
    prof = sat.pivot(index="brojac", columns="sat", values="vozila_sat")
    prof = prof.div(prof.sum(axis=1), axis=0).round(4)
    dn["tip"] = np.select([dn.datum.dt.dayofweek < 5, dn.datum.dt.dayofweek == 5], ["radni", "subota"], "nedjelja")
    f = dn.groupby(["brojac", "tip"]).vozila.mean().unstack()
    f = f.div(dn.groupby("brojac").vozila.mean(), axis=0).median().round(3).to_dict()
    print("Faktor dana (prema prosjeku):", f)
    json.dump({"profili": {k: v.tolist() for k, v in prof.iterrows()}, "dan": f},
              open(OUT / "guzva_profili.json", "w"))

    g = g.drop(columns=["_d"], errors="ignore")
    g["geometry"] = g.geometry.simplify(4)
    out = g[["klasa", "ime", "pgds", "pgds_smjer", "trake", "kapacitet", "izvor", "brojac", "profil", "geometry"]]
    out.to_crs(CRS_WGS).to_file(OUT / "guzva_dionice.geojson", driver="GeoJSON", COORDINATE_PRECISION=5)
    print(out.groupby("izvor").geometry.apply(lambda s: round(s.length.sum() / 1000)).to_string())
    vs = out.pgds_smjer * prof.max(axis=1).reindex(out.profil).to_numpy() / out.kapacitet
    print("Vršni sat, volumen/kapacitet po klasi (medijan):", vs.groupby(out.klasa).median().round(2).to_dict())
    top = out.assign(vc=vs).sort_values("vc", ascending=False)
    print(top[top.ime != ""].drop_duplicates("ime").head(12)[["ime", "klasa", "pgds", "trake", "kapacitet", "vc"]]
          .round(2).to_string(index=False))


if __name__ == "__main__":
    main()
