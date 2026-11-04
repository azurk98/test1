"""Najbolje slobodne lokacije za novi supermarket (Huffov gravitacijski model).

Ulaz:  raw/Sarajewo.osm.gz (mreža, postojeće trgovine, namjena zemljišta),
       raw/overture_places.parquet (Overture Maps Places; dopuna trgovina koje OSM nema),
       out/polja_h3.gpkg (stanovnici), out/dostupnost_h3.csv
Izlaz: out/supermarket_kandidati.csv/.gpkg (dvije strategije: bijela_mrlja, najveci_promet),
       out/supermarket_postojeci.csv (postojeće trgovine s kupcima po modelu),
       out/supermarket_pokrivenost.csv (minute pješice do najbližeg supermarketa po polju),
       out/supermarket_trgovine.csv

Model
-----
Domaćinstvo u polju i kupuje u trgovini j s vjerovatnoćom
    P_ij = A_j · t_ij^-λ / Σ_k A_k · t_ik^-λ          (t ≤ T_MAX, inače 0)
A_j je privlačnost (veličina) trgovine, t_ij vrijeme putovanja u minutama:
min(pješice, autom + 2 min parkiranje), najmanje 1 min. λ = 2 (uobičajeno
za namirnice). Nova trgovina standardne veličine (A = 1) u polju c osvaja
    Σ_i stanovnici_i · P_ic.
Lokacije se biraju redom (pohlepno): nakon svakog izbora nova trgovina
ulazi u konkurenciju, pa sljedeći izbor ne kanibalizuje prethodni.

"Slobodno" polje: u njemu nema supermarketa (convenience je dozvoljen) i
glavna cesta je na najviše MAX_CESTA_M. Za svako polje navode se znakovi
mogućeg zemljišta (gradilište, napušteno zemljište, parking, veći poslovni
objekat) — stvarnu dostupnost parcele treba provjeriti na terenu i u katastru.
Potražnja postoji samo u četiri modelirane općine; konkurencija se računa
iz cijelog OSM ekstrakta (i Ilidža, Vogošća).
"""
from __future__ import annotations

import gzip
import importlib.util
import re
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
from scipy.sparse.csgraph import connected_components, dijkstra
from scipy.spatial import cKDTree
from shapely.geometry import Polygon

from common import CRS_M, CRS_WGS, OUT, RAW

_s = importlib.util.spec_from_file_location("dost", Path(__file__).with_name("08_dostupnost.py"))
dost = importlib.util.module_from_spec(_s)
_s.loader.exec_module(dost)

LAMBDA = 2.0
LAMBDE_TEST = (1.5, 2.0, 2.5)
T_MAX = 20.0          # min; dalje se ne ide u kupovinu namirnica
PARKING_MIN = 2.0
MAX_CESTA_M = 400
N_IZBOR = 10
MIN_RAZMAK_M = 700    # izabrane lokacije ne bliže od ovoga

# privlačnost postojećih trgovina (supermarket ~1000 m² = 1)
A_TIP = {"supermarket": 1.0, "mall": 1.0,  # OSM "mall" uključuje i poslovne centre bez marketa
         "department_store": 0.5, "convenience": 0.25,
         "grocery": 0.25, "general": 0.25, "greengrocer": 0.1}
NIJE_NAMIRNICE = {"dm", "müller", "muller", "lilly", "dm drogerie markt"}

# Overture Maps Places (raw/overture_places.parquet) kao drugi izvor trgovina
OVERTURE_KAT = {"grocery_store", "supermarket", "convenience_store", "hypermarket", "discount_store"}
LANCI = re.compile(r"\b(bingo|konzum|amko|mercator|robot|hose|megamarkt|tropic|deny|merkur|penny|klas|neo market)\b")
NIJE_NAMIRNICE_RE = re.compile(
    r"(aparat|tehnik|pcelar|slastic|serdz|home|health|apoteka|ljekarn|cvjecar|kozmet|cosmetic|candy|boutique|"
    r"namjestaj|tekstil|obuc|parfem|elektro|auto|sport|book|knjig|vulkan|kinesk|jumbo|trading|limited|"
    r"bureg|burek|pekar|caff|cafe|ambalaz|\bart\b|art$|mesnic|plantaz|frutta|\bd\.? ?o\.? ?o\b|komerc|b ?& ?h|"
    r"\bmarketi\b|edeka|1\.99|gric|bariba|smart mjesto)")
