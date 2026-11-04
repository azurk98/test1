# Validacija
Sve ispod nivoa općine je model (raspodjela), ne mjerenje.

## 1. Zbir po općini
**OK**

| opcina | model | FZS_2026 | razlika |
|---|---|---|---|
| Centar Sarajevo | 51598 | 51598 | 0 |
| Novi Grad Sarajevo | 124111 | 124111 | 0 |
| Novo Sarajevo | 61796 | 61796 | 0 |
| Stari Grad Sarajevo | 33103 | 33103 | 0 |

## 2. Stari Grad: model bez MZ ograničenja vs Graf 3 (udjeli)
Graf 3 ukupno 38,124, FZS 33,103 (porede se udjeli).

**MAPE po MZ: 17.1%** (glavna mjera kvaliteta modela)

| mz | graf3_udio | model_udio | rel_greska |
|---|---|---|---|
| Mošćanica | 0.116 | 0.181 | 0.565 |
| Mahmutovac | 0.056 | 0.032 | 0.416 |
| Kovači | 0.040 | 0.051 | 0.278 |
| Bistrik | 0.083 | 0.063 | 0.236 |
| Mjedenica | 0.018 | 0.021 | 0.172 |
| Babića bašča | 0.043 | 0.035 | 0.170 |
| Medrese | 0.086 | 0.072 | 0.163 |
| Baščaršija | 0.056 | 0.064 | 0.145 |
| Sumbuluša | 0.038 | 0.033 | 0.126 |
| Vratnik | 0.087 | 0.076 | 0.125 |
| Ferhadija | 0.029 | 0.031 | 0.078 |
| Toka-Džeka | 0.043 | 0.040 | 0.059 |
| Hrid-Jarčedoli | 0.065 | 0.069 | 0.054 |
| Širokača | 0.068 | 0.065 | 0.050 |
| Logavina | 0.091 | 0.086 | 0.050 |
| Sedrenik | 0.082 | 0.079 | 0.040 |

## 3. Novi Grad: model bez MZ ograničenja vs udjeli 2010
Udjeli 2010 preskalirani na dio općine bez novih MZ. Odstupanje > 30% je označeno; veće udjele u modelu obično objašnjava nova gradnja nakon 2010.

| mz | model_udio | udio_2010 | omjer | oznaka |
|---|---|---|---|---|
| Alipašino Polje CI | 0.010 | 0.023 | 0.422 | model < 2010 za >30%: provjeriti |
| Alipašin Most II | 0.012 | 0.025 | 0.481 | model < 2010 za >30%: provjeriti |
| Švrakino Selo I | 0.011 | 0.020 | 0.539 | model < 2010 za >30%: provjeriti |
| Čengić Vila | 0.018 | 0.031 | 0.595 | model < 2010 za >30%: provjeriti |
| Alipašino Polje CII | 0.014 | 0.023 | 0.620 | model < 2010 za >30%: provjeriti |
| Aneks | 0.018 | 0.028 | 0.666 | model < 2010 za >30%: provjeriti |
| Alipašino Polje AI | 0.017 | 0.023 | 0.722 |  |
| Buća Potok | 0.033 | 0.045 | 0.724 |  |
| Olimpijsko Selo | 0.017 | 0.023 | 0.744 |  |
| Dobrinja B | 0.037 | 0.050 | 0.746 |  |
| Švrakino Selo III | 0.014 | 0.018 | 0.769 |  |
| Dobrinja D | 0.037 | 0.047 | 0.776 |  |
| Švrakino Selo II | 0.033 | 0.040 | 0.827 |  |
| Alipašin Most I | 0.055 | 0.067 | 0.828 |  |
| Otoka | 0.021 | 0.025 | 0.831 |  |
| Alipašino Polje BII | 0.022 | 0.027 | 0.839 |  |
| Dobrinja C | 0.036 | 0.042 | 0.873 |  |
| Dolac | 0.044 | 0.049 | 0.885 |  |
| Alipašino Polje AII | 0.022 | 0.023 | 0.992 |  |
| Staro Hrasno | 0.025 | 0.024 | 1.018 |  |
| Alipašino Polje BI | 0.030 | 0.029 | 1.046 |  |
| Dobrinja A | 0.050 | 0.039 | 1.301 | model > 2010 za >30%: nova gradnja? |
| Naselje heroja Sokolje | 0.057 | 0.041 | 1.409 | model > 2010 za >30%: nova gradnja? |
| Saraj Polje | 0.061 | 0.041 | 1.498 | model > 2010 za >30%: nova gradnja? |
| Dobroševići | 0.066 | 0.029 | 2.237 | model > 2010 za >30%: nova gradnja? |
| Briješće | 0.087 | 0.037 | 2.339 | model > 2010 za >30%: nova gradnja? |
| Reljevo | 0.028 | 0.008 | 3.335 | model > 2010 za >30%: nova gradnja? |
| Alipašin Most III | 0.059 | nan | nan | nova MZ (nema 2010) |
| Zabrđe | 0.065 | nan | nan | nova MZ (nema 2010) |

Konačni udjeli korišteni kao meko ograničenje: vidi `interim/raspodjela_info.json`.

## 4. Gustina poda (stambeni m² po stanovniku, očekivano 15–60)
Medijan (polja s ≥ 10 st.): 91.5 m²/st. Polja izvan raspona: **2399** od 2854. Polja sa stanovnicima a bez stambenih zgrada (pouzdanost C, samo WorldPop): **346**.

