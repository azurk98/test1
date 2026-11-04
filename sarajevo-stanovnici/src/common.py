"""Zajedničke postavke i pomoćne funkcije za sve korake."""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
from shapely.geometry import LineString, MultiPolygon, Point, Polygon
from shapely.ops import polygonize, unary_union

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RAW = ROOT / "raw"
INTERIM = ROOT / "interim"
OUT = ROOT / "out"
for _d in (RAW, INTERIM, OUT):
    _d.mkdir(exist_ok=True)

CRS_WGS = "EPSG:4326"
CRS_M = "EPSG:32634"  # UTM 34N, metri (Sarajevo ~18.4°E)

H3_RES = 9

# OSM relacije općina (naziv kao u data/opcine_procjena_2026.csv)
OPCINE = {
    "Stari Grad Sarajevo": 2528243,
    "Centar Sarajevo": 2528180,
    "Novo Sarajevo": 2528239,
    "Novi Grad Sarajevo": 2528240,
}
GRAD_SARAJEVO_REL = 2567380

# Parametri modela
ALFA = 0.7
ALFE_SCENARIJI = (0.5, 0.7, 0.9)
SPRAT_POMAK_SCENARIJI = (-1, 0, 1)
BETA_NOVI_GRAD = 0.5
MIN_POVRSINA_ZGRADE = 25.0
VELIKA_ZGRADA = 2000.0
# Dio polja je "C" (nedostaju zgrade) ako WorldPop u njemu ima bar ovoliko
# stanovnika a stambena zapremina je 0.
C_PRAG_WORLDPOP = 5.0

# Novi Grad: iz kojih su MZ izdvojene nove MZ. Popuniti tek kad se utvrdi
# (odluka općine ili poređenje spiska ulica). Prazno = pravilo za nepoznatu
# matičnu MZ iz SPEC 5.2.
MATICNE_MZ_NOVI_GRAD: dict[str, str] = {
    # "Alipašin Most III": "?",
    # "Zabrđe": "?",
}

PODRAZUMIJEVANA_SPRATNOST = {
    "house": 2, "detached": 2, "semidetached_house": 2, "terrace": 2,
    "residential": 4, "apartments": 6, "yes": 3,
}
STAMBENE = {"house", "detached", "semidetached_house", "terrace", "apartments",
            "residential", "bungalow", "farm"}
NESTAMBENE = {
    "commercial", "retail", "office", "industrial", "warehouse", "school",
    "kindergarten", "university", "college", "hospital", "church", "mosque",
    "chapel", "religious", "public", "civic", "government", "train_station",
    "transportation", "garage", "garages", "carport", "shed", "hut", "roof",
    "service", "sports_hall", "stadium", "hotel", "kiosk", "greenhouse",
    "construction", "ruins",
}


# ---------------------------------------------------------------- nazivi

def normaliziraj(s: str | None) -> str:
    """Naziv bez dijakritika, malim slovima, bez interpunkcije."""
    if s is None or (isinstance(s, float) and np.isnan(s)):
        return ""
    s = str(s).lower().replace("đ", "dj")
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.replace("ali-pas", "alipas").replace("ali pas", "alipas")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def normaliziraj_ulicu(s: str | None) -> str:
    s = normaliziraj(s)
    zamjene = {
        r"\bul\b": "", r"\bulica\b": "", r"\bcikma\b": "cikma",
        r"\bcik\b": "cikma", r"\bbr\b": "", r"\bbb\b": "",
        r"\bn h\b": "naselje heroja", r"\bnh\b": "naselje heroja",
        r"\bdr\b": "doktora", r"\bprof\b": "profesora",
    }
    for k, v in zamjene.items():
        s = re.sub(k, v, s)
    # rimski/arapski brojevi u "I cikma", "1. cikma"
    s = re.sub(r"\b(\d+)\s*cikma", r"\1 cikma", s)
    return re.sub(r"\s+", " ", s).strip()


def kucni_broj(s) -> int | None:
    if s is None or (isinstance(s, float) and np.isnan(s)):
        return None
    m = re.match(r"\s*(\d+)", str(s))
    return int(m.group(1)) if m else None


# ---------------------------------------------------------------- OSM

def _way_geom(el: dict):
    pts = [(p["lon"], p["lat"]) for p in el.get("geometry", []) if p]
    if len(pts) < 2:
        return None
    if len(pts) >= 4 and pts[0] == pts[-1]:
        return Polygon(pts)
    return LineString(pts)


def _rel_geom(el: dict):
    outer, inner = [], []
    for m in el.get("members", []):
        if m.get("type") != "way" or not m.get("geometry"):
            continue
        pts = [(p["lon"], p["lat"]) for p in m["geometry"] if p]
        if len(pts) < 2:
            continue
        (inner if m.get("role") == "inner" else outer).append(LineString(pts))
    if not outer:
        return None
    outer_polys = list(polygonize(unary_union(outer)))
    if not outer_polys:
        return None
    geom = unary_union(outer_polys)
    if inner:
        holes = list(polygonize(unary_union(inner)))
        if holes:
            geom = geom.difference(unary_union(holes))
    return geom if not geom.is_empty else None


def overpass_u_gdf(path: Path) -> gpd.GeoDataFrame:
    """Overpass JSON (`out geom tags`) -> GeoDataFrame s kolonama tagova."""
    with open(path, encoding="utf-8") as f:
        els = json.load(f)["elements"]
    rows = []
    for el in els:
        if el["type"] == "node":
            geom = Point(el["lon"], el["lat"])
        elif el["type"] == "way":
            geom = _way_geom(el)
        else:
            geom = _rel_geom(el)
        if geom is None:
            continue
        row = dict(el.get("tags", {}))
        row["osm_type"], row["osm_id"], row["geometry"] = el["type"], el["id"], geom
        rows.append(row)
    if not rows:
        return gpd.GeoDataFrame({"osm_type": [], "osm_id": []}, geometry=[], crs=CRS_WGS)
    return gpd.GeoDataFrame(rows, geometry="geometry", crs=CRS_WGS)


