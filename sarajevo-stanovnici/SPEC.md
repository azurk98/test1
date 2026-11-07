# Procjena broja stanovnika po polju — Grad Sarajevo

Specifikacija za izradu u Claude Codeu. Ulazni podaci koje je trebalo ručno izvući nalaze se u `data/`; sve ostalo skripte preuzimaju same.

**Pokretanje:** raspakuj folder, otvori ga u Claude Codeu i napiši: *„Pročitaj SPEC.md i implementiraj ga korak po korak. Prije koraka 5 mi pokaži koliko zgrada u OSM-u ima spratnost i adresu.“*

## 1. Cilj

Za svako polje heksagonalne mreže (H3, rezolucija 9, oko 0,1 km² po polju) procijeniti broj stanovnika i starosne grupe na području četiri gradske općine: Centar, Stari Grad, Novo Sarajevo, Novi Grad.

Dva pravila koja se ne krše:

1. Zbir svih polja jedne općine mora biti tačno jednak zvaničnoj procjeni FZS-a za tu općinu (30.06.2026).
2. Sve ispod nivoa općine je raspodjela (model), a ne mjerenje. Zato svako polje dobije i raspon (min–max) i oznaku pouzdanosti.

## 2. Izlazi

| Datoteka | Sadržaj |
|---|---|
| `out/polja_h3.gpkg` (+ `.geojson`) | `h3_id`, `opcina`, `mz` (ako je poznata), `stanovnici`, `stanovnici_min`, `stanovnici_max`, `d0_14`, `d15_64`, `d65plus`, `pouzdanost` (A/B/C), `izvor_tezine` |
| `out/mz_zbirovi.csv` | Procijenjeni broj stanovnika po MZ, gdje je MZ granica poznata |
| `out/karta.html` | Interaktivna karta: boja po broju stanovnika, tooltip s brojkama i pouzdanošću |
| `out/validacija.md` | Rezultati provjera iz odjeljka 6 |

Oznake pouzdanosti:
- **A**: polje je u zoni sa poznatim zbirom MZ i dobrim podacima o zgradama.
- **B**: poznat je samo zbir općine, ali su podaci o zgradama dobri.
- **C**: polje se oslanja uglavnom na WorldPop, jer podaci o zgradama fale.

## 3. Ulazni podaci

### Već izvučeno (`data/`)

| Datoteka | Šta je | Napomena |
|---|---|---|
| `opcine_procjena_2026.csv` | FZS procjena na 30.06.2026: ukupno i po grupama 0–14, 15–64, 65+, za svih 9 općina KS | Tvrdi kontrolni zbirovi |
| `mz_lista.csv` | Sve 82 MZ: općina, OSM relacija (gdje postoji), izvor granica, dostupni podaci | Poligoni u OSM-u: Stari Grad svih 16, Novo Sarajevo 17 od 18 (Dolac Malta nema). Centar i Novi Grad nemaju |
| `mz_novi_grad_2010.csv` | Novi Grad, stanovnici po MZ na 31.12.2010 (evidencija MZ): ukupno, starost, spol, domaćinstva | 27 od 29 MZ; Alipašin Most III i Zabrđe tada nisu postojale. Kod Saraj Polja i Dolca zbir starosnih grupa odstupa za 100 (greška u izvoru). Saraj Polje ima samo 1,5 stanovnika po domaćinstvu (ostale MZ 2,0–3,8), pa je sumnjiv i broj domaćinstava |
| `stari_grad_graf3_nepotvrdjeno.csv` | Stari Grad, stanovnici i domaćinstva po MZ, Strategija 2024–2027, Graf 3 (str. 16) | Vrijednosti su izvučene **bez naziva MZ**. Prije upotrebe pročitati nazive sa grafikona (render stranice). Ne pretpostavljati abecedni redoslijed |

### Preuzimaju skripte

| Izvor | Upotreba | Gdje |
|---|---|---|
| WorldPop R2025A, 100 m, constrained, BIH, godina 2026 | Rezervna raspodjela unutar zone | `https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/BIH/v1/100m/constrained/` (datoteka po obrascu `bih_pop_2026_CN_100m_R2025A_v1.tif`, provjeriti naziv) |
| OSM zgrade: `building`, `building:levels`, `height`, `addr:street`, `addr:housenumber` | Glavna težina: stambena zapremina | Overpass (upit ispod) ili Geofabrik `bosnia-herzegovina-latest.osm.pbf` + pyrosm |
| OSM granice općina | Kontrolne zone | Relacije: Stari Grad 2528243, Centar 2528180, Novo Sarajevo 2528239, Novi Grad 2528240; Grad Sarajevo 2567380 |
| OSM granice MZ | Zone za MZ zbirove i izvještaj | ID-jevi relacija u `data/mz_lista.csv` |
| OSM POI (`shop`, `amenity`, `office`) | Poslovno prizemlje kod stambenih zgrada | Isti upit |
| OSM `landuse` | Stambeno, industrijsko, komercijalno | Isti upit |
| Novi Grad: spisak ulica i kućnih brojeva po MZ (04.11.2025) | Pridruživanje zgrada MZ preko adresa | `https://www.novigradsarajevo.ba/wp-content/uploads/2025/12/04.11.2025.-Lista-naziva-i-ulica-po-mjesnih-zajednicama.pdf` |
| Stari Grad: Strategija 2024–2027 | Nazivi MZ na Grafu 3 | `https://starigrad.ba/userfiles/file/2024/2/strategija.pdf` |
| Centar: Odluka o osnivanju i organizaciji MZ | Provjeriti da li navodi ulice po MZ (vjerovatno sken: OCR) | `https://www.centar.ba/documents/download/86618/odluka-o-osnivanju-i-organizaciji-mjesnih-zajednica-na-podrucju-opcine-centar` |
| Opcionalno: GHSL GHS-BUILT-H (visina zgrada, 100 m) | Spratnost gdje je OSM nema | JRC GHSL |

