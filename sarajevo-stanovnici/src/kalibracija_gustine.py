"""Procjena omjera gustine stanovanja kuće/blokovi (GUSTINA_NISKA u common.py).

Na MZ Novog Grada (poligoni iz koraka 04, stanovnici 2010) regresija bez
slobodnog člana i s nenegativnim koeficijentima:
    stanovnici(mz) = a · m²_blokovi(mz) + b · m²_niske(mz)
Omjer b/a je gustina m² u niskim zgradama relativno prema blokovima.
Ispisuje i grešku udjela MZ (MAPE) bez korekcije, s korekcijom i
uz izostavljanje jedne MZ (leave-one-out).
"""
import geopandas as gpd
import numpy as np
import pandas as pd
from scipy.optimize import nnls

from common import DATA, INTERIM, normaliziraj

z = gpd.read_file(INTERIM / "zgrade.gpkg")
z = z[z.opcina == "Novi Grad Sarajevo"]
mz = gpd.read_file(INTERIM / "mz_novi_grad.gpkg")
c = z.copy()
c["geometry"] = z.representative_point()
j = gpd.sjoin(c, mz[["mz", "geometry"]], predicate="within")
z["mz"] = j[~j.index.duplicated()].mz.reindex(z.index)
n10 = pd.read_csv(DATA / "mz_novi_grad_2010.csv")
n10 = n10.set_index(n10.mz_danas.map(normaliziraj)).stanovnici

for prag in (4, 5, 6):
    z["kl"] = np.where(z.spratnost >= prag, "blok", "nisko")
    V = z.pivot_table(index="mz", columns="kl", values="zapremina", aggfunc="sum", fill_value=0)
    V["st"] = [n10.get(normaliziraj(m), np.nan) for m in V.index]
    V = V.dropna()  # nove MZ (Alipašin Most III, Zabrđe) nemaju podatke iz 2010
    A, y = V[["blok", "nisko"]].to_numpy(), V.st.to_numpy()
    (a, b), _ = nnls(A, y)

    def mape(r, idx=None):
        w = V.blok + r * V.nisko
        e = np.abs(w / w.sum() - y / y.sum()) / (y / y.sum())
        return e.mean() if idx is None else e.iloc[idx]

    loo = []
    for i in range(len(V)):
        m = np.ones(len(V), bool)
        m[i] = False
        (ai, bi), _ = nnls(A[m], y[m])
        loo.append(mape(bi / max(ai, 1e-12), i))
    print(f"prag {prag} spratova: m²/st. blokovi {1 / a:.0f}, niske {1 / max(b, 1e-12):.0f}, "
          f"omjer {b / a:.2f} | MAPE udjela: bez korekcije {mape(1):.2f}, "
          f"s korekcijom {mape(b / a):.2f}, LOO {np.mean(loo):.2f}")


# ---- α (pokrenuti nakon 05_raspodjela.py): greška udjela MZ po α
p = INTERIM / "raspodjela_dijelovi.gpkg"
if p.exists():
    d = gpd.read_file(p)
    d = d[d.opcina == "Novi Grad Sarajevo"]
    g = d.groupby("mz")[["B", "P"]].sum()
    g["st"] = [n10.get(normaliziraj(m), np.nan) for m in g.index]
    g = g.dropna()
    t = g.st / g.st.sum()
    for a in (0.0, 0.3, 0.5, 0.7, 0.9, 1.0):
        w = a * g.B / g.B.sum() + (1 - a) * g.P / g.P.sum()
        s = w / w.sum()
        print(f"α = {a:.1f}: MAPE udjela MZ {np.mean(np.abs(s - t) / t):.3f}")