| h3_id | opcina | mz | stanovnici | stambeni_m2 | m2_po_st | pouzdanost |
|---|---|---|---|---|---|---|
| 8a1ef4582acffff | Centar Sarajevo | Hrastovi-Mrkovići | 45 | 73.800 | 1.600 | C |
| 8a1ef4582497fff | Novo Sarajevo | Velešići | 11 | 19.000 | 1.700 | B |
| 8a1ef4582037fff | Centar Sarajevo | Park-Višnjik | 32 | 64.900 | 2.000 | B |
| 8a1ef4591b17fff | Centar Sarajevo | Koševsko Brdo | 40 | 89.000 | 2.200 | B |
| 8a1ef459019ffff | Novi Grad Sarajevo | Otoka | 141 | 393.200 | 2.800 | C |
| 8a1ef4590007fff | Novi Grad Sarajevo | Otoka | 114 | 427.600 | 3.800 | C |
| 8a1ef4590517fff | Novi Grad Sarajevo | Alipašino Polje CI | 205 | 898.000 | 4.400 | C |
| 8a1ef45956f7fff | Novo Sarajevo | Pofalići I | 76 | 359.400 | 4.700 | C |
| 8a1ef4590567fff | Novi Grad Sarajevo | Alipašino Polje AI | 57 | 274.200 | 4.800 | C |
| 8a1ef459c1a7fff | Stari Grad Sarajevo | Širokača | 50 | 255.000 | 5.100 | C |
| 8a1ef4583127fff | Stari Grad Sarajevo | Sedrenik | 21 | 122.300 | 5.800 | A |
| 8a1ef4590a1ffff | Novo Sarajevo | Pofalići II | 111 | 646.500 | 5.800 | C |
| 8a1ef4590337fff | Novi Grad Sarajevo | Čengić Vila | 104 | 630.300 | 6.100 | C |
| 8a1ef4580c8ffff | Centar Sarajevo | Pionirska Dolina | 10 | 78.600 | 7.900 | B |
| 8a1ef458280ffff | Centar Sarajevo | Koševo II | 25 | 206.700 | 8.300 | B |
| 8a1ef4583617fff | Stari Grad Sarajevo | Mošćanica | 29 | 244.800 | 8.400 | C |
| 8a1ef45908d7fff | Novi Grad Sarajevo | Alipašin Most III | 81 | 702.000 | 8.700 | C |
| 8a1ef4590ba7fff | Novo Sarajevo | Pofalići II | 82 | 823.800 | 10.000 | C |
| 8a1ef45956cffff | Novo Sarajevo | Pofalići I | 63 | 645.800 | 10.300 | C |
| 8a1ef4596227fff | Novi Grad Sarajevo | Alipašino Polje AII | 10 | 105.500 | 10.600 | A |
| 8a1ef4582727fff | Centar Sarajevo | Park-Višnjik | 55 | 581.700 | 10.600 | B |
| 8a1ef4591a0ffff | Centar Sarajevo | Marijin Dvor | 33 | 373.900 | 11.300 | B |
| 8a1ef45829b7fff | Centar Sarajevo | Džidžikovac-Koševo I | 23 | 265.900 | 11.600 | C |
| 8a1ef459cd37fff | Centar Sarajevo | Skenderija-Podtekija | 28 | 357.200 | 12.800 | B |
| 8a1ef4591197fff | Novo Sarajevo | Grbavica II | 188 | 11,280.400 | 60.000 | B |
| 8a1ef4590447fff | Novi Grad Sarajevo | Švrakino Selo I | 161 | 9,666.500 | 60.000 | A |
| 8a1ef459caf7fff | Stari Grad Sarajevo | Mahmutovac | 72 | 4,323.500 | 60.000 | A |
| 8a1ef459c88ffff | Stari Grad Sarajevo | Širokača | 73 | 4,384.500 | 60.100 | A |
| 8a1ef45911affff | Novo Sarajevo | Grbavica II | 450 | 27,031.300 | 60.100 | B |
| 8a1ef4596a57fff | Novi Grad Sarajevo | Alipašin Most I | 111 | 6,668.700 | 60.100 | A |
| 8a1ef459caa7fff | Stari Grad Sarajevo | Bistrik | 88 | 5,291.300 | 60.100 | A |
| 8a1ef4596337fff | Novi Grad Sarajevo | Alipašin Most I | 11 | 661.600 | 60.100 | A |
| 8a1ef4591d4ffff | Novo Sarajevo | Željeznička | 380 | 22,858.200 | 60.200 | B |
| 8a1ef4590b9ffff | Novo Sarajevo | Čengić Vila I | 87 | 5,236.000 | 60.200 | B |
| 8a1ef4591d0ffff | Novo Sarajevo | Malta | 405 | 24,375.700 | 60.200 | B |
| 8a1ef459170ffff | Novo Sarajevo | Vraca | 104 | 6,260.700 | 60.200 | B |
| 8a1ef4591ab7fff | Novo Sarajevo | Kovačići | 383 | 23,056.600 | 60.200 | B |
| 8a1ef459116ffff | Novo Sarajevo | Kovačići | 313 | 18,846.200 | 60.200 | B |
| 8a1ef4591d17fff | Novo Sarajevo | Malta | 416 | 25,062.100 | 60.200 | B |
| 8a1ef458079ffff | Centar Sarajevo | Hrastovi-Mrkovići | 11 | 662.900 | 60.300 | B |
| 8a1ef459036ffff | Novo Sarajevo | Hrasno | 490 | 29,537.800 | 60.300 | B |
| 8a1ef4591ccffff | Novo Sarajevo | Grbavica II | 507 | 30,564.600 | 60.300 | B |
| 8a1ef4590d5ffff | Novi Grad Sarajevo | Alipašin Most II | 78 | 4,702.700 | 60.300 | A |
| 8a1ef459198ffff | Novo Sarajevo | Željeznička | 317 | 19,156.100 | 60.400 | B |
| 8a1ef4591d57fff | Novo Sarajevo | Željeznička | 522 | 31,549.000 | 60.400 | B |
| 8a1ef459112ffff | Novo Sarajevo | Grbavica I | 411 | 24,851.600 | 60.500 | B |
| 8a1ef459001ffff | Novi Grad Sarajevo | Otoka | 551 | 33,326.200 | 60.500 | A |
| 8a1ef45838b7fff | Stari Grad Sarajevo | Sedrenik | 18 | 1,090.100 | 60.600 | A |
| 8a1ef4595037fff | Novo Sarajevo | Pofalići II | 16 | 969.200 | 60.600 | B |
| 8a1ef459c04ffff | Stari Grad Sarajevo | Mahmutovac | 91 | 5,514.100 | 60.600 | A |
| 8a1ef45911a7fff | Novo Sarajevo | Grbavica II | 544 | 32,979.600 | 60.600 | B |
| 8a1ef4591157fff | Novo Sarajevo | Grbavica I | 470 | 28,512.400 | 60.700 | B |
| 8a1ef459ca9ffff | Stari Grad Sarajevo | Mahmutovac | 149 | 9,046.500 | 60.700 | A |
| 8a1ef4596287fff | Novi Grad Sarajevo | Saraj Polje | 157 | 9,538.400 | 60.800 | A |
| 8a1ef45954f7fff | Novo Sarajevo | Pofalići II | 15 | 911.400 | 60.800 | B |
| 8a1ef4583d27fff | Centar Sarajevo | Hrastovi-Mrkovići | 19 | 1,156.300 | 60.900 | B |
| 8a1ef4591d5ffff | Novo Sarajevo | Željeznička | 640 | 38,955.100 | 60.900 | B |
| 8a1ef4590adffff | Novo Sarajevo | Čengić Vila I | 426 | 25,938.200 | 60.900 | B |
| 8a1ef4591117fff | Novo Sarajevo | Grbavica II | 659 | 40,125.700 | 60.900 | B |
| 8a1ef4590d4ffff | Novi Grad Sarajevo | Alipašin Most II | 91 | 5,544.800 | 60.900 | A |
| 8a1ef4590a57fff | Novo Sarajevo | Čengić Vila I | 551 | 33,583.500 | 61.000 | B |
| 8a1ef4590967fff | Novi Grad Sarajevo | Dolac | 78 | 4,755.600 | 61.000 | A |
| 8a1ef4591d67fff | Novo Sarajevo | Željeznička | 322 | 19,644.400 | 61.000 | B |
| 8a1ef45b272ffff | Novi Grad Sarajevo | Zabrđe | 14 | 854.400 | 61.000 | A |
| 8a1ef45918affff | Novo Sarajevo | Željeznička | 655 | 40,001.900 | 61.100 | B |
| 8a1ef4591daffff | Novo Sarajevo | Malta | 491 | 29,996.900 | 61.100 | B |
| 8a1ef4590877fff | Novi Grad Sarajevo | Buća Potok | 200 | 12,221.300 | 61.100 | A |
| 8a1ef4591027fff | Novo Sarajevo | Grbavica I | 201 | 12,286.500 | 61.100 | B |
| 8a1ef4582a27fff | Centar Sarajevo | Hrastovi-Mrkovići | 32 | 1,956.600 | 61.100 | B |
| 8a1ef4590a4ffff | Novo Sarajevo | Malta | 665 | 40,675.900 | 61.200 | B |
| 8a1ef4596c67fff | Novi Grad Sarajevo | Briješće | 26 | 1,591.900 | 61.200 | A |
| 8a1ef4591c67fff | Novo Sarajevo | Željeznička | 850 | 52,045.600 | 61.200 | B |
| 8a1ef459c32ffff | Stari Grad Sarajevo | Mahmutovac | 95 | 5,823.800 | 61.300 | A |
| 8a1ef4595d2ffff | Novi Grad Sarajevo | Dolac | 14 | 858.800 | 61.300 | A |
| 8a1ef4591d1ffff | Novo Sarajevo | Malta | 567 | 34,800.700 | 61.400 | B |
| 8a1ef4591b87fff | Novo Sarajevo | Željeznička | 24 | 1,474.600 | 61.400 | B |
| 8a1ef459044ffff | Novi Grad Sarajevo | Švrakino Selo I | 185 | 11,369.900 | 61.500 | A |
| 8a1ef458379ffff | Stari Grad Sarajevo | Vratnik | 72 | 4,425.700 | 61.500 | A |
| 8a1ef459099ffff | Novi Grad Sarajevo | Alipašin Most II | 94 | 5,790.100 | 61.600 | A |
| 8a1ef4591187fff | Novo Sarajevo | Grbavica II | 363 | 22,398.900 | 61.700 | B |
| 8a1ef459034ffff | Novo Sarajevo | Hrasno | 378 | 23,336.200 | 61.700 | B |
| 8a1ef459cceffff | Centar Sarajevo | Soukbunar | 37 | 2,284.700 | 61.700 | B |
| 8a1ef4590767fff | Novi Grad Sarajevo | Aneks | 37 | 2,287.800 | 61.800 | A |
| 8a1ef459caeffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 36 | 2,226.400 | 61.800 | A |
| 8a1ef4580457fff | Centar Sarajevo | Pionirska Dolina | 11 | 681.400 | 61.900 | B |
| 8a1ef4591c87fff | Novo Sarajevo | Trg heroja | 631 | 39,104.300 | 62.000 | B |
| 8a1ef4580547fff | Centar Sarajevo | Pionirska Dolina | 11 | 682.100 | 62.000 | B |
| 8a1ef4591077fff | Novo Sarajevo | Grbavica I | 426 | 26,415.800 | 62.000 | B |
| 8a1ef4592867fff | Novi Grad Sarajevo | Švrakino Selo II | 219 | 13,607.500 | 62.100 | A |
| 8a1ef459caaffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 77 | 4,787.000 | 62.200 | A |
| 8a1ef459ca17fff | Stari Grad Sarajevo | Babića bašča | 82 | 5,100.200 | 62.200 | A |
| 8a1ef45920affff | Novi Grad Sarajevo | Dobrinja D | 139 | 8,650.800 | 62.200 | A |
| 8a1ef45839b7fff | Stari Grad Sarajevo | Sedrenik | 12 | 746.900 | 62.200 | A |
| 8a1ef458252ffff | Novo Sarajevo | Velešići | 89 | 5,544.400 | 62.300 | B |
| 8a1ef4583d57fff | Stari Grad Sarajevo | Sedrenik | 41 | 2,556.800 | 62.400 | A |
| 8a1ef459639ffff | Novi Grad Sarajevo | Alipašino Polje AII | 150 | 9,356.000 | 62.400 | A |
| 8a1ef4592977fff | Novi Grad Sarajevo | Alipašino Polje BI | 274 | 17,091.800 | 62.400 | A |
| 8a1ef4591d07fff | Novo Sarajevo | Malta | 524 | 32,700.600 | 62.400 | B |
| 8a1ef4583cf7fff | Stari Grad Sarajevo | Medrese | 73 | 4,561.200 | 62.500 | A |
| 8a1ef4590c4ffff | Novi Grad Sarajevo | Alipašin Most III | 26 | 1,624.700 | 62.500 | A |
| 8a1ef4595697fff | Novo Sarajevo | Pofalići II | 81 | 5,066.900 | 62.600 | B |
| 8a1ef45962dffff | Novi Grad Sarajevo | Alipašino Polje BI | 288 | 18,017.100 | 62.600 | A |
| 8a1ef4590ac7fff | Novo Sarajevo | Čengić Vila I | 242 | 15,141.600 | 62.600 | B |
| 8a1ef4590a2ffff | Novo Sarajevo | Pofalići II | 69 | 4,320.800 | 62.600 | B |
| 8a1ef459cc27fff | Centar Sarajevo | Skenderija-Podtekija | 60 | 3,764.300 | 62.700 | B |
| 8a1ef4590037fff | Novi Grad Sarajevo | Alipašin Most III | 277 | 17,390.100 | 62.800 | A |
| 8a1ef4592967fff | Novi Grad Sarajevo | Alipašino Polje BI | 294 | 18,464.200 | 62.800 | A |
| 8a1ef4583daffff | Stari Grad Sarajevo | Sedrenik | 56 | 3,520.000 | 62.900 | A |
| 8a1ef459c337fff | Stari Grad Sarajevo | Mahmutovac | 111 | 6,980.400 | 62.900 | A |
| 8a1ef4590c27fff | Novi Grad Sarajevo | Alipašin Most II | 82 | 5,156.900 | 62.900 | A |
| 8a1ef4590a6ffff | Novo Sarajevo | Pofalići II | 323 | 20,315.400 | 62.900 | B |
| 8a1ef4591007fff | Novo Sarajevo | Grbavica I | 316 | 19,884.300 | 62.900 | B |
| 8a1ef45908b7fff | Novi Grad Sarajevo | Alipašin Most II | 113 | 7,111.000 | 62.900 | A |
| 8a1ef459c177fff | Stari Grad Sarajevo | Toka-Džeka | 96 | 6,041.400 | 62.900 | A |
| 8a1ef4590d77fff | Novi Grad Sarajevo | Alipašin Most II | 94 | 5,915.900 | 62.900 | A |
| 8a1ef459c307fff | Stari Grad Sarajevo | Mahmutovac | 81 | 5,099.200 | 63.000 | A |
| 8a1ef459030ffff | Novi Grad Sarajevo | Staro Hrasno | 459 | 28,896.600 | 63.000 | A |
| 8a1ef45942cffff | Novi Grad Sarajevo | Dolac | 282 | 17,754.500 | 63.000 | A |
| 8a1ef4591547fff | Novo Sarajevo | Grbavica II | 90 | 5,674.100 | 63.000 | B |
| 8a1ef4590a97fff | Novo Sarajevo | Čengić Vila II | 413 | 26,045.200 | 63.100 | B |
| 8a1ef4591507fff | Novo Sarajevo | Hrasno Brdo | 102 | 6,434.700 | 63.100 | B |
| 8a1ef4591ae7fff | Centar Sarajevo | Skenderija-Podtekija | 40 | 2,525.200 | 63.100 | B |
| 8a1ef459c857fff | Stari Grad Sarajevo | Bistrik | 137 | 8,648.900 | 63.100 | A |
| 8a1ef4582147fff | Centar Sarajevo | Koševo II | 77 | 4,861.500 | 63.100 | B |
| 8a1ef4595baffff | Novo Sarajevo | Velešići | 17 | 1,075.400 | 63.300 | B |
| 8a1ef4591c1ffff | Novo Sarajevo | Trg heroja | 314 | 19,907.700 | 63.400 | B |
| 8a1ef4590897fff | Novi Grad Sarajevo | Alipašin Most II | 129 | 8,181.100 | 63.400 | A |
| 8a1ef459115ffff | Novo Sarajevo | Grbavica I | 514 | 32,617.500 | 63.500 | B |
| 8a1ef459c0dffff | Stari Grad Sarajevo | Toka-Džeka | 28 | 1,777.400 | 63.500 | A |
| 8a1ef459ca6ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 19 | 1,206.400 | 63.500 | A |
| 8a1ef45918b7fff | Novo Sarajevo | Željeznička | 350 | 22,235.000 | 63.500 | B |
| 8a1ef4591d77fff | Novo Sarajevo | Željeznička | 692 | 43,970.400 | 63.500 | B |
| 8a1ef459cb2ffff | Stari Grad Sarajevo | Babića bašča | 92 | 5,846.300 | 63.500 | A |
| 8a1ef4582d47fff | Centar Sarajevo | Koševsko Brdo | 51 | 3,243.300 | 63.600 | B |
| 8a1ef459288ffff | Novi Grad Sarajevo | Dobrinja A | 17 | 1,081.500 | 63.600 | A |
| 8a1ef4592907fff | Novi Grad Sarajevo | Alipašino Polje BI | 317 | 20,167.500 | 63.600 | A |
| 8a1ef45962d7fff | Novi Grad Sarajevo | Alipašino Polje BI | 402 | 25,578.500 | 63.600 | A |
| 8a1ef4591d6ffff | Novo Sarajevo | Željeznička | 157 | 9,990.000 | 63.600 | B |
| 8a1ef4591d37fff | Novo Sarajevo | Pofalići II | 405 | 25,788.000 | 63.700 | B |
| 8a1ea92c8227fff | Novi Grad Sarajevo | Briješće | 15 | 955.200 | 63.700 | A |
| 8a1ef459146ffff | Novo Sarajevo | Vraca | 20 | 1,274.100 | 63.700 | B |
| 8a1ef459c35ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 14 | 892.100 | 63.700 | A |
| 8a1ef45b2197fff | Novi Grad Sarajevo | Zabrđe | 109 | 6,946.500 | 63.700 | A |
| 8a1ef459c157fff | Stari Grad Sarajevo | Toka-Džeka | 75 | 4,779.900 | 63.700 | A |
| 8a1ef45923a7fff | Novi Grad Sarajevo | Dobrinja C | 161 | 10,269.900 | 63.800 | A |
| 8a1ef4590357fff | Novi Grad Sarajevo | Staro Hrasno | 341 | 21,782.000 | 63.900 | A |
| 8a1ef45807b7fff | Centar Sarajevo | Hrastovi-Mrkovići | 24 | 1,534.200 | 63.900 | B |
| 8a1ef459c377fff | Stari Grad Sarajevo | Mahmutovac | 70 | 4,475.700 | 63.900 | A |
| 8a1ef45832b7fff | Stari Grad Sarajevo | Mošćanica | 14 | 895.300 | 64.000 | A |
| 8a1ef459c147fff | Stari Grad Sarajevo | Bistrik | 112 | 7,171.300 | 64.000 | A |
| 8a1ef4591a97fff | Novo Sarajevo | Grbavica I | 236 | 15,115.200 | 64.000 | B |
| 8a1ef45b25affff | Novi Grad Sarajevo | Zabrđe | 26 | 1,666.100 | 64.100 | A |
| 8a1ef4596327fff | Novi Grad Sarajevo | Alipašin Most I | 71 | 4,554.200 | 64.100 | A |
| 8a1ef459562ffff | Novo Sarajevo | Pofalići II | 80 | 5,134.700 | 64.200 | B |
| 8a1ef4592737fff | Novi Grad Sarajevo | Dobrinja B | 18 | 1,155.600 | 64.200 | A |
| 8a1ef459135ffff | Centar Sarajevo | Soukbunar | 41 | 2,632.300 | 64.200 | B |
| 8a1ef459615ffff | Novi Grad Sarajevo | Briješće | 27 | 1,733.600 | 64.200 | A |
| 8a1ef459088ffff | Novi Grad Sarajevo | Buća Potok | 78 | 5,009.400 | 64.200 | A |
| 8a1ef459568ffff | Novo Sarajevo | Pofalići II | 547 | 35,141.500 | 64.200 | B |
| 8a1ef4590c47fff | Novi Grad Sarajevo | Alipašin Most III | 398 | 25,571.500 | 64.200 | A |
| 8a1ea92c96f7fff | Novi Grad Sarajevo | Briješće | 37 | 2,378.300 | 64.300 | A |
| 8a1ef4590237fff | Novi Grad Sarajevo | Staro Hrasno | 796 | 51,184.100 | 64.300 | A |
| 8a1ef45909b7fff | Novi Grad Sarajevo | Alipašin Most II | 43 | 2,766.300 | 64.300 | A |
| 8a1ef459cb6ffff | Stari Grad Sarajevo | Vratnik | 61 | 3,929.200 | 64.400 | A |
| 8a1ef458218ffff | Centar Sarajevo | Park-Višnjik | 59 | 3,807.400 | 64.500 | B |
| 8a1ef459086ffff | Novi Grad Sarajevo | Buća Potok | 177 | 11,427.300 | 64.600 | A |
| 8a1ef459620ffff | Novi Grad Sarajevo | Alipašino Polje AII | 406 | 26,252.700 | 64.700 | A |
| 8a1ef4590c5ffff | Novi Grad Sarajevo | Alipašin Most III | 151 | 9,765.000 | 64.700 | A |
| 8a1ef4590af7fff | Novo Sarajevo | Čengić Vila I | 184 | 11,900.600 | 64.700 | B |
| 8a1ef4582ce7fff | Centar Sarajevo | Koševsko Brdo | 47 | 3,042.300 | 64.700 | B |
| 8a1ef4591d8ffff | Novo Sarajevo | Trg heroja | 263 | 17,044.500 | 64.800 | B |
| 8a1ef4591a87fff | Novo Sarajevo | Kovačići | 406 | 26,344.700 | 64.900 | B |
| 8a1ef4596217fff | Novi Grad Sarajevo | Alipašino Polje AII | 407 | 26,412.700 | 64.900 | A |
| 8a1ef459624ffff | Novi Grad Sarajevo | Alipašino Polje AI | 119 | 7,723.400 | 64.900 | A |
| 8a1ef459154ffff | Novo Sarajevo | Vraca | 212 | 13,765.700 | 64.900 | B |
| 8a1ef4592887fff | Novi Grad Sarajevo | Dobrinja A | 226 | 14,678.000 | 64.900 | A |
| 8a1ef45962a7fff | Novi Grad Sarajevo | Alipašino Polje AII | 290 | 18,836.300 | 65.000 | A |
| 8a1ef4590537fff | Novi Grad Sarajevo | Alipašino Polje AI | 184 | 11,954.700 | 65.000 | A |
| 8a1ea92c9cc7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 44 | 2,860.300 | 65.000 | A |
| 8a1ef459c167fff | Stari Grad Sarajevo | Bistrik | 129 | 8,390.600 | 65.000 | A |
| 8a1ef4594c77fff | Novi Grad Sarajevo | Zabrđe | 15 | 977.100 | 65.100 | A |
| 8a1ef4596017fff | Novi Grad Sarajevo | Briješće | 54 | 3,519.900 | 65.200 | A |
| 8a1ef459500ffff | Novo Sarajevo | Pofalići II | 10 | 652.100 | 65.200 | B |
| 8a1ef45946dffff | Novi Grad Sarajevo | Alipašin Most II | 135 | 8,804.800 | 65.200 | A |
| 8a1ef459298ffff | Novi Grad Sarajevo | Saraj Polje | 150 | 9,804.000 | 65.400 | A |
| 8a1ef4592917fff | Novi Grad Sarajevo | Saraj Polje | 230 | 15,032.800 | 65.400 | A |
| 8a1ef4590a37fff | Novo Sarajevo | Pofalići II | 190 | 12,429.700 | 65.400 | B |
| 8a1ea92c9837fff | Novi Grad Sarajevo | Zabrđe | 16 | 1,047.600 | 65.500 | A |
| 8a1ef459105ffff | Novo Sarajevo | Kovačići | 226 | 14,821.800 | 65.600 | B |
| 8a1ef4591aaffff | Novo Sarajevo | Kovačići | 255 | 16,726.100 | 65.600 | B |
| 8a1ef4591c4ffff | Novo Sarajevo | Grbavica II | 200 | 13,124.100 | 65.600 | B |
| 8a1ef4594c2ffff | Novi Grad Sarajevo | Zabrđe | 16 | 1,050.100 | 65.600 | A |
| 8a1ef459c267fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 11 | 722.400 | 65.700 | A |
| 8a1ef45834c7fff | Stari Grad Sarajevo | Vratnik | 95 | 6,239.100 | 65.700 | C |
| 8a1ef45864dffff | Centar Sarajevo | Šip | 21 | 1,379.200 | 65.700 | B |
| 8a1ef459056ffff | Novi Grad Sarajevo | Švrakino Selo II | 90 | 5,911.500 | 65.700 | A |
| 8a1ef45826e7fff | Centar Sarajevo | Trg oslobođenja-Centar | 71 | 4,668.000 | 65.700 | B |
| 8a1ef4590aa7fff | Novo Sarajevo | Pofalići II | 175 | 11,510.800 | 65.800 | B |
| 8a1ef459292ffff | Novi Grad Sarajevo | Alipašino Polje BI | 462 | 30,402.000 | 65.800 | A |
| 8a1ef4592927fff | Novi Grad Sarajevo | Alipašino Polje BI | 711 | 46,798.400 | 65.800 | A |
| 8a1ef4590a9ffff | Novo Sarajevo | Čengić Vila II | 192 | 12,641.600 | 65.800 | B |
| 8a1ef45960e7fff | Novi Grad Sarajevo | Briješće | 68 | 4,478.500 | 65.900 | A |
| 8a1ef459cc57fff | Centar Sarajevo | Soukbunar | 39 | 2,569.600 | 65.900 | B |
| 8a1ef45928a7fff | Novi Grad Sarajevo | Dobrinja A | 245 | 16,146.100 | 65.900 | A |
| 8a1ea92cd54ffff | Novi Grad Sarajevo | Dobroševići | 11 | 725.300 | 65.900 | A |
| 8a1ef45908a7fff | Novi Grad Sarajevo | Alipašin Most II | 159 | 10,495.400 | 66.000 | A |
| 8a1ef459084ffff | Novi Grad Sarajevo | Buća Potok | 39 | 2,576.000 | 66.100 | A |
| 8a1ef458234ffff | Stari Grad Sarajevo | Logavina | 96 | 6,345.600 | 66.100 | A |
| 8a1ef4591d87fff | Novo Sarajevo | Malta | 47 | 3,108.400 | 66.100 | B |
| 8a1ef4582427fff | Centar Sarajevo | Koševsko Brdo | 71 | 4,696.100 | 66.100 | B |
| 8a1ea92cb94ffff | Novi Grad Sarajevo | Briješće | 13 | 861.600 | 66.300 | A |
| 8a1ef4596c4ffff | Novi Grad Sarajevo | Briješće | 61 | 4,048.000 | 66.400 | A |
| 8a1ef459c06ffff | Stari Grad Sarajevo | Mahmutovac | 147 | 9,758.000 | 66.400 | A |
| 8a1ef459c507fff | Centar Sarajevo | Soukbunar | 14 | 929.600 | 66.400 | C |
| 8a1ef45907a7fff | Novi Grad Sarajevo | Švrakino Selo I | 85 | 5,647.800 | 66.400 | A |
| 8a1ef45834dffff | Stari Grad Sarajevo | Kovači | 50 | 3,325.300 | 66.500 | A |
| 8a1ef459011ffff | Novi Grad Sarajevo | Alipašin Most III | 845 | 56,233.100 | 66.500 | A |
| 8a1ef4583047fff | Stari Grad Sarajevo | Mošćanica | 16 | 1,065.000 | 66.600 | A |
| 8a1ef45960affff | Novi Grad Sarajevo | Briješće | 14 | 933.100 | 66.700 | A |
| 8a1ef4594c17fff | Novi Grad Sarajevo | Zabrđe | 29 | 1,934.000 | 66.700 | A |
| 8a1ef459c0a7fff | Stari Grad Sarajevo | Širokača | 44 | 2,938.300 | 66.800 | A |
| 8a1ef459289ffff | Novi Grad Sarajevo | Dobrinja A | 480 | 32,079.500 | 66.800 | A |
| 8a1ef4590737fff | Novi Grad Sarajevo | Švrakino Selo I | 106 | 7,090.000 | 66.900 | A |
| 8a1ef459dca7fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 14 | 937.100 | 66.900 | A |
| 8a1ef458249ffff | Centar Sarajevo | Crni Vrh-Gorica | 135 | 9,040.000 | 67.000 | B |
| 8a1ef4582517fff | Novo Sarajevo | Velešići | 175 | 11,733.600 | 67.000 | B |
| 8a1ef4590727fff | Novi Grad Sarajevo | Švrakino Selo I | 107 | 7,174.800 | 67.100 | A |
| 8a1ef459046ffff | Novi Grad Sarajevo | Švrakino Selo I | 106 | 7,110.100 | 67.100 | A |
| 8a1ef459039ffff | Novi Grad Sarajevo | Aneks | 157 | 10,541.300 | 67.100 | A |
| 8a1ea92c94b7fff | Novi Grad Sarajevo | Briješće | 15 | 1,007.800 | 67.200 | A |
| 8a1ea92c960ffff | Novi Grad Sarajevo | Briješće | 87 | 5,845.500 | 67.200 | A |
| 8a1ef45946effff | Novi Grad Sarajevo | Buća Potok | 26 | 1,749.100 | 67.300 | A |
| 8a1ef4590777fff | Novi Grad Sarajevo | Švrakino Selo III | 119 | 8,011.000 | 67.300 | A |
| 8a1ef459c24ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 10 | 673.600 | 67.400 | A |
| 8a1ef4583537fff | Stari Grad Sarajevo | Medrese | 114 | 7,681.000 | 67.400 | A |
| 8a1ef45908cffff | Novo Sarajevo | Kvadrant | 33 | 2,224.100 | 67.400 | B |
| 8a1ea92c9547fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 124 | 8,366.200 | 67.500 | A |
| 8a1ea92c9857fff | Novi Grad Sarajevo | Zabrđe | 81 | 5,465.500 | 67.500 | A |
| 8a1ef459076ffff | Novi Grad Sarajevo | Aneks | 147 | 9,934.200 | 67.600 | A |
| 8a1ef4586607fff | Centar Sarajevo | Šip | 48 | 3,245.000 | 67.600 | B |
| 8a1ef4590d1ffff | Novi Grad Sarajevo | Alipašin Most I | 98 | 6,625.500 | 67.600 | A |
| 8a1ea92c96c7fff | Novi Grad Sarajevo | Briješće | 92 | 6,233.100 | 67.800 | A |
| 8a1ef459c017fff | Stari Grad Sarajevo | Širokača | 47 | 3,186.000 | 67.800 | A |
| 8a1ef459c567fff | Stari Grad Sarajevo | Širokača | 28 | 1,900.300 | 67.900 | A |
| 8a1ef4596067fff | Novi Grad Sarajevo | Briješće | 153 | 10,388.800 | 67.900 | A |
| 8a1ef45919b7fff | Novo Sarajevo | Pofalići I | 18 | 1,222.400 | 67.900 | B |
| 8a1ef45907affff | Novi Grad Sarajevo | Švrakino Selo I | 56 | 3,803.400 | 67.900 | A |
| 8a1ef4590227fff | Novi Grad Sarajevo | Staro Hrasno | 298 | 20,239.800 | 67.900 | A |
| 8a1ef45962b7fff | Novi Grad Sarajevo | Saraj Polje | 127 | 8,629.100 | 67.900 | A |
| 8a1ef4590367fff | Novo Sarajevo | Hrasno | 220 | 14,952.000 | 68.000 | B |
| 8a1ef4582117fff | Centar Sarajevo | Koševsko Brdo | 96 | 6,530.800 | 68.000 | B |
| 8a1ef459619ffff | Novi Grad Sarajevo | Briješće | 23 | 1,565.600 | 68.100 | A |
| 8a1ea92c948ffff | Novi Grad Sarajevo | Briješće | 24 | 1,634.500 | 68.100 | A |
| 8a1ea92c96b7fff | Novi Grad Sarajevo | Briješće | 70 | 4,767.700 | 68.100 | A |
| 8a1ef4583987fff | Stari Grad Sarajevo | Sedrenik | 12 | 818.400 | 68.200 | A |
| 8a1ea92c836ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 11 | 750.700 | 68.200 | A |
| 8a1ef4583547fff | Stari Grad Sarajevo | Sumbuluša | 70 | 4,779.000 | 68.300 | A |
| 8a1ef459cb37fff | Stari Grad Sarajevo | Bistrik | 152 | 10,397.600 | 68.400 | A |
| 8a1ef459606ffff | Novi Grad Sarajevo | Saraj Polje | 33 | 2,259.600 | 68.500 | A |
| 8a1ef4592a67fff | Novi Grad Sarajevo | Švrakino Selo II | 11 | 753.400 | 68.500 | A |
| 8a1ef458259ffff | Novo Sarajevo | Velešići | 25 | 1,713.100 | 68.500 | B |
| 8a1ef4582507fff | Novo Sarajevo | Velešići | 161 | 11,040.900 | 68.600 | B |
| 8a1ef4590067fff | Novo Sarajevo | Čengić Vila II | 268 | 18,379.500 | 68.600 | B |
| 8a1ef45914e7fff | Novo Sarajevo | Vraca | 19 | 1,303.300 | 68.600 | B |
| 8a1ef4592897fff | Novi Grad Sarajevo | Dobrinja A | 519 | 35,642.300 | 68.700 | A |
| 8a1ef459602ffff | Novi Grad Sarajevo | Briješće | 155 | 10,659.600 | 68.800 | A |
| 8a1ef4591d27fff | Novo Sarajevo | Pofalići II | 307 | 21,129.600 | 68.800 | B |
| 8a1ef4583017fff | Stari Grad Sarajevo | Mošćanica | 19 | 1,307.900 | 68.800 | A |
| 8a1ea92c8537fff | Novi Grad Sarajevo | Dobroševići | 12 | 826.800 | 68.900 | A |
| 8a1ef4582cd7fff | Novo Sarajevo | Velešići | 78 | 5,375.200 | 68.900 | B |
| 8a1ef4582d67fff | Centar Sarajevo | Koševsko Brdo | 44 | 3,032.600 | 68.900 | B |
| 8a1ea92c9707fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 28 | 1,930.600 | 68.900 | A |
| 8a1ef4596047fff | Novi Grad Sarajevo | Saraj Polje | 95 | 6,550.900 | 69.000 | A |
| 8a1ef4590c9ffff | Novi Grad Sarajevo | Alipašino Polje AI | 34 | 2,345.400 | 69.000 | A |
| 8a1ea92c9977fff | Novi Grad Sarajevo | Zabrđe | 21 | 1,448.900 | 69.000 | A |
| 8a1ef459c127fff | Stari Grad Sarajevo | Širokača | 88 | 6,073.400 | 69.000 | A |
| 8a1ef459c0cffff | Stari Grad Sarajevo | Toka-Džeka | 43 | 2,967.800 | 69.000 | A |
| 8a1ef459ca27fff | Stari Grad Sarajevo | Babića bašča | 105 | 7,249.400 | 69.000 | A |
| 8a1ef4590717fff | Novi Grad Sarajevo | Švrakino Selo I | 122 | 8,424.600 | 69.100 | A |
| 8a1ef459664ffff | Novi Grad Sarajevo | Saraj Polje | 451 | 31,162.300 | 69.100 | A |
| 8a1ef45921b7fff | Novi Grad Sarajevo | Dobrinja D | 135 | 9,330.600 | 69.100 | A |
| 8a1ea92c9417fff | Novi Grad Sarajevo | Briješće | 181 | 12,528.300 | 69.200 | A |
| 8a1ea92cc0e7fff | Novi Grad Sarajevo | Dobroševići | 10 | 692.600 | 69.300 | A |
| 8a1ef4582687fff | Centar Sarajevo | Marijin Dvor | 98 | 6,790.500 | 69.300 | B |
| 8a1ef459009ffff | Novi Grad Sarajevo | Švrakino Selo I | 147 | 10,193.500 | 69.300 | A |
| 8a1ef4583c0ffff | Stari Grad Sarajevo | Sedrenik | 53 | 3,675.300 | 69.300 | A |
| 8a1ea92c811ffff | Novi Grad Sarajevo | Dobroševići | 14 | 970.900 | 69.400 | A |
| 8a1ef4590117fff | Novi Grad Sarajevo | Alipašin Most III | 575 | 39,937.700 | 69.500 | A |
| 8a1ea92c9b77fff | Novi Grad Sarajevo | Zabrđe | 20 | 1,392.500 | 69.600 | A |
| 8a1ef4590c57fff | Novi Grad Sarajevo | Alipašin Most III | 543 | 37,836.500 | 69.700 | A |
| 8a1ea92c998ffff | Novi Grad Sarajevo | Zabrđe | 11 | 766.500 | 69.700 | A |
| 8a1ef4595407fff | Novi Grad Sarajevo | Dolac | 15 | 1,045.300 | 69.700 | A |
| 8a1ef4590d0ffff | Novi Grad Sarajevo | Alipašin Most II | 70 | 4,880.800 | 69.700 | A |
| 8a1ef459055ffff | Novi Grad Sarajevo | Švrakino Selo I | 42 | 2,929.100 | 69.700 | A |
| 8a1ea92c91affff | Novi Grad Sarajevo | Naselje heroja Sokolje | 58 | 4,047.900 | 69.800 | A |
| 8a1ef45928b7fff | Novi Grad Sarajevo | Dobrinja A | 439 | 30,657.400 | 69.800 | A |
| 8a1ea92cc8a7fff | Novi Grad Sarajevo | Dobroševići | 10 | 698.500 | 69.800 | A |
| 8a1ef4583a1ffff | Stari Grad Sarajevo | Mošćanica | 13 | 908.200 | 69.900 | A |
| 8a1ef459cb27fff | Stari Grad Sarajevo | Kovači | 61 | 4,262.800 | 69.900 | A |
| 8a1ef4590887fff | Novi Grad Sarajevo | Alipašin Most II | 86 | 6,016.900 | 70.000 | A |
| 8a1ef45b2587fff | Novi Grad Sarajevo | Zabrđe | 11 | 769.700 | 70.000 | A |
| 8a1ef4596a5ffff | Novi Grad Sarajevo | Alipašin Most I | 118 | 8,257.600 | 70.000 | A |
| 8a1ef45b2cdffff | Novi Grad Sarajevo | Reljevo | 39 | 2,729.400 | 70.000 | A |
| 8a1ef4591a8ffff | Novo Sarajevo | Kovačići | 352 | 24,646.200 | 70.000 | B |
| 8a1ef4582177fff | Centar Sarajevo | Park-Višnjik | 57 | 4,000.400 | 70.200 | B |
| 8a1ef4591017fff | Novo Sarajevo | Grbavica I | 313 | 21,982.300 | 70.200 | B |
| 8a1ef4591c57fff | Novo Sarajevo | Grbavica II | 240 | 16,894.100 | 70.400 | B |
| 8a1ef459dc97fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 17 | 1,196.700 | 70.400 | A |
| 8a1ef459cba7fff | Stari Grad Sarajevo | Bistrik | 131 | 9,225.100 | 70.400 | A |
| 8a1ef4583187fff | Stari Grad Sarajevo | Sedrenik | 28 | 1,972.500 | 70.400 | A |
| 8a1ea92c9bb7fff | Novi Grad Sarajevo | Zabrđe | 46 | 3,242.300 | 70.500 | A |
| 8a1ea92c830ffff | Novi Grad Sarajevo | Briješće | 81 | 5,716.500 | 70.600 | A |
| 8a1ef4595aa7fff | Novo Sarajevo | Velešići | 11 | 777.500 | 70.700 | B |
| 8a1ef4596297fff | Novi Grad Sarajevo | Saraj Polje | 553 | 39,097.600 | 70.700 | A |
| 8a1ef459666ffff | Novi Grad Sarajevo | Saraj Polje | 545 | 38,536.600 | 70.700 | A |
| 8a1ef4583ad7fff | Stari Grad Sarajevo | Mošćanica | 10 | 707.400 | 70.700 | A |
| 8a1ef459002ffff | Novi Grad Sarajevo | Alipašin Most III | 350 | 24,778.200 | 70.800 | A |
| 8a1ef458620ffff | Centar Sarajevo | Betanija | 13 | 920.500 | 70.800 | B |
| 8a1ef4582477fff | Centar Sarajevo | Ciglane | 69 | 4,886.700 | 70.800 | B |
| 8a1ef4596037fff | Novi Grad Sarajevo | Briješće | 51 | 3,612.000 | 70.800 | A |
| 8a1ef4580d77fff | Centar Sarajevo | Pionirska Dolina | 10 | 708.300 | 70.800 | B |
| 8a1ef4591da7fff | Novo Sarajevo | Malta | 368 | 26,079.300 | 70.900 | B |
| 8a1ef458340ffff | Stari Grad Sarajevo | Vratnik | 118 | 8,365.500 | 70.900 | A |
| 8a1ea92cc607fff | Novi Grad Sarajevo | Dobroševići | 10 | 709.300 | 70.900 | A |
| 8a1ef4590daffff | Novi Grad Sarajevo | Alipašin Most I | 31 | 2,204.100 | 71.100 | A |
| 8a1ef4582827fff | Centar Sarajevo | Betanija | 35 | 2,488.700 | 71.100 | B |
| 8a1ef4595257fff | Novo Sarajevo | Velešići | 126 | 8,964.500 | 71.100 | B |
| 8a1ef4591a1ffff | Centar Sarajevo | Marijin Dvor | 73 | 5,194.800 | 71.200 | B |
| 8a1ef4592c27fff | Novi Grad Sarajevo | Dobrinja A | 108 | 7,685.400 | 71.200 | A |
| 8a1ea92c8b87fff | Novi Grad Sarajevo | Dobroševići | 28 | 1,993.000 | 71.200 | A |
| 8a1ef4586617fff | Centar Sarajevo | Šip | 45 | 3,205.400 | 71.200 | B |
| 8a1ea92c9a9ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 13 | 928.000 | 71.400 | A |
| 8a1ef459cb8ffff | Stari Grad Sarajevo | Bistrik | 127 | 9,067.400 | 71.400 | A |
| 8a1ef459c8dffff | Stari Grad Sarajevo | Bistrik | 108 | 7,712.400 | 71.400 | A |
| 8a1ef4592567fff | Novi Grad Sarajevo | Dobrinja B | 243 | 17,357.500 | 71.400 | A |
| 8a1ef4592a77fff | Novi Grad Sarajevo | Švrakino Selo II | 12 | 857.200 | 71.400 | A |
| 8a1ef459c107fff | Stari Grad Sarajevo | Širokača | 87 | 6,217.900 | 71.500 | A |
| 8a1ea92cd1b7fff | Novi Grad Sarajevo | Dobroševići | 11 | 786.500 | 71.500 | A |
| 8a1ef459502ffff | Novo Sarajevo | Pofalići II | 11 | 787.000 | 71.500 | B |
| 8a1ef4582b6ffff | Centar Sarajevo | Hrastovi-Mrkovići | 22 | 1,574.200 | 71.600 | B |
| 8a1ef45939b7fff | Novo Sarajevo | Hrasno Brdo | 15 | 1,073.700 | 71.600 | B |
| 8a1ea92cc187fff | Novi Grad Sarajevo | Dobroševići | 17 | 1,217.800 | 71.600 | A |
| 8a1ef4583cb7fff | Stari Grad Sarajevo | Medrese | 96 | 6,880.500 | 71.700 | A |
| 8a1ef459038ffff | Novi Grad Sarajevo | Aneks | 66 | 4,732.900 | 71.700 | A |
| 8a1ef4596a37fff | Novi Grad Sarajevo | Alipašin Most I | 33 | 2,374.000 | 71.900 | A |
| 8a1ef4592b77fff | Novi Grad Sarajevo | Švrakino Selo II | 19 | 1,368.500 | 72.000 | A |
| 8a1ea92cd427fff | Novi Grad Sarajevo | Dobroševići | 34 | 2,449.900 | 72.100 | A |
| 8a1ea92c8177fff | Novi Grad Sarajevo | Dobroševići | 24 | 1,729.800 | 72.100 | A |
| 8a1ef45910b7fff | Novo Sarajevo | Vraca | 278 | 20,073.900 | 72.200 | B |
| 8a1ef459c0e7fff | Stari Grad Sarajevo | Toka-Džeka | 50 | 3,619.400 | 72.400 | A |
| 8a1ef459575ffff | Novo Sarajevo | Pofalići I | 73 | 5,288.000 | 72.400 | B |
| 8a1ea92cd197fff | Novi Grad Sarajevo | Dobroševići | 15 | 1,086.900 | 72.500 | A |
| 8a1ef459ccb7fff | Centar Sarajevo | Soukbunar | 45 | 3,264.500 | 72.500 | B |
| 8a1ef45b2507fff | Novi Grad Sarajevo | Zabrđe | 26 | 1,886.300 | 72.600 | A |
| 8a1ef458291ffff | Centar Sarajevo | Betanija | 11 | 798.300 | 72.600 | B |
| 8a1ef4583577fff | Stari Grad Sarajevo | Medrese | 79 | 5,734.600 | 72.600 | A |
| 8a1ef459078ffff | Novi Grad Sarajevo | Švrakino Selo I | 91 | 6,607.100 | 72.600 | A |
| 8a1ea92cd247fff | Novi Grad Sarajevo | Reljevo | 13 | 945.700 | 72.700 | A |
| 8a1ef459214ffff | Novi Grad Sarajevo | Dobrinja C | 89 | 6,475.300 | 72.800 | A |
| 8a1ef45824e7fff | Centar Sarajevo | Koševsko Brdo | 59 | 4,295.200 | 72.800 | B |
| 8a1ef4596187fff | Novi Grad Sarajevo | Briješće | 56 | 4,078.500 | 72.800 | A |
| 8a1ea92cd2affff | Novi Grad Sarajevo | Zabrđe | 237 | 17,262.600 | 72.800 | A |
| 8a1ef4583ccffff | Stari Grad Sarajevo | Sumbuluša | 65 | 4,743.900 | 73.000 | A |
| 8a1ef4582527fff | Novo Sarajevo | Velešići | 268 | 19,580.700 | 73.100 | B |
| 8a1ef459409ffff | Novi Grad Sarajevo | Alipašin Most I | 10 | 730.700 | 73.100 | A |
| 8a1ef458644ffff | Centar Sarajevo | Šip | 38 | 2,778.700 | 73.100 | B |
| 8a1ef4583567fff | Stari Grad Sarajevo | Sumbuluša | 62 | 4,536.600 | 73.200 | A |
| 8a1ef4596a0ffff | Novi Grad Sarajevo | Alipašin Most I | 36 | 2,635.800 | 73.200 | A |
| 8a1ea92ea6cffff | Novi Grad Sarajevo | Dobroševići | 12 | 879.100 | 73.300 | A |
| 8a1ef45946c7fff | Novi Grad Sarajevo | Alipašin Most II | 107 | 7,839.700 | 73.300 | A |
| 8a1ea92cca27fff | Novi Grad Sarajevo | Dobroševići | 15 | 1,099.200 | 73.300 | A |
| 8a1ea92c8cc7fff | Novi Grad Sarajevo | Dobroševići | 20 | 1,466.500 | 73.300 | A |
| 8a1ef4590707fff | Novi Grad Sarajevo | Švrakino Selo I | 93 | 6,822.800 | 73.400 | A |
| 8a1ea92c8c07fff | Novi Grad Sarajevo | Dobroševići | 20 | 1,467.300 | 73.400 | A |
| 8a1ef459015ffff | Novo Sarajevo | Čengić Vila II | 314 | 23,047.000 | 73.400 | B |
| 8a1ea92c8b97fff | Novi Grad Sarajevo | Dobroševići | 58 | 4,262.200 | 73.500 | A |
| 8a1ea92c9027fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 10 | 735.400 | 73.500 | A |
| 8a1ea92c8daffff | Novi Grad Sarajevo | Dobroševići | 18 | 1,325.500 | 73.600 | A |
| 8a1ef459080ffff | Novi Grad Sarajevo | Buća Potok | 55 | 4,054.900 | 73.700 | A |
| 8a1ef4592577fff | Novi Grad Sarajevo | Dobrinja B | 33 | 2,433.700 | 73.700 | A |
| 8a1ea92c8d27fff | Novi Grad Sarajevo | Dobroševići | 48 | 3,540.400 | 73.800 | A |
| 8a1ef45952cffff | Novo Sarajevo | Pofalići I | 31 | 2,287.100 | 73.800 | B |
| 8a1ef459c047fff | Stari Grad Sarajevo | Toka-Džeka | 80 | 5,909.800 | 73.900 | A |
| 8a1ea92c8167fff | Novi Grad Sarajevo | Dobroševići | 13 | 960.500 | 73.900 | A |
| 8a1ef45807affff | Centar Sarajevo | Hrastovi-Mrkovići | 15 | 1,108.900 | 73.900 | B |
| 8a1ef458208ffff | Centar Sarajevo | Park-Višnjik | 63 | 4,658.000 | 73.900 | B |
| 8a1ef4583cc7fff | Stari Grad Sarajevo | Medrese | 78 | 5,768.500 | 74.000 | A |
| 8a1ef459cb97fff | Stari Grad Sarajevo | Bistrik | 147 | 10,899.600 | 74.100 | A |
| 8a1ef45901affff | Novi Grad Sarajevo | Alipašin Most III | 717 | 53,167.700 | 74.200 | A |
| 8a1ef459569ffff | Novo Sarajevo | Pofalići II | 180 | 13,358.600 | 74.200 | B |
| 8a1ef458341ffff | Stari Grad Sarajevo | Kovači | 62 | 4,603.000 | 74.200 | A |
| 8a1ef4595687fff | Novo Sarajevo | Pofalići II | 35 | 2,599.600 | 74.300 | B |
| 8a1ef45910cffff | Novo Sarajevo | Gornji Kovačići | 47 | 3,492.400 | 74.300 | B |
| 8a1ea92cca37fff | Novi Grad Sarajevo | Dobroševići | 11 | 819.000 | 74.500 | A |
| 8a1ef4590787fff | Novi Grad Sarajevo | Švrakino Selo I | 61 | 4,542.700 | 74.500 | A |
| 8a1ef4582d4ffff | Centar Sarajevo | Koševsko Brdo | 51 | 3,799.500 | 74.500 | B |
| 8a1ef45966dffff | Novi Grad Sarajevo | Saraj Polje | 19 | 1,418.100 | 74.600 | A |
| 8a1ef459cc17fff | Centar Sarajevo | Soukbunar | 52 | 3,882.300 | 74.700 | B |
| 8a1ef459c117fff | Stari Grad Sarajevo | Širokača | 90 | 6,722.200 | 74.700 | A |
| 8a1ef4591aeffff | Centar Sarajevo | Skenderija-Podtekija | 54 | 4,034.600 | 74.700 | B |
| 8a1ef45904e7fff | Novi Grad Sarajevo | Švrakino Selo II | 34 | 2,541.500 | 74.800 | A |
| 8a1ef45919a7fff | Novo Sarajevo | Pofalići I | 24 | 1,796.600 | 74.900 | B |
| 8a1ef4594717fff | Novi Grad Sarajevo | Alipašin Most I | 23 | 1,724.500 | 75.000 | A |
| 8a1ea92c970ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 129 | 9,681.500 | 75.100 | A |
| 8a1ef4595707fff | Novo Sarajevo | Pofalići II | 155 | 11,653.900 | 75.200 | B |
| 8a1ef458648ffff | Centar Sarajevo | Šip | 14 | 1,053.200 | 75.200 | B |
| 8a1ef459155ffff | Novo Sarajevo | Vraca | 206 | 15,500.200 | 75.200 | B |
| 8a1ef4596aeffff | Novi Grad Sarajevo | Alipašin Most I | 44 | 3,314.000 | 75.300 | A |
| 8a1ef459604ffff | Novi Grad Sarajevo | Saraj Polje | 303 | 22,832.400 | 75.400 | A |
| 8a1ef45844cffff | Centar Sarajevo | Betanija | 10 | 753.700 | 75.400 | B |
| 8a1ea92cd74ffff | Novi Grad Sarajevo | Zabrđe | 14 | 1,055.200 | 75.400 | A |
| 8a1ea92c985ffff | Novi Grad Sarajevo | Zabrđe | 76 | 5,730.300 | 75.400 | A |
| 8a1ef4596207fff | Novi Grad Sarajevo | Alipašino Polje AII | 36 | 2,715.800 | 75.400 | A |
| 8a1ef459ca67fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 37 | 2,792.600 | 75.500 | A |
| 8a1ef458440ffff | Centar Sarajevo | Betanija | 10 | 754.900 | 75.500 | B |
| 8a1ef4591337fff | Novo Sarajevo | Gornji Kovačići | 32 | 2,415.600 | 75.500 | B |
| 8a1ef4583d9ffff | Stari Grad Sarajevo | Sedrenik | 75 | 5,662.100 | 75.500 | A |
| 8a1ef4582aeffff | Centar Sarajevo | Hrastovi-Mrkovići | 43 | 3,247.600 | 75.500 | B |
| 8a1ef4590487fff | Novi Grad Sarajevo | Švrakino Selo II | 38 | 2,871.300 | 75.600 | A |
| 8a1ef459dd9ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 31 | 2,343.000 | 75.600 | A |
| 8a1ef4596ae7fff | Novi Grad Sarajevo | Alipašin Most I | 42 | 3,175.300 | 75.600 | A |
| 8a1ef4596b77fff | Novi Grad Sarajevo | Alipašin Most I | 14 | 1,058.800 | 75.600 | A |
| 8a1ef4592c4ffff | Novi Grad Sarajevo | Dobrinja D | 235 | 17,775.300 | 75.600 | A |
| 8a1ef4582cb7fff | Novo Sarajevo | Gornji Velešići | 158 | 11,953.300 | 75.700 | B |
| 8a1ef4594737fff | Novi Grad Sarajevo | Alipašin Most I | 19 | 1,437.600 | 75.700 | A |
| 8a1ef459572ffff | Novo Sarajevo | Pofalići II | 181 | 13,695.200 | 75.700 | B |
| 8a1ef459c34ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 23 | 1,740.800 | 75.700 | A |
| 8a1ea92c9137fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 96 | 7,267.500 | 75.700 | A |
| 8a1ef4586447fff | Centar Sarajevo | Šip | 35 | 2,650.400 | 75.700 | B |
| 8a1ef458314ffff | Stari Grad Sarajevo | Mošćanica | 12 | 908.800 | 75.700 | A |
| 8a1ef459520ffff | Novo Sarajevo | Velešići | 29 | 2,197.800 | 75.800 | B |
| 8a1ef4592d57fff | Novi Grad Sarajevo | Saraj Polje | 144 | 10,933.200 | 75.900 | A |
| 8a1ef45961affff | Novi Grad Sarajevo | Briješće | 76 | 5,778.600 | 76.000 | A |
| 8a1ef4591267fff | Centar Sarajevo | Soukbunar | 30 | 2,281.300 | 76.000 | B |
| 8a1ea92c901ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 139 | 10,571.300 | 76.100 | A |
| 8a1ef45944d7fff | Novi Grad Sarajevo | Alipašin Most I | 32 | 2,437.100 | 76.200 | A |
| 8a1ef45834cffff | Stari Grad Sarajevo | Vratnik | 99 | 7,541.600 | 76.200 | A |
| 8a1ef4583c9ffff | Stari Grad Sarajevo | Medrese | 117 | 8,919.300 | 76.200 | A |
| 8a1ef459ca77fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 60 | 4,598.700 | 76.600 | A |
| 8a1ef4583c37fff | Stari Grad Sarajevo | Sedrenik | 61 | 4,675.400 | 76.600 | A |
| 8a1ef4596a77fff | Novi Grad Sarajevo | Alipašin Most I | 53 | 4,063.100 | 76.700 | A |
| 8a1ef458679ffff | Centar Sarajevo | Šip | 38 | 2,915.800 | 76.700 | B |
| 8a1ef459262ffff | Novi Grad Sarajevo | Dobrinja B | 13 | 998.000 | 76.800 | A |
| 8a1ef4583707fff | Stari Grad Sarajevo | Vratnik | 74 | 5,682.000 | 76.800 | A |
| 8a1ea92c996ffff | Novi Grad Sarajevo | Zabrđe | 18 | 1,382.800 | 76.800 | A |
| 8a1ef4590b97fff | Novo Sarajevo | Kvadrant | 26 | 1,999.500 | 76.900 | B |
| 8a1ef4592327fff | Novi Grad Sarajevo | Dobrinja C | 24 | 1,845.900 | 76.900 | A |
| 8a1ea92cc0c7fff | Novi Grad Sarajevo | Dobroševići | 14 | 1,077.100 | 76.900 | A |
| 8a1ef45910dffff | Novo Sarajevo | Vraca | 23 | 1,769.700 | 76.900 | B |
| 8a1ea92cd747fff | Novi Grad Sarajevo | Zabrđe | 11 | 847.500 | 77.000 | A |
| 8a1ef4596647fff | Novi Grad Sarajevo | Saraj Polje | 205 | 15,794.700 | 77.000 | A |
| 8a1ef4596a17fff | Novi Grad Sarajevo | Alipašin Most I | 48 | 3,701.400 | 77.100 | A |
| 8a1ef459074ffff | Novi Grad Sarajevo | Aneks | 77 | 5,937.900 | 77.100 | A |
| 8a1ef4586b17fff | Centar Sarajevo | Betanija | 10 | 771.200 | 77.100 | B |
| 8a1ef459021ffff | Novi Grad Sarajevo | Staro Hrasno | 84 | 6,477.800 | 77.100 | A |
| 8a1ef458354ffff | Stari Grad Sarajevo | Sumbuluša | 70 | 5,399.100 | 77.100 | A |
| 8a1ef45834effff | Stari Grad Sarajevo | Vratnik | 106 | 8,182.500 | 77.200 | A |
| 8a1ef4583997fff | Stari Grad Sarajevo | Sedrenik | 22 | 1,698.300 | 77.200 | A |
| 8a1ef4592197fff | Novi Grad Sarajevo | Dobrinja B | 224 | 17,300.600 | 77.200 | A |
| 8a1ef45b2597fff | Novi Grad Sarajevo | Zabrđe | 96 | 7,416.600 | 77.300 | A |
| 8a1ef4591567fff | Novo Sarajevo | Grbavica II | 42 | 3,247.500 | 77.300 | B |
| 8a1ef6965a4ffff | Novi Grad Sarajevo | Saraj Polje | 160 | 12,378.800 | 77.400 | A |
| 8a1ef459071ffff | Novi Grad Sarajevo | Švrakino Selo III | 56 | 4,334.800 | 77.400 | A |
| 8a1ef4591447fff | Novo Sarajevo | Vraca | 28 | 2,169.500 | 77.500 | B |
| 8a1ef459574ffff | Novo Sarajevo | Pofalići I | 177 | 13,714.600 | 77.500 | B |
| 8a1ef4590157fff | Novi Grad Sarajevo | Alipašin Most III | 303 | 23,480.400 | 77.500 | A |
| 8a1ef459c007fff | Stari Grad Sarajevo | Toka-Džeka | 63 | 4,883.400 | 77.500 | A |
| 8a1ef4590987fff | Novi Grad Sarajevo | Buća Potok | 70 | 5,426.600 | 77.500 | A |
| 8a1ef4596a07fff | Novi Grad Sarajevo | Alipašin Most I | 53 | 4,109.000 | 77.500 | A |
| 8a1ea92c9c0ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 99 | 7,678.200 | 77.600 | A |
| 8a1ef4596b4ffff | Novi Grad Sarajevo | Alipašin Most I | 135 | 10,471.200 | 77.600 | A |
| 8a1ef45944affff | Novi Grad Sarajevo | Alipašin Most I | 29 | 2,250.300 | 77.600 | A |
| 8a1ea92c9567fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 211 | 16,372.600 | 77.600 | A |
| 8a1ef45b258ffff | Novi Grad Sarajevo | Zabrđe | 12 | 931.200 | 77.600 | A |
| 8a1ea92c9ccffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 169 | 13,129.000 | 77.700 | A |
| 8a1ef4592b27fff | Novi Grad Sarajevo | Švrakino Selo II | 24 | 1,865.100 | 77.700 | A |
| 8a1ef458209ffff | Centar Sarajevo | Ciglane | 95 | 7,384.200 | 77.700 | B |
| 8a1ef459c8d7fff | Stari Grad Sarajevo | Širokača | 94 | 7,307.700 | 77.700 | A |
| 8a1ef4582597fff | Novo Sarajevo | Pofalići I | 30 | 2,334.100 | 77.800 | B |
| 8a1ef4583507fff | Stari Grad Sarajevo | Medrese | 130 | 10,116.400 | 77.800 | A |
| 8a1ef459c187fff | Stari Grad Sarajevo | Širokača | 54 | 4,204.800 | 77.900 | A |
| 8a1ef4591047fff | Novo Sarajevo | Grbavica I | 256 | 19,945.200 | 77.900 | B |
| 8a1ef45832a7fff | Stari Grad Sarajevo | Mošćanica | 10 | 779.200 | 77.900 | A |
| 8a1ef4583917fff | Stari Grad Sarajevo | Sedrenik | 10 | 779.400 | 77.900 | A |
| 8a1ef4582b8ffff | Centar Sarajevo | Breka | 51 | 3,981.600 | 78.100 | B |
| 8a1ef459c80ffff | Stari Grad Sarajevo | Baščaršija | 91 | 7,112.000 | 78.200 | A |
| 8a1ef4591347fff | Centar Sarajevo | Soukbunar | 40 | 3,126.500 | 78.200 | B |
| 8a1ef45b2cf7fff | Novi Grad Sarajevo | Reljevo | 11 | 860.400 | 78.200 | A |
| 8a1ef45805affff | Centar Sarajevo | Pionirska Dolina | 33 | 2,582.900 | 78.300 | B |
| 8a1ef4591717fff | Novo Sarajevo | Vraca | 17 | 1,331.200 | 78.300 | B |
| 8a1ef459c027fff | Stari Grad Sarajevo | Toka-Džeka | 84 | 6,578.300 | 78.300 | A |
| 8a1ea92c8137fff | Novi Grad Sarajevo | Dobroševići | 118 | 9,241.000 | 78.300 | A |
| 8a1ef459c99ffff | Centar Sarajevo | Trg oslobođenja-Centar | 65 | 5,093.500 | 78.400 | B |
| 8a1ef459cda7fff | Centar Sarajevo | Skenderija-Podtekija | 53 | 4,153.700 | 78.400 | B |
| 8a1ef4592547fff | Novi Grad Sarajevo | Dobrinja B | 62 | 4,865.500 | 78.500 | A |
| 8a1ef458236ffff | Stari Grad Sarajevo | Sedrenik | 82 | 6,439.300 | 78.500 | A |
| 8a1ef4594207fff | Novi Grad Sarajevo | Dolac | 61 | 4,791.300 | 78.500 | A |
| 8a1ef4592c07fff | Novi Grad Sarajevo | Dobrinja A | 139 | 10,918.800 | 78.600 | A |
| 8a1ef459cb57fff | Stari Grad Sarajevo | Babića bašča | 107 | 8,418.800 | 78.700 | A |
| 8a1ef45821affff | Centar Sarajevo | Ciglane | 109 | 8,580.100 | 78.700 | B |
| 8a1ef459ca07fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 85 | 6,692.700 | 78.700 | A |
| 8a1ef459072ffff | Novi Grad Sarajevo | Švrakino Selo III | 68 | 5,356.300 | 78.800 | A |
| 8a1ef459052ffff | Novi Grad Sarajevo | Švrakino Selo II | 45 | 3,545.300 | 78.800 | A |
| 8a1ef45b2c8ffff | Novi Grad Sarajevo | Reljevo | 28 | 2,206.800 | 78.800 | A |
| 8a1ef45902b7fff | Novi Grad Sarajevo | Aneks | 88 | 6,945.900 | 78.900 | A |
| 8a1ef4591db7fff | Novo Sarajevo | Čengić Vila I | 46 | 3,631.300 | 78.900 | B |
| 8a1ef459cb67fff | Stari Grad Sarajevo | Vratnik | 105 | 8,296.600 | 79.000 | A |
| 8a1ef4592d67fff | Novi Grad Sarajevo | Saraj Polje | 72 | 5,691.300 | 79.000 | A |
| 8a1ef4591af7fff | Novo Sarajevo | Kovačići | 65 | 5,138.800 | 79.100 | B |
| 8a1ef459012ffff | Novi Grad Sarajevo | Alipašin Most III | 56 | 4,430.100 | 79.100 | A |
| 8a1ef4583c1ffff | Stari Grad Sarajevo | Sedrenik | 70 | 5,544.700 | 79.200 | A |
| 8a1ef458376ffff | Stari Grad Sarajevo | Mošćanica | 11 | 871.400 | 79.200 | A |
| 8a1ef4594607fff | Novi Grad Sarajevo | Alipašin Most I | 43 | 3,406.800 | 79.200 | A |
| 8a1ef459188ffff | Novo Sarajevo | Željeznička | 37 | 2,933.400 | 79.300 | B |
| 8a1ef4583ca7fff | Stari Grad Sarajevo | Medrese | 86 | 6,823.500 | 79.300 | A |
| 8a1ef4590d17fff | Novi Grad Sarajevo | Alipašin Most I | 59 | 4,681.500 | 79.300 | A |
| 8a1ef4592db7fff | Novi Grad Sarajevo | Dobrinja A | 126 | 9,998.300 | 79.400 | A |
| 8a1ef4583457fff | Stari Grad Sarajevo | Vratnik | 119 | 9,447.000 | 79.400 | A |
| 8a1ef4596a1ffff | Novi Grad Sarajevo | Alipašin Most I | 49 | 3,892.800 | 79.400 | A |
| 8a1ef45958b7fff | Novi Grad Sarajevo | Dolac | 11 | 874.300 | 79.500 | A |
| 8a1ef458058ffff | Centar Sarajevo | Pionirska Dolina | 35 | 2,786.000 | 79.600 | B |
| 8a1ef459618ffff | Novi Grad Sarajevo | Briješće | 57 | 4,539.700 | 79.600 | A |
| 8a1ef4583887fff | Stari Grad Sarajevo | Sedrenik | 33 | 2,628.700 | 79.700 | A |
| 8a1ef459dda7fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 35 | 2,789.000 | 79.700 | A |
| 8a1ea92c9d6ffff | Novi Grad Sarajevo | Zabrđe | 11 | 876.900 | 79.700 | A |
| 8a1ef4592a37fff | Novi Grad Sarajevo | Švrakino Selo II | 19 | 1,515.100 | 79.700 | A |
| 8a1ef4596b8ffff | Novi Grad Sarajevo | Alipašin Most I | 20 | 1,595.900 | 79.800 | A |
| 8a1ef458352ffff | Stari Grad Sarajevo | Medrese | 101 | 8,065.400 | 79.900 | A |
| 8a1ef459446ffff | Novi Grad Sarajevo | Alipašin Most I | 17 | 1,358.000 | 79.900 | A |
| 8a1ef4596667fff | Novi Grad Sarajevo | Saraj Polje | 325 | 25,963.000 | 79.900 | A |
| 8a1ef4594747fff | Novi Grad Sarajevo | Alipašin Most I | 35 | 2,797.100 | 79.900 | A |
| 8a1ef459560ffff | Novo Sarajevo | Pofalići I | 38 | 3,036.800 | 79.900 | B |
| 8a1ef4582db7fff | Novo Sarajevo | Velešići | 19 | 1,518.400 | 79.900 | B |
| 8a1ef45834e7fff | Stari Grad Sarajevo | Vratnik | 88 | 7,041.400 | 80.000 | A |
| 8a1ef4596b5ffff | Novi Grad Sarajevo | Alipašin Most I | 62 | 4,962.800 | 80.000 | A |
| 8a1ef4595797fff | Novo Sarajevo | Pofalići II | 35 | 2,802.000 | 80.100 | B |
| 8a1ea92c9817fff | Novi Grad Sarajevo | Zabrđe | 12 | 961.000 | 80.100 | A |
| 8a1ef458271ffff | Centar Sarajevo | Džidžikovac-Koševo I | 79 | 6,332.800 | 80.200 | B |
| 8a1ea92c8357fff | Novi Grad Sarajevo | Briješće | 62 | 4,974.200 | 80.200 | A |
| 8a1ef458226ffff | Stari Grad Sarajevo | Logavina | 117 | 9,388.400 | 80.200 | A |
| 8a1ef45944c7fff | Novi Grad Sarajevo | Alipašin Most I | 45 | 3,613.500 | 80.300 | A |
| 8a1ef4583797fff | Stari Grad Sarajevo | Vratnik | 100 | 8,038.400 | 80.400 | A |
| 8a1ef4590217fff | Novi Grad Sarajevo | Staro Hrasno | 91 | 7,316.000 | 80.400 | A |
| 8a1ef4582c17fff | Novo Sarajevo | Gornji Velešići | 66 | 5,307.400 | 80.400 | B |
| 8a1ea92c9827fff | Novi Grad Sarajevo | Zabrđe | 31 | 2,493.200 | 80.400 | A |
| 8a1ef45908dffff | Novi Grad Sarajevo | Alipašin Most III | 46 | 3,700.300 | 80.400 | A |
| 8a1ea92ceb6ffff | Novi Grad Sarajevo | Dobroševići | 10 | 804.600 | 80.500 | A |
| 8a1ef4594447fff | Novi Grad Sarajevo | Alipašin Most I | 40 | 3,223.600 | 80.600 | A |
| 8a1ef459cbaffff | Stari Grad Sarajevo | Bistrik | 159 | 12,816.000 | 80.600 | A |
| 8a1ef459475ffff | Novi Grad Sarajevo | Dolac | 25 | 2,015.500 | 80.600 | A |
| 8a1ef4583caffff | Stari Grad Sarajevo | Medrese | 102 | 8,229.600 | 80.700 | A |
| 8a1ef4590917fff | Novi Grad Sarajevo | Buća Potok | 168 | 13,576.900 | 80.800 | A |
| 8a1ea92cc10ffff | Novi Grad Sarajevo | Dobroševići | 11 | 889.300 | 80.800 | A |
| 8a1ef4591adffff | Centar Sarajevo | Soukbunar | 68 | 5,501.300 | 80.900 | B |
| 8a1ef45944dffff | Novi Grad Sarajevo | Alipašin Most I | 47 | 3,802.900 | 80.900 | A |
| 8a1ef4596b57fff | Novi Grad Sarajevo | Alipašin Most I | 57 | 4,612.600 | 80.900 | A |
| 8a1ef459064ffff | Novi Grad Sarajevo | Aneks | 56 | 4,532.500 | 80.900 | A |
| 8a1ef45820cffff | Centar Sarajevo | Park-Višnjik | 71 | 5,747.400 | 80.900 | B |
| 8a1ef459cd87fff | Centar Sarajevo | Soukbunar | 56 | 4,535.700 | 81.000 | B |
| 8a1ef459281ffff | Novi Grad Sarajevo | Olimpijsko Selo | 47 | 3,808.400 | 81.000 | A |
| 8a1ef45946affff | Novi Grad Sarajevo | Alipašin Most I | 46 | 3,728.200 | 81.000 | A |
| 8a1ef459564ffff | Novo Sarajevo | Pofalići I | 103 | 8,349.600 | 81.100 | B |
| 8a1ef4594767fff | Novi Grad Sarajevo | Dolac | 22 | 1,784.100 | 81.100 | A |
| 8a1ef4590267fff | Novo Sarajevo | Trg heroja | 175 | 14,192.400 | 81.100 | B |
| 8a1ef4591ca7fff | Novo Sarajevo | Trg heroja | 181 | 14,689.500 | 81.200 | B |
| 8a1ef45b252ffff | Novi Grad Sarajevo | Zabrđe | 28 | 2,272.500 | 81.200 | A |
| 8a1ef4582997fff | Centar Sarajevo | Koševsko Brdo | 35 | 2,841.300 | 81.200 | B |
| 8a1ef4592b8ffff | Novi Grad Sarajevo | Švrakino Selo II | 10 | 811.900 | 81.200 | A |
| 8a1ef45946d7fff | Novi Grad Sarajevo | Buća Potok | 74 | 6,009.600 | 81.200 | A |
| 8a1ef4582c67fff | Centar Sarajevo | Koševsko Brdo | 58 | 4,711.700 | 81.200 | B |
| 8a1ea92c9c2ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 111 | 9,025.400 | 81.300 | A |
| 8a1ef45908affff | Novi Grad Sarajevo | Buća Potok | 85 | 6,913.900 | 81.300 | A |
| 8a1ef4596a2ffff | Novi Grad Sarajevo | Alipašin Most I | 76 | 6,185.200 | 81.400 | A |
| 8a1ef459141ffff | Novo Sarajevo | Vraca | 27 | 2,199.700 | 81.500 | B |
| 8a1ef459066ffff | Novi Grad Sarajevo | Aneks | 92 | 7,498.100 | 81.500 | A |
| 8a1ef4591987fff | Novo Sarajevo | Pofalići I | 41 | 3,342.400 | 81.500 | B |
| 8a1ef4594697fff | Novi Grad Sarajevo | Alipašin Most I | 67 | 5,464.000 | 81.600 | A |
| 8a1ef459444ffff | Novi Grad Sarajevo | Alipašin Most I | 40 | 3,263.700 | 81.600 | A |
| 8a1ef45806cffff | Stari Grad Sarajevo | Sedrenik | 34 | 2,774.800 | 81.600 | A |
| 8a1ef459c12ffff | Stari Grad Sarajevo | Širokača | 110 | 8,981.300 | 81.600 | A |
| 8a1ef45822e7fff | Stari Grad Sarajevo | Logavina | 127 | 10,369.500 | 81.600 | A |
| 8a1ef45b2ceffff | Novi Grad Sarajevo | Reljevo | 22 | 1,796.400 | 81.700 | A |
| 8a1ef459255ffff | Novi Grad Sarajevo | Dobrinja B | 28 | 2,286.700 | 81.700 | A |
| 8a1ef4596a27fff | Novi Grad Sarajevo | Alipašin Most I | 72 | 5,883.400 | 81.700 | A |
| 8a1ef4583c17fff | Stari Grad Sarajevo | Sedrenik | 69 | 5,638.700 | 81.700 | A |
| 8a1ef459c087fff | Stari Grad Sarajevo | Širokača | 48 | 3,923.200 | 81.700 | A |
| 8a1ef45824f7fff | Centar Sarajevo | Koševsko Brdo | 80 | 6,539.200 | 81.700 | B |
| 8a1ef459448ffff | Novi Grad Sarajevo | Alipašin Most I | 48 | 3,925.000 | 81.800 | A |
| 8a1ef4582407fff | Centar Sarajevo | Koševsko Brdo | 72 | 5,889.500 | 81.800 | B |
| 8a1ef459285ffff | Novi Grad Sarajevo | Švrakino Selo II | 18 | 1,473.500 | 81.900 | A |
| 8a1ef4591707fff | Novo Sarajevo | Vraca | 28 | 2,292.600 | 81.900 | B |
| 8a1ef4596b27fff | Novi Grad Sarajevo | Alipašin Most I | 26 | 2,129.800 | 81.900 | A |
| 8a1ef459100ffff | Novo Sarajevo | Grbavica I | 148 | 12,126.500 | 81.900 | B |
| 8a1ef4590d2ffff | Novi Grad Sarajevo | Alipašin Most I | 109 | 8,931.000 | 81.900 | A |
| 8a1ef459cbb7fff | Stari Grad Sarajevo | Bistrik | 169 | 13,853.100 | 82.000 | A |
| 8a1ef458261ffff | Centar Sarajevo | Trg oslobođenja-Centar | 108 | 8,853.500 | 82.000 | B |
| 8a1ef4591087fff | Novo Sarajevo | Vraca | 113 | 9,264.200 | 82.000 | B |
| 8a1ef459611ffff | Novi Grad Sarajevo | Briješće | 27 | 2,213.800 | 82.000 | A |
| 8a1ef45954cffff | Novo Sarajevo | Pofalići II | 32 | 2,624.000 | 82.000 | B |
| 8a1ea92c9197fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 130 | 10,661.900 | 82.000 | A |
| 8a1ef4594477fff | Novi Grad Sarajevo | Alipašin Most I | 33 | 2,706.500 | 82.000 | A |
| 8a1ea92c9887fff | Novi Grad Sarajevo | Zabrđe | 18 | 1,476.400 | 82.000 | A |
| 8a1ef4580597fff | Centar Sarajevo | Pionirska Dolina | 27 | 2,214.800 | 82.000 | B |
| 8a1ef459ca37fff | Stari Grad Sarajevo | Babića bašča | 135 | 11,080.100 | 82.100 | A |
| 8a1ef459029ffff | Novi Grad Sarajevo | Aneks | 100 | 8,214.300 | 82.100 | A |
| 8a1ef459cb07fff | Stari Grad Sarajevo | Babića bašča | 158 | 12,980.400 | 82.200 | A |
| 8a1ef4583c27fff | Stari Grad Sarajevo | Sedrenik | 61 | 5,013.300 | 82.200 | A |
| 8a1ea92eb84ffff | Novi Grad Sarajevo | Reljevo | 13 | 1,069.300 | 82.300 | A |
| 8a1ef4592a9ffff | Novi Grad Sarajevo | Dobrinja C | 42 | 3,456.200 | 82.300 | A |
| 8a1ef459081ffff | Novi Grad Sarajevo | Buća Potok | 84 | 6,919.400 | 82.400 | A |
| 8a1ef4582b2ffff | Centar Sarajevo | Hrastovi-Mrkovići | 35 | 2,883.200 | 82.400 | B |
| 8a1ef4591ce7fff | Novo Sarajevo | Grbavica II | 78 | 6,426.600 | 82.400 | B |
| 8a1ef45839a7fff | Stari Grad Sarajevo | Sedrenik | 11 | 906.800 | 82.400 | A |
| 8a1ef459192ffff | Novo Sarajevo | Pofalići I | 40 | 3,298.500 | 82.500 | B |
| 8a1ef459c557fff | Stari Grad Sarajevo | Širokača | 10 | 825.100 | 82.500 | A |
| 8a1ef458695ffff | Centar Sarajevo | Betanija | 15 | 1,237.900 | 82.500 | B |
| 8a1ef45906b7fff | Novi Grad Sarajevo | Švrakino Selo II | 38 | 3,136.500 | 82.500 | A |
| 8a1ef459cb87fff | Stari Grad Sarajevo | Bistrik | 166 | 13,708.200 | 82.600 | A |
| 8a1ef459462ffff | Novi Grad Sarajevo | Alipašin Most I | 57 | 4,708.000 | 82.600 | A |
| 8a1ef45906c7fff | Novo Sarajevo | Hrasno Brdo | 14 | 1,158.600 | 82.800 | B |
| 8a1ea92c971ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 17 | 1,407.300 | 82.800 | A |
| 8a1ef4582ac7fff | Centar Sarajevo | Hrastovi-Mrkovići | 54 | 4,471.900 | 82.800 | B |
| 8a1ef459c1affff | Stari Grad Sarajevo | Širokača | 82 | 6,791.000 | 82.800 | A |
| 8a1ef459441ffff | Novi Grad Sarajevo | Alipašin Most I | 48 | 3,975.400 | 82.800 | A |
| 8a1ef45907b7fff | Novi Grad Sarajevo | Švrakino Selo II | 68 | 5,635.700 | 82.900 | A |
| 8a1ef4590297fff | Novi Grad Sarajevo | Aneks | 113 | 9,365.200 | 82.900 | A |
| 8a1ef4594727fff | Novi Grad Sarajevo | Alipašin Most I | 27 | 2,239.400 | 82.900 | A |
| 8a1ef4591357fff | Centar Sarajevo | Soukbunar | 28 | 2,322.900 | 83.000 | B |
| 8a1ef458224ffff | Stari Grad Sarajevo | Logavina | 122 | 10,132.100 | 83.100 | A |
| 8a1ea92c982ffff | Novi Grad Sarajevo | Zabrđe | 52 | 4,320.100 | 83.100 | A |
| 8a1ef45920a7fff | Novi Grad Sarajevo | Dobrinja B | 83 | 6,900.400 | 83.100 | A |
| 8a1ef4583c87fff | Stari Grad Sarajevo | Medrese | 107 | 8,897.400 | 83.200 | A |
| 8a1ef4582cc7fff | Centar Sarajevo | Koševsko Brdo | 87 | 7,235.100 | 83.200 | B |
| 8a1ef4594617fff | Novi Grad Sarajevo | Alipašin Most I | 63 | 5,241.200 | 83.200 | A |
| 8a1ef45834b7fff | Stari Grad Sarajevo | Logavina | 146 | 12,150.600 | 83.200 | A |
| 8a1ef6965a77fff | Novi Grad Sarajevo | Saraj Polje | 13 | 1,082.100 | 83.200 | A |
| 8a1ef4596b67fff | Novi Grad Sarajevo | Alipašin Most I | 65 | 5,412.000 | 83.300 | A |
| 8a1ef459020ffff | Novo Sarajevo | Hrasno Brdo | 120 | 9,995.000 | 83.300 | B |
| 8a1ef4595677fff | Novo Sarajevo | Pofalići I | 42 | 3,498.700 | 83.300 | B |
| 8a1ef45b2cc7fff | Novi Grad Sarajevo | Reljevo | 65 | 5,415.200 | 83.300 | A |
| 8a1ef4591ac7fff | Centar Sarajevo | Skenderija-Podtekija | 55 | 4,583.600 | 83.300 | B |
| 8a1ef459cc77fff | Centar Sarajevo | Soukbunar | 50 | 4,167.700 | 83.400 | B |
| 8a1ef4590287fff | Novi Grad Sarajevo | Aneks | 112 | 9,335.900 | 83.400 | A |
| 8a1ef459096ffff | Novi Grad Sarajevo | Dolac | 43 | 3,584.900 | 83.400 | A |
| 8a1ef4590667fff | Novi Grad Sarajevo | Švrakino Selo III | 79 | 6,592.400 | 83.400 | A |
| 8a1ef459460ffff | Novi Grad Sarajevo | Buća Potok | 54 | 4,512.500 | 83.600 | A |
| 8a1ef4595b6ffff | Centar Sarajevo | Šip | 33 | 2,758.200 | 83.600 | B |
| 8a1ef4596b47fff | Novi Grad Sarajevo | Alipašin Most I | 76 | 6,353.100 | 83.600 | A |
| 8a1ef4593907fff | Novi Grad Sarajevo | Aneks | 87 | 7,273.500 | 83.600 | A |
| 8a1ef45944e7fff | Novi Grad Sarajevo | Alipašin Most I | 54 | 4,522.600 | 83.800 | A |
| 8a1ef45908f7fff | Novi Grad Sarajevo | Buća Potok | 97 | 8,130.500 | 83.800 | A |
| 8a1ef459280ffff | Novi Grad Sarajevo | Olimpijsko Selo | 77 | 6,455.600 | 83.800 | A |
| 8a1ef459dd1ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 20 | 1,677.000 | 83.800 | A |
| 8a1ef4582347fff | Centar Sarajevo | Bardakčije | 84 | 7,043.800 | 83.900 | B |
| 8a1ef4595507fff | Novi Grad Sarajevo | Dolac | 16 | 1,342.000 | 83.900 | A |
| 8a1ea92eb85ffff | Novi Grad Sarajevo | Reljevo | 20 | 1,677.700 | 83.900 | A |
| 8a1ef4582daffff | Novo Sarajevo | Gornji Velešići | 26 | 2,181.500 | 83.900 | B |
| 8a1ef45910e7fff | Novo Sarajevo | Vraca | 77 | 6,465.800 | 84.000 | B |
| 8a1ef4590817fff | Novi Grad Sarajevo | Buća Potok | 94 | 7,895.400 | 84.000 | A |
| 8a1ef45820e7fff | Centar Sarajevo | Park-Višnjik | 80 | 6,720.900 | 84.000 | B |
| 8a1ef459cc4ffff | Centar Sarajevo | Soukbunar | 67 | 5,629.400 | 84.000 | B |
| 8a1ef4596a67fff | Novi Grad Sarajevo | Alipašin Most I | 111 | 9,326.600 | 84.000 | A |
| 8a1ef45868e7fff | Centar Sarajevo | Betanija | 10 | 841.400 | 84.100 | B |
| 8a1ef459075ffff | Novi Grad Sarajevo | Švrakino Selo III | 69 | 5,807.000 | 84.200 | A |
| 8a1ef45b2ccffff | Novi Grad Sarajevo | Reljevo | 117 | 9,847.300 | 84.200 | A |
| 8a1ef458269ffff | Centar Sarajevo | Marijin Dvor | 81 | 6,817.900 | 84.200 | B |
| 8a1ea92c9d4ffff | Novi Grad Sarajevo | Zabrđe | 17 | 1,431.000 | 84.200 | A |
| 8a1ef459098ffff | Novi Grad Sarajevo | Buća Potok | 127 | 10,693.700 | 84.200 | A |
| 8a1ea92cd2f7fff | Novi Grad Sarajevo | Zabrđe | 23 | 1,937.300 | 84.200 | A |
| 8a1ea92cc1b7fff | Novi Grad Sarajevo | Dobroševići | 38 | 3,201.600 | 84.300 | A |
| 8a1ef45956affff | Novo Sarajevo | Pofalići II | 39 | 3,287.000 | 84.300 | B |
| 8a1ef459c0effff | Stari Grad Sarajevo | Toka-Džeka | 54 | 4,551.500 | 84.300 | A |
| 8a1ea92c9acffff | Novi Grad Sarajevo | Zabrđe | 12 | 1,011.500 | 84.300 | A |
| 8a1ef459082ffff | Novi Grad Sarajevo | Buća Potok | 93 | 7,840.300 | 84.300 | A |
| 8a1ef459549ffff | Novi Grad Sarajevo | Buća Potok | 87 | 7,334.700 | 84.300 | A |
| 8a1ef459c15ffff | Stari Grad Sarajevo | Toka-Džeka | 102 | 8,601.300 | 84.300 | A |
| 8a1ef4580557fff | Centar Sarajevo | Pionirska Dolina | 17 | 1,433.800 | 84.300 | B |
| 8a1ef4590d37fff | Novi Grad Sarajevo | Alipašin Most I | 103 | 8,687.800 | 84.300 | A |
| 8a1ef459cce7fff | Centar Sarajevo | Soukbunar | 52 | 4,388.000 | 84.400 | B |
| 8a1ef4596a47fff | Novi Grad Sarajevo | Alipašin Most I | 119 | 10,048.100 | 84.400 | A |
| 8a1ef459c3b7fff | Stari Grad Sarajevo | Toka-Džeka | 25 | 2,112.500 | 84.500 | A |
| 8a1ea92eb12ffff | Novi Grad Sarajevo | Reljevo | 15 | 1,268.500 | 84.600 | A |
| 8a1ef458642ffff | Centar Sarajevo | Šip | 25 | 2,114.800 | 84.600 | B |
| 8a1ef459c26ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 14 | 1,184.400 | 84.600 | A |
| 8a1ef4584827fff | Centar Sarajevo | Nahorevo | 10 | 846.100 | 84.600 | B |
| 8a1ef4594777fff | Novi Grad Sarajevo | Alipašin Most I | 63 | 5,334.900 | 84.700 | A |
| 8a1ef4596b6ffff | Novi Grad Sarajevo | Alipašin Most I | 89 | 7,537.300 | 84.700 | A |
| 8a1ef4582c1ffff | Novo Sarajevo | Velešići | 65 | 5,508.100 | 84.700 | B |
| 8a1ef459cb5ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 62 | 5,262.300 | 84.900 | A |
| 8a1ef45947a7fff | Novi Grad Sarajevo | Alipašin Most I | 70 | 5,942.300 | 84.900 | A |
| 8a1ef4594267fff | Novi Grad Sarajevo | Dolac | 11 | 933.900 | 84.900 | A |
| 8a1ef4580697fff | Centar Sarajevo | Hrastovi-Mrkovići | 29 | 2,462.800 | 84.900 | B |
| 8a1ea92c9a77fff | Novi Grad Sarajevo | Zabrđe | 13 | 1,104.300 | 84.900 | A |
| 8a1ef459095ffff | Novi Grad Sarajevo | Dolac | 68 | 5,776.900 | 85.000 | A |
| 8a1ef459c137fff | Stari Grad Sarajevo | Širokača | 98 | 8,326.100 | 85.000 | A |
| 8a1ef4594627fff | Novi Grad Sarajevo | Alipašin Most I | 75 | 6,373.800 | 85.000 | A |
| 8a1ef4594707fff | Novi Grad Sarajevo | Alipašin Most I | 63 | 5,354.000 | 85.000 | A |
| 8a1ef4591b4ffff | Centar Sarajevo | Marijin Dvor | 107 | 9,094.100 | 85.000 | B |
| 8a1ef4595a07fff | Novo Sarajevo | Velešići | 12 | 1,020.000 | 85.000 | B |
| 8a1ef4594757fff | Novi Grad Sarajevo | Alipašin Most I | 73 | 6,205.300 | 85.000 | A |
| 8a1ef4583ceffff | Stari Grad Sarajevo | Medrese | 83 | 7,056.200 | 85.000 | A |
| 8a1ef4591a5ffff | Centar Sarajevo | Skenderija-Podtekija | 67 | 5,697.100 | 85.000 | B |
| 8a1ef4582baffff | Centar Sarajevo | Hrastovi-Mrkovići | 48 | 4,083.700 | 85.100 | B |
| 8a1ef459600ffff | Novi Grad Sarajevo | Briješće | 44 | 3,745.100 | 85.100 | A |
| 8a1ea92cd367fff | Novi Grad Sarajevo | Reljevo | 21 | 1,787.700 | 85.100 | A |
| 8a1ef45804b7fff | Centar Sarajevo | Koševo II | 82 | 6,983.900 | 85.200 | B |
| 8a1ef4590747fff | Novi Grad Sarajevo | Švrakino Selo III | 89 | 7,582.100 | 85.200 | A |
| 8a1ef458678ffff | Centar Sarajevo | Šip | 56 | 4,771.000 | 85.200 | B |
| 8a1ef4594797fff | Novi Grad Sarajevo | Alipašin Most I | 80 | 6,816.600 | 85.200 | A |
| 8a1ef4582d0ffff | Centar Sarajevo | Donji Velešići | 50 | 4,261.900 | 85.200 | B |
| 8a1ef4583007fff | Stari Grad Sarajevo | Mošćanica | 14 | 1,193.400 | 85.200 | A |
| 8a1ea92eb057fff | Novi Grad Sarajevo | Reljevo | 10 | 852.700 | 85.300 | A |
| 8a1ef45835a7fff | Stari Grad Sarajevo | Medrese | 153 | 13,052.600 | 85.300 | A |
| 8a1ef4594687fff | Novi Grad Sarajevo | Alipašin Most I | 95 | 8,109.500 | 85.400 | A |
| 8a1ea92c9c47fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 218 | 18,609.400 | 85.400 | A |
| 8a1ef4595647fff | Novo Sarajevo | Pofalići I | 166 | 14,176.700 | 85.400 | B |
| 8a1ef4582557fff | Centar Sarajevo | Koševsko Brdo | 69 | 5,895.800 | 85.400 | B |
| 8a1ef4580487fff | Centar Sarajevo | Hrastovi-Mrkovići | 38 | 3,247.700 | 85.500 | B |
| 8a1ef4596a4ffff | Novi Grad Sarajevo | Alipašin Most I | 121 | 10,341.500 | 85.500 | A |
| 8a1ef45902a7fff | Novi Grad Sarajevo | Aneks | 89 | 7,606.600 | 85.500 | A |
| 8a1ef459c897fff | Centar Sarajevo | Skenderija-Podtekija | 94 | 8,034.400 | 85.500 | B |
| 8a1ef459472ffff | Novi Grad Sarajevo | Alipašin Most I | 67 | 5,726.800 | 85.500 | A |
| 8a1ef4590947fff | Novi Grad Sarajevo | Dolac | 54 | 4,616.000 | 85.500 | A |
| 8a1ef4590837fff | Novi Grad Sarajevo | Buća Potok | 103 | 8,804.900 | 85.500 | A |
| 8a1ef4593937fff | Novi Grad Sarajevo | Aneks | 89 | 7,610.000 | 85.500 | A |
| 8a1ef459469ffff | Novi Grad Sarajevo | Alipašin Most I | 106 | 9,066.300 | 85.500 | A |
| 8a1ef4582a1ffff | Centar Sarajevo | Hrastovi-Mrkovići | 54 | 4,619.100 | 85.500 | B |
| 8a1ef45826d7fff | Centar Sarajevo | Trg oslobođenja-Centar | 79 | 6,758.300 | 85.500 | B |
| 8a1ef45822effff | Stari Grad Sarajevo | Logavina | 124 | 10,611.100 | 85.600 | A |
| 8a1ef4586a1ffff | Centar Sarajevo | Betanija | 11 | 941.400 | 85.600 | B |
| 8a1ef4582367fff | Centar Sarajevo | Bardakčije | 57 | 4,880.300 | 85.600 | B |
| 8a1ef459c0d7fff | Stari Grad Sarajevo | Širokača | 44 | 3,767.600 | 85.600 | A |
| 8a1ef45943a7fff | Novi Grad Sarajevo | Dolac | 12 | 1,027.600 | 85.600 | A |
| 8a1ea92c9b87fff | Novi Grad Sarajevo | Zabrđe | 68 | 5,823.600 | 85.600 | A |
| 8a1ef4590b5ffff | Novo Sarajevo | Pofalići II | 26 | 2,227.000 | 85.700 | B |
| 8a1ef459391ffff | Novo Sarajevo | Hrasno Brdo | 22 | 1,884.600 | 85.700 | B |
| 8a1ef459468ffff | Novi Grad Sarajevo | Buća Potok | 79 | 6,768.000 | 85.700 | A |
| 8a1ef459dc0ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 29 | 2,485.400 | 85.700 | A |
| 8a1ef459c037fff | Stari Grad Sarajevo | Toka-Džeka | 82 | 7,034.800 | 85.800 | A |
| 8a1ef459636ffff | Novi Grad Sarajevo | Alipašin Most I | 87 | 7,473.300 | 85.900 | A |
| 8a1ef459cb1ffff | Stari Grad Sarajevo | Babića bašča | 163 | 14,011.900 | 86.000 | A |
| 8a1ef45804c7fff | Centar Sarajevo | Pionirska Dolina | 39 | 3,353.600 | 86.000 | B |
| 8a1ef458220ffff | Centar Sarajevo | Bardakčije | 95 | 8,170.000 | 86.000 | B |
| 8a1ef45864cffff | Centar Sarajevo | Šip | 51 | 4,386.400 | 86.000 | B |
| 8a1ef4595b2ffff | Centar Sarajevo | Šip | 15 | 1,290.200 | 86.000 | B |
| 8a1ef4594637fff | Novi Grad Sarajevo | Alipašin Most I | 79 | 6,797.800 | 86.000 | A |
| 8a1ef45946b7fff | Novi Grad Sarajevo | Alipašin Most I | 110 | 9,465.300 | 86.000 | A |
| 8a1ef459ccc7fff | Centar Sarajevo | Soukbunar | 42 | 3,614.800 | 86.100 | B |
| 8a1ef4590acffff | Novo Sarajevo | Čengić Vila I | 54 | 4,649.900 | 86.100 | B |
| 8a1ef45944effff | Novi Grad Sarajevo | Alipašin Most I | 94 | 8,095.700 | 86.100 | A |
| 8a1ef459479ffff | Novi Grad Sarajevo | Alipašin Most I | 101 | 8,703.200 | 86.200 | A |
| 8a1ef4590867fff | Novi Grad Sarajevo | Buća Potok | 106 | 9,143.000 | 86.300 | A |
| 8a1ef4590757fff | Novi Grad Sarajevo | Švrakino Selo III | 83 | 7,160.100 | 86.300 | A |
| 8a1ef4590d07fff | Novi Grad Sarajevo | Alipašin Most I | 130 | 11,215.800 | 86.300 | A |
| 8a1ef4583c77fff | Stari Grad Sarajevo | Sedrenik | 55 | 4,745.700 | 86.300 | A |
| 8a1ef459478ffff | Novi Grad Sarajevo | Alipašin Most I | 95 | 8,197.200 | 86.300 | A |
| 8a1ef4590827fff | Novi Grad Sarajevo | Buća Potok | 107 | 9,233.200 | 86.300 | A |
| 8a1ef4584c87fff | Centar Sarajevo | Betanija | 10 | 863.300 | 86.300 | B |
| 8a1ef459091ffff | Novi Grad Sarajevo | Buća Potok | 100 | 8,632.800 | 86.300 | A |
| 8a1ef45826b7fff | Centar Sarajevo | Crni Vrh-Gorica | 114 | 9,842.200 | 86.300 | B |
| 8a1ef45946a7fff | Novi Grad Sarajevo | Alipašin Most I | 102 | 8,809.900 | 86.400 | A |
| 8a1ef459470ffff | Novi Grad Sarajevo | Alipašin Most I | 85 | 7,342.700 | 86.400 | A |
| 8a1ef459254ffff | Novi Grad Sarajevo | Dobrinja B | 77 | 6,653.000 | 86.400 | A |
| 8a1ef4594787fff | Novi Grad Sarajevo | Alipašin Most I | 102 | 8,814.400 | 86.400 | A |
| 8a1ef4586267fff | Centar Sarajevo | Betanija | 13 | 1,123.500 | 86.400 | B |
| 8a1ef4592b6ffff | Novi Grad Sarajevo | Švrakino Selo II | 58 | 5,012.700 | 86.400 | A |
| 8a1ef459392ffff | Novi Grad Sarajevo | Aneks | 70 | 6,053.400 | 86.500 | A |
| 8a1ef4596a6ffff | Novi Grad Sarajevo | Alipašin Most I | 146 | 12,628.700 | 86.500 | A |
| 8a1ef45952d7fff | Novo Sarajevo | Pofalići I | 49 | 4,239.100 | 86.500 | B |
| 8a1ef459109ffff | Novo Sarajevo | Vraca | 35 | 3,028.400 | 86.500 | B |
| 8a1ef4590d27fff | Novi Grad Sarajevo | Alipašin Most I | 111 | 9,606.700 | 86.500 | A |
| 8a1ef459c367fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 41 | 3,549.000 | 86.600 | A |
| 8a1ef4591537fff | Novo Sarajevo | Hrasno Brdo | 92 | 7,965.200 | 86.600 | B |
| 8a1ef4590697fff | Novi Grad Sarajevo | Švrakino Selo II | 39 | 3,377.200 | 86.600 | A |
| 8a1ef4595437fff | Novi Grad Sarajevo | Dolac | 73 | 6,323.400 | 86.600 | A |
| 8a1ef459119ffff | Novo Sarajevo | Grbavica II | 90 | 7,797.800 | 86.600 | B |
| 8a1ef45902d7fff | Novi Grad Sarajevo | Aneks | 60 | 5,199.300 | 86.700 | A |
| 8a1ea92c9c5ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 196 | 16,987.000 | 86.700 | A |
| 8a1ef4582257fff | Stari Grad Sarajevo | Logavina | 123 | 10,660.700 | 86.700 | A |
| 8a1ea92c90a7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 96 | 8,322.700 | 86.700 | A |
| 8a1ef4594247fff | Novi Grad Sarajevo | Dolac | 29 | 2,515.000 | 86.700 | A |
| 8a1ef45822cffff | Stari Grad Sarajevo | Logavina | 127 | 11,015.100 | 86.700 | A |
| 8a1ef4592a1ffff | Novi Grad Sarajevo | Švrakino Selo II | 13 | 1,127.600 | 86.700 | A |
| 8a1ef4591d2ffff | Novo Sarajevo | Pofalići II | 245 | 21,257.300 | 86.800 | B |
| 8a1ef4591577fff | Novo Sarajevo | Grbavica II | 44 | 3,819.100 | 86.800 | B |
| 8a1ef45944cffff | Novi Grad Sarajevo | Alipašin Most I | 102 | 8,854.400 | 86.800 | A |
| 8a1ef459060ffff | Novi Grad Sarajevo | Švrakino Selo III | 69 | 5,990.000 | 86.800 | A |
| 8a1ef45904affff | Novi Grad Sarajevo | Švrakino Selo II | 75 | 6,511.100 | 86.800 | A |
| 8a1ef4594457fff | Novi Grad Sarajevo | Alipašin Most I | 94 | 8,160.600 | 86.800 | A |
| 8a1ef459176ffff | Novo Sarajevo | Vraca | 33 | 2,865.600 | 86.800 | B |
| 8a1ef4582cf7fff | Novo Sarajevo | Velešići | 102 | 8,862.000 | 86.900 | B |
| 8a1ef4593927fff | Novi Grad Sarajevo | Aneks | 132 | 11,468.800 | 86.900 | A |
| 8a1ef45904f7fff | Novi Grad Sarajevo | Švrakino Selo II | 65 | 5,648.500 | 86.900 | A |
| 8a1ea92c9a1ffff | Novi Grad Sarajevo | Zabrđe | 17 | 1,478.100 | 86.900 | A |
| 8a1ef459cc37fff | Centar Sarajevo | Soukbunar | 64 | 5,565.300 | 87.000 | B |
| 8a1ef4590807fff | Novi Grad Sarajevo | Buća Potok | 118 | 10,262.100 | 87.000 | A |
| 8a1ef4591a17fff | Centar Sarajevo | Marijin Dvor | 87 | 7,571.200 | 87.000 | B |
| 8a1ef4586917fff | Centar Sarajevo | Betanija | 10 | 870.400 | 87.000 | B |
| 8a1ef4590647fff | Novi Grad Sarajevo | Švrakino Selo III | 81 | 7,054.900 | 87.100 | A |
| 8a1ef4595af7fff | Novo Sarajevo | Velešići | 15 | 1,306.700 | 87.100 | B |
| 8a1ef459294ffff | Novi Grad Sarajevo | Švrakino Selo II | 75 | 6,533.800 | 87.100 | A |
| 8a1ef45804affff | Centar Sarajevo | Hrastovi-Mrkovići | 38 | 3,310.500 | 87.100 | B |
| 8a1ef4582b4ffff | Centar Sarajevo | Hrastovi-Mrkovići | 33 | 2,876.300 | 87.200 | B |
| 8a1ef45947affff | Novi Grad Sarajevo | Alipašin Most I | 106 | 9,240.600 | 87.200 | A |
| 8a1ef459cdaffff | Centar Sarajevo | Skenderija-Podtekija | 61 | 5,317.800 | 87.200 | B |
| 8a1ef45805b7fff | Centar Sarajevo | Pionirska Dolina | 26 | 2,267.500 | 87.200 | B |
| 8a1ef4595ae7fff | Novo Sarajevo | Velešići | 14 | 1,221.200 | 87.200 | B |
| 8a1ef45947b7fff | Novi Grad Sarajevo | Alipašin Most I | 109 | 9,508.300 | 87.200 | A |
| 8a1ea92c9b37fff | Novi Grad Sarajevo | Zabrđe | 23 | 2,006.700 | 87.200 | A |
| 8a1ef4582adffff | Centar Sarajevo | Bardakčije | 61 | 5,322.400 | 87.300 | B |
| 8a1ef4590627fff | Novi Grad Sarajevo | Švrakino Selo III | 82 | 7,157.000 | 87.300 | A |
| 8a1ef459cd1ffff | Centar Sarajevo | Skenderija-Podtekija | 58 | 5,063.900 | 87.300 | B |
| 8a1ef459069ffff | Novi Grad Sarajevo | Švrakino Selo II | 22 | 1,920.900 | 87.300 | A |
| 8a1ef459425ffff | Novi Grad Sarajevo | Dolac | 32 | 2,794.400 | 87.300 | A |
| 8a1ef458312ffff | Stari Grad Sarajevo | Sedrenik | 33 | 2,882.400 | 87.300 | A |
| 8a1ef459461ffff | Novi Grad Sarajevo | Buća Potok | 79 | 6,901.800 | 87.400 | A |
| 8a1ef4595b1ffff | Novo Sarajevo | Velešići | 13 | 1,136.000 | 87.400 | B |
| 8a1ef4582087fff | Centar Sarajevo | Ciglane | 135 | 11,797.700 | 87.400 | B |
| 8a1ef45944f7fff | Novi Grad Sarajevo | Alipašin Most I | 126 | 11,022.400 | 87.500 | A |
| 8a1ef45902affff | Novi Grad Sarajevo | Staro Hrasno | 63 | 5,513.600 | 87.500 | A |
| 8a1ef4590637fff | Novi Grad Sarajevo | Švrakino Selo III | 81 | 7,097.000 | 87.600 | A |
| 8a1ef4592097fff | Novi Grad Sarajevo | Dobrinja B | 83 | 7,273.100 | 87.600 | A |
| 8a1ef4583d4ffff | Stari Grad Sarajevo | Sedrenik | 46 | 4,034.000 | 87.700 | A |
| 8a1ef458318ffff | Stari Grad Sarajevo | Sedrenik | 47 | 4,123.200 | 87.700 | A |
| 8a1ef45940dffff | Novi Grad Sarajevo | Dolac | 49 | 4,299.200 | 87.700 | A |
| 8a1ef45b248ffff | Novi Grad Sarajevo | Zabrđe | 21 | 1,844.600 | 87.800 | A |
| 8a1ef4590797fff | Novi Grad Sarajevo | Švrakino Selo II | 66 | 5,797.400 | 87.800 | A |
| 8a1ef459c85ffff | Stari Grad Sarajevo | Bistrik | 179 | 15,725.900 | 87.900 | A |
| 8a1ef4592baffff | Novi Grad Sarajevo | Švrakino Selo II | 15 | 1,317.900 | 87.900 | A |
| 8a1ef459471ffff | Novi Grad Sarajevo | Alipašin Most I | 112 | 9,840.700 | 87.900 | A |
| 8a1ea92ccb07fff | Novi Grad Sarajevo | Dobroševići | 11 | 966.800 | 87.900 | A |
| 8a1ef459542ffff | Novi Grad Sarajevo | Dolac | 21 | 1,846.200 | 87.900 | A |
| 8a1ef45909affff | Novi Grad Sarajevo | Buća Potok | 105 | 9,232.300 | 87.900 | A |
| 8a1ef45940c7fff | Novi Grad Sarajevo | Dolac | 22 | 1,934.800 | 87.900 | A |
| 8a1ef4591857fff | Novo Sarajevo | Željeznička | 32 | 2,815.600 | 88.000 | B |
| 8a1ef4582c4ffff | Centar Sarajevo | Koševsko Brdo | 70 | 6,159.900 | 88.000 | B |
| 8a1ef458351ffff | Stari Grad Sarajevo | Medrese | 146 | 12,860.100 | 88.100 | A |
| 8a1ef45822c7fff | Stari Grad Sarajevo | Logavina | 138 | 12,159.800 | 88.100 | A |
| 8a1ea92c99affff | Novi Grad Sarajevo | Zabrđe | 23 | 2,027.300 | 88.100 | A |
| 8a1ef4592c37fff | Novi Grad Sarajevo | Dobrinja A | 150 | 13,231.300 | 88.200 | A |
| 8a1ef459438ffff | Novi Grad Sarajevo | Dolac | 30 | 2,646.400 | 88.200 | A |
| 8a1ef459445ffff | Novi Grad Sarajevo | Alipašin Most I | 141 | 12,443.000 | 88.200 | A |
| 8a1ef459ca4ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 31 | 2,735.700 | 88.200 | A |
| 8a1ef4586457fff | Centar Sarajevo | Šip | 48 | 4,236.900 | 88.300 | B |
| 8a1ef459209ffff | Novi Grad Sarajevo | Dobrinja B | 97 | 8,564.200 | 88.300 | A |
| 8a1ef4590507fff | Novi Grad Sarajevo | Alipašino Polje AI | 111 | 9,808.400 | 88.400 | A |
| 8a1ef458641ffff | Centar Sarajevo | Šip | 45 | 3,977.200 | 88.400 | B |
| 8a1ef4590a07fff | Novo Sarajevo | Pofalići II | 118 | 10,431.200 | 88.400 | B |
| 8a1ef4592a07fff | Novi Grad Sarajevo | Švrakino Selo II | 20 | 1,768.200 | 88.400 | A |
| 8a1ef459070ffff | Novi Grad Sarajevo | Švrakino Selo III | 105 | 9,286.800 | 88.400 | A |
| 8a1ef45848d7fff | Centar Sarajevo | Nahorevo | 13 | 1,150.200 | 88.500 | B |
| 8a1ea92c9987fff | Novi Grad Sarajevo | Zabrđe | 26 | 2,300.600 | 88.500 | A |
| 8a1ef4583427fff | Stari Grad Sarajevo | Sumbuluša | 115 | 10,176.800 | 88.500 | A |
| 8a1ef4595777fff | Novo Sarajevo | Pofalići II | 123 | 10,898.900 | 88.600 | B |
| 8a1ef4583d67fff | Stari Grad Sarajevo | Sedrenik | 43 | 3,811.600 | 88.600 | A |
| 8a1ea92c9947fff | Novi Grad Sarajevo | Zabrđe | 40 | 3,548.500 | 88.700 | A |
| 8a1ef45831affff | Stari Grad Sarajevo | Sedrenik | 56 | 4,968.700 | 88.700 | A |
| 8a1ef4584127fff | Centar Sarajevo | Nahorevo | 10 | 887.300 | 88.700 | B |
| 8a1ef4590677fff | Novi Grad Sarajevo | Švrakino Selo III | 78 | 6,922.800 | 88.800 | A |
| 8a1ef45825affff | Novo Sarajevo | Velešići | 58 | 5,148.800 | 88.800 | B |
| 8a1ea92cc88ffff | Novi Grad Sarajevo | Dobroševići | 52 | 4,617.300 | 88.800 | A |
| 8a1ef458350ffff | Stari Grad Sarajevo | Medrese | 132 | 11,721.200 | 88.800 | A |
| 8a1ef459048ffff | Novi Grad Sarajevo | Švrakino Selo II | 76 | 6,751.600 | 88.800 | A |
| 8a1ef4583517fff | Stari Grad Sarajevo | Medrese | 160 | 14,217.200 | 88.900 | A |
| 8a1ef4590607fff | Novi Grad Sarajevo | Švrakino Selo III | 77 | 6,842.300 | 88.900 | A |
| 8a1ef458245ffff | Centar Sarajevo | Crni Vrh-Gorica | 103 | 9,154.400 | 88.900 | B |
| 8a1ef4595b0ffff | Centar Sarajevo | Šip | 22 | 1,956.000 | 88.900 | B |
| 8a1ef458246ffff | Centar Sarajevo | Ciglane | 119 | 10,581.900 | 88.900 | B |
| 8a1ef4582ad7fff | Centar Sarajevo | Breka | 71 | 6,316.000 | 89.000 | B |
| 8a1ef459dcb7fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 28 | 2,491.400 | 89.000 | A |
| 8a1ef4582c9ffff | Novo Sarajevo | Gornji Velešići | 110 | 9,789.600 | 89.000 | B |
| 8a1ef45830b7fff | Stari Grad Sarajevo | Sumbuluša | 40 | 3,561.500 | 89.000 | A |
| 8a1ef4594677fff | Novi Grad Sarajevo | Dolac | 37 | 3,294.700 | 89.000 | A |
| 8a1ef459d1b7fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 18 | 1,602.900 | 89.100 | A |
| 8a1ef4591967fff | Novo Sarajevo | Pofalići I | 44 | 3,918.600 | 89.100 | B |
| 8a1ef458050ffff | Centar Sarajevo | Pionirska Dolina | 27 | 2,405.200 | 89.100 | B |
| 8a1ef4595267fff | Novo Sarajevo | Velešići | 45 | 4,010.900 | 89.100 | B |
| 8a1ef4591a6ffff | Centar Sarajevo | Marijin Dvor | 87 | 7,755.000 | 89.100 | B |
| 8a1ef459465ffff | Novi Grad Sarajevo | Buća Potok | 92 | 8,201.400 | 89.100 | A |
| 8a1ef459c8effff | Stari Grad Sarajevo | Bistrik | 209 | 18,644.400 | 89.200 | A |
| 8a1ef4583527fff | Stari Grad Sarajevo | Medrese | 132 | 11,776.300 | 89.200 | A |
| 8a1ef45824affff | Centar Sarajevo | Koševsko Brdo | 125 | 11,157.600 | 89.300 | B |
| 8a1ef459c11ffff | Stari Grad Sarajevo | Toka-Džeka | 102 | 9,106.200 | 89.300 | A |
| 8a1ef459062ffff | Novi Grad Sarajevo | Švrakino Selo III | 97 | 8,666.400 | 89.300 | A |
| 8a1ef4592a0ffff | Novi Grad Sarajevo | Švrakino Selo II | 12 | 1,072.100 | 89.300 | A |
| 8a1ef4580407fff | Centar Sarajevo | Pionirska Dolina | 38 | 3,395.800 | 89.400 | B |
| 8a1ef4583c8ffff | Stari Grad Sarajevo | Medrese | 115 | 10,277.200 | 89.400 | A |
| 8a1ea92c98e7fff | Novi Grad Sarajevo | Zabrđe | 21 | 1,877.700 | 89.400 | A |
| 8a1ea92c9b1ffff | Novi Grad Sarajevo | Zabrđe | 24 | 2,146.800 | 89.400 | A |
| 8a1ef458640ffff | Centar Sarajevo | Šip | 50 | 4,473.200 | 89.500 | B |
| 8a1ef459156ffff | Novo Sarajevo | Grbavica II | 80 | 7,157.300 | 89.500 | B |
| 8a1ef4590baffff | Novo Sarajevo | Pofalići II | 47 | 4,206.300 | 89.500 | B |
| 8a1ef4582447fff | Centar Sarajevo | Ciglane | 143 | 12,802.800 | 89.500 | B |
| 8a1ef45906a7fff | Novi Grad Sarajevo | Švrakino Selo II | 87 | 7,789.500 | 89.500 | A |
| 8a1ef45864c7fff | Centar Sarajevo | Šip | 46 | 4,118.700 | 89.500 | B |
| 8a1ef4590687fff | Novi Grad Sarajevo | Švrakino Selo II | 57 | 5,104.500 | 89.600 | A |
| 8a1ef45946e7fff | Novi Grad Sarajevo | Buća Potok | 113 | 10,120.500 | 89.600 | A |
| 8a1ef459079ffff | Novi Grad Sarajevo | Švrakino Selo II | 77 | 6,899.100 | 89.600 | A |
| 8a1ef4583cd7fff | Stari Grad Sarajevo | Medrese | 105 | 9,414.400 | 89.700 | A |
| 8a1ef459dd8ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 22 | 1,974.000 | 89.700 | A |
| 8a1ef4596b2ffff | Novi Grad Sarajevo | Alipašin Most I | 25 | 2,243.500 | 89.700 | A |
| 8a1ef459c84ffff | Stari Grad Sarajevo | Bistrik | 161 | 14,450.500 | 89.800 | A |
| 8a1ef4596657fff | Novi Grad Sarajevo | Saraj Polje | 55 | 4,938.800 | 89.800 | A |
| 8a1ef4590a0ffff | Novo Sarajevo | Pofalići II | 110 | 9,879.000 | 89.800 | B |
| 8a1ef4594397fff | Novi Grad Sarajevo | Dolac | 19 | 1,706.500 | 89.800 | A |
| 8a1ef45b208ffff | Novi Grad Sarajevo | Zabrđe | 10 | 898.200 | 89.800 | A |
| 8a1ea92c9baffff | Novi Grad Sarajevo | Zabrđe | 85 | 7,636.500 | 89.800 | A |
| 8a1ef459cd97fff | Centar Sarajevo | Soukbunar | 63 | 5,660.500 | 89.800 | B |
| 8a1ea92c9c4ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 74 | 6,652.800 | 89.900 | A |
| 8a1ef4591a47fff | Centar Sarajevo | Marijin Dvor | 59 | 5,305.100 | 89.900 | B |
| 8a1ea92ccaaffff | Novi Grad Sarajevo | Dobroševići | 11 | 989.200 | 89.900 | A |
| 8a1ef4596d77fff | Novi Grad Sarajevo | Briješće | 10 | 899.400 | 89.900 | A |
| 8a1ef4595237fff | Novo Sarajevo | Velešići | 30 | 2,698.100 | 89.900 | B |
| 8a1ef459cd5ffff | Centar Sarajevo | Skenderija-Podtekija | 98 | 8,816.400 | 90.000 | B |
| 8a1ef45b20b7fff | Novi Grad Sarajevo | Zabrđe | 13 | 1,169.600 | 90.000 | A |
| 8a1ef4582aaffff | Centar Sarajevo | Breka | 83 | 7,468.800 | 90.000 | B |
| 8a1ef4590617fff | Novi Grad Sarajevo | Švrakino Selo III | 92 | 8,281.400 | 90.000 | A |
| 8a1ef45804d7fff | Centar Sarajevo | Hrastovi-Mrkovići | 33 | 2,970.800 | 90.000 | B |
| 8a1ef4590957fff | Novi Grad Sarajevo | Dolac | 89 | 8,016.700 | 90.100 | A |
| 8a1ef459199ffff | Novo Sarajevo | Željeznička | 39 | 3,513.600 | 90.100 | B |
| 8a1ef459dcd7fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 22 | 1,982.300 | 90.100 | A |
| 8a1ef458355ffff | Stari Grad Sarajevo | Sumbuluša | 111 | 10,001.600 | 90.100 | A |
| 8a1ef459dceffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 14 | 1,261.700 | 90.100 | A |
| 8a1ef4590207fff | Novi Grad Sarajevo | Staro Hrasno | 82 | 7,390.800 | 90.100 | A |
| 8a1ef459561ffff | Novo Sarajevo | Pofalići I | 45 | 4,060.300 | 90.200 | B |
| 8a1ea92c9b0ffff | Novi Grad Sarajevo | Zabrđe | 16 | 1,443.800 | 90.200 | A |
| 8a1ea92c9897fff | Novi Grad Sarajevo | Zabrđe | 19 | 1,715.100 | 90.300 | A |
| 8a1ef4592b5ffff | Novi Grad Sarajevo | Švrakino Selo II | 51 | 4,604.000 | 90.300 | A |
| 8a1ef45904cffff | Novi Grad Sarajevo | Švrakino Selo II | 93 | 8,398.000 | 90.300 | A |
| 8a1ef458290ffff | Centar Sarajevo | Betanija | 38 | 3,434.300 | 90.400 | B |
| 8a1ef458451ffff | Centar Sarajevo | Betanija | 10 | 904.000 | 90.400 | B |
| 8a1ef4591937fff | Novo Sarajevo | Pofalići I | 108 | 9,768.300 | 90.400 | B |
| 8a1ef459208ffff | Novi Grad Sarajevo | Dobrinja B | 131 | 11,857.200 | 90.500 | A |
| 8a1ef45b24b7fff | Novi Grad Sarajevo | Zabrđe | 35 | 3,170.400 | 90.600 | A |
| 8a1ef4590b4ffff | Novo Sarajevo | Pofalići II | 40 | 3,623.500 | 90.600 | B |
| 8a1ef4586467fff | Centar Sarajevo | Šip | 33 | 2,991.100 | 90.600 | B |
| 8a1ef45904d7fff | Novi Grad Sarajevo | Švrakino Selo II | 89 | 8,067.300 | 90.600 | A |
| 8a1ef458206ffff | Centar Sarajevo | Koševo II | 114 | 10,334.300 | 90.700 | B |
| 8a1ef4592847fff | Novi Grad Sarajevo | Švrakino Selo II | 60 | 5,440.500 | 90.700 | A |
| 8a1ef45868affff | Centar Sarajevo | Betanija | 18 | 1,632.700 | 90.700 | B |
| 8a1ef459172ffff | Novo Sarajevo | Vraca | 35 | 3,174.900 | 90.700 | B |
| 8a1ef4592b67fff | Novi Grad Sarajevo | Švrakino Selo II | 89 | 8,074.900 | 90.700 | A |
| 8a1ea92c9a87fff | Novi Grad Sarajevo | Zabrđe | 23 | 2,087.000 | 90.700 | A |
| 8a1ea92c90c7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 19 | 1,724.000 | 90.700 | A |
| 8a1ea92c92b7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 21 | 1,905.600 | 90.700 | A |
| 8a1ef459061ffff | Novi Grad Sarajevo | Švrakino Selo III | 89 | 8,085.000 | 90.800 | A |
| 8a1ef459274ffff | Novi Grad Sarajevo | Dobrinja B | 108 | 9,812.200 | 90.900 | A |
| 8a1ef45b259ffff | Novi Grad Sarajevo | Zabrđe | 32 | 2,908.000 | 90.900 | A |
| 8a1ef459c02ffff | Stari Grad Sarajevo | Toka-Džeka | 89 | 8,095.900 | 91.000 | A |
| 8a1ef4595397fff | Novo Sarajevo | Pofalići I | 30 | 2,729.800 | 91.000 | B |
| 8a1ef4580b2ffff | Centar Sarajevo | Betanija | 13 | 1,183.200 | 91.000 | B |
| 8a1ef4583477fff | Stari Grad Sarajevo | Vratnik | 127 | 11,560.900 | 91.000 | A |
| 8a1ef4582737fff | Centar Sarajevo | Ciglane | 147 | 13,383.800 | 91.000 | B |
| 8a1ef4595597fff | Novi Grad Sarajevo | Dolac | 56 | 5,099.400 | 91.100 | A |
| 8a1ea92c9097fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 60 | 5,463.700 | 91.100 | A |
| 8a1ef4594d8ffff | Novi Grad Sarajevo | Zabrđe | 11 | 1,001.700 | 91.100 | A |
| 8a1ef45946f7fff | Novi Grad Sarajevo | Buća Potok | 126 | 11,478.600 | 91.100 | A |
| 8a1ef459189ffff | Novo Sarajevo | Željeznička | 71 | 6,468.200 | 91.100 | B |
| 8a1ef459c50ffff | Stari Grad Sarajevo | Širokača | 22 | 2,004.300 | 91.100 | A |
| 8a1ef4583117fff | Stari Grad Sarajevo | Sedrenik | 55 | 5,014.800 | 91.200 | A |
| 8a1ef459c0affff | Stari Grad Sarajevo | Širokača | 65 | 5,928.500 | 91.200 | A |
| 8a1ef4594667fff | Novi Grad Sarajevo | Dolac | 46 | 4,196.200 | 91.200 | A |
| 8a1ef45904dffff | Novi Grad Sarajevo | Švrakino Selo II | 90 | 8,211.300 | 91.200 | A |
| 8a1ea92c981ffff | Novi Grad Sarajevo | Zabrđe | 17 | 1,551.400 | 91.300 | A |
| 8a1ef4595367fff | Novo Sarajevo | Velešići | 63 | 5,753.100 | 91.300 | B |
| 8a1ef45b2557fff | Novi Grad Sarajevo | Zabrđe | 15 | 1,369.900 | 91.300 | A |
| 8a1ef4592b4ffff | Novi Grad Sarajevo | Švrakino Selo II | 68 | 6,211.800 | 91.300 | A |
| 8a1ef45904c7fff | Novi Grad Sarajevo | Švrakino Selo II | 100 | 9,139.900 | 91.400 | A |
| 8a1ef4591b07fff | Centar Sarajevo | Marijin Dvor | 152 | 13,895.900 | 91.400 | B |
| 8a1ef458645ffff | Centar Sarajevo | Šip | 55 | 5,028.600 | 91.400 | B |
| 8a1ef45b20affff | Novi Grad Sarajevo | Zabrđe | 11 | 1,006.300 | 91.500 | A |
| 8a1ef45904effff | Novi Grad Sarajevo | Švrakino Selo II | 115 | 10,521.200 | 91.500 | A |
| 8a1ef459390ffff | Novi Grad Sarajevo | Aneks | 70 | 6,405.600 | 91.500 | A |
| 8a1ef45867b7fff | Centar Sarajevo | Šip | 60 | 5,491.100 | 91.500 | B |
| 8a1ea92cc757fff | Novi Grad Sarajevo | Dobroševići | 24 | 2,197.000 | 91.500 | A |
| 8a1ef4595327fff | Novo Sarajevo | Velešići | 10 | 916.100 | 91.600 | B |
| 8a1ea92c98effff | Novi Grad Sarajevo | Zabrđe | 32 | 2,935.400 | 91.700 | A |
| 8a1ef4595a0ffff | Novo Sarajevo | Velešići | 21 | 1,927.100 | 91.800 | B |
| 8a1ef459cc07fff | Centar Sarajevo | Soukbunar | 67 | 6,149.400 | 91.800 | B |
| 8a1ef4595aeffff | Novo Sarajevo | Velešići | 13 | 1,193.600 | 91.800 | B |
| 8a1ef4583317fff | Stari Grad Sarajevo | Mošćanica | 13 | 1,193.900 | 91.800 | A |
| 8a1ef45920b7fff | Novi Grad Sarajevo | Dobrinja B | 146 | 13,409.900 | 91.800 | A |
| 8a1ef4580427fff | Centar Sarajevo | Pionirska Dolina | 31 | 2,848.200 | 91.900 | B |
| 8a1ef45953a7fff | Novo Sarajevo | Pofalići I | 14 | 1,286.700 | 91.900 | B |
| 8a1ef45950effff | Novo Sarajevo | Pofalići I | 26 | 2,389.700 | 91.900 | B |
| 8a1ef458488ffff | Centar Sarajevo | Nahorevo | 11 | 1,011.400 | 91.900 | B |
| 8a1ea92c918ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 50 | 4,597.400 | 91.900 | A |
| 8a1ef45b2cd7fff | Novi Grad Sarajevo | Reljevo | 78 | 7,173.500 | 92.000 | A |
| 8a1ef45b255ffff | Novi Grad Sarajevo | Zabrđe | 16 | 1,471.700 | 92.000 | A |
| 8a1ef45906e7fff | Novi Grad Sarajevo | Švrakino Selo II | 65 | 5,981.300 | 92.000 | A |
| 8a1ef458624ffff | Centar Sarajevo | Pionirska Dolina | 24 | 2,208.700 | 92.000 | B |
| 8a1ef45909a7fff | Novi Grad Sarajevo | Buća Potok | 95 | 8,743.000 | 92.000 | A |
| 8a1ef4590b87fff | Novo Sarajevo | Čengić Vila I | 20 | 1,840.800 | 92.000 | B |
| 8a1ef45b2ce7fff | Novi Grad Sarajevo | Reljevo | 37 | 3,405.900 | 92.100 | A |
| 8a1ef458625ffff | Centar Sarajevo | Betanija | 18 | 1,657.500 | 92.100 | B |
| 8a1ef4586907fff | Centar Sarajevo | Betanija | 17 | 1,566.000 | 92.100 | B |
| 8a1ef459c19ffff | Stari Grad Sarajevo | Širokača | 64 | 5,895.700 | 92.100 | A |
| 8a1ef459cae7fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 74 | 6,818.200 | 92.100 | A |
| 8a1ef458241ffff | Centar Sarajevo | Koševsko Brdo | 80 | 7,371.700 | 92.100 | B |
| 8a1ef459216ffff | Novi Grad Sarajevo | Dobrinja C | 29 | 2,672.300 | 92.100 | A |
| 8a1ef45b249ffff | Novi Grad Sarajevo | Zabrđe | 36 | 3,317.500 | 92.200 | A |
| 8a1ef45914affff | Novo Sarajevo | Vraca | 25 | 2,304.200 | 92.200 | B |
| 8a1ef4592b47fff | Novi Grad Sarajevo | Švrakino Selo II | 85 | 7,834.600 | 92.200 | A |
| 8a1ef4590b2ffff | Novo Sarajevo | Pofalići II | 42 | 3,873.200 | 92.200 | B |
| 8a1ef45846f7fff | Centar Sarajevo | Betanija | 13 | 1,199.400 | 92.300 | B |
| 8a1ea92cc797fff | Novi Grad Sarajevo | Dobroševići | 11 | 1,014.900 | 92.300 | A |
| 8a1ea92c989ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 89 | 8,212.400 | 92.300 | A |
| 8a1ef458048ffff | Centar Sarajevo | Hrastovi-Mrkovići | 39 | 3,600.200 | 92.300 | B |
| 8a1ef459219ffff | Novi Grad Sarajevo | Dobrinja B | 155 | 14,317.400 | 92.400 | A |
| 8a1ef45b2487fff | Novi Grad Sarajevo | Zabrđe | 34 | 3,140.800 | 92.400 | A |
| 8a1ef459698ffff | Novi Grad Sarajevo | Briješće | 24 | 2,219.500 | 92.500 | A |
| 8a1ea92c9a17fff | Novi Grad Sarajevo | Zabrđe | 36 | 3,329.600 | 92.500 | A |
| 8a1ef459028ffff | Novi Grad Sarajevo | Staro Hrasno | 80 | 7,399.500 | 92.500 | A |
| 8a1ef4595a8ffff | Novo Sarajevo | Velešići | 15 | 1,387.400 | 92.500 | B |
| 8a1ef4582d07fff | Centar Sarajevo | Donji Velešići | 33 | 3,054.100 | 92.500 | B |
| 8a1ea92cd057fff | Novi Grad Sarajevo | Reljevo | 12 | 1,111.600 | 92.600 | A |
| 8a1ef45b24a7fff | Novi Grad Sarajevo | Zabrđe | 29 | 2,686.900 | 92.700 | A |
| 8a1ef4592557fff | Novi Grad Sarajevo | Dobrinja B | 15 | 1,389.900 | 92.700 | A |
| 8a1ef4586b5ffff | Centar Sarajevo | Betanija | 16 | 1,482.600 | 92.700 | B |
| 8a1ef4580787fff | Centar Sarajevo | Hrastovi-Mrkovići | 21 | 1,946.400 | 92.700 | B |
| 8a1ef45912a7fff | Novo Sarajevo | Gornji Kovačići | 13 | 1,205.100 | 92.700 | B |
| 8a1ef4591927fff | Novo Sarajevo | Pofalići I | 60 | 5,564.700 | 92.700 | B |
| 8a1ef459439ffff | Novi Grad Sarajevo | Dolac | 32 | 2,968.300 | 92.800 | A |
| 8a1ef459431ffff | Novi Grad Sarajevo | Dolac | 16 | 1,484.300 | 92.800 | A |
| 8a1ef45940d7fff | Novi Grad Sarajevo | Dolac | 27 | 2,505.300 | 92.800 | A |
| 8a1ef459dd57fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 30 | 2,783.900 | 92.800 | A |
| 8a1ef4596077fff | Novi Grad Sarajevo | Briješće | 68 | 6,312.100 | 92.800 | A |
| 8a1ef45b2577fff | Novi Grad Sarajevo | Zabrđe | 12 | 1,113.900 | 92.800 | A |
| 8a1ea92c9b17fff | Novi Grad Sarajevo | Zabrđe | 33 | 3,064.000 | 92.800 | A |
| 8a1ef4590b37fff | Novo Sarajevo | Pofalići II | 85 | 7,895.600 | 92.900 | B |
| 8a1ef45918f7fff | Novo Sarajevo | Željeznička | 51 | 4,741.000 | 93.000 | B |
| 8a1ea92c9007fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 28 | 2,603.700 | 93.000 | A |
| 8a1ef458205ffff | Centar Sarajevo | Park-Višnjik | 95 | 8,848.000 | 93.100 | B |
| 8a1ef4583d87fff | Stari Grad Sarajevo | Sedrenik | 84 | 7,826.700 | 93.200 | A |
| 8a1ef45902c7fff | Novo Sarajevo | Hrasno Brdo | 90 | 8,387.600 | 93.200 | B |
| 8a1ea92c9b27fff | Novi Grad Sarajevo | Zabrđe | 32 | 2,983.600 | 93.200 | A |
| 8a1ef4582b97fff | Centar Sarajevo | Koševo II | 67 | 6,247.400 | 93.200 | B |
| 8a1ef459dd5ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 26 | 2,424.400 | 93.200 | A |
| 8a1ef4590a67fff | Novo Sarajevo | Pofalići II | 40 | 3,730.500 | 93.300 | B |
| 8a1ef459c727fff | Stari Grad Sarajevo | Širokača | 41 | 3,824.900 | 93.300 | A |
| 8a1ef459c0b7fff | Stari Grad Sarajevo | Širokača | 60 | 5,597.700 | 93.300 | A |
| 8a1ef459578ffff | Novo Sarajevo | Pofalići II | 50 | 4,665.000 | 93.300 | B |
| 8a1ef4596baffff | Novi Grad Sarajevo | Briješće | 14 | 1,306.300 | 93.300 | A |
| 8a1ef4583d5ffff | Stari Grad Sarajevo | Sedrenik | 59 | 5,506.400 | 93.300 | A |
| 8a1ef458311ffff | Stari Grad Sarajevo | Sedrenik | 57 | 5,319.800 | 93.300 | A |
| 8a1ef459256ffff | Novi Grad Sarajevo | Dobrinja B | 178 | 16,625.600 | 93.400 | A |
| 8a1ef4583467fff | Stari Grad Sarajevo | Vratnik | 108 | 10,087.500 | 93.400 | A |
| 8a1ea92c9207fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 10 | 934.500 | 93.500 | A |
| 8a1ef4593947fff | Novo Sarajevo | Hrasno Brdo | 26 | 2,431.300 | 93.500 | B |
| 8a1ef4595a57fff | Novo Sarajevo | Gornji Velešići | 23 | 2,151.300 | 93.500 | B |
| 8a1ef45954dffff | Novo Sarajevo | Pofalići II | 44 | 4,116.300 | 93.600 | B |
| 8a1ef459c8cffff | Stari Grad Sarajevo | Bistrik | 206 | 19,272.400 | 93.600 | A |
| 8a1ef4590a27fff | Novo Sarajevo | Pofalići II | 31 | 2,900.700 | 93.600 | B |
| 8a1ef458346ffff | Stari Grad Sarajevo | Vratnik | 94 | 8,796.700 | 93.600 | A |
| 8a1ef4591acffff | Centar Sarajevo | Soukbunar | 69 | 6,459.400 | 93.600 | B |
| 8a1ef45820effff | Centar Sarajevo | Park-Višnjik | 79 | 7,395.600 | 93.600 | B |
| 8a1ef45910d7fff | Novo Sarajevo | Vraca | 46 | 4,308.300 | 93.700 | B |
| 8a1ef45942effff | Novi Grad Sarajevo | Dolac | 50 | 4,683.700 | 93.700 | A |
| 8a1ef4583d0ffff | Stari Grad Sarajevo | Sedrenik | 65 | 6,090.700 | 93.700 | A |
| 8a1ef4582027fff | Centar Sarajevo | Koševo II | 131 | 12,281.200 | 93.700 | B |
| 8a1ef459180ffff | Novo Sarajevo | Željeznička | 35 | 3,282.600 | 93.800 | B |
| 8a1ef4583557fff | Stari Grad Sarajevo | Sumbuluša | 126 | 11,819.200 | 93.800 | A |
| 8a1ef45867affff | Centar Sarajevo | Šip | 64 | 6,004.100 | 93.800 | B |
| 8a1ef4591907fff | Novo Sarajevo | Pofalići I | 62 | 5,818.200 | 93.800 | B |
| 8a1ef4583447fff | Stari Grad Sarajevo | Vratnik | 126 | 11,826.800 | 93.900 | A |
| 8a1ef4583037fff | Stari Grad Sarajevo | Sedrenik | 46 | 4,318.300 | 93.900 | A |
| 8a1ef459c36ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 44 | 4,131.400 | 93.900 | A |
| 8a1ef4592087fff | Novi Grad Sarajevo | Dobrinja B | 188 | 17,657.600 | 93.900 | A |
| 8a1ea92c96effff | Novi Grad Sarajevo | Briješće | 55 | 5,167.700 | 94.000 | A |
| 8a1ef4583c07fff | Stari Grad Sarajevo | Sedrenik | 77 | 7,236.500 | 94.000 | A |
| 8a1ea92c98b7fff | Novi Grad Sarajevo | Zabrđe | 28 | 2,632.000 | 94.000 | A |
| 8a1ef4591c37fff | Novo Sarajevo | Malta | 82 | 7,711.100 | 94.000 | B |
| 8a1ef4583587fff | Stari Grad Sarajevo | Medrese | 167 | 15,707.100 | 94.100 | A |
| 8a1ea92cd21ffff | Novi Grad Sarajevo | Reljevo | 102 | 9,593.900 | 94.100 | A |
| 8a1ef458268ffff | Centar Sarajevo | Trg oslobođenja-Centar | 94 | 8,842.700 | 94.100 | B |
| 8a1ef459dc27fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 38 | 3,577.500 | 94.100 | A |
| 8a1ef459c10ffff | Stari Grad Sarajevo | Toka-Džeka | 117 | 11,022.600 | 94.200 | A |
| 8a1ef459130ffff | Novo Sarajevo | Gornji Kovačići | 65 | 6,124.300 | 94.200 | B |
| 8a1ea92c999ffff | Novi Grad Sarajevo | Zabrđe | 35 | 3,298.200 | 94.200 | A |
| 8a1ef4595657fff | Novo Sarajevo | Pofalići I | 60 | 5,655.400 | 94.300 | B |
| 8a1ef4590b67fff | Novo Sarajevo | Pofalići II | 45 | 4,243.400 | 94.300 | B |
| 8a1ef458370ffff | Stari Grad Sarajevo | Vratnik | 56 | 5,281.300 | 94.300 | A |
| 8a1ef458204ffff | Centar Sarajevo | Park-Višnjik | 89 | 8,394.800 | 94.300 | B |
| 8a1ef45952effff | Novo Sarajevo | Pofalići I | 55 | 5,190.200 | 94.400 | B |
| 8a1ef459c847fff | Stari Grad Sarajevo | Bistrik | 152 | 14,344.800 | 94.400 | A |
| 8a1ef459dc67fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 20 | 1,889.100 | 94.500 | A |
| 8a1ef4582d9ffff | Novo Sarajevo | Gornji Velešići | 45 | 4,250.700 | 94.500 | B |
| 8a1ea92c9ab7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 18 | 1,701.700 | 94.500 | A |
| 8a1ef4595387fff | Novo Sarajevo | Pofalići I | 30 | 2,836.600 | 94.600 | B |
| 8a1ef45953b7fff | Novo Sarajevo | Pofalići I | 26 | 2,458.600 | 94.600 | B |
| 8a1ef4592ca7fff | Novi Grad Sarajevo | Dobrinja A | 46 | 4,350.100 | 94.600 | A |
| 8a1ef4586817fff | Centar Sarajevo | Betanija | 12 | 1,135.000 | 94.600 | B |
| 8a1ef459c967fff | Stari Grad Sarajevo | Logavina | 143 | 13,525.200 | 94.600 | A |
| 8a1ef4591b6ffff | Centar Sarajevo | Crni Vrh-Gorica | 83 | 7,851.700 | 94.600 | B |
| 8a1ef4582277fff | Stari Grad Sarajevo | Logavina | 124 | 11,737.500 | 94.700 | A |
| 8a1ef459424ffff | Novi Grad Sarajevo | Dolac | 46 | 4,354.400 | 94.700 | A |
| 8a1ef459144ffff | Novo Sarajevo | Vraca | 37 | 3,503.600 | 94.700 | B |
| 8a1ef459396ffff | Novo Sarajevo | Hrasno Brdo | 36 | 3,409.600 | 94.700 | B |
| 8a1ef4595667fff | Novo Sarajevo | Pofalići I | 60 | 5,684.200 | 94.700 | B |
| 8a1ea92eb65ffff | Novi Grad Sarajevo | Reljevo | 10 | 947.700 | 94.800 | A |
| 8a1ea92cd2d7fff | Novi Grad Sarajevo | Zabrđe | 105 | 9,952.500 | 94.800 | A |
| 8a1ef45956a7fff | Novo Sarajevo | Pofalići II | 57 | 5,403.700 | 94.800 | B |
| 8a1ef459551ffff | Novi Grad Sarajevo | Dolac | 48 | 4,553.500 | 94.900 | A |
| 8a1ef4595b5ffff | Novo Sarajevo | Gornji Velešići | 12 | 1,138.500 | 94.900 | B |
| 8a1ef4595b47fff | Centar Sarajevo | Šip | 31 | 2,943.400 | 94.900 | B |
| 8a1ef459d9a7fff | Stari Grad Sarajevo | Mošćanica | 13 | 1,234.400 | 95.000 | A |
| 8a1ef45b20a7fff | Novi Grad Sarajevo | Zabrđe | 15 | 1,424.400 | 95.000 | A |
| 8a1ef45b2497fff | Novi Grad Sarajevo | Zabrđe | 50 | 4,748.700 | 95.000 | A |
| 8a1ef4580b37fff | Centar Sarajevo | Betanija | 17 | 1,614.900 | 95.000 | B |
| 8a1ef459c18ffff | Stari Grad Sarajevo | Širokača | 82 | 7,789.700 | 95.000 | A |
| 8a1ef45910a7fff | Novo Sarajevo | Vraca | 92 | 8,742.900 | 95.000 | B |
| 8a1ef459559ffff | Novi Grad Sarajevo | Dolac | 75 | 7,127.400 | 95.000 | A |
| 8a1ef4583497fff | Stari Grad Sarajevo | Baščaršija | 123 | 11,690.400 | 95.000 | A |
| 8a1ea92c9807fff | Novi Grad Sarajevo | Zabrđe | 64 | 6,082.900 | 95.000 | A |
| 8a1ef45913affff | Novo Sarajevo | Gornji Kovačići | 39 | 3,708.300 | 95.100 | B |
| 8a1ef4592c5ffff | Novi Grad Sarajevo | Dobrinja D | 102 | 9,700.300 | 95.100 | A |
| 8a1ef459674ffff | Novi Grad Sarajevo | Saraj Polje | 53 | 5,040.500 | 95.100 | A |
| 8a1ef4586b77fff | Centar Sarajevo | Betanija | 13 | 1,237.200 | 95.200 | B |
| 8a1ef4592c77fff | Novi Grad Sarajevo | Dobrinja A | 46 | 4,377.800 | 95.200 | A |
| 8a1ef4595337fff | Novo Sarajevo | Velešići | 16 | 1,523.700 | 95.200 | B |
| 8a1ef4583637fff | Stari Grad Sarajevo | Vratnik | 72 | 6,860.600 | 95.300 | A |
| 8a1ef458235ffff | Stari Grad Sarajevo | Logavina | 112 | 10,681.000 | 95.400 | A |
| 8a1ef458295ffff | Centar Sarajevo | Koševo II | 54 | 5,150.400 | 95.400 | B |
| 8a1ea92c91b7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 114 | 10,882.700 | 95.500 | A |
| 8a1ef4591b57fff | Centar Sarajevo | Marijin Dvor | 119 | 11,363.500 | 95.500 | B |
| 8a1ea92c9b2ffff | Novi Grad Sarajevo | Zabrđe | 18 | 1,718.900 | 95.500 | A |
| 8a1ef4582d87fff | Novo Sarajevo | Gornji Velešići | 40 | 3,820.300 | 95.500 | B |
| 8a1ef4584927fff | Centar Sarajevo | Nahorevo | 15 | 1,432.600 | 95.500 | B |
| 8a1ef4591baffff | Centar Sarajevo | Marijin Dvor | 73 | 6,972.900 | 95.500 | B |
| 8a1ef4592667fff | Novi Grad Sarajevo | Dobrinja B | 30 | 2,867.500 | 95.600 | A |
| 8a1ef45b256ffff | Novi Grad Sarajevo | Zabrđe | 14 | 1,338.500 | 95.600 | A |
| 8a1ea92c90effff | Novi Grad Sarajevo | Naselje heroja Sokolje | 79 | 7,553.400 | 95.600 | A |
| 8a1ea92c980ffff | Novi Grad Sarajevo | Zabrđe | 55 | 5,262.200 | 95.700 | A |
| 8a1ef4594657fff | Novi Grad Sarajevo | Dolac | 102 | 9,763.400 | 95.700 | A |
| 8a1ef4595c37fff | Novi Grad Sarajevo | Dolac | 12 | 1,148.900 | 95.700 | A |
| 8a1ef45910c7fff | Novo Sarajevo | Vraca | 48 | 4,598.100 | 95.800 | B |
| 8a1ef4584507fff | Centar Sarajevo | Betanija | 11 | 1,054.000 | 95.800 | B |
| 8a1ef459dd87fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 44 | 4,216.700 | 95.800 | A |
| 8a1ef4584837fff | Centar Sarajevo | Nahorevo | 10 | 958.700 | 95.900 | B |
| 8a1ef459106ffff | Novo Sarajevo | Kovačići | 146 | 13,999.700 | 95.900 | B |
| 8a1ef4592ceffff | Novi Grad Sarajevo | Dobrinja A | 132 | 12,657.500 | 95.900 | A |
| 8a1ef45952c7fff | Novo Sarajevo | Pofalići I | 66 | 6,329.400 | 95.900 | B |
| 8a1ef458690ffff | Centar Sarajevo | Betanija | 12 | 1,151.400 | 95.900 | B |
| 8a1ef459ca1ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 89 | 8,542.400 | 96.000 | A |
| 8a1ef4583d6ffff | Stari Grad Sarajevo | Sedrenik | 41 | 3,938.200 | 96.100 | A |
| 8a1ef4595617fff | Novo Sarajevo | Pofalići II | 56 | 5,380.000 | 96.100 | B |
| 8a1ef45954d7fff | Novo Sarajevo | Pofalići II | 48 | 4,612.100 | 96.100 | B |
| 8a1ef458266ffff | Centar Sarajevo | Mejtaš-Bjelave | 90 | 8,648.700 | 96.100 | B |
| 8a1ef458061ffff | Centar Sarajevo | Hrastovi-Mrkovići | 17 | 1,634.500 | 96.100 | B |
| 8a1ef458248ffff | Centar Sarajevo | Crni Vrh-Gorica | 106 | 10,193.700 | 96.200 | B |
| 8a1ef459521ffff | Novo Sarajevo | Velešići | 57 | 5,481.700 | 96.200 | B |
| 8a1ef45854dffff | Centar Sarajevo | Betanija | 11 | 1,058.600 | 96.200 | B |
| 8a1ef459dce7fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 31 | 2,983.900 | 96.300 | A |
| 8a1ea92cd64ffff | Novi Grad Sarajevo | Zabrđe | 37 | 3,562.700 | 96.300 | A |
| 8a1ef459394ffff | Novo Sarajevo | Hrasno Brdo | 13 | 1,251.900 | 96.300 | B |
| 8a1ef45942dffff | Novi Grad Sarajevo | Dolac | 88 | 8,474.700 | 96.300 | A |
| 8a1ef459428ffff | Novi Grad Sarajevo | Dolac | 75 | 7,224.900 | 96.300 | A |
| 8a1ef4590277fff | Novo Sarajevo | Hrasno Brdo | 69 | 6,649.000 | 96.400 | B |
| 8a1ef4594237fff | Novi Grad Sarajevo | Dolac | 42 | 4,048.200 | 96.400 | A |
| 8a1ef4590977fff | Novi Grad Sarajevo | Dolac | 100 | 9,638.600 | 96.400 | A |
| 8a1ef4582c37fff | Novo Sarajevo | Gornji Velešići | 47 | 4,532.300 | 96.400 | B |
| 8a1ef4582567fff | Centar Sarajevo | Koševsko Brdo | 111 | 10,710.000 | 96.500 | B |
| 8a1ef459090ffff | Novi Grad Sarajevo | Dolac | 100 | 9,655.000 | 96.500 | A |
| 8a1ef4582187fff | Centar Sarajevo | Ciglane | 130 | 12,552.900 | 96.600 | B |
| 8a1ef4582a67fff | Centar Sarajevo | Hrastovi-Mrkovići | 46 | 4,442.500 | 96.600 | B |
| 8a1ef4590907fff | Novi Grad Sarajevo | Dolac | 138 | 13,345.600 | 96.700 | A |
| 8a1ef459cd9ffff | Centar Sarajevo | Soukbunar | 67 | 6,480.200 | 96.700 | B |
| 8a1ef459c947fff | Stari Grad Sarajevo | Logavina | 137 | 13,262.400 | 96.800 | A |
| 8a1ef4583487fff | Stari Grad Sarajevo | Kovači | 83 | 8,034.900 | 96.800 | A |
| 8a1ef4590247fff | Novo Sarajevo | Hrasno Brdo | 126 | 12,198.500 | 96.800 | B |
| 8a1ef459c56ffff | Stari Grad Sarajevo | Širokača | 61 | 5,907.100 | 96.800 | A |
| 8a1ef459466ffff | Novi Grad Sarajevo | Dolac | 76 | 7,361.600 | 96.900 | A |
| 8a1ef459548ffff | Novo Sarajevo | Pofalići II | 53 | 5,137.300 | 96.900 | B |
| 8a1ef45940cffff | Novi Grad Sarajevo | Dolac | 31 | 3,005.400 | 96.900 | A |
| 8a1ea92eb187fff | Novi Grad Sarajevo | Reljevo | 12 | 1,163.600 | 97.000 | A |
| 8a1ef45825a7fff | Novo Sarajevo | Velešići | 75 | 7,274.300 | 97.000 | B |
| 8a1ef459cdb7fff | Centar Sarajevo | Skenderija-Podtekija | 128 | 12,417.300 | 97.000 | B |
| 8a1ef459545ffff | Novo Sarajevo | Pofalići II | 32 | 3,106.600 | 97.100 | B |
| 8a1ef458622ffff | Centar Sarajevo | Betanija | 11 | 1,068.400 | 97.100 | B |
| 8a1ef4595627fff | Novo Sarajevo | Pofalići II | 58 | 5,633.200 | 97.100 | B |
| 8a1ef4592c17fff | Novi Grad Sarajevo | Dobrinja A | 128 | 12,433.600 | 97.100 | A |
| 8a1ea92c90d7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 42 | 4,082.200 | 97.200 | A |
| 8a1ea92c9867fff | Novi Grad Sarajevo | Zabrđe | 70 | 6,810.000 | 97.300 | A |
| 8a1ef459665ffff | Novi Grad Sarajevo | Saraj Polje | 35 | 3,406.400 | 97.300 | A |
| 8a1ef4595207fff | Novo Sarajevo | Velešići | 45 | 4,379.700 | 97.300 | B |
| 8a1ef4590937fff | Novi Grad Sarajevo | Dolac | 97 | 9,442.400 | 97.300 | A |
| 8a1ea92c9967fff | Novi Grad Sarajevo | Zabrđe | 55 | 5,354.100 | 97.300 | A |
| 8a1ef458202ffff | Centar Sarajevo | Park-Višnjik | 119 | 11,589.500 | 97.400 | B |
| 8a1ef45b20f7fff | Novi Grad Sarajevo | Zabrđe | 15 | 1,460.900 | 97.400 | A |
| 8a1ef45b251ffff | Novi Grad Sarajevo | Zabrđe | 38 | 3,701.200 | 97.400 | A |
| 8a1ef4593917fff | Novo Sarajevo | Hrasno Brdo | 78 | 7,600.800 | 97.400 | B |
| 8a1ef4590657fff | Novi Grad Sarajevo | Švrakino Selo III | 77 | 7,504.500 | 97.500 | A |
| 8a1ea92ebc6ffff | Novi Grad Sarajevo | Reljevo | 10 | 975.000 | 97.500 | A |
| 8a1ef459422ffff | Novi Grad Sarajevo | Dolac | 37 | 3,611.200 | 97.600 | A |
| 8a1ef4590137fff | Novi Grad Sarajevo | Alipašin Most III | 108 | 10,541.800 | 97.600 | A |
| 8a1ef459104ffff | Novo Sarajevo | Gornji Kovačići | 58 | 5,661.300 | 97.600 | B |
| 8a1ef4595767fff | Novo Sarajevo | Pofalići I | 44 | 4,296.200 | 97.600 | B |
| 8a1ea92c9aaffff | Novi Grad Sarajevo | Zabrđe | 41 | 4,003.400 | 97.600 | A |
| 8a1ef4586baffff | Centar Sarajevo | Betanija | 10 | 976.500 | 97.700 | B |
| 8a1ef4584737fff | Centar Sarajevo | Betanija | 13 | 1,269.500 | 97.700 | B |
| 8a1ef459536ffff | Novo Sarajevo | Gornji Velešići | 44 | 4,297.900 | 97.700 | B |
| 8a1ef459ca0ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 87 | 8,500.000 | 97.700 | A |
| 8a1ea92c9337fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 11 | 1,074.900 | 97.700 | A |
| 8a1ef6965a5ffff | Novi Grad Sarajevo | Saraj Polje | 35 | 3,421.200 | 97.700 | A |
| 8a1ef4583167fff | Stari Grad Sarajevo | Mošćanica | 12 | 1,173.000 | 97.700 | A |
| 8a1ef4595517fff | Novi Grad Sarajevo | Dolac | 55 | 5,380.300 | 97.800 | A |
| 8a1ea92c9aeffff | Novi Grad Sarajevo | Zabrđe | 42 | 4,108.800 | 97.800 | A |
| 8a1ef45943affff | Novi Grad Sarajevo | Dolac | 35 | 3,424.500 | 97.800 | A |
| 8a1ef4582d5ffff | Centar Sarajevo | Koševsko Brdo | 119 | 11,643.600 | 97.800 | B |
| 8a1ea92c9b8ffff | Novi Grad Sarajevo | Zabrđe | 50 | 4,893.700 | 97.900 | A |
| 8a1ef4580737fff | Centar Sarajevo | Hrastovi-Mrkovići | 16 | 1,566.100 | 97.900 | B |
| 8a1ef4583787fff | Stari Grad Sarajevo | Vratnik | 116 | 11,360.200 | 97.900 | A |
| 8a1ef4582d97fff | Novo Sarajevo | Velešići | 39 | 3,820.100 | 98.000 | B |
| 8a1ea92c9a27fff | Novi Grad Sarajevo | Zabrđe | 36 | 3,526.800 | 98.000 | A |
| 8a1ef4594da7fff | Novi Grad Sarajevo | Zabrđe | 16 | 1,567.600 | 98.000 | A |
| 8a1ef4595a17fff | Novo Sarajevo | Velešići | 12 | 1,175.900 | 98.000 | B |
| 8a1ef4582977fff | Centar Sarajevo | Betanija | 57 | 5,585.900 | 98.000 | B |
| 8a1ea92c9877fff | Novi Grad Sarajevo | Zabrđe | 69 | 6,762.300 | 98.000 | A |
| 8a1ef45902e7fff | Novi Grad Sarajevo | Staro Hrasno | 111 | 10,880.100 | 98.000 | A |
| 8a1ef4594647fff | Novi Grad Sarajevo | Dolac | 93 | 9,115.900 | 98.000 | A |
| 8a1ef4584517fff | Centar Sarajevo | Betanija | 11 | 1,078.300 | 98.000 | B |
| 8a1ef459c577fff | Stari Grad Sarajevo | Širokača | 42 | 4,117.300 | 98.000 | A |
| 8a1ef459c08ffff | Stari Grad Sarajevo | Širokača | 66 | 6,472.200 | 98.100 | A |
| 8a1ef45950f7fff | Novo Sarajevo | Pofalići II | 20 | 1,961.800 | 98.100 | B |
| 8a1ea92c961ffff | Novi Grad Sarajevo | Briješće | 12 | 1,177.100 | 98.100 | A |
| 8a1ef4596997fff | Novi Grad Sarajevo | Briješće | 86 | 8,437.600 | 98.100 | A |
| 8a1ea92c9917fff | Novi Grad Sarajevo | Zabrđe | 60 | 5,886.800 | 98.100 | A |
| 8a1ef4594287fff | Novi Grad Sarajevo | Dolac | 72 | 7,065.600 | 98.100 | A |
| 8a1ef45822dffff | Stari Grad Sarajevo | Logavina | 147 | 14,426.000 | 98.100 | A |
| 8a1ef4590927fff | Novi Grad Sarajevo | Dolac | 97 | 9,519.800 | 98.100 | A |
| 8a1ef45b24affff | Novi Grad Sarajevo | Zabrđe | 36 | 3,533.200 | 98.100 | A |
| 8a1ef45942d7fff | Novi Grad Sarajevo | Dolac | 98 | 9,618.500 | 98.100 | A |
| 8a1ef45942c7fff | Novi Grad Sarajevo | Dolac | 82 | 8,053.100 | 98.200 | A |
| 8a1ef458675ffff | Centar Sarajevo | Šip | 34 | 3,339.400 | 98.200 | B |
| 8a1ef45804cffff | Centar Sarajevo | Pionirska Dolina | 34 | 3,339.500 | 98.200 | B |
| 8a1ea92c8c1ffff | Novi Grad Sarajevo | Dobroševići | 26 | 2,554.300 | 98.200 | A |
| 8a1ef4583d97fff | Stari Grad Sarajevo | Sedrenik | 100 | 9,826.700 | 98.300 | A |
| 8a1ea92c9b07fff | Novi Grad Sarajevo | Zabrđe | 47 | 4,618.800 | 98.300 | A |
| 8a1ea92c994ffff | Novi Grad Sarajevo | Zabrđe | 67 | 6,587.600 | 98.300 | A |
| 8a1ef459579ffff | Novo Sarajevo | Pofalići II | 60 | 5,901.400 | 98.400 | B |
| 8a1ef459504ffff | Novo Sarajevo | Velešići | 21 | 2,066.300 | 98.400 | B |
| 8a1ef45955b7fff | Novi Grad Sarajevo | Dolac | 89 | 8,757.400 | 98.400 | A |
| 8a1ef4582d8ffff | Novo Sarajevo | Gornji Velešići | 53 | 5,215.100 | 98.400 | B |
| 8a1ef4582a9ffff | Centar Sarajevo | Breka | 73 | 7,184.000 | 98.400 | B |
| 8a1ef45864effff | Centar Sarajevo | Šip | 63 | 6,199.900 | 98.400 | B |
| 8a1ef45864e7fff | Centar Sarajevo | Šip | 57 | 5,610.700 | 98.400 | B |
| 8a1ef458681ffff | Centar Sarajevo | Betanija | 21 | 2,067.900 | 98.500 | B |
| 8a1ef459464ffff | Novi Grad Sarajevo | Dolac | 121 | 11,917.400 | 98.500 | A |
| 8a1ef4595607fff | Novo Sarajevo | Pofalići II | 59 | 5,814.500 | 98.600 | B |
| 8a1ef458255ffff | Centar Sarajevo | Koševsko Brdo | 126 | 12,417.400 | 98.600 | B |
| 8a1ea92c995ffff | Novi Grad Sarajevo | Zabrđe | 86 | 8,479.700 | 98.600 | A |
| 8a1ef4590257fff | Novo Sarajevo | Hrasno Brdo | 74 | 7,299.200 | 98.600 | B |
| 8a1ef45b24f7fff | Novi Grad Sarajevo | Zabrđe | 26 | 2,565.000 | 98.700 | A |
| 8a1ef459c347fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 43 | 4,242.500 | 98.700 | A |
| 8a1ea92c88b7fff | Novi Grad Sarajevo | Dobroševići | 35 | 3,454.700 | 98.700 | A |
| 8a1ef4595287fff | Novo Sarajevo | Pofalići I | 66 | 6,519.100 | 98.800 | B |
| 8a1ef459558ffff | Novi Grad Sarajevo | Dolac | 90 | 8,891.100 | 98.800 | A |
| 8a1ef4591727fff | Novo Sarajevo | Vraca | 54 | 5,335.400 | 98.800 | B |
| 8a1ef459d197fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 23 | 2,272.600 | 98.800 | A |
| 8a1ef459c097fff | Stari Grad Sarajevo | Širokača | 41 | 4,051.700 | 98.800 | A |
| 8a1ef45942b7fff | Novi Grad Sarajevo | Dolac | 71 | 7,017.500 | 98.800 | A |
| 8a1ef45837b7fff | Stari Grad Sarajevo | Vratnik | 128 | 12,652.900 | 98.900 | A |
| 8a1ea92c9957fff | Novi Grad Sarajevo | Zabrđe | 100 | 9,885.700 | 98.900 | A |
| 8a1ef459c8affff | Stari Grad Sarajevo | Mjedenica | 89 | 8,798.800 | 98.900 | A |
| 8a1ef459429ffff | Novi Grad Sarajevo | Dolac | 96 | 9,493.600 | 98.900 | A |
| 8a1ef459145ffff | Novo Sarajevo | Vraca | 42 | 4,154.000 | 98.900 | B |
| 8a1ef4586797fff | Centar Sarajevo | Šip | 61 | 6,035.500 | 98.900 | B |
| 8a1ef45942e7fff | Novi Grad Sarajevo | Dolac | 82 | 8,113.600 | 98.900 | A |
| 8a1ea92c910ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 18 | 1,781.700 | 99.000 | A |
| 8a1ef4590197fff | Novi Grad Sarajevo | Otoka | 48 | 4,751.500 | 99.000 | A |
| 8a1ea92c9a0ffff | Novi Grad Sarajevo | Zabrđe | 39 | 3,863.600 | 99.100 | A |
| 8a1ef4590107fff | Novi Grad Sarajevo | Alipašin Most III | 95 | 9,415.800 | 99.100 | A |
| 8a1ef459cc1ffff | Centar Sarajevo | Soukbunar | 69 | 6,839.000 | 99.100 | B |
| 8a1ef4593957fff | Novo Sarajevo | Hrasno Brdo | 30 | 2,973.500 | 99.100 | B |
| 8a1ef45804effff | Centar Sarajevo | Pionirska Dolina | 17 | 1,685.200 | 99.100 | B |
| 8a1ef458345ffff | Stari Grad Sarajevo | Vratnik | 140 | 13,888.800 | 99.200 | A |
| 8a1ea92c9117fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 58 | 5,756.200 | 99.200 | A |
| 8a1ef4594297fff | Novi Grad Sarajevo | Dolac | 84 | 8,338.400 | 99.300 | A |
| 8a1ef459426ffff | Novi Grad Sarajevo | Dolac | 61 | 6,056.300 | 99.300 | A |
| 8a1ef4592c47fff | Novi Grad Sarajevo | Dobrinja A | 74 | 7,349.100 | 99.300 | A |
| 8a1ea92c9a5ffff | Novi Grad Sarajevo | Zabrđe | 37 | 3,675.700 | 99.300 | A |
| 8a1ef45b250ffff | Novi Grad Sarajevo | Zabrđe | 52 | 5,166.200 | 99.400 | A |
| 8a1ef459cd8ffff | Centar Sarajevo | Soukbunar | 110 | 10,930.800 | 99.400 | B |
| 8a1ea92c9a07fff | Novi Grad Sarajevo | Zabrđe | 51 | 5,069.000 | 99.400 | A |
| 8a1ef4595787fff | Novo Sarajevo | Pofalići II | 56 | 5,566.200 | 99.400 | B |
| 8a1ea92c9a57fff | Novi Grad Sarajevo | Zabrđe | 50 | 4,970.800 | 99.400 | A |
| 8a1ef4592987fff | Novi Grad Sarajevo | Saraj Polje | 121 | 12,032.700 | 99.400 | A |
| 8a1ef45826a7fff | Centar Sarajevo | Trg oslobođenja-Centar | 133 | 13,234.800 | 99.500 | B |
| 8a1ef4583757fff | Stari Grad Sarajevo | Mošćanica | 13 | 1,293.600 | 99.500 | A |
| 8a1ea92c9ba7fff | Novi Grad Sarajevo | Zabrđe | 75 | 7,466.500 | 99.600 | A |
| 8a1ea92c984ffff | Novi Grad Sarajevo | Zabrđe | 66 | 6,571.000 | 99.600 | A |
| 8a1ef4595587fff | Novi Grad Sarajevo | Dolac | 99 | 9,857.900 | 99.600 | A |
| 8a1ef459535ffff | Novo Sarajevo | Velešići | 53 | 5,278.600 | 99.600 | B |
| 8a1ef4584107fff | Centar Sarajevo | Nahorevo | 15 | 1,494.500 | 99.600 | B |
| 8a1ef4595d8ffff | Novi Grad Sarajevo | Dolac | 14 | 1,395.000 | 99.600 | A |
| 8a1ef45968cffff | Novi Grad Sarajevo | Briješće | 119 | 11,857.700 | 99.600 | A |
| 8a1ef459092ffff | Novi Grad Sarajevo | Dolac | 133 | 13,254.800 | 99.700 | A |
| 8a1ef4590b27fff | Novo Sarajevo | Pofalići II | 64 | 6,378.700 | 99.700 | B |
| 8a1ef45942a7fff | Novi Grad Sarajevo | Dolac | 78 | 7,776.900 | 99.700 | A |
| 8a1ef45952dffff | Novo Sarajevo | Pofalići I | 74 | 7,378.400 | 99.700 | B |
| 8a1ef4594257fff | Novi Grad Sarajevo | Dolac | 91 | 9,073.800 | 99.700 | A |
| 8a1ef4591557fff | Novo Sarajevo | Hrasno Brdo | 66 | 6,582.800 | 99.700 | B |
| 8a1ea92cd28ffff | Novi Grad Sarajevo | Zabrđe | 63 | 6,283.900 | 99.700 | A |
| 8a1ef4582c47fff | Centar Sarajevo | Koševsko Brdo | 80 | 7,980.900 | 99.800 | B |
| 8a1ef4595637fff | Novo Sarajevo | Pofalići II | 60 | 5,989.200 | 99.800 | B |
| 8a1ef4596c2ffff | Novi Grad Sarajevo | Briješće | 10 | 998.400 | 99.800 | A |
| 8a1ef458388ffff | Stari Grad Sarajevo | Sedrenik | 38 | 3,794.200 | 99.800 | A |
| 8a1ef45957b7fff | Novo Sarajevo | Pofalići II | 50 | 4,994.900 | 99.900 | B |
| 8a1ea92c9d47fff | Novi Grad Sarajevo | Zabrđe | 45 | 4,495.600 | 99.900 | A |
| 8a1ea92c9727fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 57 | 5,695.400 | 99.900 | A |
| 8a1ef4591a9ffff | Novo Sarajevo | Kovačići | 126 | 12,589.700 | 99.900 | B |
| 8a1ea92c9ae7fff | Novi Grad Sarajevo | Zabrđe | 49 | 4,899.800 | 100.000 | A |
| 8a1ef4586477fff | Centar Sarajevo | Šip | 55 | 5,504.100 | 100.100 | B |
| 8a1ea92c9847fff | Novi Grad Sarajevo | Zabrđe | 80 | 8,007.600 | 100.100 | A |
| 8a1ea92c986ffff | Novi Grad Sarajevo | Zabrđe | 76 | 7,607.200 | 100.100 | A |
| 8a1ef458359ffff | Stari Grad Sarajevo | Logavina | 161 | 16,117.500 | 100.100 | A |
| 8a1ef4582af7fff | Centar Sarajevo | Breka | 73 | 7,308.400 | 100.100 | B |
| 8a1ef4591587fff | Novo Sarajevo | Hrasno Brdo | 56 | 5,607.300 | 100.100 | B |
| 8a1ef45838affff | Stari Grad Sarajevo | Sedrenik | 21 | 2,103.600 | 100.200 | A |
| 8a1ef4595557fff | Novi Grad Sarajevo | Dolac | 58 | 5,811.100 | 100.200 | A |
| 8a1ef4594217fff | Novi Grad Sarajevo | Dolac | 82 | 8,218.900 | 100.200 | A |
| 8a1ef45942f7fff | Novi Grad Sarajevo | Dolac | 97 | 9,727.100 | 100.300 | A |
| 8a1ef45954effff | Novo Sarajevo | Pofalići II | 41 | 4,113.700 | 100.300 | B |
| 8a1ef4592ab7fff | Novi Grad Sarajevo | Dobrinja C | 58 | 5,821.900 | 100.400 | A |
| 8a1ef4592d9ffff | Novi Grad Sarajevo | Dobrinja A | 109 | 10,958.500 | 100.500 | A |
| 8a1ef45910affff | Novo Sarajevo | Vraca | 81 | 8,153.800 | 100.700 | B |
| 8a1ef45952e7fff | Novo Sarajevo | Velešići | 72 | 7,248.000 | 100.700 | B |
| 8a1ef4580517fff | Centar Sarajevo | Pionirska Dolina | 50 | 5,034.700 | 100.700 | B |
| 8a1ef4594277fff | Novi Grad Sarajevo | Dolac | 66 | 6,652.900 | 100.800 | A |
| 8a1ef45955a7fff | Novi Grad Sarajevo | Dolac | 110 | 11,088.800 | 100.800 | A |
| 8a1ef4594d87fff | Novi Grad Sarajevo | Zabrđe | 31 | 3,125.100 | 100.800 | A |
| 8a1ea92c919ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 44 | 4,442.300 | 101.000 | A |
| 8a1ea92c90f7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 40 | 4,038.800 | 101.000 | A |
| 8a1ef459c887fff | Stari Grad Sarajevo | Mjedenica | 90 | 9,087.900 | 101.000 | A |
| 8a1ef4586837fff | Centar Sarajevo | Betanija | 11 | 1,110.700 | 101.000 | B |
| 8a1ef4582717fff | Centar Sarajevo | Džidžikovac-Koševo I | 123 | 12,434.500 | 101.100 | B |
| 8a1ef4595217fff | Novo Sarajevo | Pofalići I | 63 | 6,369.000 | 101.100 | B |
| 8a1ef4582c87fff | Novo Sarajevo | Gornji Velešići | 67 | 6,776.600 | 101.100 | B |
| 8a1ef459c077fff | Stari Grad Sarajevo | Toka-Džeka | 95 | 9,613.300 | 101.200 | A |
| 8a1ef4582c07fff | Novo Sarajevo | Gornji Velešići | 87 | 8,805.600 | 101.200 | B |
| 8a1ef459576ffff | Novo Sarajevo | Pofalići I | 60 | 6,073.400 | 101.200 | B |
| 8a1ef4582547fff | Centar Sarajevo | Koševsko Brdo | 158 | 15,993.700 | 101.200 | B |
| 8a1ef45827a7fff | Centar Sarajevo | Crni Vrh-Gorica | 94 | 9,519.800 | 101.300 | B |
| 8a1ef4595737fff | Novo Sarajevo | Pofalići II | 34 | 3,445.100 | 101.300 | B |
| 8a1ef45822affff | Centar Sarajevo | Mejtaš-Bjelave | 97 | 9,834.400 | 101.400 | B |
| 8a1ef459528ffff | Novo Sarajevo | Pofalići I | 73 | 7,401.500 | 101.400 | B |
| 8a1ef458316ffff | Stari Grad Sarajevo | Mošćanica | 14 | 1,420.000 | 101.400 | A |
| 8a1ef4591327fff | Novo Sarajevo | Gornji Kovačići | 65 | 6,593.000 | 101.400 | B |
| 8a1ef4591ad7fff | Novo Sarajevo | Kovačići | 83 | 8,419.700 | 101.400 | B |
| 8a1ef4583287fff | Stari Grad Sarajevo | Mošćanica | 14 | 1,420.300 | 101.500 | A |
| 8a1ef4594ca7fff | Novi Grad Sarajevo | Zabrđe | 25 | 2,536.800 | 101.500 | A |
| 8a1ea92cd5affff | Novi Grad Sarajevo | Dobroševići | 11 | 1,116.200 | 101.500 | A |
| 8a1ef459cc9ffff | Centar Sarajevo | Soukbunar | 59 | 5,987.400 | 101.500 | B |
| 8a1ef4582cdffff | Centar Sarajevo | Koševsko Brdo | 188 | 19,084.400 | 101.500 | B |
| 8a1ef4594db7fff | Novi Grad Sarajevo | Zabrđe | 50 | 5,075.800 | 101.500 | A |
| 8a1ef458442ffff | Centar Sarajevo | Betanija | 15 | 1,523.000 | 101.500 | B |
| 8a1ef45952a7fff | Novo Sarajevo | Pofalići I | 67 | 6,802.900 | 101.500 | B |
| 8a1ea92cd0dffff | Novi Grad Sarajevo | Reljevo | 54 | 5,483.600 | 101.500 | A |
| 8a1ef45942affff | Novi Grad Sarajevo | Dolac | 114 | 11,577.000 | 101.600 | A |
| 8a1ef4582807fff | Centar Sarajevo | Betanija | 100 | 10,157.100 | 101.600 | B |
| 8a1ef4591a4ffff | Centar Sarajevo | Skenderija-Podtekija | 82 | 8,333.100 | 101.600 | B |
| 8a1ef4582b67fff | Centar Sarajevo | Hrastovi-Mrkovići | 42 | 4,270.800 | 101.700 | B |
| 8a1ea92eb08ffff | Novi Grad Sarajevo | Reljevo | 12 | 1,220.400 | 101.700 | A |
| 8a1ef458691ffff | Centar Sarajevo | Betanija | 16 | 1,627.300 | 101.700 | B |
| 8a1ef4591237fff | Novo Sarajevo | Gornji Kovačići | 35 | 3,560.500 | 101.700 | B |
| 8a1ef459101ffff | Novo Sarajevo | Vraca | 82 | 8,342.200 | 101.700 | B |
| 8a1ea92c9a37fff | Novi Grad Sarajevo | Zabrđe | 81 | 8,241.700 | 101.700 | A |
| 8a1ea92c9aa7fff | Novi Grad Sarajevo | Zabrđe | 82 | 8,347.400 | 101.800 | A |
| 8a1ef45955affff | Novi Grad Sarajevo | Dolac | 121 | 12,318.900 | 101.800 | A |
| 8a1ef4595aaffff | Novo Sarajevo | Velešići | 20 | 2,036.300 | 101.800 | B |
| 8a1ef459010ffff | Novi Grad Sarajevo | Alipašin Most III | 104 | 10,597.700 | 101.900 | A |
| 8a1ef45952affff | Novo Sarajevo | Pofalići I | 73 | 7,438.800 | 101.900 | B |
| 8a1ef458256ffff | Centar Sarajevo | Koševsko Brdo | 166 | 16,915.800 | 101.900 | B |
| 8a1ea92c972ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 56 | 5,706.800 | 101.900 | A |
| 8a1ef4582a07fff | Centar Sarajevo | Hrastovi-Mrkovići | 60 | 6,114.800 | 101.900 | B |
| 8a1ef459dc07fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 42 | 4,281.800 | 101.900 | A |
| 8a1ef459c00ffff | Stari Grad Sarajevo | Toka-Džeka | 88 | 8,973.000 | 102.000 | A |
| 8a1ef458378ffff | Stari Grad Sarajevo | Vratnik | 100 | 10,196.800 | 102.000 | A |
| 8a1ef45952b7fff | Novo Sarajevo | Pofalići I | 70 | 7,142.900 | 102.000 | B |
| 8a1ef459524ffff | Novo Sarajevo | Velešići | 86 | 8,777.400 | 102.100 | B |
| 8a1ef4582357fff | Centar Sarajevo | Bardakčije | 84 | 8,580.800 | 102.200 | B |
| 8a1ef459142ffff | Novo Sarajevo | Vraca | 71 | 7,256.200 | 102.200 | B |
| 8a1ef4595317fff | Novo Sarajevo | Pofalići I | 23 | 2,350.900 | 102.200 | B |
| 8a1ef4591397fff | Novo Sarajevo | Gornji Kovačići | 47 | 4,804.300 | 102.200 | B |
| 8a1ef4592d1ffff | Novi Grad Sarajevo | Dobrinja A | 57 | 5,828.300 | 102.300 | A |
| 8a1ef4583c5ffff | Stari Grad Sarajevo | Sumbuluša | 93 | 9,511.300 | 102.300 | A |
| 8a1ef458371ffff | Stari Grad Sarajevo | Vratnik | 102 | 10,438.200 | 102.300 | A |
| 8a1ef4591257fff | Centar Sarajevo | Soukbunar | 15 | 1,536.300 | 102.400 | B |
| 8a1ef45821b7fff | Centar Sarajevo | Koševsko Brdo | 109 | 11,165.600 | 102.400 | B |
| 8a1ef4595b67fff | Centar Sarajevo | Šip | 55 | 5,635.000 | 102.500 | B |
| 8a1ef458240ffff | Centar Sarajevo | Koševsko Brdo | 143 | 14,651.700 | 102.500 | B |
| 8a1ef45952f7fff | Novo Sarajevo | Pofalići I | 76 | 7,787.400 | 102.500 | B |
| 8a1ef45835affff | Stari Grad Sarajevo | Medrese | 131 | 13,425.400 | 102.500 | A |
| 8a1ef45b2477fff | Novi Grad Sarajevo | Zabrđe | 50 | 5,126.900 | 102.500 | A |
| 8a1ea92c9b67fff | Novi Grad Sarajevo | Zabrđe | 10 | 1,025.600 | 102.600 | A |
| 8a1ef4595427fff | Novi Grad Sarajevo | Dolac | 102 | 10,464.400 | 102.600 | A |
| 8a1ef45824cffff | Centar Sarajevo | Crni Vrh-Gorica | 85 | 8,720.700 | 102.600 | B |
| 8a1ef45827affff | Centar Sarajevo | Džidžikovac-Koševo I | 104 | 10,678.100 | 102.700 | B |
| 8a1ef4582c97fff | Novo Sarajevo | Gornji Velešići | 75 | 7,702.800 | 102.700 | B |
| 8a1ef4582927fff | Centar Sarajevo | Betanija | 36 | 3,698.400 | 102.700 | B |
| 8a1ef45834f7fff | Stari Grad Sarajevo | Kovači | 74 | 7,603.400 | 102.700 | A |
| 8a1ef458244ffff | Centar Sarajevo | Ciglane | 95 | 9,762.800 | 102.800 | B |
| 8a1ef45821a7fff | Centar Sarajevo | Koševsko Brdo | 196 | 20,144.800 | 102.800 | B |
| 8a1ef459420ffff | Novi Grad Sarajevo | Dolac | 130 | 13,364.400 | 102.800 | A |
| 8a1ef4582b9ffff | Centar Sarajevo | Breka | 115 | 11,824.300 | 102.800 | B |
| 8a1ef45912affff | Novo Sarajevo | Gornji Kovačići | 28 | 2,880.000 | 102.900 | B |
| 8a1ef4580627fff | Centar Sarajevo | Hrastovi-Mrkovići | 10 | 1,028.600 | 102.900 | B |
| 8a1ef459550ffff | Novi Grad Sarajevo | Dolac | 87 | 8,950.800 | 102.900 | A |
| 8a1ef4595357fff | Novo Sarajevo | Velešići | 42 | 4,321.300 | 102.900 | B |
| 8a1ef45847affff | Centar Sarajevo | Betanija | 12 | 1,234.700 | 102.900 | B |
| 8a1ef459cb17fff | Stari Grad Sarajevo | Bistrik | 249 | 25,627.300 | 102.900 | A |
| 8a1ef458636ffff | Centar Sarajevo | Betanija | 11 | 1,132.500 | 103.000 | B |
| 8a1ef4591387fff | Novo Sarajevo | Gornji Kovačići | 54 | 5,559.600 | 103.000 | B |
| 8a1ef459421ffff | Novi Grad Sarajevo | Dolac | 138 | 14,211.900 | 103.000 | A |
| 8a1ef458284ffff | Centar Sarajevo | Koševo II | 64 | 6,595.100 | 103.000 | B |
| 8a1ef4582d6ffff | Centar Sarajevo | Koševsko Brdo | 68 | 7,009.600 | 103.100 | B |
| 8a1ef459c817fff | Stari Grad Sarajevo | Ferhadija | 133 | 13,710.000 | 103.100 | A |
| 8a1ef4583aeffff | Stari Grad Sarajevo | Mošćanica | 13 | 1,340.400 | 103.100 | A |
| 8a1ef4591317fff | Novo Sarajevo | Gornji Kovačići | 69 | 7,114.500 | 103.100 | B |
| 8a1ef459121ffff | Novo Sarajevo | Gornji Kovačići | 23 | 2,371.600 | 103.100 | B |
| 8a1ef459dc8ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 22 | 2,269.000 | 103.100 | A |
| 8a1ef459126ffff | Centar Sarajevo | Soukbunar | 45 | 4,642.700 | 103.200 | B |
| 8a1ef459136ffff | Centar Sarajevo | Soukbunar | 68 | 7,016.400 | 103.200 | B |
| 8a1ef45824d7fff | Centar Sarajevo | Crni Vrh-Gorica | 98 | 10,113.300 | 103.200 | B |
| 8a1ea92c90dffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 28 | 2,890.000 | 103.200 | A |
| 8a1ef459525ffff | Novo Sarajevo | Velešići | 88 | 9,088.600 | 103.300 | B |
| 8a1ea92cd217fff | Novi Grad Sarajevo | Zabrđe | 200 | 20,680.800 | 103.400 | A |
| 8a1ef4591477fff | Novo Sarajevo | Vraca | 67 | 6,928.700 | 103.400 | B |
| 8a1ef458231ffff | Centar Sarajevo | Bardakčije | 146 | 15,099.000 | 103.400 | B |
| 8a1ef4584527fff | Centar Sarajevo | Betanija | 12 | 1,241.600 | 103.500 | B |
| 8a1ef4586a5ffff | Centar Sarajevo | Betanija | 17 | 1,759.600 | 103.500 | B |
| 8a1ea92c965ffff | Novi Grad Sarajevo | Briješće | 106 | 10,972.500 | 103.500 | A |
| 8a1ef45968a7fff | Novi Grad Sarajevo | Briješće | 14 | 1,450.200 | 103.600 | A |
| 8a1ef459cc8ffff | Centar Sarajevo | Soukbunar | 64 | 6,630.700 | 103.600 | B |
| 8a1ef459140ffff | Novo Sarajevo | Vraca | 64 | 6,633.400 | 103.600 | B |
| 8a1ef459529ffff | Novo Sarajevo | Pofalići I | 91 | 9,433.800 | 103.700 | B |
| 8a1ef458680ffff | Centar Sarajevo | Betanija | 12 | 1,244.500 | 103.700 | B |
| 8a1ef4591057fff | Novo Sarajevo | Grbavica I | 85 | 8,816.700 | 103.700 | B |
| 8a1ef45826f7fff | Centar Sarajevo | Trg oslobođenja-Centar | 159 | 16,492.700 | 103.700 | B |
| 8a1ea92c96e7fff | Novi Grad Sarajevo | Briješće | 14 | 1,452.400 | 103.700 | A |
| 8a1ef459681ffff | Novi Grad Sarajevo | Briješće | 20 | 2,075.200 | 103.800 | A |
| 8a1ef458219ffff | Centar Sarajevo | Ciglane | 151 | 15,670.600 | 103.800 | B |
| 8a1ef4583c6ffff | Stari Grad Sarajevo | Sedrenik | 66 | 6,851.900 | 103.800 | A |
| 8a1ef45914effff | Novo Sarajevo | Vraca | 21 | 2,180.200 | 103.800 | B |
| 8a1ef459ccaffff | Centar Sarajevo | Soukbunar | 71 | 7,374.700 | 103.900 | B |
| 8a1ef4596117fff | Novi Grad Sarajevo | Briješće | 95 | 9,867.900 | 103.900 | A |
| 8a1ef45915b7fff | Novo Sarajevo | Hrasno Brdo | 67 | 6,959.400 | 103.900 | B |
| 8a1ef459459ffff | Novi Grad Sarajevo | Briješće | 11 | 1,143.400 | 103.900 | A |
| 8a1ef4595a27fff | Centar Sarajevo | Šip | 28 | 2,911.600 | 104.000 | B |
| 8a1ef459c86ffff | Stari Grad Sarajevo | Baščaršija | 107 | 11,129.700 | 104.000 | A |
| 8a1ef4591457fff | Novo Sarajevo | Vraca | 66 | 6,865.300 | 104.000 | B |
| 8a1ef4592d0ffff | Novi Grad Sarajevo | Dobrinja A | 54 | 5,617.300 | 104.000 | A |
| 8a1ef4586707fff | Centar Sarajevo | Šip | 106 | 11,026.800 | 104.000 | B |
| 8a1ef4586787fff | Centar Sarajevo | Šip | 75 | 7,802.400 | 104.000 | B |
| 8a1ef4582067fff | Centar Sarajevo | Koševo II | 75 | 7,804.300 | 104.100 | B |
| 8a1ef45950cffff | Novo Sarajevo | Pofalići I | 49 | 5,104.200 | 104.200 | B |
| 8a1ef4586a47fff | Centar Sarajevo | Betanija | 11 | 1,145.900 | 104.200 | B |
| 8a1ef4583c67fff | Stari Grad Sarajevo | Sedrenik | 68 | 7,084.800 | 104.200 | A |
| 8a1ef4582d1ffff | Novo Sarajevo | Gornji Velešići | 65 | 6,772.600 | 104.200 | B |
| 8a1ef458296ffff | Centar Sarajevo | Koševo II | 105 | 10,949.800 | 104.300 | B |
| 8a1ef459025ffff | Novo Sarajevo | Hrasno Brdo | 84 | 8,762.800 | 104.300 | B |
| 8a1ef459539ffff | Novo Sarajevo | Pofalići I | 64 | 6,676.600 | 104.300 | B |
| 8a1ef45957affff | Novo Sarajevo | Pofalići II | 69 | 7,198.800 | 104.300 | B |
| 8a1ef4595727fff | Novo Sarajevo | Pofalići II | 43 | 4,486.300 | 104.300 | B |
| 8a1ea92cd08ffff | Novi Grad Sarajevo | Reljevo | 10 | 1,043.400 | 104.300 | A |
| 8a1ef4591097fff | Novo Sarajevo | Vraca | 81 | 8,452.700 | 104.400 | B |
| 8a1ef459526ffff | Novo Sarajevo | Velešići | 84 | 8,769.000 | 104.400 | B |
| 8a1ef4593967fff | Novo Sarajevo | Hrasno Brdo | 55 | 5,743.200 | 104.400 | B |
| 8a1ef4582537fff | Novo Sarajevo | Velešići | 99 | 10,337.900 | 104.400 | B |
| 8a1ef459566ffff | Novo Sarajevo | Pofalići I | 100 | 10,447.200 | 104.500 | B |
| 8a1ef45915affff | Novo Sarajevo | Hrasno Brdo | 78 | 8,150.400 | 104.500 | B |
| 8a1ef4582ab7fff | Centar Sarajevo | Breka | 181 | 18,915.000 | 104.500 | B |
| 8a1ef4583767fff | Stari Grad Sarajevo | Mošćanica | 14 | 1,463.700 | 104.500 | A |
| 8a1ef458222ffff | Centar Sarajevo | Bardakčije | 91 | 9,517.400 | 104.600 | B |
| 8a1ef4586247fff | Centar Sarajevo | Betanija | 24 | 2,510.100 | 104.600 | B |
| 8a1ef4585477fff | Centar Sarajevo | Betanija | 11 | 1,150.900 | 104.600 | B |
| 8a1ef4591217fff | Novo Sarajevo | Gornji Kovačići | 31 | 3,246.200 | 104.700 | B |
| 8a1ef45804dffff | Centar Sarajevo | Hrastovi-Mrkovići | 42 | 4,398.700 | 104.700 | B |
| 8a1ef459538ffff | Novo Sarajevo | Pofalići I | 61 | 6,389.200 | 104.700 | B |
| 8a1ef4594417fff | Novi Grad Sarajevo | Briješće | 22 | 2,304.400 | 104.700 | A |
| 8a1ef458232ffff | Centar Sarajevo | Bardakčije | 85 | 8,915.900 | 104.900 | B |
| 8a1ef4595297fff | Novo Sarajevo | Pofalići I | 96 | 10,070.700 | 104.900 | B |
| 8a1ef459534ffff | Novo Sarajevo | Velešići | 70 | 7,344.400 | 104.900 | B |
| 8a1ef45902dffff | Novo Sarajevo | Hrasno Brdo | 66 | 6,926.000 | 104.900 | B |
| 8a1ef45910effff | Novo Sarajevo | Vraca | 74 | 7,766.800 | 105.000 | B |
| 8a1ef45837affff | Stari Grad Sarajevo | Vratnik | 108 | 11,339.600 | 105.000 | A |
| 8a1ef45910f7fff | Novo Sarajevo | Vraca | 81 | 8,506.700 | 105.000 | B |
| 8a1ef4582787fff | Centar Sarajevo | Crni Vrh-Gorica | 107 | 11,247.100 | 105.100 | B |
| 8a1ef45902effff | Novo Sarajevo | Hrasno Brdo | 84 | 8,829.600 | 105.100 | B |
| 8a1ef45854d7fff | Centar Sarajevo | Betanija | 17 | 1,788.600 | 105.200 | B |
| 8a1ef458449ffff | Centar Sarajevo | Betanija | 10 | 1,052.500 | 105.200 | B |
| 8a1ef4583c4ffff | Stari Grad Sarajevo | Sedrenik | 75 | 7,895.600 | 105.300 | A |
| 8a1ef4591b27fff | Centar Sarajevo | Crni Vrh-Gorica | 268 | 28,218.000 | 105.300 | B |
| 8a1ef4592c2ffff | Novi Grad Sarajevo | Dobrinja A | 63 | 6,640.800 | 105.400 | A |
| 8a1ef45913a7fff | Novo Sarajevo | Gornji Kovačići | 77 | 8,118.500 | 105.400 | B |
| 8a1ef4591b8ffff | Centar Sarajevo | Marijin Dvor | 68 | 7,171.000 | 105.500 | B |
| 8a1ef4582967fff | Centar Sarajevo | Betanija | 43 | 4,535.000 | 105.500 | B |
| 8a1ef4582227fff | Centar Sarajevo | Bardakčije | 105 | 11,076.500 | 105.500 | B |
| 8a1ef458262ffff | Centar Sarajevo | Džidžikovac-Koševo I | 160 | 16,878.600 | 105.500 | B |
| 8a1ef4595a77fff | Novo Sarajevo | Gornji Velešići | 37 | 3,903.400 | 105.500 | B |
| 8a1ef4582bb7fff | Centar Sarajevo | Koševo II | 80 | 8,440.700 | 105.500 | B |
| 8a1ef4582caffff | Novo Sarajevo | Gornji Velešići | 78 | 8,230.100 | 105.500 | B |
| 8a1ef4583b47fff | Stari Grad Sarajevo | Mošćanica | 14 | 1,477.700 | 105.500 | A |
| 8a1ef4580c9ffff | Centar Sarajevo | Pionirska Dolina | 38 | 4,010.800 | 105.500 | B |
| 8a1ea92c905ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 70 | 7,389.800 | 105.600 | A |
| 8a1ef45956b7fff | Novo Sarajevo | Pofalići II | 90 | 9,502.600 | 105.600 | B |
| 8a1ef4591737fff | Novo Sarajevo | Vraca | 59 | 6,234.400 | 105.700 | B |
| 8a1ef459158ffff | Novo Sarajevo | Vraca | 67 | 7,080.300 | 105.700 | B |
| 8a1ef459544ffff | Novo Sarajevo | Pofalići II | 51 | 5,390.900 | 105.700 | B |
| 8a1ef4582217fff | Centar Sarajevo | Bardakčije | 137 | 14,489.900 | 105.800 | B |
| 8a1ef4596987fff | Novi Grad Sarajevo | Briješće | 17 | 1,798.700 | 105.800 | A |
| 8a1ef4590167fff | Novo Sarajevo | Kvadrant | 165 | 17,461.400 | 105.800 | B |
| 8a1ef45837a7fff | Stari Grad Sarajevo | Vratnik | 136 | 14,395.200 | 105.800 | A |
| 8a1ef459c8b7fff | Centar Sarajevo | Skenderija-Podtekija | 195 | 20,642.800 | 105.900 | B |
| 8a1ef45914a7fff | Novo Sarajevo | Hrasno Brdo | 60 | 6,351.900 | 105.900 | B |
| 8a1ef4586637fff | Centar Sarajevo | Šip | 116 | 12,283.600 | 105.900 | B |
| 8a1ef4595347fff | Novo Sarajevo | Velešići | 60 | 6,353.700 | 105.900 | B |
| 8a1ef4591307fff | Novo Sarajevo | Gornji Kovačići | 71 | 7,525.600 | 106.000 | B |
| 8a1ef45906effff | Novo Sarajevo | Hrasno Brdo | 57 | 6,042.800 | 106.000 | B |
| 8a1ef4591517fff | Novo Sarajevo | Hrasno Brdo | 95 | 10,075.600 | 106.100 | B |
| 8a1ef4582a77fff | Centar Sarajevo | Hrastovi-Mrkovići | 58 | 6,154.000 | 106.100 | B |
| 8a1ef45826effff | Centar Sarajevo | Trg oslobođenja-Centar | 138 | 14,645.700 | 106.100 | B |
| 8a1ef4596b87fff | Novi Grad Sarajevo | Briješće | 24 | 2,547.800 | 106.200 | A |
| 8a1ef459134ffff | Centar Sarajevo | Soukbunar | 67 | 7,114.500 | 106.200 | B |
| 8a1ef4591bb7fff | Novo Sarajevo | Željeznička | 60 | 6,374.100 | 106.200 | B |
| 8a1ef45864f7fff | Centar Sarajevo | Šip | 55 | 5,843.400 | 106.200 | B |
| 8a1ef4582ca7fff | Novo Sarajevo | Gornji Velešići | 81 | 8,606.300 | 106.300 | B |
| 8a1ef459cc87fff | Centar Sarajevo | Soukbunar | 72 | 7,650.100 | 106.300 | B |
| 8a1ef45826cffff | Centar Sarajevo | Trg oslobođenja-Centar | 192 | 20,405.700 | 106.300 | B |
| 8a1ef4591467fff | Novo Sarajevo | Vraca | 82 | 8,716.600 | 106.300 | B |
| 8a1ef458272ffff | Centar Sarajevo | Park-Višnjik | 112 | 11,909.400 | 106.300 | B |
| 8a1ef459cca7fff | Centar Sarajevo | Soukbunar | 77 | 8,197.400 | 106.500 | B |
| 8a1ef45939a7fff | Novo Sarajevo | Hrasno Brdo | 55 | 5,855.300 | 106.500 | B |
| 8a1ef459cd2ffff | Centar Sarajevo | Skenderija-Podtekija | 173 | 18,418.400 | 106.500 | B |
| 8a1ef458279ffff | Centar Sarajevo | Crni Vrh-Gorica | 118 | 12,564.300 | 106.500 | B |
| 8a1ef458409ffff | Centar Sarajevo | Nahorevo | 19 | 2,023.900 | 106.500 | B |
| 8a1ef459c527fff | Centar Sarajevo | Soukbunar | 43 | 4,581.700 | 106.600 | B |
| 8a1ef4582577fff | Centar Sarajevo | Koševsko Brdo | 223 | 23,769.300 | 106.600 | B |
| 8a1ef45915a7fff | Novo Sarajevo | Hrasno Brdo | 95 | 10,131.500 | 106.600 | B |
| 8a1ef4595757fff | Novo Sarajevo | Pofalići II | 83 | 8,851.800 | 106.600 | B |
| 8a1ef4583c2ffff | Stari Grad Sarajevo | Sedrenik | 84 | 8,961.400 | 106.700 | A |
| 8a1ef4582327fff | Centar Sarajevo | Breka | 85 | 9,069.200 | 106.700 | B |
| 8a1ef459571ffff | Novo Sarajevo | Pofalići II | 76 | 8,110.300 | 106.700 | B |
| 8a1ef459131ffff | Novo Sarajevo | Gornji Kovačići | 72 | 7,685.400 | 106.700 | B |
| 8a1ef459065ffff | Novo Sarajevo | Hrasno Brdo | 81 | 8,648.600 | 106.800 | B |
| 8a1ef4595747fff | Novo Sarajevo | Pofalići I | 84 | 8,970.600 | 106.800 | B |
| 8a1ef4586717fff | Centar Sarajevo | Šip | 169 | 18,053.400 | 106.800 | B |
| 8a1ef4582877fff | Centar Sarajevo | Koševo II | 69 | 7,374.000 | 106.900 | B |
| 8a1ef45828effff | Centar Sarajevo | Koševo II | 102 | 10,900.800 | 106.900 | B |
| 8a1ea92c90b7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 20 | 2,137.800 | 106.900 | A |
| 8a1ef45957a7fff | Novo Sarajevo | Pofalići II | 65 | 6,947.800 | 106.900 | B |
| 8a1ef45846d7fff | Centar Sarajevo | Betanija | 17 | 1,817.300 | 106.900 | B |
| 8a1ef45902cffff | Novo Sarajevo | Hrasno Brdo | 73 | 7,804.800 | 106.900 | B |
| 8a1ef4591407fff | Novo Sarajevo | Vraca | 76 | 8,126.400 | 106.900 | B |
| 8a1ef4582c77fff | Centar Sarajevo | Koševsko Brdo | 84 | 8,983.300 | 106.900 | B |
| 8a1ef459c98ffff | Centar Sarajevo | Trg oslobođenja-Centar | 175 | 18,725.000 | 107.000 | B |
| 8a1ef458071ffff | Centar Sarajevo | Hrastovi-Mrkovići | 21 | 2,247.600 | 107.000 | B |
| 8a1ef4591b2ffff | Centar Sarajevo | Crni Vrh-Gorica | 269 | 28,793.400 | 107.000 | B |
| 8a1ef45828cffff | Centar Sarajevo | Koševo II | 86 | 9,207.800 | 107.100 | B |
| 8a1ef458671ffff | Centar Sarajevo | Šip | 165 | 17,685.000 | 107.200 | B |
| 8a1ef4592c0ffff | Novi Grad Sarajevo | Dobrinja A | 69 | 7,413.100 | 107.400 | A |
| 8a1ef459c96ffff | Stari Grad Sarajevo | Logavina | 165 | 17,727.400 | 107.400 | A |
| 8a1ef458344ffff | Stari Grad Sarajevo | Vratnik | 129 | 13,862.200 | 107.500 | A |
| 8a1ea92cc60ffff | Novi Grad Sarajevo | Dobroševići | 17 | 1,827.000 | 107.500 | A |
| 8a1ef4591437fff | Novo Sarajevo | Hrasno Brdo | 81 | 8,706.800 | 107.500 | B |
| 8a1ef459024ffff | Novo Sarajevo | Hrasno Brdo | 111 | 11,932.400 | 107.500 | B |
| 8a1ef4592d8ffff | Novi Grad Sarajevo | Dobrinja A | 120 | 12,904.000 | 107.500 | A |
| 8a1ef4592d6ffff | Novi Grad Sarajevo | Saraj Polje | 41 | 4,410.200 | 107.600 | A |
| 8a1ef45869affff | Centar Sarajevo | Betanija | 10 | 1,075.700 | 107.600 | B |
| 8a1ef4592d4ffff | Novi Grad Sarajevo | Saraj Polje | 47 | 5,056.100 | 107.600 | A |
| 8a1ef4592c87fff | Novi Grad Sarajevo | Dobrinja A | 16 | 1,721.800 | 107.600 | A |
| 8a1ef4591597fff | Novo Sarajevo | Hrasno Brdo | 72 | 7,750.100 | 107.600 | B |
| 8a1ef459cd4ffff | Centar Sarajevo | Skenderija-Podtekija | 170 | 18,312.100 | 107.700 | B |
| 8a1ef458415ffff | Centar Sarajevo | Nahorevo | 11 | 1,185.500 | 107.800 | B |
| 8a1ef4591417fff | Novo Sarajevo | Vraca | 74 | 7,975.900 | 107.800 | B |
| 8a1ef45913b7fff | Novo Sarajevo | Gornji Kovačići | 80 | 8,625.300 | 107.800 | B |
| 8a1ef45828dffff | Centar Sarajevo | Koševo II | 185 | 19,947.000 | 107.800 | B |
| 8a1ef459159ffff | Novo Sarajevo | Hrasno Brdo | 72 | 7,767.500 | 107.900 | B |
| 8a1ef458662ffff | Centar Sarajevo | Šip | 76 | 8,200.800 | 107.900 | B |
| 8a1ef459dc37fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 40 | 4,318.700 | 108.000 | A |
| 8a1ef4582267fff | Stari Grad Sarajevo | Logavina | 144 | 15,553.500 | 108.000 | A |
| 8a1ef4593977fff | Novo Sarajevo | Hrasno Brdo | 65 | 7,024.800 | 108.100 | B |
| 8a1ef459699ffff | Novi Grad Sarajevo | Briješće | 35 | 3,783.700 | 108.100 | A |
| 8a1ef4582307fff | Centar Sarajevo | Bardakčije | 95 | 10,277.300 | 108.200 | B |
| 8a1ef459570ffff | Novo Sarajevo | Pofalići II | 81 | 8,764.300 | 108.200 | B |
| 8a1ef4582aa7fff | Centar Sarajevo | Breka | 203 | 21,970.800 | 108.200 | B |
| 8a1ef45820f7fff | Centar Sarajevo | Park-Višnjik | 171 | 18,515.600 | 108.300 | B |
| 8a1ef458242ffff | Centar Sarajevo | Koševsko Brdo | 113 | 12,241.000 | 108.300 | B |
| 8a1ef4582337fff | Centar Sarajevo | Park-Višnjik | 94 | 10,185.100 | 108.400 | B |
| 8a1ef459dcf7fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 37 | 4,009.300 | 108.400 | A |
| 8a1ef4586ae7fff | Centar Sarajevo | Betanija | 19 | 2,058.900 | 108.400 | B |
| 8a1ef45914b7fff | Novo Sarajevo | Hrasno Brdo | 49 | 5,310.300 | 108.400 | B |
| 8a1ef459150ffff | Novo Sarajevo | Grbavica II | 109 | 11,813.100 | 108.400 | B |
| 8a1ef459108ffff | Novo Sarajevo | Vraca | 96 | 10,408.800 | 108.400 | B |
| 8a1ef45966e7fff | Novi Grad Sarajevo | Saraj Polje | 45 | 4,879.800 | 108.400 | A |
| 8a1ea92c9157fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 32 | 3,471.000 | 108.500 | A |
| 8a1ef459c92ffff | Stari Grad Sarajevo | Logavina | 153 | 16,596.700 | 108.500 | A |
| 8a1ef4586627fff | Centar Sarajevo | Šip | 138 | 14,975.200 | 108.500 | B |
| 8a1ef4595717fff | Novo Sarajevo | Pofalići II | 69 | 7,488.400 | 108.500 | B |
| 8a1ef458221ffff | Centar Sarajevo | Bardakčije | 107 | 11,612.900 | 108.500 | B |
| 8a1ef459ccd7fff | Centar Sarajevo | Soukbunar | 59 | 6,403.500 | 108.500 | B |
| 8a1ef459dc77fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 41 | 4,451.300 | 108.600 | A |
| 8a1ef45867a7fff | Centar Sarajevo | Šip | 74 | 8,035.700 | 108.600 | B |
| 8a1ef458292ffff | Centar Sarajevo | Betanija | 61 | 6,624.400 | 108.600 | B |
| 8a1ef458230ffff | Centar Sarajevo | Bardakčije | 98 | 10,646.800 | 108.600 | B |
| 8a1ef458418ffff | Centar Sarajevo | Nahorevo | 17 | 1,848.400 | 108.700 | B |
| 8a1ef458265ffff | Centar Sarajevo | Trg oslobođenja-Centar | 136 | 14,792.000 | 108.800 | B |
| 8a1ef45846c7fff | Centar Sarajevo | Betanija | 19 | 2,066.600 | 108.800 | B |
| 8a1ef4596817fff | Novi Grad Sarajevo | Briješće | 24 | 2,612.600 | 108.900 | A |
| 8a1ef45950c7fff | Novo Sarajevo | Pofalići II | 58 | 6,315.300 | 108.900 | B |
| 8a1ea92c915ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 31 | 3,376.800 | 108.900 | A |
| 8a1ef45820b7fff | Centar Sarajevo | Ciglane | 357 | 38,912.200 | 109.000 | B |
| 8a1ef4595a1ffff | Novo Sarajevo | Velešići | 45 | 4,905.100 | 109.000 | B |
| 8a1ef458264ffff | Centar Sarajevo | Trg oslobođenja-Centar | 238 | 25,954.400 | 109.100 | B |
| 8a1ef45950dffff | Novo Sarajevo | Pofalići II | 69 | 7,527.700 | 109.100 | B |
| 8a1ef4583147fff | Stari Grad Sarajevo | Mošćanica | 15 | 1,637.200 | 109.100 | A |
| 8a1ef45b12f7fff | Centar Sarajevo | Betanija | 13 | 1,419.100 | 109.200 | B |
| 8a1ef45969affff | Novi Grad Sarajevo | Briješće | 20 | 2,183.500 | 109.200 | A |
| 8a1ef45918d7fff | Novo Sarajevo | Željeznička | 102 | 11,139.600 | 109.200 | B |
| 8a1ef4580d8ffff | Centar Sarajevo | Pionirska Dolina | 30 | 3,277.100 | 109.200 | B |
| 8a1ef4582247fff | Stari Grad Sarajevo | Logavina | 150 | 16,388.300 | 109.300 | A |
| 8a1ef45862effff | Centar Sarajevo | Betanija | 13 | 1,420.400 | 109.300 | B |
| 8a1ef4586ac7fff | Centar Sarajevo | Betanija | 17 | 1,858.300 | 109.300 | B |
| 8a1ef45958d7fff | Novo Sarajevo | Pofalići II | 13 | 1,421.700 | 109.400 | B |
| 8a1ef45834affff | Stari Grad Sarajevo | Kovači | 87 | 9,517.100 | 109.400 | A |
| 8a1ef45866effff | Centar Sarajevo | Koševsko Brdo | 64 | 7,002.900 | 109.400 | B |
| 8a1ef45939affff | Novo Sarajevo | Hrasno Brdo | 43 | 4,707.400 | 109.500 | B |
| 8a1ea92c9127fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 19 | 2,081.500 | 109.600 | A |
| 8a1ef45835b7fff | Stari Grad Sarajevo | Logavina | 162 | 17,747.300 | 109.600 | A |
| 8a1ef458229ffff | Centar Sarajevo | Mejtaš-Bjelave | 110 | 12,055.400 | 109.600 | B |
| 8a1ef4583d2ffff | Stari Grad Sarajevo | Sedrenik | 65 | 7,124.000 | 109.600 | A |
| 8a1ef4582097fff | Centar Sarajevo | Ciglane | 329 | 36,059.000 | 109.600 | B |
| 8a1ef45961a7fff | Novi Grad Sarajevo | Briješće | 60 | 6,577.700 | 109.600 | A |
| 8a1ef4582777fff | Centar Sarajevo | Džidžikovac-Koševo I | 159 | 17,442.800 | 109.700 | B |
| 8a1ea92c9b97fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 29 | 3,182.500 | 109.700 | A |
| 8a1ef45968e7fff | Novi Grad Sarajevo | Briješće | 19 | 2,086.400 | 109.800 | A |
| 8a1ef4582a17fff | Centar Sarajevo | Hrastovi-Mrkovići | 83 | 9,119.000 | 109.900 | B |
| 8a1ef458655ffff | Centar Sarajevo | Šip | 40 | 4,395.400 | 109.900 | B |
| 8a1ef458634ffff | Centar Sarajevo | Betanija | 17 | 1,868.400 | 109.900 | B |
| 8a1ef4583597fff | Stari Grad Sarajevo | Logavina | 167 | 18,356.700 | 109.900 | A |
| 8a1ef4583737fff | Stari Grad Sarajevo | Vratnik | 109 | 11,984.000 | 109.900 | A |
| 8a1ef45917a7fff | Novo Sarajevo | Vraca | 15 | 1,649.400 | 110.000 | B |
| 8a1ef45868effff | Centar Sarajevo | Betanija | 14 | 1,541.400 | 110.100 | B |
| 8a1ef45827b7fff | Centar Sarajevo | Crni Vrh-Gorica | 126 | 13,890.900 | 110.200 | B |
| 8a1ef4582197fff | Centar Sarajevo | Koševsko Brdo | 161 | 17,749.900 | 110.200 | B |
| 8a1ef459505ffff | Novo Sarajevo | Pofalići I | 43 | 4,741.700 | 110.300 | B |
| 8a1ef4592da7fff | Novi Grad Sarajevo | Dobrinja A | 67 | 7,388.600 | 110.300 | A |
| 8a1ef4592d5ffff | Novi Grad Sarajevo | Dobrinja A | 58 | 6,398.200 | 110.300 | A |
| 8a1ef45b129ffff | Centar Sarajevo | Betanija | 12 | 1,323.800 | 110.300 | B |
| 8a1ef4583137fff | Stari Grad Sarajevo | Sedrenik | 73 | 8,055.300 | 110.300 | A |
| 8a1ef4592ccffff | Novi Grad Sarajevo | Dobrinja A | 123 | 13,582.300 | 110.400 | A |
| 8a1ef4582c8ffff | Novo Sarajevo | Gornji Velešići | 113 | 12,492.000 | 110.500 | B |
| 8a1ef459151ffff | Novo Sarajevo | Hrasno Brdo | 115 | 12,722.400 | 110.600 | B |
| 8a1ef4582a8ffff | Centar Sarajevo | Breka | 158 | 17,481.000 | 110.600 | B |
| 8a1ef4582ba7fff | Centar Sarajevo | Koševo II | 77 | 8,523.100 | 110.700 | B |
| 8a1ef4584117fff | Centar Sarajevo | Nahorevo | 20 | 2,214.100 | 110.700 | B |
| 8a1ef459cd67fff | Centar Sarajevo | Skenderija-Podtekija | 158 | 17,494.600 | 110.700 | B |
| 8a1ef4580d0ffff | Centar Sarajevo | Pionirska Dolina | 34 | 3,767.900 | 110.800 | B |
| 8a1ef45828affff | Centar Sarajevo | Džidžikovac-Koševo I | 89 | 9,863.700 | 110.800 | B |
| 8a1ef4595a9ffff | Novo Sarajevo | Velešići | 25 | 2,772.000 | 110.900 | B |
| 8a1ef458039ffff | Centar Sarajevo | Hrastovi-Mrkovići | 11 | 1,219.900 | 110.900 | B |
| 8a1ef45804a7fff | Centar Sarajevo | Hrastovi-Mrkovići | 62 | 6,876.100 | 110.900 | B |
| 8a1ef45950d7fff | Novo Sarajevo | Pofalići II | 67 | 7,434.200 | 111.000 | B |
| 8a1ef4586367fff | Centar Sarajevo | Betanija | 17 | 1,886.800 | 111.000 | B |
| 8a1ef459d937fff | Stari Grad Sarajevo | Mošćanica | 19 | 2,108.900 | 111.000 | A |
| 8a1ef45823a7fff | Centar Sarajevo | Park-Višnjik | 251 | 27,871.100 | 111.000 | B |
| 8a1ef4582ccffff | Centar Sarajevo | Koševsko Brdo | 247 | 27,437.800 | 111.100 | B |
| 8a1ea92c9c77fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 128 | 14,220.300 | 111.100 | A |
| 8a1ea92c90cffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 34 | 3,782.100 | 111.200 | A |
| 8a1ef458278ffff | Centar Sarajevo | Džidžikovac-Koševo I | 231 | 25,711.800 | 111.300 | B |
| 8a1ea92c902ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 34 | 3,784.400 | 111.300 | A |
| 8a1ef459c09ffff | Stari Grad Sarajevo | Širokača | 66 | 7,347.900 | 111.300 | A |
| 8a1ef45826c7fff | Centar Sarajevo | Trg oslobođenja-Centar | 336 | 37,425.400 | 111.400 | B |
| 8a1ef4582317fff | Centar Sarajevo | Park-Višnjik | 184 | 20,512.900 | 111.500 | B |
| 8a1ef4582757fff | Centar Sarajevo | Džidžikovac-Koševo I | 164 | 18,287.800 | 111.500 | B |
| 8a1ea92c9037fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 20 | 2,232.400 | 111.600 | A |
| 8a1ef4592d97fff | Novi Grad Sarajevo | Dobrinja A | 41 | 4,577.100 | 111.600 | A |
| 8a1ef4592c1ffff | Novi Grad Sarajevo | Dobrinja A | 148 | 16,546.900 | 111.800 | A |
| 8a1ea92c8827fff | Novi Grad Sarajevo | Dobroševići | 12 | 1,341.700 | 111.800 | A |
| 8a1ef4584097fff | Centar Sarajevo | Nahorevo | 17 | 1,901.600 | 111.900 | B |
| 8a1ea92c9d5ffff | Novi Grad Sarajevo | Zabrđe | 49 | 5,482.600 | 111.900 | A |
| 8a1ef4582b1ffff | Centar Sarajevo | Hrastovi-Mrkovići | 64 | 7,161.900 | 111.900 | B |
| 8a1ef45823affff | Centar Sarajevo | Mejtaš-Bjelave | 125 | 13,989.900 | 111.900 | B |
| 8a1ef459cc97fff | Centar Sarajevo | Soukbunar | 73 | 8,175.500 | 112.000 | B |
| 8a1ef459c997fff | Centar Sarajevo | Trg oslobođenja-Centar | 189 | 21,173.900 | 112.000 | B |
| 8a1ef45822a7fff | Centar Sarajevo | Mejtaš-Bjelave | 125 | 14,006.300 | 112.100 | B |
| 8a1ef45849a7fff | Centar Sarajevo | Nahorevo | 14 | 1,568.800 | 112.100 | B |
| 8a1ea92c911ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 16 | 1,793.600 | 112.100 | A |
| 8a1ef4591367fff | Centar Sarajevo | Soukbunar | 85 | 9,536.600 | 112.200 | B |
| 8a1ef4592d27fff | Novi Grad Sarajevo | Saraj Polje | 50 | 5,611.400 | 112.200 | A |
| 8a1ef4586927fff | Centar Sarajevo | Betanija | 27 | 3,031.300 | 112.300 | B |
| 8a1ef459c9affff | Centar Sarajevo | Trg oslobođenja-Centar | 293 | 32,896.800 | 112.300 | B |
| 8a1ef4583d17fff | Centar Sarajevo | Hrastovi-Mrkovići | 76 | 8,533.000 | 112.300 | B |
| 8a1ef45807a7fff | Centar Sarajevo | Hrastovi-Mrkovići | 19 | 2,133.400 | 112.300 | B |
| 8a1ef459cd0ffff | Centar Sarajevo | Skenderija-Podtekija | 271 | 30,435.000 | 112.300 | B |
| 8a1ef4582677fff | Centar Sarajevo | Mejtaš-Bjelave | 117 | 13,145.700 | 112.400 | B |
| 8a1ef458665ffff | Centar Sarajevo | Džidžikovac-Koševo I | 79 | 8,879.800 | 112.400 | B |
| 8a1ef4590177fff | Novi Grad Sarajevo | Alipašin Most III | 141 | 15,862.900 | 112.500 | A |
| 8a1ef45820dffff | Centar Sarajevo | Park-Višnjik | 283 | 31,838.900 | 112.500 | B |
| 8a1ef4584c67fff | Centar Sarajevo | Nahorevo | 10 | 1,125.100 | 112.500 | B |
| 8a1ef4582377fff | Centar Sarajevo | Bardakčije | 92 | 10,359.400 | 112.600 | B |
| 8a1ef459661ffff | Novi Grad Sarajevo | Saraj Polje | 31 | 3,490.800 | 112.600 | A |
| 8a1ef4582107fff | Centar Sarajevo | Džidžikovac-Koševo I | 132 | 14,864.500 | 112.600 | B |
| 8a1ef458294ffff | Centar Sarajevo | Koševo II | 154 | 17,344.700 | 112.600 | B |
| 8a1ef4582607fff | Centar Sarajevo | Džidžikovac-Koševo I | 196 | 22,079.200 | 112.600 | B |
| 8a1ef4584187fff | Centar Sarajevo | Nahorevo | 18 | 2,027.700 | 112.600 | B |
| 8a1ea92cc2e7fff | Novi Grad Sarajevo | Dobroševići | 11 | 1,239.200 | 112.700 | A |
| 8a1ef45966c7fff | Novi Grad Sarajevo | Saraj Polje | 51 | 5,747.500 | 112.700 | A |
| 8a1ef4582a47fff | Centar Sarajevo | Hrastovi-Mrkovići | 65 | 7,328.800 | 112.800 | B |
| 8a1ef45a229ffff | Centar Sarajevo | Nahorevo | 10 | 1,127.600 | 112.800 | B |
| 8a1ef458041ffff | Centar Sarajevo | Pionirska Dolina | 50 | 5,642.200 | 112.800 | B |
| 8a1ef4582ceffff | Centar Sarajevo | Koševsko Brdo | 179 | 20,201.900 | 112.900 | B |
| 8a1ef4591427fff | Novo Sarajevo | Hrasno Brdo | 130 | 14,672.900 | 112.900 | B |
| 8a1ef4580577fff | Centar Sarajevo | Pionirska Dolina | 31 | 3,501.200 | 112.900 | B |
| 8a1ef4590a77fff | Novo Sarajevo | Pofalići II | 104 | 11,747.300 | 113.000 | B |
| 8a1ef4582a97fff | Centar Sarajevo | Breka | 184 | 20,785.700 | 113.000 | B |
| 8a1ef4582837fff | Centar Sarajevo | Betanija | 223 | 25,195.000 | 113.000 | B |
| 8a1ef458254ffff | Centar Sarajevo | Ciglane | 435 | 49,166.700 | 113.000 | B |
| 8a1ef4582a0ffff | Centar Sarajevo | Hrastovi-Mrkovići | 69 | 7,804.800 | 113.100 | B |
| 8a1ef4584ccffff | Centar Sarajevo | Betanija | 11 | 1,244.300 | 113.100 | B |
| 8a1ef45918c7fff | Novo Sarajevo | Željeznička | 122 | 13,802.100 | 113.100 | B |
| 8a1ef4582287fff | Centar Sarajevo | Mejtaš-Bjelave | 118 | 13,357.700 | 113.200 | B |
| 8a1ef4595377fff | Novo Sarajevo | Velešići | 70 | 7,925.600 | 113.200 | B |
| 8a1ea92c9c67fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 41 | 4,642.700 | 113.200 | A |
| 8a1ef4583da7fff | Centar Sarajevo | Hrastovi-Mrkovići | 87 | 9,856.600 | 113.300 | B |
| 8a1ef458342ffff | Stari Grad Sarajevo | Sumbuluša | 187 | 21,186.500 | 113.300 | A |
| 8a1ef4592daffff | Novi Grad Sarajevo | Dobrinja A | 85 | 9,632.200 | 113.300 | A |
| 8a1ef458275ffff | Centar Sarajevo | Mejtaš-Bjelave | 170 | 19,268.800 | 113.300 | B |
| 8a1ef458216ffff | Centar Sarajevo | Breka | 115 | 13,034.900 | 113.300 | B |
| 8a1ef4580caffff | Centar Sarajevo | Pionirska Dolina | 55 | 6,234.500 | 113.400 | B |
| 8a1ef45830c7fff | Stari Grad Sarajevo | Mošćanica | 20 | 2,267.200 | 113.400 | A |
| 8a1ef4580d07fff | Centar Sarajevo | Pionirska Dolina | 31 | 3,514.800 | 113.400 | B |
| 8a1ef45822d7fff | Stari Grad Sarajevo | Logavina | 144 | 16,333.600 | 113.400 | A |
| 8a1ef4586967fff | Centar Sarajevo | Betanija | 13 | 1,474.600 | 113.400 | B |
| 8a1ef4580797fff | Centar Sarajevo | Hrastovi-Mrkovići | 46 | 5,221.600 | 113.500 | B |
| 8a1ef459c917fff | Centar Sarajevo | Trg oslobođenja-Centar | 139 | 15,783.200 | 113.500 | B |
| 8a1ef4580507fff | Centar Sarajevo | Pionirska Dolina | 55 | 6,245.400 | 113.600 | B |
| 8a1ea92c90e7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 37 | 4,201.800 | 113.600 | A |
| 8a1ef4586857fff | Centar Sarajevo | Betanija | 24 | 2,727.800 | 113.700 | B |
| 8a1ef45a22d7fff | Centar Sarajevo | Nahorevo | 13 | 1,477.700 | 113.700 | B |
| 8a1ef45828c7fff | Centar Sarajevo | Koševo II | 208 | 23,646.000 | 113.700 | B |
| 8a1ef4582397fff | Centar Sarajevo | Mejtaš-Bjelave | 145 | 16,491.100 | 113.700 | B |
| 8a1ef4580d2ffff | Centar Sarajevo | Betanija | 51 | 5,802.600 | 113.800 | B |
| 8a1ef4582857fff | Centar Sarajevo | Koševo II | 87 | 9,898.600 | 113.800 | B |
| 8a1ef4582c5ffff | Centar Sarajevo | Koševsko Brdo | 135 | 15,361.500 | 113.800 | B |
| 8a1ef4592d2ffff | Novi Grad Sarajevo | Saraj Polje | 52 | 5,917.300 | 113.800 | A |
| 8a1ef45b12dffff | Centar Sarajevo | Betanija | 17 | 1,934.600 | 113.800 | B |
| 8a1ea92c98cffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 37 | 4,213.900 | 113.900 | A |
| 8a1ef458670ffff | Centar Sarajevo | Šip | 166 | 18,906.400 | 113.900 | B |
| 8a1ef4582a37fff | Centar Sarajevo | Hrastovi-Mrkovići | 79 | 9,003.700 | 114.000 | B |
| 8a1ef4590027fff | Novi Grad Sarajevo | Alipašin Most III | 169 | 19,280.800 | 114.100 | A |
| 8a1ef45862dffff | Centar Sarajevo | Betanija | 212 | 24,195.500 | 114.100 | B |
| 8a1ef4582237fff | Centar Sarajevo | Bardakčije | 113 | 12,900.900 | 114.200 | B |
| 8a1ef458270ffff | Centar Sarajevo | Džidžikovac-Koševo I | 172 | 19,641.000 | 114.200 | B |
| 8a1ef45966f7fff | Novi Grad Sarajevo | Saraj Polje | 54 | 6,166.900 | 114.200 | A |
| 8a1ef4580aa7fff | Centar Sarajevo | Betanija | 28 | 3,197.700 | 114.200 | B |
| 8a1ef4594487fff | Novi Grad Sarajevo | Briješće | 24 | 2,742.200 | 114.300 | A |
| 8a1ef4591a67fff | Centar Sarajevo | Marijin Dvor | 167 | 19,088.300 | 114.300 | B |
| 8a1ef4582167fff | Centar Sarajevo | Koševo II | 124 | 14,180.500 | 114.400 | B |
| 8a1ef4580527fff | Centar Sarajevo | Pionirska Dolina | 43 | 4,919.700 | 114.400 | B |
| 8a1ef4580437fff | Centar Sarajevo | Pionirska Dolina | 60 | 6,866.500 | 114.400 | B |
| 8a1ef45857b7fff | Centar Sarajevo | Betanija | 11 | 1,259.800 | 114.500 | B |
| 8a1ea92c88d7fff | Novi Grad Sarajevo | Dobroševići | 52 | 5,958.700 | 114.600 | A |
| 8a1ea92c956ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 62 | 7,107.600 | 114.600 | A |
| 8a1ef4584c17fff | Centar Sarajevo | Betanija | 19 | 2,178.900 | 114.700 | B |
| 8a1ea92c9187fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 29 | 3,326.300 | 114.700 | A |
| 8a1ef45846cffff | Centar Sarajevo | Betanija | 24 | 2,753.000 | 114.700 | B |
| 8a1ef45968f7fff | Novi Grad Sarajevo | Briješće | 22 | 2,524.500 | 114.700 | A |
| 8a1ef458214ffff | Centar Sarajevo | Koševo II | 246 | 28,234.200 | 114.800 | B |
| 8a1ef4583667fff | Stari Grad Sarajevo | Mošćanica | 22 | 2,525.700 | 114.800 | A |
| 8a1ef4582467fff | Centar Sarajevo | Ciglane | 306 | 35,144.900 | 114.900 | B |
| 8a1ef458054ffff | Centar Sarajevo | Pionirska Dolina | 17 | 1,952.600 | 114.900 | B |
| 8a1ef459dcc7fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 31 | 3,562.800 | 114.900 | A |
| 8a1ef458239ffff | Centar Sarajevo | Mejtaš-Bjelave | 147 | 16,894.700 | 114.900 | B |
| 8a1ef459cd57fff | Centar Sarajevo | Skenderija-Podtekija | 216 | 24,831.100 | 115.000 | B |
| 8a1ea92c8c9ffff | Novi Grad Sarajevo | Dobroševići | 104 | 11,956.400 | 115.000 | A |
| 8a1ef458085ffff | Centar Sarajevo | Betanija | 13 | 1,495.500 | 115.000 | B |
| 8a1ef45862cffff | Centar Sarajevo | Betanija | 168 | 19,330.000 | 115.100 | B |
| 8a1ea92c9077fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 94 | 10,816.900 | 115.100 | A |
| 8a1ea92c881ffff | Novi Grad Sarajevo | Dobroševići | 14 | 1,611.700 | 115.100 | A |
| 8a1ef4580c27fff | Centar Sarajevo | Pionirska Dolina | 29 | 3,339.600 | 115.200 | B |
| 8a1ef459c81ffff | Stari Grad Sarajevo | Mjedenica | 139 | 16,008.800 | 115.200 | A |
| 8a1ea92c9317fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 33 | 3,803.000 | 115.200 | A |
| 8a1ef4582137fff | Centar Sarajevo | Džidžikovac-Koševo I | 129 | 14,876.300 | 115.300 | B |
| 8a1ef459c9b7fff | Centar Sarajevo | Trg oslobođenja-Centar | 236 | 27,233.000 | 115.400 | B |
| 8a1ef4580d1ffff | Centar Sarajevo | Pionirska Dolina | 33 | 3,809.300 | 115.400 | B |
| 8a1ef4582a6ffff | Centar Sarajevo | Hrastovi-Mrkovići | 62 | 7,157.100 | 115.400 | B |
| 8a1ea92c8c8ffff | Novi Grad Sarajevo | Dobroševići | 79 | 9,122.300 | 115.500 | A |
| 8a1ef459c9a7fff | Centar Sarajevo | Trg oslobođenja-Centar | 191 | 22,056.200 | 115.500 | B |
| 8a1ef4583327fff | Stari Grad Sarajevo | Mošćanica | 15 | 1,732.800 | 115.500 | A |
| 8a1ef458238ffff | Centar Sarajevo | Mejtaš-Bjelave | 121 | 13,983.200 | 115.600 | B |
| 8a1ef4586acffff | Centar Sarajevo | Betanija | 39 | 4,508.300 | 115.600 | B |
| 8a1ef4582a57fff | Centar Sarajevo | Hrastovi-Mrkovići | 76 | 8,790.200 | 115.700 | B |
| 8a1ef459605ffff | Novi Grad Sarajevo | Saraj Polje | 24 | 2,776.400 | 115.700 | A |
| 8a1ef4582a87fff | Centar Sarajevo | Breka | 351 | 40,611.800 | 115.700 | B |
| 8a1ef45822f7fff | Centar Sarajevo | Bardakčije | 133 | 15,392.800 | 115.700 | B |
| 8a1ef45929b7fff | Novi Grad Sarajevo | Saraj Polje | 61 | 7,059.900 | 115.700 | A |
| 8a1ea92cc6effff | Novi Grad Sarajevo | Dobroševići | 10 | 1,157.600 | 115.800 | A |
| 8a1ef4580b8ffff | Centar Sarajevo | Betanija | 12 | 1,390.600 | 115.900 | B |
| 8a1ea92c932ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 15 | 1,739.000 | 115.900 | A |
| 8a1ef4586b57fff | Centar Sarajevo | Betanija | 29 | 3,364.200 | 116.000 | B |
| 8a1ef45823b7fff | Centar Sarajevo | Park-Višnjik | 115 | 13,342.900 | 116.000 | B |
| 8a1ef4598177fff | Stari Grad Sarajevo | Širokača | 13 | 1,508.600 | 116.000 | A |
| 8a1ef4583717fff | Stari Grad Sarajevo | Vratnik | 128 | 14,859.100 | 116.100 | A |
| 8a1ef4582847fff | Centar Sarajevo | Koševo II | 85 | 9,870.200 | 116.100 | B |
| 8a1ea92c9237fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 34 | 3,951.300 | 116.200 | A |
| 8a1ef45906cffff | Novo Sarajevo | Hrasno Brdo | 21 | 2,441.500 | 116.300 | B |
| 8a1ef4580db7fff | Centar Sarajevo | Betanija | 22 | 2,558.400 | 116.300 | B |
| 8a1ef4582637fff | Centar Sarajevo | Džidžikovac-Koševo I | 222 | 25,816.500 | 116.300 | B |
| 8a1ef4580587fff | Centar Sarajevo | Pionirska Dolina | 62 | 7,211.200 | 116.300 | B |
| 8a1ef4582867fff | Centar Sarajevo | Koševo II | 66 | 7,682.000 | 116.400 | B |
| 8a1ef4584557fff | Centar Sarajevo | Betanija | 13 | 1,514.200 | 116.500 | B |
| 8a1ef459ccf7fff | Centar Sarajevo | Soukbunar | 83 | 9,671.400 | 116.500 | B |
| 8a1ef4582697fff | Centar Sarajevo | Marijin Dvor | 160 | 18,658.300 | 116.600 | B |
| 8a1ea92c92e7fff | Novi Grad Sarajevo | Briješće | 19 | 2,216.600 | 116.700 | A |
| 8a1ef45b21affff | Novi Grad Sarajevo | Zabrđe | 15 | 1,752.100 | 116.800 | A |
| 8a1ef4580ca7fff | Centar Sarajevo | Pionirska Dolina | 51 | 5,959.500 | 116.900 | B |
| 8a1ef4580a27fff | Centar Sarajevo | Betanija | 15 | 1,753.400 | 116.900 | B |
| 8a1ea92c9627fff | Novi Grad Sarajevo | Briješće | 55 | 6,431.900 | 116.900 | A |
| 8a1ef45862d7fff | Centar Sarajevo | Betanija | 72 | 8,423.400 | 117.000 | B |
| 8a1ef4596b9ffff | Novi Grad Sarajevo | Briješće | 26 | 3,043.500 | 117.100 | A |
| 8a1ef4582b5ffff | Centar Sarajevo | Hrastovi-Mrkovići | 65 | 7,609.300 | 117.100 | B |
| 8a1ef4592d37fff | Novi Grad Sarajevo | Saraj Polje | 57 | 6,674.000 | 117.100 | A |
| 8a1ef4582647fff | Centar Sarajevo | Trg oslobođenja-Centar | 179 | 20,977.300 | 117.200 | B |
| 8a1ef459d187fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 30 | 3,516.300 | 117.200 | A |
| 8a1ef4582b77fff | Centar Sarajevo | Hrastovi-Mrkovići | 92 | 10,790.900 | 117.300 | B |
| 8a1ef45828e7fff | Centar Sarajevo | Koševo II | 161 | 18,891.700 | 117.300 | B |
| 8a1ef4596867fff | Novi Grad Sarajevo | Briješće | 26 | 3,051.100 | 117.300 | A |
| 8a1ea92c8987fff | Novi Grad Sarajevo | Dobroševići | 12 | 1,409.200 | 117.400 | A |
| 8a1ef459125ffff | Centar Sarajevo | Soukbunar | 13 | 1,527.000 | 117.500 | B |
| 8a1ef459690ffff | Novi Grad Sarajevo | Briješće | 23 | 2,702.100 | 117.500 | A |
| 8a1ef458481ffff | Centar Sarajevo | Nahorevo | 11 | 1,292.300 | 117.500 | B |
| 8a1ea92c9a97fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 34 | 3,995.000 | 117.500 | A |
| 8a1ef459cd6ffff | Centar Sarajevo | Skenderija-Podtekija | 165 | 19,398.700 | 117.600 | B |
| 8a1ef4596957fff | Novi Grad Sarajevo | Briješće | 26 | 3,057.200 | 117.600 | A |
| 8a1ea92cd5a7fff | Novi Grad Sarajevo | Dobroševići | 14 | 1,646.800 | 117.600 | A |
| 8a1ef459c8a7fff | Centar Sarajevo | Skenderija-Podtekija | 183 | 21,529.800 | 117.600 | B |
| 8a1ea92cc2effff | Novi Grad Sarajevo | Dobroševići | 15 | 1,764.900 | 117.700 | A |
| 8a1ea92c93b7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 41 | 4,826.700 | 117.700 | A |
| 8a1ea92c938ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 31 | 3,650.900 | 117.800 | A |
| 8a1ef45805a7fff | Centar Sarajevo | Pionirska Dolina | 57 | 6,715.100 | 117.800 | B |
| 8a1ef4580107fff | Centar Sarajevo | Pionirska Dolina | 13 | 1,532.600 | 117.900 | B |
| 8a1ef45836a7fff | Stari Grad Sarajevo | Vratnik | 81 | 9,558.600 | 118.000 | A |
| 8a1ef4586a0ffff | Centar Sarajevo | Betanija | 36 | 4,249.800 | 118.000 | B |
| 8a1ef4586867fff | Centar Sarajevo | Betanija | 24 | 2,834.900 | 118.100 | B |
| 8a1ef4582b27fff | Centar Sarajevo | Koševo II | 81 | 9,569.400 | 118.100 | B |
| 8a1ef459cd47fff | Centar Sarajevo | Skenderija-Podtekija | 219 | 25,893.400 | 118.200 | B |
| 8a1ef45b12affff | Centar Sarajevo | Betanija | 10 | 1,182.400 | 118.200 | B |
| 8a1ef4582627fff | Centar Sarajevo | Džidžikovac-Koševo I | 273 | 32,284.300 | 118.300 | B |
| 8a1ea92c906ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 40 | 4,730.400 | 118.300 | A |
| 8a1ea92c966ffff | Novi Grad Sarajevo | Briješće | 26 | 3,077.100 | 118.300 | A |
| 8a1ef4586877fff | Centar Sarajevo | Betanija | 22 | 2,604.700 | 118.400 | B |
| 8a1ef4584897fff | Centar Sarajevo | Nahorevo | 12 | 1,420.800 | 118.400 | B |
| 8a1ef4592d77fff | Novi Grad Sarajevo | Saraj Polje | 57 | 6,750.300 | 118.400 | A |
| 8a1ef458274ffff | Centar Sarajevo | Mejtaš-Bjelave | 159 | 18,844.900 | 118.500 | B |
| 8a1ef459675ffff | Novi Grad Sarajevo | Saraj Polje | 18 | 2,134.200 | 118.600 | A |
| 8a1ef459c987fff | Centar Sarajevo | Trg oslobođenja-Centar | 301 | 35,689.400 | 118.600 | B |
| 8a1ef4592c57fff | Novi Grad Sarajevo | Dobrinja A | 108 | 12,807.300 | 118.600 | A |
| 8a1ef459c837fff | Stari Grad Sarajevo | Ferhadija | 160 | 18,975.300 | 118.600 | A |
| 8a1ef4591b47fff | Centar Sarajevo | Marijin Dvor | 210 | 24,915.800 | 118.600 | B |
| 8a1ea92c88effff | Novi Grad Sarajevo | Dobroševići | 10 | 1,186.800 | 118.700 | A |
| 8a1ef4583b07fff | Stari Grad Sarajevo | Mošćanica | 12 | 1,425.700 | 118.800 | A |
| 8a1ef4586b47fff | Centar Sarajevo | Betanija | 26 | 3,089.400 | 118.800 | B |
| 8a1ef4580b07fff | Centar Sarajevo | Betanija | 15 | 1,783.600 | 118.900 | B |
| 8a1ef458685ffff | Centar Sarajevo | Betanija | 26 | 3,091.800 | 118.900 | B |
| 8a1ef4582617fff | Centar Sarajevo | Džidžikovac-Koševo I | 245 | 29,147.300 | 119.000 | B |
| 8a1ef45850dffff | Centar Sarajevo | Betanija | 40 | 4,758.900 | 119.000 | B |
| 8a1ea92c976ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 46 | 5,473.200 | 119.000 | A |
| 8a1ef4580c0ffff | Centar Sarajevo | Pionirska Dolina | 33 | 3,927.600 | 119.000 | B |
| 8a1ea92c88f7fff | Novi Grad Sarajevo | Dobroševići | 18 | 2,142.400 | 119.000 | A |
| 8a1ea92c9307fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 36 | 4,285.500 | 119.000 | A |
| 8a1ef4596c0ffff | Novi Grad Sarajevo | Briješće | 16 | 1,905.400 | 119.100 | A |
| 8a1ea92c8887fff | Novi Grad Sarajevo | Dobroševići | 16 | 1,906.000 | 119.100 | A |
| 8a1ef4596907fff | Novi Grad Sarajevo | Briješće | 91 | 10,842.900 | 119.200 | A |
| 8a1ea92c9057fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 50 | 5,959.100 | 119.200 | A |
| 8a1ef4582797fff | Centar Sarajevo | Crni Vrh-Gorica | 144 | 17,163.800 | 119.200 | B |
| 8a1ef45866cffff | Centar Sarajevo | Koševsko Brdo | 176 | 20,980.400 | 119.200 | B |
| 8a1ef459cd77fff | Centar Sarajevo | Skenderija-Podtekija | 290 | 34,583.100 | 119.300 | B |
| 8a1ef4582c27fff | Centar Sarajevo | Donji Velešići | 90 | 10,741.900 | 119.400 | B |
| 8a1ef4580537fff | Centar Sarajevo | Pionirska Dolina | 60 | 7,165.600 | 119.400 | B |
| 8a1ef4583d37fff | Centar Sarajevo | Hrastovi-Mrkovići | 68 | 8,135.000 | 119.600 | B |
| 8a1ef4592caffff | Novi Grad Sarajevo | Dobrinja A | 119 | 14,250.800 | 119.800 | A |
| 8a1ef459669ffff | Novi Grad Sarajevo | Saraj Polje | 56 | 6,707.400 | 119.800 | A |
| 8a1ea92c900ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 47 | 5,631.100 | 119.800 | A |
| 8a1ea92cc287fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,198.600 | 119.900 | A |
| 8a1ef4580daffff | Centar Sarajevo | Pionirska Dolina | 30 | 3,596.000 | 119.900 | B |
| 8a1ef4580b5ffff | Centar Sarajevo | Betanija | 10 | 1,199.500 | 119.900 | B |
| 8a1ef4583d07fff | Centar Sarajevo | Hrastovi-Mrkovići | 85 | 10,196.300 | 120.000 | B |
| 8a1ef458049ffff | Centar Sarajevo | Hrastovi-Mrkovići | 78 | 9,357.000 | 120.000 | B |
| 8a1ea92c988ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 28 | 3,359.400 | 120.000 | A |
| 8a1ef45836e7fff | Stari Grad Sarajevo | Babića bašča | 19 | 2,279.600 | 120.000 | A |
| 8a1ef458285ffff | Centar Sarajevo | Koševo II | 99 | 11,882.900 | 120.000 | B |
| 8a1ea92cdd97fff | Novi Grad Sarajevo | Dobroševići | 11 | 1,320.600 | 120.100 | A |
| 8a1ea92cd5b7fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,200.700 | 120.100 | A |
| 8a1ea92cc247fff | Novi Grad Sarajevo | Dobroševići | 15 | 1,801.300 | 120.100 | A |
| 8a1ef4592d17fff | Novi Grad Sarajevo | Saraj Polje | 86 | 10,334.600 | 120.200 | A |
| 8a1ef4582a2ffff | Centar Sarajevo | Hrastovi-Mrkovići | 77 | 9,254.200 | 120.200 | B |
| 8a1ea92c88a7fff | Novi Grad Sarajevo | Dobroševići | 61 | 7,332.800 | 120.200 | A |
| 8a1ef459d19ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 31 | 3,727.400 | 120.200 | A |
| 8a1ef4582767fff | Centar Sarajevo | Mejtaš-Bjelave | 135 | 16,234.000 | 120.300 | B |
| 8a1ef4592cc7fff | Novi Grad Sarajevo | Dobrinja A | 120 | 14,438.600 | 120.300 | A |
| 8a1ea92c9777fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 58 | 6,982.500 | 120.400 | A |
| 8a1ef4582387fff | Centar Sarajevo | Mejtaš-Bjelave | 186 | 22,396.500 | 120.400 | B |
| 8a1ef4583b97fff | Stari Grad Sarajevo | Mošćanica | 10 | 1,204.500 | 120.400 | A |
| 8a1ef4592d07fff | Novi Grad Sarajevo | Saraj Polje | 80 | 9,637.600 | 120.500 | A |
| 8a1ef6965b5ffff | Novi Grad Sarajevo | Saraj Polje | 28 | 3,373.600 | 120.500 | A |
| 8a1ea92c962ffff | Novi Grad Sarajevo | Briješće | 31 | 3,735.800 | 120.500 | A |
| 8a1ea92cc277fff | Novi Grad Sarajevo | Dobroševići | 13 | 1,567.100 | 120.500 | A |
| 8a1ef45841affff | Centar Sarajevo | Nahorevo | 26 | 3,134.300 | 120.600 | B |
| 8a1ef45848affff | Centar Sarajevo | Nahorevo | 20 | 2,413.300 | 120.700 | B |
| 8a1ea92cc25ffff | Novi Grad Sarajevo | Dobroševići | 13 | 1,569.100 | 120.700 | A |
| 8a1ea92c916ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 46 | 5,553.600 | 120.700 | A |
| 8a1ef4583067fff | Stari Grad Sarajevo | Mošćanica | 15 | 1,811.600 | 120.800 | A |
| 8a1ef45945a7fff | Novi Grad Sarajevo | Briješće | 19 | 2,294.700 | 120.800 | A |
| 8a1ea92c92affff | Novi Grad Sarajevo | Briješće | 14 | 1,692.300 | 120.900 | A |
| 8a1ea92c9047fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 52 | 6,286.300 | 120.900 | A |
| 8a1ea92c98dffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 52 | 6,289.700 | 121.000 | A |
| 8a1ef458276ffff | Centar Sarajevo | Mejtaš-Bjelave | 160 | 19,360.600 | 121.000 | B |
| 8a1ef4584957fff | Centar Sarajevo | Nahorevo | 12 | 1,452.500 | 121.000 | B |
| 8a1ef45966effff | Novi Grad Sarajevo | Saraj Polje | 78 | 9,442.900 | 121.100 | A |
| 8a1ea92c9767fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 62 | 7,507.900 | 121.100 | A |
| 8a1ef45833a7fff | Stari Grad Sarajevo | Mošćanica | 19 | 2,301.300 | 121.100 | A |
| 8a1ea92cc64ffff | Novi Grad Sarajevo | Dobroševići | 13 | 1,575.000 | 121.200 | A |
| 8a1ef4592997fff | Novi Grad Sarajevo | Saraj Polje | 80 | 9,695.400 | 121.200 | A |
| 8a1ef45968c7fff | Novi Grad Sarajevo | Briješće | 30 | 3,636.500 | 121.200 | A |
| 8a1ea92c9647fff | Novi Grad Sarajevo | Briješće | 32 | 3,879.400 | 121.200 | A |
| 8a1ef4582207fff | Centar Sarajevo | Bardakčije | 130 | 15,765.300 | 121.300 | B |
| 8a1ef4584807fff | Centar Sarajevo | Nahorevo | 17 | 2,063.000 | 121.400 | B |
| 8a1ef458402ffff | Centar Sarajevo | Nahorevo | 31 | 3,762.200 | 121.400 | B |
| 8a1ea92c912ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 56 | 6,800.100 | 121.400 | A |
| 8a1ef4592d87fff | Novi Grad Sarajevo | Dobrinja A | 125 | 15,186.000 | 121.500 | A |
| 8a1ea92c8d4ffff | Novi Grad Sarajevo | Dobroševići | 12 | 1,458.100 | 121.500 | A |
| 8a1ef45966d7fff | Novi Grad Sarajevo | Saraj Polje | 77 | 9,358.600 | 121.500 | A |
| 8a1ef4582297fff | Centar Sarajevo | Mejtaš-Bjelave | 227 | 27,596.600 | 121.600 | B |
| 8a1ea92cd717fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,216.400 | 121.600 | A |
| 8a1ea92c9147fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 58 | 7,056.400 | 121.700 | A |
| 8a1ef459668ffff | Novi Grad Sarajevo | Saraj Polje | 78 | 9,490.000 | 121.700 | A |
| 8a1ef4582c57fff | Centar Sarajevo | Koševsko Brdo | 137 | 16,685.900 | 121.800 | B |
| 8a1ea92cd467fff | Novi Grad Sarajevo | Dobroševići | 11 | 1,341.500 | 122.000 | A |
| 8a1ef4592cd7fff | Novi Grad Sarajevo | Dobrinja A | 100 | 12,197.100 | 122.000 | A |
| 8a1ea92c921ffff | Novi Grad Sarajevo | Briješće | 27 | 3,294.500 | 122.000 | A |
| 8a1ea92c9557fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 65 | 7,937.600 | 122.100 | A |
| 8a1ef4583627fff | Stari Grad Sarajevo | Mošćanica | 40 | 4,887.100 | 122.200 | A |
| 8a1ea92c9177fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 61 | 7,453.500 | 122.200 | A |
| 8a1ef45822b7fff | Centar Sarajevo | Mejtaš-Bjelave | 143 | 17,473.100 | 122.200 | B |
| 8a1ef45966affff | Novi Grad Sarajevo | Saraj Polje | 29 | 3,543.500 | 122.200 | A |
| 8a1ef459299ffff | Novi Grad Sarajevo | Saraj Polje | 73 | 8,921.900 | 122.200 | A |
| 8a1ef459cd17fff | Centar Sarajevo | Skenderija-Podtekija | 82 | 10,029.200 | 122.300 | B |
| 8a1ef4580417fff | Centar Sarajevo | Pionirska Dolina | 78 | 9,540.800 | 122.300 | B |
| 8a1ef4582b07fff | Centar Sarajevo | Hrastovi-Mrkovići | 73 | 8,937.700 | 122.400 | B |
| 8a1ef4582667fff | Centar Sarajevo | Mejtaš-Bjelave | 192 | 23,517.100 | 122.500 | B |
| 8a1ef4582657fff | Centar Sarajevo | Trg oslobođenja-Centar | 296 | 36,261.100 | 122.500 | B |
| 8a1ef4592c8ffff | Novi Grad Sarajevo | Dobrinja A | 62 | 7,597.100 | 122.500 | A |
| 8a1ef4592ce7fff | Novi Grad Sarajevo | Dobrinja A | 138 | 16,927.100 | 122.700 | A |
| 8a1ea92c974ffff | Novi Grad Sarajevo | Briješće | 42 | 5,153.200 | 122.700 | A |
| 8a1ef4596ba7fff | Novi Grad Sarajevo | Briješće | 47 | 5,768.100 | 122.700 | A |
| 8a1ef4592cdffff | Novi Grad Sarajevo | Dobrinja A | 139 | 17,070.900 | 122.800 | A |
| 8a1ea92cc30ffff | Novi Grad Sarajevo | Dobroševići | 13 | 1,597.300 | 122.900 | A |
| 8a1ef4586757fff | Centar Sarajevo | Šip | 84 | 10,323.800 | 122.900 | B |
| 8a1ef6965a2ffff | Novi Grad Sarajevo | Saraj Polje | 22 | 2,705.800 | 123.000 | A |
| 8a1ef4586a77fff | Centar Sarajevo | Betanija | 31 | 3,814.000 | 123.000 | B |
| 8a1ea92c9747fff | Novi Grad Sarajevo | Briješće | 39 | 4,803.200 | 123.200 | A |
| 8a1ef4582747fff | Centar Sarajevo | Mejtaš-Bjelave | 142 | 17,499.500 | 123.200 | B |
| 8a1ef4596b07fff | Novi Grad Sarajevo | Briješće | 28 | 3,451.200 | 123.300 | A |
| 8a1ea92c9387fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 55 | 6,779.900 | 123.300 | A |
| 8a1ea92cd58ffff | Novi Grad Sarajevo | Dobroševići | 15 | 1,849.100 | 123.300 | A |
| 8a1ea92c8b27fff | Novi Grad Sarajevo | Dobroševići | 21 | 2,588.800 | 123.300 | A |
| 8a1ea92c9677fff | Novi Grad Sarajevo | Briješće | 37 | 4,562.800 | 123.300 | A |
| 8a1ef6965a47fff | Novi Grad Sarajevo | Saraj Polje | 72 | 8,880.900 | 123.300 | A |
| 8a1ea92c904ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 57 | 7,031.900 | 123.400 | A |
| 8a1ef4596b37fff | Novi Grad Sarajevo | Briješće | 36 | 4,445.100 | 123.500 | A |
| 8a1ef4584617fff | Centar Sarajevo | Betanija | 25 | 3,088.700 | 123.500 | B |
| 8a1ea92c93a7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 52 | 6,426.500 | 123.600 | A |
| 8a1ef4582a5ffff | Centar Sarajevo | Hrastovi-Mrkovići | 91 | 11,248.200 | 123.600 | B |
| 8a1ea92cd497fff | Novi Grad Sarajevo | Dobroševići | 12 | 1,483.600 | 123.600 | A |
| 8a1ea92c93affff | Novi Grad Sarajevo | Naselje heroja Sokolje | 57 | 7,047.200 | 123.600 | A |
| 8a1ef4591b5ffff | Centar Sarajevo | Marijin Dvor | 158 | 19,540.300 | 123.700 | B |
| 8a1ea92c9167fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 62 | 7,673.400 | 123.800 | A |
| 8a1ef4596677fff | Novi Grad Sarajevo | Saraj Polje | 87 | 10,768.100 | 123.800 | A |
| 8a1ef45968affff | Novi Grad Sarajevo | Briješće | 33 | 4,084.900 | 123.800 | A |
| 8a1ef4592cf7fff | Novi Grad Sarajevo | Dobrinja A | 153 | 18,944.800 | 123.800 | A |
| 8a1ef458694ffff | Centar Sarajevo | Betanija | 55 | 6,811.800 | 123.900 | B |
| 8a1ef4596d57fff | Novi Grad Sarajevo | Briješće | 33 | 4,087.800 | 123.900 | A |
| 8a1ea92c822ffff | Novi Grad Sarajevo | Briješće | 16 | 1,982.200 | 123.900 | A |
| 8a1ef45966cffff | Novi Grad Sarajevo | Saraj Polje | 85 | 10,530.500 | 123.900 | A |
| 8a1ea92c920ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 45 | 5,576.600 | 123.900 | A |
| 8a1ef4586407fff | Centar Sarajevo | Šip | 39 | 4,833.100 | 123.900 | B |
| 8a1ea92c914ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 62 | 7,684.700 | 123.900 | A |
| 8a1ef4580c17fff | Centar Sarajevo | Pionirska Dolina | 44 | 5,453.900 | 124.000 | B |
| 8a1ef4586b0ffff | Centar Sarajevo | Betanija | 25 | 3,100.600 | 124.000 | B |
| 8a1ef458338ffff | Stari Grad Sarajevo | Mošćanica | 19 | 2,362.400 | 124.300 | A |
| 8a1ef4592d47fff | Novi Grad Sarajevo | Saraj Polje | 86 | 10,701.000 | 124.400 | A |
| 8a1ef4582b0ffff | Centar Sarajevo | Hrastovi-Mrkovići | 78 | 9,707.900 | 124.500 | B |
| 8a1ef4584c4ffff | Centar Sarajevo | Nahorevo | 20 | 2,490.200 | 124.500 | B |
| 8a1ea92cc207fff | Novi Grad Sarajevo | Dobroševići | 13 | 1,618.900 | 124.500 | A |
| 8a1ef459696ffff | Novi Grad Sarajevo | Briješće | 33 | 4,111.400 | 124.600 | A |
| 8a1ea92c9357fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 37 | 4,610.100 | 124.600 | A |
| 8a1ef4582b37fff | Centar Sarajevo | Hrastovi-Mrkovići | 79 | 9,850.400 | 124.700 | B |
| 8a1ef458348ffff | Stari Grad Sarajevo | Kovači | 101 | 12,595.600 | 124.700 | A |
| 8a1ea92cc367fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,247.400 | 124.700 | A |
| 8a1ef4596b97fff | Novi Grad Sarajevo | Briješće | 49 | 6,114.000 | 124.800 | A |
| 8a1ea92c922ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 38 | 4,742.200 | 124.800 | A |
| 8a1ea92c8b37fff | Novi Grad Sarajevo | Dobroševići | 15 | 1,872.200 | 124.800 | A |
| 8a1ef45b12d7fff | Centar Sarajevo | Betanija | 23 | 2,870.800 | 124.800 | B |
| 8a1ef4596c87fff | Novi Grad Sarajevo | Briješće | 18 | 2,248.200 | 124.900 | A |
| 8a1ef459c927fff | Centar Sarajevo | Mejtaš-Bjelave | 220 | 27,489.000 | 125.000 | B |
| 8a1ea92c931ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 59 | 7,382.100 | 125.100 | A |
| 8a1ef458228ffff | Centar Sarajevo | Mejtaš-Bjelave | 157 | 19,650.600 | 125.200 | B |
| 8a1ef4586a07fff | Centar Sarajevo | Betanija | 30 | 3,758.200 | 125.300 | B |
| 8a1ea92c8ba7fff | Novi Grad Sarajevo | Dobroševići | 11 | 1,378.100 | 125.300 | A |
| 8a1ef4583a8ffff | Stari Grad Sarajevo | Mošćanica | 22 | 2,758.300 | 125.400 | A |
| 8a1ef4596977fff | Novi Grad Sarajevo | Briješće | 33 | 4,138.400 | 125.400 | A |
| 8a1ea92cd40ffff | Novi Grad Sarajevo | Dobroševići | 14 | 1,756.000 | 125.400 | A |
| 8a1ef45834a7fff | Stari Grad Sarajevo | Kovači | 112 | 14,049.200 | 125.400 | A |
| 8a1ef458358ffff | Stari Grad Sarajevo | Kovači | 104 | 13,046.800 | 125.400 | A |
| 8a1ef6965a67fff | Novi Grad Sarajevo | Saraj Polje | 34 | 4,270.700 | 125.600 | A |
| 8a1ea92cd4cffff | Novi Grad Sarajevo | Dobroševići | 13 | 1,633.400 | 125.600 | A |
| 8a1ef459449ffff | Novi Grad Sarajevo | Briješće | 28 | 3,520.100 | 125.700 | A |
| 8a1ea92c9447fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 28 | 3,521.100 | 125.800 | A |
| 8a1ef4596857fff | Novi Grad Sarajevo | Briješće | 44 | 5,534.400 | 125.800 | A |
| 8a1ef459cd07fff | Centar Sarajevo | Skenderija-Podtekija | 81 | 10,192.600 | 125.800 | B |
| 8a1ef45969b7fff | Novi Grad Sarajevo | Briješće | 57 | 7,176.500 | 125.900 | A |
| 8a1ef458461ffff | Centar Sarajevo | Betanija | 19 | 2,392.800 | 125.900 | B |
| 8a1ef4582ae7fff | Centar Sarajevo | Hrastovi-Mrkovići | 102 | 12,849.300 | 126.000 | B |
| 8a1ef458389ffff | Stari Grad Sarajevo | Sedrenik | 94 | 11,842.400 | 126.000 | A |
| 8a1ea92c8b2ffff | Novi Grad Sarajevo | Dobroševići | 12 | 1,511.900 | 126.000 | A |
| 8a1ea92c964ffff | Novi Grad Sarajevo | Briješće | 42 | 5,293.700 | 126.000 | A |
| 8a1ef4582b17fff | Centar Sarajevo | Hrastovi-Mrkovići | 91 | 11,474.900 | 126.100 | B |
| 8a1ea92c91a7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 51 | 6,434.800 | 126.200 | A |
| 8a1ea92c9c6ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 42 | 5,302.300 | 126.200 | A |
| 8a1ef459692ffff | Novi Grad Sarajevo | Briješće | 37 | 4,671.100 | 126.200 | A |
| 8a1ef4596cb7fff | Novi Grad Sarajevo | Briješće | 12 | 1,515.400 | 126.300 | A |
| 8a1ef45826dffff | Centar Sarajevo | Trg oslobođenja-Centar | 156 | 19,709.200 | 126.300 | B |
| 8a1ea92cd44ffff | Novi Grad Sarajevo | Dobroševići | 18 | 2,274.900 | 126.400 | A |
| 8a1ea92c9227fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 61 | 7,709.400 | 126.400 | A |
| 8a1ea92c9067fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 74 | 9,352.800 | 126.400 | A |
| 8a1ef4582b57fff | Centar Sarajevo | Hrastovi-Mrkovići | 85 | 10,749.800 | 126.500 | B |
| 8a1ef4583407fff | Stari Grad Sarajevo | Kovači | 100 | 12,650.700 | 126.500 | A |
| 8a1ea92c88c7fff | Novi Grad Sarajevo | Dobroševići | 18 | 2,277.500 | 126.500 | A |
| 8a1ea92cc6c7fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,265.400 | 126.500 | A |
| 8a1ef4582b47fff | Centar Sarajevo | Hrastovi-Mrkovići | 77 | 9,745.600 | 126.600 | B |
| 8a1ea92c9397fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 72 | 9,121.500 | 126.700 | A |
| 8a1ea92c930ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 59 | 7,475.100 | 126.700 | A |
| 8a1ea92cd4effff | Novi Grad Sarajevo | Dobroševići | 14 | 1,773.900 | 126.700 | A |
| 8a1ef6965b57fff | Novi Grad Sarajevo | Saraj Polje | 23 | 2,916.000 | 126.800 | A |
| 8a1ef45830cffff | Stari Grad Sarajevo | Mošćanica | 22 | 2,791.100 | 126.900 | A |
| 8a1ef4583a17fff | Stari Grad Sarajevo | Mošćanica | 20 | 2,538.300 | 126.900 | A |
| 8a1ea92c954ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 38 | 4,824.100 | 126.900 | A |
| 8a1ef458051ffff | Centar Sarajevo | Pionirska Dolina | 78 | 9,906.600 | 127.000 | B |
| 8a1ea92cc327fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,270.200 | 127.000 | A |
| 8a1ea92c9247fff | Novi Grad Sarajevo | Briješće | 23 | 2,922.500 | 127.100 | A |
| 8a1ea92c96affff | Novi Grad Sarajevo | Briješće | 16 | 2,033.300 | 127.100 | A |
| 8a1ef45944b7fff | Novi Grad Sarajevo | Briješće | 36 | 4,576.000 | 127.100 | A |
| 8a1ea92cc2b7fff | Novi Grad Sarajevo | Dobroševići | 15 | 1,907.800 | 127.200 | A |
| 8a1ef459660ffff | Novi Grad Sarajevo | Saraj Polje | 89 | 11,322.500 | 127.200 | A |
| 8a1ef4594597fff | Novi Grad Sarajevo | Briješće | 35 | 4,453.900 | 127.300 | A |
| 8a1ef458305ffff | Stari Grad Sarajevo | Mošćanica | 27 | 3,436.900 | 127.300 | A |
| 8a1ea92cc257fff | Novi Grad Sarajevo | Dobroševići | 20 | 2,548.100 | 127.400 | A |
| 8a1ef4596bb7fff | Novi Grad Sarajevo | Briješće | 60 | 7,648.700 | 127.500 | A |
| 8a1ef4596827fff | Novi Grad Sarajevo | Briješće | 54 | 6,885.200 | 127.500 | A |
| 8a1ef45846e7fff | Centar Sarajevo | Betanija | 25 | 3,191.000 | 127.600 | B |
| 8a1ea92cd4b7fff | Novi Grad Sarajevo | Dobroševići | 12 | 1,532.100 | 127.700 | A |
| 8a1ef4586947fff | Centar Sarajevo | Betanija | 42 | 5,365.000 | 127.700 | B |
| 8a1ef4580b17fff | Centar Sarajevo | Betanija | 25 | 3,197.900 | 127.900 | B |
| 8a1ef459c937fff | Centar Sarajevo | Mejtaš-Bjelave | 169 | 21,618.800 | 127.900 | B |
| 8a1ef459c977fff | Stari Grad Sarajevo | Logavina | 192 | 24,576.300 | 128.000 | A |
| 8a1ef4596967fff | Novi Grad Sarajevo | Briješće | 46 | 5,890.200 | 128.000 | A |
| 8a1ea92cc39ffff | Novi Grad Sarajevo | Dobroševići | 15 | 1,920.700 | 128.000 | A |
| 8a1ea92c8107fff | Novi Grad Sarajevo | Dobroševići | 17 | 2,177.800 | 128.100 | A |
| 8a1ef459c907fff | Stari Grad Sarajevo | Ferhadija | 157 | 20,114.300 | 128.100 | A |
| 8a1ef458288ffff | Centar Sarajevo | Džidžikovac-Koševo I | 104 | 13,325.000 | 128.100 | B |
| 8a1ef45968effff | Novi Grad Sarajevo | Briješće | 71 | 9,104.800 | 128.200 | A |
| 8a1ef4596927fff | Novi Grad Sarajevo | Briješće | 42 | 5,389.000 | 128.300 | A |
| 8a1ef458310ffff | Stari Grad Sarajevo | Mošćanica | 35 | 4,491.200 | 128.300 | A |
| 8a1ea92c9297fff | Novi Grad Sarajevo | Briješće | 38 | 4,878.400 | 128.400 | A |
| 8a1ea92c885ffff | Novi Grad Sarajevo | Dobroševići | 16 | 2,054.600 | 128.400 | A |
| 8a1ef4596937fff | Novi Grad Sarajevo | Briješće | 52 | 6,677.800 | 128.400 | A |
| 8a1ef4594587fff | Novi Grad Sarajevo | Briješće | 36 | 4,624.700 | 128.500 | A |
| 8a1ea92cd49ffff | Novi Grad Sarajevo | Dobroševići | 19 | 2,442.100 | 128.500 | A |
| 8a1ef4596b17fff | Novi Grad Sarajevo | Briješće | 50 | 6,432.500 | 128.700 | A |
| 8a1ea92cc117fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,287.700 | 128.800 | A |
| 8a1ea92cc2cffff | Novi Grad Sarajevo | Dobroševići | 13 | 1,674.300 | 128.800 | A |
| 8a1ea92cdd9ffff | Novi Grad Sarajevo | Dobroševići | 18 | 2,318.300 | 128.800 | A |
| 8a1ea92c89a7fff | Novi Grad Sarajevo | Dobroševići | 18 | 2,318.900 | 128.800 | A |
| 8a1ef459610ffff | Novi Grad Sarajevo | Briješće | 33 | 4,253.600 | 128.900 | A |
| 8a1ea92c92cffff | Novi Grad Sarajevo | Briješće | 37 | 4,770.400 | 128.900 | A |
| 8a1ef4594497fff | Novi Grad Sarajevo | Briješće | 42 | 5,417.600 | 129.000 | A |
| 8a1ea92cd447fff | Novi Grad Sarajevo | Dobroševići | 21 | 2,708.900 | 129.000 | A |
| 8a1ef458e92ffff | Stari Grad Sarajevo | Mošćanica | 11 | 1,419.100 | 129.000 | A |
| 8a1ea92cc6d7fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,290.700 | 129.100 | A |
| 8a1ef4584c8ffff | Centar Sarajevo | Betanija | 13 | 1,678.500 | 129.100 | B |
| 8a1ef4596917fff | Novi Grad Sarajevo | Briješće | 64 | 8,266.300 | 129.200 | A |
| 8a1ea92cd417fff | Novi Grad Sarajevo | Dobroševići | 16 | 2,066.800 | 129.200 | A |
| 8a1ef4583b9ffff | Stari Grad Sarajevo | Mošćanica | 16 | 2,066.900 | 129.200 | A |
| 8a1ef4596837fff | Novi Grad Sarajevo | Briješće | 61 | 7,884.400 | 129.300 | A |
| 8a1ea92c928ffff | Novi Grad Sarajevo | Briješće | 47 | 6,075.700 | 129.300 | A |
| 8a1ef4583ac7fff | Stari Grad Sarajevo | Mošćanica | 15 | 1,939.500 | 129.300 | A |
| 8a1ef4594517fff | Novi Grad Sarajevo | Briješće | 29 | 3,752.000 | 129.400 | A |
| 8a1ef45830e7fff | Stari Grad Sarajevo | Mošćanica | 18 | 2,329.700 | 129.400 | A |
| 8a1ef4596877fff | Novi Grad Sarajevo | Briješće | 58 | 7,507.400 | 129.400 | A |
| 8a1ef4594437fff | Novi Grad Sarajevo | Briješće | 23 | 2,977.300 | 129.400 | A |
| 8a1ea92c925ffff | Novi Grad Sarajevo | Briješće | 34 | 4,401.600 | 129.500 | A |
| 8a1ea92c9277fff | Novi Grad Sarajevo | Briješće | 46 | 5,956.500 | 129.500 | A |
| 8a1ef459686ffff | Novi Grad Sarajevo | Briješće | 62 | 8,034.300 | 129.600 | A |
| 8a1ea92c9657fff | Novi Grad Sarajevo | Briješće | 74 | 9,591.700 | 129.600 | A |
| 8a1ef459680ffff | Novi Grad Sarajevo | Briješće | 62 | 8,037.500 | 129.600 | A |
| 8a1ea92c9757fff | Novi Grad Sarajevo | Briješće | 58 | 7,524.600 | 129.700 | A |
| 8a1ef45969a7fff | Novi Grad Sarajevo | Briješće | 73 | 9,472.000 | 129.800 | A |
| 8a1ef458364ffff | Stari Grad Sarajevo | Mošćanica | 25 | 3,245.900 | 129.800 | A |
| 8a1ea92cca5ffff | Novi Grad Sarajevo | Dobroševići | 10 | 1,298.400 | 129.800 | A |
| 8a1ef459695ffff | Novi Grad Sarajevo | Briješće | 56 | 7,273.800 | 129.900 | A |
| 8a1ef45817a7fff | Stari Grad Sarajevo | Mošćanica | 12 | 1,559.100 | 129.900 | A |
| 8a1ef4596847fff | Novi Grad Sarajevo | Briješće | 68 | 8,839.700 | 130.000 | A |
| 8a1ef45b2527fff | Novi Grad Sarajevo | Reljevo | 25 | 3,254.300 | 130.200 | A |
| 8a1ea92c975ffff | Novi Grad Sarajevo | Briješće | 62 | 8,078.200 | 130.300 | A |
| 8a1ef4596947fff | Novi Grad Sarajevo | Briješće | 51 | 6,647.100 | 130.300 | A |
| 8a1ef4586aeffff | Centar Sarajevo | Betanija | 54 | 7,038.100 | 130.300 | B |
| 8a1ef4596807fff | Novi Grad Sarajevo | Briješće | 81 | 10,558.700 | 130.400 | A |
| 8a1ef458286ffff | Centar Sarajevo | Koševo II | 152 | 19,818.500 | 130.400 | B |
| 8a1ef458349ffff | Stari Grad Sarajevo | Baščaršija | 122 | 15,908.400 | 130.400 | A |
| 8a1ea92c9ceffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 75 | 9,783.000 | 130.400 | A |
| 8a1ef459684ffff | Novi Grad Sarajevo | Briješće | 62 | 8,093.200 | 130.500 | A |
| 8a1ea92c89b7fff | Novi Grad Sarajevo | Dobroševići | 19 | 2,480.400 | 130.500 | A |
| 8a1ea92c8c6ffff | Novi Grad Sarajevo | Dobroševići | 26 | 3,397.200 | 130.700 | A |
| 8a1ea92cc6dffff | Novi Grad Sarajevo | Dobroševići | 16 | 2,090.700 | 130.700 | A |
| 8a1ea92cc707fff | Novi Grad Sarajevo | Dobroševići | 14 | 1,831.700 | 130.800 | A |
| 8a1ef4582a4ffff | Centar Sarajevo | Hrastovi-Mrkovići | 102 | 13,351.200 | 130.900 | B |
| 8a1ea92c8d5ffff | Novi Grad Sarajevo | Dobroševići | 10 | 1,309.300 | 130.900 | A |
| 8a1ea92cc70ffff | Novi Grad Sarajevo | Dobroševići | 14 | 1,834.800 | 131.100 | A |
| 8a1ef4584817fff | Centar Sarajevo | Nahorevo | 30 | 3,931.800 | 131.100 | B |
| 8a1ef459685ffff | Novi Grad Sarajevo | Briješće | 91 | 11,927.500 | 131.100 | A |
| 8a1ea92c9667fff | Novi Grad Sarajevo | Briješće | 65 | 8,522.400 | 131.100 | A |
| 8a1ea92c924ffff | Novi Grad Sarajevo | Briješće | 34 | 4,457.900 | 131.100 | A |
| 8a1ef459682ffff | Novi Grad Sarajevo | Briješće | 83 | 10,883.300 | 131.100 | A |
| 8a1ea92cc31ffff | Novi Grad Sarajevo | Dobroševići | 15 | 1,967.600 | 131.200 | A |
| 8a1ea92cc6a7fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,312.400 | 131.200 | A |
| 8a1ea92cc6cffff | Novi Grad Sarajevo | Dobroševići | 16 | 2,100.600 | 131.300 | A |
| 8a1ea92c9c57fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 89 | 11,687.900 | 131.300 | A |
| 8a1ea92c929ffff | Novi Grad Sarajevo | Briješće | 61 | 8,010.900 | 131.300 | A |
| 8a1ea92c89affff | Novi Grad Sarajevo | Dobroševići | 28 | 3,677.800 | 131.300 | A |
| 8a1ea92cd457fff | Novi Grad Sarajevo | Dobroševići | 19 | 2,495.900 | 131.400 | A |
| 8a1ef459694ffff | Novi Grad Sarajevo | Briješće | 63 | 8,278.200 | 131.400 | A |
| 8a1ea92c92dffff | Novi Grad Sarajevo | Briješće | 51 | 6,701.500 | 131.400 | A |
| 8a1ea92c812ffff | Novi Grad Sarajevo | Dobroševići | 19 | 2,500.000 | 131.600 | A |
| 8a1ea92c92f7fff | Novi Grad Sarajevo | Briješće | 56 | 7,371.600 | 131.600 | A |
| 8a1ea92c92d7fff | Novi Grad Sarajevo | Briješće | 64 | 8,426.600 | 131.700 | A |
| 8a1ea92cc20ffff | Novi Grad Sarajevo | Dobroševići | 22 | 2,896.700 | 131.700 | A |
| 8a1ea92cd59ffff | Novi Grad Sarajevo | Dobroševići | 19 | 2,505.900 | 131.900 | A |
| 8a1ea92cc227fff | Novi Grad Sarajevo | Dobroševići | 19 | 2,509.200 | 132.100 | A |
| 8a1ef4582127fff | Centar Sarajevo | Džidžikovac-Koševo I | 170 | 22,458.700 | 132.100 | B |
| 8a1ea92c9257fff | Novi Grad Sarajevo | Briješće | 54 | 7,138.700 | 132.200 | A |
| 8a1ef4581657fff | Stari Grad Sarajevo | Mošćanica | 11 | 1,454.400 | 132.200 | A |
| 8a1ea92cc3a7fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,322.500 | 132.200 | A |
| 8a1ea92cd42ffff | Novi Grad Sarajevo | Dobroševići | 17 | 2,249.500 | 132.300 | A |
| 8a1ea92cd267fff | Novi Grad Sarajevo | Reljevo | 10 | 1,323.300 | 132.300 | A |
| 8a1ea92c880ffff | Novi Grad Sarajevo | Dobroševići | 25 | 3,309.300 | 132.400 | A |
| 8a1ea92cd517fff | Novi Grad Sarajevo | Dobroševići | 33 | 4,370.600 | 132.400 | A |
| 8a1ea92c888ffff | Novi Grad Sarajevo | Dobroševići | 27 | 3,576.400 | 132.500 | A |
| 8a1ea92cbb8ffff | Novi Grad Sarajevo | Briješće | 20 | 2,650.000 | 132.500 | A |
| 8a1ef458470ffff | Centar Sarajevo | Betanija | 13 | 1,722.800 | 132.500 | B |
| 8a1ea92cc66ffff | Novi Grad Sarajevo | Dobroševići | 22 | 2,916.200 | 132.600 | A |
| 8a1ef4586a57fff | Centar Sarajevo | Betanija | 55 | 7,293.600 | 132.600 | B |
| 8a1ef458289ffff | Centar Sarajevo | Džidžikovac-Koševo I | 117 | 15,517.600 | 132.600 | B |
| 8a1ef45830effff | Stari Grad Sarajevo | Mošćanica | 26 | 3,448.900 | 132.700 | A |
| 8a1ef45840affff | Centar Sarajevo | Nahorevo | 17 | 2,256.100 | 132.700 | B |
| 8a1ea92cc177fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,328.000 | 132.800 | A |
| 8a1ea92cd097fff | Novi Grad Sarajevo | Dobroševići | 12 | 1,594.500 | 132.900 | A |
| 8a1ef459c957fff | Stari Grad Sarajevo | Baščaršija | 151 | 20,064.100 | 132.900 | A |
| 8a1ea92cc21ffff | Novi Grad Sarajevo | Dobroševići | 23 | 3,056.500 | 132.900 | A |
| 8a1ea92ccadffff | Novi Grad Sarajevo | Dobroševići | 12 | 1,595.700 | 133.000 | A |
| 8a1ef45945b7fff | Novi Grad Sarajevo | Briješće | 61 | 8,113.900 | 133.000 | A |
| 8a1ea92cdc97fff | Novi Grad Sarajevo | Dobroševići | 26 | 3,461.100 | 133.100 | A |
| 8a1ea92c8cf7fff | Novi Grad Sarajevo | Dobroševići | 24 | 3,196.400 | 133.200 | A |
| 8a1ea92c889ffff | Novi Grad Sarajevo | Dobroševići | 28 | 3,729.700 | 133.200 | A |
| 8a1ea92ccc67fff | Novi Grad Sarajevo | Dobroševići | 13 | 1,731.700 | 133.200 | A |
| 8a1ef4583027fff | Stari Grad Sarajevo | Mošćanica | 30 | 3,996.300 | 133.200 | A |
| 8a1ea92cc297fff | Novi Grad Sarajevo | Dobroševići | 24 | 3,199.400 | 133.300 | A |
| 8a1ef45945affff | Novi Grad Sarajevo | Briješće | 69 | 9,221.000 | 133.600 | A |
| 8a1ef4583a5ffff | Stari Grad Sarajevo | Mošćanica | 13 | 1,738.800 | 133.800 | A |
| 8a1ea92c8817fff | Novi Grad Sarajevo | Dobroševići | 33 | 4,418.000 | 133.900 | A |
| 8a1ef45b174ffff | Centar Sarajevo | Betanija | 17 | 2,276.100 | 133.900 | B |
| 8a1ea92cd51ffff | Novi Grad Sarajevo | Dobroševići | 33 | 4,422.600 | 134.000 | A |
| 8a1ea92c8997fff | Novi Grad Sarajevo | Dobroševići | 30 | 4,021.100 | 134.000 | A |
| 8a1ef458411ffff | Centar Sarajevo | Nahorevo | 38 | 5,094.100 | 134.100 | B |
| 8a1ea92cc36ffff | Novi Grad Sarajevo | Dobroševići | 18 | 2,413.800 | 134.100 | A |
| 8a1ea92c8d67fff | Novi Grad Sarajevo | Dobroševići | 13 | 1,743.400 | 134.100 | A |
| 8a1ea92cd4c7fff | Novi Grad Sarajevo | Dobroševići | 33 | 4,428.200 | 134.200 | A |
| 8a1ea92cc38ffff | Novi Grad Sarajevo | Dobroševići | 17 | 2,283.500 | 134.300 | A |
| 8a1ea92cc35ffff | Novi Grad Sarajevo | Dobroševići | 26 | 3,496.100 | 134.500 | A |
| 8a1ea92c882ffff | Novi Grad Sarajevo | Dobroševići | 12 | 1,614.700 | 134.600 | A |
| 8a1ea92cd4d7fff | Novi Grad Sarajevo | Dobroševići | 42 | 5,652.500 | 134.600 | A |
| 8a1ea92cc22ffff | Novi Grad Sarajevo | Dobroševići | 22 | 2,961.900 | 134.600 | A |
| 8a1ea92cc267fff | Novi Grad Sarajevo | Dobroševići | 32 | 4,313.700 | 134.800 | A |
| 8a1ea92cca57fff | Novi Grad Sarajevo | Dobroševići | 13 | 1,752.500 | 134.800 | A |
| 8a1ef4580027fff | Centar Sarajevo | Hrastovi-Mrkovići | 25 | 3,370.800 | 134.800 | B |
| 8a1ef4583ae7fff | Stari Grad Sarajevo | Mošćanica | 22 | 2,967.500 | 134.900 | A |
| 8a1ea92cdcb7fff | Novi Grad Sarajevo | Dobroševići | 25 | 3,373.900 | 135.000 | A |
| 8a1ea92c899ffff | Novi Grad Sarajevo | Dobroševići | 35 | 4,723.600 | 135.000 | A |
| 8a1ea92cc347fff | Novi Grad Sarajevo | Dobroševići | 18 | 2,429.900 | 135.000 | A |
| 8a1ef4584457fff | Centar Sarajevo | Betanija | 11 | 1,486.000 | 135.100 | B |
| 8a1ea92c8917fff | Novi Grad Sarajevo | Dobroševići | 23 | 3,107.600 | 135.100 | A |
| 8a1ea92cc04ffff | Novi Grad Sarajevo | Dobroševići | 10 | 1,352.400 | 135.200 | A |
| 8a1ea92cc8d7fff | Novi Grad Sarajevo | Dobroševići | 14 | 1,895.500 | 135.400 | A |
| 8a1ea92cca0ffff | Novi Grad Sarajevo | Dobroševići | 11 | 1,490.800 | 135.500 | A |
| 8a1ea92c8857fff | Novi Grad Sarajevo | Dobroševići | 32 | 4,337.400 | 135.500 | A |
| 8a1ef4583af7fff | Stari Grad Sarajevo | Mošćanica | 21 | 2,850.700 | 135.700 | A |
| 8a1ea92cc79ffff | Novi Grad Sarajevo | Dobroševići | 13 | 1,765.200 | 135.800 | A |
| 8a1ef459d517fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 34 | 4,620.700 | 135.900 | A |
| 8a1ea92cc737fff | Novi Grad Sarajevo | Dobroševići | 11 | 1,495.100 | 135.900 | A |
| 8a1ea92c8ce7fff | Novi Grad Sarajevo | Dobroševići | 28 | 3,806.100 | 135.900 | A |
| 8a1ea92ccac7fff | Novi Grad Sarajevo | Dobroševići | 17 | 2,312.000 | 136.000 | A |
| 8a1ea92cd477fff | Novi Grad Sarajevo | Dobroševići | 26 | 3,537.700 | 136.100 | A |
| 8a1ea92cc24ffff | Novi Grad Sarajevo | Dobroševići | 32 | 4,354.100 | 136.100 | A |
| 8a1ef4580baffff | Centar Sarajevo | Betanija | 19 | 2,587.100 | 136.200 | B |
| 8a1ea92c88e7fff | Novi Grad Sarajevo | Dobroševići | 43 | 5,855.600 | 136.200 | A |
| 8a1ea92cc68ffff | Novi Grad Sarajevo | Dobroševići | 14 | 1,906.500 | 136.200 | A |
| 8a1ea92c884ffff | Novi Grad Sarajevo | Dobroševići | 16 | 2,179.600 | 136.200 | A |
| 8a1ea92cc0affff | Novi Grad Sarajevo | Dobroševići | 13 | 1,771.800 | 136.300 | A |
| 8a1ea92cc657fff | Novi Grad Sarajevo | Dobroševići | 21 | 2,862.200 | 136.300 | A |
| 8a1ea92ccb97fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,363.300 | 136.300 | A |
| 8a1ea92cc7affff | Novi Grad Sarajevo | Dobroševići | 15 | 2,045.300 | 136.400 | A |
| 8a1ef459c867fff | Stari Grad Sarajevo | Baščaršija | 156 | 21,296.800 | 136.500 | A |
| 8a1ef4586a2ffff | Centar Sarajevo | Betanija | 72 | 9,837.300 | 136.600 | B |
| 8a1ea92c8907fff | Novi Grad Sarajevo | Dobroševići | 13 | 1,776.300 | 136.600 | A |
| 8a1ea92c8947fff | Novi Grad Sarajevo | Dobroševići | 11 | 1,503.500 | 136.700 | A |
| 8a1ea92cc74ffff | Novi Grad Sarajevo | Dobroševići | 23 | 3,144.900 | 136.700 | A |
| 8a1ef4583437fff | Stari Grad Sarajevo | Kovači | 105 | 14,359.500 | 136.800 | A |
| 8a1ea92cc727fff | Novi Grad Sarajevo | Dobroševići | 17 | 2,325.100 | 136.800 | A |
| 8a1ea92c8caffff | Novi Grad Sarajevo | Dobroševići | 16 | 2,189.700 | 136.900 | A |
| 8a1ef4583aaffff | Stari Grad Sarajevo | Mošćanica | 24 | 3,286.200 | 136.900 | A |
| 8a1ef458329ffff | Stari Grad Sarajevo | Mošćanica | 25 | 3,424.700 | 137.000 | A |
| 8a1ef45809b7fff | Centar Sarajevo | Betanija | 28 | 3,836.500 | 137.000 | B |
| 8a1ea92cd4f7fff | Novi Grad Sarajevo | Dobroševići | 36 | 4,932.900 | 137.000 | A |
| 8a1ea92cdc27fff | Novi Grad Sarajevo | Dobroševići | 11 | 1,508.400 | 137.100 | A |
| 8a1ea92c8d77fff | Novi Grad Sarajevo | Dobroševići | 24 | 3,295.900 | 137.300 | A |
| 8a1ea92ccad7fff | Novi Grad Sarajevo | Dobroševići | 13 | 1,787.400 | 137.500 | A |
| 8a1ea92cd537fff | Novi Grad Sarajevo | Dobroševići | 34 | 4,682.900 | 137.700 | A |
| 8a1ea92cdc9ffff | Novi Grad Sarajevo | Dobroševići | 26 | 3,582.000 | 137.800 | A |
| 8a1ea92cc65ffff | Novi Grad Sarajevo | Dobroševići | 26 | 3,582.200 | 137.800 | A |
| 8a1ea92cc26ffff | Novi Grad Sarajevo | Dobroševići | 46 | 6,338.500 | 137.800 | A |
| 8a1ea92c8d47fff | Novi Grad Sarajevo | Dobroševići | 21 | 2,898.200 | 138.000 | A |
| 8a1ea92cc357fff | Novi Grad Sarajevo | Dobroševići | 25 | 3,455.200 | 138.200 | A |
| 8a1ea92c886ffff | Novi Grad Sarajevo | Dobroševići | 34 | 4,702.300 | 138.300 | A |
| 8a1ea92cc71ffff | Novi Grad Sarajevo | Dobroševići | 20 | 2,766.400 | 138.300 | A |
| 8a1ea92cc2a7fff | Novi Grad Sarajevo | Dobroševići | 20 | 2,768.600 | 138.400 | A |
| 8a1ea92cd45ffff | Novi Grad Sarajevo | Dobroševići | 50 | 6,925.800 | 138.500 | A |
| 8a1ea92cc647fff | Novi Grad Sarajevo | Dobroševići | 41 | 5,683.200 | 138.600 | A |
| 8a1ea92cc667fff | Novi Grad Sarajevo | Dobroševići | 30 | 4,163.700 | 138.800 | A |
| 8a1ea92cc307fff | Novi Grad Sarajevo | Dobroševići | 17 | 2,360.400 | 138.800 | A |
| 8a1ea92cc637fff | Novi Grad Sarajevo | Dobroševići | 17 | 2,360.400 | 138.800 | A |
| 8a1ea92cc78ffff | Novi Grad Sarajevo | Dobroševići | 24 | 3,335.900 | 139.000 | A |
| 8a1ef459d16ffff | Stari Grad Sarajevo | Mošćanica | 10 | 1,390.300 | 139.000 | A |
| 8a1ea92cdc8ffff | Novi Grad Sarajevo | Dobroševići | 21 | 2,920.000 | 139.000 | A |
| 8a1ea92cd3b7fff | Novi Grad Sarajevo | Reljevo | 14 | 1,946.900 | 139.100 | A |
| 8a1ea92c8127fff | Novi Grad Sarajevo | Dobroševići | 55 | 7,661.900 | 139.300 | A |
| 8a1ea92cc6affff | Novi Grad Sarajevo | Dobroševići | 12 | 1,672.200 | 139.300 | A |
| 8a1ef4583b57fff | Stari Grad Sarajevo | Mošćanica | 22 | 3,072.400 | 139.700 | A |
| 8a1ea92c898ffff | Novi Grad Sarajevo | Dobroševići | 65 | 9,090.400 | 139.900 | A |
| 8a1ea92c8d6ffff | Novi Grad Sarajevo | Dobroševići | 42 | 5,874.900 | 139.900 | A |
| 8a1ea92c8d2ffff | Novi Grad Sarajevo | Dobroševići | 11 | 1,539.800 | 140.000 | A |
| 8a1ef4580d57fff | Centar Sarajevo | Pionirska Dolina | 54 | 7,564.400 | 140.100 | B |
| 8a1ea92c88affff | Novi Grad Sarajevo | Dobroševići | 56 | 7,848.100 | 140.100 | A |
| 8a1ea92cca87fff | Novi Grad Sarajevo | Dobroševići | 12 | 1,681.800 | 140.200 | A |
| 8a1ef4583a0ffff | Stari Grad Sarajevo | Mošćanica | 25 | 3,506.700 | 140.300 | A |
| 8a1ea92cc017fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,403.200 | 140.300 | A |
| 8a1ef4583ab7fff | Stari Grad Sarajevo | Mošćanica | 23 | 3,227.900 | 140.300 | A |
| 8a1ea92cca9ffff | Novi Grad Sarajevo | Dobroševići | 19 | 2,668.300 | 140.400 | A |
| 8a1ea92ccc2ffff | Novi Grad Sarajevo | Dobroševići | 17 | 2,388.100 | 140.500 | A |
| 8a1ea92cc2f7fff | Novi Grad Sarajevo | Dobroševići | 29 | 4,077.800 | 140.600 | A |
| 8a1ea92ccacffff | Novi Grad Sarajevo | Dobroševići | 24 | 3,375.900 | 140.700 | A |
| 8a1ea92c8847fff | Novi Grad Sarajevo | Dobroševići | 40 | 5,627.000 | 140.700 | A |
| 8a1ea92cc0f7fff | Novi Grad Sarajevo | Dobroševići | 25 | 3,522.300 | 140.900 | A |
| 8a1ef45841a7fff | Centar Sarajevo | Nahorevo | 54 | 7,608.900 | 140.900 | B |
| 8a1ef45828f7fff | Centar Sarajevo | Koševo II | 195 | 27,500.500 | 141.000 | B |
| 8a1ea92ccc77fff | Novi Grad Sarajevo | Dobroševići | 21 | 2,963.000 | 141.100 | A |
| 8a1ea92ccd07fff | Novi Grad Sarajevo | Dobroševići | 12 | 1,695.300 | 141.300 | A |
| 8a1ef4580667fff | Stari Grad Sarajevo | Sedrenik | 10 | 1,414.200 | 141.400 | A |
| 8a1ea92cd48ffff | Novi Grad Sarajevo | Dobroševići | 57 | 8,065.700 | 141.500 | A |
| 8a1ea92c8c47fff | Novi Grad Sarajevo | Dobroševići | 33 | 4,670.100 | 141.500 | A |
| 8a1ea92c8ceffff | Novi Grad Sarajevo | Dobroševići | 18 | 2,548.700 | 141.600 | A |
| 8a1ea92cc16ffff | Novi Grad Sarajevo | Dobroševići | 14 | 1,982.600 | 141.600 | A |
| 8a1ea92cc34ffff | Novi Grad Sarajevo | Dobroševići | 56 | 7,934.400 | 141.700 | A |
| 8a1ef4583297fff | Stari Grad Sarajevo | Mošćanica | 29 | 4,109.000 | 141.700 | A |
| 8a1ef4580d27fff | Centar Sarajevo | Betanija | 36 | 5,114.200 | 142.100 | B |
| 8a1ea92cc397fff | Novi Grad Sarajevo | Dobroševići | 20 | 2,842.100 | 142.100 | A |
| 8a1ef4583b6ffff | Stari Grad Sarajevo | Mošćanica | 11 | 1,568.100 | 142.600 | A |
| 8a1ef4583a97fff | Stari Grad Sarajevo | Mošćanica | 26 | 3,711.100 | 142.700 | A |
| 8a1ea92cd05ffff | Novi Grad Sarajevo | Reljevo | 16 | 2,288.300 | 143.000 | A |
| 8a1ef45b12c7fff | Centar Sarajevo | Betanija | 44 | 6,300.800 | 143.200 | B |
| 8a1ea92cc677fff | Novi Grad Sarajevo | Dobroševići | 51 | 7,304.900 | 143.200 | A |
| 8a1ef458339ffff | Stari Grad Sarajevo | Mošćanica | 26 | 3,726.500 | 143.300 | A |
| 8a1ea92cc14ffff | Novi Grad Sarajevo | Dobroševići | 10 | 1,434.700 | 143.500 | A |
| 8a1ea92c8c4ffff | Novi Grad Sarajevo | Dobroševići | 76 | 10,917.200 | 143.600 | A |
| 8a1ea92cc717fff | Novi Grad Sarajevo | Dobroševići | 25 | 3,597.400 | 143.900 | A |
| 8a1ef45868c7fff | Centar Sarajevo | Betanija | 25 | 3,605.700 | 144.200 | B |
| 8a1ef4582887fff | Centar Sarajevo | Džidžikovac-Koševo I | 120 | 17,323.700 | 144.400 | B |
| 8a1ef4583417fff | Stari Grad Sarajevo | Kovači | 119 | 17,204.100 | 144.600 | A |
| 8a1ef45b2c87fff | Novi Grad Sarajevo | Reljevo | 15 | 2,171.300 | 144.800 | A |
| 8a1ea92cc047fff | Novi Grad Sarajevo | Dobroševići | 13 | 1,882.300 | 144.800 | A |
| 8a1ea92cda97fff | Novi Grad Sarajevo | Reljevo | 10 | 1,448.000 | 144.800 | A |
| 8a1ea92cdb6ffff | Novi Grad Sarajevo | Reljevo | 11 | 1,594.700 | 145.000 | A |
| 8a1ef459c91ffff | Stari Grad Sarajevo | Ferhadija | 183 | 26,542.100 | 145.000 | A |
| 8a1ef4583b67fff | Stari Grad Sarajevo | Mošćanica | 14 | 2,031.700 | 145.100 | A |
| 8a1ea92ccd2ffff | Novi Grad Sarajevo | Dobroševići | 10 | 1,458.600 | 145.900 | A |
| 8a1ef459d15ffff | Stari Grad Sarajevo | Mošćanica | 20 | 2,933.300 | 146.700 | A |
| 8a1ef459d14ffff | Stari Grad Sarajevo | Mošćanica | 15 | 2,211.700 | 147.400 | A |
| 8a1ef4583b27fff | Stari Grad Sarajevo | Mošćanica | 17 | 2,514.000 | 147.900 | A |
| 8a1ea92cdba7fff | Novi Grad Sarajevo | Reljevo | 11 | 1,633.700 | 148.500 | A |
| 8a1ea92cd0effff | Novi Grad Sarajevo | Reljevo | 22 | 3,267.500 | 148.500 | A |
| 8a1ef459c94ffff | Stari Grad Sarajevo | Baščaršija | 168 | 25,033.300 | 149.000 | A |
| 8a1ef4583a47fff | Stari Grad Sarajevo | Mošćanica | 16 | 2,398.500 | 149.900 | A |
| 8a1ea92cdb4ffff | Novi Grad Sarajevo | Reljevo | 16 | 2,403.500 | 150.200 | A |
| 8a1ef45b211ffff | Novi Grad Sarajevo | Reljevo | 10 | 1,506.400 | 150.600 | A |
| 8a1ef458179ffff | Stari Grad Sarajevo | Mošćanica | 15 | 2,266.300 | 151.100 | A |
| 8a1ea92cd0c7fff | Novi Grad Sarajevo | Reljevo | 15 | 2,279.400 | 152.000 | A |
| 8a1ef45b2c07fff | Novi Grad Sarajevo | Reljevo | 15 | 2,285.500 | 152.400 | A |
| 8a1ea92cda07fff | Novi Grad Sarajevo | Reljevo | 14 | 2,133.400 | 152.400 | A |
| 8a1ef459d49ffff | Stari Grad Sarajevo | Širokača | 80 | 12,198.200 | 152.500 | A |
| 8a1ef458306ffff | Stari Grad Sarajevo | Mošćanica | 30 | 4,575.000 | 152.500 | A |
| 8a1ef4581647fff | Stari Grad Sarajevo | Mošćanica | 12 | 1,842.000 | 153.500 | A |
| 8a1ef45b2cb7fff | Novi Grad Sarajevo | Reljevo | 25 | 3,844.700 | 153.800 | A |
| 8a1ea92cd72ffff | Novi Grad Sarajevo | Reljevo | 14 | 2,153.600 | 153.800 | A |
| 8a1ef459c95ffff | Stari Grad Sarajevo | Baščaršija | 163 | 25,085.500 | 153.900 | A |
| 8a1ef45b2c97fff | Novi Grad Sarajevo | Reljevo | 34 | 5,239.300 | 154.100 | A |
| 8a1ea92cda2ffff | Novi Grad Sarajevo | Reljevo | 23 | 3,549.700 | 154.300 | A |
| 8a1ef4583a4ffff | Stari Grad Sarajevo | Mošćanica | 11 | 1,698.300 | 154.400 | A |
| 8a1ea92cda37fff | Novi Grad Sarajevo | Reljevo | 12 | 1,852.800 | 154.400 | A |
| 8a1ea92cda77fff | Novi Grad Sarajevo | Reljevo | 12 | 1,861.600 | 155.100 | A |
| 8a1ea92cd0cffff | Novi Grad Sarajevo | Reljevo | 27 | 4,188.800 | 155.100 | A |
| 8a1ea92cda67fff | Novi Grad Sarajevo | Reljevo | 14 | 2,177.100 | 155.500 | A |
| 8a1ef4583a37fff | Stari Grad Sarajevo | Mošćanica | 16 | 2,498.700 | 156.200 | A |
| 8a1ea92cd857fff | Novi Grad Sarajevo | Reljevo | 12 | 1,874.200 | 156.200 | A |
| 8a1ef45b2c27fff | Novi Grad Sarajevo | Reljevo | 16 | 2,507.900 | 156.700 | A |
| 8a1ea92cda4ffff | Novi Grad Sarajevo | Reljevo | 10 | 1,568.600 | 156.900 | A |
| 8a1ef45816b7fff | Stari Grad Sarajevo | Mošćanica | 15 | 2,354.900 | 157.000 | A |
| 8a1ea92cda17fff | Novi Grad Sarajevo | Reljevo | 24 | 3,770.300 | 157.100 | A |
| 8a1ea92cd9affff | Novi Grad Sarajevo | Reljevo | 18 | 2,830.700 | 157.300 | A |
| 8a1ef4583157fff | Stari Grad Sarajevo | Mošćanica | 24 | 3,774.600 | 157.300 | A |
| 8a1ef45812c7fff | Stari Grad Sarajevo | Mošćanica | 10 | 1,575.900 | 157.600 | A |
| 8a1ef45b2caffff | Novi Grad Sarajevo | Reljevo | 17 | 2,692.500 | 158.400 | A |
| 8a1ef459d157fff | Stari Grad Sarajevo | Mošćanica | 10 | 1,588.300 | 158.800 | A |
| 8a1ea92cd98ffff | Novi Grad Sarajevo | Reljevo | 12 | 1,908.400 | 159.000 | A |
| 8a1ef45b2d1ffff | Novi Grad Sarajevo | Reljevo | 22 | 3,509.700 | 159.500 | A |
| 8a1ef4583a07fff | Stari Grad Sarajevo | Mošćanica | 28 | 4,472.600 | 159.700 | A |
| 8a1ea92cd337fff | Novi Grad Sarajevo | Reljevo | 24 | 3,836.300 | 159.800 | A |
| 8a1ea92cd06ffff | Novi Grad Sarajevo | Reljevo | 25 | 4,002.200 | 160.100 | A |
| 8a1ef45b2117fff | Novi Grad Sarajevo | Reljevo | 11 | 1,761.900 | 160.200 | A |
| 8a1ea92cdbaffff | Novi Grad Sarajevo | Reljevo | 13 | 2,086.000 | 160.500 | A |
| 8a1ef459c827fff | Stari Grad Sarajevo | Baščaršija | 196 | 31,501.100 | 160.700 | A |
| 8a1ea92cd04ffff | Novi Grad Sarajevo | Reljevo | 35 | 5,627.200 | 160.800 | A |
| 8a1ef4583b8ffff | Stari Grad Sarajevo | Mošćanica | 15 | 2,416.100 | 161.100 | A |
| 8a1ef4583a87fff | Stari Grad Sarajevo | Mošćanica | 33 | 5,323.500 | 161.300 | A |
| 8a1ef4581787fff | Stari Grad Sarajevo | Mošćanica | 20 | 3,231.600 | 161.600 | A |
| 8a1ef45b2c0ffff | Novi Grad Sarajevo | Reljevo | 12 | 1,950.100 | 162.500 | A |
| 8a1ef4583a27fff | Stari Grad Sarajevo | Mošćanica | 26 | 4,239.000 | 163.000 | A |
| 8a1ef4583b5ffff | Stari Grad Sarajevo | Mošćanica | 24 | 3,931.900 | 163.800 | A |
| 8a1ef458366ffff | Stari Grad Sarajevo | Mošćanica | 36 | 5,907.300 | 164.100 | A |
| 8a1ef459c807fff | Stari Grad Sarajevo | Baščaršija | 195 | 32,226.900 | 165.300 | A |
| 8a1ef45812d7fff | Stari Grad Sarajevo | Mošćanica | 16 | 2,661.000 | 166.300 | A |
| 8a1ef4583a67fff | Stari Grad Sarajevo | Mošćanica | 18 | 2,995.400 | 166.400 | A |
| 8a1ea92cd877fff | Novi Grad Sarajevo | Reljevo | 12 | 1,997.400 | 166.500 | A |
| 8a1ef459c90ffff | Stari Grad Sarajevo | Baščaršija | 199 | 33,192.000 | 166.800 | A |
| 8a1ef458315ffff | Stari Grad Sarajevo | Mošćanica | 22 | 3,674.200 | 167.000 | A |
| 8a1ef459c877fff | Stari Grad Sarajevo | Baščaršija | 164 | 27,430.200 | 167.300 | A |
| 8a1ef458164ffff | Stari Grad Sarajevo | Mošćanica | 14 | 2,347.000 | 167.600 | A |
| 8a1ef458304ffff | Stari Grad Sarajevo | Mošćanica | 35 | 5,880.200 | 168.000 | A |
| 8a1ef459c82ffff | Stari Grad Sarajevo | Baščaršija | 194 | 32,771.200 | 168.900 | A |
| 8a1ef4583337fff | Stari Grad Sarajevo | Mošćanica | 32 | 5,410.200 | 169.100 | A |
| 8a1ef45812dffff | Stari Grad Sarajevo | Mošćanica | 16 | 2,714.900 | 169.700 | A |
| 8a1ef4583a2ffff | Stari Grad Sarajevo | Mošćanica | 32 | 5,433.900 | 169.800 | A |
| 8a1ef45816e7fff | Stari Grad Sarajevo | Mošćanica | 10 | 1,718.000 | 171.800 | A |
| 8a1ef4583b2ffff | Stari Grad Sarajevo | Mošćanica | 26 | 4,482.000 | 172.400 | A |
| 8a1ef4583aa7fff | Stari Grad Sarajevo | Mošćanica | 30 | 5,178.700 | 172.600 | A |
| 8a1ef4583a9ffff | Stari Grad Sarajevo | Mošćanica | 35 | 6,052.600 | 172.900 | A |
| 8a1ef458eda7fff | Stari Grad Sarajevo | Mošćanica | 11 | 1,934.600 | 175.900 | A |
| 8a1ef4583b37fff | Stari Grad Sarajevo | Mošćanica | 17 | 3,010.500 | 177.100 | A |
| 8a1ef4583b0ffff | Stari Grad Sarajevo | Mošćanica | 28 | 4,958.900 | 177.100 | A |
| 8a1ef458e90ffff | Stari Grad Sarajevo | Mošćanica | 10 | 1,775.300 | 177.500 | A |
| 8a1ef4583a57fff | Stari Grad Sarajevo | Mošćanica | 32 | 5,735.200 | 179.200 | A |
| 8a1ef4583a6ffff | Stari Grad Sarajevo | Mošćanica | 16 | 2,869.500 | 179.300 | A |
| 8a1ef458128ffff | Stari Grad Sarajevo | Mošćanica | 11 | 1,985.500 | 180.500 | A |
| 8a1ef45817affff | Stari Grad Sarajevo | Mošćanica | 23 | 4,164.600 | 181.100 | A |
| 8a1ef4583a77fff | Stari Grad Sarajevo | Mošćanica | 36 | 6,715.500 | 186.500 | A |
| 8a1ef458178ffff | Stari Grad Sarajevo | Mošćanica | 25 | 4,737.300 | 189.500 | A |
| 8a1ef4583b77fff | Stari Grad Sarajevo | Mošćanica | 35 | 6,689.800 | 191.100 | A |
| 8a1ef4581697fff | Stari Grad Sarajevo | Mošćanica | 27 | 5,213.000 | 193.100 | A |
| 8a1ef458148ffff | Stari Grad Sarajevo | Mošćanica | 19 | 3,686.100 | 194.000 | A |
| 8a1ef45814d7fff | Stari Grad Sarajevo | Mošćanica | 26 | 5,074.400 | 195.200 | A |
| 8a1ef4581487fff | Stari Grad Sarajevo | Mošćanica | 12 | 2,352.600 | 196.000 | A |
| 8a1ef4583acffff | Stari Grad Sarajevo | Mošćanica | 11 | 2,201.200 | 200.100 | A |
| 8a1ef45830f7fff | Stari Grad Sarajevo | Mošćanica | 20 | 4,102.700 | 205.100 | A |
| 8a1ef4581567fff | Stari Grad Sarajevo | Mošćanica | 15 | 3,220.200 | 214.700 | A |
| 8a1ef458022ffff | Stari Grad Sarajevo | Mošćanica | 18 | 3,938.900 | 218.800 | A |
| 8a1ef4583b4ffff | Stari Grad Sarajevo | Mošćanica | 48 | 10,571.800 | 220.200 | A |
| 8a1ef45803affff | Stari Grad Sarajevo | Mošćanica | 13 | 2,926.800 | 225.100 | A |
| 8a1ef45802b7fff | Stari Grad Sarajevo | Mošćanica | 10 | 2,274.800 | 227.500 | A |
| 8a1ef4580227fff | Stari Grad Sarajevo | Mošćanica | 16 | 3,683.200 | 230.200 | A |
| 8a1ef4585777fff | Stari Grad Sarajevo | Mošćanica | 15 | 3,454.500 | 230.300 | A |
| 8a1ef45802e7fff | Stari Grad Sarajevo | Mošćanica | 17 | 4,221.800 | 248.300 | A |

