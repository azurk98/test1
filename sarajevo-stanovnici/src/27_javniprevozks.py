"""Linije, stanice i redovi vožnje s portala Ministarstva saobraćaja KS (javniprevozks.ba).

Javni API portala (bez prijave): spisak linija po vrsti vozila, red vožnje po liniji (svi polasci
po smjeru i danima u sedmici) i stanice po smjeru. Preuzima se polako (1 zahtjev u sekundi) i
čuva u raw/javniprevozks/ (ne ponavlja već preuzeto). Podaci su vlasništvo Ministarstva; koriste se
za nekomercijalnu analizu, a u repozitorij idu samo izvedene tabele.

Izlaz: data/jpks_linije.csv     linija, vrsta, smjer, polazaka radnim danom, u vršnom satu (7–9 h)
       data/jpks_stanice.csv    stanica, koordinate, linije koje staju
       data/jpks_polasci_sat.csv polazaka po liniji, smjeru i satu (radni dan)
"""
from __future__ import annotations

import json
import time
from collections import defaultdict

import pandas as pd
import requests

from common import DATA, RAW

API = "https://javniprevozks.ba/api/public/lines"
VRSTA = {1: "minibus", 2: "autobus", 3: "trolejbus", 4: "tramvaj"}
UA = {"User-Agent": "sarajevo-stanovnici research (non-commercial)"}
DIR = RAW / "javniprevozks"


def preuzmi(url: str, fajl: str):
    f = DIR / fajl
    if f.exists() and f.stat().st_size > 2:
        return json.loads(f.read_text(encoding="utf-8"))
    r = requests.get(url, headers=UA, timeout=60)
    time.sleep(1.0)
    if r.status_code != 200:
        print("  !", r.status_code, url)
        return None
    f.write_text(r.text, encoding="utf-8")
    return r.json()


def main() -> None:
    DIR.mkdir(parents=True, exist_ok=True)
    linije, stanice, sat = [], {}, []
    sta_linije = defaultdict(set)
    for v, vrsta in VRSTA.items():
        lst = preuzmi(f"{API}/list?vehicleTypeIds={v}", f"lines_{v}.json") or []
        print(f"{vrsta}: {len(lst)} linija", flush=True)
        for ln in lst:
            tt = preuzmi(f"{API}/timetables/{ln['id']}/list", f"tt_{ln['id']}.json") or []
            for tl in tt:
                pol = [x for x in tl.get("timetable", []) if x.get("receives_passengers", True)]
                radni = sorted(x["start_time"] for x in pol if set(x["days_of_week"]) & {1, 2, 3, 4, 5})
                sub = [x for x in pol if 6 in x["days_of_week"]]
                ned = [x for x in pol if 7 in x["days_of_week"]]
                h = [int(t[:2]) for t in radni]
                st = preuzmi(f"{API}/terminus-line/{tl['id']}/stations-with-distance/list/0/0", f"st_{tl['id']}.json") or []
                for s in st:
                    stanice[s["id"]] = (s["name"], s["latitude"], s["longitude"])
                    sta_linije[s["id"]].add(f"{vrsta}:{ln['code']}")
                linije.append({"linija_id": ln["id"], "vrsta": vrsta, "linija": ln["code"], "naziv": ln["name"],
                               "smjer_id": tl["id"], "smjer": tl["name"], "stanica": len(st),
                               "polazaka_radni": len(radni), "polazaka_subota": len(sub), "polazaka_nedjelja": len(ned),
                               "vrsni_sat_7_9": round(sum(7 <= x < 9 for x in h) / 2, 1),
                               "prvi": radni[0][:5] if radni else "", "zadnji": radni[-1][:5] if radni else ""})
                for hh in range(24):
                    sat.append((ln["id"], tl["id"], hh, sum(x == hh for x in h)))
            print(f"  {vrsta} {ln['code']}: {len(tt)} smjerova", flush=True)
    L = pd.DataFrame(linije)
    L.to_csv(DATA / "jpks_linije.csv", index=False)
    S = pd.DataFrame([(k, n, la, lo, " ".join(sorted(sta_linije[k]))) for k, (n, la, lo) in stanice.items()],
                     columns=["stanica_id", "naziv", "lat", "lon", "linije"])
    S.to_csv(DATA / "jpks_stanice.csv", index=False)
    pd.DataFrame(sat, columns=["linija_id", "smjer_id", "sat", "polazaka"]).to_csv(DATA / "jpks_polasci_sat.csv", index=False)
    print(f"Linija {L.linija_id.nunique()}, smjerova {len(L)}, stanica {len(S)}")
    print(L.groupby("vrsta").agg(linija=("linija_id", "nunique"), polazaka_radni=("polazaka_radni", "sum")).to_string())


if __name__ == "__main__":
    main()
