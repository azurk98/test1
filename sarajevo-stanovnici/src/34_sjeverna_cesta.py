"""Idejna trasa nove ceste: Zabrđe – Sokolje – Buća Potok – Velešići – Koševsko brdo – Koševo.

Uslovi: uzdužni nagib ≤ MAX_NAGIB, što manje oštrih krivina, dozvoljeni usjeci, tuneli, mostovi i
rušenje (rušenje ima cijenu). Koncept za raspravu, ne projekat.

1. Horizontalna trasa: najjeftiniji put na mreži RES m (8 susjeda) između obaveznih tačaka.
   Cijena koraka = dužina + K_VIS · |razlika terena| (drži izohipse) + K_ZGRADA za ćeliju sa zgradom
   (rušenje) + K_STRMO · dužina na terenu strmijem od 35% (veliki zemljani radovi).
2. Izglađivanje (Chaikin) i polumjeri krivina (tri tačke na ±25 m); oštra krivina: R < R_MIN.
3. Uzdužni profil: dinamičko programiranje po stanicama na DS m: visina ceste u koracima od 0,5 m,
   promjena ≤ MAX_NAGIB · DS; cijena = usjek (m) + 1,3 · nasip (m); usjek > 15 m = tunel (fiksna
   cijena po stanici), nasip > 12 m = most (fiksna cijena). Na krajevima cesta je na terenu.
4. Bilans: dužina, tuneli, mostovi, iskop/nasip (širina 15 m), zgrade u pojasu 20 m (rušenje).
Teren: Copernicus GLO-30, tlo (grey opening), 30 m → nagib i dubine su gruba procjena.
Izlaz: out/sjeverna_cesta.geojson (dionice: cesta/usjek/nasip/tunel/most), out/sjeverna_cesta.json
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio
from rasterio.features import rasterize
from scipy.ndimage import gaussian_filter, grey_opening, map_coordinates
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import dijkstra
from shapely.geometry import LineString, Point

from common import CRS_M, CRS_WGS, INTERIM, OUT


def _uvezi(ime, fajl):
    s = importlib.util.spec_from_file_location(ime, Path(__file__).with_name(fajl))
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


TACKE = [("Zabrđe", 18.3097, 43.8741), ("Sokolje", 18.3190, 43.8690), ("Buća Potok", 18.3700, 43.8640),
         ("Velešići", 18.3990, 43.8655), ("Koševsko brdo", 18.4040, 43.8705), ("Koševo", 18.4085, 43.8720)]
RES = 20.0
K_VIS = 12.0
K_ZGRADA = 1200.0
K_STRMO = 3.0
MAX_NAGIB = 0.06
DS = 20.0
R_MIN = 80.0
UPROSTI_M = 45.0
TUNEL_M, MOST_M = 15.0, 12.0
C_TUNEL, C_MOST = 60.0, 40.0
import os
C_RUSENJE = float(os.environ.get("C_RUSENJE", 120.0))   # po stanici od 20 m koja nije u tunelu a ima zgradu u pojasu 10 m


def main() -> None:
    ter = _uvezi("ter", "10_teren.py")
    z, t = ter.dem()
    z = gaussian_filter(grey_opening(z, size=(3, 3)), 0.7)
    tk = gpd.GeoSeries([Point(lo, la) for _, lo, la in TACKE], crs=CRS_WGS).to_crs(CRS_M)
    x0, y0 = tk.x.min() - 1500, tk.y.min() - 1500
    x1, y1 = tk.x.max() + 1500, tk.y.max() + 1500
    nx, ny = int((x1 - x0) / RES), int((y1 - y0) / RES)
    gx = x0 + (np.arange(nx) + 0.5) * RES
    gy = y1 - (np.arange(ny) + 0.5) * RES
    XX, YY = np.meshgrid(gx, gy)
    ll = gpd.GeoSeries(gpd.points_from_xy(XX.ravel(), YY.ravel()), crs=CRS_M).to_crs(CRS_WGS)
    col = (ll.x.to_numpy() - t.c) / t.a - 0.5
    row = (ll.y.to_numpy() - t.f) / t.e - 0.5
    H = map_coordinates(z, [row, col], order=1).reshape(ny, nx)

    zg = gpd.read_file(INTERIM / "zgrade.gpkg", columns=["geometry"]).to_crs(CRS_M)
    from rasterio.transform import from_origin
    tr = from_origin(x0, y1, RES, RES)
    zgr = rasterize(((g, 1) for g in zg.geometry), out_shape=(ny, nx), transform=tr, fill=0, all_touched=False).astype(bool)
    nag_t = np.hypot(*np.gradient(H, RES))

    # graf mreže
    idx = np.arange(nx * ny).reshape(ny, nx)
    rows, cols, w = [], [], []
    for dy, dx in ((0, 1), (1, 0), (1, 1), (1, -1)):
        a = idx[0:ny - dy, max(0, -dx):nx - max(0, dx)]
        b = idx[dy:ny, max(0, dx):nx - max(0, -dx)]
        L = RES * np.hypot(dx, dy)
        ha, hb = H.ravel()[a.ravel()], H.ravel()[b.ravel()]
        c = (L + K_VIS * np.abs(ha - hb) + K_ZGRADA * (zgr.ravel()[b.ravel()] | zgr.ravel()[a.ravel()])
             + K_STRMO * L * ((nag_t.ravel()[a.ravel()] > 0.35) | (nag_t.ravel()[b.ravel()] > 0.35)))
        rows += [a.ravel(), b.ravel()]; cols += [b.ravel(), a.ravel()]; w += [c, c]
    G = coo_matrix((np.concatenate(w), (np.concatenate(rows), np.concatenate(cols))), shape=(nx * ny, nx * ny)).tocsr()

    def celija(p):
        return int(np.clip(round((y1 - p.y) / RES - 0.5), 0, ny - 1)) * nx + int(np.clip(round((p.x - x0) / RES - 0.5), 0, nx - 1))

    put = []
    for a_, b_ in zip(tk[:-1], tk[1:]):
        s, e = celija(a_), celija(b_)
        _, P = dijkstra(G, indices=[s], return_predecessors=True)
        seg = [e]
        while seg[-1] != s:
            seg.append(P[0, seg[-1]])
        put += seg[::-1] if not put else seg[::-1][1:]
    pts = np.c_[XX.ravel()[put], YY.ravel()[put]]
    # pojednostavljenje (zadrži glavne prelome, tolerancija UPROSTI_M), pa izglađivanje (Chaikin, 6 prolaza)
    pts = np.array(LineString(pts).simplify(UPROSTI_M).coords)
    for _ in range(6):
        q = 0.75 * pts[:-1] + 0.25 * pts[1:]
        r = 0.25 * pts[:-1] + 0.75 * pts[1:]
        pts = np.vstack([pts[:1], np.column_stack([q, r]).reshape(-1, 2), pts[-1:]])
    g = LineString(pts)
    L = g.length
    st = np.arange(0, L, DS)
    sp = np.array([[g.interpolate(x).x, g.interpolate(x).y] for x in st])
    sll = gpd.GeoSeries(gpd.points_from_xy(sp[:, 0], sp[:, 1]), crs=CRS_M).to_crs(CRS_WGS)
    hz = map_coordinates(z, [(sll.y.to_numpy() - t.f) / t.e - 0.5, (sll.x.to_numpy() - t.c) / t.a - 0.5], order=1)

    # polumjeri krivina (±25 m)
    k = int(25 / DS) or 1
    R = np.full(len(st), np.inf)
    for i in range(k, len(st) - k):
        a, b, c = sp[i - k], sp[i], sp[i + k]
        ab, bc, ca = np.linalg.norm(b - a), np.linalg.norm(c - b), np.linalg.norm(a - c)
        cr = abs((b - a)[0] * (c - a)[1] - (b - a)[1] * (c - a)[0])
        if cr > 1e-6:
            R[i] = ab * bc * ca / (2 * cr)
    ostre = R < R_MIN

    # zgrade uz stanicu (pojas 10 m): prolaz na terenu, u usjeku ili nasipu znači rušenje -> cijena,
    # pa profil radije ide tunelom ispod izgrađenog dijela
    sp_g = gpd.GeoSeries(gpd.points_from_xy(sp[:, 0], sp[:, 1]), crs=CRS_M)
    zg_si = zg.sindex
    ima_zgr = np.array([len(zg_si.query(p.buffer(10), predicate="intersects")) > 0 for p in sp_g])
    # uzdužni profil (DP)
    zmin, zmax = hz.min() - 40, hz.max() + 40
    Zs = np.arange(zmin, zmax, 0.5)
    korak = int(np.floor(MAX_NAGIB * DS / 0.5))

    def cijena(zr, zt):
        d = zt - zr
        usjek, nasip = np.clip(d, 0, None), np.clip(-d, 0, None)
        c = np.where(usjek > TUNEL_M, C_TUNEL, usjek) + np.where(nasip > MOST_M, C_MOST, 1.3 * nasip)
        return c

    INF = 1e18
    cost = np.full(len(Zs), INF)
    cost[np.argmin(np.abs(Zs - hz[0]))] = 0
    back = np.zeros((len(st), len(Zs)), np.int32)
    for i in range(1, len(st)):
        best = np.full(len(Zs), INF); arg = np.zeros(len(Zs), np.int32)
        for d in range(-korak, korak + 1):
            sh = np.roll(cost, d)
            if d > 0:
                sh[:d] = INF
            elif d < 0:
                sh[d:] = INF
            better = sh < best
            best[better] = sh[better]; arg[better] = (np.arange(len(Zs)) - d)[better]
        cost = best + cijena(Zs, hz[i]) + (np.where(hz[i] - Zs > TUNEL_M, 0.0, C_RUSENJE) if ima_zgr[i] else 0.0)
        back[i] = arg
    kraj = np.argmin(cost + 5 * np.abs(Zs - hz[-1]))
    prof = np.zeros(len(st), int); prof[-1] = kraj
    for i in range(len(st) - 1, 0, -1):
        prof[i - 1] = back[i, prof[i]]
    zr = Zs[prof]
    d = hz - zr
    vrsta = np.where(d > TUNEL_M, "tunel", np.where(-d > MOST_M, "most", np.where(d > 3, "usjek", np.where(-d > 3, "nasip", "teren"))))
    nag = np.abs(np.diff(zr)) / DS

    # zgrade u pojasu 20 m (osim u tunelu)
    traka = gpd.GeoSeries([LineString(sp[i:i + 2]) for i in range(len(sp) - 1)], crs=CRS_M)
    van_tunela = traka[vrsta[:-1] != "tunel"].buffer(10).union_all()
    rusenje = zg[zg.intersects(van_tunela)]

    def duz(v):
        return float((vrsta[:-1] == v).sum() * DS / 1000)
    out = {"duzina_km": round(L / 1000, 2), "max_nagib_pct": round(float(nag.max() * 100), 1),
           "tunel_km": round(duz("tunel"), 2), "most_km": round(duz("most"), 2), "usjek_km": round(duz("usjek"), 2),
           "nasip_km": round(duz("nasip"), 2), "na_terenu_km": round(duz("teren"), 2),
           "iskop_m3": round(float((np.clip(d, 0, TUNEL_M)[d <= TUNEL_M]).sum() * DS * 15)),
           "nasip_m3": round(float((np.clip(-d, 0, MOST_M)[-d <= MOST_M]).sum() * DS * 15)),
           "zgrada_za_rusenje": int(len(rusenje)), "otisak_rusenja_m2": round(float(rusenje.area.sum())),
           "ostrih_krivina_R<80m": int(np.sum(np.diff(ostre.astype(int)) == 1)),
           "min_radijus_m": round(float(R[np.isfinite(R)].min())) if np.isfinite(R).any() else None,
           "tacke": [n for n, _, _ in TACKE]}
    # priključci: stanice najbliže obaveznim tačkama, dužina između njih po trasi
    st_tacke = [int(np.argmin(np.hypot(*(sp - np.array([p.x, p.y])).T))) for p in tk]
    out["prikljucci"] = [{"naziv": n, "lon": lo, "lat": la, "km": round(float(st[i] / 1000), 2)} for (n, lo, la), i in zip(TACKE, st_tacke)]
    json.dump(out, open(OUT / "sjeverna_cesta.json", "w"), ensure_ascii=False, indent=1)
    # dionice po vrsti
    rows = []
    i = 0
    while i < len(sp) - 1:
        j = i
        while j < len(sp) - 1 and vrsta[j] == vrsta[i]:
            j += 1
        rows.append({"vrsta": vrsta[i], "od_km": round(st[i] / 1000, 2), "duzina_m": round((j - i) * DS),
                     "geometry": LineString(sp[i:j + 1])})
        i = j
    gpd.GeoDataFrame(rows, crs=CRS_M).to_crs(CRS_WGS).to_file(OUT / "sjeverna_cesta.geojson", driver="GeoJSON",
                                                             COORDINATE_PRECISION=5)
    rusenje.assign(geometry=rusenje.representative_point()).to_crs(CRS_WGS)[["geometry"]].to_file(
        OUT / "sjeverna_cesta_rusenje.geojson", driver="GeoJSON", COORDINATE_PRECISION=5)
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
