"""MZ poligoni za Centar iz Odluke o osnivanju i organizaciji MZ (2022).

Ulaz:  raw/centar_odluka_mz.pdf (Službene novine KS, 04.08.2022: ulice i rasponi kućnih brojeva za
       svih 19 MZ), interim/zgrade.gpkg, interim/dijelovi.gpkg (iz 04), raw/granice.json
Izlaz: interim/centar_ulice_mz.csv  pravila (mz, ulica, od, do, paritet) izvučena iz Odluke
       interim/mz_centar.gpkg        MZ poligoni
       interim/dijelovi.gpkg         dijelovi polja s MZ i za Centar

Postupak kao za Novi Grad (04_mz_novi_grad.py): zgrada s adresom po rasponu, zgrada bez adrese po
najbližoj imenovanoj ulici (ako cijela ulica pripada jednoj MZ), ostale glasanjem susjeda; MZ
poligoni su Voronoi oko zgrada, odrezani granicom općine. Odluka je u dva stupca, pa se čita
stupac po stupac.
"""
from __future__ import annotations

import importlib.util
import re
import unicodedata
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
import shapely

from common import CRS_M, DATA, INTERIM, RAW, popuni_mz, ucitaj_granice, worldpop_po_dijelu

_s = importlib.util.spec_from_file_location("ng", Path(__file__).with_name("04_mz_novi_grad.py"))
ng = importlib.util.module_from_spec(_s)
_s.loader.exec_module(ng)

OPCINA = "Centar Sarajevo"


def tekst_odluke(pdf_path) -> str:
    import pdfplumber
    dijelovi = []
    with pdfplumber.open(pdf_path) as pdf:
        for p in pdf.pages:
            for x0, x1 in ((0, p.width / 2), (p.width / 2, p.width)):
                dijelovi.append(p.crop((x0, 0, x1, p.height)).extract_text() or "")
    t = "\n".join(dijelovi).replace("Ĉ", "Č").replace("ĉ", "č")
    t = "\n".join(l for l in t.split("\n") if not re.fullmatch(
        r"\s*(\d{1,3}|Broj|Službene novine Kantona Sarajevo|Godina XXVII|Četvrtak, 04\. augusta 2022\. godine)\s*", l))
    t = re.sub(r"Četvrtak, 4\. 8\. 2022\.\s*\d*\s*", "", t)
    t = re.sub(r"-\n", "-", t)
    return re.sub(r"\s+", " ", t)


def kljuc(s: str) -> str:
    s = unicodedata.normalize("NFKD", s.lower().replace("đ", "dj"))
    return re.sub(r"[^a-z0-9]", "", "".join(c for c in s if not unicodedata.combining(c)))


IME = re.compile(r"(?:(?<=: )|(?<=, )|(?<= i ))([A-ZČĆŽŠĐ][\wČĆŽŠĐčćžšđ.'\- ]*?)\s+(?=(?:od|broj|br\.|do)\b)")
RASPON = re.compile(r"(?:od(?: broja)? )?(\d+)\s*[a-zA-Z]?\s*do(?: broja)? (\d+)")
JEDAN = re.compile(r"\bbroj (\d+)")


def pravila_iz_odluke(t: str, nazivi: list[str]) -> pd.DataFrame:
    po_kljucu = {kljuc(n): n for n in nazivi}
    bl = list(re.finditer(r"Mjesn\w+ zajednic\w+\s*[„\"“]([^\"”“]+)[”\"“]", t))
    clanovi = []
    for i, m in enumerate(bl):
        mz = po_kljucu.get(kljuc(m.group(1)))
        if mz is None or mz in [c[0] for c in clanovi]:
            continue
        kraj = bl[i + 1].start() if i + 1 < len(bl) else len(t)
        clanovi.append((mz, t[m.end():kraj]))
    rows = []
    for mz, blok in clanovi:
        blok = re.sub(r"Član \d+\.", " ", blok)
        blok = re.sub(r"[a-z]\) Mjesno područje [„\"“][^\"”“]+[”\"“], obuhvata sl[ij]edeće ulice:", " ulice:", blok)
        dio = blok[blok.find("ulice:"):] if "ulice:" in blok else blok
        dio = re.sub(r"\s+", " ", dio)
        imena = list(IME.finditer(dio))
        for k, im in enumerate(imena):
            spec = dio[im.end():imena[k + 1].start() if k + 1 < len(imena) else len(dio)]
            spec = re.split(r"izuzev", spec)[0]
            ulica = im.group(1).strip(" -")
            if len(ulica) < 3 or ulica.lower().startswith(("sjedište", "mjesna", "ulice")):
                continue
            nasao = False
            for a, b in RASPON.findall(spec):
                a, b = int(a), int(b)
                rows.append((mz, ulica, min(a, b), max(a, b), "neparni" if a % 2 else "parni"))
                nasao = True
            rest = RASPON.sub(" ", spec)
            for a in JEDAN.findall(rest):
                a = int(a)
                rows.append((mz, ulica, a, a, "neparni" if a % 2 else "parni"))
                nasao = True
            if not nasao:
                rows.append((mz, ulica, None, None, "sve"))
    df = pd.DataFrame(rows, columns=["mz", "ulica", "od", "do", "paritet"])
    # "Naselje Nahorevo" u Odluci je "Nahorevo" u OSM-u: dodaj varijantu bez riječi "Naselje"
    nas = df[df.ulica.str.match(r"(?i)naselje ")].copy()
    nas["ulica"] = nas.ulica.str.replace(r"(?i)^naselje\s+", "", regex=True)
    return pd.concat([df, nas], ignore_index=True)


