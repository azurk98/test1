"""Gdje otvoriti autopraonicu: Huffov model na vremenu vožnje + promet koji prolazi.

Ulaz:  raw/Sarajewo.osm.gz (mreža, amenity=car_wash, pumpe, namjena zemljišta),
       raw/overture_places.parquet (autopraonice/detailing koje OSM nema),
       out/polja_h3.gpkg (stanovnici), out/putevi.geojson (klase cesta),
       out/teren_h3.csv (nagib), out/ulice_h3.csv (uske/strme ulice)
Izlaz: out/autopraonica_kandidati.csv (dvije strategije: najveci_promet, bijela_mrlja),
       out/autopraonica_postojece.csv (postojeće praonice s kupcima po modelu)

Model (procjena, ne poslovni plan)
----------------------------------
Autopraonica živi od dvije vrste kupaca:
  1. stanovnici u blizini: Huff na vremenu vožnje, λ = 2, najviše T_MAX = 12 min;
     postojeće praonice imaju privlačnost A (praonica 1, pumpa s pranjem 0,6, detailing 0,4)
  2. promet koji prolazi: kupac svraća usput, pa vrijedi vidljiva lokacija na prometnoj cesti.
     Nema brojanja saobraćaja (PGDP), pa se koristi tipični promet po klasi ceste
     (PROMET_KLASA, vozila/dan) i udio koji svrati, umanjen konkurencijom na 1 km.
  Obje vrste se svode na pranja mjesečno (red veličine, za poređenje lokacija):
    od stanovnika = Huffov udio stanovnika · AUTA_PO_STANOVNIKU · PRANJA_PO_AUTU_MJ
    od prolaza    = promet/dan · UDIO_SVRATI · 30 / (1 + praonice na ≤ 1 km)
  Gusto izgrađena polja (zgrade > MAX_IZGRADJENOST površine) se ne nude: nema mjesta za plac.

Kandidat (polje H3): u šest općina, cesta klase magistrala/primarna/sekundarna/tercijarna
na ≤ MAX_CESTA_M od centra polja (autoput nema direktan pristup), nagib terena ≤ MAX_NAGIB %,
ocjena pristupa ulica ≥ 50, bez postojeće praonice u polju. Lokacije se biraju redom
(pohlepno) uz razmak ≥ MIN_RAZMAK_M. Strategija "bijela_mrlja" bira polja koja najviše
stanovnika bez praonice u 5 min vožnje dovode u 5 min vožnje.

Ograničenja: nema podataka o broju automobila po domaćinstvu ni o prometu po ulici;
OSM/Overture nemaju sve praonice (naročito ručne praonice uz vulkanizere); stvarnu
parcelu, priključak vode i kanalizacije i dozvole treba provjeriti posebno.
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
from common import CRS_M, CRS_WGS, INTERIM, OUT, RAW


def _uvezi(ime, fajl):
    s = importlib.util.spec_from_file_location(ime, Path(__file__).with_name(fajl))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


dost = _uvezi("dost", "08_dostupnost.py")
sup = _uvezi("sup", "09_supermarket.py")

LAMBDA = 2.0
T_MAX = 12.0            # min vožnje
T_BLIZU = 5.0           # "ima praonicu blizu"
MAX_CESTA_M = 60
MAX_NAGIB = 8.0
MIN_PRISTUP = 50
MIN_RAZMAK_M = 800
N_IZBOR = 10
DUPLIKAT_M = 60
# tipičan promet (vozila/dan) po klasi ceste u gradu; pretpostavka, ne mjerenje
PROMET_KLASA = {"magistrala": 30000, "primarna": 20000, "sekundarna": 10000, "tercijarna": 4000}
UDIO_SVRATI = 0.001     # udio vozila koja dnevno svrate na pranje kad nema konkurencije (pretpostavka)
AUTA_PO_STANOVNIKU = 0.35   # red veličine za KS (registrovana putnička vozila / stanovnik)
PRANJA_PO_AUTU_MJ = 1.0     # pranja u praonici mjesečno po autu (pretpostavka; zimi više, ljeti manje)
MAX_IZGRADJENOST = 0.30
PROLAZ_KONKURENCIJA_M = 1000
A_TIP = {"praonica": 1.0, "pumpa_pranje": 0.6, "detailing": 0.4}
PRAONICA_RE = re.compile(r"(praon|car ?wash|perionic|samousluz|self ?wash|auto ?spa)")
DETAILING_RE = re.compile(r"detail")
NIJE_AUTO_RE = re.compile(r"(tepih|cilim|rubl|vesa|namjestaj)")  # praonice ćilima i rublja


def osm_objekti(xml_gz, nodes):
    """Praonice, pumpe (s oznakom pranja ili bez) iz OSM-a: (vrsta, ime, lon, lat)."""
    out = []
    with gzip.open(xml_gz, "rb") as f:
        for _, el in ET.iterparse(f):
            if el.tag in ("node", "way"):
                t = {c.get("k"): c.get("v") for c in el.findall("tag")}
                a = t.get("amenity")
                pere = t.get("car_wash") == "yes" or t.get("service:vehicle:car_wash") == "yes"
                if a == "car_wash" or a == "fuel" or pere:
                    if el.tag == "node":
                        xy = (float(el.get("lon")), float(el.get("lat")))
                    else:
                        p = [nodes[int(n.get("ref"))] for n in el.findall("nd") if int(n.get("ref")) in nodes]
                        if not p:
                            el.clear()
                            continue
                        xy = tuple(np.mean(p, axis=0))
                    vrsta = ("praonica" if a == "car_wash" else "pumpa_pranje" if pere and a == "fuel"
                             else "pumpa" if a == "fuel" else "praonica")
                    out.append((vrsta, t.get("brand") or t.get("name") or "", *xy, "osm"))
                el.clear()
            elif el.tag == "relation":
                el.clear()
    return out


def overture_objekti():
    g = gpd.read_parquet(RAW / "overture_places.parquet")
    g["kat"] = g.taxonomy.apply(lambda t: t.get("primary") if t is not None else None)
    g["ime"] = g.names.apply(lambda n: n.get("primary") if n is not None else "")
    n = g.ime.map(sup.bez_dijakritika)
    pr = (n.str.contains(PRAONICA_RE) | (g.kat == "car_wash")) & ~(n.str.contains(NIJE_AUTO_RE) & ~n.str.contains("auto|car"))
    de = (g.kat == "auto_detailing") | n.str.contains(DETAILING_RE)
    pu = g.kat == "gas_station"
    ok = (pr | de | pu) & (g.confidence >= 0.3)
    if "operating_status" in g:
        ok &= g.operating_status.fillna("open").ne("permanently_closed")
    v = g[ok].copy()
    v["vrsta"] = np.where(pr[ok], "praonica", np.where(de[ok], "detailing", "pumpa"))
    c = v.geometry.representative_point()
    return [(r, i, x, y, "overture") for r, i, x, y in zip(v.vrsta, v.ime, c.x, c.y)]


def main() -> None:
    polja = gpd.read_file(OUT / "polja_h3.gpkg")
    teren = pd.read_csv(OUT / "teren_h3.csv").set_index("h3_id").reindex(polja.h3_id)
    ulice = pd.read_csv(OUT / "ulice_h3.csv").set_index("h3_id").reindex(polja.h3_id)
    nodes, ways, _ = dost.ucitaj_mrezu(RAW / OSM_IME)
    _, land = sup.trgovine_i_zemljiste(RAW / OSM_IME, nodes)

    # --- postojeće praonice i pumpe (OSM prvo, Overture samo ako nema ničega iste vrste na 60 m)
    o = pd.DataFrame(osm_objekti(RAW / OSM_IME, nodes) + overture_objekti(),
                     columns=["vrsta", "ime", "lon", "lat", "izvor"])
    o = gpd.GeoDataFrame(o, geometry=gpd.points_from_xy(o.lon, o.lat), crs=CRS_WGS).to_crs(CRS_M)
    xy_o = np.c_[o.geometry.x, o.geometry.y]
    keep = np.ones(len(o), bool)
    grupa = o.vrsta.replace({"pumpa_pranje": "pumpa"}).to_numpy()
    for i, j in sorted(cKDTree(xy_o).query_pairs(DUPLIKAT_M)):
        if keep[i] and keep[j] and (grupa[i] == grupa[j] or {grupa[i], grupa[j]} == {"praonica", "detailing"}):
            # zadrži OSM; između praonice i detailinga zadrži praonicu
            keep[j if (o.izvor.iat[i] == "osm" or o.vrsta.iat[i] == "praonica") else i] = False
    o = o[keep].reset_index(drop=True)
    # pumpa uz koju je praonica (≤ 60 m) računa se samo kao praonica
    pr_xy = xy_o[keep][o.vrsta.isin(["praonica", "detailing"]).to_numpy()]
    if len(pr_xy):
        d_p, _ = cKDTree(pr_xy).query(np.c_[o.geometry.x, o.geometry.y])
        o = o[~((o.vrsta == "pumpa_pranje") & (d_p <= DUPLIKAT_M))].reset_index(drop=True)
    print("Objekti:", o.groupby(["izvor", "vrsta"]).size().to_dict())
    s = o[o.vrsta.isin(A_TIP)].reset_index(drop=True)
    s["A"] = s.vrsta.map(A_TIP)
    pumpe = o[o.vrsta.isin(["pumpa", "pumpa_pranje"])]

    # --- ceste uz polje
    pu = gpd.read_file(OUT / "putevi.geojson").to_crs(CRS_M)
    pu = pu[pu.klasa.isin(PROMET_KLASA)]
    cen = polja.geometry.centroid
    cxy = np.c_[cen.x, cen.y]
    cg = gpd.GeoDataFrame(geometry=cen, crs=CRS_M)
    promet = np.zeros(len(polja))
    klasa = np.array([""] * len(polja), dtype=object)
    ime_ceste = np.array([""] * len(polja), dtype=object)
    for k in sorted(PROMET_KLASA, key=PROMET_KLASA.get):          # veća klasa prepisuje manju
        j = gpd.sjoin_nearest(cg, pu[pu.klasa == k][["ime", "geometry"]], max_distance=MAX_CESTA_M,
                              how="inner").groupby(level=0).first()
        promet[j.index] = PROMET_KLASA[k]
        klasa[j.index] = k
        ime_ceste[j.index] = j.ime.fillna("").to_numpy()

    z = gpd.read_file(INTERIM / "zgrade.gpkg", columns=["geometry"])
    zc = gpd.GeoDataFrame({"a": z.area}, geometry=z.representative_point(), crs=z.crs)
    izgr = (gpd.sjoin(zc, polja[["h3_id", "geometry"]], predicate="within").groupby("h3_id").a.sum()
            / polja.set_index("h3_id").area).reindex(polja.h3_id).fillna(0).to_numpy()
    sp = gpd.sjoin(s, polja[["h3_id", "geometry"]], predicate="within")
    ima = set(sp.h3_id)
    kand = ((promet > 0) & (polja.opcina.notna()).to_numpy()
            & (teren.nagib_pct.fillna(99).to_numpy() <= MAX_NAGIB)
            & (ulice.ocjena_pristupa.fillna(0).to_numpy() >= MIN_PRISTUP)
            & (izgr <= MAX_IZGRADJENOST) & ~polja.h3_id.isin(ima).to_numpy())
    K = np.where(kand)[0]
    print(f"Kandidat-polja: {len(K)} od {len(polja)}")

    # --- vremena vožnje
    used = sorted({n for _, nds in ways for n in nds if n in nodes})
    idx = {n: k for k, n in enumerate(used)}
    pts = gpd.GeoSeries(gpd.points_from_xy(*zip(*[nodes[n] for n in used])), crs=CRS_WGS).to_crs(CRS_M)
    xy = np.c_[pts.x, pts.y]
    G = dost.graf(nodes, ways, xy, idx, "auto")
    _, lab = connected_components(G, directed=True, connection="strong")
    ok = np.where(lab == np.bincount(lab).argmax())[0]
    tr = cKDTree(xy[ok])
    dc, ic = tr.query(cxy)
    ds, is_ = tr.query(np.c_[s.geometry.x, s.geometry.y])
    nc, ns = ok[ic], ok[is_]
    pop = polja.stanovnici.to_numpy(float)
    orig = np.where(pop > 0)[0]
    p = pop[orig]
    hod = lambda d: d / 1000 / dost.PJESACKA_BRZINA * 60  # noqa: E731  (od centra polja do ceste)
    Tc = np.full((len(orig), len(K)), np.inf, dtype=np.float32)
    Ts = np.full((len(orig), len(s)), np.inf, dtype=np.float32)
    for b in range(0, len(orig), 64):
        oo = orig[b:b + 64]
        D = dijkstra(G, indices=nc[oo], limit=T_MAX)
        Tc[b:b + 64] = D[:, nc[K]] + hod(dc[oo])[:, None] + 0.5
        Ts[b:b + 64] = D[:, ns] + hod(dc[oo])[:, None] + 0.5
    Tc, Ts = np.maximum(Tc, 1.0), np.maximum(Ts, 1.0)

    def util(T):
        U = T ** -LAMBDA
        U[T > T_MAX] = 0
        return U

    Uc, Us = util(Tc), util(Ts)
    A = s.A.to_numpy()
    S0 = Us @ A
    # prolazni promet: udio svratišta dijeli se s praonicama na ≤ 1 km
    sxy = np.c_[s.geometry.x, s.geometry.y]
    ts = cKDTree(sxy)
    konk = np.array([A[ts.query_ball_point(cxy[c], PROLAZ_KONKURENCIJA_M)].sum() for c in K])
    PR = UDIO_SVRATI * 30
    MJ = AUTA_PO_STANOVNIKU * PRANJA_PO_AUTU_MJ
    prolaz = promet[K] * PR / (1 + konk)

    blizu0 = (Ts <= T_BLIZU).any(axis=1)
    print(f"Stanovnici bez praonice u {T_BLIZU:.0f} min vožnje: {p[~blizu0].sum():,.0f} od {p.sum():,.0f}; "
          f"bez ijedne u {T_MAX:.0f} min: {p[Us.sum(axis=1) == 0].sum():,.0f}")

    def izbor(strategija):
        S = S0.copy()
        pokriveno = blizu0.copy()
        B = Tc <= T_BLIZU
        mask = np.ones(len(K), bool)
        pr = prolaz.copy()
        kk = konk.copy()
        izb, kup_st, kup_pr = [], [], []
        for _ in range(N_IZBOR):
            st = MJ * (p @ (Uc / (Uc + S[:, None] + 1e-12)))
            pot = st + pr
            if strategija == "bijela_mrlja":
                dobit = (p * ~pokriveno) @ B
                score = dobit + 1e-2 * pot
            else:
                score = pot
            score[~mask] = -1
            ci = int(score.argmax())
            if score[ci] <= 0:
                break
            izb.append(ci); kup_st.append(st[ci]); kup_pr.append(pr[ci])
            S = S + Uc[:, ci]
            pokriveno |= B[:, ci]
            d = np.hypot(*(cxy[K] - cxy[K[ci]]).T)
            mask &= d >= MIN_RAZMAK_M
            kk = kk + (d <= PROLAZ_KONKURENCIJA_M)
            pr = promet[K] * PR / (1 + kk)
        return izb, kup_st, kup_pr

    lg = gpd.GeoDataFrame({"vrsta": [v for v, _ in land]}, geometry=[Polygon(x) for _, x in land],
                          crs=CRS_WGS).to_crs(CRS_M)
    lg = lg[lg.is_valid & (lg.area > 0)]
    lg["m2"] = lg.area
    tp = cKDTree(np.c_[pumpe.geometry.x, pumpe.geometry.y])
    ll = cen.to_crs(CRS_WGS)

    rows = []
    for strat in ("najveci_promet", "bijela_mrlja"):
        izb, kst, kpr = izbor(strat)
        for r, (ci, a, b) in enumerate(zip(izb, kst, kpr), 1):
            c = K[ci]
            u = lg[lg.intersects(polja.geometry.iat[c])]
            hint = "; ".join(f"{v} {int(m):,} m²".replace(",", ".") for v, m in
                             u.groupby("vrsta").m2.sum().sort_values(ascending=False).items()) or "—"
            rows.append({
                "strategija": strat, "rang": r, "h3_id": polja.h3_id.iat[c], "opcina": polja.opcina.iat[c],
                "mz": polja.mz.iat[c], "cesta": f"{klasa[c]} {ime_ceste[c]}".strip(),
                "pranja_mj": round(a + b), "od_stanovnika": round(a), "od_prolaza": round(b),
                "izgradjenost": round(float(izgr[c]), 2),
                "stanovnici_5min_voznje": int(p[Tc[:, ci] <= 5].sum()),
                "stanovnici_10min_voznje": int(p[Tc[:, ci] <= 10].sum()),
                "bez_praonice_5min": int(p[(Tc[:, ci] <= 5) & ~blizu0].sum()),
                "najbliza_praonica_m": int(ts.query(cxy[c])[0]),
                "najbliza_pumpa_m": int(tp.query(cxy[c])[0]),
                "nagib_pct": float(teren.nagib_pct.iat[c]),
                "znakovi_zemljista": hint,
                "lon": round(ll.x.iat[c], 5), "lat": round(ll.y.iat[c], 5),
            })
    out = pd.DataFrame(rows)
    out.to_csv(OUT / "autopraonica_kandidati.csv", index=False)

    mn = np.full(len(polja), np.nan)
    mn[orig] = np.round(np.minimum(Ts.min(axis=1).astype(float), 99), 1)
    pd.DataFrame({"h3_id": polja.h3_id, "praonica_auto_min": mn}).to_csv(OUT / "autopraonica_pokrivenost.csv", index=False)
    P0 = Us * A / (S0 + 1e-12)[:, None]
    s.assign(pranja_mj_stanovnici=(MJ * (p @ P0)).round(), lon=s.to_crs(CRS_WGS).geometry.x.round(5),
             lat=s.to_crs(CRS_WGS).geometry.y.round(5))[["vrsta", "ime", "izvor", "A", "pranja_mj_stanovnici", "lon", "lat"]] \
        .sort_values("pranja_mj_stanovnici", ascending=False).to_csv(OUT / "autopraonica_postojece.csv", index=False)
    pd.set_option("display.width", 250)
    for st, g in out.groupby("strategija", sort=False):
        print(f"\n== {st}")
        print(g.drop(columns=["strategija", "h3_id"]).to_string(index=False))


if __name__ == "__main__":
    main()
