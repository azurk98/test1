"""Lokacije za dva biznisa: dostavna kuhinja (dark kitchen) i muzička škola.

Ulaz:  raw/Sarajewo.osm.gz, raw/overture_places.parquet, out/polja_h3.gpkg, out/dostupnost_h3.csv,
       out/teren_h3.csv, out/ulice_h3.csv, interim/zgrade.gpkg
Izlaz: out/biz_<kljuc>_kandidati.csv, out/biz_<kljuc>_postojeci.csv, out/biz_<kljuc>_pokrivenost.csv

Oba modela su Huffov model kao za supermarket (09) i autopraonicu (19), s drugim kupcima,
načinom dolaska i konkurencijom. Brojke su red veličine za poređenje lokacija.

Dostavna kuhinja
  kupci:   odrasli (15–64 puta 1, 65+ puta 0,2); 0,03 narudžbe po odraslom dnevno (pretpostavka:
           otprilike jedna narudžba mjesečno)
  dolazak: dostavljač autom ili skuterom, do 15 min vožnje; λ = 1 (u aplikaciji udaljenost
           manje odlučuje nego kod kupovine na licu mjesta)
  konkurencija: restorani i fast food iz OSM-a i Overture (fast food, pizza, burger i sl. 1;
           ostali restorani 0,5); nova kuhinja s više virtuelnih brendova A = 2
  lokacija: cesta tercijarna ili veća na ≤ 100 m (kuriri), nagib ≤ 10%, pristup ulicama ≥ 50
  bijela mrlja: odrasli s manje od 10 restorana u 10 min vožnje

Muzička škola
  kupci:   djeca i mladi: 0,55 · (0–14) + 0,04 · (15–64) (≈ 7–18 godina); 5% njih ide u
           muzičku školu (pretpostavka)
  dolazak: min(pješice s nagibom, autom + 3 min parkiranje), do 20 min; λ = 2
  konkurencija: javne muzičke škole A = 3 (besplatne, veće), privatne A = 1, nova A = 1
  lokacija: stanica javnog prevoza na ≤ 400 m ili cesta na ≤ 150 m, nagib ≤ 12%,
           pristup ulicama ≥ 40, u polju ima zgrada (prostor za najam)
  bijela mrlja: djeca bez muzičke škole u 15 min (pješice ili autom)
"""
from __future__ import annotations

import gzip
import importlib.util
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
from scipy.sparse.csgraph import connected_components, dijkstra
from scipy.spatial import cKDTree
from shapely.geometry import Polygon

from common import OSM_IME
from common import CRS_M, CRS_WGS, DATA, INTERIM, OUT, RAW


def _uvezi(ime, fajl):
    s = importlib.util.spec_from_file_location(ime, Path(__file__).with_name(fajl))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


dost = _uvezi("dost", "08_dostupnost.py")
sup = _uvezi("sup", "09_supermarket.py")

N_IZBOR = 10
DUPLIKAT_M = 50

BRZA_HRANA = {"fast_food_restaurant", "pizza_restaurant", "burger_restaurant", "doner_kebab_restaurant",
              "chicken_restaurant", "sandwich_shop", "sushi_restaurant", "food_delivery_service",
              "chinese_restaurant", "fast_food"}
MUZ_RE = re.compile(r"(muzick\w* (i balet\w* )?(skol|atelje)|music school|school of music|rock ?school|"
                    r"pop rock skola|skola za muziku|osnovno muzicko)")
JAVNA_RE = re.compile(r"(osnovn|srednj|\bju\b|javn|mladen pozajic)")


def osm_mjesta(xml_gz, nodes):
    out = []
    with gzip.open(xml_gz, "rb") as f:
        for _, el in ET.iterparse(f):
            if el.tag in ("node", "way"):
                t = {c.get("k"): c.get("v") for c in el.findall("tag")}
                a, ime = t.get("amenity"), t.get("name", "")
                n = sup.bez_dijakritika(ime)
                vrsta = None
                if a in ("restaurant", "fast_food"):
                    vrsta = "fast_food" if a == "fast_food" else "restoran"
                elif a == "music_school" or (MUZ_RE.search(n) and a not in ("cafe", "university")):
                    vrsta = "muzicka_javna" if JAVNA_RE.search(n) else "muzicka_privatna"
                if vrsta:
                    if el.tag == "node":
                        xy = (float(el.get("lon")), float(el.get("lat")))
                    else:
                        p = [nodes[int(x.get("ref"))] for x in el.findall("nd") if int(x.get("ref")) in nodes]
                        xy = tuple(np.mean(p, axis=0)) if p else None
                    if xy:
                        out.append((vrsta, ime, *xy, "osm"))
                el.clear()
            elif el.tag == "relation":
                el.clear()
    return out