Primjer Overpass upita (area ID = 3600000000 + ID relacije):

```
[out:json][timeout:600];
area(id:3602567380)->.grad;
(
  way["building"](area.grad);
  relation["building"](area.grad);
  node["shop"](area.grad);
  node["amenity"](area.grad);
  node["office"](area.grad);
  way["landuse"](area.grad);
  relation["landuse"](area.grad);
);
out geom tags;
```

## 4. Postupak

### Korak 1: Mreža

H3 rezolucija 9 nad unijom četiri općine. Svako polje presjeći s granicama općina i MZ, pa se računa po dijelovima polja.

### Korak 2: Stambena zapremina zgrade

```
zapremina = površina_otiska_m2 × stambeni_spratovi
```

Spratnost, prvo raspoloživo:
1. `building:levels`
2. `height / 3`
3. GHSL visina / 3
4. Podrazumijevano po tipu: `house`, `detached`, `semidetached_house`, `terrace` = 2; `residential` = 4; `apartments` = 6; `yes` = 3

Kalibracija: izračunati udio zgrada sa `building:levels`. Ako je ispod 30%, uključiti GHSL.

Stambeni dio zgrade:
- **Stambene** (puna zapremina): `house`, `detached`, `semidetached_house`, `terrace`, `apartments`, `residential`, `bungalow`, `farm`.
- **`yes` (netipizirane)**: puna zapremina u `landuse=residential`, 30% u `landuse=commercial/retail`, 0 u `landuse=industrial`, 70% drugdje.
- **Nestambene** (0): `commercial`, `retail`, `office`, `industrial`, `warehouse`, `school`, `kindergarten`, `university`, `college`, `hospital`, `church`, `mosque`, `chapel`, `religious`, `public`, `civic`, `government`, `train_station`, `transportation`, `garage`, `garages`, `carport`, `shed`, `hut`, `roof`, `service`, `sports_hall`, `stadium`, `hotel`, `kiosk`, `greenhouse`, `construction`, `ruins`.
- **Poslovno prizemlje**: stambena zgrada koja sadrži `shop`/`amenity`/`office` tačku ima `stambeni_spratovi = spratnost − 1`.
- Zgrade ispod 25 m² isključiti.

Pridruživanje polju: po centroidu zgrade. Zgrade veće od 2000 m² razrezati po poljima.

### Korak 3: WorldPop

Zbir piksela po dijelu polja (piksel dijeliti po površini presjeka).

### Korak 4: Kombinovana težina

Unutar svake zone `z`:

```
W(c,z) = α · B(c,z)/ΣB(z) + (1 − α) · P(c,z)/ΣP(z)
```

- `B` je stambena zapremina iz koraka 2, a `P` je WorldPop.
- `α = 0.7` kao početna vrijednost, po općini.
- **Provjera nedostajućih zgrada**: dio polja gdje je WorldPop značajan a `B = 0` označiti kao pouzdanost C i u njemu koristiti samo WorldPop.

### Korak 5: Kontrolni zbirovi (odozgo prema dolje)

1. **Općina:** `T(o)` = FZS 30.06.2026 (tvrdi zbir).
2. **MZ unutar općine:**
   - **Stari Grad** (tek kad se potvrde nazivi na Grafu 3): `T(mz) = T(o) × n(mz) / Σn`. Koriste se samo udjeli, pa razlika između evidencije i FZS-a ne smeta.
   - **Novi Grad** (podaci iz 2010, meko ograničenje): `T(mz) = T(o) × [β·udio_2010 + (1 − β)·udio_modela]`, uz `β = 0.5`, jer je od 2010. bilo nove gradnje.
     - `udio_modela` je udio težine `W` te MZ u općini, prije MZ ograničenja.
     - Alipašin Most III i Zabrđe nisu postojale 2010. Utvrditi iz kojih su MZ izdvojene (odluka općine ili poređenje spiska ulica). Matičnu i novu MZ tretirati kao jednu grupu za `udio_2010`, a unutar grupe dijeliti po `udio_modela`.
     - Ako se matična MZ ne može utvrditi: za dvije nove MZ uzeti `udio_modela`, a udjele ostalih 27 preskalirati na ostatak.
   - **Novo Sarajevo i Centar:** nema MZ podataka. Raspodjela ide samo po težinama unutar općine; MZ služi samo za izvještaj.
