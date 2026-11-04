# Procjena broja stanovnika po H3 polju: Grad Sarajevo

Implementacija specifikacije iz [`SPEC.md`](SPEC.md).

## Pokretanje

```bash
pip install -r requirements.txt
cd src
python 01_preuzimanje.py        # OSM (Overpass), WorldPop, PDF-ovi općina -> raw/
python 02_zgrade.py             # zgrade, spratnost, stambeni udio + KONTROLNA TAČKA
python 03_mreza.py              # H3 res 9, dijelovi polja (polje ∩ općina ∩ MZ), WorldPop
python 04_mz_novi_grad.py       # MZ Novog Grada iz adresa (staje ako je < 40% adresirano)
python 05_raspodjela.py         # težine, kontrolni zbirovi, starosne grupe, 9 scenarija
python 06_provjera.py           # -> out/validacija.md
python 07_karta.py              # -> out/karta.html
```

**Kontrolna tačka prije koraka 5:** `02_zgrade.py` ispisuje (i sprema u
`interim/zgrade_statistika.json`) koliko zgrada ima `building:levels` i adresu,
ukupno i po općini. Pregledati prije pokretanja `05_raspodjela.py`.

## Ručni koraci (ne mogu se automatizovati pouzdano)

| Šta | Gdje | Posljedica ako se preskoči |
|---|---|---|
| Pročitati nazive MZ na Grafu 3 (Strategija Stari Grad, str. 16) i spremiti `data/stari_grad_graf3.csv` (`mz,stanovnici`) | `raw/stari_grad_strategija.pdf` | Stari Grad samo sa zbirom općine; nema MAPE provjere (validacija 2) |
| Pregledati `interim/novi_grad_ulice_mz_auto.csv` (izvučeno iz PDF-a heuristički) i ispravljenu verziju spremiti kao `data/novi_grad_ulice_mz.csv` | `raw/novi_grad_ulice_mz.pdf` | MZ Novog Grada se oslanjaju na neprovjereno parsiranje PDF-a |
| Utvrditi matične MZ za Alipašin Most III i Zabrđe, upisati u `MATICNE_MZ_NOVI_GRAD` u `src/common.py` | odluka općine | Koristi se pravilo za nepoznatu matičnu MZ (SPEC 5.2) |
| Ako je < 30% zgrada sa spratnošću: isječak GHS-BUILT-H 100 m kao `raw/ghsl_built_h.tif` | JRC GHSL | Koristi se podrazumijevana spratnost po tipu |

## Odluke u implementaciji (gdje SPEC ostavlja prostor)

- Metrički CRS: EPSG:32634 (UTM 34N).
- Raspon (korak 8): puna mreža 3 × 3 scenarija (α ∈ {0.5, 0.7, 0.9} × spratnost −1/0/+1);
  glavni scenarij α = 0.7, pomak 0. Pomak se primjenjuje samo na zgrade s podrazumijevanom spratnošću.
- „Značajan WorldPop" za oznaku C: ≥ 5 stanovnika u dijelu polja (`C_PRAG_WORLDPOP`). U takvom dijelu težina je samo WorldPop.
- Netipizirane zgrade i nepoznati tipovi (`building=*` koji nije ni na jednom spisku) tretiraju se kao `yes`.
- Kad se landuse poligoni preklapaju, prioritet je industrial > commercial/retail > residential.
- Stari Grad: dijelovi općine koje OSM MZ poligoni ne pokrivaju pripajaju se susjednoj MZ. Novo Sarajevo: ostaju bez MZ (npr. Dolac Malta).
- Cijeli brojevi: metoda najvećeg ostatka po općini (zbir tačno = FZS), pa po dijelu polja za starosne grupe (zbir grupa = ukupno u polju). Zbir grupa po općini zbog toga može odstupati od FZS-a za nekoliko osoba; prikazano u validaciji.
- Pouzdanost polja: C ako dijelovi s oznakom C nose ≥ 50% stanovnika polja, inače A ako dijelovi s MZ kontrolnim zbirom nose ≥ 50%, inače B.
- Opcionalna korekcija starosti po MZ Novog Grada (korak 7) nije implementirana.
- Polja izlaze s dodatnim kolonama `stambeni_m2` i `worldpop` (za provjeru gustine).
