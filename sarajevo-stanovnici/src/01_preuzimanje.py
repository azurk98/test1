"""Korak 0: preuzimanje sirovih podataka u raw/.

Postojeće datoteke se ne preuzimaju ponovo (--force za ponovno preuzimanje).
"""
from __future__ import annotations

import argparse
import sys
import time

import requests

from common import GRAD_SARAJEVO_REL, OPCINE, RAW, DATA

import pandas as pd

OVERPASS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://maps.mail.ru/osm/tools/overpass/api/interpreter",
]

AREA = 3600000000 + GRAD_SARAJEVO_REL

UPIT_OSM = f"""
[out:json][timeout:600];
area(id:{AREA})->.grad;
(
  way["building"](area.grad);
  relation["building"](area.grad);
  node["shop"](area.grad);
  node["amenity"](area.grad);
  node["office"](area.grad);
  node["addr:housenumber"]["addr:street"](area.grad);
  way["landuse"](area.grad);
  relation["landuse"](area.grad);
  way["leisure"="park"](area.grad);
  relation["leisure"="park"](area.grad);
  way["aeroway"="aerodrome"](area.grad);
  relation["aeroway"="aerodrome"](area.grad);
);
out geom tags;
"""

WORLDPOP_DIR = ("https://data.worldpop.org/GIS/Population/Global_2015_2030/"
                "R2025A/2026/BIH/v1/100m/constrained/")
WORLDPOP_KANDIDATI = [
    "bih_pop_2026_CN_100m_R2025A_v1.tif",
    "BIH_pop_2026_CN_100m_R2025A_v1.tif",
    "bih_pop_2026_CN_100m_R2025A_v1_0.tif",
]

PDF = {
    "novi_grad_ulice_mz.pdf": "https://www.novigradsarajevo.ba/wp-content/uploads/2025/12/04.11.2025.-Lista-naziva-i-ulica-po-mjesnih-zajednicama.pdf",
    "stari_grad_strategija.pdf": "https://starigrad.ba/userfiles/file/2024/2/strategija.pdf",
    "centar_odluka_mz.pdf": "https://www.centar.ba/documents/download/86618/odluka-o-osnivanju-i-organizaciji-mjesnih-zajednica-na-podrucju-opcine-centar",
}

BBBIKE = "https://download.bbbike.org/osm/bbbike/Sarajewo/Sarajewo.osm.gz"

UA = {"User-Agent": "sarajevo-stanovnici/1.0 (procjena stanovnistva, istrazivacki skript)"}


def overpass(upit: str, cilj, force: bool) -> None:
    if cilj.exists() and not force:
        print(f"  postoji: {cilj.name}")
        return
    zadnja = None
    for url in OVERPASS:
        for pokusaj in range(3):
            try:
                print(f"  Overpass {url} (pokušaj {pokusaj + 1})")
                r = requests.post(url, data={"data": upit}, headers=UA, timeout=900)
                if r.status_code == 200 and r.content.lstrip().startswith(b"{"):
                    cilj.write_bytes(r.content)
                    print(f"  -> {cilj.name} ({len(r.content) / 1e6:.1f} MB)")
                    return
                zadnja = f"HTTP {r.status_code}: {r.text[:200]}"
            except requests.RequestException as e:
                zadnja = str(e)
            time.sleep(10 * (pokusaj + 1))
    raise RuntimeError(f"Overpass nije uspio: {zadnja}")


def preuzmi(url: str, cilj, force: bool) -> bool:
    if cilj.exists() and not force:
        print(f"  postoji: {cilj.name}")
        return True
    try:
        with requests.get(url, headers=UA, stream=True, timeout=300) as r:
            if r.status_code != 200:
                print(f"  HTTP {r.status_code}: {url}")
                return False
            tmp = cilj.with_suffix(cilj.suffix + ".part")
            with open(tmp, "wb") as f:
                for chunk in r.iter_content(1 << 20):
                    f.write(chunk)
            tmp.rename(cilj)
            print(f"  -> {cilj.name}")
            return True
    except requests.RequestException as e:
        print(f"  greška: {e}")
        return False


GHSL_URL = ("https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_BUILT_H_GLOBE_R2023A/"
            "GHS_BUILT_H_ANBH_E2018_GLOBE_R2023A_54009_100/V1-0/tiles/"
            "GHS_BUILT_H_ANBH_E2018_GLOBE_R2023A_54009_100_V1_0_R4_C20.zip")  # pločica sa Sarajevom


