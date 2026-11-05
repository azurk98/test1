"""Predložene nove linije javnog prevoza (trase za kartu) -> out/nove_linije.geojson

Na osnovu 25_prijedlozi.py:
  P1  glavna linija sjeverozapad Novog Grada: Zabrđe – Briješće – Sokolje – Alipašin Most;
      Dobroševići dobijaju minibus do početka P1 (Zabrđe)
  P2  Lukavica (Istočno Sarajevo) – Željeznička stanica (u OSM-u nema linije; provjeriti RS prevoznika)
  P3  Stup – Alipašin Most III
  M*  minibus za brdska naselja: od težišta stanovnika koji su > 8 min od stanice do najbliže
      tramvajske/trolejbuske stanice
Trasa = najkraći put po cestama (mreža iz 24_putovanja.py). Za svaku liniju: dužina, stanovnici i
radna mjesta do 400 m, "novi korisnici" = stanovnici do 400 m od trase koji su danas > 8 min hoda od
stanice, okvirno vrijeme vožnje (vrijeme autom · 1,4 za stajanje) i broj stanica (svakih ~400 m).
Trase su skica za raspravu, ne projekat: ulice za minibus treba provjeriti na terenu (širina, okretište).
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
from scipy.sparse.csgraph import dijkstra
from scipy.spatial import cKDTree
from shapely.geometry import LineString

from common import CRS_M, CRS_WGS, OUT


def _uvezi(ime, fajl):
    s = importlib.util.spec_from_file_location(ime, Path(__file__).with_name(fajl))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


mp = _uvezi("mp", "24_putovanja.py")

BRDSKA = [("Centar Sarajevo", "Hrastovi-Mrkovići"), ("Centar Sarajevo", "Betanija"), ("Centar Sarajevo", "Soukbunar"),
          ("Stari Grad Sarajevo", "Mošćanica"), ("Stari Grad Sarajevo", "Širokača"), ("Novi Grad Sarajevo", "Dolac"),
          ("Novi Grad Sarajevo", "Alipašin Most I")]


def main() -> None:
    wmeta, xy, ll, e, idx = mp.mreza()
    n = len(xy)
    G = mp.graf(e, n, e.t0.to_numpy())
    from scipy.sparse.csgraph import connected_components
    _, lab = connected_components(G, directed=True, connection="strong")
    ok = np.where(lab == np.bincount(lab).argmax())[0]
    tk = cKDTree(xy[ok])

    def cvor(lon, lat):
        p = gpd.GeoSeries(gpd.points_from_xy([lon], [lat]), crs=CRS_WGS).to_crs(CRS_M)[0]
        return ok[tk.query([p.x, p.y])[1]]

    def trasa(tacke):
        cv = [cvor(*t) for t in tacke]
        put, minute = [cv[0]], 0.0
        for a, b in zip(cv[:-1], cv[1:]):
            D, P = dijkstra(G, indices=[a], return_predecessors=True)
            minute += D[0, b]
            seg = [b]
            while seg[-1] != a:
                seg.append(P[0, seg[-1]])
            put += seg[::-1][1:]
        return LineString([ll[i] for i in put]), minute

    polja = gpd.read_file(OUT / "polja_h3.gpkg")
    pv = pd.read_csv(OUT / "prevoz_h3.csv").set_index("h3_id").reindex(polja.h3_id)
    rm = pd.read_csv(OUT / "radna_mjesta_h3.csv").set_index("h3_id").radna_mjesta.reindex(polja.h3_id).fillna(0).to_numpy()
    pc = polja.geometry.centroid
    pcw = pc.to_crs(CRS_WGS)
    daleko = (pv.stanica_min.to_numpy() > 8) & (polja.stanovnici.to_numpy() > 0)

    def tezište(maska):
        w = polja.stanovnici.to_numpy()[maska]
        return float(np.average(pcw.x[maska], weights=w)), float(np.average(pcw.y[maska], weights=w))

    def mz(op, ime, samo_daleko=False):
        m = ((polja.opcina == op) & (polja.mz == ime)).to_numpy() & (polja.stanovnici.to_numpy() > 0)
        if samo_daleko and (m & daleko).sum():
            m &= daleko
        return tezište(m)

    # tramvajske i trolejbuske stanice: OSM stanice do 60 m od trunk linija
    li = gpd.read_file(OUT / "linije.geojson").to_crs(CRS_M)
    trunk = li[li["mod"].isin(["tram", "trolleybus"])]
    _, _, stops = mp.dost.ucitaj_mrezu(mp.RAW / "Sarajewo.osm.gz")
    st = gpd.GeoDataFrame(pd.DataFrame(stops, columns=["lon", "lat", "tip", "ime"]),
                          geometry=gpd.points_from_xy([s[0] for s in stops], [s[1] for s in stops]), crs=CRS_WGS).to_crs(CRS_M)
    st = st[st.distance(trunk.union_all()) <= 60].reset_index(drop=True)
    tst = cKDTree(np.c_[st.geometry.x, st.geometry.y])

    def najbliza_stanica(lon, lat):
        p = gpd.GeoSeries(gpd.points_from_xy([lon], [lat]), crs=CRS_WGS).to_crs(CRS_M)[0]
        i = tst.query([p.x, p.y])[1]
        r = st.iloc[i]
        return (r.lon, r.lat), r.ime or "tramvaj/trolejbus"

    am_stanica, am_ime = najbliza_stanica(18.3475, 43.8480)    # Alipašin most
    linije = [
        ("P1", "glavna", "Zabrđe – Briješće – Sokolje – Alipašin Most",
         [mz("Novi Grad Sarajevo", "Zabrđe"), mz("Novi Grad Sarajevo", "Briješće"),
          mz("Novi Grad Sarajevo", "Naselje heroja Sokolje"), am_stanica],
         "Najjači pravac bez tramvaja/trolejbusa (~3.700 putovanja dnevno). Trolejbus ili električni autobus "
         "svakih 7–10 min, presjedanje na tramvaj na Alipašinom mostu."),
        ("P2", "glavna", "Lukavica – Željeznička stanica",
         [(18.371, 43.824), najbliza_stanica(18.4000, 43.8565)[0]],
         "~2.200 putovanja dnevno, u OSM-u nema linije; provjeriti postoji li linija prevoznika iz RS-a."),
        ("P3", "glavna", "Stup – Alipašin Most",
         [(18.303, 43.839), am_stanica],
         "~2.100 putovanja dnevno; spaja Stup i istočni dio Ilidže s Alipašinim mostom bez presjedanja."),
    ]
    for i, (op, ime) in enumerate(BRDSKA, 1):
        a = mz(op, ime, samo_daleko=True)
        s_xy, s_ime = najbliza_stanica(*a)
        linije.append((f"M{i}", "minibus", f"{ime} – {s_ime}", [a, s_xy],
                       f"Minibus za strmo naselje: od dijela {ime} najdaljeg od stanice do stanice {s_ime}."))

    linije.append((f"M{len(BRDSKA) + 1}", "minibus", "Dobroševići – Zabrđe (P1)",
                   [mz("Novi Grad Sarajevo", "Dobroševići", samo_daleko=True), mz("Novi Grad Sarajevo", "Zabrđe")],
                   "Minibus za Dobroševiće do početka linije P1 u Zabrđu."))
    rows = []
    for lid, tip, naziv, tacke, opis in linije:
        g, minute = trasa(tacke)
        gm = gpd.GeoSeries([g], crs=CRS_WGS).to_crs(CRS_M)[0]
        u = pc.within(gm.buffer(400)).to_numpy()
        rows.append({"id": lid, "tip": tip, "naziv": naziv, "opis": opis, "duzina_km": round(gm.length / 1000, 1),
                     "stanovnici_400m": int(polja.stanovnici[u].sum()), "radna_mjesta_400m": int(rm[u].sum()),
                     "novi_korisnici": int(polja.stanovnici[u & daleko].sum()),
                     "voznja_min": round(minute * 1.4), "stanica": max(2, round(gm.length / 400)),
                     "geometry": g.simplify(0.00003)})
    out = gpd.GeoDataFrame(rows, crs=CRS_WGS)
    out.to_file(OUT / "nove_linije.geojson", driver="GeoJSON", COORDINATE_PRECISION=5)
    pd.set_option("display.width", 250)
    print(out.drop(columns=["geometry", "opis"]).to_string(index=False))


if __name__ == "__main__":
    main()