## 5. Vizuelna provjera
Stanovnici u zonama gdje ih ne bi trebalo biti (aproksimacija: ravnomjerno po dijelu polja):

| vrsta | procijenjeno_stanovnika (površinski) |
|---|---|
| aerodrom | 591.000 |
| landuse=industrial | 6,673.000 |
| park | 6,839.000 |

Najgušće MZ (od 81 sa poznatim granicama):

| rang | opcina | mz | st | st_po_km2 |
|---|---|---|---|---|
| 1 | Novi Grad Sarajevo | Alipašino Polje BII | 3026 | 27,995.000 |
| 2 | Novi Grad Sarajevo | Alipašino Polje CII | 2341 | 24,772.000 |
| 3 | Novi Grad Sarajevo | Alipašino Polje CI | 2029 | 24,562.000 |
| 4 | Novi Grad Sarajevo | Alipašino Polje BI | 3700 | 23,232.000 |
| 5 | Novo Sarajevo | Malta | 4200 | 21,748.000 |
| 6 | Novo Sarajevo | Trg heroja | 4936 | 18,842.000 |
| 7 | Novi Grad Sarajevo | Otoka | 2884 | 18,162.000 |
| 8 | Novi Grad Sarajevo | Čengić Vila | 3067 | 17,765.000 |
| 9 | Novo Sarajevo | Grbavica I | 5870 | 17,599.000 |
| 10 | Novo Sarajevo | Hrasno | 1768 | 16,140.000 |
| 11 | Novo Sarajevo | Čengić Vila II | 1574 | 15,696.000 |
| 12 | Novi Grad Sarajevo | Staro Hrasno | 3038 | 14,403.000 |
| 13 | Novo Sarajevo | Grbavica II | 5511 | 14,117.000 |
| 14 | Novi Grad Sarajevo | Alipašin Most III | 7264 | 13,191.000 |
| 15 | Novo Sarajevo | Čengić Vila I | 3870 | 13,063.000 |