def ghsl(force: bool) -> bool:
    """Preuzme GHSL pločicu i izreže okvir Sarajeva u raw/ghsl_built_h.tif."""
    cilj = RAW / "ghsl_built_h.tif"
    if cilj.exists() and not force:
        print(f"  postoji: {cilj.name}")
        return True
    zp = RAW / "ghsl_tile.zip"
    if not preuzmi(GHSL_URL, zp, force):
        return False
    import zipfile

    import rasterio
    from rasterio.warp import transform_bounds
    from rasterio.windows import from_bounds
    with zipfile.ZipFile(zp) as z:
        ime = next(n for n in z.namelist() if n.endswith(".tif"))
        z.extract(ime, RAW / "ghsl_x")
    with rasterio.open(RAW / "ghsl_x" / ime) as src:
        b = transform_bounds("EPSG:4326", src.crs, 18.13, 43.72, 18.56, 44.02)
        win = from_bounds(*b, transform=src.transform).round_offsets().round_lengths()
        prof = src.profile | {"width": int(win.width), "height": int(win.height),
                              "transform": src.window_transform(win), "compress": "deflate"}
        with rasterio.open(cilj, "w", **prof) as dst:
            dst.write(src.read(window=win))
    print(f"  -> {cilj.name}")
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--bbbike", action="store_true", help="OSM iz BBBike ekstrakta umjesto Overpassa")
    a = ap.parse_args()
    greske = []

    print("OSM granice općina i MZ")
    mz = pd.read_csv(DATA / "mz_lista.csv").osm_relacija.dropna().astype(int)
    rels = sorted(set(OPCINE.values()) | {GRAD_SARAJEVO_REL} | set(mz))
    upit = f"[out:json][timeout:300];\nrel(id:{','.join(map(str, rels))});\nout geom tags;\n"
    osm_greske = []
    if not a.bbbike:
        try:
            overpass(upit, RAW / "granice.json", a.force)
        except RuntimeError as e:
            osm_greske.append(str(e))

        print("OSM zgrade, POI, landuse, parkovi, aerodrom")
        try:
            overpass(UPIT_OSM, RAW / "osm_grad.json", a.force)
        except RuntimeError as e:
            osm_greske.append(str(e))

    if osm_greske or a.bbbike:
        # Rezerva: BBBike sedmični OSM ekstrakt za Sarajevo (18.24–18.52 E, 43.77–43.94 N)
        print("Overpass nedostupan ili --bbbike: koristim BBBike ekstrakt")
        xml = RAW / "Sarajewo.osm.gz"
        if preuzmi(BBBIKE, xml, a.force):
            from osm_xml import dopuni_relacije_iz_api, konvertuj
            if a.force or not (RAW / "osm_grad.json").exists():
                info = konvertuj(xml, set(rels), RAW / "granice.json", RAW / "osm_grad.json")
                print(f"  {info}")
                # granice koje izlaze iz okvira ekstrakta: pune verzije s OSM API-ja
                dopuna = info["nedostaju_relacije"] + info["nepotpune_relacije"]
                if dopuna:
                    print(f"  dopuna relacija s api.openstreetmap.org: {dopuna}")
                    neusp = dopuni_relacije_iz_api(dopuna, RAW / "granice.json", UA)
                    if neusp:
                        greske.append(f"OSM API: relacije nisu dopunjene: {neusp}")
        else:
            greske += osm_greske

    print("WorldPop 2026")
    cilj = RAW / "worldpop_2026.tif"
    if not any(preuzmi(WORLDPOP_DIR + ime, cilj, a.force) for ime in WORLDPOP_KANDIDATI):
        greske.append(f"WorldPop: nijedan naziv nije pronađen u {WORLDPOP_DIR}; "
                      "provjeriti naziv i spremiti kao raw/worldpop_2026.tif")

    print("Overture Maps Places (dopuna trgovina)")
    ov = RAW / "overture_places.parquet"
    if ov.exists() and not a.force:
        print(f"  postoji: {ov.name}")
    else:
        import subprocess
        r = subprocess.run(["overturemaps", "download", "--bbox=18.13,43.72,18.56,44.02", "-f", "geoparquet",
                            "--type=place", "-o", str(ov)], capture_output=True, text=True)
        if r.returncode != 0 or not ov.exists():
            greske.append(f"Overture: {r.stderr[-300:]}")
        else:
            print(f"  -> {ov.name}")

    print("PDF dokumenti općina")
    for ime, url in PDF.items():
        if not preuzmi(url, RAW / ime, a.force):
            greske.append(f"{ime}: {url}")

    print("GHSL GHS-BUILT-H (prosječna visina zgrada, 100 m, 2018)")
    if not ghsl(a.force):
        greske.append(f"GHSL: {GHSL_URL}")

    if greske:
        print("\nNIJE PREUZETO:")
        for g in greske:
            print("  -", g)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
