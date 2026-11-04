"""Korak 6: MZ poligoni za Novi Grad iz adresa zgrada.

Ulaz:  raw/novi_grad_ulice_mz.pdf (ili ručno provjeren data/novi_grad_ulice_mz.csv),
       interim/zgrade.gpkg, interim/polja.gpkg, interim/dijelovi_03.gpkg, raw/granice.json
Izlaz: interim/novi_grad_ulice_mz_auto.csv  (izvučeno iz PDF-a, za ručnu provjeru)
       interim/mz_novi_grad.gpkg            (MZ poligoni)
       interim/zgrade_mz_novi_grad.gpkg     (svrstane zgrade)
       interim/dijelovi.gpkg                (dijelovi polja s MZ i za Novi Grad)

Format pravila (CSV): mz, ulica, od, do, paritet
  paritet: sve | parni | neparni;  od/do prazno = cijela ulica.
Ako data/novi_grad_ulice_mz.csv postoji, koristi se on (ručno provjeren),
inače automatski izvučen spisak iz PDF-a.

Ako je adresirano < 40% stambenih zgrada, skripta staje (izlaz 2) dok se ne
pokrene sa --nastavi.
"""
from __future__ import annotations

import argparse
import re
import sys

import geopandas as gpd
import numpy as np
import pandas as pd
import shapely
from scipy.spatial import cKDTree

from common import (CRS_M, DATA, INTERIM, RAW, kucni_broj, normaliziraj,
                    normaliziraj_ulicu, popuni_mz, ucitaj_granice, worldpop_po_dijelu)

OPCINA = "Novi Grad Sarajevo"
K_SUSJEDA = 7
TESKE_ULICE = ["Safeta Zajke", "Adema Buće", "Safeta Hadžića", "Novopazarska", "Džemala Bijedića"]


# ------------------------------------------------------------ PDF -> pravila

def parsiraj_brojeve(tekst: str) -> list[tuple[int | None, int | None, str]]:
    """'neparni 1-55, parni od 2 do 40' -> [(1,55,'neparni'), (2,40,'parni')]."""
    t = normaliziraj(tekst)
    if not t or re.search(r"\b(cijela|sve|svi|kompletna|citava)\b", t) and not re.search(r"\d", t):
        return [(None, None, "sve")]
    out = []
    for dio in re.split(r"[;,/]|\s+i\s+", str(tekst).lower()):
        dio = normaliziraj(dio)
        if not dio:
            continue
        par = "parni" if "neparn" not in dio and "parn" in dio else ("neparni" if "neparn" in dio else "sve")
        brojevi = [int(x) for x in re.findall(r"\d+", dio)]
        if len(brojevi) >= 2:
            out.append((min(brojevi[:2]), max(brojevi[:2]), par))
        elif len(brojevi) == 1:
            if re.search(r"\b(od|preko|dalje|nadalje)\b", dio) or dio.endswith(("do kraja", "kraja")):
                out.append((brojevi[0], None, par))
            else:
                out.append((brojevi[0], brojevi[0], par))
        elif par != "sve" or "bb" in dio:
            out.append((None, None, par))
    return out or [(None, None, "sve")]


