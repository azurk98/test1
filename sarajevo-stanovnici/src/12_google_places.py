"""Trgovine namirnica iz Google Places API (New) -> raw/google_places.json

Pokretanje:
    export GOOGLE_MAPS_API_KEY=...        (u postavkama okruženja, ne u kodu)
    python 12_google_places.py --koliko   procjena broja zahtjeva, bez poziva API-ja
    python 12_google_places.py            prikupljanje
    python 09_supermarket.py              model s Google trgovinama

Pretraga: Nearby Search (New) u krugovima oko H3 polja rezolucije 8 (~0,74 km²)
koja pokrivaju naseljena polja. Google vraća najviše 20 mjesta po zahtjevu; kad
vrati 20, krug se dijeli na 7 polja rezolucije 9 i pretražuje ponovo.

Uslovi Google Maps Platform (provjeriti aktuelnu verziju):
- place_id se smije čuvati trajno; koordinate najduže 30 dana, zato se uz
  podatke čuva datum preuzimanja i 09_supermarket.py ih ne koristi nakon 30 dana;
- Places sadržaj se ne smije prikazivati na karti koja nije Google karta, zato se
  Google trgovine ne crtaju na karti, nego samo ulaze u model.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import time

import geopandas as gpd
import h3
import requests

from common import OUT, RAW

URL = "https://places.googleapis.com/v1/places:searchNearby"
TIPOVI = ["supermarket", "grocery_store", "convenience_store", "market", "food_store"]
POLJA = "places.id,places.displayName,places.location,places.types,places.primaryType,places.businessStatus"
RADIJUS = {8: 560.0, 9: 215.0, 10: 85.0}
CILJ = RAW / "google_places.json"


def polazna_polja() -> list[str]:
    p = gpd.read_file(OUT / "polja_h3.gpkg")
    nas = p[p.stanovnici > 0].h3_id
    return sorted({h3.cell_to_parent(h, 8) for h in nas})


def trazi(kljuc: str, cell: str, tipovi: list[str]) -> list[dict]:
    lat, lng = h3.cell_to_latlng(cell)
    body = {"includedTypes": tipovi, "maxResultCount": 20, "rankPreference": "DISTANCE",
            "locationRestriction": {"circle": {"center": {"latitude": lat, "longitude": lng},
                                               "radius": RADIJUS[h3.get_resolution(cell)]}}}
    for pokusaj in range(4):
        r = requests.post(URL, json=body, timeout=30,
                          headers={"X-Goog-Api-Key": kljuc, "X-Goog-FieldMask": POLJA})
        if r.status_code == 200:
            return r.json().get("places", [])
        if r.status_code in (429, 500, 503):
            time.sleep(2 ** pokusaj)
            continue
        raise RuntimeError(f"HTTP {r.status_code}: {r.text[:400]}")
    raise RuntimeError("Places API ne odgovara (429/5xx)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--koliko", action="store_true", help="samo procjena broja zahtjeva")
    a = ap.parse_args()
    start = polazna_polja()
    if a.koliko:
        print(f"Polaznih krugova (H3 res 8): {len(start)}; uz dijeljenje gustih tipično "
              f"{len(start)}–{len(start) * 3} zahtjeva.")
        return 0
    kljuc = os.environ.get("GOOGLE_MAPS_API_KEY")
    if not kljuc:
        print("Nema GOOGLE_MAPS_API_KEY u okruženju.")
        return 1

    tipovi = list(TIPOVI)
    mjesta, red, n = {}, list(start), 0
    while red:
        cell = red.pop()
        try:
            res = trazi(kljuc, cell, tipovi)
        except RuntimeError as e:
            if "includedTypes" in str(e) or "Unsupported types" in str(e):
                # nepoznat tip u ovoj verziji API-ja: izbaci ga i pokušaj ponovo
                for t in list(tipovi):
                    if t in str(e) and t not in ("supermarket", "grocery_store"):
                        tipovi.remove(t)
                red.append(cell)
                continue
            print(e)
            return 1
        n += 1
        for p in res:
            mjesta[p["id"]] = {"place_id": p["id"], "ime": p.get("displayName", {}).get("text", ""),
                               "lat": p["location"]["latitude"], "lon": p["location"]["longitude"],
                               "tip": p.get("primaryType", ""), "tipovi": p.get("types", []),
                               "status": p.get("businessStatus", "")}
        if len(res) >= 20 and h3.get_resolution(cell) < 10:
            red.extend(h3.cell_to_children(cell, h3.get_resolution(cell) + 1))
        if n % 50 == 0:
            print(f"  {n} zahtjeva, {len(mjesta)} mjesta, u redu {len(red)}")
    CILJ.write_text(json.dumps({"preuzeto": dt.date.today().isoformat(), "tipovi": tipovi,
                                "zahtjeva": n, "mjesta": list(mjesta.values())}, ensure_ascii=False))
    print(f"-> {CILJ.name}: {len(mjesta)} mjesta iz {n} zahtjeva (tipovi: {tipovi})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