Dobrinja, Alipašino Polje, Grbavica (očekivano visoko):

| rang | opcina | mz | st | st_po_km2 |
|---|---|---|---|---|
| 1 | Novi Grad Sarajevo | Alipašino Polje BII | 3026 | 27,995.000 |
| 2 | Novi Grad Sarajevo | Alipašino Polje CII | 2341 | 24,772.000 |
| 3 | Novi Grad Sarajevo | Alipašino Polje CI | 2029 | 24,562.000 |
| 4 | Novi Grad Sarajevo | Alipašino Polje BI | 3700 | 23,232.000 |
| 9 | Novo Sarajevo | Grbavica I | 5870 | 17,599.000 |
| 13 | Novo Sarajevo | Grbavica II | 5511 | 14,117.000 |
| 16 | Novi Grad Sarajevo | Dobrinja D | 5223 | 12,959.000 |
| 19 | Novi Grad Sarajevo | Alipašino Polje AII | 2784 | 11,196.000 |
| 25 | Novi Grad Sarajevo | Dobrinja C | 4832 | 9,631.000 |
| 29 | Novi Grad Sarajevo | Alipašino Polje AI | 2501 | 9,079.000 |
| 30 | Novi Grad Sarajevo | Dobrinja B | 5383 | 8,901.000 |
| 32 | Novi Grad Sarajevo | Dobrinja A | 5535 | 8,852.000 |

Karta za vizuelni pregled: `out/karta.html`.

## 6. Starosne grupe
Zbir grupa = ukupno u svakom polju: **OK** (0 polja odstupa).

Odstupanje zbira grupa po općini od FZS-a (posljedica zaokruživanja po polju):

| opcina | d0_14 | d15_64 | d65plus |
|---|---|---|---|
| Centar Sarajevo | -33 | 36 | -3 |
| Novi Grad Sarajevo | -71 | 37 | 34 |
| Novo Sarajevo | -10 | -5 | 15 |
| Stari Grad Sarajevo | -37 | 68 | -31 |

## Napomene o modelu
- **Stari Grad Sarajevo**: MZ zbirovi iz Grafa 3 (udjeli)
- **Novi Grad Sarajevo**: MZ: β=0.5·udio_2010 + (1−β)·udio_modela; nove MZ s matičnom: nema; bez matične: ['Alipašin Most III', 'Zabrđe']
- Pouzdanost polja: {'B': 5847, 'A': 2500, 'C': 686}