def izvuci_pravila_iz_pdf(pdf_path, mz_nazivi: list[str]) -> pd.DataFrame:
    import pdfplumber

    mz_norm = {normaliziraj(m): m for m in mz_nazivi}
    # dodatni oblici naziva u dokumentima
    for m in mz_nazivi:
        mz_norm.setdefault(normaliziraj(m).replace("alipasino polje ", "alipasino polje "), m)
        mz_norm.setdefault(normaliziraj(m.replace("Naselje heroja", "N.H.")), m)

    def prepoznaj_mz(txt: str) -> str | None:
        n = normaliziraj(re.sub(r"^\s*(mz|mjesna zajednica)\s*", "", txt, flags=re.I))
        n = re.sub(r"^(mz|mjesna zajednica)\s+", "", n)
        if n in mz_norm:
            return mz_norm[n]
        for k, v in mz_norm.items():
            if n.startswith(k) and len(n) - len(k) <= 3:
                return v
        return None

    redovi, trenutna = [], None
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tabele = page.extract_tables()
            linije = []
            if tabele:
                for tab in tabele:
                    for red in tab:
                        celije = [c.strip() for c in red if c and c.strip()]
                        if celije:
                            linije.append(celije)
            else:
                for l in (page.extract_text() or "").splitlines():
                    if l.strip():
                        linije.append([l.strip()])
            for celije in linije:
                prva = celije[0]
                mz = prepoznaj_mz(" ".join(celije)) or prepoznaj_mz(prva)
                if mz:
                    trenutna = mz
                    continue
                if trenutna is None:
                    continue
                # ukloni redni broj
                celije = [re.sub(r"^\d+\.\s*", "", c) for c in celije]
                if len(celije) >= 2:
                    ulica, brojevi = celije[0], " ".join(celije[1:])
                else:
                    m = re.match(r"^(?P<u>.*?[A-Za-zčćžšđČĆŽŠĐ.)])\s*(?:[-–:]\s*)?(?P<b>(?:(?:ne)?parni|od|br\.?|bb|\d).*)?$",
                                 celije[0])
                    if not m:
                        continue
                    ulica, brojevi = m.group("u"), m.group("b") or ""
                if len(normaliziraj(ulica)) < 3 or normaliziraj(ulica) in ("naziv ulice", "ulica", "r br"):
                    continue
                for od, do, par in parsiraj_brojeve(brojevi):
                    redovi.append({"mz": trenutna, "ulica": ulica.strip(), "od": od, "do": do,
                                   "paritet": par, "izvorni_tekst": " | ".join(celije)})
    return pd.DataFrame(redovi, columns=["mz", "ulica", "od", "do", "paritet", "izvorni_tekst"])


# ------------------------------------------------------------ svrstavanje

def svrstaj_po_adresi(z: pd.DataFrame, pravila: pd.DataFrame) -> pd.Series:
    pr = pravila.copy()
    pr["u"] = pr.ulica.map(normaliziraj_ulicu)
    po_ulici = {u: g for u, g in pr.groupby("u")}
    rez = []
    for ulica, br in zip(z.addr_street, z.addr_housenumber):
        u = normaliziraj_ulicu(ulica)
        g = po_ulici.get(u)
        if g is None:
            rez.append(None)
            continue
        n = kucni_broj(br)
        kandidati = []
        for _, r in g.iterrows():
            if n is not None:
                if r.paritet == "parni" and n % 2:
                    continue
                if r.paritet == "neparni" and not n % 2:
                    continue
                if pd.notna(r.od) and n < r.od:
                    continue
                if pd.notna(r["do"]) and n > r["do"]:
                    continue
            kandidati.append(r.mz)
        if not kandidati and g.mz.nunique() == 1:
            kandidati = [g.mz.iloc[0]]
        rez.append(pd.Series(kandidati).mode().iloc[0] if kandidati else None)
    return pd.Series(rez, index=z.index)