def main() -> None:
    nazivi = pd.read_csv(DATA / "mz_lista.csv").query("opcina == @OPCINA").mz.tolist()
    t = tekst_odluke(RAW / "centar_odluka_mz.pdf")
    pravila = pravila_iz_odluke(t, nazivi)
    pravila.to_csv(INTERIM / "centar_ulice_mz.csv", index=False)
    print(f"Pravila iz Odluke: {len(pravila)} redova, {pravila.ulica.nunique()} ulica, "
          f"{pravila.mz.nunique()} od {len(nazivi)} MZ")
    nema = sorted(set(nazivi) - set(pravila.mz))
    if nema:
        print("MZ bez ulica:", nema)

    z = gpd.read_file(INTERIM / "zgrade.gpkg")
    z = z[z.opcina == OPCINA].copy()
    adr = z.addr_street.notna() & z.addr_housenumber.notna()
    z["mz"] = None
    z.loc[adr, "mz"] = ng.svrstaj_po_adresi(z[adr], pravila)
    z["mz_izvor"] = np.where(z.mz.notna(), "adresa", "knn")
    bez = z.mz.isna()
    z.loc[bez, "mz"] = ng.svrstaj_po_ulici(z[bez], pravila)
    z.loc[bez & z.mz.notna(), "mz_izvor"] = "ulica"
    stamb = z.zapremina > 0
    print(f"Centar: {len(z)} zgrada; svrstavanje stambenih: " + ", ".join(
        f"{k} {v:.0%}" for k, v in z[stamb].mz_izvor.where(z[stamb].mz.notna(), "knn")
        .value_counts(normalize=True).items()))
    z["mz"] = ng.knn_glasanje(z)

    opcine, _ = ucitaj_granice()
    oc = opcine[opcine.opcina == OPCINA].geometry.iloc[0]
    tacke = z[z.mz.notna()].copy()
    tacke["geometry"] = tacke.representative_point()
    tacke = tacke.drop_duplicates(subset="geometry")
    vor = shapely.voronoi_polygons(shapely.MultiPoint(tacke.geometry.to_list()), extend_to=oc.envelope.buffer(1000))
    vor = gpd.GeoDataFrame(geometry=list(vor.geoms), crs=CRS_M)
    vor = gpd.sjoin(vor, tacke[["mz", "geometry"]], predicate="contains").dissolve(by="mz").reset_index()
    vor = popuni_mz(oc, vor[["mz", "geometry"]], popuni_rupe=True)
    vor["opcina"] = OPCINA
    vor.to_file(INTERIM / "mz_centar.gpkg", driver="GPKG")
    print(f"MZ poligona Centar: {len(vor)}")

    d = gpd.read_file(INTERIM / "dijelovi.gpkg")
    ostali = d[d.opcina != OPCINA]
    dc = d[d.opcina == OPCINA][["h3_id", "opcina", "geometry"]]
    dc = gpd.overlay(dc, vor[["mz", "geometry"]], how="intersection", keep_geom_type=True).explode(ignore_index=True)
    dc = dc[dc.area > 1].dissolve(by=["h3_id", "opcina", "mz"], as_index=False)
    dc["povrsina"] = dc.area
    dc["P"] = worldpop_po_dijelu(dc)
    d = gpd.GeoDataFrame(pd.concat([ostali, dc[ostali.columns]], ignore_index=True), crs=CRS_M)
    d.to_file(INTERIM / "dijelovi.gpkg", driver="GPKG")
    print(f"interim/dijelovi.gpkg: {len(d)} dijelova")


if __name__ == "__main__":
    main()
