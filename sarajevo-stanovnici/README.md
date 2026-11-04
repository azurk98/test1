# Procjena broja stanovnika po H3 polju: Grad Sarajevo

Implementacija specifikacije iz [`SPEC.md`](SPEC.md).

## Pokretanje

```bash
pip install -r requirements.txt
cd src
python 01_preuzimanje.py        # OSM (Overpass; --bbbike za BBBike ekstrakt), WorldPop, GHSL, PDF-ovi -> raw/
python 02_zgrade.py             # zgrade, spratnost, stambeni udio + KONTROLNA TAČKA
python 03_mreza.py              # H3 res 9, dijelovi polja (polje ∩ općina ∩ MZ), WorldPop
python 04_mz_novi_grad.py --nastavi  # MZ Novog Grada iz adresa (bez --nastavi staje ako je < 40% adresirano)
python 05_raspodjela.py         # težine, kontrolni zbirovi, starosne grupe, 9 scenarija
python kalibracija_gustine.py   # (dijagnostika) omjer gustine kuće/blokovi i α na MZ Novog Grada
python 06_provjera.py           # -> out/validacija.md
python 07_karta.py              # -> out/karta.html
python 08_dostupnost.py         # dostupnost i atraktivnost lokacije -> out/dostupnost_h3.gpkg/.csv
python 09_supermarket.py        # lokacije za novi supermarket (Huff) -> out/supermarket_*.csv/.gpkg
python 10_teren.py              # topografija: reljef, izohipse, visina i nagib po polju -> out/teren_*
python 07_karta.py              # ponovo, da karta dobije slojeve iz koraka 08–10
```

**Kontrolna tačka prije koraka 5:** `02_zgrade.py` ispisuje (i sprema u
`interim/zgrade_statistika.json`) koliko zgrada ima `building:levels` i adresu,
ukupno i po općini. Pregledati prije pokretanja `05_raspodjela.py`.

## Ručni koraci (ne mogu se automatizovati pouzdano)

| Šta | Gdje | Posljedica ako se preskoči |
|---|---|---|
| Pročitati nazive MZ na Grafu 3 (Strategija Stari Grad, str. 16) i spremiti `data/stari_grad_graf3.csv` (`mz,stanovnici`) | `raw/stari_grad_strategija.pdf` | Stari Grad samo sa zbirom općine; nema MAPE provjere (validacija 2) |
| (Opcionalno) pregledati `interim/novi_grad_ulice_mz_auto.csv` (620 pravila, 290 ulica, izvučeno iz tabela PDF-a; napomene o izuzecima u koloni `izvorni_tekst` se ne primjenjuju) i ispravljenu verziju spremiti kao `data/novi_grad_ulice_mz.csv` | `raw/novi_grad_ulice_mz.pdf` | Izuzeci iz napomena (npr. brojevi koji pripadaju Novom Sarajevu) se ignorišu |
| Utvrditi matične MZ za Alipašin Most III i Zabrđe, upisati u `MATICNE_MZ_NOVI_GRAD` u `src/common.py` | odluka općine | Koristi se pravilo za nepoznatu matičnu MZ (SPEC 5.2) |

## Prvo pokretanje (04.11.2026)

- **OSM**: Overpass nije bio dostupan (prekid veze / preopterećen), pa je korišten BBBike
  sedmični ekstrakt za Sarajevo (`--bbbike`). Granice koje izlaze iz okvira ekstrakta
  (Centar, Stari Grad, Grad Sarajevo, MZ Mošćanica) dopunjene su s `api.openstreetmap.org`.
  Dijelovi Centra i Starog Grada izvan okvira imaju ~40 stanovnika po WorldPopu (zanemarivo).
- **Kontrolna tačka**: 46.838 zgrada; `building:levels` ima **4,7%**, adresu **11,2%**
  (Novi Grad stambene: **8,3%**, ispod praga od 40%). Nastavljeno sa `--nastavi`; adrese
  su svrstane u MZ u 95% slučajeva, sve 29 MZ dobile su poligon, ali su granice grube.