def overture_mjesta():
    g = gpd.read_parquet(RAW / "overture_places.parquet")
    g["kat"] = g.taxonomy.apply(lambda t: t.get("primary") if t is not None else None).fillna("")
    g["ime"] = g.names.apply(lambda n: n.get("primary") if n is not None else "")
    n = g.ime.map(sup.bez_dijakritika)
    ok = g.confidence >= 0.4
    if "operating_status" in g:
        ok &= g.operating_status.fillna("open").ne("permanently_closed")
    rest = ok & (g.kat.str.endswith("restaurant") | g.kat.isin(BRZA_HRANA)) & ~g.kat.str.contains("equipment")
    muz = ok & (((g.kat == "music_school") & ~n.str.contains("modular|mimika")) | n.str.contains(MUZ_RE))
    rows = []
    c = g.geometry.representative_point()
    for i in np.where(rest)[0]:
        rows.append(("fast_food" if g.kat.iat[i] in BRZA_HRANA else "restoran", g.ime.iat[i], c.x.iat[i], c.y.iat[i], "overture"))
    for i in np.where(muz)[0]:
        rows.append(("muzicka_javna" if JAVNA_RE.search(n.iat[i]) else "muzicka_privatna", g.ime.iat[i],
                     c.x.iat[i], c.y.iat[i], "overture"))
    return rows


def bez_duplikata(o: gpd.GeoDataFrame, prag: float) -> gpd.GeoDataFrame:
    """Isti objekt iz dva izvora: ista grupa (restoran/škola) bliže od praga; zadrži OSM, a za
    škole javnu verziju i višu privlačnost."""
    grp = o.vrsta.str.startswith("muzicka").to_numpy()
    xy = np.c_[o.geometry.x, o.geometry.y]
    keep = np.ones(len(o), bool)
    for i, j in sorted(cKDTree(xy).query_pairs(prag)):
        if keep[i] and keep[j] and grp[i] == grp[j]:
            bolji_i = (o.A.iat[i], o.izvor.iat[i] == "osm") >= (o.A.iat[j], o.izvor.iat[j] == "osm")
            keep[j if bolji_i else i] = False
    return o[keep].reset_index(drop=True)


