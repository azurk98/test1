"""Brojači saobraćaja Direkcije za puteve KS, 2025 (publikacija Ministarstva saobraćaja KS, maj 2026).

Preuzimanje: https://ms.ks.gov.ba/sites/ms.ks.gov.ba/files/2026-05/11-publikacija-2025-final.pdf
             -> raw/saobracaj/publikacija-2025.pdf
Pokretanje:  python 21_brojaci_saobracaja.py ../raw/saobracaj/publikacija-2025.pdf \
                 ../data/brojaci_2025.csv ../data/brojaci_2025_dnevno.csv
Izlaz: lokacije i PGDS 2025 po brojaču; broj vozila po danu (oba smjera) za 2025.
Napomena: kod KSBS04/05, KSBS08/11 i KSBS26/29a publikacija ponavlja iste koordinate
(greška u izvoru); KSBS22 nema opisnu stranu pa ni koordinate. Nazivi i KSBS22 dopunjeni
su ručno iz tabele 5.
"""
import re, sys, calendar
import pdfplumber, pandas as pd
pdf = sys.argv[1]
info, dani = {}, []
DM = [31,28,31,30,31,30,31,31,30,31,30,31]
def dms(s):
    m = re.search(r"(\d+)\s*°?\s*(\d+)\s*'\s*([\d.,]+)", s)
    return None if not m else int(m[1]) + int(m[2])/60 + float(m[3].replace(',', '.'))/3600
with pdfplumber.open(pdf) as p:
    for i, pg in enumerate(p.pages[44:110]):
        t = pg.extract_text() or ""
        m = re.search(r"Tabela \d+\. Brojač (KSBS\w+)", t)
        if m and "Koordinate" in t:
            k = m[1]
            mx = re.search(r"\bX\s+(\d+)\D{1,3}(\d+)\D{1,3}([\d.,]+)", t)
            my = re.search(r"\bY\s+(\d+)\D{1,3}(\d+)\D{1,3}([\d.,]+)", t)
            f_ = lambda m: int(m[1]) + int(m[2]) / 60 + float(m[3].rstrip('.,').replace(',', '.')) / 3600
            lat = f_(mx) if mx else None
            lon = f_(my) if my else None
            pg_ = re.search(r"PGDS\s+([\d.]+)", t)
            naziv = re.search(r"Naziv lokacije i općine\s+([^\n]+)", t)
            info[k] = {"brojac": k, "lat": lat, "lon": lon,
                       "pgds_2025": int(pg_[1].replace('.', '')) if pg_ else None,
                       "lokacija": naziv[1].strip() if naziv else ""}
        m = re.search(r"Brojanje vozila po danima u mjesecu \(2025\.\) - Brojač (KSBS\w+)", t)
        if m:
            k = m[1]
            for line in t.split("\n"):
                tok = line.split()
                if not tok or not tok[0].isdigit() or not 1 <= int(tok[0]) <= 31:
                    continue
                d, vals = int(tok[0]), tok[1:]
                if not all(v == "/" or v.isdigit() for v in vals) or not vals:
                    continue
                if len(vals) == 12:
                    mjeseci = range(12)
                else:
                    mjeseci = [j for j in range(12) if DM[j] >= d]
                    if len(mjeseci) != len(vals):
                        print("preskočeno", k, d, len(vals), file=sys.stderr); continue
                for j, v in zip(mjeseci, vals):
                    if v != "/" and DM[j] >= d:
                        dani.append((k, f"2025-{j+1:02d}-{d:02d}", int(v)))
i = pd.DataFrame(info.values())
i["lat"], i["lon"] = i.lat.round(5), i.lon.round(5)
dup = i.duplicated(subset=["lat", "lon"], keep=False)
i["koordinate"] = pd.Series(["ponovljene u izvoru (vjerovatno greška)" if x else "iz publikacije" for x in dup])
d = pd.DataFrame(dani, columns=["brojac", "datum", "vozila"])
i.to_csv(sys.argv[2], index=False); d.to_csv(sys.argv[3], index=False)
print(i.to_string()); print(d.groupby("brojac").size().to_string())