def poligoni(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    return gdf[gdf.geom_type.isin(["Polygon", "MultiPolygon"])].copy()


def ucitaj_granice() -> tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
    """Vraća (općine, MZ iz OSM-a) u metričkom CRS-u."""
    g = poligoni(overpass_u_gdf(RAW / "granice.json")).to_crs(CRS_M)
    rel2op = {v: k for k, v in OPCINE.items()}
    op = g[g.osm_id.isin(rel2op)].copy()
    op["opcina"] = op.osm_id.map(rel2op)
    op = op[["opcina", "geometry"]].reset_index(drop=True)

    mzl = pd.read_csv(DATA / "mz_lista.csv").dropna(subset=["osm_relacija"])
    mzl["osm_relacija"] = mzl.osm_relacija.astype(int)
    mz = g.merge(mzl[["opcina", "mz", "osm_relacija"]], left_on="osm_id",
                 right_on="osm_relacija")
    mz = gpd.GeoDataFrame(mz[["opcina", "mz", "geometry"]], crs=CRS_M)
    return op, mz


def opcine_ukupno() -> pd.DataFrame:
    df = pd.read_csv(DATA / "opcine_procjena_2026.csv")
    return df[df.opcina.isin(OPCINE)].set_index("opcina")


# ---------------------------------------------------------------- MZ pokrivanje

def popuni_mz(opcina_geom, mz: gpd.GeoDataFrame, popuni_rupe: bool) -> gpd.GeoDataFrame:
    """Odreže MZ poligone na općinu i ukloni preklapanja. Ako je popuni_rupe,
    dijelove općine bez MZ pripoji MZ s najdužom zajedničkom granicom
    (ili najbližoj)."""
    out, zauzeto = [], None
    for _, r in mz.iterrows():
        g = r.geometry.intersection(opcina_geom)
        if zauzeto is not None:
            g = g.difference(zauzeto)
        if g.is_empty:
            continue
        zauzeto = g if zauzeto is None else zauzeto.union(g)
        out.append({"mz": r.mz, "geometry": g})
    res = gpd.GeoDataFrame(out, geometry="geometry", crs=mz.crs)
    if not popuni_rupe or res.empty:
        return res
    rupe = opcina_geom.difference(unary_union(res.geometry))
    dijelovi = [] if rupe.is_empty else list(getattr(rupe, "geoms", [rupe]))
    for d in dijelovi:
        if d.area < 1:
            continue
        granica = res.geometry.boundary.intersection(d.boundary).length
        i = granica.idxmax() if granica.max() > 0 else res.distance(d).idxmin()
        res.at[i, "geometry"] = res.at[i, "geometry"].union(d)
    return res


# ---------------------------------------------------------------- zaokruživanje

def najveci_ostatak(vrijednosti: np.ndarray, ukupno: int) -> np.ndarray:
    """Cjelobrojna raspodjela koja tačno daje `ukupno` (metoda najvećeg ostatka)."""
    v = np.asarray(vrijednosti, dtype=float)
    if v.sum() <= 0:
        out = np.zeros(len(v), dtype=int)
        if len(v):
            out[0] = ukupno
        return out
    x = v / v.sum() * ukupno
    base = np.floor(x).astype(int)
    ost = ukupno - base.sum()
    if ost > 0:
        base[np.argsort(-(x - base), kind="stable")[:ost]] += 1
    return base


# ---------------------------------------------------------------- WorldPop

def worldpop_po_dijelu(dijelovi: gpd.GeoDataFrame, tif: Path | None = None) -> np.ndarray:
    """Zbir WorldPop piksela po dijelu polja; piksel se dijeli po površini presjeka."""
    import rasterio
    from rasterio.windows import from_bounds
    from shapely.geometry import box

    tif = tif or RAW / "worldpop_2026.tif"
    if not tif.exists():
        print(f"UPOZORENJE: nema {tif.name}; WorldPop = 0 (ostaju samo zgrade)")
        return np.zeros(len(dijelovi))
    with rasterio.open(tif) as src:
        d = dijelovi.to_crs(src.crs)
        win = from_bounds(*d.total_bounds, transform=src.transform).round_offsets().round_lengths()
        arr = src.read(1, window=win, boundless=True, fill_value=0).astype(float)
        if src.nodata is not None:
            arr[arr == src.nodata] = 0
        arr[~np.isfinite(arr) | (arr < 0)] = 0
        t = src.window_transform(win)
    rr, cc = np.nonzero(arr > 0)
    if len(rr) == 0:
        return np.zeros(len(dijelovi))
    x0, y0 = t * (cc, rr)
    x1, y1 = t * (cc + 1, rr + 1)
    pix = gpd.GeoDataFrame({"v": arr[rr, cc]},
                           geometry=[box(a, b, c, e) for a, b, c, e in zip(x0, y1, x1, y0)],
                           crs=d.crs).to_crs(CRS_M)
    pix["pa"] = pix.area
    dm = dijelovi[["geometry"]].copy()
    dm["_i"] = np.arange(len(dm))
    ov = gpd.overlay(pix, dm, how="intersection", keep_geom_type=True)
    ov["w"] = ov.v * ov.area / ov.pa
    return ov.groupby("_i").w.sum().reindex(range(len(dm)), fill_value=0).to_numpy()