- **Spratnost**: GHSL je na zgradama s poznatom spratnošću gotovo nekoristan (r = 0,13,
  ~3 sprata bez obzira na stvarnu visinu). Zato se, umjesto GHSL/3, spratnost procjenjuje
  modelom (gradient boosting na 2.194 zgrade s `building:levels`; ulazi: površina i oblik
  otiska, tip, gustina i veličina okolnih zgrada, GHSL). Prostorna unakrsna provjera
  (blokovi 500 m): r = 0,70, MAE 1,7 sprata.
- **Validacija**: zbirovi općina i starosnih grupa tačni. Stambena površina je precijenjena
  (medijan ~80 m²/st.; vjerovatno pomoćni objekti tipa `yes`), što utiče samo na apsolutni
  nivo, ne na raspodjelu unutar općine. Visoke zgrade (Alipašino Polje, Dobrinja C/D) su
  bile potcijenjene u odnosu na prigradska naselja (Briješće, Dobroševići); vidi ispravku ispod.
- **Ispravka potcjenjivanja visokih zgrada** (`src/kalibracija_gustine.py`, na MZ Novog Grada 2010):
  1. *Gustina stanovanja*: m² u zgradama ispod 5 spratova nosi ~0,5 stanovnika u odnosu na m²
     u blokovima (~100 vs ~50 m²/st.; stabilno za pragove 4–6). `GUSTINA_NISKA = 0.5`.
  2. *α = 0,9* umjesto 0,7: WorldPop daje visokim MZ 11% stanovnika Novog Grada (evidencija 2010: 30%),
     a prigradskim 34% (2010: 13%). Greška udjela MZ pada s α (0,7: 0,40; 0,9: 0,375; 1,0: 0,37).
     Scenariji raspona ostaju 0,5 / 0,7 / 0,9.
  Rezultat: Alipašino Polje 0,70–1,10 udjela iz 2010 (prije 0,29–0,69), Dobrinja D 0,92 (0,65),
  Olimpijsko Selo 0,83 (0,61); Briješće 1,75 (2,24), Dobroševići 2,50 (3,14).
  Preostala odstupanja (Dobrinja C, Švrakino Selo I, Aneks) potiču od grubih MZ poligona.

## Dostupnost i atraktivnost lokacije (`08_dostupnost.py`)

Dodatni pokazatelji po polju, za analizu lokacija; procjena stanovnika se ne mijenja.

| Kolona | Značenje |
|---|---|
| `pjesice_5/10/15` | stanovnici dostupni pješice (OSM ulice i staze, 4,8 km/h) |
| `auto_5/10/15` | stanovnici dostupni autom (jednosmjerne, `maxspeed` ili tipična brzina klase × 0,65) |
| `poi_10min` | trgovine, usluge, uredi (`shop`/`amenity`/`office`) za 10 min pješice |
| `stanica_m`, `stanica_tip` | najbliža stanica (tramvaj / trolejbus / autobus; oznake < 40 m spojene) |
| `stanice_400m`, `tramvaj_400m` | broj stanica u krugu 400 m |
| `glavna_cesta_m` | udaljenost do magistralne/primarne/sekundarne ceste |
| `ulice_km_km2`, `raskrsnice_km2` | gustina ulica i raskrsnica |
| `atraktivnost` | 0–100: ponderisani percentilni rangovi (pješice 10 min 20%, auto 10 min 15%, POI 20%, stanice 400 m 15%, najbliža stanica 10%, glavna cesta 10%, raskrsnice 10%); ponderi u `TEZINE` |

Ograničenja: dostupni stanovnici samo iz četiri modelirane općine (rubni efekat prema Ilidži,
Vogošći, Istočnom Sarajevu); bez podataka o gužvi; javni prevoz je samo blizina stanica, bez voznog reda.

## Lokacije za supermarket (`09_supermarket.py`)

Huffov model: stanovnici polja dijele kupovinu namirnica na trgovine do 20 min
(P ∝ veličina · vrijeme^-2; vrijeme = min(pješice, autom + 2 min)). Postojeće trgovine iz OSM-a:
supermarket = 1 (ili površina/1000 m², 0,5–4), mall 1, department_store 0,5, convenience 0,25.
Nova trgovina (A = 1) u svakom polju bez supermarketa, ≤ 400 m od glavne ceste; izbor redom
(svaki izbor ulazi u konkurenciju), najmanje 700 m razmaka. Dvije strategije:

- **bijela_mrlja**: najviše stanovnika koji danas hodaju > 10 min do supermarketa dolazi na ≤ 10 min.
  Prva tri: Briješće, Naselje heroja Sokolje, Švrakino Selo III (najviše kupaca među njima, ~1.900).
- **najveci_promet**: najviše osvojenih kupaca (uglavnom od konkurencije): Željeznička, Trg heroja,
  Alipašino Polje BII; stabilno za λ 1,5–2,5.

Danas ~56.000 od 270.600 stanovnika (21%) nema supermarket u 10 min pješice (prema OSM-u).
Oprez: bijele mrlje su u prigradskim dijelovima Novog Grada, gdje je model stanovništva najnesigurniji
(1,75–2,5× udjela iz 2010) i gdje OSM vjerovatno ne bilježi sve male trgovine. Kolona
`znakovi_zemljista` (parking, poslovni objekat, gradilište) je samo nagovještaj; vlasništvo i
namjenu provjeriti u katastru i prostornom planu.

## Topografija (`10_teren.py`)

Copernicus DEM GLO-30 (30 m; © DLR e.V. 2010–2014, © Airbus Defence and Space GmbH 2014–2018,
Copernicus licenca). To je model površine (uključuje zgrade i krošnje), pa se prije računanja
izglađuje (~60 m). Izlazi: `teren_h3.csv` (srednja/min/max visina, srednji nagib u % po polju),
`teren_reljef.png` (sjenčenje + boje po visini), `teren_sjena.png`, `teren_izohipse.geojson`
(50 m, glavne 250 m), `teren_okvir.json` (okvir slika). Stanovnici po nagibu polja: ravno (< 5%)
~93.000, 5–10% ~51.000, 10–20% ~90.000, > 20% ~36.000; iznad 700 m n.v. ~15.600.

Lokalna karta (`out/karta.html`): podloge Esri satelit (zadano), OpenTopoMap, OpenStreetMap;
preko njih Esri sjenčenje reljefa i izohipse.

## Odluke u implementaciji (gdje SPEC ostavlja prostor)

- Metrički CRS: EPSG:32634 (UTM 34N).
- Raspon (korak 8): puna mreža 3 × 3 scenarija (α ∈ {0.5, 0.7, 0.9} × spratnost −1/0/+1);
  glavni scenarij α = 0.7, pomak 0. Pomak se primjenjuje na procijenjenu spratnost (model ili
  podrazumijevana), ne na spratnost upisanu u OSM.
- „Značajan WorldPop" za oznaku C: ≥ 5 stanovnika u dijelu polja (`C_PRAG_WORLDPOP`). U takvom dijelu težina je samo WorldPop.
- Netipizirane zgrade i nepoznati tipovi (`building=*` koji nije ni na jednom spisku) tretiraju se kao `yes`.
- Kad se landuse poligoni preklapaju, prioritet je industrial > commercial/retail > residential.
- Stari Grad: dijelovi općine koje OSM MZ poligoni ne pokrivaju pripajaju se susjednoj MZ. Novo Sarajevo: ostaju bez MZ (npr. Dolac Malta).
- Cijeli brojevi: metoda najvećeg ostatka po općini (zbir tačno = FZS), pa po dijelu polja za starosne grupe (zbir grupa = ukupno u polju). Zbir grupa po općini zbog toga može odstupati od FZS-a za nekoliko osoba; prikazano u validaciji.
- Pouzdanost polja: C ako dijelovi s oznakom C nose ≥ 50% stanovnika polja, inače A ako dijelovi s MZ kontrolnim zbirom nose ≥ 50%, inače B.
- Opcionalna korekcija starosti po MZ Novog Grada (korak 7) nije implementirana.
- Polja izlaze s dodatnim kolonama `stambeni_m2` i `worldpop` (za provjeru gustine).