3. **Raspodjela:** `stanovnici(c,z) = T(z) × W(c,z) / ΣW(z)`. Polje = zbir njegovih dijelova.

### Korak 6: MZ za Novi Grad (nema poligona)

1. Normalizirati nazive ulica u OSM-u i u spisku: dijakritici, `Ali-pašino` / `Alipašino`, `čikma`, skraćenice.
2. Zgradu s `addr:street` + `addr:housenumber` svrstati u MZ po rasponu brojeva (parni/neparni, od–do).
3. Zgrade bez adrese svrstati glasanjem k najbližih zgrada s adresom.
4. Iz svrstanih zgrada napraviti MZ poligone (Voronoi oko zgrada, spojiti po MZ, odrezati granicom općine).

Prvo izmjeriti pokrivenost adresama. Ako je manje od 40% zgrada adresirano, prijaviti to prije nastavka.

Najteže su ulice koje dijele više MZ: Safeta Zajke, Adema Buće, Safeta Hadžića, Novopazarska, Džemala Bijedića.

### Korak 7: Starosne grupe

Starosnu strukturu općine (FZS 2026) primijeniti na polja. Opcionalno korigovati po MZ starosnoj strukturi Novog Grada iz 2010, skaliranoj na 2026.

### Korak 8: Raspon i pouzdanost

Pokrenuti tri scenarija:
- `α ∈ {0.5, 0.7, 0.9}`
- podrazumijevana spratnost −1 / 0 / +1

Za svako polje upisati najmanju i najveću vrijednost kao `stanovnici_min` / `stanovnici_max`.

## 5. Struktura projekta

```
sarajevo-stanovnici/
  SPEC.md
  data/          # ulazi iz ovog razgovora
  raw/           # preuzeto (ne mijenjati ručno)
  interim/       # međurezultati
  src/
    01_preuzimanje.py
    02_zgrade.py
    03_mreza.py
    04_mz_novi_grad.py
    05_raspodjela.py
    06_provjera.py
    07_karta.py
  out/
```

Python 3.11+: `geopandas`, `shapely>=2`, `h3>=4`, `rasterio`, `exactextract` (ili `rasterstats`), `pyrosm` ili `osmnx`, `pandas`, `folium` ili `pydeck`.

Svaki korak čita iz `raw/`, `data/` ili `interim/` i piše u `interim/` ili `out/`, tako da se može ponoviti zasebno.

## 6. Provjera (u `out/validacija.md`)

1. **Zbir po općini:** mora biti tačno jednak FZS-u.
2. **Stari Grad bez MZ ograničenja:** pokrenuti model samo sa zbirom općine, uporediti udjele MZ s Grafom 3 i dati prosječnu grešku po MZ (MAPE). Porede se udjeli, ne brojke, jer Graf 3 ukupno daje 38.124, a FZS 33.103. To je glavna mjera kvaliteta modela.
3. **Novi Grad:** model bez MZ ograničenja uporediti s udjelima iz 2010. Velika odstupanja treba objasniti novom gradnjom ili ih označiti.
4. **Gustina poda:** stambeni m² po stanovniku po polju bi trebalo biti oko 15–60. Polja izvan toga izlistati.
5. **Vizuelno:** bez stanovnika u industrijskim zonama, parkovima i na aerodromu; Dobrinja, Alipašino Polje i Grbavica gusti.
6. **Starosne grupe:** zbir grupa jednak ukupnom u svakom polju.

## 7. Ograničenja

- Zvanični najmanji nivo je općina. Sve ispod je procjena.
- Općinske evidencije po MZ su iz različitih godina i metodologija, i precjenjuju broj stanovnika (dijaspora ostaje prijavljena). Zato se koriste samo udjeli.
- OSM granice MZ su okvirne. Po oznaci `source` u OSM-u nastale su kombinacijom podataka popisa 1991. i poslijeratnih podataka. Provjeriti da li se rubovi MZ poklapaju s granicom općine.
- Ovo je procjena **stanovnika po mjestu stanovanja**, ne dnevno prisutnih ljudi. Za analizu tržišta sljedeći korak je dnevno stanovništvo: radna mjesta, škole, fakulteti, preko zapremine poslovnih zgrada i kapaciteta ustanova.

## 8. Mogući dodatni izvori

- **CIK, Opći izbori 4.10.2026:** rezultati po biračkim mjestima, uz odluke OIK-a o pridruživanju ulica biračkim mjestima. Ako CIK objavljuje broj upisanih birača po biračkom mjestu, to daje broj odraslih po MZ za sve četiri općine.
- **Izvještaji OIK-a o izborima za savjete MZ:** Novo Sarajevo 2023, Centar 2025. Mogu sadržavati broj birača po MZ.
- **Popis 2013 po naseljenim mjestima:** kontrolni zbir za sela (npr. Bojnik, Rečica): `T(nm) = popis_2013(nm) × T(o)_2026 / popis_2013(o)`. Ostatak općine ide gradskom dijelu.
