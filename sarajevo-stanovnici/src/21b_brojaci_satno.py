"""Satni profil (prosječni satni saobraćaj u danu, kriva UKUPNI, grafik 2) za svaki brojač iz
publikacije brojanja KS 2025. Grafikoni su vektorski: oblik se čita iz tačaka krive (visina iznad
nule), a razmjer tako da je zbir 24 sata jednak PGDS-u brojača.

Pokretanje: python 21b_brojaci_satno.py ../raw/saobracaj/publikacija-2025.pdf \
                ../data/brojaci_2025.csv ../data/brojaci_2025_satno.csv
Sat 0 = 00:00–01:00 (na grafikonu oznaka 01:00).
"""
import re, sys
import numpy as np, pandas as pd, pdfplumber
UK = (0.357, 0.608, 0.835)
pgds = pd.read_csv(sys.argv[2]).set_index("brojac").pgds_2025
rows = []
with pdfplumber.open(sys.argv[1]) as p:
    for i in range(110, 226):
        pg = p.pages[i]
        t = pg.extract_text() or ""
        m = re.search(r"Identifikaciona oznaka brojača\s+(KSBS\w+)", t)
        if not m:
            continue
        k = m[1]
        cur = [c for c in pg.curves if len(c["pts"]) == 24 and isinstance(c.get("stroking_color"), (tuple, list))
               and len(c["stroking_color"]) == 3 and np.allclose(c["stroking_color"], UK, atol=0.02)]
        if not cur:
            print("nema krive", k, file=sys.stderr); continue
        c = min(cur, key=lambda c: c["top"])
        pts = sorted(c["pts"])
        xmin = pts[0][0]
        ws = pg.extract_words()
        nule = [w for w in ws if w["text"] == "0" and w["x1"] < xmin + 2 and c["top"] - 5 < w["top"] < c["bottom"] + 25]
        if not nule:
            print("nema nule", k, file=sys.stderr); continue
        z = max(nule, key=lambda w: w["top"])
        y0 = (z["top"] + z["bottom"]) / 2
        h = np.clip(y0 - np.array([pt[1] for pt in pts]), 0, None)
        if h.sum() <= 0 or k not in pgds:
            print("prazno", k, file=sys.stderr); continue
        val = h / h.sum() * pgds[k]
        for s, x in enumerate(val):
            rows.append((k, s, round(float(x), 1)))
        print(k, f"str. {i+1}: vrh {int(val.argmax())}h, udio vršnog sata {h.max()/h.sum():.3f}", file=sys.stderr)
pd.DataFrame(rows, columns=["brojac", "sat", "vozila_sat"]).to_csv(sys.argv[3], index=False)
