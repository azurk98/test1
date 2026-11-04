# Procjena broja stanovnika po H3 polju: Grad Sarajevo

Mreža: H3 rezolucija **10** (~0,015 km², stranica šestougla ~66 m; 9.033 polja), zadano u `common.py`
(`H3_RES`, ili varijabla okruženja `H3_RES=9` za rezoluciju iz SPEC-a, ~0,105 km²). Na rezoluciji 10
procjena po polju je nesigurnija (manje zgrada po polju), ali zbirovi po općini ostaju tačni; MAPE za
Stari Grad 17,1% (rezolucija 9: 16,4%).

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
python 12_google_places.py      # (opcionalno, treba GOOGLE_MAPS_API_KEY) trgovine iz Google Places -> raw/
python 10_teren.py              # topografija: reljef, izohipse, visina i nagib po polju -> out/teren_*
python 11_putevi.py             # mreža puteva za prikaz -> out/putevi.geojson
python 15_ulice.py              # pristup autom: uske i strme ulice -> out/ulice_h3.csv (prije koraka 14)
python 14_kvalitet_zivota.py    # kvalitet života: pješačka dostupnost sadržaja -> out/kvalitet_zivota_h3.csv
python 16_sunce.py              # sati sunca zimi (zasjenjenje brdima) -> out/sunce_h3.csv
python 17_zrak.py               # smog i magla zimi: izloženost inverziji -> out/zrak_h3.csv
python 13_stranica.py           # interaktivna stranica (artifact) -> out/stranica.html
python 07_karta.py              # ponovo, da karta dobije slojeve iz koraka 08–11
```

**Kontrolna tačka prije koraka 5:** `02_zgrade.py` ispisuje (i sprema u
`interim/zgrade_statistika.json`) koliko zgrada ima `building:levels` i adresu,
ukupno i po općini. Pregledati prije pokretanja `05_raspodjela.py`.

## Ručni koraci (ne mogu se automatizovati pouzdano)

| Šta | Gdje | Posljedica ako se preskoči |
|---|---|---|
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
| `pjesice_5/10/15` | stanovnici dostupni pješice (OSM ulice i staze; 4,8 km/h na ravnom, nagib po Toblerovoj formuli iz Copernicus DEM-a: 10% uzbrdo 3,4 km/h, 20% uzbrdo 2,4 km/h) |
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

Postojeće trgovine: OSM + 28 trgovina koje ima samo Overture Maps Places (`raw/overture_places.parquet`,
filtrirano po kategoriji, pouzdanosti i nazivu; duplikati < 75 m od OSM-a uklonjeni). Poređenje dva
izvora (Lincoln–Petersen) procjenjuje 400–675 trgovina namirnica u četiri općine, a OSM ih ima 237
(35–60%); nedostaju uglavnom male nezavisne trgovine. Uz nagib u pješačkom vremenu ~73.100 od 270.600 stanovnika (27%)
nema supermarket u 10 min pješice (prema OSM + Overture; bez nagiba bilo bi ~53.900). Nagib smanjuje
pješački doseg na strmim padinama (> 20%) na manje od pola, pa u bijele mrlje ulaze i brdska naselja
(Hrasno Brdo, Velešići, Hrid-Jarčedoli).
Oprez: bijele mrlje su u prigradskim dijelovima Novog Grada, gdje je model stanovništva najnesigurniji
(1,75–2,5× udjela iz 2010) i gdje OSM vjerovatno ne bilježi sve male trgovine. Kolona
`znakovi_zemljista` (parking, poslovni objekat, gradilište) je samo nagovještaj; vlasništvo i
namjenu provjeriti u katastru i prostornom planu.

## Google Places (`12_google_places.py`, opcionalno)

Nearby Search (New) za tipove supermarket, grocery_store, convenience_store, market, food_store u
krugovima oko H3 polja rezolucije 8 koja pokrivaju naseljena polja (183 kruga, gusta područja se dijele;
procjena 180–550 zahtjeva: `--koliko`). Ključ se čita iz `GOOGLE_MAPS_API_KEY`. Prema uslovima Google
Maps Platform: koordinate se koriste najviše 30 dana od preuzimanja (`09_supermarket.py` ih poslije
ignoriše), a Google trgovine se ne crtaju na kartama (ulaze samo u model).

## Kvalitet života (`14_kvalitet_zivota.py`)

Minute hoda (OSM mreža, nagib po Tobleru) od svakog polja do najbližeg sadržaja: trgovina namirnica
(iz 09), stanica javnog prevoza, osnovna škola, ambulanta/dom zdravlja/poliklinika, park (pristup s
ruba parka), vrtić, apoteka, dječije igralište, bolnica, sportski teren ili centar (sve iz OSM-a;
`out/sadrzaji.geojson`). Bodovi po kategoriji 1/(1+(t/t50)²), indeks 0–100 = ponderisani zbir minus
kazne za buku (≤ 150 m od autoputa/magistrale/primarne ceste), industriju (> 25% polja) i vrlo strm
teren (> 20%). Ponderi i t50 u `KATEGORIJE` su procjena. Prosječan indeks po stanovniku: Novo Sarajevo 71,
Centar 58, Novi Grad 51, Stari Grad 47. Najbolje MZ: Kovačići, Čengić Vila I, Malta, Željeznička, Trg heroja;
najslabije: Reljevo, Zabrđe, Dobroševići, Mošćanica.

## Pristup autom: uske i strme ulice (`15_ulice.py`)

OSM gotovo nema širinu ulica (29 od 6.650 stambenih), pa se širina procjenjuje kao koridor između
zgrada (okomice lijevo i desno do 20 m s polovine svake dionice): < 9 m usko, < 6 m vrlo usko; uske su
i `lanes=1`, `living_street`, `track`. Ograde i zidovi nisu u OSM-u, pa stvarna ulica može biti uža.
Nagib: Copernicus DSM bez zgrada (najniža tačka u 90 m, pa izglađivanje), mjeren na 100 m duž ulice
(kraće dionice su šum DEM-a od 30 m); mostovi i tuneli isključeni. Provjera: primarne ceste 90%
dionica ≤ 6,8%. Za svako polje: put autom do najbliže tercijarne ili veće ceste (najveći nagib, metri
uskog puta, makadam) i udio strmih/uskih ulica u polju; ocjena 0–100. Loš pristup oduzima do 15 bodova
od indeksa kvaliteta života. Najteži pristup: Toka-Džeka, Gornji Velešići, Sumbuluša, Mahmutovac,
Hrid-Jarčedoli. Najveći uspon na putu do glavne ceste: ≤ 8% za ~182.000 stanovnika, 8–12% ~21.000,
12–16% ~23.000, 16–20% ~20.000, > 20% ~24.000; ~33.000 stanovnika ima više od 100 m uske ulice do glavne ceste.

## Najbolje za život (stranica, pogled „Best to live“)

Jedna ocjena 0–100 po naseljenom polju, računa se u pregledniku iz svih slojeva: svakodnevni sadržaji
pješice (koji se broje najviše zavisi od profila), pristup autom, zimsko sunce (≤ 3 h = 0, 7,8 h = 100),
čist zrak i malo magle (100 − indeks), mir (udaljenost od bučnih cesta, industrija) i blag teren
(≤ 5% = 100, ≥ 25% = 0). Profili: uravnoteženo, porodica s djecom, penzioneri, bez auta, zrak i sunce;
klizači za vlastite pondere. Uravnoteženo: najbolje Dobrinja D, Malta, Čengić Vila I i II, Željeznička;
„zrak i sunce“: Sedrenik, Dobrinja D, Medrese; najslabije Toka-Džeka, Mahmutovac, Hrid-Jarčedoli.

## Smog i magla (`17_zrak.py`)

Relativni indeksi izloženosti (0–100), ne mjerenje. Inverzija: udio inverzionih dana kad je polje ispod
gornje granice, iz visine iznad dna doline (najniža tačka terena u krugu 3 km), uz pretpostavljenu granicu
~200 m iznad dna (logistička, širina 50 m). Smog = inverzija × (1 + 0,5 × blizina prometnih cesta);
magla = inverzija × blizina rijeka. Provjera na FHMZ stanicama (godišnji PM2.5 2025, izvještaj u
`raw/zrak/`; koordinate stanica približne): Spearman 0,56 (0,74 bez Saraj Polja, obuhvat 66%). Prva
verzija s gustinom malih kuća kao znakom grijanja na čvrsto gorivo dala je obrnut odnos (r = −0,42; oko
Bjelava je mnogo kuća, a zrak je najčišći jer centar grije plin), pa je izbačena; podaci o gasnoj mreži
bi to riješili. ~210.000 stanovnika je ispod inverzije u > 90% inverzionih dana; najmanje izloženi: Mošćanica,
Sedrenik, Toka-Džeka, Širokača (200–260 m iznad dna doline).

## Sati sunca zimi (`16_sunce.py`)

Sati direktnog sunca 21. decembra i 21. januara (vedar dan): položaj sunca svakih 5 minuta, za 7 tačaka
po polju zraka prema suncu do 25 km kroz Copernicus DEM (bez zgrada, uz zakrivljenost Zemlje i refrakciju).
Na ravnom horizontu 21. decembar ima 8,8 h. Najviše sunca: južne padine (Medrese, Sedrenik ~7,9 h) i
otvoreni zapad (Dobroševići, Sokolje, Briješće); najmanje: Mahmutovac (2,2 h), Toka-Džeka (2,7 h),
Hrid-Jarčedoli, Širokača, Babića bašča, Bistrik, Mjedenica (4,2–5,6 h; sjeverne padine ispod Trebevića i
kanjon Miljacke). Sjena susjednih zgrada i zimska magla u dolini nisu uključeni.

## Topografija (`10_teren.py`)

Copernicus DEM GLO-30 (30 m; © DLR e.V. 2010–2014, © Airbus Defence and Space GmbH 2014–2018,
Copernicus licenca). To je model površine (uključuje zgrade i krošnje), pa se prije računanja
izglađuje (~60 m). Izlazi: `teren_h3.csv` (srednja/min/max visina, srednji nagib u % po polju),
`teren_reljef.png` (sjenčenje + boje po visini), `teren_sjena.png`, `teren_izohipse.geojson`
(50 m, glavne 250 m), `teren_okvir.json` (okvir slika). Stanovnici po nagibu polja: ravno (< 5%)
~93.000, 5–10% ~51.000, 10–20% ~90.000, > 20% ~36.000; iznad 700 m n.v. ~15.600.

Lokalna karta (`out/karta.html`): podloge Esri satelit (zadano), OpenTopoMap, OpenStreetMap;
preko njih Esri sjenčenje reljefa i izohipse.

## MZ Novog Grada po nazivima ulica

Pored adresa s kućnim brojem (8% stambenih zgrada), zgrada bez adrese dobija najbližu imenovanu OSM
ulicu (≤ 50 m); ako cijela ta ulica po spisku pripada jednoj MZ, zgrada ide u tu MZ. Direktno svrstano:
70% stambenih zgrada (adresa 8%, ulica 62%), ostatak glasanjem susjeda. Dobrinja C više nije uska
traka (0,92 udjela iz 2010; prije 0,08), Švrakino Selo I 0,58 (0,20), Aneks 0,71 (0,38). Reljevo sada
dobija svih ~830 zgrada svojih ulica (3,2× udjela iz 2010: 1.193 stanovnika 2010. na 828 kuća, vjerovatno
rast ili vikendice), pa je ukupna MAPE prema 2010. 0,396 (prije 0,375).

## Graf 3 i parametri po općini

Nazivi MZ na Grafu 3 (Strategija Starog Grada 2024–2027, str. 16) pročitani su s renderovane stranice
(`data/stari_grad_graf3.csv`; redoslijed stubova nije abecedni). Stari Grad sada ima MZ kontrolne zbirove,
a provjera 2 (MAPE) je moguća. S parametrima kalibrisanim na Novom Gradu (α 0,9, niske 0,5) MAPE je bila
29,5%; u Starom Gradu (stare mahale, malo blokova) najbolje odgovara α ≈ 0,5 bez korekcije za kuće
(MAPE 16,4%, izmjereno na istim podacima na kojima je kalibrisano). Zato su α i gustina niskih zgrada
po općini (`ALFA_OPCINA`, `GUSTINA_NISKA_OPCINA` u `common.py`); Novo Sarajevo preuzima parametre
Novog Grada (blokovi), Centar sredinu (nema podataka).

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