OVERTURE_MIN_POUZDANOST = 0.4
DUPLIKAT_M = 75


def bez_dijakritika(s) -> str:
    s = unicodedata.normalize("NFKD", str(s or "").lower().replace("đ", "dj"))
    return "".join(c for c in s if not unicodedata.combining(c))


def overture_trgovine(osm: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Trgovine namirnica iz Overture koje nisu u OSM-u (dalje od DUPLIKAT_M)."""
    f = RAW / "overture_places.parquet"
    if not f.exists():
        return osm.iloc[0:0]
    g = gpd.read_parquet(f)
    g["kat"] = g.taxonomy.apply(lambda t: t.get("primary") if t is not None else None)
    g["ime"] = g.names.apply(lambda n: n.get("primary") if n is not None else "")
    n = g.ime.map(bez_dijakritika)
    lanac = n.str.contains(LANCI)
    ok = (g.kat.isin(OVERTURE_KAT) | ((g.kat == "shopping") & lanac)) & ~n.str.contains(NIJE_NAMIRNICE_RE)
    ok &= (g.confidence >= OVERTURE_MIN_POUZDANOST) | lanac
    if "operating_status" in g:
        ok &= g.operating_status.fillna("open").ne("permanently_closed")
    v = g[ok].to_crs(CRS_M).copy()
    v["geometry"] = v.geometry.representative_point()
    v["tip"] = np.where(lanac[ok] | v.kat.isin(["supermarket", "hypermarket"]), "supermarket", "convenience")
    t = cKDTree(np.c_[osm.geometry.x, osm.geometry.y])
    d, _ = t.query(np.c_[v.geometry.x, v.geometry.y])
    v = v[d > DUPLIKAT_M]
    return gpd.GeoDataFrame({"tip": v.tip, "ime": v.ime, "izvor": "overture"}, geometry=v.geometry, crs=CRS_M)


def trgovine_i_zemljiste(xml_gz, nodes):
    shops, land = [], []
    with gzip.open(xml_gz, "rb") as f:
        for _, el in ET.iterparse(f):
            if el.tag in ("node", "way"):
                t = {c.get("k"): c.get("v") for c in el.findall("tag")}
                tip = t.get("shop")
                ime = (t.get("brand") or t.get("name") or "").strip()
                if el.tag == "node":
                    xy = [(float(el.get("lon")), float(el.get("lat")))]
                else:
                    xy = [nodes[int(n.get("ref"))] for n in el.findall("nd") if int(n.get("ref")) in nodes]
                if tip in A_TIP and ime.lower() not in NIJE_NAMIRNICE and xy:
                    shops.append((el.tag, tip, ime, xy))
                if el.tag == "way" and len(xy) >= 4:
                    vrsta = None
                    if t.get("landuse") in ("construction", "brownfield", "greenfield"):
                        vrsta = t["landuse"]
                    elif t.get("amenity") == "parking" and t.get("parking", "surface") == "surface":
                        vrsta = "parking"
                    elif t.get("building") in ("retail", "commercial", "warehouse", "industrial"):
                        vrsta = "poslovni_objekat"
                    if vrsta:
                        land.append((vrsta, xy))
                el.clear()
            elif el.tag == "relation":
                el.clear()
    return shops, land


def main() -> None:
    polja = gpd.read_file(OUT / "polja_h3.gpkg")
    acc = pd.read_csv(OUT / "dostupnost_h3.csv").set_index("h3_id")
    nodes, ways, _ = dost.ucitaj_mrezu(RAW / "Sarajewo.osm.gz")
    shops, land = trgovine_i_zemljiste(RAW / "Sarajewo.osm.gz", nodes)

    # --- postojeće trgovine (tačke; poligoni -> težište, A po površini)
    rows = []
    for tag, tip, ime, xy in shops:
        if tag == "node":
            g, pov = gpd.points_from_xy([xy[0][0]], [xy[0][1]])[0], None
        else:
            poly = Polygon(xy)
            if not poly.is_valid or poly.area == 0:
                continue
            g, pov = poly.representative_point(), poly
        rows.append({"tip": tip, "ime": ime, "geometry": g, "poly": pov})
    s = gpd.GeoDataFrame(rows, crs=CRS_WGS).to_crs(CRS_M)
    povr = gpd.GeoSeries([p if p is not None else None for p in s.poly], crs=CRS_WGS).to_crs(CRS_M).area
    s["A"] = s.tip.map(A_TIP)
    vel = (s.tip == "supermarket") & povr.notna() & (povr > 0)
    s.loc[vel, "A"] = np.clip(povr[vel] / 1000, 0.5, 4.0)
    s = s.drop(columns="poly")
    # duplikati: ista vrsta trgovine bliže od 40 m (tačka u poligonu i sl.)
    xy_s = np.c_[s.geometry.x, s.geometry.y]
    keep = np.ones(len(s), bool)
    t = cKDTree(xy_s)
    for i, j in sorted(t.query_pairs(40)):
        if keep[i] and keep[j] and s.tip.iat[i] == s.tip.iat[j]:
            keep[j if s.A.iat[i] >= s.A.iat[j] else i] = False
    s = s[keep].reset_index(drop=True)
    s["izvor"] = "osm"
    ov = overture_trgovine(s)
    ov["A"] = ov.tip.map(A_TIP)
    s = gpd.GeoDataFrame(pd.concat([s, ov], ignore_index=True), crs=CRS_M)
    print(f"Postojeće trgovine: {s.groupby(['izvor', 'tip']).size().to_dict()}")

    # --- mreža i čvorovi
    used = sorted({n for _, nds in ways for n in nds if n in nodes})
    idx = {n: k for k, n in enumerate(used)}
    pts = gpd.GeoSeries(gpd.points_from_xy(*zip(*[nodes[n] for n in used])), crs=CRS_WGS).to_crs(CRS_M)
    xy = np.c_[pts.x, pts.y]
    cen = polja.geometry.centroid
    cxy = np.c_[cen.x, cen.y]
    pop = polja.stanovnici.to_numpy(float)
    orig = np.where(pop > 0)[0]

    def vremena(mod):
        G = dost.graf(nodes, ways, xy, idx, mod)
        _, lab = connected_components(G, directed=True, connection="strong" if mod == "auto" else "weak")
        ok = np.where(lab == np.bincount(lab).argmax())[0]
        tr = cKDTree(xy[ok])
        dc, ic = tr.query(cxy)
        ds, is_ = tr.query(np.c_[s.geometry.x, s.geometry.y])
        nc, ns = ok[ic], ok[is_]
        hod = lambda d: d / 1000 / dost.PJESACKA_BRZINA * 60  # noqa: E731
        Tc = np.full((len(orig), len(polja)), np.inf)
        Ts = np.full((len(orig), len(s)), np.inf)
        for b in range(0, len(orig), 64):
            o = orig[b:b + 64]
            D = dijkstra(G, indices=nc[o], limit=T_MAX)
            Tc[b:b + 64] = D[:, nc] + hod(dc[o])[:, None] + hod(dc)[None, :]
            Ts[b:b + 64] = D[:, ns] + hod(dc[o])[:, None] + hod(ds)[None, :]
        return Tc, Ts

    Wc, Ws = vremena("pjesice")
    Cc, Cs = vremena("auto")
    Tc = np.maximum(np.minimum(Wc, Cc + PARKING_MIN), 1.0)
    Ts = np.maximum(np.minimum(Ws, Cs + PARKING_MIN), 1.0)
    p = pop[orig]

    def util(T, lam):
        U = T ** -lam
        U[T > T_MAX] = 0
        return U

    # --- kandidati: polja bez supermarketa, blizu glavne ceste, u 4 općine
    sp = gpd.sjoin(s[s.tip.isin(["supermarket", "mall", "department_store"])], polja[["h3_id", "geometry"]],
                   predicate="within")
    ima = set(sp.h3_id)
    cesta = acc.reindex(polja.h3_id).glavna_cesta_m.to_numpy()
    kand = np.array([(h not in ima) and (c <= MAX_CESTA_M) for h, c in zip(polja.h3_id, cesta)])

    def izbor(lam, n=N_IZBOR):
        Uc = util(Tc, lam)
        S = util(Ts, lam) @ s.A.to_numpy()
        izabrano, prihod = [], []
        mask = kand.copy()
        for _ in range(n):
            cap = p @ (Uc / (Uc + S[:, None] + 1e-12))
            cap[~mask] = -1
            c = int(cap.argmax())
            izabrano.append(c)
            prihod.append(cap[c])
            S = S + Uc[:, c]
            mask &= np.hypot(*(cxy - cxy[c]).T) >= MIN_RAZMAK_M
        return izabrano, prihod

    izb, kup = izbor(LAMBDA)

    # osjetljivost na λ: koliko izabranih ostaje u top 10 (unutar 1 polja)
    stab = {}
    for lam in LAMBDE_TEST:
        if lam == LAMBDA:
            continue
        drugi, _ = izbor(lam)
        tr = cKDTree(cxy[drugi])
        stab[lam] = [tr.query(cxy[c])[0] <= 400 for c in izb]

    # pokrivenost danas
    U0 = util(Ts, LAMBDA)
    bez_10 = (Ws.min(axis=1) > 10)  # nema trgovine (bilo koje) u 10 min pješice
    sup = s.tip.isin(["supermarket", "mall", "department_store"]).to_numpy()
    bez_sup_10 = (Ws[:, sup].min(axis=1) > 10)
    print(f"Stanovnici bez ijedne trgovine namirnica u 10 min pješice: {p[bez_10].sum():,.0f}; "
          f"bez supermarketa: {p[bez_sup_10].sum():,.0f} od {p.sum():,.0f}")

    # znakovi zemljišta u polju
    lg = gpd.GeoDataFrame({"vrsta": [v for v, _ in land]}, geometry=[Polygon(x) for _, x in land],
                          crs=CRS_WGS).to_crs(CRS_M)
    lg = lg[lg.is_valid & (lg.area > 0)]
    lg["m2"] = lg.area

    # postojeći tržišni udio konkurencije u Huffu (za kontekst)
    P0 = U0 * s.A.to_numpy() / (U0 @ s.A.to_numpy() + 1e-12)[:, None]
    s["kupci_model"] = (p @ P0).round()
    s[["tip", "ime", "A", "izvor", "kupci_model"]].assign(
        lon=s.to_crs(CRS_WGS).geometry.x.round(5), lat=s.to_crs(CRS_WGS).geometry.y.round(5)
    ).sort_values("kupci_model", ascending=False).to_csv(OUT / "supermarket_postojeci.csv", index=False)

    def izbor_praznine(lam=LAMBDA, n=N_IZBOR):
        """Bijele mrlje: redom bira polje koje najviše stanovnika bez supermarketa
        u 10 min pješice dovodi u 10 min pješice; uz to računa Huffove kupce."""
        Uc = util(Tc, lam)
        S = util(Ts, lam) @ s.A.to_numpy()
        pokriveno = ~bez_sup_10
        mask = kand.copy()
        W10 = Wc <= 10
        izabrano, prihod = [], []
        for _ in range(n):
            dobit = (p * ~pokriveno) @ W10
            cap = p @ (Uc / (Uc + S[:, None] + 1e-12))
            score = dobit + 1e-3 * cap
            score[~mask] = -1
            c = int(score.argmax())
            if dobit[c] <= 0:
                break
            izabrano.append(c)
            prihod.append(cap[c])
            pokriveno |= W10[:, c]
            S = S + Uc[:, c]
            mask &= np.hypot(*(cxy - cxy[c]).T) >= MIN_RAZMAK_M
        return izabrano, prihod

    sx = np.c_[s.geometry.x, s.geometry.y]
    ts = cKDTree(sx[sup])

    def tabela(izb, kup, strategija, stab=None):
      rows = []
      for r, (c, k) in enumerate(zip(izb, kup), 1):
        hexg = polja.geometry.iat[c]
        u = lg[lg.intersects(hexg)]
        hint = "; ".join(f"{v} {int(m):,} m²".replace(",", ".") for v, m in
                         u.groupby("vrsta").m2.sum().sort_values(ascending=False).items()) or "—"
        d_sup, _ = ts.query(cxy[c])
        w10 = Wc[:, c] <= 10
        rows.append({
            "strategija": strategija, "rang": r, "h3_id": polja.h3_id.iat[c], "opcina": polja.opcina.iat[c], "mz": polja.mz.iat[c],
            "kupci_procjena": int(round(k)),
            "stanovnici_10min_pjesice": int(p[w10].sum()),
            "od_toga_bez_supermarketa_10min": int(p[w10 & bez_sup_10].sum()),
            "najblizi_supermarket_m": int(d_sup),
            "glavna_cesta_m": int(cesta[c]),
            "stabilno_lambda": "/".join("da" if v[r - 1] else "ne" for v in stab.values()) if stab else "",
            "znakovi_zemljista": hint,
            "lon": round(polja.to_crs(CRS_WGS).geometry.centroid.x.iat[c], 5),
            "lat": round(polja.to_crs(CRS_WGS).geometry.centroid.y.iat[c], 5),
        })
      return rows

    # pokrivenost po polju (naseljena polja): minute pješice do najbližeg supermarketa
    min_sup = np.full(len(polja), np.nan)
    min_sup[orig] = np.round(np.minimum(Ws[:, sup].min(axis=1), 99), 1)
    pd.DataFrame({"h3_id": polja.h3_id, "supermarket_pjesice_min": min_sup}).to_csv(
        OUT / "supermarket_pokrivenost.csv", index=False)
    s.assign(lon=s.to_crs(CRS_WGS).geometry.x.round(5), lat=s.to_crs(CRS_WGS).geometry.y.round(5))[
        ["tip", "ime", "A", "izvor", "lon", "lat"]].to_csv(OUT / "supermarket_trgovine.csv", index=False)

    izb2, kup2 = izbor_praznine()
    out = pd.DataFrame(tabela(izb2, kup2, "bijela_mrlja") + tabela(izb, kup, "najveci_promet", stab))
    izb_sve = izb2 + izb
    out.to_csv(OUT / "supermarket_kandidati.csv", index=False)
    gpd.GeoDataFrame(out, geometry=[polja.geometry.iat[c] for c in izb_sve], crs=CRS_M).to_file(
        OUT / "supermarket_kandidati.gpkg", driver="GPKG")
    pd.set_option("display.width", 250)
    for st, g in out.groupby("strategija", sort=False):
        print(f"\n== {st}")
        print(g.drop(columns=["strategija", "h3_id", "lon", "lat"]).to_string(index=False))
    print(f"(stabilno_lambda: ostaje li lokacija među izabranima uz λ = {', '.join(map(str, stab))})")


if __name__ == "__main__":
    main()