def knn_glasanje(z: gpd.GeoDataFrame) -> pd.Series:
    poz = z.mz.notna()
    if poz.sum() == 0:
        return z.mz
    xy = np.c_[z.geometry.centroid.x, z.geometry.centroid.y]
    tree = cKDTree(xy[poz.values])
    lab = z.mz[poz].to_numpy()
    k = min(K_SUSJEDA, int(poz.sum()))
    nep = np.where(~poz.values)[0]
    dist, idx = tree.query(xy[nep], k=k)
    dist, idx = np.atleast_2d(dist).reshape(len(nep), k), np.atleast_2d(idx).reshape(len(nep), k)
    out = z.mz.copy()
    for i, row_d, row_i in zip(nep, dist, idx):
        glas = {}
        for d, j in zip(row_d, row_i):
            glas[lab[j]] = glas.get(lab[j], 0) + 1 / max(d, 1.0)
        out.iloc[i] = max(glas, key=glas.get)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--nastavi", action="store_true",
                    help="nastavi i kad je adresirano < 40%% zgrada")
    a = ap.parse_args()

    mzl = pd.read_csv(DATA / "mz_lista.csv")
    nazivi = mzl[mzl.opcina == OPCINA].mz.tolist()

    rucno = DATA / "novi_grad_ulice_mz.csv"
    if rucno.exists():
        pravila = pd.read_csv(rucno)
        print(f"Pravila: {rucno.name} (ručno provjereno), {len(pravila)} redova")
    else:
        pdf = RAW / "novi_grad_ulice_mz.pdf"
        if not pdf.exists():
            print("Nema raw/novi_grad_ulice_mz.pdf ni data/novi_grad_ulice_mz.csv")
            return 1
        pravila = izvuci_pravila_iz_pdf(pdf, nazivi)
        pravila.to_csv(INTERIM / "novi_grad_ulice_mz_auto.csv", index=False)
        print(f"Pravila iz PDF-a: {len(pravila)} redova -> interim/novi_grad_ulice_mz_auto.csv "
              "(PROVJERITI; ispravljenu verziju spremiti kao data/novi_grad_ulice_mz.csv)")
    nema = sorted(set(nazivi) - set(pravila.mz))
    if nema:
        print(f"UPOZORENJE: MZ bez ijedne ulice u spisku: {nema}")

    z = gpd.read_file(INTERIM / "zgrade.gpkg")
    z = z[z.opcina == OPCINA].copy()
    stamb = z.zapremina > 0
    adr = z.addr_street.notna() & z.addr_housenumber.notna()
    pokr = adr[stamb].mean() if stamb.any() else 0
    print(f"Novi Grad: {len(z)} zgrada, stambenih {stamb.sum()}, adresirano stambenih {pokr:.1%}")
    if pokr < 0.40 and not a.nastavi:
        print("STOP: adresirano je manje od 40% stambenih zgrada (SPEC korak 6). "
              "Pokrenuti ponovo sa --nastavi ako je to prihvatljivo.")
        return 2

    z["mz"] = None
    z.loc[adr, "mz"] = svrstaj_po_adresi(z[adr], pravila)
    z["mz_izvor"] = np.where(z.mz.notna(), "adresa", "knn")
    print(f"Svrstano po adresi: {z.mz.notna().sum()} od {adr.sum()} adresiranih")
    ne = z[adr & z.mz.isna()]
    if len(ne):
        top = ne.addr_street.value_counts().head(15)
        print("Najčešće nesvrstane ulice:\n" + top.to_string())
    for u in TESKE_ULICE:
        m = z.addr_street.map(normaliziraj_ulicu) == normaliziraj_ulicu(u)
        print(f"  {u}: {m.sum()} zgrada -> {z.loc[m, 'mz'].value_counts().to_dict()}")

    z["mz"] = knn_glasanje(z)
    z.to_file(INTERIM / "zgrade_mz_novi_grad.gpkg", driver="GPKG")

    # Voronoi oko zgrada -> MZ poligoni
    opcine, _ = ucitaj_granice()
    ng = opcine[opcine.opcina == OPCINA].geometry.iloc[0]
    tacke = z[z.mz.notna()].copy()
    tacke["geometry"] = tacke.representative_point()
    tacke = tacke.drop_duplicates(subset="geometry")
    vor = shapely.voronoi_polygons(shapely.MultiPoint(tacke.geometry.to_list()),
                                   extend_to=ng.envelope.buffer(1000))
    vor = gpd.GeoDataFrame(geometry=list(vor.geoms), crs=CRS_M)
    vor = gpd.sjoin(vor, tacke[["mz", "geometry"]], predicate="contains").dissolve(by="mz").reset_index()
    vor = popuni_mz(ng, vor[["mz", "geometry"]], popuni_rupe=True)
    vor["opcina"] = OPCINA
    vor.to_file(INTERIM / "mz_novi_grad.gpkg", driver="GPKG")
    print(f"MZ poligona Novi Grad: {len(vor)}")

    # dijelovi polja za Novi Grad s MZ
    d = gpd.read_file(INTERIM / "dijelovi_03.gpkg")
    ostali = d[d.opcina != OPCINA]
    dng = d[d.opcina == OPCINA][["h3_id", "opcina", "geometry"]]
    dng = gpd.overlay(dng, vor[["mz", "geometry"]], how="intersection", keep_geom_type=True)
    dng = dng.explode(ignore_index=True)
    dng = dng[dng.area > 1].dissolve(by=["h3_id", "opcina", "mz"], as_index=False)
    dng["povrsina"] = dng.area
    dng["P"] = worldpop_po_dijelu(dng)
    d = gpd.GeoDataFrame(pd.concat([ostali, dng[ostali.columns]], ignore_index=True), crs=CRS_M)
    d.to_file(INTERIM / "dijelovi.gpkg", driver="GPKG")
    print(f"interim/dijelovi.gpkg: {len(d)} dijelova")
    return 0


if __name__ == "__main__":
    sys.exit(main())