def main() -> None:
    polja = gpd.read_file(OUT / "polja_h3.gpkg")
    acc = pd.read_csv(OUT / "dostupnost_h3.csv").set_index("h3_id").reindex(polja.h3_id)
    teren = pd.read_csv(OUT / "teren_h3.csv").set_index("h3_id").reindex(polja.h3_id)
    ulice = pd.read_csv(OUT / "ulice_h3.csv").set_index("h3_id").reindex(polja.h3_id)
    nodes, ways, _ = dost.ucitaj_mrezu(RAW / OSM_IME)
    _, land = sup.trgovine_i_zemljiste(RAW / OSM_IME, nodes)

    o = pd.DataFrame(osm_mjesta(RAW / OSM_IME, nodes) + overture_mjesta(),
                     columns=["vrsta", "ime", "lon", "lat", "izvor"])
    if (DATA / "rucno_mjesta.csv").exists():   # ručne dopune (npr. škole kojih nema u OSM/Overture)
        o = pd.concat([o, pd.read_csv(DATA / "rucno_mjesta.csv")[["vrsta", "ime", "lon", "lat", "izvor"]]], ignore_index=True)
    o = gpd.GeoDataFrame(o, geometry=gpd.points_from_xy(o.lon, o.lat), crs=CRS_WGS).to_crs(CRS_M)
    o["A"] = o.vrsta.map({"fast_food": 1.0, "restoran": 0.5, "muzicka_javna": 3.0, "muzicka_privatna": 1.0})
    o = bez_duplikata(o[o.vrsta.str.startswith("muzicka")], 40).pipe(
        lambda m: pd.concat([m, bez_duplikata(o[~o.vrsta.str.startswith("muzicka")], DUPLIKAT_M)], ignore_index=True))
    o = gpd.GeoDataFrame(o, crs=CRS_M)
    print("Objekti:", o.groupby(["vrsta", "izvor"]).size().to_dict())

    # --- zajedničko: mreža, polja, izgrađenost, ceste
    cen = polja.geometry.centroid
    cxy = np.c_[cen.x, cen.y]
    z = gpd.read_file(INTERIM / "zgrade.gpkg", columns=["geometry"])
    zc = gpd.GeoDataFrame({"a": z.area}, geometry=z.representative_point(), crs=z.crs)
    izgr = (gpd.sjoin(zc, polja[["h3_id", "geometry"]], predicate="within").groupby("h3_id").a.sum()
            / polja.set_index("h3_id").area).reindex(polja.h3_id).fillna(0).to_numpy()
    pu = gpd.read_file(OUT / "putevi.geojson").to_crs(CRS_M)
    pu = pu[pu.klasa.isin(["magistrala", "primarna", "sekundarna", "tercijarna"])]
    j = gpd.sjoin_nearest(gpd.GeoDataFrame(geometry=cen, crs=CRS_M), pu[["geometry"]], distance_col="d")
    cesta_m = j.groupby(level=0).d.min().reindex(range(len(polja))).fillna(9999).to_numpy()
    nagib = teren.nagib_pct.fillna(99).to_numpy()
    pristup = ulice.ocjena_pristupa.fillna(0).to_numpy()
    u4 = polja.opcina.notna().to_numpy()

    used = sorted({n for _, nds in ways for n in nds if n in nodes})
    idx = {n: k for k, n in enumerate(used)}
    pts = gpd.GeoSeries(gpd.points_from_xy(*zip(*[nodes[n] for n in used])), crs=CRS_WGS).to_crs(CRS_M)
    xy = np.c_[pts.x, pts.y]
    ll = np.array([nodes[n] for n in used])
    vis = dost.visine_cvorova(ll[:, 0], ll[:, 1])
    grafovi = {}

    def vremena(mod, orig, kol_xy, t_max):
        """Minute od centara polja `orig` do tačaka kol_xy (mreža + hod do i od mreže)."""
        if mod not in grafovi:
            G = dost.graf(nodes, ways, xy, idx, mod, visine=vis if mod == "pjesice" else None)
            _, lab = connected_components(G, directed=True, connection="strong" if mod == "auto" else "weak")
            ok = np.where(lab == np.bincount(lab).argmax())[0]
            grafovi[mod] = (G, ok, cKDTree(xy[ok]))
        G, ok, tr = grafovi[mod]
        dc, ic = tr.query(cxy[orig])
        dk, ik = tr.query(kol_xy)
        hod = lambda d: d / 1000 / dost.PJESACKA_BRZINA * 60  # noqa: E731
        T = np.full((len(orig), len(kol_xy)), np.inf, dtype=np.float32)
        for b in range(0, len(orig), 64):
            D = dijkstra(G, indices=ok[ic[b:b + 64]], limit=t_max)
            T[b:b + 64] = D[:, ok[ik]] + hod(dc[b:b + 64])[:, None] + hod(dk)[None, :]
        return np.maximum(T, 1.0)

    lg = gpd.GeoDataFrame({"vrsta": [v for v, _ in land]}, geometry=[Polygon(x) for _, x in land],
                          crs=CRS_WGS).to_crs(CRS_M)
    lg = lg[lg.is_valid & (lg.area > 0)]
    lg["m2"] = lg.area
    llc = cen.to_crs(CRS_WGS)

    def analiza(kljuc, naziv, potraznja, stopa, konk, kand, T_fn, t_max, lam, A_novo, t_blizu, prazno_fn,
                jedinica):
        orig = np.where(potraznja > 0)[0]
        p = potraznja[orig]
        K = np.where(kand)[0]
        s = konk.reset_index(drop=True)
        sxy = np.c_[s.geometry.x, s.geometry.y]
        Tc, Ts = T_fn(orig, cxy[K], t_max), T_fn(orig, sxy, t_max)
        U = lambda T: np.where(T <= t_max, T.astype(float) ** -lam, 0)  # noqa: E731
        Uc, Us = U(Tc) * A_novo, U(Ts)
        A = s.A.to_numpy()
        S0 = Us @ A
        nepokriveno = prazno_fn(Ts, A)
        print(f"\n### {naziv}: kandidat-polja {len(K)}, potražnja {p.sum():,.0f}, "
              f"bez ponude ({jedinica}): {p[nepokriveno].sum():,.0f}")
        B = Tc <= t_blizu
        rows = []
        for strat in ("najvise", "bijela_mrlja"):
            S, pok, mask = S0.copy(), ~nepokriveno, np.ones(len(K), bool)
            for r in range(1, N_IZBOR + 1):
                cap = p @ (Uc / (Uc + S[:, None] + 1e-12))
                score = cap.copy() if strat == "najvise" else (p * ~pok) @ B + 1e-3 * cap
                score[~mask] = -1
                ci = int(score.argmax())
                if score[ci] <= 0 or (strat == "bijela_mrlja" and ((p * ~pok) @ B)[ci] <= 0):
                    break
                c = K[ci]
                u = lg[lg.intersects(polja.geometry.iat[c])]
                rows.append({
                    "strategija": strat, "rang": r, "h3_id": polja.h3_id.iat[c], "opcina": polja.opcina.iat[c],
                    "mz": polja.mz.iat[c], "procjena": round(float(cap[ci]) * stopa, 1),
                    "potraznja_blizu": int(p[B[:, ci]].sum()),
                    "novo_pokriveno": int(p[B[:, ci] & ~pok].sum()),
                    "najblizi_konkurent_m": int(np.hypot(*(sxy - cxy[c]).T).min()),
                    "konkurenata_1500m": int((np.hypot(*(sxy - cxy[c]).T) <= 1500).sum()),
                    "cesta_m": int(cesta_m[c]), "stanica_m": int(acc.stanica_m.iat[c]),
                    "nagib_pct": float(nagib[c]),
                    "znakovi_zemljista": "; ".join(f"{v} {int(m):,} m²".replace(",", ".") for v, m in
                                                   u.groupby("vrsta").m2.sum().sort_values(ascending=False).items()) or "—",
                    "lon": round(llc.x.iat[c], 5), "lat": round(llc.y.iat[c], 5)})
                S = S + Uc[:, ci]
                pok |= B[:, ci]
                mask &= np.hypot(*(cxy[K] - cxy[c]).T) >= 800
        out = pd.DataFrame(rows)
        out.to_csv(OUT / f"biz_{kljuc}_kandidati.csv", index=False)
        P0 = Us * A / (S0 + 1e-12)[:, None]
        ll_s = s.to_crs(CRS_WGS).geometry
        s.assign(procjena=(stopa * (p @ P0)).round(1), lon=ll_s.x.round(5), lat=ll_s.y.round(5))[
            ["vrsta", "ime", "izvor", "A", "procjena", "lon", "lat"]].sort_values("procjena", ascending=False) \
            .to_csv(OUT / f"biz_{kljuc}_postojeci.csv", index=False)
        mn = np.full(len(polja), np.nan)
        mn[orig] = np.round(np.minimum(Ts.min(axis=1).astype(float), 99), 1)
        ponuda = np.full(len(polja), np.nan)
        ponuda[orig] = (Ts <= t_blizu).sum(axis=1)
        pd.DataFrame({"h3_id": polja.h3_id, "min_do_najblizeg": mn, "u_blizini": ponuda}).to_csv(
            OUT / f"biz_{kljuc}_pokrivenost.csv", index=False)
        pd.set_option("display.width", 250)
        for st, g in out.groupby("strategija", sort=False):
            print(f"== {st}")
            print(g.drop(columns=["strategija", "h3_id", "lon", "lat"]).to_string(index=False))

    # --- dostavna kuhinja
    odrasli = polja.d15_64.to_numpy(float) + 0.2 * polja.d65plus.to_numpy(float)
    rest = o[o.vrsta.isin(["fast_food", "restoran"])]
    kand = u4 & (cesta_m <= 100) & (nagib <= 10) & (pristup >= 50)
    analiza("dostava", "Dostavna kuhinja", odrasli, 0.03, rest, kand,
            lambda orig, kxy, tm: vremena("auto", orig, kxy, tm), 15.0, 1.0, 2.0, 10.0,
            lambda Ts, A: (Ts <= 10).sum(axis=1) < 10, "manje od 10 restorana u 10 min vožnje")

    # --- muzička škola
    djeca = 0.55 * polja.d0_14.to_numpy(float) + 0.04 * polja.d15_64.to_numpy(float)
    ms = o[o.vrsta.str.startswith("muzicka")]
    print("Muzičke škole:", ms[["vrsta", "ime", "izvor"]].to_string(index=False))
    kand = (u4 & ((acc.stanica_m.to_numpy() <= 400) | (cesta_m <= 150)) & (nagib <= 12) & (pristup >= 40)
            & (izgr >= 0.05))

    def t_muz(orig, kxy, tm):
        return np.minimum(vremena("pjesice", orig, kxy, tm), vremena("auto", orig, kxy, tm) + 3)

    analiza("muzicka", "Muzička škola", djeca, 0.05, ms, kand, t_muz, 20.0, 2.0, 1.0, 15.0,
            lambda Ts, A: Ts.min(axis=1) > 15, "nijedna škola u 15 min")


if __name__ == "__main__":
    main()
