# Validacija
Sve ispod nivoa općine je model (raspodjela), ne mjerenje.

## 1. Zbir po općini
**OK**

| opcina | model | FZS_2026 | razlika |
|---|---|---|---|
| Centar Sarajevo | 51598 | 51598 | 0 |
| Ilidža | 74137 | 74137 | 0 |
| Novi Grad Sarajevo | 124111 | 124111 | 0 |
| Novo Sarajevo | 61796 | 61796 | 0 |
| Stari Grad Sarajevo | 33103 | 33103 | 0 |
| Vogošća | 30450 | 30450 | 0 |

## 2. Stari Grad: model bez MZ ograničenja vs Graf 3 (udjeli)
Graf 3 ukupno 38,124, FZS 33,103 (porede se udjeli).

**MAPE po MZ: 17.4%** (glavna mjera kvaliteta modela)

| mz | graf3_udio | model_udio | rel_greska |
|---|---|---|---|
| Mošćanica | 0.116 | 0.183 | 0.585 |
| Mahmutovac | 0.056 | 0.032 | 0.415 |
| Kovači | 0.040 | 0.050 | 0.262 |
| Bistrik | 0.083 | 0.063 | 0.240 |
| Medrese | 0.086 | 0.070 | 0.180 |
| Babića bašča | 0.043 | 0.036 | 0.167 |
| Mjedenica | 0.018 | 0.021 | 0.164 |
| Baščaršija | 0.056 | 0.065 | 0.153 |
| Vratnik | 0.087 | 0.075 | 0.138 |
| Sumbuluša | 0.038 | 0.033 | 0.127 |
| Ferhadija | 0.029 | 0.032 | 0.110 |
| Hrid-Jarčedoli | 0.065 | 0.069 | 0.055 |
| Logavina | 0.091 | 0.086 | 0.055 |
| Sedrenik | 0.082 | 0.078 | 0.055 |
| Toka-Džeka | 0.043 | 0.041 | 0.045 |
| Širokača | 0.068 | 0.066 | 0.038 |

## 3. Novi Grad: model bez MZ ograničenja vs udjeli 2010
Udjeli 2010 preskalirani na dio općine bez novih MZ. Odstupanje > 30% je označeno; veće udjele u modelu obično objašnjava nova gradnja nakon 2010.

| mz | model_udio | udio_2010 | omjer | oznaka |
|---|---|---|---|---|
| Alipašino Polje CI | 0.010 | 0.023 | 0.427 | model < 2010 za >30%: provjeriti |
| Alipašin Most II | 0.011 | 0.025 | 0.469 | model < 2010 za >30%: provjeriti |
| Švrakino Selo I | 0.010 | 0.020 | 0.519 | model < 2010 za >30%: provjeriti |
| Čengić Vila | 0.018 | 0.031 | 0.599 | model < 2010 za >30%: provjeriti |
| Alipašino Polje CII | 0.014 | 0.023 | 0.602 | model < 2010 za >30%: provjeriti |
| Aneks | 0.017 | 0.027 | 0.615 | model < 2010 za >30%: provjeriti |
| Alipašino Polje AI | 0.016 | 0.023 | 0.697 | model < 2010 za >30%: provjeriti |
| Dobrinja D | 0.033 | 0.047 | 0.708 |  |
| Švrakino Selo III | 0.013 | 0.018 | 0.736 |  |
| Buća Potok | 0.033 | 0.045 | 0.739 |  |
| Dobrinja B | 0.037 | 0.049 | 0.752 |  |
| Olimpijsko Selo | 0.017 | 0.023 | 0.753 |  |
| Alipašin Most I | 0.054 | 0.066 | 0.810 |  |
| Dobrinja C | 0.034 | 0.041 | 0.816 |  |
| Švrakino Selo II | 0.033 | 0.039 | 0.843 |  |
| Alipašino Polje BII | 0.022 | 0.026 | 0.849 |  |
| Dolac | 0.042 | 0.049 | 0.856 |  |
| Otoka | 0.022 | 0.025 | 0.868 |  |
| Alipašino Polje AII | 0.022 | 0.022 | 0.991 |  |
| Alipašino Polje BI | 0.030 | 0.029 | 1.032 |  |
| Staro Hrasno | 0.025 | 0.024 | 1.034 |  |
| Dobrinja A | 0.052 | 0.038 | 1.362 | model > 2010 za >30%: nova gradnja? |
| Naselje heroja Sokolje | 0.056 | 0.040 | 1.377 | model > 2010 za >30%: nova gradnja? |
| Saraj Polje | 0.062 | 0.041 | 1.515 | model > 2010 za >30%: nova gradnja? |
| Dobroševići | 0.066 | 0.029 | 2.253 | model > 2010 za >30%: nova gradnja? |
| Briješće | 0.087 | 0.037 | 2.349 | model > 2010 za >30%: nova gradnja? |
| Reljevo | 0.033 | 0.008 | 4.062 | model > 2010 za >30%: nova gradnja? |
| Alipašin Most III | 0.061 | nan | nan | nova MZ (nema 2010) |
| Zabrđe | 0.069 | nan | nan | nova MZ (nema 2010) |

Konačni udjeli korišteni kao meko ograničenje: vidi `interim/raspodjela_info.json`.

## 4. Gustina poda (stambeni m² po stanovniku, očekivano 15–60)
Medijan (polja s ≥ 10 st.): 103.0 m²/st. Polja izvan raspona: **4501** od 5029. Polja sa stanovnicima a bez stambenih zgrada (pouzdanost C, samo WorldPop): **708**.

| h3_id | opcina | mz | stanovnici | stambeni_m2 | m2_po_st | pouzdanost |
|---|---|---|---|---|---|---|
| 8a1ef4582acffff | Centar Sarajevo | Hrastovi-Mrkovići | 45 | 73.800 | 1.600 | C |
| 8a1ef4582497fff | Novo Sarajevo | Velešići | 11 | 19.000 | 1.700 | B |
| 8a1ef459019ffff | Novi Grad Sarajevo | Otoka | 143 | 393.200 | 2.700 | C |
| 8a1ef45956f7fff | Novo Sarajevo | Pofalići I | 75 | 239.600 | 3.200 | C |
| 8a1ef4590007fff | Novi Grad Sarajevo | Otoka | 116 | 427.600 | 3.700 | C |
| 8a1ef4582037fff | Centar Sarajevo | Park-Višnjik | 32 | 129.800 | 4.100 | B |
| 8a1ef4590517fff | Novi Grad Sarajevo | Alipašino Polje CI | 205 | 898.000 | 4.400 | C |
| 8a1ef4591b17fff | Centar Sarajevo | Koševsko Brdo | 40 | 178.000 | 4.400 | B |
| 8a1ef459c1a7fff | Stari Grad Sarajevo | Širokača | 50 | 255.000 | 5.100 | C |
| 8a1ef4583617fff | Stari Grad Sarajevo | Mošćanica | 29 | 163.200 | 5.600 | C |
| 8a1ef4583127fff | Stari Grad Sarajevo | Sedrenik | 21 | 122.300 | 5.800 | A |
| 8a1ef4590a1ffff | Novo Sarajevo | Pofalići II | 111 | 646.500 | 5.800 | C |
| 8a1ef4590567fff | Novi Grad Sarajevo | Alipašino Polje AI | 58 | 365.600 | 6.300 | C |
| 8a1ef4590337fff | Novi Grad Sarajevo | Čengić Vila | 104 | 840.400 | 8.100 | C |
| 8a1ef458280ffff | Centar Sarajevo | Koševo II | 25 | 206.700 | 8.300 | B |
| 8a1ef45908d7fff | Novi Grad Sarajevo | Alipašin Most III | 84 | 702.000 | 8.400 | C |
| 8a1ea92cd707fff | Novi Grad Sarajevo | Reljevo | 12 | 105.800 | 8.800 | C |
| 8a1ef45b0617fff | Vogošća | Vogošća | 26 | 232.800 | 9.000 | C |
| 8a1ef4590ba7fff | Novo Sarajevo | Pofalići II | 82 | 823.800 | 10.000 | C |
| 8a1ef4596227fff | Novi Grad Sarajevo | Alipašino Polje AII | 10 | 105.500 | 10.600 | A |
| 8a1ef4582727fff | Centar Sarajevo | Park-Višnjik | 55 | 581.700 | 10.600 | B |
| 8a1ef6965a6ffff | Ilidža | Stupsko Brdo | 46 | 493.500 | 10.700 | C |
| 8a1ef4591a0ffff | Centar Sarajevo | Marijin Dvor | 33 | 373.900 | 11.300 | B |
| 8a1ef45956cffff | Novo Sarajevo | Pofalići I | 70 | 807.300 | 11.500 | C |
| 8a1ef45829b7fff | Centar Sarajevo | Džidžikovac-Koševo I | 23 | 265.900 | 11.600 | C |
| 8a1ef459cd37fff | Centar Sarajevo | Skenderija-Podtekija | 28 | 357.200 | 12.800 | B |
| 8a1ef4590c97fff | Novi Grad Sarajevo | Alipašino Polje AI | 15 | 193.800 | 12.900 | A |
| 8a1ef4591867fff | Novo Sarajevo | Željeznička | 30 | 405.400 | 13.500 | C |
| 8a1ef4596797fff | Ilidža | Naselje Bulevar | 18 | 251.600 | 14.000 | C |
| 8a1ef45911affff | Novo Sarajevo | Grbavica II | 463 | 27,785.900 | 60.000 | B |
| 8a1ef4591d0ffff | Novo Sarajevo | Malta | 406 | 24,375.700 | 60.000 | B |
| 8a1ea92dd81ffff | Ilidža | Gladno polje | 10 | 600.500 | 60.100 | B |
| 8a1ef4591ccffff | Novo Sarajevo | Grbavica II | 496 | 29,830.100 | 60.100 | B |
| 8a1ef459036ffff | Novo Sarajevo | Hrasno | 491 | 29,537.800 | 60.200 | B |
| 8a1ef4590107fff | Novi Grad Sarajevo | Alipašin Most III | 192 | 11,551.100 | 60.200 | A |
| 8a1ef4590c4ffff | Novi Grad Sarajevo | Alipašin Most III | 27 | 1,624.700 | 60.200 | A |
| 8a1ef459116ffff | Novo Sarajevo | Kovačići | 316 | 19,044.000 | 60.300 | B |
| 8a1ea92c3ad7fff | Ilidža | Kakrinje | 24 | 1,447.300 | 60.300 | B |
| 8a1ef459112ffff | Novo Sarajevo | Grbavica I | 412 | 24,851.600 | 60.300 | B |
| 8a1ef45906affff | Novi Grad Sarajevo | Švrakino Selo II | 13 | 784.200 | 60.300 | A |
| 8a1ef4591ab7fff | Novo Sarajevo | Kovačići | 384 | 23,178.600 | 60.400 | B |
| 8a1ef4596287fff | Novi Grad Sarajevo | Saraj Polje | 158 | 9,538.400 | 60.400 | A |
| 8a1ef45911a7fff | Novo Sarajevo | Grbavica II | 546 | 32,979.600 | 60.400 | B |
| 8a1ef4591d57fff | Novo Sarajevo | Željeznička | 543 | 32,802.400 | 60.400 | B |
| 8a1ef459198ffff | Novo Sarajevo | Željeznička | 317 | 19,156.100 | 60.400 | B |
| 8a1ef4591197fff | Novo Sarajevo | Grbavica II | 189 | 11,427.600 | 60.500 | B |
| 8a1ef4590adffff | Novo Sarajevo | Čengić Vila I | 426 | 25,771.800 | 60.500 | B |
| 8a1ef4583387fff | Stari Grad Sarajevo | Mošćanica | 14 | 847.200 | 60.500 | A |
| 8a1ef45900affff | Novi Grad Sarajevo | Otoka | 279 | 16,885.700 | 60.500 | A |
| 8a1ef4591157fff | Novo Sarajevo | Grbavica I | 471 | 28,512.400 | 60.500 | B |
| 8a1ef4591d07fff | Novo Sarajevo | Malta | 547 | 33,141.500 | 60.600 | B |
| 8a1ef45b486ffff | Vogošća | Ljubina-Poturovići | 12 | 727.400 | 60.600 | B |
| 8a1ef4591117fff | Novo Sarajevo | Grbavica II | 635 | 38,500.200 | 60.600 | B |
| 8a1ef4591d5ffff | Novo Sarajevo | Željeznička | 642 | 38,955.100 | 60.700 | B |
| 8a1ef45b0637fff | Vogošća | Vogošća | 70 | 4,247.900 | 60.700 | B |
| 8a1ef45b25affff | Novi Grad Sarajevo | Zabrđe | 25 | 1,517.700 | 60.700 | A |
| 8a1ef45954f7fff | Novo Sarajevo | Pofalići II | 15 | 911.400 | 60.800 | B |
| 8a1ef4582897fff | Centar Sarajevo | Džidžikovac-Koševo I | 31 | 1,883.600 | 60.800 | B |
| 8a1ef4582da7fff | Novo Sarajevo | Gornji Velešići | 48 | 2,917.800 | 60.800 | B |
| 8a1ef4591027fff | Novo Sarajevo | Grbavica I | 202 | 12,286.500 | 60.800 | B |
| 8a1ef45b1657fff | Vogošća | Hotonj | 17 | 1,034.100 | 60.800 | B |
| 8a1ef4590a57fff | Novo Sarajevo | Čengić Vila I | 552 | 33,583.500 | 60.800 | B |
| 8a1ef4591daffff | Novo Sarajevo | Malta | 493 | 29,996.900 | 60.800 | B |
| 8a1ef45942cffff | Novi Grad Sarajevo | Dolac | 273 | 16,619.200 | 60.900 | A |
| 8a1ef459caaffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 76 | 4,627.000 | 60.900 | A |
| 8a1ef45918affff | Novo Sarajevo | Željeznička | 657 | 40,001.900 | 60.900 | B |
| 8a1ef4591aaffff | Novo Sarajevo | Kovačići | 283 | 17,246.600 | 60.900 | B |
| 8a1ef4590d77fff | Novi Grad Sarajevo | Alipašin Most II | 97 | 5,915.900 | 61.000 | A |
| 8a1ef4591d67fff | Novo Sarajevo | Željeznička | 323 | 19,713.200 | 61.000 | B |
| 8a1ef4590a4ffff | Novo Sarajevo | Malta | 666 | 40,675.900 | 61.100 | B |
| 8a1ef4591c67fff | Novo Sarajevo | Željeznička | 852 | 52,045.600 | 61.100 | B |
| 8a1ef45b6447fff | Vogošća | Krivoglavci | 10 | 611.000 | 61.100 | B |
| 8a1ef45b38effff | Vogošća | Ugorsko | 10 | 611.100 | 61.100 | B |
| 8a1ef4582a27fff | Centar Sarajevo | Hrastovi-Mrkovići | 32 | 1,956.600 | 61.100 | B |
| 8a1ef4591c57fff | Novo Sarajevo | Grbavica II | 291 | 17,800.600 | 61.200 | B |
| 8a1ef459c52ffff | Centar Sarajevo | Soukbunar | 15 | 918.100 | 61.200 | B |
| 8a1ef4596cb7fff | Novi Grad Sarajevo | Briješće | 18 | 1,102.100 | 61.200 | A |
| 8a1ef458281ffff | Centar Sarajevo | Koševo II | 52 | 3,184.900 | 61.200 | B |
| 8a1ef4591547fff | Novo Sarajevo | Grbavica II | 87 | 5,331.000 | 61.300 | B |
| 8a1ef459c0dffff | Stari Grad Sarajevo | Toka-Džeka | 28 | 1,716.200 | 61.300 | A |
| 8a1ea92c9957fff | Novi Grad Sarajevo | Zabrđe | 252 | 15,464.300 | 61.400 | A |
| 8a1ef4590877fff | Novi Grad Sarajevo | Buća Potok | 199 | 12,221.300 | 61.400 | A |
| 8a1ef4595697fff | Novo Sarajevo | Pofalići II | 80 | 4,913.600 | 61.400 | B |
| 8a1ef45920affff | Novi Grad Sarajevo | Dobrinja D | 130 | 7,985.200 | 61.400 | A |
| 8a1ef4591b87fff | Novo Sarajevo | Željeznička | 24 | 1,474.600 | 61.400 | B |
| 8a1ef459639ffff | Novi Grad Sarajevo | Alipašino Polje AII | 149 | 9,158.200 | 61.500 | A |
| 8a1ef4591507fff | Novo Sarajevo | Hrasno Brdo | 99 | 6,086.500 | 61.500 | B |
| 8a1ef45b6737fff | Vogošća | Krivoglavci | 10 | 614.800 | 61.500 | B |
| 8a1ef45b159ffff | Vogošća | Vogošća | 54 | 3,320.800 | 61.500 | B |
| 8a1ef4590897fff | Novi Grad Sarajevo | Alipašin Most II | 132 | 8,120.200 | 61.500 | A |
| 8a1ef4592977fff | Novi Grad Sarajevo | Alipašino Polje BI | 267 | 16,429.700 | 61.500 | A |
| 8a1ef45962dffff | Novi Grad Sarajevo | Alipašino Polje BI | 280 | 17,234.200 | 61.600 | A |
| 8a1ef45962a7fff | Novi Grad Sarajevo | Alipašino Polje AII | 306 | 18,836.300 | 61.600 | A |
| 8a1ef6965c1ffff | Ilidža | Ilidža | 18 | 1,108.200 | 61.600 | B |
| 8a1ef459034ffff | Novo Sarajevo | Hrasno | 379 | 23,336.200 | 61.600 | B |
| 8a1ef4591d1ffff | Novo Sarajevo | Malta | 558 | 34,360.300 | 61.600 | B |
| 8a1ef45b4377fff | Vogošća | Kremeš | 12 | 738.900 | 61.600 | B |
| 8a1ef4582d47fff | Centar Sarajevo | Koševsko Brdo | 50 | 3,083.000 | 61.700 | B |
| 8a1ef4591077fff | Novo Sarajevo | Grbavica I | 392 | 24,190.000 | 61.700 | B |
| 8a1ef4590a2ffff | Novo Sarajevo | Pofalići II | 70 | 4,320.800 | 61.700 | B |
| 8a1ef45b44cffff | Vogošća | Ljubina-Poturovići | 11 | 679.200 | 61.700 | B |
| 8a1ef459cceffff | Centar Sarajevo | Soukbunar | 37 | 2,284.700 | 61.700 | B |
| 8a1ef4591c87fff | Novo Sarajevo | Trg heroja | 629 | 38,841.400 | 61.800 | B |
| 8a1ef4590497fff | Novi Grad Sarajevo | Švrakino Selo II | 153 | 9,456.700 | 61.800 | A |
| 8a1ef459c177fff | Stari Grad Sarajevo | Toka-Džeka | 93 | 5,748.900 | 61.800 | A |
| 8a1ef459001ffff | Novi Grad Sarajevo | Otoka | 539 | 33,326.200 | 61.800 | A |
| 8a1ef4592967fff | Novi Grad Sarajevo | Alipašino Polje BI | 286 | 17,684.700 | 61.800 | A |
| 8a1ef459caeffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 36 | 2,226.400 | 61.800 | A |
| 8a1ef4582427fff | Centar Sarajevo | Koševsko Brdo | 68 | 4,207.900 | 61.900 | B |
| 8a1ef45b6377fff | Vogošća | Vogošća | 16 | 990.300 | 61.900 | B |
| 8a1ef4596327fff | Novi Grad Sarajevo | Alipašin Most I | 73 | 4,518.500 | 61.900 | A |
| 8a1ef4596c67fff | Novi Grad Sarajevo | Briješće | 25 | 1,548.600 | 61.900 | A |
| 8a1ef459dc97fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 16 | 991.600 | 62.000 | A |
| 8a1ef4590c27fff | Novi Grad Sarajevo | Alipašin Most II | 86 | 5,330.300 | 62.000 | A |
| 8a1ef45909b7fff | Novi Grad Sarajevo | Alipašin Most II | 44 | 2,730.500 | 62.100 | A |
| 8a1ef45b281ffff | Vogošća | Vogošća | 12 | 745.100 | 62.100 | B |
| 8a1ef459135ffff | Centar Sarajevo | Soukbunar | 41 | 2,547.300 | 62.100 | B |
| 8a1ef459c307fff | Stari Grad Sarajevo | Mahmutovac | 80 | 4,973.800 | 62.200 | A |
| 8a1ef45b3ce7fff | Vogošća | Ugorsko | 23 | 1,430.700 | 62.200 | B |
| 8a1ef45b6667fff | Vogošća | Krivoglavci | 15 | 934.600 | 62.300 | B |
| 8a1ef459c337fff | Stari Grad Sarajevo | Mahmutovac | 112 | 6,980.400 | 62.300 | A |
| 8a1ef6965d6ffff | Ilidža | Ilidža | 44 | 2,746.900 | 62.400 | B |
| 8a1ef459568ffff | Novo Sarajevo | Pofalići II | 570 | 35,593.800 | 62.400 | B |
| 8a1ef45b1137fff | Vogošća | Vogošća | 25 | 1,561.700 | 62.500 | B |
| 8a1ef45b3b1ffff | Vogošća | Hotonj | 43 | 2,688.400 | 62.500 | B |
| 8a1ea92c9917fff | Novi Grad Sarajevo | Zabrđe | 119 | 7,442.200 | 62.500 | A |
| 8a1ea925b88ffff | Vogošća | Gora | 26 | 1,626.400 | 62.600 | B |
| 8a1ef4590037fff | Novi Grad Sarajevo | Alipašin Most III | 278 | 17,390.100 | 62.600 | A |
| 8a1ea92c9837fff | Novi Grad Sarajevo | Zabrđe | 15 | 938.300 | 62.600 | A |
| 8a1ef4590ac7fff | Novo Sarajevo | Čengić Vila I | 242 | 15,141.600 | 62.600 | B |
| 8a1ef45b2a47fff | Vogošća | Uglješići | 16 | 1,001.400 | 62.600 | B |
| 8a1ef4591187fff | Novo Sarajevo | Grbavica II | 383 | 23,974.200 | 62.600 | B |
| 8a1ef459cb2ffff | Stari Grad Sarajevo | Babića bašča | 91 | 5,696.400 | 62.600 | A |
| 8a1ef4595baffff | Novo Sarajevo | Velešići | 18 | 1,126.900 | 62.600 | B |
| 8a1ef459c857fff | Stari Grad Sarajevo | Bistrik | 139 | 8,710.600 | 62.700 | A |
| 8a1ef459c157fff | Stari Grad Sarajevo | Toka-Džeka | 73 | 4,575.500 | 62.700 | A |
| 8a1ef4591d37fff | Novo Sarajevo | Pofalići II | 409 | 25,637.400 | 62.700 | B |
| 8a1ef45b565ffff | Vogošća | Tihovići | 10 | 627.000 | 62.700 | B |
| 8a1ef696580ffff | Ilidža | Naselje Bulevar | 10 | 627.100 | 62.700 | B |
| 8a1ef4591007fff | Novo Sarajevo | Grbavica I | 317 | 19,884.300 | 62.700 | B |
| 8a1ef459cc27fff | Centar Sarajevo | Skenderija-Podtekija | 60 | 3,764.300 | 62.700 | B |
| 8a1ef45946dffff | Novi Grad Sarajevo | Alipašin Most II | 130 | 8,156.900 | 62.700 | A |
| 8a1ef45b3ceffff | Vogošća | Ugorsko | 11 | 690.400 | 62.800 | B |
| 8a1ef45962d7fff | Novi Grad Sarajevo | Alipašino Polje BI | 368 | 23,102.100 | 62.800 | A |
| 8a1ef45923a7fff | Novi Grad Sarajevo | Dobrinja C | 167 | 10,484.800 | 62.800 | A |
| 8a1ea92e90affff | Vogošća | Svrake | 14 | 879.100 | 62.800 | B |
| 8a1ea92d9b2ffff | Ilidža | Blažuj | 13 | 816.600 | 62.800 | B |
| 8a1ea92e93b7fff | Vogošća | Semizovac | 12 | 754.000 | 62.800 | B |
| 8a1ea92e9017fff | Vogošća | Svrake | 14 | 879.800 | 62.800 | B |
| 8a1ef45b6b5ffff | Vogošća | Ljubina-Poturovići | 18 | 1,132.300 | 62.900 | B |
| 8a1ef4590507fff | Novi Grad Sarajevo | Alipašino Polje AI | 168 | 10,568.600 | 62.900 | A |
| 8a1ef4590a97fff | Novo Sarajevo | Čengić Vila II | 414 | 26,045.200 | 62.900 | B |
| 8a1ef4596337fff | Novi Grad Sarajevo | Alipašin Most I | 12 | 755.100 | 62.900 | A |
| 8a1ef4590a6ffff | Novo Sarajevo | Pofalići II | 326 | 20,534.500 | 63.000 | B |
| 8a1ef459056ffff | Novi Grad Sarajevo | Švrakino Selo II | 163 | 10,273.200 | 63.000 | A |
| 8a1ef45b6297fff | Vogošća | Krivoglavci | 17 | 1,071.700 | 63.000 | B |
| 8a1ef45b2aa7fff | Vogošća | Vogošća | 25 | 1,576.200 | 63.000 | B |
| 8a1ea92cd757fff | Novi Grad Sarajevo | Zabrđe | 267 | 16,833.800 | 63.000 | A |
| 8a1ef45b156ffff | Vogošća | Hotonj | 11 | 693.700 | 63.100 | B |
| 8a1ef4592907fff | Novi Grad Sarajevo | Alipašino Polje BI | 333 | 21,001.200 | 63.100 | A |
| 8a1ef459030ffff | Novi Grad Sarajevo | Staro Hrasno | 458 | 28,896.600 | 63.100 | A |
| 8a1ef45b075ffff | Vogošća | Vogošća | 10 | 631.200 | 63.100 | B |
| 8a1ef4591ae7fff | Centar Sarajevo | Skenderija-Podtekija | 40 | 2,525.200 | 63.100 | B |
| 8a1ef45b2ab7fff | Vogošća | Vogošća | 12 | 757.600 | 63.100 | B |
| 8a1ef45b6347fff | Vogošća | Vogošća | 10 | 631.400 | 63.100 | B |
| 8a1ef4592c6ffff | Novi Grad Sarajevo | Dobrinja A | 158 | 9,976.500 | 63.100 | A |
| 8a1ef45b295ffff | Vogošća | Vogošća | 17 | 1,073.500 | 63.100 | B |
| 8a1ef45b4187fff | Vogošća | Ljubina-Poturovići | 10 | 632.500 | 63.200 | B |
| 8a1ef45b3337fff | Vogošća | Hotonj | 15 | 948.800 | 63.300 | B |
| 8a1ef458258ffff | Novo Sarajevo | Velešići | 34 | 2,152.000 | 63.300 | B |
| 8a1ef459c167fff | Stari Grad Sarajevo | Bistrik | 128 | 8,104.500 | 63.300 | A |
| 8a1ef4590137fff | Novi Grad Sarajevo | Alipašin Most III | 198 | 12,536.700 | 63.300 | A |
| 8a1ef45b3c77fff | Vogošća | Ugorsko | 27 | 1,709.900 | 63.300 | B |
| 8a1ef45b62effff | Vogošća | Vogošća | 58 | 3,674.100 | 63.300 | B |
| 8a1ef4591d77fff | Novo Sarajevo | Željeznička | 694 | 43,970.400 | 63.400 | B |
| 8a1ef459cb6ffff | Stari Grad Sarajevo | Vratnik | 62 | 3,929.200 | 63.400 | A |
| 8a1ef45908a7fff | Novi Grad Sarajevo | Alipašin Most II | 142 | 9,000.300 | 63.400 | A |
| 8a1ef4591c1ffff | Novo Sarajevo | Trg heroja | 314 | 19,907.700 | 63.400 | B |
| 8a1ef459620ffff | Novi Grad Sarajevo | Alipašino Polje AII | 414 | 26,252.700 | 63.400 | A |
| 8a1ef45b0897fff | Vogošća | Vogošća | 16 | 1,015.600 | 63.500 | B |
| 8a1ef45b0b17fff | Vogošća | Vogošća | 12 | 762.200 | 63.500 | B |
| 8a1ef459076ffff | Novi Grad Sarajevo | Aneks | 154 | 9,782.700 | 63.500 | A |
| 8a1ef45900cffff | Novi Grad Sarajevo | Aneks | 71 | 4,510.300 | 63.500 | A |
| 8a1ef45b4daffff | Vogošća | Nebočaj | 10 | 635.900 | 63.600 | B |
| 8a1ef459288ffff | Novi Grad Sarajevo | Dobrinja A | 17 | 1,081.500 | 63.600 | A |
| 8a1ef6964b5ffff | Ilidža | Pejton | 73 | 4,645.000 | 63.600 | B |
| 8a1ea92c9697fff | Novi Grad Sarajevo | Briješće | 10 | 636.400 | 63.600 | A |
| 8a1ef4596217fff | Novi Grad Sarajevo | Alipašino Polje AII | 415 | 26,412.700 | 63.600 | A |
| 8a1ea925b38ffff | Vogošća | Kremeš | 22 | 1,401.300 | 63.700 | B |
| 8a1ef459146ffff | Novo Sarajevo | Vraca | 20 | 1,274.100 | 63.700 | B |
| 8a1ea92dd22ffff | Ilidža | Blažuj | 77 | 4,911.400 | 63.800 | B |
| 8a1ef45918b7fff | Novo Sarajevo | Željeznička | 340 | 21,717.000 | 63.900 | B |
| 8a1ef45807b7fff | Centar Sarajevo | Hrastovi-Mrkovići | 24 | 1,534.200 | 63.900 | B |
| 8a1ef45b3c0ffff | Vogošća | Ugorsko | 22 | 1,406.400 | 63.900 | B |
| 8a1ef459c377fff | Stari Grad Sarajevo | Mahmutovac | 70 | 4,475.700 | 63.900 | A |
| 8a1ef4590727fff | Novi Grad Sarajevo | Švrakino Selo I | 104 | 6,652.200 | 64.000 | A |
| 8a1ef45907a7fff | Novi Grad Sarajevo | Švrakino Selo I | 83 | 5,310.200 | 64.000 | A |
| 8a1ef45b076ffff | Vogošća | Vogošća | 98 | 6,271.000 | 64.000 | B |
| 8a1ef4591a97fff | Novo Sarajevo | Grbavica I | 220 | 14,080.900 | 64.000 | B |
| 8a1ea92c9cc7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 40 | 2,560.500 | 64.000 | A |
| 8a1ef4583d57fff | Stari Grad Sarajevo | Sedrenik | 43 | 2,752.600 | 64.000 | A |
| 8a1ef4595017fff | Novo Sarajevo | Pofalići II | 10 | 640.500 | 64.000 | B |
| 8a1ef45b3adffff | Vogošća | Hotonj | 17 | 1,088.900 | 64.100 | B |
| 8a1ef4590357fff | Novi Grad Sarajevo | Staro Hrasno | 340 | 21,782.000 | 64.100 | A |
| 8a1ef45b6a2ffff | Vogošća | Ljubina-Poturovići | 10 | 641.000 | 64.100 | B |
| 8a1ef4583547fff | Stari Grad Sarajevo | Sumbuluša | 68 | 4,359.400 | 64.100 | A |
| 8a1ef45b0777fff | Vogošća | Vogošća | 195 | 12,509.500 | 64.200 | B |
| 8a1ef459046ffff | Novi Grad Sarajevo | Švrakino Selo I | 103 | 6,610.100 | 64.200 | A |
| 8a1ef459562ffff | Novo Sarajevo | Pofalići II | 80 | 5,134.700 | 64.200 | B |
| 8a1ef4592737fff | Novi Grad Sarajevo | Dobrinja B | 18 | 1,155.600 | 64.200 | A |
| 8a1ef4590c47fff | Novi Grad Sarajevo | Alipašin Most III | 398 | 25,571.500 | 64.200 | A |
| 8a1ea925a5b7fff | Vogošća | Donja Vogošća | 29 | 1,863.500 | 64.300 | B |
| 8a1ef45b0607fff | Vogošća | Vogošća | 198 | 12,724.100 | 64.300 | B |
| 8a1ef45946effff | Novi Grad Sarajevo | Buća Potok | 26 | 1,670.900 | 64.300 | A |
| 8a1ea92cb827fff | Ilidža | Doglodi | 10 | 642.700 | 64.300 | B |
| 8a1ef45b3827fff | Vogošća | Hotonj | 79 | 5,079.700 | 64.300 | B |
| 8a1ef6965a0ffff | Ilidža | Naselje Bulevar | 32 | 2,058.000 | 64.300 | B |
| 8a1ef45b0567fff | Vogošća | Vogošća | 139 | 8,940.600 | 64.300 | B |
| 8a1ef45b305ffff | Vogošća | Grahovište | 11 | 707.500 | 64.300 | B |
| 8a1ef45b3c37fff | Vogošća | Ugorsko | 30 | 1,930.900 | 64.400 | B |
| 8a1ef45b4237fff | Vogošća | Kremeš | 13 | 836.800 | 64.400 | B |
| 8a1ef459039ffff | Novi Grad Sarajevo | Aneks | 158 | 10,175.900 | 64.400 | A |
| 8a1ef45b43affff | Vogošća | Kremeš | 17 | 1,094.900 | 64.400 | B |
| 8a1ef4590237fff | Novi Grad Sarajevo | Staro Hrasno | 823 | 53,009.100 | 64.400 | A |
| 8a1ef4594c2ffff | Novi Grad Sarajevo | Zabrđe | 10 | 644.600 | 64.500 | A |
| 8a1ef458291ffff | Centar Sarajevo | Betanija | 10 | 644.600 | 64.500 | B |
| 8a1ef4590737fff | Novi Grad Sarajevo | Švrakino Selo I | 105 | 6,769.100 | 64.500 | A |
| 8a1ef45b62d7fff | Vogošća | Vogošća | 16 | 1,032.000 | 64.500 | B |
| 8a1ea92e90a7fff | Vogošća | Svrake | 12 | 774.100 | 64.500 | B |
| 8a1ef458234ffff | Stari Grad Sarajevo | Logavina | 96 | 6,194.400 | 64.500 | A |
| 8a1ef4591d8ffff | Novo Sarajevo | Trg heroja | 264 | 17,044.500 | 64.600 | B |
| 8a1ea92e9b97fff | Vogošća | Donja Vogošća | 18 | 1,163.500 | 64.600 | B |
| 8a1ef45b0867fff | Vogošća | Kremeš | 21 | 1,358.400 | 64.700 | B |
| 8a1ef459292ffff | Novi Grad Sarajevo | Alipašino Polje BI | 437 | 28,270.200 | 64.700 | A |
| 8a1ea92c9447fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 68 | 4,401.400 | 64.700 | A |
| 8a1ef4591a87fff | Novo Sarajevo | Kovačići | 407 | 26,344.700 | 64.700 | B |
| 8a1ef4582ce7fff | Centar Sarajevo | Koševsko Brdo | 47 | 3,042.300 | 64.700 | B |
| 8a1ef45b59affff | Vogošća | Kremeš | 19 | 1,230.700 | 64.800 | B |
| 8a1ef459600ffff | Novi Grad Sarajevo | Briješće | 65 | 4,213.700 | 64.800 | A |
| 8a1ef45b3c47fff | Vogošća | Ugorsko | 10 | 648.400 | 64.800 | B |
| 8a1ef45b3047fff | Vogošća | Grahovište | 10 | 648.800 | 64.900 | B |
| 8a1ef45b339ffff | Vogošća | Grahovište | 25 | 1,622.000 | 64.900 | B |
| 8a1ef45910b7fff | Novo Sarajevo | Vraca | 320 | 20,784.700 | 65.000 | B |
| 8a1ef4590af7fff | Novo Sarajevo | Čengić Vila I | 185 | 12,017.000 | 65.000 | B |
| 8a1ea925b8b7fff | Vogošća | Gora | 42 | 2,728.300 | 65.000 | B |
| 8a1ef45b6127fff | Vogošća | Krivoglavci | 36 | 2,339.500 | 65.000 | B |
| 8a1ea925b4e7fff | Vogošća | Garež | 14 | 909.800 | 65.000 | B |
| 8a1ef45b68d7fff | Vogošća | Krivoglavci | 25 | 1,625.200 | 65.000 | B |
| 8a1ef45b5267fff | Vogošća | Tihovići | 10 | 650.100 | 65.000 | B |
| 8a1ef45b32b7fff | Vogošća | Grahovište | 20 | 1,300.300 | 65.000 | B |
| 8a1ea92ed2e7fff | Vogošća | Donja Vogošća | 13 | 845.300 | 65.000 | B |
| 8a1ef459015ffff | Novo Sarajevo | Čengić Vila II | 371 | 24,125.500 | 65.000 | B |
| 8a1ef4595aa7fff | Novo Sarajevo | Velešići | 18 | 1,170.500 | 65.000 | B |
| 8a1ef4592927fff | Novi Grad Sarajevo | Alipašino Polje BI | 734 | 47,734.800 | 65.000 | A |
| 8a1ef45907affff | Novi Grad Sarajevo | Švrakino Selo I | 56 | 3,642.300 | 65.000 | A |
| 8a1ef45b4adffff | Vogošća | Kremeš | 14 | 910.600 | 65.000 | B |
| 8a1ef45b2a4ffff | Vogošća | Uglješići | 30 | 1,951.800 | 65.100 | B |
| 8a1ef45b1677fff | Vogošća | Hotonj | 15 | 976.300 | 65.100 | B |
| 8a1ea92cd54ffff | Novi Grad Sarajevo | Dobroševići | 13 | 846.200 | 65.100 | A |
| 8a1ef45b6677fff | Vogošća | Krivoglavci | 17 | 1,107.000 | 65.100 | B |
| 8a1ef45b0767fff | Vogošća | Vogošća | 385 | 25,074.600 | 65.100 | B |
| 8a1ef4583daffff | Stari Grad Sarajevo | Sedrenik | 59 | 3,843.800 | 65.100 | A |
| 8a1ef45b4207fff | Vogošća | Kremeš | 14 | 912.500 | 65.200 | B |
| 8a1ef4596017fff | Novi Grad Sarajevo | Briješće | 54 | 3,519.900 | 65.200 | A |
| 8a1ef45834dffff | Stari Grad Sarajevo | Kovači | 51 | 3,325.300 | 65.200 | A |
| 8a1ef45b00dffff | Vogošća | Vogošća | 467 | 30,460.400 | 65.200 | B |
| 8a1ef45b074ffff | Vogošća | Vogošća | 383 | 24,989.700 | 65.200 | B |
| 8a1ef45b4c57fff | Vogošća | Ljubina-Poturovići | 30 | 1,957.900 | 65.300 | B |
| 8a1ef45b0d57fff | Vogošća | Kremeš | 18 | 1,174.800 | 65.300 | B |
| 8a1ef45b5917fff | Vogošća | Kremeš | 30 | 1,958.300 | 65.300 | B |
| 8a1ef45b1117fff | Vogošća | Vogošća | 87 | 5,682.300 | 65.300 | B |
| 8a1ef459624ffff | Novi Grad Sarajevo | Alipašino Polje AI | 144 | 9,409.900 | 65.300 | A |
| 8a1ef4590a07fff | Novo Sarajevo | Pofalići II | 184 | 12,027.100 | 65.400 | B |
| 8a1ef45b04effff | Vogošća | Vogošća | 26 | 1,700.600 | 65.400 | B |
| 8a1ef45b4d17fff | Vogošća | Nebočaj | 15 | 981.900 | 65.500 | B |
| 8a1ef45b4197fff | Vogošća | Ljubina-Poturovići | 11 | 720.100 | 65.500 | B |
| 8a1ef45b07affff | Vogošća | Vogošća | 599 | 39,217.400 | 65.500 | B |
| 8a1ea92c960ffff | Novi Grad Sarajevo | Briješće | 78 | 5,106.900 | 65.500 | A |
| 8a1ef4592917fff | Novi Grad Sarajevo | Alipašino Polje BI | 250 | 16,368.600 | 65.500 | A |
| 8a1ea92e9467fff | Vogošća | Svrake | 15 | 982.100 | 65.500 | B |
| 8a1ea925b8a7fff | Vogošća | Gora | 20 | 1,311.300 | 65.600 | B |
| 8a1ef45b0017fff | Vogošća | Vogošća | 77 | 5,049.400 | 65.600 | B |
| 8a1ef4596a57fff | Novi Grad Sarajevo | Alipašin Most I | 98 | 6,427.400 | 65.600 | A |
| 8a1ef4586607fff | Centar Sarajevo | Šip | 58 | 3,806.000 | 65.600 | B |
| 8a1ef4594c17fff | Novi Grad Sarajevo | Zabrđe | 27 | 1,772.200 | 65.600 | A |
| 8a1ef4583537fff | Stari Grad Sarajevo | Medrese | 117 | 7,681.000 | 65.600 | A |
| 8a1ef459115ffff | Novo Sarajevo | Grbavica I | 488 | 32,037.900 | 65.700 | B |
| 8a1ef45864dffff | Centar Sarajevo | Šip | 21 | 1,379.200 | 65.700 | B |
| 8a1ef45b439ffff | Vogošća | Kremeš | 24 | 1,576.300 | 65.700 | B |
| 8a1ef45b1877fff | Vogošća | Vogošća | 141 | 9,267.000 | 65.700 | B |
| 8a1ef45b58b7fff | Vogošća | Kremeš | 19 | 1,249.100 | 65.700 | B |
| 8a1ef4596247fff | Novi Grad Sarajevo | Alipašino Polje AI | 217 | 14,266.600 | 65.700 | A |
| 8a1ef45b3d17fff | Vogošća | Uglješići | 30 | 1,972.700 | 65.800 | B |
| 8a1ef6965c37fff | Ilidža | Ilidža | 148 | 9,733.400 | 65.800 | B |
| 8a1ef4590aa7fff | Novo Sarajevo | Pofalići II | 175 | 11,510.800 | 65.800 | B |
| 8a1ea925bd27fff | Vogošća | Gora | 100 | 6,577.600 | 65.800 | B |
| 8a1ef459298ffff | Novi Grad Sarajevo | Saraj Polje | 146 | 9,609.400 | 65.800 | A |
| 8a1ef4582507fff | Novo Sarajevo | Velešići | 188 | 12,378.800 | 65.800 | B |
| 8a1ef459cc57fff | Centar Sarajevo | Soukbunar | 39 | 2,569.600 | 65.900 | B |
| 8a1ef4591c4ffff | Novo Sarajevo | Grbavica II | 176 | 11,602.100 | 65.900 | B |
| 8a1ef4590067fff | Novo Sarajevo | Čengić Vila II | 285 | 18,792.500 | 65.900 | B |
| 8a1ef69654cffff | Ilidža | Sokolović-kolonija | 25 | 1,648.500 | 65.900 | B |
| 8a1ef45b626ffff | Vogošća | Vogošća | 27 | 1,782.900 | 66.000 | B |
| 8a1ef459615ffff | Novi Grad Sarajevo | Briješće | 27 | 1,783.200 | 66.000 | A |
| 8a1ef459084ffff | Novi Grad Sarajevo | Buća Potok | 39 | 2,576.000 | 66.100 | A |
| 8a1ef459105ffff | Novo Sarajevo | Kovačići | 201 | 13,283.700 | 66.100 | B |
| 8a1ef45b060ffff | Vogošća | Vogošća | 252 | 16,654.900 | 66.100 | B |
| 8a1ef4592887fff | Novi Grad Sarajevo | Dobrinja A | 222 | 14,678.000 | 66.100 | A |
| 8a1ea92c9117fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 101 | 6,678.200 | 66.100 | A |
| 8a1ef4590c5ffff | Novi Grad Sarajevo | Alipašin Most III | 154 | 10,182.600 | 66.100 | A |
| 8a1ef459009ffff | Novi Grad Sarajevo | Švrakino Selo I | 134 | 8,862.000 | 66.100 | A |
| 8a1ef45b52a7fff | Vogošća | Tihovići | 11 | 727.600 | 66.100 | B |
| 8a1ef45b00cffff | Vogošća | Vogošća | 232 | 15,359.100 | 66.200 | B |
| 8a1ef459cba7fff | Stari Grad Sarajevo | Bistrik | 127 | 8,409.200 | 66.200 | A |
| 8a1ef45b3287fff | Vogošća | Grahovište | 15 | 993.200 | 66.200 | B |
| 8a1ef459c06ffff | Stari Grad Sarajevo | Mahmutovac | 150 | 9,942.500 | 66.300 | A |
| 8a1ea925b4f7fff | Vogošća | Garež | 22 | 1,458.600 | 66.300 | B |
| 8a1ef45b6c27fff | Vogošća | Svrake | 15 | 994.800 | 66.300 | B |
| 8a1ef4590a37fff | Novo Sarajevo | Pofalići II | 194 | 12,869.300 | 66.300 | B |
| 8a1ef459086ffff | Novi Grad Sarajevo | Buća Potok | 168 | 11,147.300 | 66.400 | A |
| 8a1ef45b4ceffff | Vogošća | Ljubina-Poturovići | 32 | 2,124.000 | 66.400 | B |
| 8a1ef459c267fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 12 | 797.100 | 66.400 | A |
| 8a1ef459c147fff | Stari Grad Sarajevo | Bistrik | 117 | 7,772.500 | 66.400 | A |
| 8a1ea92c96c7fff | Novi Grad Sarajevo | Briješće | 67 | 4,452.200 | 66.500 | A |
| 8a1ea92e9b47fff | Vogošća | Nebočaj | 16 | 1,064.100 | 66.500 | B |
| 8a1ea92ca4e7fff | Ilidža | Blažuj | 14 | 931.100 | 66.500 | B |
| 8a1ef459011ffff | Novi Grad Sarajevo | Alipašin Most III | 845 | 56,233.100 | 66.500 | A |
| 8a1ef4590717fff | Novi Grad Sarajevo | Švrakino Selo I | 122 | 8,126.000 | 66.600 | A |
| 8a1ea92c9b77fff | Novi Grad Sarajevo | Zabrđe | 20 | 1,332.200 | 66.600 | A |
| 8a1ef45919b7fff | Novo Sarajevo | Pofalići I | 17 | 1,132.500 | 66.600 | B |
| 8a1ef45b45a7fff | Vogošća | Semizovac | 157 | 10,474.400 | 66.700 | B |
| 8a1ea92c836ffff | Novi Grad Sarajevo | Briješće | 18 | 1,201.100 | 66.700 | A |
| 8a1ef45921b7fff | Novi Grad Sarajevo | Dobrinja D | 128 | 8,544.500 | 66.800 | A |
| 8a1ef459c0a7fff | Stari Grad Sarajevo | Širokača | 44 | 2,938.300 | 66.800 | A |
| 8a1ef4583797fff | Stari Grad Sarajevo | Vratnik | 90 | 6,017.300 | 66.900 | A |
| 8a1ef45b43a7fff | Vogošća | Kremeš | 17 | 1,137.200 | 66.900 | B |
| 8a1ef458079ffff | Centar Sarajevo | Hrastovi-Mrkovići | 11 | 735.800 | 66.900 | B |
| 8a1ef4586617fff | Centar Sarajevo | Šip | 43 | 2,877.200 | 66.900 | B |
| 8a1ef4596a5ffff | Novi Grad Sarajevo | Alipašin Most I | 119 | 7,967.700 | 67.000 | A |
| 8a1ef458249ffff | Centar Sarajevo | Crni Vrh-Gorica | 135 | 9,040.000 | 67.000 | B |
| 8a1ef45928a7fff | Novi Grad Sarajevo | Dobrinja A | 241 | 16,146.100 | 67.000 | A |
| 8a1ef45b479ffff | Vogošća | Ljubina-Poturovići | 15 | 1,005.200 | 67.000 | B |
| 8a1ef459ca27fff | Stari Grad Sarajevo | Babića bašča | 103 | 6,903.700 | 67.000 | A |
| 8a1ef4582517fff | Novo Sarajevo | Velešići | 175 | 11,733.600 | 67.000 | B |
| 8a1ef4590777fff | Novi Grad Sarajevo | Švrakino Selo III | 107 | 7,177.700 | 67.100 | A |
| 8a1ef45b1d17fff | Vogošća | Blagovac | 10 | 671.100 | 67.100 | B |
| 8a1ef45b0707fff | Vogošća | Vogošća | 307 | 20,608.200 | 67.100 | B |
| 8a1ef458340ffff | Stari Grad Sarajevo | Vratnik | 117 | 7,869.800 | 67.300 | A |
| 8a1ef4596417fff | Ilidža | Naselje Bulevar | 31 | 2,087.300 | 67.300 | B |
| 8a1ef45908cffff | Novo Sarajevo | Kvadrant | 33 | 2,224.100 | 67.400 | B |
| 8a1ef4596067fff | Novi Grad Sarajevo | Briješće | 166 | 11,195.400 | 67.400 | A |
| 8a1ef45b681ffff | Vogošća | Svrake | 23 | 1,551.900 | 67.500 | B |
| 8a1ea925a69ffff | Vogošća | Nebočaj | 14 | 945.600 | 67.500 | B |
| 8a1ea92ce0d7fff | Ilidža | Lipe | 10 | 675.600 | 67.600 | B |
| 8a1ef4590a9ffff | Novo Sarajevo | Čengić Vila II | 200 | 13,522.000 | 67.600 | B |
| 8a1ef459038ffff | Novi Grad Sarajevo | Aneks | 65 | 4,400.100 | 67.700 | A |
| 8a1ef459602ffff | Novi Grad Sarajevo | Briješće | 136 | 9,214.500 | 67.800 | A |
| 8a1ef459c017fff | Stari Grad Sarajevo | Širokača | 47 | 3,186.000 | 67.800 | A |
| 8a1ef45b0457fff | Vogošća | Vogošća | 283 | 19,196.900 | 67.800 | B |
| 8a1ea925bd67fff | Vogošća | Gora | 101 | 6,851.900 | 67.800 | B |
| 8a1ef4590227fff | Novi Grad Sarajevo | Staro Hrasno | 298 | 20,239.800 | 67.900 | A |
| 8a1ea92c9627fff | Novi Grad Sarajevo | Briješće | 115 | 7,813.200 | 67.900 | A |
| 8a1ef459289ffff | Novi Grad Sarajevo | Dobrinja A | 472 | 32,079.500 | 68.000 | A |
| 8a1ef4583c0ffff | Stari Grad Sarajevo | Sedrenik | 54 | 3,675.300 | 68.100 | A |
| 8a1ef45839b7fff | Stari Grad Sarajevo | Sedrenik | 13 | 885.000 | 68.100 | A |
| 8a1ef4592c57fff | Novi Grad Sarajevo | Dobrinja A | 227 | 15,455.500 | 68.100 | A |
| 8a1ef459c567fff | Stari Grad Sarajevo | Širokača | 29 | 1,975.400 | 68.100 | A |
| 8a1ef4590117fff | Novi Grad Sarajevo | Alipašin Most III | 595 | 40,566.100 | 68.200 | A |
| 8a1ef4582177fff | Centar Sarajevo | Park-Višnjik | 65 | 4,434.400 | 68.200 | B |
| 8a1ea92c9707fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 31 | 2,114.900 | 68.200 | A |
| 8a1ef459575ffff | Novo Sarajevo | Pofalići I | 69 | 4,708.000 | 68.200 | B |
| 8a1ef458218ffff | Centar Sarajevo | Park-Višnjik | 67 | 4,571.600 | 68.200 | B |
| 8a1ef459055ffff | Novi Grad Sarajevo | Švrakino Selo I | 39 | 2,663.900 | 68.300 | A |
| 8a1ef4590d0ffff | Novi Grad Sarajevo | Alipašin Most II | 76 | 5,192.900 | 68.300 | A |
| 8a1ef4590887fff | Novi Grad Sarajevo | Alipašin Most II | 82 | 5,607.000 | 68.400 | A |
| 8a1ef45900c7fff | Novi Grad Sarajevo | Aneks | 240 | 16,419.500 | 68.400 | A |
| 8a1ea92cd74ffff | Novi Grad Sarajevo | Zabrđe | 11 | 753.200 | 68.500 | A |
| 8a1ef45960e7fff | Novi Grad Sarajevo | Briješće | 66 | 4,519.300 | 68.500 | A |
| 8a1ef459078ffff | Novi Grad Sarajevo | Švrakino Selo I | 87 | 5,965.300 | 68.600 | A |
| 8a1ef4595b77fff | Centar Sarajevo | Šip | 21 | 1,440.100 | 68.600 | B |
| 8a1ef459c35ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 15 | 1,028.800 | 68.600 | A |
| 8a1ea92e9387fff | Vogošća | Semizovac | 105 | 7,202.700 | 68.600 | B |
| 8a1ef45826e7fff | Centar Sarajevo | Trg oslobođenja-Centar | 75 | 5,145.900 | 68.600 | B |
| 8a1ef459150ffff | Novo Sarajevo | Grbavica II | 215 | 14,758.400 | 68.600 | B |
| 8a1ef4590367fff | Novo Sarajevo | Hrasno | 223 | 15,320.300 | 68.700 | B |
| 8a1ef45b612ffff | Vogošća | Krivoglavci | 12 | 824.400 | 68.700 | B |
| 8a1ef459c127fff | Stari Grad Sarajevo | Širokača | 86 | 5,908.500 | 68.700 | A |
| 8a1ea92c9417fff | Novi Grad Sarajevo | Briješće | 277 | 19,037.700 | 68.700 | A |
| 8a1ef459154ffff | Novo Sarajevo | Vraca | 195 | 13,404.800 | 68.700 | B |
| 8a1ea92c91affff | Novi Grad Sarajevo | Naselje heroja Sokolje | 51 | 3,506.200 | 68.700 | A |
| 8a1ef4591d27fff | Novo Sarajevo | Pofalići II | 309 | 21,260.700 | 68.800 | B |
| 8a1ef45860b7fff | Vogošća | Kobilja Glava | 16 | 1,101.000 | 68.800 | B |
| 8a1ef4594c9ffff | Novi Grad Sarajevo | Briješće | 17 | 1,169.800 | 68.800 | A |
| 8a1ef4590daffff | Novi Grad Sarajevo | Alipašin Most I | 32 | 2,204.100 | 68.900 | A |
| 8a1ef4591d87fff | Novo Sarajevo | Malta | 49 | 3,376.400 | 68.900 | B |
| 8a1ef4582d67fff | Centar Sarajevo | Koševsko Brdo | 44 | 3,032.600 | 68.900 | B |
| 8a1ea92cbb57fff | Novi Grad Sarajevo | Briješće | 13 | 896.300 | 68.900 | A |
| 8a1ea92c9977fff | Novi Grad Sarajevo | Zabrđe | 21 | 1,448.900 | 69.000 | A |
| 8a1ef459c0cffff | Stari Grad Sarajevo | Toka-Džeka | 43 | 2,967.800 | 69.000 | A |
| 8a1ef45b4ce7fff | Vogošća | Semizovac | 10 | 690.700 | 69.100 | B |
| 8a1ef459664ffff | Novi Grad Sarajevo | Saraj Polje | 451 | 31,162.300 | 69.100 | A |
| 8a1ef459cb37fff | Stari Grad Sarajevo | Bistrik | 153 | 10,572.200 | 69.100 | A |
| 8a1ea92c318ffff | Ilidža | Gladno polje | 15 | 1,036.600 | 69.100 | B |
| 8a1ef459c8dffff | Stari Grad Sarajevo | Bistrik | 107 | 7,394.600 | 69.100 | A |
| 8a1ef4596047fff | Novi Grad Sarajevo | Saraj Polje | 107 | 7,401.300 | 69.200 | A |
| 8a1ef459604ffff | Novi Grad Sarajevo | Saraj Polje | 250 | 17,302.100 | 69.200 | A |
| 8a1ef4582687fff | Centar Sarajevo | Marijin Dvor | 98 | 6,790.500 | 69.300 | B |
| 8a1ef458341ffff | Stari Grad Sarajevo | Kovači | 62 | 4,297.400 | 69.300 | A |
| 8a1ef459cb8ffff | Stari Grad Sarajevo | Bistrik | 126 | 8,735.100 | 69.300 | A |
| 8a1ef4583cb7fff | Stari Grad Sarajevo | Medrese | 97 | 6,725.800 | 69.300 | A |
| 8a1ef459dd8ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 17 | 1,179.300 | 69.400 | A |
| 8a1ef45b644ffff | Vogošća | Krivoglavci | 12 | 833.500 | 69.500 | B |
| 8a1ef458689ffff | Vogošća | Kobilja Glava | 14 | 972.600 | 69.500 | B |
| 8a1ef4582477fff | Centar Sarajevo | Ciglane | 63 | 4,385.800 | 69.600 | B |
| 8a1ef4582d4ffff | Centar Sarajevo | Koševsko Brdo | 48 | 3,343.700 | 69.700 | B |
| 8a1ef4583d9ffff | Stari Grad Sarajevo | Sedrenik | 74 | 5,156.000 | 69.700 | A |
| 8a1ef4590c57fff | Novi Grad Sarajevo | Alipašin Most III | 543 | 37,836.500 | 69.700 | A |
| 8a1ea92c998ffff | Novi Grad Sarajevo | Zabrđe | 11 | 766.500 | 69.700 | A |
| 8a1ef4595407fff | Novi Grad Sarajevo | Dolac | 15 | 1,045.300 | 69.700 | A |
| 8a1ea92c8cc7fff | Novi Grad Sarajevo | Dobroševići | 13 | 906.600 | 69.700 | A |
| 8a1ea925b997fff | Vogošća | Gora | 60 | 4,185.100 | 69.800 | B |
| 8a1ef4592a67fff | Novi Grad Sarajevo | Švrakino Selo II | 12 | 837.500 | 69.800 | A |
| 8a1ef45b2507fff | Novi Grad Sarajevo | Zabrđe | 27 | 1,886.300 | 69.900 | A |
| 8a1ef4592897fff | Novi Grad Sarajevo | Dobrinja A | 510 | 35,642.300 | 69.900 | A |
| 8a1ef459ca6ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 20 | 1,398.300 | 69.900 | A |
| 8a1ef4596447fff | Ilidža | Stup | 44 | 3,076.600 | 69.900 | B |
| 8a1ea92ce687fff | Ilidža | Lipe | 13 | 909.500 | 70.000 | B |
| 8a1ef45b2587fff | Novi Grad Sarajevo | Zabrđe | 11 | 769.700 | 70.000 | A |
| 8a1ef4591017fff | Novo Sarajevo | Grbavica I | 314 | 21,982.300 | 70.000 | B |
| 8a1ef4596767fff | Ilidža | Stupsko Brdo | 24 | 1,681.500 | 70.100 | B |
| 8a1ef459dcaffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 12 | 840.900 | 70.100 | A |
| 8a1ef459214ffff | Novi Grad Sarajevo | Dobrinja C | 85 | 5,958.300 | 70.100 | A |
| 8a1ef4591a8ffff | Novo Sarajevo | Kovačići | 332 | 23,279.700 | 70.100 | B |
| 8a1ef459c117fff | Stari Grad Sarajevo | Širokača | 86 | 6,030.500 | 70.100 | A |
| 8a1ef6965c17fff | Ilidža | Lužani | 25 | 1,754.600 | 70.200 | B |
| 8a1ef4583577fff | Stari Grad Sarajevo | Medrese | 77 | 5,408.100 | 70.200 | A |
| 8a1ef459cb97fff | Stari Grad Sarajevo | Bistrik | 143 | 10,065.700 | 70.400 | A |
| 8a1ea925bc27fff | Vogošća | Gora | 12 | 845.000 | 70.400 | B |
| 8a1ef459605ffff | Novi Grad Sarajevo | Saraj Polje | 47 | 3,309.600 | 70.400 | A |
| 8a1ef4595257fff | Novo Sarajevo | Velešići | 125 | 8,804.800 | 70.400 | B |
| 8a1ef4583187fff | Stari Grad Sarajevo | Sedrenik | 28 | 1,972.500 | 70.400 | A |
| 8a1ea925bdaffff | Vogošća | Gora | 16 | 1,128.600 | 70.500 | B |
| 8a1ef45928b7fff | Novi Grad Sarajevo | Dobrinja A | 430 | 30,342.900 | 70.600 | A |
| 8a1ef459666ffff | Novi Grad Sarajevo | Saraj Polje | 546 | 38,536.600 | 70.600 | A |
| 8a1ef4596a0ffff | Novi Grad Sarajevo | Alipašin Most I | 35 | 2,470.500 | 70.600 | A |
| 8a1ef459606ffff | Novi Grad Sarajevo | Saraj Polje | 39 | 2,753.700 | 70.600 | A |
| 8a1ef45b376ffff | Vogošća | Grahovište | 31 | 2,189.000 | 70.600 | B |
| 8a1ef45b419ffff | Vogošća | Ljubina-Poturovići | 21 | 1,484.000 | 70.700 | B |
| 8a1ea92ccb1ffff | Novi Grad Sarajevo | Dobroševići | 10 | 706.700 | 70.700 | A |
| 8a1ef4591da7fff | Novo Sarajevo | Malta | 369 | 26,079.300 | 70.700 | B |
| 8a1ef4596297fff | Novi Grad Sarajevo | Saraj Polje | 553 | 39,097.600 | 70.700 | A |
| 8a1ef4583cc7fff | Stari Grad Sarajevo | Medrese | 79 | 5,601.100 | 70.900 | A |
| 8a1ef45b299ffff | Vogošća | Vogošća | 26 | 1,843.900 | 70.900 | B |
| 8a1ef4592567fff | Novi Grad Sarajevo | Dobrinja B | 240 | 17,038.400 | 71.000 | A |
| 8a1ef4583017fff | Stari Grad Sarajevo | Mošćanica | 20 | 1,420.200 | 71.000 | A |
| 8a1ef45946c7fff | Novi Grad Sarajevo | Alipašin Most II | 92 | 6,544.400 | 71.100 | A |
| 8a1ef4591a1ffff | Centar Sarajevo | Marijin Dvor | 73 | 5,194.800 | 71.200 | B |
| 8a1ea92c811ffff | Novi Grad Sarajevo | Dobroševići | 25 | 1,780.100 | 71.200 | A |
| 8a1ef4583c37fff | Stari Grad Sarajevo | Sedrenik | 61 | 4,344.700 | 71.200 | A |
| 8a1ef4596a37fff | Novi Grad Sarajevo | Alipašin Most I | 35 | 2,496.100 | 71.300 | A |
| 8a1ea92c9a9ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 13 | 928.000 | 71.400 | A |
| 8a1ef459c24ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 11 | 785.800 | 71.400 | A |
| 8a1ef45b41b7fff | Vogošća | Ljubina-Poturovići | 15 | 1,071.900 | 71.500 | B |
| 8a1ef45952cffff | Novo Sarajevo | Pofalići I | 32 | 2,287.100 | 71.500 | B |
| 8a1ef45b1427fff | Vogošća | Hotonj | 20 | 1,429.700 | 71.500 | B |
| 8a1ea92c8167fff | Novi Grad Sarajevo | Dobroševići | 17 | 1,215.300 | 71.500 | A |
| 8a1ea92dda4ffff | Ilidža | Lipe | 18 | 1,287.200 | 71.500 | B |
| 8a1ef4590707fff | Novi Grad Sarajevo | Švrakino Selo I | 98 | 7,009.800 | 71.500 | A |
| 8a1ea925a407fff | Vogošća | Nebočaj | 14 | 1,001.600 | 71.500 | B |
| 8a1ef45939b7fff | Novo Sarajevo | Hrasno Brdo | 15 | 1,073.700 | 71.600 | B |
| 8a1ea92d982ffff | Ilidža | Blažuj | 10 | 716.800 | 71.700 | B |
| 8a1ef4596037fff | Novi Grad Sarajevo | Briješće | 64 | 4,588.200 | 71.700 | A |
| 8a1ef45b00d7fff | Vogošća | Vogošća | 183 | 13,120.600 | 71.700 | B |
| 8a1ef458648ffff | Centar Sarajevo | Šip | 16 | 1,148.900 | 71.800 | B |
| 8a1ef4592c27fff | Novi Grad Sarajevo | Dobrinja A | 107 | 7,685.400 | 71.800 | A |
| 8a1ea92ccb37fff | Novi Grad Sarajevo | Dobroševići | 15 | 1,077.500 | 71.800 | A |
| 8a1ef4594717fff | Novi Grad Sarajevo | Alipašin Most I | 24 | 1,724.500 | 71.900 | A |
| 8a1ef4583ccffff | Stari Grad Sarajevo | Sumbuluša | 66 | 4,743.900 | 71.900 | A |
| 8a1ef4594737fff | Novi Grad Sarajevo | Alipašin Most I | 20 | 1,437.600 | 71.900 | A |
| 8a1ef45b4d37fff | Vogošća | Nebočaj | 17 | 1,222.300 | 71.900 | B |
| 8a1ef45b1c97fff | Vogošća | Blagovac | 23 | 1,654.300 | 71.900 | B |
| 8a1ef4596c4ffff | Novi Grad Sarajevo | Briješće | 53 | 3,812.800 | 71.900 | A |
| 8a1ea92cc0e7fff | Novi Grad Sarajevo | Dobroševići | 11 | 791.600 | 72.000 | A |
| 8a1ef4583567fff | Stari Grad Sarajevo | Sumbuluša | 63 | 4,536.600 | 72.000 | A |
| 8a1ef459c047fff | Stari Grad Sarajevo | Toka-Džeka | 80 | 5,761.500 | 72.000 | A |
| 8a1ef4592b77fff | Novi Grad Sarajevo | Švrakino Selo II | 19 | 1,368.500 | 72.000 | A |
| 8a1ea925b4d7fff | Vogošća | Garež | 20 | 1,442.900 | 72.100 | B |
| 8a1ea92cd427fff | Novi Grad Sarajevo | Dobroševići | 36 | 2,598.600 | 72.200 | A |
| 8a1ef458226ffff | Stari Grad Sarajevo | Logavina | 113 | 8,165.100 | 72.300 | A |
| 8a1ef45910cffff | Novo Sarajevo | Gornji Kovačići | 46 | 3,324.700 | 72.300 | B |
| 8a1ef4583c9ffff | Stari Grad Sarajevo | Medrese | 118 | 8,529.700 | 72.300 | A |
| 8a1ef45821affff | Centar Sarajevo | Ciglane | 93 | 6,729.200 | 72.400 | B |
| 8a1ef459c0e7fff | Stari Grad Sarajevo | Toka-Džeka | 50 | 3,619.400 | 72.400 | A |
| 8a1ef45b1c5ffff | Vogošća | Vogošća | 111 | 8,039.300 | 72.400 | B |
| 8a1ef4591557fff | Novo Sarajevo | Grbavica II | 106 | 7,679.400 | 72.400 | B |
| 8a1ea92ce6c7fff | Ilidža | Lipe | 14 | 1,014.300 | 72.400 | B |
| 8a1ea92cc8e7fff | Novi Grad Sarajevo | Dobroševići | 11 | 797.400 | 72.500 | A |
| 8a1ea92ca7a7fff | Ilidža | Blažuj | 16 | 1,160.300 | 72.500 | B |
| 8a1ef6965967fff | Ilidža | Naselje Bulevar | 34 | 2,465.700 | 72.500 | B |
| 8a1ea92ea6cffff | Novi Grad Sarajevo | Dobroševići | 13 | 942.800 | 72.500 | A |
| 8a1ef459ccb7fff | Centar Sarajevo | Soukbunar | 45 | 3,264.500 | 72.500 | B |
| 8a1ea92e9a9ffff | Vogošća | Nebočaj | 11 | 798.000 | 72.500 | B |
| 8a1ef45b3d47fff | Vogošća | Ugorsko | 13 | 943.100 | 72.500 | B |
| 8a1ef4595037fff | Novo Sarajevo | Pofalići II | 12 | 870.600 | 72.600 | B |
| 8a1ef4596c87fff | Novi Grad Sarajevo | Briješće | 30 | 2,177.900 | 72.600 | A |
| 8a1ef6965a77fff | Novi Grad Sarajevo | Saraj Polje | 12 | 871.800 | 72.600 | A |
| 8a1ea925bcf7fff | Vogošća | Gora | 14 | 1,017.400 | 72.700 | B |
| 8a1ef459cc17fff | Centar Sarajevo | Soukbunar | 51 | 3,706.700 | 72.700 | B |
| 8a1ef458236ffff | Stari Grad Sarajevo | Sedrenik | 82 | 5,960.800 | 72.700 | A |
| 8a1ea92cc607fff | Novi Grad Sarajevo | Dobroševići | 13 | 945.700 | 72.700 | A |
| 8a1ea92ca697fff | Ilidža | Plandište | 24 | 1,746.100 | 72.800 | B |
| 8a1ef4586447fff | Centar Sarajevo | Šip | 34 | 2,475.000 | 72.800 | B |
| 8a1ef45824e7fff | Centar Sarajevo | Koševsko Brdo | 59 | 4,295.200 | 72.800 | B |
| 8a1ef459cb27fff | Stari Grad Sarajevo | Kovači | 63 | 4,588.700 | 72.800 | A |
| 8a1ef4591267fff | Centar Sarajevo | Soukbunar | 29 | 2,113.100 | 72.900 | B |
| 8a1ea92c9577fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 22 | 1,604.300 | 72.900 | A |
| 8a1ef459002ffff | Novi Grad Sarajevo | Alipašin Most III | 363 | 26,476.300 | 72.900 | A |
| 8a1ef45b2857fff | Vogošća | Vogošća | 10 | 729.400 | 72.900 | B |
| 8a1ea92c8537fff | Novi Grad Sarajevo | Dobroševići | 17 | 1,240.200 | 73.000 | A |
| 8a1ef459dd9ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 30 | 2,192.000 | 73.100 | A |
| 8a1ea92cc8a7fff | Novi Grad Sarajevo | Dobroševići | 19 | 1,388.500 | 73.100 | A |
| 8a1ef45b178ffff | Vogošća | Hotonj | 154 | 11,256.400 | 73.100 | B |
| 8a1ef458644ffff | Centar Sarajevo | Šip | 38 | 2,778.700 | 73.100 | B |
| 8a1ef6965d8ffff | Ilidža | Lužani | 37 | 2,706.100 | 73.100 | B |
| 8a1ef45b44affff | Vogošća | Semizovac | 66 | 4,829.100 | 73.200 | B |
| 8a1ef4582117fff | Centar Sarajevo | Koševsko Brdo | 107 | 7,837.000 | 73.200 | B |
| 8a1ef4583caffff | Stari Grad Sarajevo | Medrese | 98 | 7,179.200 | 73.300 | A |
| 8a1ef4582827fff | Centar Sarajevo | Betanija | 36 | 2,637.400 | 73.300 | B |
| 8a1ef4590787fff | Novi Grad Sarajevo | Švrakino Selo I | 62 | 4,542.700 | 73.300 | A |
| 8a1ea92c8b97fff | Novi Grad Sarajevo | Dobroševići | 62 | 4,546.300 | 73.300 | A |
| 8a1ea92c8c07fff | Novi Grad Sarajevo | Dobroševići | 32 | 2,347.600 | 73.400 | A |
| 8a1ef4583507fff | Stari Grad Sarajevo | Medrese | 129 | 9,481.100 | 73.500 | A |
| 8a1ea92cca37fff | Novi Grad Sarajevo | Dobroševići | 13 | 955.600 | 73.500 | A |
| 8a1ea92c8b87fff | Novi Grad Sarajevo | Dobroševići | 41 | 3,014.500 | 73.500 | A |
| 8a1ef4592577fff | Novi Grad Sarajevo | Dobrinja B | 54 | 3,971.100 | 73.500 | A |
| 8a1ea92c9027fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 10 | 735.400 | 73.500 | A |
| 8a1ea92c548ffff | Ilidža | Rakovica | 10 | 735.700 | 73.600 | B |
| 8a1ef4586c27fff | Vogošća | Kobilja Glava | 15 | 1,103.600 | 73.600 | B |
| 8a1ef696536ffff | Ilidža | Stupsko Brdo | 21 | 1,545.400 | 73.600 | B |
| 8a1ea92ea2cffff | Novi Grad Sarajevo | Dobroševići | 15 | 1,103.900 | 73.600 | A |
| 8a1ef45832b7fff | Stari Grad Sarajevo | Mošćanica | 15 | 1,104.000 | 73.600 | A |
| 8a1ef4595707fff | Novo Sarajevo | Pofalići II | 176 | 12,956.400 | 73.600 | B |
| 8a1ef4582b6ffff | Centar Sarajevo | Hrastovi-Mrkovići | 22 | 1,620.100 | 73.600 | B |
| 8a1ea92c9bb7fff | Novi Grad Sarajevo | Zabrđe | 44 | 3,242.300 | 73.700 | A |
| 8a1ef459c107fff | Stari Grad Sarajevo | Širokača | 87 | 6,413.100 | 73.700 | A |
| 8a1ef459572ffff | Novo Sarajevo | Pofalići II | 207 | 15,269.000 | 73.800 | B |
| 8a1ef4583ca7fff | Stari Grad Sarajevo | Medrese | 87 | 6,420.000 | 73.800 | A |
| 8a1ea92c8d27fff | Novi Grad Sarajevo | Dobroševići | 43 | 3,173.300 | 73.800 | A |
| 8a1ef45b3c07fff | Vogošća | Ugorsko | 10 | 738.200 | 73.800 | B |
| 8a1ef4596187fff | Novi Grad Sarajevo | Briješće | 71 | 5,242.200 | 73.800 | A |
| 8a1ef45b258ffff | Novi Grad Sarajevo | Zabrđe | 10 | 738.400 | 73.800 | A |
| 8a1ef4596ae7fff | Novi Grad Sarajevo | Alipašin Most I | 43 | 3,175.300 | 73.800 | A |
| 8a1ea92cca27fff | Novi Grad Sarajevo | Dobroševići | 15 | 1,107.900 | 73.900 | A |
| 8a1ef4591717fff | Novo Sarajevo | Vraca | 16 | 1,182.000 | 73.900 | B |
| 8a1ef45914f7fff | Novo Sarajevo | Vraca | 10 | 739.300 | 73.900 | B |
| 8a1ea92cc817fff | Novi Grad Sarajevo | Dobroševići | 10 | 739.500 | 74.000 | A |
| 8a1ea92dd36ffff | Ilidža | Lipe | 30 | 2,219.400 | 74.000 | B |
| 8a1ef45b1ca7fff | Vogošća | Blagovac | 12 | 888.300 | 74.000 | B |
| 8a1ef459074ffff | Novi Grad Sarajevo | Aneks | 78 | 5,776.800 | 74.100 | A |
| 8a1ef45961a7fff | Novi Grad Sarajevo | Briješće | 99 | 7,335.700 | 74.100 | A |
| 8a1ef459dca7fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 16 | 1,185.900 | 74.100 | A |
| 8a1ea92c30affff | Ilidža | Gladno polje | 17 | 1,260.100 | 74.100 | B |
| 8a1ef4591347fff | Centar Sarajevo | Soukbunar | 38 | 2,819.000 | 74.200 | B |
| 8a1ef459569ffff | Novo Sarajevo | Pofalići II | 180 | 13,358.600 | 74.200 | B |
| 8a1ea92c8daffff | Novi Grad Sarajevo | Dobroševići | 25 | 1,855.700 | 74.200 | A |
| 8a1ea92c3987fff | Ilidža | Kakrinje | 16 | 1,187.800 | 74.200 | B |
| 8a1ef45b071ffff | Vogošća | Vogošća | 355 | 26,354.500 | 74.200 | B |
| 8a1ef4592db7fff | Novi Grad Sarajevo | Dobrinja A | 130 | 9,655.700 | 74.300 | A |
| 8a1ef4592327fff | Novi Grad Sarajevo | Dobrinja C | 24 | 1,784.700 | 74.400 | A |
| 8a1ef696178ffff | Ilidža | Lasica | 10 | 744.400 | 74.400 | B |
| 8a1ef459072ffff | Novi Grad Sarajevo | Švrakino Selo III | 63 | 4,689.600 | 74.400 | A |
| 8a1ef45914e7fff | Novo Sarajevo | Vraca | 20 | 1,488.800 | 74.400 | B |
| 8a1ea92c901ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 142 | 10,571.300 | 74.400 | A |
| 8a1ef458352ffff | Stari Grad Sarajevo | Medrese | 100 | 7,445.600 | 74.500 | A |
| 8a1ef4582367fff | Centar Sarajevo | Bardakčije | 52 | 3,872.400 | 74.500 | B |
| 8a1ea92c894ffff | Novi Grad Sarajevo | Dobroševići | 15 | 1,117.100 | 74.500 | A |
| 8a1ea92c33affff | Ilidža | Gladno polje | 32 | 2,383.200 | 74.500 | B |
| 8a1ef4596577fff | Ilidža | Stup | 40 | 2,979.800 | 74.500 | B |
| 8a1ef459064ffff | Novi Grad Sarajevo | Aneks | 50 | 3,725.100 | 74.500 | A |
| 8a1ea92cc187fff | Novi Grad Sarajevo | Dobroševići | 21 | 1,565.700 | 74.600 | A |
| 8a1ef45966dffff | Novi Grad Sarajevo | Saraj Polje | 19 | 1,418.100 | 74.600 | A |
| 8a1ef45b3957fff | Vogošća | Hotonj | 21 | 1,567.400 | 74.600 | B |
| 8a1ef4583047fff | Stari Grad Sarajevo | Mošćanica | 16 | 1,194.300 | 74.600 | A |
| 8a1ef459c8d7fff | Stari Grad Sarajevo | Širokača | 90 | 6,721.200 | 74.700 | A |
| 8a1ef45902b7fff | Novi Grad Sarajevo | Aneks | 93 | 6,945.900 | 74.700 | A |
| 8a1ef458620ffff | Centar Sarajevo | Betanija | 14 | 1,045.700 | 74.700 | B |
| 8a1ef4583a1ffff | Stari Grad Sarajevo | Mošćanica | 13 | 971.100 | 74.700 | A |
| 8a1ef459012ffff | Novi Grad Sarajevo | Alipašin Most III | 55 | 4,108.700 | 74.700 | A |
| 8a1ef4596a07fff | Novi Grad Sarajevo | Alipašin Most I | 55 | 4,109.000 | 74.700 | A |
| 8a1ef4591aeffff | Centar Sarajevo | Skenderija-Podtekija | 54 | 4,034.600 | 74.700 | B |
| 8a1ea92ce677fff | Ilidža | Lipe | 15 | 1,120.900 | 74.700 | B |
| 8a1ef45b148ffff | Vogošća | Hotonj | 175 | 13,078.500 | 74.700 | B |
| 8a1ef459071ffff | Novi Grad Sarajevo | Švrakino Selo III | 58 | 4,334.800 | 74.700 | A |
| 8a1ef6961327fff | Ilidža | Donji Kotorac | 49 | 3,662.500 | 74.700 | B |
| 8a1ef45904e7fff | Novi Grad Sarajevo | Švrakino Selo II | 34 | 2,541.500 | 74.800 | A |
| 8a1ef6966967fff | Ilidža | Vrelo Bosne | 13 | 971.800 | 74.800 | B |
| 8a1ef45b00c7fff | Vogošća | Vogošća | 86 | 6,429.100 | 74.800 | B |
| 8a1ea92cc10ffff | Novi Grad Sarajevo | Dobroševići | 12 | 897.800 | 74.800 | A |
| 8a1ef458252ffff | Novo Sarajevo | Velešići | 72 | 5,387.800 | 74.800 | B |
| 8a1ef45919a7fff | Novo Sarajevo | Pofalići I | 24 | 1,796.600 | 74.900 | B |
| 8a1ea92c3007fff | Ilidža | Gladno polje | 39 | 2,921.200 | 74.900 | B |
| 8a1ef4582b8ffff | Centar Sarajevo | Breka | 50 | 3,747.600 | 75.000 | B |
| 8a1ef4583787fff | Stari Grad Sarajevo | Vratnik | 94 | 7,046.100 | 75.000 | A |
| 8a1ea92c8027fff | Ilidža | Dolovi | 11 | 824.800 | 75.000 | B |
| 8a1ef459080ffff | Novi Grad Sarajevo | Buća Potok | 54 | 4,054.900 | 75.100 | A |
| 8a1ef4582cb7fff | Novo Sarajevo | Gornji Velešići | 157 | 11,791.300 | 75.100 | B |
| 8a1ef4590487fff | Novi Grad Sarajevo | Švrakino Selo II | 36 | 2,706.200 | 75.200 | A |
| 8a1ea92cb597fff | Ilidža | Kamenjača | 13 | 977.600 | 75.200 | B |
| 8a1ea92ce75ffff | Ilidža | Lipe | 11 | 827.300 | 75.200 | B |
| 8a1ef6965407fff | Ilidža | Ilidža | 133 | 10,006.400 | 75.200 | B |
| 8a1ef4596a77fff | Novi Grad Sarajevo | Alipašin Most I | 54 | 4,063.100 | 75.200 | A |
| 8a1ef459ca67fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 38 | 2,862.500 | 75.300 | A |
| 8a1ef45946affff | Novi Grad Sarajevo | Alipašin Most I | 38 | 2,862.800 | 75.300 | A |
| 8a1ea92ceb27fff | Ilidža | Vlakovo | 12 | 904.100 | 75.300 | B |
| 8a1ef45839a7fff | Stari Grad Sarajevo | Sedrenik | 12 | 904.600 | 75.400 | A |
| 8a1ef458208ffff | Centar Sarajevo | Park-Višnjik | 66 | 4,975.700 | 75.400 | B |
| 8a1ef4591337fff | Novo Sarajevo | Gornji Kovačići | 32 | 2,415.600 | 75.500 | B |
| 8a1ef458271ffff | Centar Sarajevo | Džidžikovac-Koševo I | 76 | 5,737.800 | 75.500 | B |
| 8a1ea92c9857fff | Novi Grad Sarajevo | Zabrđe | 56 | 4,228.900 | 75.500 | A |
| 8a1ef45961affff | Novi Grad Sarajevo | Briješće | 74 | 5,589.700 | 75.500 | A |
| 8a1ef4596a17fff | Novi Grad Sarajevo | Alipašin Most I | 49 | 3,701.400 | 75.500 | A |
| 8a1ef4586097fff | Vogošća | Kobilja Glava | 19 | 1,435.600 | 75.600 | B |
| 8a1ef4596b77fff | Novi Grad Sarajevo | Alipašin Most I | 14 | 1,058.800 | 75.600 | A |
| 8a1ef459c34ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 23 | 1,740.800 | 75.700 | A |
| 8a1ef696550ffff | Ilidža | Ilidža | 57 | 4,314.200 | 75.700 | B |
| 8a1ef458314ffff | Stari Grad Sarajevo | Mošćanica | 12 | 908.800 | 75.700 | A |
| 8a1ef45805affff | Centar Sarajevo | Pionirska Dolina | 32 | 2,423.500 | 75.700 | B |
| 8a1ea92ce027fff | Ilidža | Lipe | 21 | 1,590.900 | 75.800 | B |
| 8a1ef4583707fff | Stari Grad Sarajevo | Vratnik | 75 | 5,682.000 | 75.800 | A |
| 8a1ef459520ffff | Novo Sarajevo | Velešići | 29 | 2,197.800 | 75.800 | B |
| 8a1ef459052ffff | Novi Grad Sarajevo | Švrakino Selo II | 43 | 3,261.100 | 75.800 | A |
| 8a1ea92cd197fff | Novi Grad Sarajevo | Dobroševići | 19 | 1,441.600 | 75.900 | A |
| 8a1ef4592b27fff | Novi Grad Sarajevo | Švrakino Selo II | 23 | 1,745.100 | 75.900 | A |
| 8a1ea92c9c5ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 225 | 17,075.800 | 75.900 | A |
| 8a1ea92ca8e7fff | Ilidža | Dolovi | 16 | 1,214.800 | 75.900 | B |
| 8a1ea92ca40ffff | Ilidža | Blažuj | 39 | 2,963.600 | 76.000 | B |
| 8a1ea92ca68ffff | Ilidža | Plandište | 26 | 1,976.200 | 76.000 | B |
| 8a1ef4590987fff | Novi Grad Sarajevo | Buća Potok | 65 | 4,942.600 | 76.000 | A |
| 8a1ef458354ffff | Stari Grad Sarajevo | Sumbuluša | 71 | 5,399.100 | 76.000 | A |
| 8a1ef45b272ffff | Novi Grad Sarajevo | Zabrđe | 11 | 836.500 | 76.000 | A |
| 8a1ea92c129ffff | Ilidža | Gladno polje | 14 | 1,064.700 | 76.100 | B |
| 8a1ef459021ffff | Novi Grad Sarajevo | Staro Hrasno | 78 | 5,932.600 | 76.100 | A |
| 8a1ef45901affff | Novi Grad Sarajevo | Alipašin Most III | 744 | 56,641.700 | 76.100 | A |
| 8a1ea92ce2dffff | Ilidža | Dolovi | 11 | 837.700 | 76.200 | B |
| 8a1ef45b48c7fff | Vogošća | Semizovac | 82 | 6,244.800 | 76.200 | B |
| 8a1ef45944d7fff | Novi Grad Sarajevo | Alipašin Most I | 32 | 2,437.100 | 76.200 | A |
| 8a1ef4583c17fff | Stari Grad Sarajevo | Sedrenik | 69 | 5,256.200 | 76.200 | A |
| 8a1ea92ca127fff | Ilidža | Dolovi | 16 | 1,219.400 | 76.200 | B |
| 8a1ea92ca8effff | Ilidža | Dolovi | 17 | 1,295.900 | 76.200 | B |
| 8a1ef45b28f7fff | Vogošća | Vogošća | 17 | 1,296.000 | 76.200 | B |
| 8a1ef6960557fff | Ilidža | Stojčevac | 23 | 1,753.600 | 76.200 | B |
| 8a1ea925b567fff | Vogošća | Gora | 18 | 1,373.400 | 76.300 | B |
| 8a1ef459c187fff | Stari Grad Sarajevo | Širokača | 53 | 4,049.500 | 76.400 | A |
| 8a1ef6964b6ffff | Ilidža | Otes | 67 | 5,120.500 | 76.400 | B |
| 8a1ef459574ffff | Novo Sarajevo | Pofalići I | 175 | 13,374.700 | 76.400 | B |
| 8a1ef4592d57fff | Novi Grad Sarajevo | Saraj Polje | 143 | 10,933.200 | 76.500 | A |
| 8a1ef4583917fff | Stari Grad Sarajevo | Sedrenik | 11 | 841.100 | 76.500 | A |
| 8a1ea92c52affff | Ilidža | Zenik | 12 | 917.800 | 76.500 | B |
| 8a1ea92c985ffff | Novi Grad Sarajevo | Zabrđe | 69 | 5,278.700 | 76.500 | A |
| 8a1ef4592d67fff | Novi Grad Sarajevo | Saraj Polje | 70 | 5,357.700 | 76.500 | A |
| 8a1ef69650affff | Ilidža | Butmir | 65 | 4,978.300 | 76.600 | B |
| 8a1ef459656ffff | Ilidža | Stup | 129 | 9,882.700 | 76.600 | B |
| 8a1ea92c502ffff | Ilidža | Zenik | 12 | 919.700 | 76.600 | B |
| 8a1ef459ca77fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 60 | 4,598.700 | 76.600 | A |
| 8a1ef4582cd7fff | Novo Sarajevo | Velešići | 58 | 4,445.800 | 76.700 | B |
| 8a1ef4591ce7fff | Novo Sarajevo | Grbavica II | 104 | 7,976.600 | 76.700 | B |
| 8a1ef459cbaffff | Stari Grad Sarajevo | Bistrik | 155 | 11,889.100 | 76.700 | A |
| 8a1ef458058ffff | Centar Sarajevo | Pionirska Dolina | 34 | 2,608.100 | 76.700 | B |
| 8a1ef458679ffff | Centar Sarajevo | Šip | 38 | 2,915.800 | 76.700 | B |
| 8a1ef4590d17fff | Novi Grad Sarajevo | Alipašin Most I | 61 | 4,681.500 | 76.700 | A |
| 8a1ef459409ffff | Novi Grad Sarajevo | Alipašin Most I | 10 | 767.600 | 76.800 | A |
| 8a1ea92ca6affff | Ilidža | Plandište | 45 | 3,454.800 | 76.800 | B |
| 8a1ef4591567fff | Novo Sarajevo | Grbavica II | 40 | 3,071.300 | 76.800 | B |
| 8a1ea92d98e7fff | Ilidža | Blažuj | 17 | 1,305.600 | 76.800 | B |
| 8a1ef4583c1ffff | Stari Grad Sarajevo | Sedrenik | 70 | 5,376.500 | 76.800 | A |
| 8a1ea92c996ffff | Novi Grad Sarajevo | Zabrđe | 18 | 1,382.800 | 76.800 | A |
| 8a1ea92c0257fff | Ilidža | Kakrinje | 10 | 768.500 | 76.900 | B |
| 8a1ea92c9c0ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 104 | 7,998.300 | 76.900 | A |
| 8a1ef4592197fff | Novi Grad Sarajevo | Dobrinja B | 223 | 17,151.800 | 76.900 | A |
| 8a1ef6963b8ffff | Ilidža | Lasica | 66 | 5,077.000 | 76.900 | B |
| 8a1ea92c44affff | Ilidža | Buhotina | 11 | 846.200 | 76.900 | B |
| 8a1ea92cc0c7fff | Novi Grad Sarajevo | Dobroševići | 14 | 1,077.100 | 76.900 | A |
| 8a1ef45910dffff | Novo Sarajevo | Vraca | 23 | 1,769.700 | 76.900 | B |
| 8a1ea92c971ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 15 | 1,154.700 | 77.000 | A |
| 8a1ef6971a4ffff | Ilidža | Hrasnica | 16 | 1,231.700 | 77.000 | B |
| 8a1ef45b2597fff | Novi Grad Sarajevo | Zabrđe | 92 | 7,086.600 | 77.000 | A |
| 8a1ef6965da7fff | Ilidža | Pejton | 154 | 11,862.700 | 77.000 | B |
| 8a1ef4583987fff | Stari Grad Sarajevo | Sedrenik | 13 | 1,001.400 | 77.000 | A |
| 8a1ef4596647fff | Novi Grad Sarajevo | Saraj Polje | 205 | 15,794.700 | 77.000 | A |
| 8a1ef459c007fff | Stari Grad Sarajevo | Toka-Džeka | 61 | 4,703.600 | 77.100 | A |
| 8a1ef459066ffff | Novi Grad Sarajevo | Aneks | 89 | 6,864.800 | 77.100 | A |
| 8a1ef6965d57fff | Ilidža | Ilidža | 212 | 16,361.000 | 77.200 | B |
| 8a1ef6965ca7fff | Ilidža | Lužani | 163 | 12,585.800 | 77.200 | B |
| 8a1ef459088ffff | Novi Grad Sarajevo | Buća Potok | 59 | 4,555.900 | 77.200 | A |
| 8a1ef6965d87fff | Ilidža | Lužani | 98 | 7,572.300 | 77.300 | B |
| 8a1ef459ca07fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 85 | 6,568.900 | 77.300 | A |
| 8a1ef6965a4ffff | Novi Grad Sarajevo | Saraj Polje | 134 | 10,357.000 | 77.300 | A |
| 8a1ea92c9d5ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 74 | 5,725.500 | 77.400 | A |
| 8a1ef6960b37fff | Ilidža | Sokolović-kolonija | 18 | 1,393.100 | 77.400 | B |
| 8a1ea92ca017fff | Ilidža | Osjek | 27 | 2,090.100 | 77.400 | B |
| 8a1ef459244ffff | Ilidža | Stupsko Brdo | 54 | 4,181.400 | 77.400 | B |
| 8a1ef459029ffff | Novi Grad Sarajevo | Aneks | 102 | 7,899.700 | 77.400 | A |
| 8a1ef4583c87fff | Stari Grad Sarajevo | Medrese | 107 | 8,287.800 | 77.500 | A |
| 8a1ef459dda7fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 36 | 2,789.000 | 77.500 | A |
| 8a1ef4591447fff | Novo Sarajevo | Vraca | 28 | 2,169.500 | 77.500 | B |
| 8a1ef6965cf7fff | Ilidža | Ilidža | 24 | 1,859.600 | 77.500 | B |
| 8a1ea92caaa7fff | Ilidža | Bjelaće | 31 | 2,402.900 | 77.500 | B |
| 8a1ef6964367fff | Ilidža | Lužani | 143 | 11,085.900 | 77.500 | B |
| 8a1ef6964107fff | Ilidža | Plandište | 17 | 1,317.900 | 77.500 | B |
| 8a1ef696a6b7fff | Ilidža | Krupac | 10 | 775.700 | 77.600 | B |
| 8a1ef4596477fff | Ilidža | Stup | 206 | 15,983.600 | 77.600 | B |
| 8a1ef45944affff | Novi Grad Sarajevo | Alipašin Most I | 29 | 2,250.300 | 77.600 | A |
| 8a1ef4595687fff | Novo Sarajevo | Pofalići II | 36 | 2,793.700 | 77.600 | B |
| 8a1ef45964a7fff | Ilidža | Naselje Bulevar | 48 | 3,726.300 | 77.600 | B |
| 8a1ef4596667fff | Novi Grad Sarajevo | Saraj Polje | 344 | 26,707.200 | 77.600 | A |
| 8a1ea92c8137fff | Novi Grad Sarajevo | Dobroševići | 119 | 9,241.000 | 77.700 | A |
| 8a1ef459096ffff | Novi Grad Sarajevo | Dolac | 39 | 3,029.000 | 77.700 | A |
| 8a1ea92c578ffff | Ilidža | Zenik | 10 | 776.800 | 77.700 | B |
| 8a1ef4594747fff | Novi Grad Sarajevo | Alipašin Most I | 36 | 2,797.100 | 77.700 | A |
| 8a1ea92cbd57fff | Ilidža | Doglodi | 20 | 1,554.000 | 77.700 | B |
| 8a1ef458209ffff | Centar Sarajevo | Ciglane | 95 | 7,384.200 | 77.700 | B |
| 8a1ef4596a1ffff | Novi Grad Sarajevo | Alipašin Most I | 49 | 3,811.400 | 77.800 | A |
| 8a1ef696694ffff | Ilidža | Vrutci | 11 | 856.200 | 77.800 | B |
| 8a1ea92cb3affff | Ilidža | Azići | 105 | 8,175.600 | 77.900 | B |
| 8a1ef6965c27fff | Ilidža | Ilidža | 124 | 9,662.200 | 77.900 | B |
| 8a1ea92ce967fff | Ilidža | Lipe | 22 | 1,714.900 | 78.000 | B |
| 8a1ef459cb57fff | Stari Grad Sarajevo | Babića bašča | 108 | 8,418.800 | 78.000 | A |
| 8a1ea92c84a7fff | Ilidža | Dolovi | 27 | 2,106.400 | 78.000 | B |
| 8a1ef4594617fff | Novi Grad Sarajevo | Alipašin Most I | 44 | 3,433.800 | 78.000 | A |
| 8a1ef6963b87fff | Ilidža | Lasica | 149 | 11,635.400 | 78.100 | B |
| 8a1ef459654ffff | Ilidža | Stup | 284 | 22,179.100 | 78.100 | B |
| 8a1ef459611ffff | Novi Grad Sarajevo | Briješće | 29 | 2,264.900 | 78.100 | A |
| 8a1ef45834effff | Stari Grad Sarajevo | Vratnik | 111 | 8,672.400 | 78.100 | A |
| 8a1ea92dd06ffff | Ilidža | Lipe | 74 | 5,782.000 | 78.100 | B |
| 8a1ef459446ffff | Novi Grad Sarajevo | Alipašin Most I | 18 | 1,406.400 | 78.100 | A |
| 8a1ef4592d87fff | Novi Grad Sarajevo | Dobrinja A | 207 | 16,174.600 | 78.100 | A |
| 8a1ef459c80ffff | Stari Grad Sarajevo | Baščaršija | 91 | 7,112.000 | 78.200 | A |
| 8a1ef4596b57fff | Novi Grad Sarajevo | Alipašin Most I | 59 | 4,612.600 | 78.200 | A |
| 8a1ef6963327fff | Ilidža | Lasica | 77 | 6,022.600 | 78.200 | B |
| 8a1ef45b2cf7fff | Novi Grad Sarajevo | Reljevo | 11 | 860.400 | 78.200 | A |
| 8a1ef4590297fff | Novi Grad Sarajevo | Aneks | 118 | 9,231.400 | 78.200 | A |
| 8a1ef4596567fff | Ilidža | Stup | 164 | 12,831.300 | 78.200 | B |
| 8a1ef69642affff | Ilidža | Lužani | 45 | 3,521.300 | 78.300 | B |
| 8a1ef459cbb7fff | Stari Grad Sarajevo | Bistrik | 165 | 12,917.400 | 78.300 | A |
| 8a1ef696432ffff | Ilidža | Lužani | 58 | 4,541.400 | 78.300 | B |
| 8a1ef4590287fff | Novi Grad Sarajevo | Aneks | 115 | 9,007.400 | 78.300 | A |
| 8a1ea92c30f7fff | Ilidža | Gladno polje | 46 | 3,603.300 | 78.300 | B |
| 8a1ef45b019ffff | Vogošća | Vogošća | 247 | 19,350.000 | 78.300 | B |
| 8a1ea92c91b7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 155 | 12,144.000 | 78.300 | A |
| 8a1ef696a6a7fff | Ilidža | Krupac | 21 | 1,645.300 | 78.300 | B |
| 8a1ef459c99ffff | Centar Sarajevo | Trg oslobođenja-Centar | 65 | 5,093.500 | 78.400 | B |
| 8a1ef45b06e7fff | Vogošća | Uglješići | 59 | 4,623.600 | 78.400 | B |
| 8a1ef459cda7fff | Centar Sarajevo | Skenderija-Podtekija | 53 | 4,153.700 | 78.400 | B |
| 8a1ef696a79ffff | Ilidža | Krupac | 10 | 783.900 | 78.400 | B |
| 8a1ea92c9817fff | Novi Grad Sarajevo | Zabrđe | 13 | 1,019.200 | 78.400 | A |
| 8a1ef4582b2ffff | Centar Sarajevo | Hrastovi-Mrkovići | 33 | 2,587.500 | 78.400 | B |
| 8a1ea92ccd27fff | Ilidža | Vlakovo | 19 | 1,490.300 | 78.400 | B |
| 8a1ef45b3a07fff | Vogošća | Hotonj | 15 | 1,176.700 | 78.400 | B |
| 8a1ea92ce307fff | Ilidža | Dolovi | 18 | 1,412.200 | 78.500 | B |
| 8a1ef4593907fff | Novi Grad Sarajevo | Aneks | 83 | 6,512.300 | 78.500 | A |
| 8a1ef4592547fff | Novi Grad Sarajevo | Dobrinja B | 62 | 4,865.500 | 78.500 | A |
| 8a1ea92c280ffff | Ilidža | Rudnik | 30 | 2,354.400 | 78.500 | B |
| 8a1ea92ca437fff | Ilidža | Blažuj | 93 | 7,300.400 | 78.500 | B |
| 8a1ef4583997fff | Stari Grad Sarajevo | Sedrenik | 23 | 1,805.600 | 78.500 | A |
| 8a1ef4596b5ffff | Novi Grad Sarajevo | Alipašin Most I | 65 | 5,103.400 | 78.500 | A |
| 8a1ef696182ffff | Ilidža | Donji Kotorac | 10 | 785.200 | 78.500 | B |
| 8a1ef45944c7fff | Novi Grad Sarajevo | Alipašin Most I | 46 | 3,613.500 | 78.600 | A |
| 8a1ea92cea17fff | Ilidža | Dolovi | 15 | 1,178.400 | 78.600 | B |
| 8a1ef459524ffff | Novo Sarajevo | Velešići | 119 | 9,352.800 | 78.600 | B |
| 8a1ef69612b7fff | Ilidža | Donji Kotorac | 30 | 2,358.000 | 78.600 | B |
| 8a1ea92c858ffff | Ilidža | Dolovi | 14 | 1,100.600 | 78.600 | B |
| 8a1ef45b449ffff | Vogošća | Semizovac | 148 | 11,634.600 | 78.600 | B |
| 8a1ef4590d2ffff | Novi Grad Sarajevo | Alipašin Most I | 102 | 8,018.700 | 78.600 | A |
| 8a1ef696116ffff | Ilidža | Donji Kotorac | 170 | 13,369.000 | 78.600 | B |
| 8a1ef6964b4ffff | Ilidža | Pejton | 178 | 14,001.500 | 78.700 | B |
| 8a1ef45835a7fff | Stari Grad Sarajevo | Medrese | 149 | 11,721.400 | 78.700 | A |
| 8a1ea92c360ffff | Ilidža | Gladno polje | 19 | 1,494.700 | 78.700 | B |
| 8a1ef45b310ffff | Vogošća | Ugorsko | 17 | 1,337.500 | 78.700 | B |
| 8a1ef4594647fff | Novi Grad Sarajevo | Dolac | 119 | 9,366.000 | 78.700 | A |
| 8a1ea92dd24ffff | Ilidža | Blažuj | 96 | 7,555.800 | 78.700 | B |
| 8a1ef4594447fff | Novi Grad Sarajevo | Alipašin Most I | 39 | 3,069.600 | 78.700 | A |
| 8a1ef6965d97fff | Ilidža | Lužani | 325 | 25,582.000 | 78.700 | B |
| 8a1ea92c2aaffff | Ilidža | Rakovica | 15 | 1,180.700 | 78.700 | B |
| 8a1ef45820cffff | Centar Sarajevo | Park-Višnjik | 69 | 5,432.900 | 78.700 | B |
| 8a1ef4592c07fff | Novi Grad Sarajevo | Dobrinja A | 137 | 10,791.700 | 78.800 | A |
| 8a1ea92cd247fff | Novi Grad Sarajevo | Reljevo | 12 | 945.700 | 78.800 | A |
| 8a1ea92ca687fff | Ilidža | Plandište | 120 | 9,458.300 | 78.800 | B |
| 8a1ef6960807fff | Ilidža | Stojčevac | 10 | 788.500 | 78.900 | B |
| 8a1ea92dd917fff | Ilidža | Gladno polje | 138 | 10,889.700 | 78.900 | B |
| 8a1ef4582aeffff | Centar Sarajevo | Hrastovi-Mrkovići | 45 | 3,551.200 | 78.900 | B |
| 8a1ef6964a37fff | Ilidža | Vreoca | 83 | 6,551.300 | 78.900 | B |
| 8a1ef4591db7fff | Novo Sarajevo | Čengić Vila I | 46 | 3,631.300 | 78.900 | B |
| 8a1ea92cacb7fff | Ilidža | Lipe | 48 | 3,789.300 | 78.900 | B |
| 8a1ea92c948ffff | Novi Grad Sarajevo | Briješće | 19 | 1,500.100 | 79.000 | A |
| 8a1ef459641ffff | Ilidža | Naselje Bulevar | 297 | 23,451.500 | 79.000 | B |
| 8a1ef69613a7fff | Ilidža | Donji Kotorac | 165 | 13,029.800 | 79.000 | B |
| 8a1ef6965197fff | Ilidža | Ilidža | 259 | 20,456.800 | 79.000 | B |
| 8a1ea925b127fff | Vogošća | Gora | 12 | 948.100 | 79.000 | B |
| 8a1ea92ca137fff | Ilidža | Dolovi | 13 | 1,027.300 | 79.000 | B |
| 8a1ea92c3837fff | Ilidža | Kakrinje | 14 | 1,106.700 | 79.000 | B |
| 8a1ef4596a2ffff | Novi Grad Sarajevo | Alipašin Most I | 79 | 6,245.000 | 79.100 | A |
| 8a1ea92cb797fff | Ilidža | Otes | 245 | 19,372.700 | 79.100 | B |
| 8a1ef696542ffff | Ilidža | Ilidža | 259 | 20,484.000 | 79.100 | B |
| 8a1ef45834e7fff | Stari Grad Sarajevo | Vratnik | 89 | 7,041.400 | 79.100 | A |
| 8a1ea92cb237fff | Ilidža | Azići | 180 | 14,243.000 | 79.100 | B |
| 8a1ea92c965ffff | Novi Grad Sarajevo | Briješće | 162 | 12,820.200 | 79.100 | A |
| 8a1ef6960d8ffff | Ilidža | Stojčevac | 22 | 1,741.100 | 79.100 | B |
| 8a1ef4595797fff | Novo Sarajevo | Pofalići II | 33 | 2,611.900 | 79.100 | B |
| 8a1ea92ceb47fff | Ilidža | Vlakovo | 11 | 870.700 | 79.200 | B |
| 8a1ef4596707fff | Ilidža | Stupsko Brdo | 619 | 49,001.300 | 79.200 | B |
| 8a1ea92ce74ffff | Ilidža | Dolovi | 28 | 2,216.600 | 79.200 | B |
| 8a1ef459075ffff | Novi Grad Sarajevo | Švrakino Selo III | 69 | 5,462.900 | 79.200 | A |
| 8a1ef45964e7fff | Ilidža | Naselje Bulevar | 667 | 52,811.200 | 79.200 | B |
| 8a1ea92c0947fff | Ilidža | Rakovica | 17 | 1,346.000 | 79.200 | B |
| 8a1ef45964f7fff | Ilidža | Naselje Bulevar | 438 | 34,680.700 | 79.200 | B |
| 8a1ef45944dffff | Novi Grad Sarajevo | Alipašin Most I | 48 | 3,802.900 | 79.200 | A |
| 8a1ef4590d1ffff | Novi Grad Sarajevo | Alipašin Most I | 77 | 6,100.600 | 79.200 | A |
| 8a1ef459c027fff | Stari Grad Sarajevo | Toka-Džeka | 83 | 6,578.300 | 79.300 | A |
| 8a1ef45806cffff | Stari Grad Sarajevo | Sedrenik | 35 | 2,774.800 | 79.300 | A |
| 8a1ef459188ffff | Novo Sarajevo | Željeznička | 37 | 2,933.400 | 79.300 | B |
| 8a1ef4596b67fff | Novi Grad Sarajevo | Alipašin Most I | 57 | 4,520.200 | 79.300 | A |
| 8a1ef4583c27fff | Stari Grad Sarajevo | Sedrenik | 61 | 4,837.700 | 79.300 | A |
| 8a1ea92ce35ffff | Ilidža | Dolovi | 11 | 872.600 | 79.300 | B |
| 8a1ef45b620ffff | Vogošća | Vogošća | 24 | 1,904.000 | 79.300 | B |
| 8a1ef4594727fff | Novi Grad Sarajevo | Alipašin Most I | 29 | 2,300.900 | 79.300 | A |
| 8a1ef6940d07fff | Ilidža | Lasica | 22 | 1,745.900 | 79.400 | B |
| 8a1ef4593937fff | Novi Grad Sarajevo | Aneks | 79 | 6,269.700 | 79.400 | A |
| 8a1ef6960c57fff | Ilidža | Stojčevac | 18 | 1,428.700 | 79.400 | B |
| 8a1ef45832a7fff | Stari Grad Sarajevo | Mošćanica | 11 | 873.200 | 79.400 | A |
| 8a1ea92c30a7fff | Ilidža | Gladno polje | 19 | 1,508.300 | 79.400 | B |
| 8a1ef4582c67fff | Centar Sarajevo | Koševsko Brdo | 57 | 4,526.000 | 79.400 | B |
| 8a1ef4594697fff | Novi Grad Sarajevo | Alipašin Most I | 64 | 5,083.100 | 79.400 | A |
| 8a1ef4582d0ffff | Centar Sarajevo | Donji Velešići | 46 | 3,653.800 | 79.400 | B |
| 8a1ef4583457fff | Stari Grad Sarajevo | Vratnik | 124 | 9,851.400 | 79.400 | A |
| 8a1ef4594607fff | Novi Grad Sarajevo | Alipašin Most I | 43 | 3,417.300 | 79.500 | A |
| 8a1ef6963a17fff | Ilidža | Lasica | 245 | 19,473.000 | 79.500 | B |
| 8a1ef4592c8ffff | Novi Grad Sarajevo | Dobrinja A | 97 | 7,711.100 | 79.500 | A |
| 8a1ef4596a27fff | Novi Grad Sarajevo | Alipašin Most I | 74 | 5,883.400 | 79.500 | A |
| 8a1ef45908dffff | Novi Grad Sarajevo | Alipašin Most III | 48 | 3,817.400 | 79.500 | A |
| 8a1ea92ca11ffff | Ilidža | Dolovi | 37 | 2,943.100 | 79.500 | B |
| 8a1ef45906c7fff | Novo Sarajevo | Hrasno Brdo | 14 | 1,113.600 | 79.500 | B |
| 8a1ea92dd85ffff | Ilidža | Lipe | 17 | 1,352.600 | 79.600 | B |
| 8a1ef45964c7fff | Ilidža | Naselje Bulevar | 636 | 50,615.900 | 79.600 | B |
| 8a1ea92c9827fff | Novi Grad Sarajevo | Zabrđe | 32 | 2,546.800 | 79.600 | A |
| 8a1ef4594477fff | Novi Grad Sarajevo | Alipašin Most I | 34 | 2,706.500 | 79.600 | A |
| 8a1ef459444ffff | Novi Grad Sarajevo | Alipašin Most I | 41 | 3,263.700 | 79.600 | A |
| 8a1ef458224ffff | Stari Grad Sarajevo | Logavina | 123 | 9,795.000 | 79.600 | A |
| 8a1ea92ea687fff | Ilidža | Vlakovo | 21 | 1,672.600 | 79.600 | B |
| 8a1ef694650ffff | Ilidža | Hrasnica | 121 | 9,640.000 | 79.700 | B |
| 8a1ea92c2a1ffff | Ilidža | Rakovica | 11 | 876.500 | 79.700 | B |
| 8a1ef459cb87fff | Stari Grad Sarajevo | Bistrik | 162 | 12,912.300 | 79.700 | A |
| 8a1ea92cb2cffff | Ilidža | Azići | 155 | 12,369.700 | 79.800 | B |
| 8a1ef6965527fff | Ilidža | Ilidža | 72 | 5,747.300 | 79.800 | B |
| 8a1ef6960887fff | Ilidža | Stojčevac | 30 | 2,394.700 | 79.800 | B |
| 8a1ea92dd34ffff | Ilidža | Lipe | 241 | 19,242.100 | 79.800 | B |
| 8a1ea92c3ceffff | Ilidža | Gladno polje | 74 | 5,910.300 | 79.900 | B |
| 8a1ef459dd1ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 20 | 1,597.500 | 79.900 | A |
| 8a1ef459560ffff | Novo Sarajevo | Pofalići I | 36 | 2,875.700 | 79.900 | B |
| 8a1ef6965d47fff | Ilidža | Ilidža | 228 | 18,214.200 | 79.900 | B |
| 8a1ea92c9c2ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 114 | 9,108.400 | 79.900 | A |
| 8a1ef45b390ffff | Vogošća | Hotonj | 46 | 3,675.800 | 79.900 | B |
| 8a1ef4590157fff | Novi Grad Sarajevo | Alipašin Most III | 315 | 25,220.500 | 80.100 | A |
| 8a1ef459448ffff | Novi Grad Sarajevo | Alipašin Most I | 49 | 3,925.000 | 80.100 | A |
| 8a1ea92c5077fff | Ilidža | Zenik | 39 | 3,125.200 | 80.100 | B |
| 8a1ef45b6607fff | Vogošća | Krivoglavci | 15 | 1,202.500 | 80.200 | B |
| 8a1ef4594637fff | Novi Grad Sarajevo | Alipašin Most I | 51 | 4,089.500 | 80.200 | A |
| 8a1ef4590667fff | Novi Grad Sarajevo | Švrakino Selo III | 76 | 6,096.100 | 80.200 | A |
| 8a1ef45b52e7fff | Vogošća | Tihovići | 14 | 1,123.100 | 80.200 | B |
| 8a1ef459475ffff | Novi Grad Sarajevo | Dolac | 29 | 2,327.100 | 80.200 | A |
| 8a1ea92ca41ffff | Ilidža | Blažuj | 108 | 8,667.700 | 80.300 | B |
| 8a1ef45b0727fff | Vogošća | Vogošća | 153 | 12,280.000 | 80.300 | B |
| 8a1ea92c445ffff | Ilidža | Buhotina | 13 | 1,043.500 | 80.300 | B |
| 8a1ef4582347fff | Centar Sarajevo | Bardakčije | 82 | 6,582.500 | 80.300 | B |
| 8a1ef6965c87fff | Ilidža | Lužani | 282 | 22,642.400 | 80.300 | B |
| 8a1ef45804affff | Centar Sarajevo | Hrastovi-Mrkovići | 35 | 2,810.500 | 80.300 | B |
| 8a1ef4595987fff | Vogošća | Kobilja Glava | 47 | 3,774.900 | 80.300 | B |
| 8a1ef459c087fff | Stari Grad Sarajevo | Širokača | 47 | 3,775.000 | 80.300 | A |
| 8a1ef6964aeffff | Ilidža | Lužani | 27 | 2,171.000 | 80.400 | B |
| 8a1ef6971acffff | Ilidža | Hrasnica | 20 | 1,608.700 | 80.400 | B |
| 8a1ea92c91a7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 91 | 7,319.700 | 80.400 | A |
| 8a1ef459192ffff | Novo Sarajevo | Pofalići I | 41 | 3,298.500 | 80.500 | B |
| 8a1ea92ceb6ffff | Novi Grad Sarajevo | Dobroševići | 10 | 804.600 | 80.500 | A |
| 8a1ef4590917fff | Novi Grad Sarajevo | Buća Potok | 141 | 11,346.300 | 80.500 | A |
| 8a1ef45944e7fff | Novi Grad Sarajevo | Alipašin Most I | 54 | 4,345.400 | 80.500 | A |
| 8a1ef45946d7fff | Novi Grad Sarajevo | Buća Potok | 65 | 5,234.500 | 80.500 | A |
| 8a1ef45822effff | Stari Grad Sarajevo | Logavina | 121 | 9,749.200 | 80.600 | A |
| 8a1ef4583887fff | Stari Grad Sarajevo | Sedrenik | 35 | 2,820.300 | 80.600 | A |
| 8a1ea92c9727fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 77 | 6,206.700 | 80.600 | A |
| 8a1ef4590267fff | Novo Sarajevo | Trg heroja | 176 | 14,192.400 | 80.600 | B |
| 8a1ef6960817fff | Ilidža | Stojčevac | 11 | 887.300 | 80.700 | B |
| 8a1ef4591087fff | Novo Sarajevo | Vraca | 109 | 8,792.800 | 80.700 | B |
| 8a1ef459cce7fff | Centar Sarajevo | Soukbunar | 49 | 3,956.400 | 80.700 | B |
| 8a1ef4582407fff | Centar Sarajevo | Koševsko Brdo | 71 | 5,733.400 | 80.800 | B |
| 8a1ef459618ffff | Novi Grad Sarajevo | Briješće | 72 | 5,817.500 | 80.800 | A |
| 8a1ea92cac4ffff | Ilidža | Dolovi | 13 | 1,051.500 | 80.900 | B |
| 8a1ef4591adffff | Centar Sarajevo | Soukbunar | 68 | 5,501.300 | 80.900 | B |
| 8a1ef459659ffff | Ilidža | Naselje Bulevar | 73 | 5,906.000 | 80.900 | B |
| 8a1ef4582597fff | Novo Sarajevo | Pofalići I | 31 | 2,508.800 | 80.900 | B |
| 8a1ef4596617fff | Ilidža | Stupsko Brdo | 41 | 3,318.700 | 80.900 | B |
| 8a1ef4582c17fff | Novo Sarajevo | Gornji Velešići | 60 | 4,856.900 | 80.900 | B |
| 8a1ea92c96f7fff | Novi Grad Sarajevo | Briješće | 24 | 1,943.100 | 81.000 | A |
| 8a1ef4580597fff | Centar Sarajevo | Pionirska Dolina | 27 | 2,186.400 | 81.000 | B |
| 8a1ef459cd87fff | Centar Sarajevo | Soukbunar | 56 | 4,535.700 | 81.000 | B |
| 8a1ef45b050ffff | Vogošća | Vogošća | 124 | 10,045.800 | 81.000 | B |
| 8a1ef459281ffff | Novi Grad Sarajevo | Olimpijsko Selo | 47 | 3,808.400 | 81.000 | A |
| 8a1ef459ca37fff | Stari Grad Sarajevo | Babića bašča | 133 | 10,777.400 | 81.000 | A |
| 8a1ea92cb267fff | Ilidža | Azići | 89 | 7,215.800 | 81.100 | B |
| 8a1ef4594767fff | Novi Grad Sarajevo | Dolac | 22 | 1,784.100 | 81.100 | A |
| 8a1ef458376ffff | Stari Grad Sarajevo | Mošćanica | 12 | 973.400 | 81.100 | A |
| 8a1ef4594627fff | Novi Grad Sarajevo | Alipašin Most I | 61 | 4,948.300 | 81.100 | A |
| 8a1ef459441ffff | Novi Grad Sarajevo | Alipašin Most I | 49 | 3,975.400 | 81.100 | A |
| 8a1ef4596a67fff | Novi Grad Sarajevo | Alipašin Most I | 105 | 8,523.400 | 81.200 | A |
| 8a1ef4582997fff | Centar Sarajevo | Koševsko Brdo | 35 | 2,841.300 | 81.200 | B |
| 8a1ea92cb44ffff | Ilidža | Otes | 312 | 25,328.600 | 81.200 | B |
| 8a1ef4592b8ffff | Novi Grad Sarajevo | Švrakino Selo II | 10 | 811.900 | 81.200 | A |
| 8a1ef69650c7fff | Ilidža | Butmir | 31 | 2,517.200 | 81.200 | B |
| 8a1ef6960117fff | Ilidža | Stojčevac | 26 | 2,111.200 | 81.200 | B |
| 8a1ef45908affff | Novi Grad Sarajevo | Buća Potok | 83 | 6,744.400 | 81.300 | A |
| 8a1ef4593927fff | Novi Grad Sarajevo | Aneks | 125 | 10,161.200 | 81.300 | A |
| 8a1ef4596b8ffff | Novi Grad Sarajevo | Alipašin Most I | 22 | 1,788.600 | 81.300 | A |
| 8a1ef4582ac7fff | Centar Sarajevo | Hrastovi-Mrkovići | 53 | 4,312.700 | 81.400 | B |
| 8a1ef4595677fff | Novo Sarajevo | Pofalići I | 41 | 3,336.800 | 81.400 | B |
| 8a1ef4596b47fff | Novi Grad Sarajevo | Alipašin Most I | 78 | 6,353.100 | 81.400 | A |
| 8a1ef6965d9ffff | Ilidža | Lužani | 199 | 16,208.600 | 81.500 | B |
| 8a1ef6965daffff | Ilidža | Lužani | 168 | 13,685.600 | 81.500 | B |
| 8a1ef459141ffff | Novo Sarajevo | Vraca | 27 | 2,199.700 | 81.500 | B |
| 8a1ef45822e7fff | Stari Grad Sarajevo | Logavina | 128 | 10,430.100 | 81.500 | A |
| 8a1ef45b0307fff | Vogošća | Blagovac | 10 | 815.100 | 81.500 | B |
| 8a1ef4591987fff | Novo Sarajevo | Pofalići I | 41 | 3,342.400 | 81.500 | B |
| 8a1ef45910e7fff | Novo Sarajevo | Vraca | 72 | 5,872.600 | 81.600 | B |
| 8a1ef4583517fff | Stari Grad Sarajevo | Medrese | 155 | 12,656.300 | 81.700 | A |
| 8a1ef4596737fff | Ilidža | Stupsko Brdo | 195 | 15,929.400 | 81.700 | B |
| 8a1ef459462ffff | Novi Grad Sarajevo | Alipašin Most I | 59 | 4,819.700 | 81.700 | A |
| 8a1ea92c108ffff | Ilidža | Vlakovo | 10 | 817.100 | 81.700 | B |
| 8a1ef6961d37fff | Ilidža | Sokolović-kolonija | 264 | 21,581.400 | 81.700 | B |
| 8a1ef4590527fff | Novi Grad Sarajevo | Alipašino Polje AI | 68 | 5,560.400 | 81.800 | A |
| 8a1ef4590baffff | Novo Sarajevo | Pofalići II | 55 | 4,497.500 | 81.800 | B |
| 8a1ef459100ffff | Novo Sarajevo | Grbavica I | 140 | 11,450.800 | 81.800 | B |
| 8a1ef45b252ffff | Novi Grad Sarajevo | Zabrđe | 27 | 2,208.800 | 81.800 | A |
| 8a1ef4583c77fff | Stari Grad Sarajevo | Sedrenik | 54 | 4,418.300 | 81.800 | A |
| 8a1ef4596457fff | Ilidža | Stup | 590 | 48,292.000 | 81.900 | B |
| 8a1ef45947a7fff | Novi Grad Sarajevo | Alipašin Most I | 67 | 5,485.000 | 81.900 | A |
| 8a1ef4591707fff | Novo Sarajevo | Vraca | 28 | 2,292.600 | 81.900 | B |
| 8a1ef4596b6ffff | Novi Grad Sarajevo | Alipašin Most I | 86 | 7,042.600 | 81.900 | A |
| 8a1ef4590947fff | Novi Grad Sarajevo | Dolac | 50 | 4,095.000 | 81.900 | A |
| 8a1ef459262ffff | Novi Grad Sarajevo | Dobrinja B | 13 | 1,064.800 | 81.900 | A |
| 8a1ef4596b27fff | Novi Grad Sarajevo | Alipašin Most I | 26 | 2,129.800 | 81.900 | A |
| 8a1ef45b0467fff | Vogošća | Vogošća | 121 | 9,914.600 | 81.900 | B |
| 8a1ef4583ad7fff | Stari Grad Sarajevo | Mošćanica | 10 | 819.500 | 81.900 | A |
| 8a1ef4594777fff | Novi Grad Sarajevo | Alipašin Most I | 61 | 4,999.000 | 82.000 | A |
| 8a1ea92c9d4ffff | Novi Grad Sarajevo | Zabrđe | 15 | 1,229.400 | 82.000 | A |
| 8a1ef4596547fff | Ilidža | Stup | 292 | 23,932.300 | 82.000 | B |
| 8a1ef4592d5ffff | Novi Grad Sarajevo | Dobrinja A | 86 | 7,051.900 | 82.000 | A |
| 8a1ef6965c4ffff | Ilidža | Ilidža | 130 | 10,662.000 | 82.000 | B |
| 8a1ea92c9887fff | Novi Grad Sarajevo | Zabrđe | 18 | 1,476.400 | 82.000 | A |
| 8a1ef4591ca7fff | Novo Sarajevo | Trg heroja | 172 | 14,109.700 | 82.000 | B |
| 8a1ef459478ffff | Novi Grad Sarajevo | Alipašin Most I | 70 | 5,744.000 | 82.100 | A |
| 8a1ef4591ac7fff | Centar Sarajevo | Skenderija-Podtekija | 54 | 4,431.400 | 82.100 | B |
| 8a1ef4590d37fff | Novi Grad Sarajevo | Alipašin Most I | 110 | 9,029.600 | 82.100 | A |
| 8a1ef459cb5ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 60 | 4,925.500 | 82.100 | A |
| 8a1ef4594797fff | Novi Grad Sarajevo | Alipašin Most I | 83 | 6,816.600 | 82.100 | A |
| 8a1ef458318ffff | Stari Grad Sarajevo | Sedrenik | 48 | 3,942.800 | 82.100 | A |
| 8a1ef459155ffff | Novo Sarajevo | Vraca | 181 | 14,868.100 | 82.100 | B |
| 8a1ef4596a47fff | Novi Grad Sarajevo | Alipašin Most I | 117 | 9,611.800 | 82.200 | A |
| 8a1ef459425ffff | Novi Grad Sarajevo | Dolac | 28 | 2,302.100 | 82.200 | A |
| 8a1ef4592a37fff | Novi Grad Sarajevo | Švrakino Selo II | 20 | 1,644.900 | 82.200 | A |
| 8a1ef459392ffff | Novi Grad Sarajevo | Aneks | 70 | 5,757.700 | 82.300 | A |
| 8a1ef4595b17fff | Novo Sarajevo | Velešići | 10 | 822.600 | 82.300 | B |
| 8a1ef4590967fff | Novi Grad Sarajevo | Dolac | 47 | 3,867.000 | 82.300 | A |
| 8a1ef459cc4ffff | Centar Sarajevo | Soukbunar | 66 | 5,430.700 | 82.300 | B |
| 8a1ef4590747fff | Novi Grad Sarajevo | Švrakino Selo III | 86 | 7,077.100 | 82.300 | A |
| 8a1ef459098ffff | Novi Grad Sarajevo | Buća Potok | 114 | 9,384.100 | 82.300 | A |
| 8a1ef459391ffff | Novo Sarajevo | Hrasno Brdo | 21 | 1,729.400 | 82.400 | B |
| 8a1ef459081ffff | Novi Grad Sarajevo | Buća Potok | 80 | 6,590.500 | 82.400 | A |
| 8a1ea92ca9b7fff | Ilidža | Dolovi | 17 | 1,400.600 | 82.400 | B |
| 8a1ef458312ffff | Stari Grad Sarajevo | Sedrenik | 33 | 2,719.300 | 82.400 | A |
| 8a1ea92dd337fff | Ilidža | Lipe | 126 | 10,385.300 | 82.400 | B |
| 8a1ef459c12ffff | Stari Grad Sarajevo | Širokača | 109 | 8,986.600 | 82.400 | A |
| 8a1ef45b062ffff | Vogošća | Vogošća | 143 | 11,792.900 | 82.500 | B |
| 8a1ef4594707fff | Novi Grad Sarajevo | Alipašin Most I | 61 | 5,031.200 | 82.500 | A |
| 8a1ef69608effff | Ilidža | Sokolović-kolonija | 17 | 1,402.400 | 82.500 | B |
| 8a1ef4582087fff | Centar Sarajevo | Ciglane | 118 | 9,737.400 | 82.500 | B |
| 8a1ef6965c47fff | Ilidža | Ilidža | 97 | 8,005.300 | 82.500 | B |
| 8a1ef459250ffff | Ilidža | Stupsko Brdo | 361 | 29,817.400 | 82.600 | B |
| 8a1ef4594687fff | Novi Grad Sarajevo | Alipašin Most I | 95 | 7,847.100 | 82.600 | A |
| 8a1ef6965c07fff | Ilidža | Ilidža | 260 | 21,477.600 | 82.600 | B |
| 8a1ef6941b5ffff | Ilidža | Krupac | 13 | 1,073.900 | 82.600 | B |
| 8a1ea92ccb07fff | Novi Grad Sarajevo | Dobroševići | 13 | 1,074.000 | 82.600 | A |
| 8a1ef45906b7fff | Novi Grad Sarajevo | Švrakino Selo II | 34 | 2,810.300 | 82.700 | A |
| 8a1ef4590647fff | Novi Grad Sarajevo | Švrakino Selo III | 79 | 6,533.800 | 82.700 | A |
| 8a1ef4583527fff | Stari Grad Sarajevo | Medrese | 130 | 10,752.400 | 82.700 | A |
| 8a1ef4596b4ffff | Novi Grad Sarajevo | Alipašin Most I | 116 | 9,599.600 | 82.800 | A |
| 8a1ef4594757fff | Novi Grad Sarajevo | Alipašin Most I | 79 | 6,538.100 | 82.800 | A |
| 8a1ef45b3867fff | Vogošća | Ugorsko | 13 | 1,076.600 | 82.800 | B |
| 8a1ef45831affff | Stari Grad Sarajevo | Sedrenik | 54 | 4,472.600 | 82.800 | A |
| 8a1ef459dc0ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 30 | 2,485.400 | 82.800 | A |
| 8a1ef4592527fff | Ilidža | Stupsko Brdo | 33 | 2,734.000 | 82.800 | B |
| 8a1ef459469ffff | Novi Grad Sarajevo | Alipašin Most I | 112 | 9,281.100 | 82.900 | A |
| 8a1ef4596a4ffff | Novi Grad Sarajevo | Alipašin Most I | 137 | 11,353.100 | 82.900 | A |
| 8a1ef45907b7fff | Novi Grad Sarajevo | Švrakino Selo II | 68 | 5,635.700 | 82.900 | A |
| 8a1ef4590d07fff | Novi Grad Sarajevo | Alipašin Most I | 128 | 10,609.700 | 82.900 | A |
| 8a1ef4590d27fff | Novi Grad Sarajevo | Alipašin Most I | 84 | 6,963.100 | 82.900 | A |
| 8a1ef45940dffff | Novi Grad Sarajevo | Dolac | 44 | 3,648.000 | 82.900 | A |
| 8a1ef4591357fff | Centar Sarajevo | Soukbunar | 28 | 2,322.900 | 83.000 | B |
| 8a1ef6965c77fff | Ilidža | Ilidža | 48 | 3,982.400 | 83.000 | B |
| 8a1ef4596427fff | Ilidža | Stup | 109 | 9,043.700 | 83.000 | B |
| 8a1ef4583ceffff | Stari Grad Sarajevo | Medrese | 85 | 7,056.200 | 83.000 | A |
| 8a1ef459642ffff | Ilidža | Stup | 369 | 30,635.300 | 83.000 | B |
| 8a1ef4592a77fff | Novi Grad Sarajevo | Švrakino Selo II | 16 | 1,328.400 | 83.000 | A |
| 8a1ef459636ffff | Novi Grad Sarajevo | Alipašin Most I | 90 | 7,473.300 | 83.000 | A |
| 8a1ef45946a7fff | Novi Grad Sarajevo | Alipašin Most I | 93 | 7,722.800 | 83.000 | A |
| 8a1ef45908f7fff | Novi Grad Sarajevo | Buća Potok | 88 | 7,308.800 | 83.100 | A |
| 8a1ef6964a57fff | Ilidža | Lužani | 14 | 1,162.800 | 83.100 | B |
| 8a1ef459020ffff | Novo Sarajevo | Hrasno Brdo | 109 | 9,055.100 | 83.100 | B |
| 8a1ea92cbb17fff | Ilidža | Doglodi | 40 | 3,324.000 | 83.100 | B |
| 8a1ef459285ffff | Novi Grad Sarajevo | Švrakino Selo II | 18 | 1,496.000 | 83.100 | A |
| 8a1ef45920a7fff | Novi Grad Sarajevo | Dobrinja B | 83 | 6,900.400 | 83.100 | A |
| 8a1ef458269ffff | Centar Sarajevo | Marijin Dvor | 80 | 6,651.700 | 83.100 | B |
| 8a1ef4582cc7fff | Centar Sarajevo | Koševsko Brdo | 87 | 7,235.100 | 83.200 | B |
| 8a1ef459470ffff | Novi Grad Sarajevo | Alipašin Most I | 82 | 6,819.600 | 83.200 | A |
| 8a1ef45b6357fff | Vogošća | Vogošća | 27 | 2,246.400 | 83.200 | B |
| 8a1ea92ce2d7fff | Ilidža | Dolovi | 11 | 915.500 | 83.200 | B |
| 8a1ef4583117fff | Stari Grad Sarajevo | Sedrenik | 54 | 4,495.300 | 83.200 | A |
| 8a1ea92cb5a7fff | Ilidža | Donji Doglodi | 12 | 999.100 | 83.300 | B |
| 8a1ef4591047fff | Novo Sarajevo | Grbavica I | 217 | 18,075.000 | 83.300 | B |
| 8a1ea92ce797fff | Ilidža | Lipe | 14 | 1,166.600 | 83.300 | B |
| 8a1ea92eb4a7fff | Novi Grad Sarajevo | Dobroševići | 12 | 999.900 | 83.300 | A |
| 8a1ef458261ffff | Centar Sarajevo | Trg oslobođenja-Centar | 112 | 9,333.800 | 83.300 | B |
| 8a1ef4590757fff | Novi Grad Sarajevo | Švrakino Selo III | 84 | 7,000.700 | 83.300 | A |
| 8a1ef459472ffff | Novi Grad Sarajevo | Alipašin Most I | 63 | 5,251.200 | 83.400 | A |
| 8a1ef459cc77fff | Centar Sarajevo | Soukbunar | 50 | 4,167.700 | 83.400 | B |
| 8a1ef4586d57fff | Vogošća | Hotonj | 31 | 2,584.800 | 83.400 | B |
| 8a1ef45902a7fff | Novi Grad Sarajevo | Aneks | 90 | 7,509.500 | 83.400 | A |
| 8a1ea92cc1b7fff | Novi Grad Sarajevo | Dobroševići | 38 | 3,171.100 | 83.400 | A |
| 8a1ef6964a4ffff | Ilidža | Pejton | 312 | 26,038.600 | 83.500 | B |
| 8a1ef4594457fff | Novi Grad Sarajevo | Alipašin Most I | 88 | 7,347.700 | 83.500 | A |
| 8a1ef459479ffff | Novi Grad Sarajevo | Alipašin Most I | 99 | 8,266.500 | 83.500 | A |
| 8a1ea92c9d6ffff | Novi Grad Sarajevo | Zabrđe | 14 | 1,169.100 | 83.500 | A |
| 8a1ef4582557fff | Centar Sarajevo | Koševsko Brdo | 67 | 5,597.500 | 83.500 | B |
| 8a1ef4596a6ffff | Novi Grad Sarajevo | Alipašin Most I | 154 | 12,867.600 | 83.600 | A |
| 8a1ef45902d7fff | Novi Grad Sarajevo | Aneks | 60 | 5,013.400 | 83.600 | A |
| 8a1ef459658ffff | Ilidža | Naselje Bulevar | 42 | 3,509.500 | 83.600 | B |
| 8a1ef4595b6ffff | Centar Sarajevo | Šip | 33 | 2,758.200 | 83.600 | B |
| 8a1ef4594787fff | Novi Grad Sarajevo | Alipašin Most I | 106 | 8,860.000 | 83.600 | A |
| 8a1ef45b2c8ffff | Novi Grad Sarajevo | Reljevo | 22 | 1,839.000 | 83.600 | A |
| 8a1ef45944effff | Novi Grad Sarajevo | Alipašin Most I | 95 | 7,941.700 | 83.600 | A |
| 8a1ef45804b7fff | Centar Sarajevo | Koševo II | 79 | 6,606.500 | 83.600 | B |
| 8a1ef459cb07fff | Stari Grad Sarajevo | Babića bašča | 164 | 13,717.700 | 83.600 | A |
| 8a1ef45946b7fff | Novi Grad Sarajevo | Alipašin Most I | 109 | 9,120.200 | 83.700 | A |
| 8a1ef4580487fff | Centar Sarajevo | Hrastovi-Mrkovići | 37 | 3,097.200 | 83.700 | B |
| 8a1ea92c02dffff | Ilidža | Kakrinje | 51 | 4,269.400 | 83.700 | B |
| 8a1ef458678ffff | Centar Sarajevo | Šip | 55 | 4,605.300 | 83.700 | B |
| 8a1ef45944cffff | Novi Grad Sarajevo | Alipašin Most I | 102 | 8,542.600 | 83.800 | A |
| 8a1ef4583cd7fff | Stari Grad Sarajevo | Medrese | 104 | 8,712.200 | 83.800 | A |
| 8a1ea92ddb9ffff | Ilidža | Lipe | 231 | 19,351.300 | 83.800 | B |
| 8a1ef45822cffff | Stari Grad Sarajevo | Logavina | 127 | 10,639.600 | 83.800 | A |
| 8a1ef4582a1ffff | Centar Sarajevo | Hrastovi-Mrkovići | 53 | 4,440.400 | 83.800 | B |
| 8a1ea92c296ffff | Ilidža | Rudnik | 15 | 1,256.900 | 83.800 | B |
| 8a1ef4590b97fff | Novo Sarajevo | Kvadrant | 34 | 2,849.600 | 83.800 | B |
| 8a1ef45834b7fff | Stari Grad Sarajevo | Logavina | 152 | 12,739.500 | 83.800 | A |
| 8a1ef4582c1ffff | Novo Sarajevo | Velešići | 60 | 5,029.400 | 83.800 | B |
| 8a1ef459280ffff | Novi Grad Sarajevo | Olimpijsko Selo | 77 | 6,455.600 | 83.800 | A |
| 8a1ef4590817fff | Novi Grad Sarajevo | Buća Potok | 88 | 7,379.300 | 83.900 | A |
| 8a1ef6964b1ffff | Ilidža | Vreoca | 68 | 5,702.200 | 83.900 | B |
| 8a1ef4595507fff | Novi Grad Sarajevo | Dolac | 16 | 1,342.000 | 83.900 | A |
| 8a1ef4582db7fff | Novo Sarajevo | Velešići | 19 | 1,594.100 | 83.900 | B |
| 8a1ef4592a9ffff | Novi Grad Sarajevo | Dobrinja C | 46 | 3,861.000 | 83.900 | A |
| 8a1ef6965d77fff | Ilidža | Pejton | 293 | 24,598.300 | 84.000 | B |
| 8a1ef459c0d7fff | Stari Grad Sarajevo | Širokača | 43 | 3,611.300 | 84.000 | A |
| 8a1ef4596467fff | Ilidža | Stup | 57 | 4,788.300 | 84.000 | B |
| 8a1ef45820e7fff | Centar Sarajevo | Park-Višnjik | 80 | 6,720.900 | 84.000 | B |
| 8a1ef6965c2ffff | Ilidža | Ilidža | 203 | 17,054.500 | 84.000 | B |
| 8a1ef4590627fff | Novi Grad Sarajevo | Švrakino Selo III | 82 | 6,890.100 | 84.000 | A |
| 8a1ef45947b7fff | Novi Grad Sarajevo | Alipašin Most I | 109 | 9,159.400 | 84.000 | A |
| 8a1ef4583427fff | Stari Grad Sarajevo | Sumbuluša | 111 | 9,330.600 | 84.100 | A |
| 8a1ef45868a7fff | Vogošća | Kobilja Glava | 22 | 1,850.000 | 84.100 | B |
| 8a1ef459082ffff | Novi Grad Sarajevo | Buća Potok | 89 | 7,485.400 | 84.100 | A |
| 8a1ef4580557fff | Centar Sarajevo | Pionirska Dolina | 18 | 1,514.000 | 84.100 | B |
| 8a1ef459060ffff | Novi Grad Sarajevo | Švrakino Selo III | 67 | 5,637.100 | 84.100 | A |
| 8a1ef459095ffff | Novi Grad Sarajevo | Dolac | 65 | 5,469.200 | 84.100 | A |
| 8a1ef6964137fff | Ilidža | Plandište | 26 | 2,187.900 | 84.100 | B |
| 8a1ef45804c7fff | Centar Sarajevo | Pionirska Dolina | 38 | 3,198.100 | 84.200 | B |
| 8a1ea92ca447fff | Ilidža | Blažuj | 38 | 3,198.100 | 84.200 | B |
| 8a1ef45826b7fff | Centar Sarajevo | Crni Vrh-Gorica | 111 | 9,345.200 | 84.200 | B |
| 8a1ea92dda07fff | Ilidža | Lipe | 80 | 6,735.400 | 84.200 | B |
| 8a1ef459471ffff | Novi Grad Sarajevo | Alipašin Most I | 90 | 7,584.200 | 84.300 | A |
| 8a1ef45956affff | Novo Sarajevo | Pofalići II | 39 | 3,287.000 | 84.300 | B |
| 8a1ef696590ffff | Ilidža | Naselje Bulevar | 148 | 12,477.700 | 84.300 | B |
| 8a1ef45824f7fff | Centar Sarajevo | Koševsko Brdo | 87 | 7,335.200 | 84.300 | B |
| 8a1ea92cb7a7fff | Ilidža | Otes | 375 | 31,622.800 | 84.300 | B |
| 8a1ef6965caffff | Ilidža | Lužani | 112 | 9,452.800 | 84.400 | B |
| 8a1ef4583c8ffff | Stari Grad Sarajevo | Medrese | 116 | 9,790.900 | 84.400 | A |
| 8a1ef45b3b2ffff | Vogošća | Hotonj | 69 | 5,824.100 | 84.400 | B |
| 8a1ef4580d9ffff | Centar Sarajevo | Pionirska Dolina | 10 | 844.400 | 84.400 | B |
| 8a1ef45805b7fff | Centar Sarajevo | Betanija | 25 | 2,111.100 | 84.400 | B |
| 8a1ef45947affff | Novi Grad Sarajevo | Alipašin Most I | 109 | 9,205.300 | 84.500 | A |
| 8a1ef45954cffff | Novo Sarajevo | Pofalići II | 32 | 2,703.000 | 84.500 | B |
| 8a1ef45826d7fff | Centar Sarajevo | Trg oslobođenja-Centar | 80 | 6,758.300 | 84.500 | B |
| 8a1ef459c3b7fff | Stari Grad Sarajevo | Toka-Džeka | 25 | 2,112.500 | 84.500 | A |
| 8a1ef45837b7fff | Stari Grad Sarajevo | Vratnik | 113 | 9,548.500 | 84.500 | A |
| 8a1ef459c367fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 42 | 3,549.000 | 84.500 | A |
| 8a1ef6964127fff | Ilidža | Kamenjača | 13 | 1,099.700 | 84.600 | B |
| 8a1ef459460ffff | Novi Grad Sarajevo | Buća Potok | 53 | 4,484.400 | 84.600 | A |
| 8a1ea92c320ffff | Ilidža | Gladno polje | 42 | 3,556.000 | 84.700 | B |
| 8a1ef458351ffff | Stari Grad Sarajevo | Medrese | 148 | 12,535.000 | 84.700 | A |
| 8a1ef459c897fff | Centar Sarajevo | Skenderija-Podtekija | 93 | 7,877.900 | 84.700 | B |
| 8a1ea92ccaaffff | Novi Grad Sarajevo | Dobroševići | 12 | 1,016.700 | 84.700 | A |
| 8a1ef45944f7fff | Novi Grad Sarajevo | Alipašin Most I | 119 | 10,090.700 | 84.800 | A |
| 8a1ef459070ffff | Novi Grad Sarajevo | Švrakino Selo III | 104 | 8,826.700 | 84.900 | A |
| 8a1ea92c830ffff | Novi Grad Sarajevo | Dobroševići | 80 | 6,790.100 | 84.900 | A |
| 8a1ea92cb717fff | Ilidža | Otes | 103 | 8,743.300 | 84.900 | B |
| 8a1ef4594267fff | Novi Grad Sarajevo | Dolac | 11 | 933.900 | 84.900 | A |
| 8a1ef45964affff | Ilidža | Naselje Bulevar | 277 | 23,520.800 | 84.900 | B |
| 8a1ef459445ffff | Novi Grad Sarajevo | Alipašin Most I | 130 | 11,039.300 | 84.900 | A |
| 8a1ef4580697fff | Centar Sarajevo | Hrastovi-Mrkovići | 29 | 2,462.800 | 84.900 | B |
| 8a1ef459c137fff | Stari Grad Sarajevo | Širokača | 97 | 8,243.500 | 85.000 | A |
| 8a1ef459cb1ffff | Stari Grad Sarajevo | Babića bašča | 160 | 13,598.300 | 85.000 | A |
| 8a1ef4591b4ffff | Centar Sarajevo | Marijin Dvor | 107 | 9,094.100 | 85.000 | B |
| 8a1ef458641ffff | Centar Sarajevo | Šip | 43 | 3,655.400 | 85.000 | B |
| 8a1ef4596407fff | Ilidža | Stup | 99 | 8,417.100 | 85.000 | B |
| 8a1ef4591a5ffff | Centar Sarajevo | Skenderija-Podtekija | 67 | 5,697.100 | 85.000 | B |
| 8a1ef6965c67fff | Ilidža | Ilidža | 57 | 4,847.200 | 85.000 | B |
| 8a1ea92c9137fff | Novi Grad Sarajevo | Alipašin Most I | 84 | 7,147.000 | 85.100 | A |
| 8a1ef4580457fff | Centar Sarajevo | Pionirska Dolina | 16 | 1,362.700 | 85.200 | B |
| 8a1ef4590637fff | Novi Grad Sarajevo | Švrakino Selo III | 83 | 7,071.100 | 85.200 | A |
| 8a1ef459468ffff | Novi Grad Sarajevo | Buća Potok | 75 | 6,391.900 | 85.200 | A |
| 8a1ef4583007fff | Stari Grad Sarajevo | Mošćanica | 14 | 1,193.400 | 85.200 | A |
| 8a1ef459549ffff | Novi Grad Sarajevo | Buća Potok | 86 | 7,334.700 | 85.300 | A |
| 8a1ef459c15ffff | Stari Grad Sarajevo | Toka-Džeka | 101 | 8,624.900 | 85.400 | A |
| 8a1ef45822c7fff | Stari Grad Sarajevo | Logavina | 138 | 11,788.000 | 85.400 | A |
| 8a1ea92cd21ffff | Novi Grad Sarajevo | Reljevo | 264 | 22,552.800 | 85.400 | A |
| 8a1ef45943a7fff | Novi Grad Sarajevo | Dolac | 11 | 939.700 | 85.400 | A |
| 8a1ef4596077fff | Novi Grad Sarajevo | Briješće | 84 | 7,183.300 | 85.500 | A |
| 8a1ef4590677fff | Novi Grad Sarajevo | Švrakino Selo III | 77 | 6,589.900 | 85.600 | A |
| 8a1ea92c9a77fff | Novi Grad Sarajevo | Zabrđe | 12 | 1,027.800 | 85.700 | A |
| 8a1ef4590b5ffff | Novo Sarajevo | Pofalići II | 26 | 2,227.000 | 85.700 | B |
| 8a1ea92c96b7fff | Novi Grad Sarajevo | Briješće | 47 | 4,025.900 | 85.700 | A |
| 8a1ef4582adffff | Centar Sarajevo | Bardakčije | 60 | 5,142.700 | 85.700 | B |
| 8a1ef4590607fff | Novi Grad Sarajevo | Švrakino Selo III | 78 | 6,688.100 | 85.700 | A |
| 8a1ef4583037fff | Stari Grad Sarajevo | Sedrenik | 44 | 3,773.800 | 85.800 | A |
| 8a1ef459669ffff | Novi Grad Sarajevo | Saraj Polje | 63 | 5,405.200 | 85.800 | A |
| 8a1ef459106ffff | Novo Sarajevo | Kovačići | 161 | 13,813.500 | 85.800 | B |
| 8a1ef45b018ffff | Vogošća | Vogošća | 148 | 12,698.700 | 85.800 | B |
| 8a1ef4582527fff | Novo Sarajevo | Velešići | 215 | 18,447.800 | 85.800 | B |
| 8a1ef4583d4ffff | Stari Grad Sarajevo | Sedrenik | 47 | 4,034.000 | 85.800 | A |
| 8a1ef459655ffff | Ilidža | Stup | 111 | 9,530.700 | 85.900 | B |
| 8a1ef459c0effff | Stari Grad Sarajevo | Toka-Džeka | 53 | 4,551.500 | 85.900 | A |
| 8a1ef696591ffff | Ilidža | Pejton | 23 | 1,975.700 | 85.900 | B |
| 8a1ea92d9a67fff | Ilidža | Plandište | 23 | 1,975.800 | 85.900 | B |
| 8a1ef459c1affff | Stari Grad Sarajevo | Širokača | 85 | 7,304.600 | 85.900 | A |
| 8a1ef459c85ffff | Stari Grad Sarajevo | Bistrik | 180 | 15,477.300 | 86.000 | A |
| 8a1ef458350ffff | Stari Grad Sarajevo | Medrese | 135 | 11,609.300 | 86.000 | A |
| 8a1ef45864cffff | Centar Sarajevo | Šip | 51 | 4,386.400 | 86.000 | B |
| 8a1ef459531ffff | Novo Sarajevo | Velešići | 10 | 860.100 | 86.000 | B |
| 8a1ef458220ffff | Centar Sarajevo | Bardakčije | 96 | 8,259.300 | 86.000 | B |
| 8a1ef696589ffff | Ilidža | Ilidža | 78 | 6,711.000 | 86.000 | B |
| 8a1ef459ccc7fff | Centar Sarajevo | Soukbunar | 42 | 3,614.800 | 86.100 | B |
| 8a1ef4595ae7fff | Novo Sarajevo | Velešići | 15 | 1,291.300 | 86.100 | B |
| 8a1ef4590acffff | Novo Sarajevo | Čengić Vila I | 54 | 4,649.900 | 86.100 | B |
| 8a1ef45b0d47fff | Vogošća | Kremeš | 10 | 861.600 | 86.200 | B |
| 8a1ef4595647fff | Novo Sarajevo | Pofalići I | 157 | 13,527.800 | 86.200 | B |
| 8a1ef4582cf7fff | Novo Sarajevo | Velešići | 101 | 8,705.400 | 86.200 | B |
| 8a1ea92dd267fff | Ilidža | Blažuj | 26 | 2,241.300 | 86.200 | B |
| 8a1ef4590837fff | Novi Grad Sarajevo | Buća Potok | 104 | 8,968.000 | 86.200 | A |
| 8a1ef45912a7fff | Novo Sarajevo | Gornji Kovačići | 13 | 1,121.400 | 86.300 | B |
| 8a1ef459661ffff | Ilidža | Stupsko Brdo | 111 | 9,577.900 | 86.300 | B |
| 8a1ef6964a0ffff | Ilidža | Vreoca | 41 | 3,538.400 | 86.300 | B |
| 8a1ea92c90a7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 99 | 8,544.200 | 86.300 | A |
| 8a1ef4592557fff | Ilidža | Stupsko Brdo | 103 | 8,893.100 | 86.300 | B |
| 8a1ef459438ffff | Novi Grad Sarajevo | Dolac | 31 | 2,677.200 | 86.400 | A |
| 8a1ea92c98e7fff | Novi Grad Sarajevo | Zabrđe | 20 | 1,727.300 | 86.400 | A |
| 8a1ef4595b5ffff | Novo Sarajevo | Gornji Velešići | 15 | 1,295.800 | 86.400 | B |
| 8a1ef459254ffff | Novi Grad Sarajevo | Dobrinja B | 77 | 6,653.000 | 86.400 | A |
| 8a1ef45b0717fff | Vogošća | Vogošća | 174 | 15,037.000 | 86.400 | B |
| 8a1ea92e96e7fff | Vogošća | Svrake | 18 | 1,556.300 | 86.500 | B |
| 8a1ef458311ffff | Stari Grad Sarajevo | Sedrenik | 56 | 4,842.700 | 86.500 | A |
| 8a1ef4586267fff | Centar Sarajevo | Betanija | 13 | 1,124.300 | 86.500 | B |
| 8a1ef4595af7fff | Novo Sarajevo | Velešići | 15 | 1,297.400 | 86.500 | B |
| 8a1ef4590827fff | Novi Grad Sarajevo | Buća Potok | 99 | 8,563.500 | 86.500 | A |
| 8a1ef45952d7fff | Novo Sarajevo | Pofalići I | 49 | 4,239.100 | 86.500 | B |
| 8a1ef45904f7fff | Novi Grad Sarajevo | Švrakino Selo II | 61 | 5,277.400 | 86.500 | A |
| 8a1ef459109ffff | Novo Sarajevo | Vraca | 35 | 3,028.400 | 86.500 | B |
| 8a1ef459069ffff | Novi Grad Sarajevo | Švrakino Selo II | 24 | 2,076.700 | 86.500 | A |
| 8a1ef459062ffff | Novi Grad Sarajevo | Švrakino Selo III | 98 | 8,479.700 | 86.500 | A |
| 8a1ef4582257fff | Stari Grad Sarajevo | Logavina | 124 | 10,730.300 | 86.500 | A |
| 8a1ef4586907fff | Centar Sarajevo | Betanija | 15 | 1,298.700 | 86.600 | B |
| 8a1ef4592b6ffff | Novi Grad Sarajevo | Švrakino Selo II | 56 | 4,849.100 | 86.600 | A |
| 8a1ea92c92b7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 22 | 1,905.600 | 86.600 | A |
| 8a1ea92cbaa7fff | Ilidža | Doglodi | 15 | 1,299.400 | 86.600 | B |
| 8a1ef4583d67fff | Stari Grad Sarajevo | Sedrenik | 44 | 3,811.600 | 86.600 | A |
| 8a1ef45b2927fff | Vogošća | Vogošća | 24 | 2,079.100 | 86.600 | B |
| 8a1ef458050ffff | Centar Sarajevo | Pionirska Dolina | 26 | 2,252.900 | 86.700 | B |
| 8a1ef4582c4ffff | Centar Sarajevo | Koševsko Brdo | 67 | 5,807.000 | 86.700 | B |
| 8a1ef45807affff | Centar Sarajevo | Hrastovi-Mrkovići | 16 | 1,387.000 | 86.700 | B |
| 8a1ef4582daffff | Novo Sarajevo | Gornji Velešići | 26 | 2,254.000 | 86.700 | B |
| 8a1ef4594677fff | Novi Grad Sarajevo | Dolac | 38 | 3,294.700 | 86.700 | A |
| 8a1ef4594247fff | Novi Grad Sarajevo | Dolac | 29 | 2,515.000 | 86.700 | A |
| 8a1ef4592a1ffff | Novi Grad Sarajevo | Švrakino Selo II | 13 | 1,127.600 | 86.700 | A |
| 8a1ef4591d2ffff | Novo Sarajevo | Pofalići II | 245 | 21,257.300 | 86.800 | B |
| 8a1ef459461ffff | Novi Grad Sarajevo | Buća Potok | 68 | 5,902.800 | 86.800 | A |
| 8a1ef45830b7fff | Stari Grad Sarajevo | Sumbuluša | 41 | 3,561.500 | 86.900 | A |
| 8a1ea92c981ffff | Novi Grad Sarajevo | Zabrđe | 17 | 1,476.900 | 86.900 | A |
| 8a1ef4583d87fff | Stari Grad Sarajevo | Sedrenik | 83 | 7,214.500 | 86.900 | A |
| 8a1ef459294ffff | Novi Grad Sarajevo | Švrakino Selo II | 72 | 6,259.700 | 86.900 | A |
| 8a1ea92c9a1ffff | Novi Grad Sarajevo | Zabrđe | 17 | 1,478.100 | 86.900 | A |
| 8a1ef45b2577fff | Novi Grad Sarajevo | Zabrđe | 10 | 869.800 | 87.000 | A |
| 8a1ea92ddb87fff | Ilidža | Lipe | 11 | 957.200 | 87.000 | B |
| 8a1ef4591a17fff | Centar Sarajevo | Marijin Dvor | 87 | 7,571.200 | 87.000 | B |
| 8a1ef6960b07fff | Ilidža | Sokolović-kolonija | 44 | 3,830.600 | 87.100 | B |
| 8a1ef69658b7fff | Ilidža | Ilidža | 12 | 1,044.800 | 87.100 | B |
| 8a1ef459cc37fff | Centar Sarajevo | Soukbunar | 65 | 5,660.800 | 87.100 | B |
| 8a1ef4590807fff | Novi Grad Sarajevo | Buća Potok | 108 | 9,410.700 | 87.100 | A |
| 8a1ef4582b4ffff | Centar Sarajevo | Hrastovi-Mrkovići | 33 | 2,876.300 | 87.200 | B |
| 8a1ef459cdaffff | Centar Sarajevo | Skenderija-Podtekija | 61 | 5,317.800 | 87.200 | B |
| 8a1ef45964effff | Ilidža | Naselje Bulevar | 323 | 28,161.000 | 87.200 | B |
| 8a1ef4590617fff | Novi Grad Sarajevo | Švrakino Selo III | 106 | 9,243.000 | 87.200 | A |
| 8a1ef459091ffff | Novi Grad Sarajevo | Buća Potok | 99 | 8,632.800 | 87.200 | A |
| 8a1ef4586b5ffff | Centar Sarajevo | Betanija | 17 | 1,482.600 | 87.200 | B |
| 8a1ef458355ffff | Stari Grad Sarajevo | Sumbuluša | 109 | 9,507.500 | 87.200 | A |
| 8a1ea92c9b37fff | Novi Grad Sarajevo | Zabrđe | 23 | 2,006.700 | 87.200 | A |
| 8a1ef45825affff | Novo Sarajevo | Velešići | 59 | 5,148.800 | 87.300 | B |
| 8a1ef459061ffff | Novi Grad Sarajevo | Švrakino Selo III | 93 | 8,116.600 | 87.300 | A |
| 8a1ef45915a7fff | Novo Sarajevo | Hrasno Brdo | 116 | 10,124.100 | 87.300 | B |
| 8a1ef459cd1ffff | Centar Sarajevo | Skenderija-Podtekija | 58 | 5,063.900 | 87.300 | B |
| 8a1ef696112ffff | Ilidža | Donji Kotorac | 63 | 5,500.800 | 87.300 | B |
| 8a1ef458695ffff | Centar Sarajevo | Betanija | 15 | 1,309.800 | 87.300 | B |
| 8a1ef45b386ffff | Vogošća | Ugorsko | 14 | 1,222.600 | 87.300 | B |
| 8a1ea92c9897fff | Novi Grad Sarajevo | Zabrđe | 20 | 1,747.000 | 87.300 | A |
| 8a1ea92c970ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 97 | 8,472.900 | 87.300 | A |
| 8a1ef4583d6ffff | Stari Grad Sarajevo | Sedrenik | 40 | 3,494.400 | 87.400 | A |
| 8a1ea92ca58ffff | Ilidža | Blažuj | 71 | 6,204.100 | 87.400 | B |
| 8a1ef4582baffff | Centar Sarajevo | Hrastovi-Mrkovići | 49 | 4,283.600 | 87.400 | B |
| 8a1ef45904affff | Novi Grad Sarajevo | Švrakino Selo II | 69 | 6,033.300 | 87.400 | A |
| 8a1ef696501ffff | Ilidža | Butmir | 42 | 3,673.100 | 87.500 | B |
| 8a1ef45909affff | Novi Grad Sarajevo | Buća Potok | 101 | 8,833.700 | 87.500 | A |
| 8a1ef4590797fff | Novi Grad Sarajevo | Švrakino Selo II | 66 | 5,773.200 | 87.500 | A |
| 8a1ea92cb2c7fff | Ilidža | Azići | 122 | 10,671.800 | 87.500 | B |
| 8a1ef45b0437fff | Vogošća | Vogošća | 156 | 13,657.900 | 87.600 | B |
| 8a1ef458206ffff | Centar Sarajevo | Koševo II | 106 | 9,284.500 | 87.600 | B |
| 8a1ef4592097fff | Novi Grad Sarajevo | Dobrinja B | 83 | 7,273.100 | 87.600 | A |
| 8a1ea92cb277fff | Ilidža | Azići | 282 | 24,711.500 | 87.600 | B |
| 8a1ef4596517fff | Ilidža | Stup | 508 | 44,523.500 | 87.600 | B |
| 8a1ef45867b7fff | Centar Sarajevo | Šip | 57 | 4,997.300 | 87.700 | B |
| 8a1ef4583d5ffff | Stari Grad Sarajevo | Sedrenik | 59 | 5,175.900 | 87.700 | A |
| 8a1ea92c9c4ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 78 | 6,843.000 | 87.700 | A |
| 8a1ea92cb31ffff | Ilidža | Azići | 34 | 2,984.400 | 87.800 | B |
| 8a1ef45965a7fff | Ilidža | Stup | 186 | 16,328.200 | 87.800 | B |
| 8a1ef45b248ffff | Novi Grad Sarajevo | Zabrđe | 22 | 1,932.400 | 87.800 | A |
| 8a1ef459c557fff | Stari Grad Sarajevo | Širokača | 10 | 878.600 | 87.900 | A |
| 8a1ef458640ffff | Centar Sarajevo | Šip | 49 | 4,307.300 | 87.900 | B |
| 8a1ef459542ffff | Novi Grad Sarajevo | Dolac | 21 | 1,846.200 | 87.900 | A |
| 8a1ea92cc757fff | Novi Grad Sarajevo | Dobroševići | 27 | 2,374.000 | 87.900 | A |
| 8a1ef459439ffff | Novi Grad Sarajevo | Dolac | 30 | 2,638.500 | 88.000 | A |
| 8a1ef45b4cf7fff | Vogošća | Semizovac | 25 | 2,198.800 | 88.000 | B |
| 8a1ef69650f7fff | Ilidža | Butmir | 112 | 9,851.000 | 88.000 | B |
| 8a1ef459176ffff | Novo Sarajevo | Vraca | 33 | 2,902.600 | 88.000 | B |
| 8a1ef4590957fff | Novi Grad Sarajevo | Dolac | 84 | 7,388.800 | 88.000 | A |
| 8a1ef4592baffff | Novi Grad Sarajevo | Švrakino Selo II | 18 | 1,583.800 | 88.000 | A |
| 8a1ef4591857fff | Novo Sarajevo | Željeznička | 32 | 2,815.600 | 88.000 | B |
| 8a1ef459640ffff | Ilidža | Stup | 144 | 12,678.900 | 88.000 | B |
| 8a1ef4595397fff | Novo Sarajevo | Pofalići I | 31 | 2,729.800 | 88.100 | B |
| 8a1ef459390ffff | Novi Grad Sarajevo | Aneks | 71 | 6,254.700 | 88.100 | A |
| 8a1ef45b0627fff | Vogošća | Vogošća | 69 | 6,080.300 | 88.100 | B |
| 8a1ea92c99affff | Novi Grad Sarajevo | Zabrđe | 23 | 2,027.300 | 88.100 | A |
| 8a1ea92cb787fff | Ilidža | Otes | 201 | 17,724.700 | 88.200 | B |
| 8a1ef4595597fff | Novi Grad Sarajevo | Dolac | 56 | 4,938.300 | 88.200 | A |
| 8a1ef459cd5ffff | Centar Sarajevo | Skenderija-Podtekija | 93 | 8,203.400 | 88.200 | B |
| 8a1ef45902affff | Novi Grad Sarajevo | Staro Hrasno | 64 | 5,646.500 | 88.200 | A |
| 8a1ef4584c87fff | Centar Sarajevo | Betanija | 10 | 882.300 | 88.200 | B |
| 8a1ef4586457fff | Centar Sarajevo | Šip | 48 | 4,236.900 | 88.300 | B |
| 8a1ef459209ffff | Novi Grad Sarajevo | Dobrinja B | 97 | 8,564.200 | 88.300 | A |
| 8a1ef4590b4ffff | Novo Sarajevo | Pofalići II | 39 | 3,443.800 | 88.300 | B |
| 8a1ef458370ffff | Stari Grad Sarajevo | Vratnik | 56 | 4,945.500 | 88.300 | A |
| 8a1ef45b24b7fff | Novi Grad Sarajevo | Zabrđe | 32 | 2,826.000 | 88.300 | A |
| 8a1ef4596c97fff | Ilidža | Azići | 70 | 6,183.600 | 88.300 | B |
| 8a1ef4583587fff | Stari Grad Sarajevo | Medrese | 163 | 14,399.300 | 88.300 | A |
| 8a1ef459662ffff | Ilidža | Stupsko Brdo | 34 | 3,004.500 | 88.400 | B |
| 8a1ef4592b5ffff | Novi Grad Sarajevo | Švrakino Selo II | 45 | 3,978.100 | 88.400 | A |
| 8a1ef4592a07fff | Novi Grad Sarajevo | Švrakino Selo II | 20 | 1,768.200 | 88.400 | A |
| 8a1ea92cb7affff | Ilidža | Otes | 225 | 19,892.500 | 88.400 | B |
| 8a1ef4582c9ffff | Novo Sarajevo | Gornji Velešići | 107 | 9,468.000 | 88.500 | B |
| 8a1ef4591a47fff | Centar Sarajevo | Marijin Dvor | 58 | 5,132.900 | 88.500 | B |
| 8a1ef459156ffff | Novo Sarajevo | Grbavica II | 79 | 6,992.400 | 88.500 | B |
| 8a1ef459c847fff | Stari Grad Sarajevo | Bistrik | 144 | 12,746.600 | 88.500 | A |
| 8a1ea92c574ffff | Ilidža | Zenik | 11 | 974.500 | 88.600 | B |
| 8a1ef459c037fff | Stari Grad Sarajevo | Toka-Džeka | 84 | 7,442.100 | 88.600 | A |
| 8a1ef458235ffff | Stari Grad Sarajevo | Logavina | 106 | 9,391.500 | 88.600 | A |
| 8a1ef45906a7fff | Novi Grad Sarajevo | Švrakino Selo II | 78 | 6,911.600 | 88.600 | A |
| 8a1ef6965a2ffff | Novi Grad Sarajevo | Saraj Polje | 55 | 4,875.700 | 88.600 | A |
| 8a1ef459172ffff | Novo Sarajevo | Vraca | 34 | 3,014.700 | 88.700 | B |
| 8a1ea92cc88ffff | Novi Grad Sarajevo | Dobroševići | 53 | 4,699.600 | 88.700 | A |
| 8a1ea92ca71ffff | Ilidža | Blažuj | 15 | 1,331.000 | 88.700 | B |
| 8a1ef6960347fff | Ilidža | Sokolović-kolonija | 32 | 2,840.700 | 88.800 | B |
| 8a1ef459079ffff | Novi Grad Sarajevo | Švrakino Selo II | 72 | 6,391.900 | 88.800 | A |
| 8a1ef459ca4ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 32 | 2,841.900 | 88.800 | A |
| 8a1ef45b3b37fff | Vogošća | Hotonj | 13 | 1,154.700 | 88.800 | B |
| 8a1ef45b3a2ffff | Vogošća | Hotonj | 11 | 977.100 | 88.800 | B |
| 8a1ef4583477fff | Stari Grad Sarajevo | Vratnik | 128 | 11,372.300 | 88.800 | A |
| 8a1ef4590697fff | Novi Grad Sarajevo | Švrakino Selo II | 38 | 3,377.200 | 88.900 | A |
| 8a1ef458245ffff | Centar Sarajevo | Crni Vrh-Gorica | 103 | 9,154.400 | 88.900 | B |
| 8a1ef45b008ffff | Vogošća | Vogošća | 63 | 5,602.200 | 88.900 | B |
| 8a1ea92c989ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 87 | 7,737.800 | 88.900 | A |
| 8a1ef4583467fff | Stari Grad Sarajevo | Vratnik | 107 | 9,519.500 | 89.000 | A |
| 8a1ea92eb06ffff | Novi Grad Sarajevo | Reljevo | 11 | 978.900 | 89.000 | A |
| 8a1ef4595a07fff | Novo Sarajevo | Velešići | 12 | 1,068.200 | 89.000 | B |
| 8a1ef4591967fff | Novo Sarajevo | Pofalići I | 44 | 3,918.600 | 89.100 | B |
| 8a1ef459c727fff | Stari Grad Sarajevo | Širokača | 39 | 3,473.400 | 89.100 | A |
| 8a1ef45b3b4ffff | Vogošća | Hotonj | 122 | 10,866.300 | 89.100 | B |
| 8a1ef459216ffff | Novi Grad Sarajevo | Dobrinja C | 30 | 2,672.300 | 89.100 | A |
| 8a1ef4595267fff | Novo Sarajevo | Velešići | 45 | 4,010.900 | 89.100 | B |
| 8a1ef4591a6ffff | Centar Sarajevo | Marijin Dvor | 87 | 7,755.000 | 89.100 | B |
| 8a1ea92cd667fff | Novi Grad Sarajevo | Zabrđe | 22 | 1,962.000 | 89.200 | A |
| 8a1ef459048ffff | Novi Grad Sarajevo | Švrakino Selo II | 72 | 6,422.800 | 89.200 | A |
| 8a1ef45940c7fff | Novi Grad Sarajevo | Dolac | 25 | 2,230.200 | 89.200 | A |
| 8a1ef4580427fff | Centar Sarajevo | Pionirska Dolina | 30 | 2,676.700 | 89.200 | B |
| 8a1ef45b3b77fff | Vogošća | Hotonj | 15 | 1,338.900 | 89.300 | B |
| 8a1ef45824affff | Centar Sarajevo | Koševsko Brdo | 125 | 11,157.600 | 89.300 | B |
| 8a1ef45b6b2ffff | Vogošća | Ljubina-Poturovići | 49 | 4,376.400 | 89.300 | B |
| 8a1ef45b20b7fff | Novi Grad Sarajevo | Zabrđe | 14 | 1,250.700 | 89.300 | A |
| 8a1ef4592c37fff | Novi Grad Sarajevo | Dobrinja A | 136 | 12,150.500 | 89.300 | A |
| 8a1ea92c9acffff | Novi Grad Sarajevo | Zabrđe | 11 | 982.800 | 89.300 | A |
| 8a1ef6964a1ffff | Ilidža | Vreoca | 74 | 6,616.300 | 89.400 | B |
| 8a1ef459394ffff | Novo Sarajevo | Hrasno Brdo | 14 | 1,251.900 | 89.400 | B |
| 8a1ea92c9b1ffff | Novi Grad Sarajevo | Zabrđe | 24 | 2,146.800 | 89.400 | A |
| 8a1ef6964a47fff | Ilidža | Pejton | 62 | 5,546.600 | 89.500 | B |
| 8a1ef45940d7fff | Novi Grad Sarajevo | Dolac | 28 | 2,505.300 | 89.500 | A |
| 8a1ef4595aeffff | Novo Sarajevo | Velešići | 14 | 1,253.000 | 89.500 | B |
| 8a1ef4590a0ffff | Novo Sarajevo | Pofalići II | 109 | 9,762.300 | 89.600 | B |
| 8a1ef6965d37fff | Ilidža | Pejton | 174 | 15,584.100 | 89.600 | B |
| 8a1ea92c9337fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 12 | 1,074.900 | 89.600 | A |
| 8a1ef459464ffff | Novi Grad Sarajevo | Dolac | 156 | 13,976.100 | 89.600 | A |
| 8a1ef4595777fff | Novo Sarajevo | Pofalići II | 117 | 10,482.900 | 89.600 | B |
| 8a1ef4582447fff | Centar Sarajevo | Ciglane | 144 | 12,906.100 | 89.600 | B |
| 8a1ef45942effff | Novi Grad Sarajevo | Dolac | 46 | 4,125.300 | 89.700 | A |
| 8a1ef459199ffff | Novo Sarajevo | Željeznička | 39 | 3,499.300 | 89.700 | B |
| 8a1ea925b987fff | Vogošća | Gora | 25 | 2,244.100 | 89.800 | B |
| 8a1ef459c8effff | Stari Grad Sarajevo | Bistrik | 218 | 19,571.400 | 89.800 | A |
| 8a1ea92cdad7fff | Novi Grad Sarajevo | Reljevo | 13 | 1,167.300 | 89.800 | A |
| 8a1ef6961af7fff | Ilidža | Donji Kotorac | 151 | 13,560.500 | 89.800 | B |
| 8a1ef459208ffff | Novi Grad Sarajevo | Dobrinja B | 132 | 11,857.200 | 89.800 | A |
| 8a1ef4590a27fff | Novo Sarajevo | Pofalići II | 28 | 2,515.600 | 89.800 | B |
| 8a1ef459cae7fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 72 | 6,469.300 | 89.900 | A |
| 8a1ea92c3c17fff | Ilidža | Rakovica | 13 | 1,168.500 | 89.900 | B |
| 8a1ef4584827fff | Centar Sarajevo | Nahorevo | 11 | 988.900 | 89.900 | B |
| 8a1ef459c8cffff | Stari Grad Sarajevo | Bistrik | 201 | 18,070.500 | 89.900 | A |
| 8a1ef45946e7fff | Novi Grad Sarajevo | Buća Potok | 105 | 9,440.000 | 89.900 | A |
| 8a1ef459cd97fff | Centar Sarajevo | Soukbunar | 62 | 5,574.300 | 89.900 | B |
| 8a1ef4595237fff | Novo Sarajevo | Velešići | 30 | 2,698.100 | 89.900 | B |
| 8a1ea92cb78ffff | Ilidža | Otes | 165 | 14,841.600 | 89.900 | B |
| 8a1ef4590687fff | Novi Grad Sarajevo | Švrakino Selo II | 55 | 4,947.500 | 90.000 | A |
| 8a1ef45804d7fff | Centar Sarajevo | Hrastovi-Mrkovići | 33 | 2,970.800 | 90.000 | B |
| 8a1ef458205ffff | Centar Sarajevo | Park-Višnjik | 87 | 7,832.300 | 90.000 | B |
| 8a1ef45b208ffff | Novi Grad Sarajevo | Zabrđe | 10 | 900.400 | 90.000 | A |
| 8a1ef45b2cdffff | Novi Grad Sarajevo | Reljevo | 18 | 1,620.700 | 90.000 | A |
| 8a1ef45b2487fff | Novi Grad Sarajevo | Zabrđe | 33 | 2,971.400 | 90.000 | A |
| 8a1ef459465ffff | Novi Grad Sarajevo | Buća Potok | 95 | 8,556.400 | 90.100 | A |
| 8a1ea92c9ab7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 17 | 1,531.600 | 90.100 | A |
| 8a1ef459028ffff | Novi Grad Sarajevo | Staro Hrasno | 79 | 7,117.700 | 90.100 | A |
| 8a1ef459dcd7fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 22 | 1,982.300 | 90.100 | A |
| 8a1ef45b44a7fff | Vogošća | Semizovac | 102 | 9,190.800 | 90.100 | B |
| 8a1ef4590207fff | Novi Grad Sarajevo | Staro Hrasno | 82 | 7,390.800 | 90.100 | A |
| 8a1ef4586a47fff | Centar Sarajevo | Betanija | 11 | 991.500 | 90.100 | B |
| 8a1ef459c11ffff | Stari Grad Sarajevo | Toka-Džeka | 101 | 9,106.200 | 90.200 | A |
| 8a1ef6960097fff | Ilidža | Kovači (Ilidža) | 22 | 1,983.800 | 90.200 | B |
| 8a1ea92c9987fff | Novi Grad Sarajevo | Zabrđe | 26 | 2,345.100 | 90.200 | A |
| 8a1ef459561ffff | Novo Sarajevo | Pofalići I | 45 | 4,060.300 | 90.200 | B |
| 8a1ea92c9b0ffff | Novi Grad Sarajevo | Zabrđe | 16 | 1,443.800 | 90.200 | A |
| 8a1ef4583d97fff | Stari Grad Sarajevo | Sedrenik | 95 | 8,573.800 | 90.300 | A |
| 8a1ef6960b67fff | Ilidža | Sokolović-kolonija | 105 | 9,476.400 | 90.300 | B |
| 8a1ef69650a7fff | Ilidža | Ilidža | 96 | 8,664.300 | 90.300 | B |
| 8a1ef6960b77fff | Ilidža | Sokolović-kolonija | 294 | 26,536.200 | 90.300 | B |
| 8a1ef4580787fff | Centar Sarajevo | Hrastovi-Mrkovići | 22 | 1,985.700 | 90.300 | B |
| 8a1ef4583447fff | Stari Grad Sarajevo | Vratnik | 127 | 11,464.700 | 90.300 | A |
| 8a1ef45964cffff | Ilidža | Naselje Bulevar | 104 | 9,390.600 | 90.300 | B |
| 8a1ea92c982ffff | Novi Grad Sarajevo | Zabrđe | 45 | 4,064.700 | 90.300 | A |
| 8a1ea92ca51ffff | Ilidža | Blažuj | 67 | 6,054.600 | 90.400 | B |
| 8a1ef458290ffff | Centar Sarajevo | Betanija | 38 | 3,434.300 | 90.400 | B |
| 8a1ef696595ffff | Ilidža | Naselje Bulevar | 12 | 1,084.700 | 90.400 | B |
| 8a1ef45904dffff | Novi Grad Sarajevo | Švrakino Selo II | 82 | 7,415.300 | 90.400 | A |
| 8a1ef6965a5ffff | Novi Grad Sarajevo | Saraj Polje | 46 | 4,160.200 | 90.400 | A |
| 8a1ea92eb057fff | Novi Grad Sarajevo | Reljevo | 11 | 994.800 | 90.400 | A |
| 8a1ef4590a77fff | Novo Sarajevo | Pofalići II | 140 | 12,662.100 | 90.400 | B |
| 8a1ef4591937fff | Novo Sarajevo | Pofalići I | 108 | 9,768.300 | 90.400 | B |
| 8a1ef459c84ffff | Stari Grad Sarajevo | Bistrik | 169 | 15,286.500 | 90.500 | A |
| 8a1ef4595a17fff | Novo Sarajevo | Velešići | 13 | 1,175.900 | 90.500 | B |
| 8a1ea92cb29ffff | Ilidža | Azići | 134 | 12,124.700 | 90.500 | B |
| 8a1ef45b0c67fff | Vogošća | Vogošća | 24 | 2,171.900 | 90.500 | B |
| 8a1ef4594667fff | Novi Grad Sarajevo | Dolac | 47 | 4,253.700 | 90.500 | A |
| 8a1ef45b0667fff | Vogošća | Vogošća | 19 | 1,719.700 | 90.500 | B |
| 8a1ef4582ad7fff | Centar Sarajevo | Breka | 67 | 6,065.900 | 90.500 | B |
| 8a1ef4590277fff | Novo Sarajevo | Hrasno Brdo | 63 | 5,703.800 | 90.500 | B |
| 8a1ef458680ffff | Centar Sarajevo | Betanija | 10 | 905.400 | 90.500 | B |
| 8a1ef459551ffff | Novi Grad Sarajevo | Dolac | 45 | 4,074.500 | 90.500 | A |
| 8a1ef45906e7fff | Novi Grad Sarajevo | Švrakino Selo II | 62 | 5,615.900 | 90.600 | A |
| 8a1ef4596437fff | Ilidža | Stup | 90 | 8,152.900 | 90.600 | B |
| 8a1ef45904d7fff | Novi Grad Sarajevo | Švrakino Selo II | 86 | 7,791.100 | 90.600 | A |
| 8a1ef45854c7fff | Centar Sarajevo | Betanija | 10 | 905.900 | 90.600 | B |
| 8a1ef4583557fff | Stari Grad Sarajevo | Sumbuluša | 123 | 11,143.500 | 90.600 | A |
| 8a1ef458241ffff | Centar Sarajevo | Koševsko Brdo | 78 | 7,066.800 | 90.600 | B |
| 8a1ef4590217fff | Novi Grad Sarajevo | Staro Hrasno | 77 | 6,977.400 | 90.600 | A |
| 8a1ef4586b77fff | Centar Sarajevo | Betanija | 12 | 1,087.500 | 90.600 | B |
| 8a1ef4591af7fff | Novo Sarajevo | Kovačići | 48 | 4,350.400 | 90.600 | B |
| 8a1ef45909a7fff | Novi Grad Sarajevo | Buća Potok | 93 | 8,430.400 | 90.600 | A |
| 8a1ef4592847fff | Novi Grad Sarajevo | Švrakino Selo II | 58 | 5,258.500 | 90.700 | A |
| 8a1ea92c918ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 49 | 4,444.500 | 90.700 | A |
| 8a1ea92c9a87fff | Novi Grad Sarajevo | Zabrđe | 23 | 2,087.000 | 90.700 | A |
| 8a1ea92c90c7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 19 | 1,724.000 | 90.700 | A |
| 8a1ef4592a0ffff | Novi Grad Sarajevo | Švrakino Selo II | 14 | 1,270.500 | 90.700 | A |
| 8a1ef6961d07fff | Ilidža | Sokolović-kolonija | 269 | 24,421.600 | 90.800 | B |
| 8a1ea92c3237fff | Ilidža | Gladno polje | 90 | 8,174.800 | 90.800 | B |
| 8a1ef6965577fff | Ilidža | Ilidža | 73 | 6,630.700 | 90.800 | B |
| 8a1ef458048ffff | Centar Sarajevo | Hrastovi-Mrkovići | 37 | 3,361.300 | 90.800 | B |
| 8a1ef459274ffff | Novi Grad Sarajevo | Dobrinja B | 108 | 9,812.200 | 90.900 | A |
| 8a1ea92cd01ffff | Novi Grad Sarajevo | Reljevo | 19 | 1,727.200 | 90.900 | A |
| 8a1ef4590b37fff | Novi Grad Sarajevo | Buća Potok | 83 | 7,548.300 | 90.900 | A |
| 8a1ef4586a1ffff | Centar Sarajevo | Betanija | 11 | 1,000.500 | 91.000 | B |
| 8a1ef45b2087fff | Novi Grad Sarajevo | Zabrđe | 12 | 1,091.500 | 91.000 | A |
| 8a1ef45b5db7fff | Vogošća | Kremeš | 22 | 2,001.100 | 91.000 | B |
| 8a1ea92c33b7fff | Ilidža | Gladno polje | 57 | 5,185.400 | 91.000 | B |
| 8a1ef459d1b7fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 18 | 1,637.600 | 91.000 | A |
| 8a1ea92c9947fff | Novi Grad Sarajevo | Zabrđe | 39 | 3,548.500 | 91.000 | A |
| 8a1ef4582a9ffff | Centar Sarajevo | Breka | 67 | 6,097.800 | 91.000 | B |
| 8a1ef4596b2ffff | Novi Grad Sarajevo | Alipašin Most I | 25 | 2,276.200 | 91.000 | A |
| 8a1ef45904cffff | Novi Grad Sarajevo | Švrakino Selo II | 87 | 7,922.100 | 91.100 | A |
| 8a1ef459dcb7fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 28 | 2,549.600 | 91.100 | A |
| 8a1ef4594d8ffff | Novi Grad Sarajevo | Zabrđe | 11 | 1,001.700 | 91.100 | A |
| 8a1ef6965d1ffff | Ilidža | Pejton | 191 | 17,393.800 | 91.100 | B |
| 8a1ea92ca6f7fff | Ilidža | Plandište | 19 | 1,732.100 | 91.200 | B |
| 8a1ef459559ffff | Novi Grad Sarajevo | Dolac | 67 | 6,108.400 | 91.200 | A |
| 8a1ef45946f7fff | Novi Grad Sarajevo | Buća Potok | 120 | 10,942.400 | 91.200 | A |
| 8a1ef4584737fff | Centar Sarajevo | Betanija | 12 | 1,094.300 | 91.200 | B |
| 8a1ea92cb617fff | Ilidža | Otes | 217 | 19,818.700 | 91.300 | B |
| 8a1ef4592c5ffff | Novi Grad Sarajevo | Dobrinja D | 101 | 9,225.600 | 91.300 | A |
| 8a1ef45904c7fff | Novi Grad Sarajevo | Švrakino Selo II | 88 | 8,038.200 | 91.300 | A |
| 8a1ef6961957fff | Ilidža | Donji Kotorac | 55 | 5,024.500 | 91.400 | B |
| 8a1ef45846f7fff | Centar Sarajevo | Betanija | 15 | 1,370.700 | 91.400 | B |
| 8a1ef459130ffff | Novo Sarajevo | Gornji Kovačići | 60 | 5,485.000 | 91.400 | B |
| 8a1ef4591b07fff | Centar Sarajevo | Marijin Dvor | 152 | 13,895.900 | 91.400 | B |
| 8a1ef459675ffff | Ilidža | Stupsko Brdo | 107 | 9,782.000 | 91.400 | B |
| 8a1ef458645ffff | Centar Sarajevo | Šip | 55 | 5,028.600 | 91.400 | B |
| 8a1ef4580407fff | Centar Sarajevo | Pionirska Dolina | 33 | 3,017.500 | 91.400 | B |
| 8a1ea92c9c67fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 68 | 6,222.900 | 91.500 | A |
| 8a1ef696391ffff | Ilidža | Hrasnica | 108 | 9,883.800 | 91.500 | B |
| 8a1ef4592b4ffff | Novi Grad Sarajevo | Švrakino Selo II | 66 | 6,040.800 | 91.500 | A |
| 8a1ef459dc27fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 37 | 3,386.800 | 91.500 | A |
| 8a1ef4595b1ffff | Novo Sarajevo | Velešići | 13 | 1,190.300 | 91.600 | B |
| 8a1ef459c0b7fff | Stari Grad Sarajevo | Širokača | 56 | 5,129.500 | 91.600 | A |
| 8a1ef4595327fff | Novo Sarajevo | Velešići | 10 | 916.100 | 91.600 | B |
| 8a1ef45952effff | Novo Sarajevo | Pofalići I | 53 | 4,856.700 | 91.600 | B |
| 8a1ea92cb2dffff | Ilidža | Azići | 180 | 16,494.600 | 91.600 | B |
| 8a1ef4592b67fff | Novi Grad Sarajevo | Švrakino Selo II | 85 | 7,789.600 | 91.600 | A |
| 8a1ef45b65a7fff | Novi Grad Sarajevo | Reljevo | 21 | 1,925.000 | 91.700 | A |
| 8a1ef459dd5ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 27 | 2,475.100 | 91.700 | A |
| 8a1ea92eb12ffff | Novi Grad Sarajevo | Reljevo | 16 | 1,466.900 | 91.700 | A |
| 8a1ef458346ffff | Stari Grad Sarajevo | Vratnik | 98 | 8,986.500 | 91.700 | A |
| 8a1ea92c12a7fff | Ilidža | Gladno polje | 16 | 1,467.500 | 91.700 | B |
| 8a1ea92c06a7fff | Ilidža | Rakovica | 20 | 1,834.600 | 91.700 | B |
| 8a1ea92c98effff | Novi Grad Sarajevo | Zabrđe | 32 | 2,935.400 | 91.700 | A |
| 8a1ef45902c7fff | Novo Sarajevo | Hrasno Brdo | 87 | 7,981.600 | 91.700 | B |
| 8a1ef45904effff | Novi Grad Sarajevo | Švrakino Selo II | 109 | 10,003.200 | 91.800 | A |
| 8a1ef459cc07fff | Centar Sarajevo | Soukbunar | 67 | 6,149.400 | 91.800 | B |
| 8a1ef459dce7fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 30 | 2,754.000 | 91.800 | A |
| 8a1ef6965d2ffff | Ilidža | Pejton | 271 | 24,890.800 | 91.800 | B |
| 8a1ef45950effff | Novo Sarajevo | Pofalići I | 26 | 2,389.700 | 91.900 | B |
| 8a1ef4582aaffff | Centar Sarajevo | Breka | 75 | 6,893.600 | 91.900 | B |
| 8a1ef459c36ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 43 | 3,952.400 | 91.900 | A |
| 8a1ef45920b7fff | Novi Grad Sarajevo | Dobrinja B | 144 | 13,247.300 | 92.000 | A |
| 8a1ef4594237fff | Novi Grad Sarajevo | Dolac | 44 | 4,048.200 | 92.000 | A |
| 8a1ef458624ffff | Centar Sarajevo | Pionirska Dolina | 24 | 2,208.700 | 92.000 | B |
| 8a1ef4582d07fff | Centar Sarajevo | Donji Velešići | 32 | 2,945.300 | 92.000 | B |
| 8a1ef4590b87fff | Novo Sarajevo | Čengić Vila I | 20 | 1,840.800 | 92.000 | B |
| 8a1ef45954dffff | Novo Sarajevo | Pofalići II | 46 | 4,234.000 | 92.000 | B |
| 8a1ef459c967fff | Stari Grad Sarajevo | Logavina | 142 | 13,075.500 | 92.100 | A |
| 8a1ef459219ffff | Novi Grad Sarajevo | Dobrinja B | 152 | 13,998.100 | 92.100 | A |
| 8a1ef459c19ffff | Stari Grad Sarajevo | Širokača | 64 | 5,895.700 | 92.100 | A |
| 8a1ef4586467fff | Centar Sarajevo | Šip | 35 | 3,225.200 | 92.100 | B |
| 8a1ef4583487fff | Stari Grad Sarajevo | Kovači | 83 | 7,648.600 | 92.200 | A |
| 8a1ef6965cdffff | Ilidža | Ilidža | 87 | 8,018.200 | 92.200 | B |
| 8a1ef45914affff | Novo Sarajevo | Vraca | 25 | 2,304.200 | 92.200 | B |
| 8a1ef45b395ffff | Vogošća | Hotonj | 13 | 1,198.400 | 92.200 | B |
| 8a1ea92cc797fff | Novi Grad Sarajevo | Dobroševići | 12 | 1,106.400 | 92.200 | A |
| 8a1ef4590b2ffff | Novo Sarajevo | Pofalići II | 42 | 3,873.200 | 92.200 | B |
| 8a1ef45854dffff | Centar Sarajevo | Betanija | 11 | 1,014.500 | 92.200 | B |
| 8a1ef45953b7fff | Novo Sarajevo | Pofalići I | 25 | 2,307.200 | 92.300 | B |
| 8a1ef696436ffff | Ilidža | Lužani | 160 | 14,771.200 | 92.300 | B |
| 8a1ef4595b0ffff | Centar Sarajevo | Šip | 24 | 2,216.100 | 92.300 | B |
| 8a1ef458204ffff | Centar Sarajevo | Park-Višnjik | 85 | 7,849.400 | 92.300 | B |
| 8a1ef45b05affff | Vogošća | Vogošća | 134 | 12,382.100 | 92.400 | B |
| 8a1ea92cd367fff | Novi Grad Sarajevo | Reljevo | 26 | 2,402.600 | 92.400 | A |
| 8a1ef459698ffff | Novi Grad Sarajevo | Briješće | 24 | 2,219.500 | 92.500 | A |
| 8a1ef4592b47fff | Novi Grad Sarajevo | Švrakino Selo II | 81 | 7,493.500 | 92.500 | A |
| 8a1ea92c919ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 49 | 4,534.000 | 92.500 | A |
| 8a1ef458246ffff | Centar Sarajevo | Ciglane | 122 | 11,291.500 | 92.600 | B |
| 8a1ef4595437fff | Novi Grad Sarajevo | Dolac | 54 | 4,999.800 | 92.600 | A |
| 8a1ef6975acffff | Ilidža | Stojčevac | 14 | 1,296.500 | 92.600 | B |
| 8a1ef45b16a7fff | Vogošća | Hotonj | 11 | 1,018.700 | 92.600 | B |
| 8a1ef459c0affff | Stari Grad Sarajevo | Širokača | 64 | 5,928.500 | 92.600 | A |
| 8a1ef459424ffff | Novi Grad Sarajevo | Dolac | 47 | 4,354.400 | 92.600 | A |
| 8a1ef45b24a7fff | Novi Grad Sarajevo | Zabrđe | 29 | 2,686.900 | 92.700 | A |
| 8a1ea92ca61ffff | Ilidža | Plandište | 68 | 6,302.400 | 92.700 | B |
| 8a1ef459c02ffff | Stari Grad Sarajevo | Toka-Džeka | 90 | 8,342.900 | 92.700 | A |
| 8a1ef458488ffff | Centar Sarajevo | Nahorevo | 12 | 1,112.600 | 92.700 | B |
| 8a1ef4591927fff | Novo Sarajevo | Pofalići I | 60 | 5,564.700 | 92.700 | B |
| 8a1ef45846d7fff | Centar Sarajevo | Betanija | 14 | 1,298.700 | 92.800 | B |
| 8a1ef459431ffff | Novi Grad Sarajevo | Dolac | 16 | 1,484.300 | 92.800 | A |
| 8a1ef45910a7fff | Novo Sarajevo | Vraca | 88 | 8,165.700 | 92.800 | B |
| 8a1ef4594657fff | Novi Grad Sarajevo | Dolac | 96 | 8,911.300 | 92.800 | A |
| 8a1ef45942dffff | Novi Grad Sarajevo | Dolac | 83 | 7,705.100 | 92.800 | A |
| 8a1ea92ce2affff | Ilidža | Dolovi | 11 | 1,021.500 | 92.900 | B |
| 8a1ef6965b6ffff | Ilidža | Stupsko Brdo | 17 | 1,578.900 | 92.900 | B |
| 8a1ef4583c07fff | Stari Grad Sarajevo | Sedrenik | 82 | 7,616.200 | 92.900 | A |
| 8a1ef4590977fff | Novi Grad Sarajevo | Dolac | 92 | 8,545.300 | 92.900 | A |
| 8a1ef4596b97fff | Novi Grad Sarajevo | Briješće | 61 | 5,668.600 | 92.900 | A |
| 8a1ea92ceb87fff | Ilidža | Dolovi | 11 | 1,022.200 | 92.900 | B |
| 8a1ef45918f7fff | Novo Sarajevo | Željeznička | 51 | 4,741.000 | 93.000 | B |
| 8a1ea92c30dffff | Ilidža | Gladno polje | 36 | 3,348.100 | 93.000 | B |
| 8a1ea92c9617fff | Novi Grad Sarajevo | Briješće | 10 | 930.300 | 93.000 | A |
| 8a1ef459396ffff | Novo Sarajevo | Hrasno Brdo | 35 | 3,257.400 | 93.100 | B |
| 8a1ef4582027fff | Centar Sarajevo | Koševo II | 128 | 11,913.200 | 93.100 | B |
| 8a1ef459144ffff | Novo Sarajevo | Vraca | 36 | 3,353.900 | 93.200 | B |
| 8a1ef459dd87fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 43 | 4,006.200 | 93.200 | A |
| 8a1ef459090ffff | Novi Grad Sarajevo | Dolac | 96 | 8,944.400 | 93.200 | A |
| 8a1ef45864c7fff | Centar Sarajevo | Šip | 49 | 4,565.400 | 93.200 | B |
| 8a1ef4583317fff | Stari Grad Sarajevo | Mošćanica | 13 | 1,211.300 | 93.200 | A |
| 8a1ef4583637fff | Stari Grad Sarajevo | Vratnik | 74 | 6,897.000 | 93.200 | A |
| 8a1ef4582b97fff | Centar Sarajevo | Koševo II | 67 | 6,247.400 | 93.200 | B |
| 8a1ef4590a67fff | Novo Sarajevo | Pofalići II | 40 | 3,730.500 | 93.300 | B |
| 8a1ef4594207fff | Novi Grad Sarajevo | Dolac | 47 | 4,384.800 | 93.300 | A |
| 8a1ef459578ffff | Novo Sarajevo | Pofalići II | 50 | 4,665.000 | 93.300 | B |
| 8a1ef4596baffff | Novi Grad Sarajevo | Briješće | 14 | 1,306.300 | 93.300 | A |
| 8a1ef45b6257fff | Vogošća | Vogošća | 11 | 1,026.600 | 93.300 | B |
| 8a1ea92c9a17fff | Novi Grad Sarajevo | Zabrđe | 32 | 2,986.500 | 93.300 | A |
| 8a1ef4582c37fff | Novo Sarajevo | Gornji Velešići | 44 | 4,106.700 | 93.300 | B |
| 8a1ef458266ffff | Centar Sarajevo | Mejtaš-Bjelave | 95 | 8,867.200 | 93.300 | B |
| 8a1ea92eb84ffff | Novi Grad Sarajevo | Reljevo | 21 | 1,960.300 | 93.300 | A |
| 8a1ef458388ffff | Stari Grad Sarajevo | Sedrenik | 39 | 3,640.700 | 93.400 | A |
| 8a1ea92d9857fff | Ilidža | Blažuj | 10 | 933.600 | 93.400 | B |
| 8a1ef459189ffff | Novo Sarajevo | Željeznička | 76 | 7,097.900 | 93.400 | B |
| 8a1ef4596d77fff | Novi Grad Sarajevo | Briješće | 11 | 1,027.500 | 93.400 | A |
| 8a1ef45b14dffff | Vogošća | Hotonj | 74 | 6,914.300 | 93.400 | B |
| 8a1ef4582717fff | Centar Sarajevo | Džidžikovac-Koševo I | 133 | 12,428.000 | 93.400 | B |
| 8a1ea92c9207fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 10 | 934.500 | 93.500 | A |
| 8a1ef4594397fff | Novi Grad Sarajevo | Dolac | 21 | 1,963.500 | 93.500 | A |
| 8a1ef4593947fff | Novo Sarajevo | Hrasno Brdo | 26 | 2,431.300 | 93.500 | B |
| 8a1ef69618cffff | Ilidža | Donji Kotorac | 56 | 5,237.800 | 93.500 | B |
| 8a1ef459256ffff | Novi Grad Sarajevo | Dobrinja B | 176 | 16,464.900 | 93.600 | A |
| 8a1ef4591acffff | Centar Sarajevo | Soukbunar | 69 | 6,459.400 | 93.600 | B |
| 8a1ef45b021ffff | Vogošća | Blagovac | 12 | 1,123.600 | 93.600 | B |
| 8a1ef45910d7fff | Novo Sarajevo | Vraca | 46 | 4,308.300 | 93.700 | B |
| 8a1ef45902e7fff | Novi Grad Sarajevo | Staro Hrasno | 108 | 10,115.600 | 93.700 | A |
| 8a1ef45b259ffff | Novi Grad Sarajevo | Zabrđe | 32 | 2,998.800 | 93.700 | A |
| 8a1ea92cb45ffff | Ilidža | Otes | 66 | 6,185.200 | 93.700 | B |
| 8a1ef4583d0ffff | Stari Grad Sarajevo | Sedrenik | 68 | 6,374.000 | 93.700 | A |
| 8a1ef459648ffff | Ilidža | Naselje Bulevar | 14 | 1,312.300 | 93.700 | B |
| 8a1ef458295ffff | Centar Sarajevo | Koševo II | 50 | 4,687.300 | 93.700 | B |
| 8a1ef6964a8ffff | Ilidža | Vreoca | 71 | 6,657.700 | 93.800 | B |
| 8a1ef459180ffff | Novo Sarajevo | Željeznička | 35 | 3,282.600 | 93.800 | B |
| 8a1ef45b64f7fff | Novi Grad Sarajevo | Reljevo | 13 | 1,219.500 | 93.800 | A |
| 8a1ef45b20a7fff | Novi Grad Sarajevo | Zabrđe | 16 | 1,501.000 | 93.800 | A |
| 8a1ef45867affff | Centar Sarajevo | Šip | 64 | 6,004.100 | 93.800 | B |
| 8a1ef4595667fff | Novo Sarajevo | Pofalići I | 60 | 5,630.200 | 93.800 | B |
| 8a1ef4591907fff | Novo Sarajevo | Pofalići I | 62 | 5,818.200 | 93.800 | B |
| 8a1ef4591b6ffff | Centar Sarajevo | Crni Vrh-Gorica | 83 | 7,788.900 | 93.800 | B |
| 8a1ef45942c7fff | Novi Grad Sarajevo | Dolac | 77 | 7,227.800 | 93.900 | A |
| 8a1ef45b3b87fff | Vogošća | Hotonj | 13 | 1,220.500 | 93.900 | B |
| 8a1ef4592d47fff | Novi Grad Sarajevo | Saraj Polje | 100 | 9,389.700 | 93.900 | A |
| 8a1ef45940cffff | Novi Grad Sarajevo | Dolac | 32 | 3,005.400 | 93.900 | A |
| 8a1ef4592087fff | Novi Grad Sarajevo | Dobrinja B | 188 | 17,657.600 | 93.900 | A |
| 8a1ea92c9b17fff | Novi Grad Sarajevo | Zabrđe | 31 | 2,913.300 | 94.000 | A |
| 8a1ef4596997fff | Novi Grad Sarajevo | Briješće | 97 | 9,117.900 | 94.000 | A |
| 8a1ea92c98b7fff | Novi Grad Sarajevo | Zabrđe | 28 | 2,632.000 | 94.000 | A |
| 8a1ef4591c37fff | Novo Sarajevo | Malta | 82 | 7,711.100 | 94.000 | B |
| 8a1ef4582c47fff | Centar Sarajevo | Koševsko Brdo | 73 | 6,865.000 | 94.000 | B |
| 8a1ef4595517fff | Novi Grad Sarajevo | Dolac | 52 | 4,890.300 | 94.000 | A |
| 8a1ef4590937fff | Novi Grad Sarajevo | Dolac | 88 | 8,276.200 | 94.000 | A |
| 8a1ef4582277fff | Stari Grad Sarajevo | Logavina | 126 | 11,850.300 | 94.100 | A |
| 8a1ef4590657fff | Novi Grad Sarajevo | Švrakino Selo III | 79 | 7,431.900 | 94.100 | A |
| 8a1ea92cbb97fff | Ilidža | Doglodi | 117 | 11,009.100 | 94.100 | B |
| 8a1ea92cb79ffff | Ilidža | Otes | 83 | 7,812.000 | 94.100 | B |
| 8a1ef45954d7fff | Novo Sarajevo | Pofalići II | 49 | 4,612.100 | 94.100 | B |
| 8a1ef45820effff | Centar Sarajevo | Park-Višnjik | 81 | 7,625.500 | 94.100 | B |
| 8a1ef45956a7fff | Novo Sarajevo | Pofalići II | 57 | 5,366.600 | 94.200 | B |
| 8a1ef459428ffff | Novi Grad Sarajevo | Dolac | 75 | 7,061.400 | 94.200 | A |
| 8a1ef45942b7fff | Novi Grad Sarajevo | Dolac | 64 | 6,026.700 | 94.200 | A |
| 8a1ef6965c5ffff | Ilidža | Ilidža | 87 | 8,193.000 | 94.200 | B |
| 8a1ea92eb85ffff | Novi Grad Sarajevo | Reljevo | 19 | 1,791.500 | 94.300 | A |
| 8a1ef4590b67fff | Novo Sarajevo | Pofalići II | 45 | 4,243.400 | 94.300 | B |
| 8a1ef45b20affff | Novi Grad Sarajevo | Zabrđe | 13 | 1,226.100 | 94.300 | A |
| 8a1ef459422ffff | Novi Grad Sarajevo | Dolac | 39 | 3,680.100 | 94.400 | A |
| 8a1ef459c50ffff | Stari Grad Sarajevo | Širokača | 22 | 2,076.700 | 94.400 | A |
| 8a1ef45b3a77fff | Vogošća | Hotonj | 51 | 4,815.700 | 94.400 | B |
| 8a1ef6965187fff | Ilidža | Ilidža | 151 | 14,258.400 | 94.400 | B |
| 8a1ef458625ffff | Centar Sarajevo | Betanija | 18 | 1,699.700 | 94.400 | B |
| 8a1ef45910c7fff | Novo Sarajevo | Vraca | 45 | 4,249.300 | 94.400 | B |
| 8a1ef459dc67fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 20 | 1,889.100 | 94.500 | A |
| 8a1ef4582d9ffff | Novo Sarajevo | Gornji Velešići | 45 | 4,250.700 | 94.500 | B |
| 8a1ef4595627fff | Novo Sarajevo | Pofalići II | 56 | 5,290.800 | 94.500 | B |
| 8a1ef459521ffff | Novo Sarajevo | Velešići | 58 | 5,481.700 | 94.500 | B |
| 8a1ef459660ffff | Novi Grad Sarajevo | Saraj Polje | 138 | 13,047.600 | 94.500 | A |
| 8a1ef4595387fff | Novo Sarajevo | Pofalići I | 30 | 2,836.600 | 94.600 | B |
| 8a1ef459cb67fff | Stari Grad Sarajevo | Vratnik | 129 | 12,197.600 | 94.600 | A |
| 8a1ea92c9b27fff | Novi Grad Sarajevo | Zabrđe | 31 | 2,931.500 | 94.600 | A |
| 8a1ef4592ca7fff | Novi Grad Sarajevo | Dobrinja A | 46 | 4,350.100 | 94.600 | A |
| 8a1ea92c90effff | Novi Grad Sarajevo | Naselje heroja Sokolje | 75 | 7,092.700 | 94.600 | A |
| 8a1ef459dceffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 14 | 1,324.100 | 94.600 | A |
| 8a1ef4594287fff | Novi Grad Sarajevo | Dolac | 67 | 6,339.400 | 94.600 | A |
| 8a1ef4590907fff | Novi Grad Sarajevo | Dolac | 115 | 10,882.000 | 94.600 | A |
| 8a1ef459cd9ffff | Centar Sarajevo | Soukbunar | 65 | 6,151.200 | 94.600 | B |
| 8a1ea92cd217fff | Novi Grad Sarajevo | Reljevo | 476 | 45,060.400 | 94.700 | A |
| 8a1ef45b3ba7fff | Vogošća | Hotonj | 14 | 1,326.400 | 94.700 | B |
| 8a1ef4590927fff | Novi Grad Sarajevo | Dolac | 97 | 9,193.700 | 94.800 | A |
| 8a1ef45b249ffff | Novi Grad Sarajevo | Zabrđe | 35 | 3,317.500 | 94.800 | A |
| 8a1ef4592c47fff | Novi Grad Sarajevo | Dobrinja A | 69 | 6,541.700 | 94.800 | A |
| 8a1ef459c947fff | Stari Grad Sarajevo | Logavina | 135 | 12,803.600 | 94.800 | A |
| 8a1ef45822dffff | Stari Grad Sarajevo | Logavina | 145 | 13,752.600 | 94.800 | A |
| 8a1ef459466ffff | Novi Grad Sarajevo | Dolac | 78 | 7,401.200 | 94.900 | A |
| 8a1ef45942d7fff | Novi Grad Sarajevo | Dolac | 89 | 8,448.900 | 94.900 | A |
| 8a1ea92c90d7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 43 | 4,082.200 | 94.900 | A |
| 8a1ef4595b47fff | Centar Sarajevo | Šip | 31 | 2,943.400 | 94.900 | B |
| 8a1ef459136ffff | Centar Sarajevo | Soukbunar | 60 | 5,697.000 | 95.000 | B |
| 8a1ef4582737fff | Centar Sarajevo | Ciglane | 165 | 15,669.000 | 95.000 | B |
| 8a1ef4595657fff | Novo Sarajevo | Pofalići I | 60 | 5,698.300 | 95.000 | B |
| 8a1ef4595337fff | Novo Sarajevo | Velešići | 17 | 1,614.800 | 95.000 | B |
| 8a1ea92cb697fff | Ilidža | Pejton | 13 | 1,235.200 | 95.000 | B |
| 8a1ef6961aaffff | Ilidža | Donji Kotorac | 78 | 7,412.300 | 95.000 | B |
| 8a1ef4583c5ffff | Stari Grad Sarajevo | Sumbuluša | 88 | 8,365.800 | 95.100 | A |
| 8a1ef45b0217fff | Vogošća | Blagovac | 12 | 1,141.000 | 95.100 | B |
| 8a1ef45913affff | Novo Sarajevo | Gornji Kovačići | 39 | 3,708.300 | 95.100 | B |
| 8a1ef45943affff | Novi Grad Sarajevo | Dolac | 36 | 3,424.500 | 95.100 | A |
| 8a1ef4592c77fff | Novi Grad Sarajevo | Dobrinja A | 46 | 4,377.800 | 95.200 | A |
| 8a1ef4593917fff | Novo Sarajevo | Hrasno Brdo | 76 | 7,233.500 | 95.200 | B |
| 8a1ef4583497fff | Stari Grad Sarajevo | Baščaršija | 122 | 11,612.800 | 95.200 | A |
| 8a1ef459426ffff | Novi Grad Sarajevo | Dolac | 55 | 5,235.400 | 95.200 | A |
| 8a1ef4594da7fff | Novi Grad Sarajevo | Zabrđe | 17 | 1,618.500 | 95.200 | A |
| 8a1ef458244ffff | Centar Sarajevo | Ciglane | 118 | 11,235.200 | 95.200 | B |
| 8a1ef459558ffff | Novi Grad Sarajevo | Dolac | 80 | 7,618.200 | 95.200 | A |
| 8a1ef4595b2ffff | Centar Sarajevo | Šip | 19 | 1,809.700 | 95.200 | B |
| 8a1ef458268ffff | Centar Sarajevo | Trg oslobođenja-Centar | 96 | 9,144.900 | 95.300 | B |
| 8a1ef6963b9ffff | Ilidža | Lasica | 105 | 10,004.300 | 95.300 | B |
| 8a1ea92dd90ffff | Ilidža | Gladno polje | 33 | 3,144.500 | 95.300 | B |
| 8a1ef45955b7fff | Novi Grad Sarajevo | Dolac | 79 | 7,527.800 | 95.300 | A |
| 8a1ef459c8affff | Stari Grad Sarajevo | Mjedenica | 87 | 8,290.400 | 95.300 | A |
| 8a1ea92c9807fff | Novi Grad Sarajevo | Zabrđe | 62 | 5,909.600 | 95.300 | A |
| 8a1ef4591537fff | Novo Sarajevo | Hrasno Brdo | 70 | 6,672.300 | 95.300 | B |
| 8a1ea92c910ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 17 | 1,621.500 | 95.400 | A |
| 8a1ef459dd57fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 31 | 2,957.200 | 95.400 | A |
| 8a1ef458345ffff | Stari Grad Sarajevo | Vratnik | 140 | 13,358.100 | 95.400 | A |
| 8a1ef459545ffff | Novo Sarajevo | Pofalići II | 31 | 2,958.000 | 95.400 | B |
| 8a1ef45b2497fff | Novi Grad Sarajevo | Zabrđe | 48 | 4,580.300 | 95.400 | A |
| 8a1ef4591b57fff | Centar Sarajevo | Marijin Dvor | 119 | 11,363.500 | 95.500 | B |
| 8a1ea92c9b2ffff | Novi Grad Sarajevo | Zabrđe | 18 | 1,718.900 | 95.500 | A |
| 8a1ef458039ffff | Centar Sarajevo | Hrastovi-Mrkovići | 10 | 954.900 | 95.500 | B |
| 8a1ef4582d87fff | Novo Sarajevo | Gornji Velešići | 40 | 3,820.300 | 95.500 | B |
| 8a1ef4591baffff | Centar Sarajevo | Marijin Dvor | 73 | 6,972.900 | 95.500 | B |
| 8a1ef6964b9ffff | Ilidža | Vreoca | 102 | 9,743.700 | 95.500 | B |
| 8a1ef459119ffff | Novo Sarajevo | Grbavica II | 73 | 6,974.200 | 95.500 | B |
| 8a1ef6964c17fff | Ilidža | Vrelo Bosne | 20 | 1,910.800 | 95.500 | B |
| 8a1ef4595a0ffff | Novo Sarajevo | Velešići | 21 | 2,006.500 | 95.500 | B |
| 8a1ef45b1617fff | Vogošća | Hotonj | 10 | 955.700 | 95.600 | B |
| 8a1ef4592667fff | Novi Grad Sarajevo | Dobrinja B | 30 | 2,867.500 | 95.600 | A |
| 8a1ef458359ffff | Stari Grad Sarajevo | Logavina | 157 | 15,022.600 | 95.700 | A |
| 8a1ef45942a7fff | Novi Grad Sarajevo | Dolac | 76 | 7,276.500 | 95.700 | A |
| 8a1ea92c859ffff | Ilidža | Dolovi | 15 | 1,436.400 | 95.800 | B |
| 8a1ea92cb62ffff | Ilidža | Otes | 11 | 1,053.700 | 95.800 | B |
| 8a1ef459d9a7fff | Stari Grad Sarajevo | Mošćanica | 13 | 1,245.300 | 95.800 | A |
| 8a1ef459c887fff | Stari Grad Sarajevo | Mjedenica | 87 | 8,338.300 | 95.800 | A |
| 8a1ef4595d8ffff | Novi Grad Sarajevo | Dolac | 16 | 1,533.700 | 95.900 | A |
| 8a1ef4584837fff | Centar Sarajevo | Nahorevo | 10 | 958.700 | 95.900 | B |
| 8a1ef45b255ffff | Novi Grad Sarajevo | Zabrđe | 17 | 1,630.000 | 95.900 | A |
| 8a1ef45952c7fff | Novo Sarajevo | Pofalići I | 66 | 6,329.400 | 95.900 | B |
| 8a1ef4594277fff | Novi Grad Sarajevo | Dolac | 59 | 5,659.000 | 95.900 | A |
| 8a1ea925b817fff | Vogošća | Gora | 15 | 1,438.800 | 95.900 | B |
| 8a1ef4595607fff | Novo Sarajevo | Pofalići II | 57 | 5,468.000 | 95.900 | B |
| 8a1ef459ca0ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 87 | 8,349.000 | 96.000 | A |
| 8a1ef45834cffff | Stari Grad Sarajevo | Vratnik | 128 | 12,284.200 | 96.000 | A |
| 8a1ef459ca1ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 89 | 8,542.400 | 96.000 | A |
| 8a1ea92ca637fff | Ilidža | Osjek | 13 | 1,247.900 | 96.000 | B |
| 8a1ef459c56ffff | Stari Grad Sarajevo | Širokača | 58 | 5,569.800 | 96.000 | A |
| 8a1ef45b3a5ffff | Vogošća | Hotonj | 12 | 1,152.600 | 96.000 | B |
| 8a1ef4594297fff | Novi Grad Sarajevo | Dolac | 82 | 7,876.500 | 96.100 | A |
| 8a1ef6961817fff | Ilidža | Butmir | 48 | 4,611.300 | 96.100 | B |
| 8a1ef4595617fff | Novo Sarajevo | Pofalići II | 56 | 5,380.000 | 96.100 | B |
| 8a1ef45942e7fff | Novi Grad Sarajevo | Dolac | 88 | 8,454.500 | 96.100 | A |
| 8a1ea92c9b67fff | Novi Grad Sarajevo | Zabrđe | 10 | 960.800 | 96.100 | A |
| 8a1ef4592ab7fff | Novi Grad Sarajevo | Dobrinja C | 61 | 5,862.700 | 96.100 | A |
| 8a1ef45b398ffff | Vogošća | Ugorsko | 11 | 1,057.300 | 96.100 | B |
| 8a1ef458061ffff | Centar Sarajevo | Hrastovi-Mrkovići | 17 | 1,634.500 | 96.100 | B |
| 8a1ef459092ffff | Novi Grad Sarajevo | Dolac | 120 | 11,538.100 | 96.200 | A |
| 8a1ef45804cffff | Centar Sarajevo | Pionirska Dolina | 33 | 3,173.700 | 96.200 | B |
| 8a1ef4582d5ffff | Centar Sarajevo | Koševsko Brdo | 113 | 10,868.300 | 96.200 | B |
| 8a1ef459d197fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 23 | 2,213.400 | 96.200 | A |
| 8a1ef45b039ffff | Vogošća | Blagovac | 15 | 1,443.600 | 96.200 | B |
| 8a1ef4590247fff | Novo Sarajevo | Hrasno Brdo | 126 | 12,130.500 | 96.300 | B |
| 8a1ef45b3a17fff | Vogošća | Hotonj | 14 | 1,347.900 | 96.300 | B |
| 8a1ef459429ffff | Novi Grad Sarajevo | Dolac | 90 | 8,665.100 | 96.300 | A |
| 8a1ef4595767fff | Novo Sarajevo | Pofalići I | 43 | 4,140.100 | 96.300 | B |
| 8a1ea92c96effff | Novi Grad Sarajevo | Briješće | 47 | 4,528.700 | 96.400 | A |
| 8a1ef4580737fff | Centar Sarajevo | Hrastovi-Mrkovići | 18 | 1,735.200 | 96.400 | B |
| 8a1ef4594257fff | Novi Grad Sarajevo | Dolac | 83 | 8,001.600 | 96.400 | A |
| 8a1ef6960acffff | Ilidža | Sokolović-kolonija | 97 | 9,353.200 | 96.400 | B |
| 8a1ea92c9aaffff | Novi Grad Sarajevo | Zabrđe | 40 | 3,857.500 | 96.400 | A |
| 8a1ef45b24f7fff | Novi Grad Sarajevo | Zabrđe | 24 | 2,314.600 | 96.400 | A |
| 8a1ea92c980ffff | Novi Grad Sarajevo | Zabrđe | 53 | 5,112.100 | 96.500 | A |
| 8a1ef45953a7fff | Novo Sarajevo | Pofalići I | 16 | 1,543.500 | 96.500 | B |
| 8a1ef458451ffff | Centar Sarajevo | Betanija | 10 | 964.700 | 96.500 | B |
| 8a1ef4582567fff | Centar Sarajevo | Koševsko Brdo | 111 | 10,710.000 | 96.500 | B |
| 8a1ef45966b7fff | Ilidža | Stupsko Brdo | 183 | 17,660.900 | 96.500 | B |
| 8a1ef459671ffff | Ilidža | Stupsko Brdo | 70 | 6,755.800 | 96.500 | B |
| 8a1ef459104ffff | Novo Sarajevo | Gornji Kovačići | 57 | 5,501.400 | 96.500 | B |
| 8a1ea92c9867fff | Novi Grad Sarajevo | Zabrđe | 61 | 5,887.900 | 96.500 | A |
| 8a1ef4582a67fff | Centar Sarajevo | Hrastovi-Mrkovići | 46 | 4,442.500 | 96.600 | B |
| 8a1ef45837a7fff | Stari Grad Sarajevo | Vratnik | 129 | 12,459.200 | 96.600 | A |
| 8a1ef4586d8ffff | Vogošća | Hotonj | 13 | 1,255.900 | 96.600 | B |
| 8a1ef459101ffff | Novo Sarajevo | Vraca | 70 | 6,763.400 | 96.600 | B |
| 8a1ef696594ffff | Ilidža | Naselje Bulevar | 108 | 10,435.700 | 96.600 | B |
| 8a1ef45b072ffff | Vogošća | Vogošća | 65 | 6,281.400 | 96.600 | B |
| 8a1ef458248ffff | Centar Sarajevo | Crni Vrh-Gorica | 106 | 10,244.600 | 96.600 | B |
| 8a1ef4594217fff | Novi Grad Sarajevo | Dolac | 80 | 7,739.200 | 96.700 | A |
| 8a1ef6965c0ffff | Ilidža | Ilidža | 233 | 22,542.300 | 96.700 | B |
| 8a1ef4595587fff | Novi Grad Sarajevo | Dolac | 95 | 9,193.400 | 96.800 | A |
| 8a1ef45b625ffff | Vogošća | Vogošća | 11 | 1,064.900 | 96.800 | B |
| 8a1ea92c9877fff | Novi Grad Sarajevo | Zabrđe | 63 | 6,100.700 | 96.800 | A |
| 8a1ef459548ffff | Novo Sarajevo | Pofalići II | 53 | 5,137.300 | 96.900 | B |
| 8a1ef4586417fff | Vogošća | Kobilja Glava | 45 | 4,362.400 | 96.900 | B |
| 8a1ef45825a7fff | Novo Sarajevo | Velešići | 75 | 7,274.300 | 97.000 | B |
| 8a1ef459cdb7fff | Centar Sarajevo | Skenderija-Podtekija | 128 | 12,417.300 | 97.000 | B |
| 8a1ea92cbc2ffff | Ilidža | Donji Doglodi | 106 | 10,302.900 | 97.200 | B |
| 8a1ef45b0657fff | Vogošća | Vogošća | 17 | 1,652.400 | 97.200 | B |
| 8a1ef459cc1ffff | Centar Sarajevo | Soukbunar | 67 | 6,515.400 | 97.200 | B |
| 8a1ef4595557fff | Novi Grad Sarajevo | Dolac | 53 | 5,155.600 | 97.300 | A |
| 8a1ef45864e7fff | Centar Sarajevo | Šip | 56 | 5,448.600 | 97.300 | B |
| 8a1ef45864effff | Centar Sarajevo | Šip | 62 | 6,033.200 | 97.300 | B |
| 8a1ef459665ffff | Novi Grad Sarajevo | Saraj Polje | 35 | 3,406.400 | 97.300 | A |
| 8a1ef4595207fff | Novo Sarajevo | Velešići | 45 | 4,379.700 | 97.300 | B |
| 8a1ea92c9967fff | Novi Grad Sarajevo | Zabrđe | 55 | 5,354.100 | 97.300 | A |
| 8a1ef459c18ffff | Stari Grad Sarajevo | Širokača | 80 | 7,789.700 | 97.400 | A |
| 8a1ea92c9b8ffff | Novi Grad Sarajevo | Zabrđe | 45 | 4,382.200 | 97.400 | A |
| 8a1ef45847affff | Centar Sarajevo | Betanija | 12 | 1,168.700 | 97.400 | B |
| 8a1ef45b251ffff | Novi Grad Sarajevo | Zabrđe | 38 | 3,701.200 | 97.400 | A |
| 8a1ef4590257fff | Novo Sarajevo | Hrasno Brdo | 68 | 6,623.600 | 97.400 | B |
| 8a1ef45b0ac7fff | Vogošća | Blagovac | 11 | 1,071.600 | 97.400 | B |
| 8a1ea92c3a67fff | Ilidža | Kakrinje | 11 | 1,071.700 | 97.400 | B |
| 8a1ea92cb6f7fff | Ilidža | Pejton | 17 | 1,656.400 | 97.400 | B |
| 8a1ef45942f7fff | Novi Grad Sarajevo | Dolac | 106 | 10,329.400 | 97.400 | A |
| 8a1ef458378ffff | Stari Grad Sarajevo | Vratnik | 100 | 9,745.700 | 97.500 | A |
| 8a1ef458642ffff | Centar Sarajevo | Šip | 47 | 4,582.100 | 97.500 | B |
| 8a1ef4592987fff | Novi Grad Sarajevo | Saraj Polje | 115 | 11,215.400 | 97.500 | A |
| 8a1ef45844cffff | Centar Sarajevo | Betanija | 17 | 1,658.000 | 97.500 | B |
| 8a1ef45955a7fff | Novi Grad Sarajevo | Dolac | 97 | 9,469.400 | 97.600 | A |
| 8a1ef4584127fff | Centar Sarajevo | Nahorevo | 11 | 1,073.900 | 97.600 | B |
| 8a1ef4583c6ffff | Stari Grad Sarajevo | Sedrenik | 67 | 6,541.200 | 97.600 | A |
| 8a1ef4595787fff | Novo Sarajevo | Pofalići II | 57 | 5,566.200 | 97.700 | B |
| 8a1ef4591327fff | Novo Sarajevo | Gornji Kovačići | 59 | 5,762.900 | 97.700 | B |
| 8a1ef4592c17fff | Novi Grad Sarajevo | Dobrinja A | 123 | 12,014.100 | 97.700 | A |
| 8a1ef459536ffff | Novo Sarajevo | Gornji Velešići | 44 | 4,297.900 | 97.700 | B |
| 8a1ef45b07a7fff | Vogošća | Vogošća | 22 | 2,149.900 | 97.700 | B |
| 8a1ef6960b9ffff | Ilidža | Sokolović-kolonija | 28 | 2,737.100 | 97.800 | B |
| 8a1ef45b250ffff | Novi Grad Sarajevo | Zabrđe | 46 | 4,498.000 | 97.800 | A |
| 8a1ef458371ffff | Stari Grad Sarajevo | Vratnik | 103 | 10,075.100 | 97.800 | A |
| 8a1ef45968cffff | Novi Grad Sarajevo | Briješće | 109 | 10,663.300 | 97.800 | A |
| 8a1ef4582d8ffff | Novo Sarajevo | Gornji Velešići | 50 | 4,892.100 | 97.800 | B |
| 8a1ef458202ffff | Centar Sarajevo | Park-Višnjik | 125 | 12,230.900 | 97.800 | B |
| 8a1ef459596ffff | Vogošća | Kobilja Glava | 15 | 1,468.800 | 97.900 | B |
| 8a1ef45b695ffff | Vogošća | Svrake | 13 | 1,273.100 | 97.900 | B |
| 8a1ef45966a7fff | Ilidža | Stupsko Brdo | 170 | 16,650.500 | 97.900 | B |
| 8a1ef4582d97fff | Novo Sarajevo | Velešići | 39 | 3,820.100 | 98.000 | B |
| 8a1ea92c9a27fff | Novi Grad Sarajevo | Zabrđe | 36 | 3,526.800 | 98.000 | A |
| 8a1ef4583c67fff | Stari Grad Sarajevo | Sedrenik | 66 | 6,467.400 | 98.000 | A |
| 8a1ef458681ffff | Centar Sarajevo | Betanija | 16 | 1,568.100 | 98.000 | B |
| 8a1ef4584517fff | Centar Sarajevo | Betanija | 11 | 1,078.300 | 98.000 | B |
| 8a1ef45836a7fff | Stari Grad Sarajevo | Vratnik | 65 | 6,372.400 | 98.000 | A |
| 8a1ef4583c4ffff | Stari Grad Sarajevo | Sedrenik | 72 | 7,061.600 | 98.100 | A |
| 8a1ef69651b7fff | Ilidža | Ilidža | 82 | 8,043.100 | 98.100 | B |
| 8a1ef45950f7fff | Novo Sarajevo | Pofalići II | 20 | 1,961.800 | 98.100 | B |
| 8a1ef45824d7fff | Centar Sarajevo | Crni Vrh-Gorica | 90 | 8,828.500 | 98.100 | B |
| 8a1ef45b24affff | Novi Grad Sarajevo | Zabrđe | 36 | 3,533.200 | 98.100 | A |
| 8a1ef4591a9ffff | Novo Sarajevo | Kovačići | 120 | 11,779.800 | 98.200 | B |
| 8a1ef4591727fff | Novo Sarajevo | Vraca | 51 | 5,006.600 | 98.200 | B |
| 8a1ef45955affff | Novi Grad Sarajevo | Dolac | 109 | 10,703.200 | 98.200 | A |
| 8a1ef458675ffff | Centar Sarajevo | Šip | 34 | 3,339.400 | 98.200 | B |
| 8a1ea92c9aeffff | Novi Grad Sarajevo | Zabrđe | 40 | 3,929.300 | 98.200 | A |
| 8a1ea92c9b07fff | Novi Grad Sarajevo | Zabrđe | 47 | 4,618.800 | 98.300 | A |
| 8a1ef45835affff | Stari Grad Sarajevo | Medrese | 133 | 13,074.500 | 98.300 | A |
| 8a1ef4592ceffff | Novi Grad Sarajevo | Dobrinja A | 123 | 12,092.000 | 98.300 | A |
| 8a1ef4590b27fff | Novo Sarajevo | Pofalići II | 64 | 6,292.900 | 98.300 | B |
| 8a1ef45862effff | Centar Sarajevo | Betanija | 11 | 1,081.700 | 98.300 | B |
| 8a1ef458316ffff | Stari Grad Sarajevo | Mošćanica | 14 | 1,376.800 | 98.300 | A |
| 8a1ef45942affff | Novi Grad Sarajevo | Dolac | 107 | 10,523.000 | 98.300 | A |
| 8a1ef4595427fff | Novi Grad Sarajevo | Dolac | 90 | 8,851.400 | 98.300 | A |
| 8a1ef459579ffff | Novo Sarajevo | Pofalići II | 60 | 5,901.400 | 98.400 | B |
| 8a1ea92cd2a7fff | Novi Grad Sarajevo | Zabrđe | 34 | 3,344.600 | 98.400 | A |
| 8a1ef459504ffff | Novo Sarajevo | Velešići | 21 | 2,066.300 | 98.400 | B |
| 8a1ef458691ffff | Centar Sarajevo | Betanija | 17 | 1,672.800 | 98.400 | B |
| 8a1ea92ebc6ffff | Novi Grad Sarajevo | Reljevo | 17 | 1,672.900 | 98.400 | A |
| 8a1ef45b2557fff | Novi Grad Sarajevo | Zabrđe | 16 | 1,575.500 | 98.500 | A |
| 8a1ef4582b67fff | Centar Sarajevo | Hrastovi-Mrkovići | 40 | 3,939.500 | 98.500 | B |
| 8a1ef45957b7fff | Novo Sarajevo | Pofalići II | 52 | 5,123.000 | 98.500 | B |
| 8a1ea92ddb97fff | Ilidža | Lipe | 14 | 1,379.300 | 98.500 | B |
| 8a1ea92c9a07fff | Novi Grad Sarajevo | Zabrđe | 48 | 4,732.200 | 98.600 | A |
| 8a1ef45b031ffff | Vogošća | Blagovac | 14 | 1,380.900 | 98.600 | B |
| 8a1ef6965517fff | Ilidža | Lužani | 30 | 2,959.700 | 98.700 | B |
| 8a1ef459c347fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 43 | 4,242.500 | 98.700 | A |
| 8a1ef6965ba7fff | Ilidža | Naselje Bulevar | 87 | 8,586.100 | 98.700 | B |
| 8a1ea92c9c57fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 139 | 13,723.600 | 98.700 | A |
| 8a1ef4595287fff | Novo Sarajevo | Pofalići I | 67 | 6,617.400 | 98.800 | B |
| 8a1ea92c994ffff | Novi Grad Sarajevo | Zabrđe | 62 | 6,123.800 | 98.800 | A |
| 8a1ef45b0cdffff | Vogošća | Vogošća | 12 | 1,185.400 | 98.800 | B |
| 8a1ef459c08ffff | Stari Grad Sarajevo | Širokača | 64 | 6,323.400 | 98.800 | A |
| 8a1ef4595637fff | Novo Sarajevo | Pofalići II | 59 | 5,831.800 | 98.800 | B |
| 8a1ef45b0397fff | Vogošća | Blagovac | 17 | 1,680.500 | 98.900 | B |
| 8a1ef45b39affff | Vogošća | Vogošća | 14 | 1,384.100 | 98.900 | B |
| 8a1ef45826a7fff | Centar Sarajevo | Trg oslobođenja-Centar | 132 | 13,052.600 | 98.900 | B |
| 8a1ef45834f7fff | Stari Grad Sarajevo | Kovači | 74 | 7,317.400 | 98.900 | A |
| 8a1ef459145ffff | Novo Sarajevo | Vraca | 42 | 4,154.000 | 98.900 | B |
| 8a1ef458272ffff | Centar Sarajevo | Park-Višnjik | 102 | 10,090.900 | 98.900 | B |
| 8a1ef4586797fff | Centar Sarajevo | Šip | 61 | 6,035.500 | 98.900 | B |
| 8a1ea92c9847fff | Novi Grad Sarajevo | Zabrđe | 71 | 7,026.200 | 99.000 | A |
| 8a1ef696581ffff | Ilidža | Ilidža | 15 | 1,484.800 | 99.000 | B |
| 8a1ef4596987fff | Novi Grad Sarajevo | Briješće | 15 | 1,485.300 | 99.000 | A |
| 8a1ea92cb247fff | Ilidža | Azići | 97 | 9,606.700 | 99.000 | B |
| 8a1ef4586cdffff | Vogošća | Kobilja Glava | 12 | 1,188.700 | 99.100 | B |
| 8a1ea92c9a0ffff | Novi Grad Sarajevo | Zabrđe | 39 | 3,863.600 | 99.100 | A |
| 8a1ef459420ffff | Novi Grad Sarajevo | Dolac | 117 | 11,592.500 | 99.100 | A |
| 8a1ef45848d7fff | Centar Sarajevo | Nahorevo | 14 | 1,387.500 | 99.100 | B |
| 8a1ef4593957fff | Novo Sarajevo | Hrasno Brdo | 30 | 2,973.500 | 99.100 | B |
| 8a1ef4582547fff | Centar Sarajevo | Koševsko Brdo | 148 | 14,670.300 | 99.100 | B |
| 8a1ef45804effff | Centar Sarajevo | Pionirska Dolina | 34 | 3,370.300 | 99.100 | B |
| 8a1ef45868effff | Centar Sarajevo | Betanija | 13 | 1,289.600 | 99.200 | B |
| 8a1ef4582977fff | Centar Sarajevo | Betanija | 50 | 4,960.100 | 99.200 | B |
| 8a1ea92c995ffff | Novi Grad Sarajevo | Zabrđe | 76 | 7,541.300 | 99.200 | A |
| 8a1ef459550ffff | Novi Grad Sarajevo | Dolac | 82 | 8,137.700 | 99.200 | A |
| 8a1ef4591587fff | Novo Sarajevo | Hrasno Brdo | 55 | 5,458.600 | 99.200 | B |
| 8a1ef4582c07fff | Novo Sarajevo | Gornji Velešići | 78 | 7,742.600 | 99.300 | B |
| 8a1ef459c577fff | Stari Grad Sarajevo | Širokača | 40 | 3,971.000 | 99.300 | A |
| 8a1ef4582af7fff | Centar Sarajevo | Breka | 72 | 7,150.300 | 99.300 | B |
| 8a1ef4583167fff | Stari Grad Sarajevo | Mošćanica | 11 | 1,093.200 | 99.400 | A |
| 8a1ef6960b2ffff | Ilidža | Sokolović-kolonija | 155 | 15,410.100 | 99.400 | B |
| 8a1ef45b256ffff | Novi Grad Sarajevo | Zabrđe | 17 | 1,691.600 | 99.500 | A |
| 8a1ef45827a7fff | Centar Sarajevo | Crni Vrh-Gorica | 91 | 9,055.000 | 99.500 | B |
| 8a1ef45b38a7fff | Vogošća | Ugorsko | 11 | 1,094.600 | 99.500 | B |
| 8a1ef459421ffff | Novi Grad Sarajevo | Dolac | 131 | 13,036.500 | 99.500 | A |
| 8a1ef4595a57fff | Novo Sarajevo | Gornji Velešići | 23 | 2,289.900 | 99.600 | B |
| 8a1ef45b3d77fff | Vogošća | Uglješići | 10 | 995.700 | 99.600 | B |
| 8a1ef6961b37fff | Ilidža | Donji Kotorac | 10 | 995.700 | 99.600 | B |
| 8a1ef459535ffff | Novo Sarajevo | Velešići | 53 | 5,278.600 | 99.600 | B |
| 8a1ef45952e7fff | Novo Sarajevo | Velešići | 68 | 6,772.900 | 99.600 | B |
| 8a1ef45910affff | Novo Sarajevo | Vraca | 76 | 7,572.300 | 99.600 | B |
| 8a1ef4582a07fff | Centar Sarajevo | Hrastovi-Mrkovići | 58 | 5,780.600 | 99.700 | B |
| 8a1ea92c3cc7fff | Ilidža | Rakovica | 13 | 1,295.700 | 99.700 | B |
| 8a1ef6965977fff | Ilidža | Naselje Bulevar | 42 | 4,187.400 | 99.700 | B |
| 8a1ef45b2c57fff | Vogošća | Krivoglavci | 32 | 3,190.600 | 99.700 | B |
| 8a1ef45952dffff | Novo Sarajevo | Pofalići I | 74 | 7,378.400 | 99.700 | B |
| 8a1ef4595aaffff | Novo Sarajevo | Velešići | 20 | 1,994.200 | 99.700 | B |
| 8a1ef4580517fff | Centar Sarajevo | Pionirska Dolina | 43 | 4,289.100 | 99.700 | B |
| 8a1ef459dc07fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 41 | 4,089.800 | 99.800 | A |
| 8a1ef45827affff | Centar Sarajevo | Džidžikovac-Koševo I | 109 | 10,881.000 | 99.800 | B |
| 8a1ef459dc8ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 23 | 2,296.800 | 99.900 | A |
| 8a1ef459c097fff | Stari Grad Sarajevo | Širokača | 39 | 3,897.500 | 99.900 | A |
| 8a1ef4591257fff | Centar Sarajevo | Soukbunar | 15 | 1,499.200 | 99.900 | B |
| 8a1ef4595b07fff | Novo Sarajevo | Velešići | 13 | 1,299.400 | 100.000 | B |
| 8a1ef459528ffff | Novo Sarajevo | Pofalići I | 74 | 7,401.500 | 100.000 | B |
| 8a1ef4583c2ffff | Stari Grad Sarajevo | Sedrenik | 80 | 8,002.300 | 100.000 | A |
| 8a1ef459576ffff | Novo Sarajevo | Pofalići I | 59 | 5,901.900 | 100.000 | B |
| 8a1ef4586477fff | Centar Sarajevo | Šip | 55 | 5,504.100 | 100.100 | B |
| 8a1ef45837affff | Stari Grad Sarajevo | Vratnik | 108 | 10,820.600 | 100.200 | A |
| 8a1ea92c984ffff | Novi Grad Sarajevo | Zabrđe | 61 | 6,111.800 | 100.200 | A |
| 8a1ea92cb24ffff | Ilidža | Azići | 172 | 17,237.900 | 100.200 | B |
| 8a1ef4596557fff | Ilidža | Stup | 148 | 14,834.200 | 100.200 | B |
| 8a1ef6960027fff | Ilidža | Kovači (Ilidža) | 27 | 2,706.600 | 100.200 | B |
| 8a1ef45b20f7fff | Novi Grad Sarajevo | Zabrđe | 16 | 1,605.400 | 100.300 | A |
| 8a1ea92c9a57fff | Novi Grad Sarajevo | Zabrđe | 48 | 4,816.700 | 100.300 | A |
| 8a1ef6965927fff | Ilidža | Azići | 103 | 10,337.000 | 100.400 | B |
| 8a1ea92c9a5ffff | Novi Grad Sarajevo | Zabrđe | 35 | 3,513.300 | 100.400 | A |
| 8a1ea92c9ba7fff | Novi Grad Sarajevo | Zabrđe | 66 | 6,625.800 | 100.400 | A |
| 8a1ef4594ca7fff | Novi Grad Sarajevo | Zabrđe | 19 | 1,907.600 | 100.400 | A |
| 8a1ea92c986ffff | Novi Grad Sarajevo | Zabrđe | 68 | 6,829.200 | 100.400 | A |
| 8a1ef4595a8ffff | Novo Sarajevo | Velešići | 16 | 1,606.900 | 100.400 | B |
| 8a1ea92c9ae7fff | Novi Grad Sarajevo | Zabrđe | 42 | 4,219.300 | 100.500 | A |
| 8a1ef4591a4ffff | Centar Sarajevo | Skenderija-Podtekija | 85 | 8,539.400 | 100.500 | B |
| 8a1ef459010ffff | Novi Grad Sarajevo | Alipašin Most III | 107 | 10,750.800 | 100.500 | A |
| 8a1ef459564ffff | Novo Sarajevo | Pofalići I | 72 | 7,235.500 | 100.500 | B |
| 8a1ef45838affff | Stari Grad Sarajevo | Sedrenik | 23 | 2,313.800 | 100.600 | A |
| 8a1ef459ccd7fff | Centar Sarajevo | Soukbunar | 71 | 7,143.100 | 100.600 | B |
| 8a1ef6965d0ffff | Ilidža | Pejton | 122 | 12,280.500 | 100.700 | B |
| 8a1ef4586d97fff | Vogošća | Hotonj | 13 | 1,309.000 | 100.700 | B |
| 8a1ef459c26ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 19 | 1,913.600 | 100.700 | A |
| 8a1ef6965887fff | Ilidža | Ilidža | 17 | 1,712.300 | 100.700 | B |
| 8a1ef459140ffff | Novo Sarajevo | Vraca | 58 | 5,842.200 | 100.700 | B |
| 8a1ef4591397fff | Novo Sarajevo | Gornji Kovačići | 46 | 4,634.400 | 100.700 | B |
| 8a1ef4582c77fff | Centar Sarajevo | Koševsko Brdo | 107 | 10,782.700 | 100.800 | B |
| 8a1ef45b045ffff | Vogošća | Vogošća | 106 | 10,686.800 | 100.800 | B |
| 8a1ea92c961ffff | Novi Grad Sarajevo | Briješće | 12 | 1,210.400 | 100.900 | A |
| 8a1ef4595317fff | Novo Sarajevo | Velešići | 24 | 2,421.200 | 100.900 | B |
| 8a1ea92c9baffff | Novi Grad Sarajevo | Zabrđe | 71 | 7,163.200 | 100.900 | A |
| 8a1ef4594d87fff | Novi Grad Sarajevo | Zabrđe | 29 | 2,928.200 | 101.000 | A |
| 8a1ef45952b7fff | Novo Sarajevo | Pofalići I | 69 | 6,967.300 | 101.000 | B |
| 8a1ef458262ffff | Centar Sarajevo | Džidžikovac-Koševo I | 166 | 16,763.300 | 101.000 | B |
| 8a1ef4580b37fff | Centar Sarajevo | Betanija | 18 | 1,818.000 | 101.000 | B |
| 8a1ef6964a6ffff | Ilidža | Pejton | 187 | 18,893.400 | 101.000 | B |
| 8a1ef459142ffff | Novo Sarajevo | Vraca | 67 | 6,773.900 | 101.100 | B |
| 8a1ef4591237fff | Novo Sarajevo | Gornji Kovačići | 34 | 3,438.700 | 101.100 | B |
| 8a1ef69654dffff | Ilidža | Sokolović-kolonija | 233 | 23,566.200 | 101.100 | B |
| 8a1ea92cd62ffff | Novi Grad Sarajevo | Zabrđe | 30 | 3,034.500 | 101.200 | A |
| 8a1ef696426ffff | Ilidža | Lužani | 109 | 11,036.000 | 101.200 | B |
| 8a1ef4595b67fff | Centar Sarajevo | Šip | 54 | 5,470.400 | 101.300 | B |
| 8a1ef4595217fff | Novo Sarajevo | Pofalići I | 64 | 6,483.500 | 101.300 | B |
| 8a1ef45b3817fff | Vogošća | Ugorsko | 19 | 1,924.800 | 101.300 | B |
| 8a1ef4595737fff | Novo Sarajevo | Pofalići II | 34 | 3,445.100 | 101.300 | B |
| 8a1ea92ca357fff | Ilidža | Osjek | 18 | 1,824.900 | 101.400 | B |
| 8a1ef45952affff | Novo Sarajevo | Pofalići I | 73 | 7,403.400 | 101.400 | B |
| 8a1ef45954effff | Novo Sarajevo | Pofalići II | 41 | 4,158.600 | 101.400 | B |
| 8a1ea92eb08ffff | Novi Grad Sarajevo | Reljevo | 10 | 1,014.400 | 101.400 | A |
| 8a1ef4591ad7fff | Novo Sarajevo | Kovačići | 83 | 8,419.700 | 101.400 | B |
| 8a1ef4583287fff | Stari Grad Sarajevo | Mošćanica | 14 | 1,420.300 | 101.500 | A |
| 8a1ef458222ffff | Centar Sarajevo | Bardakčije | 87 | 8,826.700 | 101.500 | B |
| 8a1ef45a35b7fff | Centar Sarajevo | Nahorevo | 10 | 1,014.600 | 101.500 | B |
| 8a1ea92c90dffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 27 | 2,739.800 | 101.500 | A |
| 8a1ea92cd5affff | Novi Grad Sarajevo | Dobroševići | 11 | 1,116.200 | 101.500 | A |
| 8a1ef45957affff | Novo Sarajevo | Pofalići II | 60 | 6,090.000 | 101.500 | B |
| 8a1ef4594db7fff | Novi Grad Sarajevo | Zabrđe | 50 | 5,075.800 | 101.500 | A |
| 8a1ea92d9b6ffff | Ilidža | Blažuj | 33 | 3,353.300 | 101.600 | B |
| 8a1ea92c9a37fff | Novi Grad Sarajevo | Zabrđe | 67 | 6,810.300 | 101.600 | A |
| 8a1ef458256ffff | Centar Sarajevo | Koševsko Brdo | 163 | 16,568.600 | 101.600 | B |
| 8a1ef696398ffff | Ilidža | Hrasnica | 56 | 5,692.700 | 101.700 | B |
| 8a1ef45b2767fff | Novi Grad Sarajevo | Zabrđe | 14 | 1,423.300 | 101.700 | A |
| 8a1ef4582b9ffff | Centar Sarajevo | Breka | 107 | 10,880.400 | 101.700 | B |
| 8a1ef4596117fff | Novi Grad Sarajevo | Briješće | 100 | 10,170.800 | 101.700 | A |
| 8a1ef45834affff | Stari Grad Sarajevo | Kovači | 86 | 8,748.800 | 101.700 | A |
| 8a1ef459674ffff | Novi Grad Sarajevo | Saraj Polje | 74 | 7,528.200 | 101.700 | A |
| 8a1ef6961aa7fff | Ilidža | Donji Kotorac | 46 | 4,681.100 | 101.800 | B |
| 8a1ea92c9d47fff | Novi Grad Sarajevo | Zabrđe | 51 | 5,192.100 | 101.800 | A |
| 8a1ef45952a7fff | Novo Sarajevo | Pofalići I | 68 | 6,923.400 | 101.800 | B |
| 8a1ea92cba97fff | Ilidža | Doglodi | 79 | 8,045.200 | 101.800 | B |
| 8a1ef45824cffff | Centar Sarajevo | Crni Vrh-Gorica | 85 | 8,656.500 | 101.800 | B |
| 8a1ef4582caffff | Novo Sarajevo | Gornji Velešići | 69 | 7,029.800 | 101.900 | B |
| 8a1ef696588ffff | Ilidža | Ilidža | 86 | 8,762.900 | 101.900 | B |
| 8a1ef459c817fff | Stari Grad Sarajevo | Ferhadija | 132 | 13,452.100 | 101.900 | A |
| 8a1ea92cc60ffff | Novi Grad Sarajevo | Dobroševići | 16 | 1,630.700 | 101.900 | A |
| 8a1ea92c9007fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 24 | 2,446.100 | 101.900 | A |
| 8a1ef459525ffff | Novo Sarajevo | Velešići | 85 | 8,663.600 | 101.900 | B |
| 8a1ef4582cdffff | Centar Sarajevo | Koševsko Brdo | 193 | 19,672.500 | 101.900 | B |
| 8a1ef459126ffff | Centar Sarajevo | Soukbunar | 44 | 4,485.100 | 101.900 | B |
| 8a1ef459c10ffff | Stari Grad Sarajevo | Toka-Džeka | 127 | 12,949.000 | 102.000 | A |
| 8a1ea92c9aa7fff | Novi Grad Sarajevo | Zabrđe | 74 | 7,553.700 | 102.100 | A |
| 8a1ef4582c87fff | Novo Sarajevo | Gornji Velešići | 67 | 6,840.000 | 102.100 | B |
| 8a1ef45821b7fff | Centar Sarajevo | Koševsko Brdo | 111 | 11,337.700 | 102.100 | B |
| 8a1ef45910f7fff | Novo Sarajevo | Vraca | 75 | 7,662.700 | 102.200 | B |
| 8a1ef45915b7fff | Novo Sarajevo | Hrasno Brdo | 65 | 6,642.500 | 102.200 | B |
| 8a1ef45965affff | Ilidža | Stup | 76 | 7,768.900 | 102.200 | B |
| 8a1ef45b696ffff | Vogošća | Semizovac | 14 | 1,431.100 | 102.200 | B |
| 8a1ef459c077fff | Stari Grad Sarajevo | Toka-Džeka | 94 | 9,613.300 | 102.300 | A |
| 8a1ef45b0447fff | Vogošća | Vogošća | 101 | 10,331.900 | 102.300 | B |
| 8a1ef458344ffff | Stari Grad Sarajevo | Vratnik | 127 | 12,994.100 | 102.300 | A |
| 8a1ea92c9c47fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 170 | 17,395.800 | 102.300 | A |
| 8a1ef4586787fff | Centar Sarajevo | Šip | 73 | 7,471.100 | 102.300 | B |
| 8a1ef4596c2ffff | Novi Grad Sarajevo | Briješće | 13 | 1,331.200 | 102.400 | A |
| 8a1ef4582d1ffff | Novo Sarajevo | Gornji Velešići | 63 | 6,454.100 | 102.400 | B |
| 8a1ef45952f7fff | Novo Sarajevo | Pofalići I | 76 | 7,787.400 | 102.500 | B |
| 8a1ef4593967fff | Novo Sarajevo | Hrasno Brdo | 56 | 5,743.200 | 102.600 | B |
| 8a1ea92cb687fff | Ilidža | Pejton | 15 | 1,538.600 | 102.600 | B |
| 8a1ef6965ce7fff | Ilidža | Ilidža | 134 | 13,746.200 | 102.600 | B |
| 8a1ef459c98ffff | Centar Sarajevo | Trg oslobođenja-Centar | 198 | 20,311.700 | 102.600 | B |
| 8a1ef6960b0ffff | Ilidža | Sokolović-kolonija | 147 | 15,091.800 | 102.700 | B |
| 8a1ef458492ffff | Centar Sarajevo | Nahorevo | 12 | 1,232.000 | 102.700 | B |
| 8a1ef458255ffff | Centar Sarajevo | Koševsko Brdo | 111 | 11,396.900 | 102.700 | B |
| 8a1ef4591477fff | Novo Sarajevo | Vraca | 66 | 6,777.000 | 102.700 | B |
| 8a1ef4582d6ffff | Centar Sarajevo | Koševsko Brdo | 62 | 6,367.400 | 102.700 | B |
| 8a1ef4582c97fff | Novo Sarajevo | Gornji Velešići | 75 | 7,702.800 | 102.700 | B |
| 8a1ef458231ffff | Centar Sarajevo | Bardakčije | 145 | 14,893.000 | 102.700 | B |
| 8a1ef459cd8ffff | Centar Sarajevo | Soukbunar | 131 | 13,455.500 | 102.700 | B |
| 8a1ef4582927fff | Centar Sarajevo | Betanija | 36 | 3,698.400 | 102.700 | B |
| 8a1ef4582357fff | Centar Sarajevo | Bardakčije | 78 | 8,013.300 | 102.700 | B |
| 8a1ef4582807fff | Centar Sarajevo | Betanija | 97 | 9,965.700 | 102.700 | B |
| 8a1ef6964c77fff | Ilidža | Plandište | 20 | 2,054.900 | 102.700 | B |
| 8a1ef4580627fff | Centar Sarajevo | Hrastovi-Mrkovići | 10 | 1,027.800 | 102.800 | B |
| 8a1ef459025ffff | Novo Sarajevo | Hrasno Brdo | 79 | 8,120.100 | 102.800 | B |
| 8a1ea92c9b87fff | Novi Grad Sarajevo | Zabrđe | 51 | 5,242.500 | 102.800 | A |
| 8a1ef4591387fff | Novo Sarajevo | Gornji Kovačići | 51 | 5,242.500 | 102.800 | B |
| 8a1ef4592d1ffff | Novi Grad Sarajevo | Dobrinja A | 55 | 5,655.200 | 102.800 | A |
| 8a1ef459cb17fff | Stari Grad Sarajevo | Bistrik | 258 | 26,534.100 | 102.800 | A |
| 8a1ef4595357fff | Novo Sarajevo | Velešići | 42 | 4,321.300 | 102.900 | B |
| 8a1ef45b2477fff | Novi Grad Sarajevo | Zabrđe | 46 | 4,733.100 | 102.900 | A |
| 8a1ef458284ffff | Centar Sarajevo | Koševo II | 64 | 6,586.000 | 102.900 | B |
| 8a1ef6963937fff | Ilidža | Kovači (Ilidža) | 25 | 2,572.900 | 102.900 | B |
| 8a1ef45826f7fff | Centar Sarajevo | Trg oslobođenja-Centar | 152 | 15,645.700 | 102.900 | B |
| 8a1ef458636ffff | Centar Sarajevo | Betanija | 11 | 1,132.500 | 103.000 | B |
| 8a1ef4595727fff | Novo Sarajevo | Pofalići II | 42 | 4,327.200 | 103.000 | B |
| 8a1ef4582787fff | Centar Sarajevo | Crni Vrh-Gorica | 104 | 10,715.000 | 103.000 | B |
| 8a1ef4584107fff | Centar Sarajevo | Nahorevo | 16 | 1,648.500 | 103.000 | B |
| 8a1ea92cd057fff | Novi Grad Sarajevo | Reljevo | 12 | 1,236.500 | 103.000 | A |
| 8a1ef4586707fff | Centar Sarajevo | Šip | 107 | 11,026.800 | 103.100 | B |
| 8a1ef4591097fff | Novo Sarajevo | Vraca | 79 | 8,142.800 | 103.100 | B |
| 8a1ef45b058ffff | Vogošća | Vogošća | 13 | 1,340.100 | 103.100 | B |
| 8a1ef4583aeffff | Stari Grad Sarajevo | Mošćanica | 13 | 1,340.400 | 103.100 | A |
| 8a1ef4591317fff | Novo Sarajevo | Gornji Kovačići | 69 | 7,114.500 | 103.100 | B |
| 8a1ef459121ffff | Novo Sarajevo | Gornji Kovačići | 23 | 2,371.600 | 103.100 | B |
| 8a1ef4586247fff | Centar Sarajevo | Betanija | 25 | 2,578.300 | 103.100 | B |
| 8a1ef459c00ffff | Stari Grad Sarajevo | Toka-Džeka | 87 | 8,973.000 | 103.100 | A |
| 8a1ef696184ffff | Ilidža | Donji Kotorac | 45 | 4,642.400 | 103.200 | B |
| 8a1ea92cb16ffff | Ilidža | Doglodi | 36 | 3,714.500 | 103.200 | B |
| 8a1ef459681ffff | Novi Grad Sarajevo | Briješće | 17 | 1,754.500 | 103.200 | A |
| 8a1ef45950cffff | Novo Sarajevo | Pofalići I | 48 | 4,955.300 | 103.200 | B |
| 8a1ea92c905ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 70 | 7,227.900 | 103.300 | A |
| 8a1ef45b6b0ffff | Vogošća | Ljubina-Poturovići | 13 | 1,343.200 | 103.300 | B |
| 8a1ef458409ffff | Centar Sarajevo | Nahorevo | 18 | 1,861.200 | 103.400 | B |
| 8a1ef45b14effff | Vogošća | Hotonj | 15 | 1,551.300 | 103.400 | B |
| 8a1ef4586967fff | Centar Sarajevo | Betanija | 11 | 1,137.700 | 103.400 | B |
| 8a1ef45915affff | Novo Sarajevo | Hrasno Brdo | 73 | 7,551.600 | 103.400 | B |
| 8a1ef45847a7fff | Centar Sarajevo | Betanija | 14 | 1,448.300 | 103.400 | B |
| 8a1ef4586a5ffff | Centar Sarajevo | Betanija | 17 | 1,759.600 | 103.500 | B |
| 8a1ef45966affff | Novi Grad Sarajevo | Saraj Polje | 32 | 3,312.300 | 103.500 | A |
| 8a1ef45b01a7fff | Vogošća | Vogošća | 11 | 1,138.600 | 103.500 | B |
| 8a1ef4592d0ffff | Novi Grad Sarajevo | Dobrinja A | 51 | 5,282.100 | 103.600 | A |
| 8a1ef45968a7fff | Novi Grad Sarajevo | Briješće | 14 | 1,450.200 | 103.600 | A |
| 8a1ef459cc8ffff | Centar Sarajevo | Soukbunar | 64 | 6,630.700 | 103.600 | B |
| 8a1ef4591457fff | Novo Sarajevo | Vraca | 63 | 6,527.400 | 103.600 | B |
| 8a1ef4595297fff | Novo Sarajevo | Pofalići I | 89 | 9,221.300 | 103.600 | B |
| 8a1ef4584927fff | Centar Sarajevo | Nahorevo | 22 | 2,280.000 | 103.600 | B |
| 8a1ef459529ffff | Novo Sarajevo | Pofalići I | 91 | 9,433.800 | 103.700 | B |
| 8a1ef4591057fff | Novo Sarajevo | Grbavica I | 82 | 8,501.900 | 103.700 | B |
| 8a1ef4582777fff | Centar Sarajevo | Mejtaš-Bjelave | 168 | 17,424.100 | 103.700 | B |
| 8a1ef459526ffff | Novo Sarajevo | Velešići | 83 | 8,610.300 | 103.700 | B |
| 8a1ea92c96e7fff | Novi Grad Sarajevo | Briješće | 14 | 1,452.400 | 103.700 | A |
| 8a1ef458296ffff | Centar Sarajevo | Koševo II | 98 | 10,167.700 | 103.800 | B |
| 8a1ef6965d17fff | Ilidža | Pejton | 155 | 16,084.300 | 103.800 | B |
| 8a1ef45910effff | Novo Sarajevo | Vraca | 70 | 7,265.700 | 103.800 | B |
| 8a1ef4582267fff | Stari Grad Sarajevo | Logavina | 144 | 14,947.100 | 103.800 | A |
| 8a1ef45b381ffff | Vogošća | Ugorsko | 15 | 1,557.100 | 103.800 | B |
| 8a1ef4582337fff | Centar Sarajevo | Park-Višnjik | 99 | 10,277.300 | 103.800 | B |
| 8a1ef45914effff | Novo Sarajevo | Vraca | 21 | 2,180.200 | 103.800 | B |
| 8a1ea92e925ffff | Vogošća | Semizovac | 20 | 2,077.300 | 103.900 | B |
| 8a1ef459ccaffff | Centar Sarajevo | Soukbunar | 71 | 7,374.700 | 103.900 | B |
| 8a1ef459538ffff | Novo Sarajevo | Pofalići I | 60 | 6,235.400 | 103.900 | B |
| 8a1ea92cd677fff | Novi Grad Sarajevo | Zabrđe | 55 | 5,717.800 | 104.000 | A |
| 8a1ef4585737fff | Centar Sarajevo | Betanija | 15 | 1,559.600 | 104.000 | B |
| 8a1ef45b6157fff | Vogošća | Krivoglavci | 12 | 1,247.700 | 104.000 | B |
| 8a1ef45912affff | Novo Sarajevo | Gornji Kovačići | 26 | 2,703.500 | 104.000 | B |
| 8a1ef4595a27fff | Centar Sarajevo | Šip | 28 | 2,911.600 | 104.000 | B |
| 8a1ef459158ffff | Novo Sarajevo | Vraca | 65 | 6,759.600 | 104.000 | B |
| 8a1ef459134ffff | Centar Sarajevo | Soukbunar | 65 | 6,762.100 | 104.000 | B |
| 8a1ef4582067fff | Centar Sarajevo | Koševo II | 75 | 7,804.300 | 104.100 | B |
| 8a1ea92e9207fff | Vogošća | Semizovac | 12 | 1,249.400 | 104.100 | B |
| 8a1ef4586ae7fff | Centar Sarajevo | Betanija | 18 | 1,875.200 | 104.200 | B |
| 8a1ef45864f7fff | Centar Sarajevo | Šip | 53 | 5,526.500 | 104.300 | B |
| 8a1ef4582877fff | Centar Sarajevo | Koševo II | 66 | 6,882.200 | 104.300 | B |
| 8a1ef458662ffff | Centar Sarajevo | Šip | 82 | 8,552.900 | 104.300 | B |
| 8a1ef45b07b7fff | Vogošća | Vogošća | 21 | 2,190.600 | 104.300 | B |
| 8a1ef459539ffff | Novo Sarajevo | Pofalići I | 64 | 6,676.600 | 104.300 | B |
| 8a1ef459566ffff | Novo Sarajevo | Pofalići I | 103 | 10,747.600 | 104.300 | B |
| 8a1ef459065ffff | Novo Sarajevo | Hrasno Brdo | 73 | 7,617.800 | 104.400 | B |
| 8a1ea92cb2f7fff | Ilidža | Azići | 15 | 1,565.300 | 104.400 | B |
| 8a1ef4596787fff | Ilidža | Stupsko Brdo | 144 | 15,030.000 | 104.400 | B |
| 8a1ef4582217fff | Centar Sarajevo | Bardakčije | 134 | 13,988.500 | 104.400 | B |
| 8a1ef459cc87fff | Centar Sarajevo | Soukbunar | 77 | 8,038.300 | 104.400 | B |
| 8a1ef459dc37fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 37 | 3,863.400 | 104.400 | A |
| 8a1ea92c9ccffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 118 | 12,322.100 | 104.400 | A |
| 8a1ef4583137fff | Stari Grad Sarajevo | Sedrenik | 72 | 7,525.300 | 104.500 | A |
| 8a1ea92cd2affff | Novi Grad Sarajevo | Zabrđe | 157 | 16,409.500 | 104.500 | A |
| 8a1ef4582ca7fff | Novo Sarajevo | Gornji Velešići | 78 | 8,153.300 | 104.500 | B |
| 8a1ef459c86ffff | Stari Grad Sarajevo | Baščaršija | 109 | 11,394.000 | 104.500 | A |
| 8a1ef45b382ffff | Vogošća | Hotonj | 20 | 2,090.700 | 104.500 | B |
| 8a1ef4591407fff | Novo Sarajevo | Vraca | 71 | 7,424.800 | 104.600 | B |
| 8a1ef4582537fff | Novo Sarajevo | Velešići | 95 | 9,937.700 | 104.600 | B |
| 8a1ef4585477fff | Centar Sarajevo | Betanija | 11 | 1,150.900 | 104.600 | B |
| 8a1ef4586cd7fff | Vogošća | Kobilja Glava | 20 | 2,092.600 | 104.600 | B |
| 8a1ef6964baffff | Ilidža | Vreoca | 97 | 10,149.400 | 104.600 | B |
| 8a1ea92cd75ffff | Novi Grad Sarajevo | Zabrđe | 99 | 10,361.500 | 104.700 | A |
| 8a1ef45914a7fff | Novo Sarajevo | Hrasno Brdo | 59 | 6,177.600 | 104.700 | B |
| 8a1ef4591217fff | Novo Sarajevo | Gornji Kovačići | 31 | 3,246.200 | 104.700 | B |
| 8a1ea92cb30ffff | Ilidža | Azići | 83 | 8,691.400 | 104.700 | B |
| 8a1ef458240ffff | Centar Sarajevo | Koševsko Brdo | 132 | 13,822.500 | 104.700 | B |
| 8a1ef45804dffff | Centar Sarajevo | Hrastovi-Mrkovići | 42 | 4,398.700 | 104.700 | B |
| 8a1ef4594417fff | Novi Grad Sarajevo | Briješće | 22 | 2,304.400 | 104.700 | A |
| 8a1ef4582677fff | Centar Sarajevo | Mejtaš-Bjelave | 139 | 14,560.200 | 104.700 | B |
| 8a1ef45b2187fff | Novi Grad Sarajevo | Zabrđe | 36 | 3,771.600 | 104.800 | A |
| 8a1ef4592d6ffff | Novi Grad Sarajevo | Saraj Polje | 39 | 4,086.600 | 104.800 | A |
| 8a1ef45828cffff | Centar Sarajevo | Koševo II | 94 | 9,854.800 | 104.800 | B |
| 8a1ef4582187fff | Centar Sarajevo | Ciglane | 98 | 10,278.900 | 104.900 | B |
| 8a1ef458232ffff | Centar Sarajevo | Bardakčije | 85 | 8,915.900 | 104.900 | B |
| 8a1ef4583737fff | Stari Grad Sarajevo | Vratnik | 108 | 11,329.200 | 104.900 | A |
| 8a1ef45902effff | Novo Sarajevo | Hrasno Brdo | 81 | 8,498.100 | 104.900 | B |
| 8a1ef459534ffff | Novo Sarajevo | Velešići | 70 | 7,344.400 | 104.900 | B |
| 8a1ef45956b7fff | Novo Sarajevo | Pofalići II | 89 | 9,339.000 | 104.900 | B |
| 8a1ea92c9157fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 30 | 3,148.200 | 104.900 | A |
| 8a1ef45902dffff | Novo Sarajevo | Hrasno Brdo | 64 | 6,718.500 | 105.000 | B |
| 8a1ef6965d5ffff | Ilidža | Ilidža | 70 | 7,351.200 | 105.000 | B |
| 8a1ef45906effff | Novo Sarajevo | Hrasno Brdo | 56 | 5,884.800 | 105.100 | B |
| 8a1ef459699ffff | Novi Grad Sarajevo | Briješće | 36 | 3,783.700 | 105.100 | A |
| 8a1ef459cc9ffff | Centar Sarajevo | Soukbunar | 62 | 6,518.500 | 105.100 | B |
| 8a1ef4595347fff | Novo Sarajevo | Velešići | 59 | 6,204.500 | 105.200 | B |
| 8a1ef4595757fff | Novo Sarajevo | Pofalići II | 81 | 8,518.300 | 105.200 | B |
| 8a1ef4591437fff | Novo Sarajevo | Hrasno Brdo | 73 | 7,679.000 | 105.200 | B |
| 8a1ef45b052ffff | Vogošća | Vogošća | 12 | 1,262.400 | 105.200 | B |
| 8a1ef45913b7fff | Novo Sarajevo | Gornji Kovačići | 74 | 7,785.500 | 105.200 | B |
| 8a1ef4582ab7fff | Centar Sarajevo | Breka | 182 | 19,150.000 | 105.200 | B |
| 8a1ef45b040ffff | Vogošća | Vogošća | 154 | 16,206.800 | 105.200 | B |
| 8a1ef45957a7fff | Novo Sarajevo | Pofalići II | 66 | 6,947.800 | 105.300 | B |
| 8a1ef4591b27fff | Centar Sarajevo | Crni Vrh-Gorica | 268 | 28,218.000 | 105.300 | B |
| 8a1ef4591307fff | Novo Sarajevo | Gornji Kovačići | 70 | 7,371.500 | 105.300 | B |
| 8a1ef459dcf7fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 35 | 3,686.300 | 105.300 | A |
| 8a1ef45b16affff | Vogošća | Hotonj | 18 | 1,896.200 | 105.300 | B |
| 8a1ef4582bb7fff | Centar Sarajevo | Koševo II | 80 | 8,429.200 | 105.400 | B |
| 8a1ef45902cffff | Novo Sarajevo | Hrasno Brdo | 71 | 7,482.400 | 105.400 | B |
| 8a1ef45b6b37fff | Vogošća | Semizovac | 21 | 2,213.200 | 105.400 | B |
| 8a1ef45827b7fff | Centar Sarajevo | Crni Vrh-Gorica | 135 | 14,233.800 | 105.400 | B |
| 8a1ef4591b8ffff | Centar Sarajevo | Marijin Dvor | 68 | 7,171.000 | 105.500 | B |
| 8a1ef45913a7fff | Novo Sarajevo | Gornji Kovačići | 74 | 7,803.800 | 105.500 | B |
| 8a1ef6964ad7fff | Ilidža | Lužani | 38 | 4,007.800 | 105.500 | B |
| 8a1ef45821a7fff | Centar Sarajevo | Koševsko Brdo | 205 | 21,621.400 | 105.500 | B |
| 8a1ef4595a77fff | Novo Sarajevo | Gornji Velešići | 37 | 3,903.400 | 105.500 | B |
| 8a1ef4580c9ffff | Centar Sarajevo | Pionirska Dolina | 38 | 4,010.800 | 105.500 | B |
| 8a1ef45822affff | Centar Sarajevo | Mejtaš-Bjelave | 105 | 11,087.600 | 105.600 | B |
| 8a1ea92ca487fff | Ilidža | Blažuj | 11 | 1,161.600 | 105.600 | B |
| 8a1ef4591517fff | Novo Sarajevo | Hrasno Brdo | 95 | 10,032.700 | 105.600 | B |
| 8a1ef4591417fff | Novo Sarajevo | Vraca | 71 | 7,499.800 | 105.600 | B |
| 8a1ef4595367fff | Novo Sarajevo | Velešići | 49 | 5,178.200 | 105.700 | B |
| 8a1ef459544ffff | Novo Sarajevo | Pofalići II | 51 | 5,390.900 | 105.700 | B |
| 8a1ea92eb187fff | Novi Grad Sarajevo | Reljevo | 11 | 1,163.600 | 105.800 | A |
| 8a1ef6965c9ffff | Ilidža | Lužani | 12 | 1,269.400 | 105.800 | B |
| 8a1ef696584ffff | Ilidža | Naselje Bulevar | 54 | 5,714.800 | 105.800 | B |
| 8a1ef45828dffff | Centar Sarajevo | Koševo II | 191 | 20,216.700 | 105.800 | B |
| 8a1ef459c8b7fff | Centar Sarajevo | Skenderija-Podtekija | 195 | 20,642.800 | 105.900 | B |
| 8a1ef4586637fff | Centar Sarajevo | Šip | 116 | 12,283.600 | 105.900 | B |
| 8a1ef459131ffff | Novo Sarajevo | Gornji Kovačići | 71 | 7,519.400 | 105.900 | B |
| 8a1ea92ca4affff | Ilidža | Blažuj | 63 | 6,673.800 | 105.900 | B |
| 8a1ef4591597fff | Novo Sarajevo | Hrasno Brdo | 70 | 7,418.600 | 106.000 | B |
| 8a1ef6965b8ffff | Ilidža | Naselje Bulevar | 83 | 8,796.400 | 106.000 | B |
| 8a1ef45914b7fff | Novo Sarajevo | Hrasno Brdo | 47 | 4,981.400 | 106.000 | B |
| 8a1ef4592c2ffff | Novi Grad Sarajevo | Dobrinja A | 58 | 6,147.600 | 106.000 | A |
| 8a1ef4583d2ffff | Stari Grad Sarajevo | Sedrenik | 64 | 6,783.700 | 106.000 | A |
| 8a1ef45b04c7fff | Vogošća | Vogošća | 14 | 1,484.200 | 106.000 | B |
| 8a1ef4591467fff | Novo Sarajevo | Vraca | 79 | 8,375.400 | 106.000 | B |
| 8a1ef45826cffff | Centar Sarajevo | Trg oslobođenja-Centar | 182 | 19,302.400 | 106.100 | B |
| 8a1ef4582a77fff | Centar Sarajevo | Hrastovi-Mrkovići | 58 | 6,154.000 | 106.100 | B |
| 8a1ef4582237fff | Centar Sarajevo | Bardakčije | 130 | 13,793.800 | 106.100 | B |
| 8a1ef458221ffff | Centar Sarajevo | Bardakčije | 104 | 11,035.400 | 106.100 | B |
| 8a1ef4582577fff | Centar Sarajevo | Koševsko Brdo | 220 | 23,351.600 | 106.100 | B |
| 8a1ef4596657fff | Novi Grad Sarajevo | Saraj Polje | 44 | 4,672.900 | 106.200 | A |
| 8a1ef4583597fff | Stari Grad Sarajevo | Logavina | 164 | 17,418.500 | 106.200 | A |
| 8a1ef45826effff | Centar Sarajevo | Trg oslobođenja-Centar | 148 | 15,721.100 | 106.200 | B |
| 8a1ef4591bb7fff | Novo Sarajevo | Željeznička | 60 | 6,374.100 | 106.200 | B |
| 8a1ef4582227fff | Centar Sarajevo | Bardakčije | 105 | 11,155.000 | 106.200 | B |
| 8a1ef4586497fff | Vogošća | Kobilja Glava | 11 | 1,168.700 | 106.200 | B |
| 8a1ef45b164ffff | Centar Sarajevo | Betanija | 12 | 1,275.400 | 106.300 | B |
| 8a1ea92c9037fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 21 | 2,232.400 | 106.300 | A |
| 8a1ef4590197fff | Novi Grad Sarajevo | Otoka | 58 | 6,171.500 | 106.400 | A |
| 8a1ef459dc77fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 40 | 4,256.300 | 106.400 | A |
| 8a1ef4591737fff | Novo Sarajevo | Vraca | 62 | 6,597.300 | 106.400 | B |
| 8a1ef45b1097fff | Vogošća | Hotonj | 10 | 1,064.600 | 106.500 | B |
| 8a1ef45b04b7fff | Vogošća | Vogošća | 13 | 1,384.000 | 106.500 | B |
| 8a1ef459cca7fff | Centar Sarajevo | Soukbunar | 77 | 8,197.400 | 106.500 | B |
| 8a1ef4584507fff | Centar Sarajevo | Betanija | 12 | 1,278.100 | 106.500 | B |
| 8a1ef4595747fff | Novo Sarajevo | Pofalići I | 81 | 8,629.100 | 106.500 | B |
| 8a1ef459c527fff | Centar Sarajevo | Soukbunar | 43 | 4,581.700 | 106.600 | B |
| 8a1ef45b1467fff | Vogošća | Hotonj | 10 | 1,065.600 | 106.600 | B |
| 8a1ef459108ffff | Novo Sarajevo | Vraca | 89 | 9,487.000 | 106.600 | B |
| 8a1ef45b0677fff | Vogošća | Vogošća | 28 | 2,985.200 | 106.600 | B |
| 8a1ef4593977fff | Novo Sarajevo | Hrasno Brdo | 63 | 6,718.400 | 106.600 | B |
| 8a1ea92ddab7fff | Ilidža | Lipe | 13 | 1,386.500 | 106.700 | B |
| 8a1ea92dd327fff | Ilidža | Lipe | 12 | 1,280.100 | 106.700 | B |
| 8a1ef45b3b97fff | Vogošća | Hotonj | 14 | 1,493.500 | 106.700 | B |
| 8a1ef4586187fff | Vogošća | Kobilja Glava | 13 | 1,386.900 | 106.700 | B |
| 8a1ef4582327fff | Centar Sarajevo | Breka | 85 | 9,069.200 | 106.700 | B |
| 8a1ef45958d7fff | Novo Sarajevo | Pofalići II | 15 | 1,600.700 | 106.700 | B |
| 8a1ef459571ffff | Novo Sarajevo | Pofalići II | 76 | 8,110.300 | 106.700 | B |
| 8a1ef4592d4ffff | Novi Grad Sarajevo | Saraj Polje | 44 | 4,697.700 | 106.800 | A |
| 8a1ef45828effff | Centar Sarajevo | Koševo II | 102 | 10,892.700 | 106.800 | B |
| 8a1ef4586717fff | Centar Sarajevo | Šip | 169 | 18,053.400 | 106.800 | B |
| 8a1ef459159ffff | Novo Sarajevo | Hrasno Brdo | 70 | 7,477.900 | 106.800 | B |
| 8a1ef6965b17fff | Ilidža | Naselje Bulevar | 21 | 2,243.500 | 106.800 | B |
| 8a1ef45969affff | Novi Grad Sarajevo | Briješće | 19 | 2,030.000 | 106.800 | A |
| 8a1ef4592c0ffff | Novi Grad Sarajevo | Dobrinja A | 65 | 6,947.200 | 106.900 | A |
| 8a1ef459024ffff | Novo Sarajevo | Hrasno Brdo | 105 | 11,224.500 | 106.900 | B |
| 8a1ea92ce10ffff | Ilidža | Lipe | 10 | 1,069.300 | 106.900 | B |
| 8a1ef45835b7fff | Stari Grad Sarajevo | Logavina | 162 | 17,325.200 | 106.900 | A |
| 8a1ef458071ffff | Centar Sarajevo | Hrastovi-Mrkovići | 22 | 2,353.000 | 107.000 | B |
| 8a1ef4592da7fff | Novi Grad Sarajevo | Dobrinja A | 61 | 6,524.600 | 107.000 | A |
| 8a1ef45b1737fff | Vogošća | Hotonj | 13 | 1,390.500 | 107.000 | B |
| 8a1ef45b048ffff | Vogošća | Vogošća | 12 | 1,283.700 | 107.000 | B |
| 8a1ef458671ffff | Centar Sarajevo | Šip | 165 | 17,653.500 | 107.000 | B |
| 8a1ef4591b2ffff | Centar Sarajevo | Crni Vrh-Gorica | 269 | 28,793.400 | 107.000 | B |
| 8a1ef4590167fff | Novo Sarajevo | Kvadrant | 177 | 18,948.700 | 107.100 | B |
| 8a1ef4595717fff | Novo Sarajevo | Pofalići II | 68 | 7,279.800 | 107.100 | B |
| 8a1ef4586887fff | Vogošća | Kobilja Glava | 12 | 1,285.000 | 107.100 | B |
| 8a1ef69600a7fff | Ilidža | Kovači (Ilidža) | 46 | 4,928.600 | 107.100 | B |
| 8a1ef45b055ffff | Vogošća | Vogošća | 38 | 4,073.600 | 107.200 | B |
| 8a1ef45b3bb7fff | Vogošća | Ugorsko | 12 | 1,286.500 | 107.200 | B |
| 8a1ef458442ffff | Centar Sarajevo | Betanija | 16 | 1,715.400 | 107.200 | B |
| 8a1ef45b02a7fff | Vogošća | Blagovac | 19 | 2,039.100 | 107.300 | B |
| 8a1ef459cd4ffff | Centar Sarajevo | Skenderija-Podtekija | 169 | 18,137.600 | 107.300 | B |
| 8a1ef45b004ffff | Vogošća | Blagovac | 23 | 2,468.800 | 107.300 | B |
| 8a1ef459cd2ffff | Centar Sarajevo | Skenderija-Podtekija | 177 | 19,000.000 | 107.300 | B |
| 8a1ef4596817fff | Novi Grad Sarajevo | Briješće | 21 | 2,254.300 | 107.300 | A |
| 8a1ea92c915ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 30 | 3,221.000 | 107.400 | A |
| 8a1ef45b3b27fff | Vogošća | Hotonj | 27 | 2,900.700 | 107.400 | B |
| 8a1ef45822a7fff | Centar Sarajevo | Mejtaš-Bjelave | 117 | 12,570.500 | 107.400 | B |
| 8a1ef459c92ffff | Stari Grad Sarajevo | Logavina | 153 | 16,439.300 | 107.400 | A |
| 8a1ef458230ffff | Centar Sarajevo | Bardakčije | 89 | 9,563.100 | 107.500 | B |
| 8a1ef4595a1ffff | Novo Sarajevo | Velešići | 44 | 4,728.600 | 107.500 | B |
| 8a1ef4580527fff | Centar Sarajevo | Pionirska Dolina | 36 | 3,868.900 | 107.500 | B |
| 8a1ef4582307fff | Centar Sarajevo | Bardakčije | 93 | 9,995.400 | 107.500 | B |
| 8a1ef4580107fff | Centar Sarajevo | Pionirska Dolina | 12 | 1,289.800 | 107.500 | B |
| 8a1ef45939a7fff | Novo Sarajevo | Hrasno Brdo | 53 | 5,697.900 | 107.500 | B |
| 8a1ef4582967fff | Centar Sarajevo | Betanija | 43 | 4,624.400 | 107.500 | B |
| 8a1ef45950c7fff | Novo Sarajevo | Pofalići II | 57 | 6,130.000 | 107.500 | B |
| 8a1ef4580b2ffff | Centar Sarajevo | Betanija | 22 | 2,366.500 | 107.600 | B |
| 8a1ef45b2917fff | Vogošća | Vogošća | 10 | 1,076.400 | 107.600 | B |
| 8a1ef45b0aaffff | Vogošća | Blagovac | 16 | 1,722.200 | 107.600 | B |
| 8a1ef45804a7fff | Centar Sarajevo | Hrastovi-Mrkovići | 58 | 6,243.400 | 107.600 | B |
| 8a1ef458415ffff | Centar Sarajevo | Nahorevo | 11 | 1,185.500 | 107.800 | B |
| 8a1ef4595967fff | Vogošća | Kobilja Glava | 15 | 1,617.400 | 107.800 | B |
| 8a1ea92c98cffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 33 | 3,558.500 | 107.800 | A |
| 8a1ef45b3a1ffff | Vogošća | Hotonj | 20 | 2,157.200 | 107.900 | B |
| 8a1ef458242ffff | Centar Sarajevo | Koševsko Brdo | 112 | 12,080.900 | 107.900 | B |
| 8a1ef6960a6ffff | Ilidža | Sokolović-kolonija | 117 | 12,622.100 | 107.900 | B |
| 8a1ef459570ffff | Novo Sarajevo | Pofalići II | 75 | 8,094.200 | 107.900 | B |
| 8a1ef458239ffff | Centar Sarajevo | Mejtaš-Bjelave | 157 | 16,946.600 | 107.900 | B |
| 8a1ef45b3b17fff | Vogošća | Hotonj | 21 | 2,268.200 | 108.000 | B |
| 8a1ef45820b7fff | Centar Sarajevo | Ciglane | 263 | 28,407.300 | 108.000 | B |
| 8a1ef4584577fff | Centar Sarajevo | Betanija | 10 | 1,080.300 | 108.000 | B |
| 8a1ea92c9197fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 96 | 10,373.100 | 108.100 | A |
| 8a1ef45b384ffff | Vogošća | Hotonj | 25 | 2,701.400 | 108.100 | B |
| 8a1ef4580d0ffff | Centar Sarajevo | Pionirska Dolina | 32 | 3,458.300 | 108.100 | B |
| 8a1ef458054ffff | Centar Sarajevo | Pionirska Dolina | 15 | 1,621.100 | 108.100 | B |
| 8a1ef459c09ffff | Stari Grad Sarajevo | Širokača | 59 | 6,383.900 | 108.200 | A |
| 8a1ef458279ffff | Centar Sarajevo | Crni Vrh-Gorica | 121 | 13,092.800 | 108.200 | B |
| 8a1ef4582247fff | Stari Grad Sarajevo | Logavina | 152 | 16,450.400 | 108.200 | A |
| 8a1ef4582aa7fff | Centar Sarajevo | Breka | 203 | 21,970.800 | 108.200 | B |
| 8a1ef458652ffff | Vogošća | Kobilja Glava | 24 | 2,597.700 | 108.200 | B |
| 8a1ef45b061ffff | Vogošća | Uglješići | 69 | 7,473.000 | 108.300 | B |
| 8a1ef45b0057fff | Vogošća | Blagovac | 22 | 2,382.800 | 108.300 | B |
| 8a1ef459ccf7fff | Centar Sarajevo | Soukbunar | 91 | 9,862.600 | 108.400 | B |
| 8a1ef45b0237fff | Vogošća | Blagovac | 25 | 2,709.700 | 108.400 | B |
| 8a1ef4582097fff | Centar Sarajevo | Ciglane | 297 | 32,203.900 | 108.400 | B |
| 8a1ef45966e7fff | Novi Grad Sarajevo | Saraj Polje | 45 | 4,879.800 | 108.400 | A |
| 8a1ef4582a17fff | Centar Sarajevo | Hrastovi-Mrkovići | 81 | 8,784.700 | 108.500 | B |
| 8a1ea92eb8effff | Novi Grad Sarajevo | Reljevo | 11 | 1,193.000 | 108.500 | A |
| 8a1ef4586627fff | Centar Sarajevo | Šip | 138 | 14,975.200 | 108.500 | B |
| 8a1ef45867a7fff | Centar Sarajevo | Šip | 74 | 8,035.700 | 108.600 | B |
| 8a1ef45b0317fff | Vogošća | Blagovac | 20 | 2,172.200 | 108.600 | B |
| 8a1ef458278ffff | Centar Sarajevo | Džidžikovac-Koševo I | 224 | 24,336.100 | 108.600 | B |
| 8a1ef6960b6ffff | Ilidža | Sokolović-kolonija | 11 | 1,195.200 | 108.700 | B |
| 8a1ea92c90e7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 34 | 3,696.700 | 108.700 | A |
| 8a1ef6961827fff | Ilidža | Butmir | 38 | 4,132.400 | 108.700 | B |
| 8a1ef45b1717fff | Vogošća | Hotonj | 10 | 1,087.600 | 108.800 | B |
| 8a1ef458265ffff | Centar Sarajevo | Trg oslobođenja-Centar | 136 | 14,792.000 | 108.800 | B |
| 8a1ef458418ffff | Centar Sarajevo | Nahorevo | 18 | 1,958.300 | 108.800 | B |
| 8a1ef6964ab7fff | Ilidža | Vreoca | 10 | 1,088.100 | 108.800 | B |
| 8a1ef459c96ffff | Stari Grad Sarajevo | Logavina | 173 | 18,824.000 | 108.800 | A |
| 8a1ef4586d27fff | Vogošća | Hotonj | 20 | 2,177.000 | 108.900 | B |
| 8a1ef4584187fff | Centar Sarajevo | Nahorevo | 17 | 1,852.600 | 109.000 | B |
| 8a1ef458264ffff | Centar Sarajevo | Trg oslobođenja-Centar | 235 | 25,610.200 | 109.000 | B |
| 8a1ef459505ffff | Novo Sarajevo | Pofalići I | 42 | 4,578.100 | 109.000 | B |
| 8a1ef4582287fff | Centar Sarajevo | Mejtaš-Bjelave | 111 | 12,101.200 | 109.000 | B |
| 8a1ef45b16e7fff | Vogošća | Hotonj | 15 | 1,635.300 | 109.000 | B |
| 8a1ef458229ffff | Centar Sarajevo | Mejtaš-Bjelave | 108 | 11,775.200 | 109.000 | B |
| 8a1ef45b606ffff | Vogošća | Krivoglavci | 21 | 2,290.000 | 109.000 | B |
| 8a1ef45b17a7fff | Vogošća | Hotonj | 20 | 2,181.000 | 109.000 | B |
| 8a1ef45912f7fff | Novo Sarajevo | Gornji Kovačići | 10 | 1,090.700 | 109.100 | B |
| 8a1ef45828e7fff | Centar Sarajevo | Koševo II | 193 | 21,065.600 | 109.100 | B |
| 8a1ef4583147fff | Stari Grad Sarajevo | Mošćanica | 15 | 1,637.200 | 109.100 | A |
| 8a1ea92cd5b7fff | Novi Grad Sarajevo | Dobroševići | 11 | 1,200.700 | 109.200 | A |
| 8a1ef45b6767fff | Vogošća | Krivoglavci | 11 | 1,200.800 | 109.200 | B |
| 8a1ef45b6177fff | Vogošća | Krivoglavci | 13 | 1,419.100 | 109.200 | B |
| 8a1ef459cd67fff | Centar Sarajevo | Skenderija-Podtekija | 162 | 17,686.100 | 109.200 | B |
| 8a1ef4584157fff | Centar Sarajevo | Nahorevo | 11 | 1,201.000 | 109.200 | B |
| 8a1ef696592ffff | Ilidža | Naselje Bulevar | 76 | 8,299.600 | 109.200 | B |
| 8a1ef45918d7fff | Novo Sarajevo | Željeznička | 102 | 11,139.600 | 109.200 | B |
| 8a1ef4580d8ffff | Centar Sarajevo | Pionirska Dolina | 30 | 3,277.100 | 109.200 | B |
| 8a1ea92c3287fff | Ilidža | Gladno polje | 11 | 1,202.100 | 109.300 | B |
| 8a1ef45b6907fff | Vogošća | Svrake | 12 | 1,311.400 | 109.300 | B |
| 8a1ef45b168ffff | Vogošća | Hotonj | 22 | 2,404.700 | 109.300 | B |
| 8a1ef4586ac7fff | Centar Sarajevo | Betanija | 17 | 1,858.300 | 109.300 | B |
| 8a1ef4595a9ffff | Novo Sarajevo | Velešići | 26 | 2,842.400 | 109.300 | B |
| 8a1ef6964c67fff | Ilidža | Plandište | 40 | 4,374.300 | 109.400 | B |
| 8a1ef45b17affff | Vogošća | Hotonj | 14 | 1,531.200 | 109.400 | B |
| 8a1ef45b2b2ffff | Vogošća | Vogošća | 16 | 1,750.400 | 109.400 | B |
| 8a1ef458634ffff | Centar Sarajevo | Betanija | 18 | 1,969.700 | 109.400 | B |
| 8a1ef45820f7fff | Centar Sarajevo | Park-Višnjik | 158 | 17,292.200 | 109.400 | B |
| 8a1ef4586837fff | Centar Sarajevo | Betanija | 15 | 1,642.300 | 109.500 | B |
| 8a1ef458650ffff | Vogošća | Kobilja Glava | 27 | 2,957.000 | 109.500 | B |
| 8a1ef4584117fff | Centar Sarajevo | Nahorevo | 18 | 1,971.500 | 109.500 | B |
| 8a1ef4582ccffff | Centar Sarajevo | Koševsko Brdo | 235 | 25,748.300 | 109.600 | B |
| 8a1ef45b0c5ffff | Vogošća | Vogošća | 18 | 1,972.300 | 109.600 | B |
| 8a1ef459695ffff | Novi Grad Sarajevo | Briješće | 69 | 7,560.500 | 109.600 | A |
| 8a1ef45950d7fff | Novo Sarajevo | Pofalići II | 62 | 6,794.500 | 109.600 | B |
| 8a1ea92c902ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 33 | 3,616.900 | 109.600 | A |
| 8a1ea92eb65ffff | Novi Grad Sarajevo | Reljevo | 10 | 1,096.100 | 109.600 | A |
| 8a1ef45b2197fff | Novi Grad Sarajevo | Zabrđe | 49 | 5,371.700 | 109.600 | A |
| 8a1ea92c90cffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 33 | 3,617.700 | 109.600 | A |
| 8a1ea92c90b7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 26 | 2,850.400 | 109.600 | A |
| 8a1ef459151ffff | Novo Sarajevo | Hrasno Brdo | 112 | 12,278.700 | 109.600 | B |
| 8a1ef458651ffff | Vogošća | Kobilja Glava | 26 | 2,850.700 | 109.600 | B |
| 8a1ef4591367fff | Centar Sarajevo | Soukbunar | 81 | 8,883.300 | 109.700 | B |
| 8a1ef4582c8ffff | Novo Sarajevo | Gornji Velešići | 105 | 11,517.200 | 109.700 | B |
| 8a1ef45939affff | Novo Sarajevo | Hrasno Brdo | 40 | 4,387.900 | 109.700 | B |
| 8a1ef4580507fff | Centar Sarajevo | Pionirska Dolina | 51 | 5,596.700 | 109.700 | B |
| 8a1ea92c9b97fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 29 | 3,182.500 | 109.700 | A |
| 8a1ef45968e7fff | Novi Grad Sarajevo | Briješće | 19 | 2,086.400 | 109.800 | A |
| 8a1ef45849a7fff | Centar Sarajevo | Nahorevo | 18 | 1,976.800 | 109.800 | B |
| 8a1ef4595b27fff | Centar Sarajevo | Šip | 13 | 1,427.800 | 109.800 | B |
| 8a1ef69618d7fff | Ilidža | Donji Kotorac | 97 | 10,653.800 | 109.800 | B |
| 8a1ef4592cd7fff | Novi Grad Sarajevo | Dobrinja A | 111 | 12,197.100 | 109.900 | A |
| 8a1ef458289ffff | Centar Sarajevo | Džidžikovac-Koševo I | 188 | 20,659.600 | 109.900 | B |
| 8a1ef45b294ffff | Vogošća | Vogošća | 13 | 1,429.000 | 109.900 | B |
| 8a1ef45b17b7fff | Vogošća | Hotonj | 22 | 2,418.400 | 109.900 | B |
| 8a1ef6963837fff | Ilidža | Hrasnica | 107 | 11,762.500 | 109.900 | B |
| 8a1ef45823affff | Centar Sarajevo | Mejtaš-Bjelave | 122 | 13,414.000 | 110.000 | B |
| 8a1ef45917a7fff | Novo Sarajevo | Vraca | 15 | 1,649.400 | 110.000 | B |
| 8a1ef459649ffff | Ilidža | Naselje Bulevar | 22 | 2,419.400 | 110.000 | B |
| 8a1ef4596b87fff | Novi Grad Sarajevo | Briješće | 24 | 2,640.100 | 110.000 | A |
| 8a1ef4586ca7fff | Vogošća | Hotonj | 26 | 2,861.200 | 110.000 | B |
| 8a1ef45950dffff | Novo Sarajevo | Pofalići II | 67 | 7,373.700 | 110.100 | B |
| 8a1ea92e92effff | Vogošća | Semizovac | 12 | 1,320.700 | 110.100 | B |
| 8a1ef4583767fff | Stari Grad Sarajevo | Mošćanica | 14 | 1,540.800 | 110.100 | A |
| 8a1ef459125ffff | Centar Sarajevo | Soukbunar | 12 | 1,320.800 | 110.100 | B |
| 8a1ef45b0357fff | Vogošća | Blagovac | 17 | 1,871.400 | 110.100 | B |
| 8a1ef4582ba7fff | Centar Sarajevo | Koševo II | 76 | 8,368.400 | 110.100 | B |
| 8a1ef45b038ffff | Vogošća | Blagovac | 29 | 3,193.400 | 110.100 | B |
| 8a1ef4582847fff | Centar Sarajevo | Koševo II | 76 | 8,373.000 | 110.200 | B |
| 8a1ef4580437fff | Centar Sarajevo | Pionirska Dolina | 55 | 6,060.300 | 110.200 | B |
| 8a1ef6965c57fff | Ilidža | Ilidža | 71 | 7,823.400 | 110.200 | B |
| 8a1ef4586daffff | Vogošća | Hotonj | 19 | 2,093.600 | 110.200 | B |
| 8a1ef4592d27fff | Novi Grad Sarajevo | Saraj Polje | 48 | 5,290.300 | 110.200 | A |
| 8a1ef458041ffff | Centar Sarajevo | Pionirska Dolina | 48 | 5,294.700 | 110.300 | B |
| 8a1ef45b3877fff | Vogošća | Ugorsko | 23 | 2,537.100 | 110.300 | B |
| 8a1ef45826c7fff | Centar Sarajevo | Trg oslobođenja-Centar | 358 | 39,493.700 | 110.300 | B |
| 8a1ef458219ffff | Centar Sarajevo | Ciglane | 121 | 13,348.700 | 110.300 | B |
| 8a1ef45b1407fff | Vogošća | Hotonj | 20 | 2,206.400 | 110.300 | B |
| 8a1ea92dda47fff | Ilidža | Lipe | 10 | 1,103.500 | 110.300 | B |
| 8a1ef45b2947fff | Vogošća | Vogošća | 10 | 1,103.500 | 110.300 | B |
| 8a1ef4586487fff | Vogošća | Kobilja Glava | 15 | 1,655.700 | 110.400 | B |
| 8a1ef45b4597fff | Vogošća | Semizovac | 16 | 1,766.300 | 110.400 | B |
| 8a1ef45b312ffff | Vogošća | Ugorsko | 11 | 1,214.700 | 110.400 | B |
| 8a1ef4580b8ffff | Centar Sarajevo | Betanija | 12 | 1,325.500 | 110.500 | B |
| 8a1ef4580aa7fff | Centar Sarajevo | Betanija | 19 | 2,099.000 | 110.500 | B |
| 8a1ef45b12f7fff | Centar Sarajevo | Betanija | 14 | 1,546.900 | 110.500 | B |
| 8a1ef459cd17fff | Centar Sarajevo | Skenderija-Podtekija | 106 | 11,717.700 | 110.500 | B |
| 8a1ef459459ffff | Novi Grad Sarajevo | Briješće | 11 | 1,216.100 | 110.600 | A |
| 8a1ef45b2b27fff | Vogošća | Vogošća | 16 | 1,770.100 | 110.600 | B |
| 8a1ef4584087fff | Centar Sarajevo | Nahorevo | 14 | 1,548.900 | 110.600 | B |
| 8a1ea92ce04ffff | Ilidža | Dolovi | 19 | 2,102.400 | 110.700 | B |
| 8a1ef45b62a7fff | Vogošća | Krivoglavci | 17 | 1,882.800 | 110.800 | B |
| 8a1ea92c9127fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 21 | 2,326.200 | 110.800 | A |
| 8a1ef45b1457fff | Vogošća | Hotonj | 19 | 2,105.700 | 110.800 | B |
| 8a1ef459c9affff | Centar Sarajevo | Trg oslobođenja-Centar | 293 | 32,473.900 | 110.800 | B |
| 8a1ef4594487fff | Novi Grad Sarajevo | Briješće | 22 | 2,438.300 | 110.800 | A |
| 8a1ef4580caffff | Centar Sarajevo | Pionirska Dolina | 51 | 5,653.000 | 110.800 | B |
| 8a1ea92e9ab7fff | Vogošća | Donja Vogošća | 11 | 1,220.200 | 110.900 | B |
| 8a1ef4580c27fff | Centar Sarajevo | Pionirska Dolina | 25 | 2,773.300 | 110.900 | B |
| 8a1ef45846c7fff | Centar Sarajevo | Betanija | 19 | 2,108.500 | 111.000 | B |
| 8a1ef45b38d7fff | Vogošća | Ugorsko | 13 | 1,443.000 | 111.000 | B |
| 8a1ef45b056ffff | Vogošća | Vogošća | 36 | 3,996.600 | 111.000 | B |
| 8a1ea92e92dffff | Vogošća | Svrake | 19 | 2,109.300 | 111.000 | B |
| 8a1ef45864b7fff | Vogošća | Kobilja Glava | 22 | 2,442.900 | 111.000 | B |
| 8a1ef45822d7fff | Stari Grad Sarajevo | Logavina | 141 | 15,662.900 | 111.100 | A |
| 8a1ef4582837fff | Centar Sarajevo | Betanija | 189 | 20,995.900 | 111.100 | B |
| 8a1ef45b664ffff | Vogošća | Vogošća | 14 | 1,555.500 | 111.100 | B |
| 8a1ef45b63a7fff | Vogošća | Krivoglavci | 24 | 2,666.800 | 111.100 | B |
| 8a1ef45b60cffff | Vogošća | Krivoglavci | 15 | 1,667.400 | 111.200 | B |
| 8a1ef45b3baffff | Vogošća | Hotonj | 27 | 3,002.500 | 111.200 | B |
| 8a1ef4582a0ffff | Centar Sarajevo | Hrastovi-Mrkovići | 68 | 7,563.200 | 111.200 | B |
| 8a1ef45b0ccffff | Vogošća | Vogošća | 15 | 1,668.400 | 111.200 | B |
| 8a1ea92dd307fff | Ilidža | Lipe | 11 | 1,223.500 | 111.200 | B |
| 8a1ef45854d7fff | Centar Sarajevo | Betanija | 23 | 2,559.000 | 111.300 | B |
| 8a1ef45b0ceffff | Vogošća | Vogošća | 11 | 1,224.500 | 111.300 | B |
| 8a1ef459594ffff | Vogošća | Kobilja Glava | 18 | 2,004.500 | 111.400 | B |
| 8a1ef458270ffff | Centar Sarajevo | Džidžikovac-Koševo I | 152 | 16,927.800 | 111.400 | B |
| 8a1ef45b0ce7fff | Vogošća | Vogošća | 15 | 1,670.600 | 111.400 | B |
| 8a1ef458276ffff | Centar Sarajevo | Mejtaš-Bjelave | 171 | 19,046.500 | 111.400 | B |
| 8a1ea92cbbb7fff | Ilidža | Doglodi | 11 | 1,225.500 | 111.400 | B |
| 8a1ef6964867fff | Ilidža | Vreoca | 10 | 1,114.100 | 111.400 | B |
| 8a1ef4586897fff | Vogošća | Kobilja Glava | 11 | 1,225.600 | 111.400 | B |
| 8a1ef4586567fff | Vogošća | Kobilja Glava | 24 | 2,676.100 | 111.500 | B |
| 8a1ef45b04f7fff | Vogošća | Vogošća | 16 | 1,784.400 | 111.500 | B |
| 8a1ef458292ffff | Centar Sarajevo | Betanija | 54 | 6,023.600 | 111.500 | B |
| 8a1ef45b690ffff | Vogošća | Svrake | 19 | 2,119.500 | 111.600 | B |
| 8a1ef45b452ffff | Vogošća | Ljubina-Poturovići | 12 | 1,338.900 | 111.600 | B |
| 8a1ef4583b47fff | Stari Grad Sarajevo | Mošćanica | 14 | 1,562.200 | 111.600 | A |
| 8a1ef45b0577fff | Vogošća | Vogošća | 32 | 3,570.800 | 111.600 | B |
| 8a1ef4592537fff | Ilidža | Stupsko Brdo | 79 | 8,815.700 | 111.600 | B |
| 8a1ef459dcc7fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 30 | 3,349.400 | 111.600 | A |
| 8a1ea92e985ffff | Vogošća | Donja Vogošća | 13 | 1,451.500 | 111.700 | B |
| 8a1ef4586587fff | Vogošća | Kobilja Glava | 22 | 2,456.400 | 111.700 | B |
| 8a1ef45b020ffff | Vogošća | Blagovac | 18 | 2,010.100 | 111.700 | B |
| 8a1ef459cd0ffff | Centar Sarajevo | Skenderija-Podtekija | 262 | 29,278.700 | 111.800 | B |
| 8a1ef4582377fff | Centar Sarajevo | Bardakčije | 90 | 10,058.200 | 111.800 | B |
| 8a1ef4582107fff | Centar Sarajevo | Džidžikovac-Koševo I | 133 | 14,864.500 | 111.800 | B |
| 8a1ef45823a7fff | Centar Sarajevo | Park-Višnjik | 234 | 26,153.900 | 111.800 | B |
| 8a1ef4591427fff | Novo Sarajevo | Hrasno Brdo | 126 | 14,086.700 | 111.800 | B |
| 8a1ef4586857fff | Centar Sarajevo | Betanija | 23 | 2,571.500 | 111.800 | B |
| 8a1ea92c90f7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 35 | 3,913.500 | 111.800 | A |
| 8a1ef45b314ffff | Vogošća | Hotonj | 13 | 1,453.800 | 111.800 | B |
| 8a1ef459c917fff | Centar Sarajevo | Trg oslobođenja-Centar | 135 | 15,097.300 | 111.800 | B |
| 8a1ef458254ffff | Centar Sarajevo | Ciglane | 375 | 41,936.900 | 111.800 | B |
| 8a1ef4582a37fff | Centar Sarajevo | Hrastovi-Mrkovići | 75 | 8,387.900 | 111.800 | B |
| 8a1ef6960adffff | Ilidža | Sokolović-kolonija | 64 | 7,158.400 | 111.800 | B |
| 8a1ef45b00effff | Vogošća | Blagovac | 29 | 3,243.600 | 111.800 | B |
| 8a1ef696586ffff | Ilidža | Naselje Bulevar | 24 | 2,684.700 | 111.900 | B |
| 8a1ef4586817fff | Vogošća | Kobilja Glava | 21 | 2,349.400 | 111.900 | B |
| 8a1ef4596717fff | Ilidža | Stupsko Brdo | 26 | 2,909.900 | 111.900 | B |
| 8a1ef45966c7fff | Novi Grad Sarajevo | Saraj Polje | 50 | 5,596.900 | 111.900 | A |
| 8a1ef45b6927fff | Vogošća | Svrake | 11 | 1,231.300 | 111.900 | B |
| 8a1ea92ca5a7fff | Ilidža | Blažuj | 30 | 3,359.000 | 112.000 | B |
| 8a1ea92e92affff | Vogošća | Svrake | 12 | 1,343.800 | 112.000 | B |
| 8a1ef4580857fff | Centar Sarajevo | Betanija | 10 | 1,120.500 | 112.100 | B |
| 8a1ef45967b7fff | Ilidža | Naselje Bulevar | 24 | 2,689.300 | 112.100 | B |
| 8a1ef4582397fff | Centar Sarajevo | Mejtaš-Bjelave | 140 | 15,690.000 | 112.100 | B |
| 8a1ef45968f7fff | Novi Grad Sarajevo | Briješće | 21 | 2,353.800 | 112.100 | A |
| 8a1ef4582197fff | Centar Sarajevo | Koševsko Brdo | 187 | 20,960.600 | 112.100 | B |
| 8a1ef45862dffff | Centar Sarajevo | Betanija | 184 | 20,627.000 | 112.100 | B |
| 8a1ef4592d97fff | Novi Grad Sarajevo | Dobrinja A | 49 | 5,493.400 | 112.100 | A |
| 8a1ef45b316ffff | Vogošća | Ugorsko | 21 | 2,354.400 | 112.100 | B |
| 8a1ef4592d2ffff | Novi Grad Sarajevo | Saraj Polje | 50 | 5,607.600 | 112.200 | A |
| 8a1ea92cd0dffff | Novi Grad Sarajevo | Reljevo | 45 | 5,047.100 | 112.200 | A |
| 8a1ef4580797fff | Centar Sarajevo | Hrastovi-Mrkovići | 45 | 5,047.800 | 112.200 | B |
| 8a1ea92e934ffff | Vogošća | Nebočaj | 15 | 1,682.600 | 112.200 | B |
| 8a1ef6964987fff | Ilidža | Kamenjača | 93 | 10,434.100 | 112.200 | B |
| 8a1ea92c9c77fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 154 | 17,280.400 | 112.200 | A |
| 8a1ea92c8987fff | Novi Grad Sarajevo | Dobroševići | 11 | 1,234.400 | 112.200 | A |
| 8a1ef4582b27fff | Centar Sarajevo | Koševo II | 73 | 8,192.800 | 112.200 | B |
| 8a1ef45b326ffff | Vogošća | Kobilja Glava | 14 | 1,571.300 | 112.200 | B |
| 8a1ef45807a7fff | Centar Sarajevo | Hrastovi-Mrkovići | 19 | 2,133.400 | 112.300 | B |
| 8a1ef4582a6ffff | Centar Sarajevo | Hrastovi-Mrkovići | 61 | 6,849.700 | 112.300 | B |
| 8a1ef45b3837fff | Vogošća | Ugorsko | 36 | 4,043.000 | 112.300 | B |
| 8a1ef45b059ffff | Vogošća | Vogošća | 12 | 1,348.000 | 112.300 | B |
| 8a1ef45b03affff | Vogošća | Blagovac | 30 | 3,370.200 | 112.300 | B |
| 8a1ef458655ffff | Centar Sarajevo | Šip | 59 | 6,628.500 | 112.300 | B |
| 8a1ef4582607fff | Centar Sarajevo | Džidžikovac-Koševo I | 187 | 21,024.900 | 112.400 | B |
| 8a1ef45b0047fff | Vogošća | Blagovac | 24 | 2,698.500 | 112.400 | B |
| 8a1ef45820dffff | Centar Sarajevo | Park-Višnjik | 279 | 31,371.600 | 112.400 | B |
| 8a1ef4595377fff | Novo Sarajevo | Velešići | 69 | 7,759.700 | 112.500 | B |
| 8a1ef4582a97fff | Centar Sarajevo | Breka | 165 | 18,561.600 | 112.500 | B |
| 8a1ef45b334ffff | Vogošća | Hotonj | 19 | 2,138.000 | 112.500 | B |
| 8a1ef6963b97fff | Ilidža | Lasica | 100 | 11,252.900 | 112.500 | B |
| 8a1ef4592daffff | Novi Grad Sarajevo | Dobrinja A | 80 | 9,004.100 | 112.600 | A |
| 8a1ef458238ffff | Centar Sarajevo | Mejtaš-Bjelave | 115 | 12,943.500 | 112.600 | B |
| 8a1ef69651a7fff | Ilidža | Ilidža | 172 | 19,360.300 | 112.600 | B |
| 8a1ef4586d17fff | Vogošća | Hotonj | 18 | 2,027.000 | 112.600 | B |
| 8a1ef45b2b1ffff | Vogošća | Vogošća | 18 | 2,027.100 | 112.600 | B |
| 8a1ef45b4577fff | Vogošća | Ljubina-Poturovići | 11 | 1,238.900 | 112.600 | B |
| 8a1ef45822f7fff | Centar Sarajevo | Bardakčije | 126 | 14,191.500 | 112.600 | B |
| 8a1ea92c911ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 18 | 2,027.600 | 112.600 | A |
| 8a1ef459cc97fff | Centar Sarajevo | Soukbunar | 77 | 8,674.100 | 112.700 | B |
| 8a1ea92cc2e7fff | Novi Grad Sarajevo | Dobroševići | 11 | 1,239.200 | 112.700 | A |
| 8a1ef4582857fff | Centar Sarajevo | Koševo II | 85 | 9,578.700 | 112.700 | B |
| 8a1ef45b3a57fff | Vogošća | Hotonj | 29 | 3,269.100 | 112.700 | B |
| 8a1ef459c81ffff | Stari Grad Sarajevo | Mjedenica | 142 | 16,008.800 | 112.700 | A |
| 8a1ea92ca0c7fff | Ilidža | Osjek | 10 | 1,127.900 | 112.800 | B |
| 8a1ea92cb64ffff | Ilidža | Pejton | 16 | 1,804.800 | 112.800 | B |
| 8a1ea92c9317fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 31 | 3,496.900 | 112.800 | A |
| 8a1ef6964a67fff | Ilidža | Pejton | 13 | 1,466.500 | 112.800 | B |
| 8a1ef45809b7fff | Centar Sarajevo | Betanija | 42 | 4,738.800 | 112.800 | B |
| 8a1ef45966f7fff | Novi Grad Sarajevo | Saraj Polje | 53 | 5,982.200 | 112.900 | A |
| 8a1ef4582b1ffff | Centar Sarajevo | Hrastovi-Mrkovići | 65 | 7,337.500 | 112.900 | B |
| 8a1ef6965307fff | Ilidža | Naselje Bulevar | 13 | 1,467.900 | 112.900 | B |
| 8a1ef4580577fff | Centar Sarajevo | Pionirska Dolina | 31 | 3,501.200 | 112.900 | B |
| 8a1ea92c9237fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 29 | 3,275.800 | 113.000 | A |
| 8a1ea92c932ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 14 | 1,581.900 | 113.000 | A |
| 8a1ef4586427fff | Vogošća | Kobilja Glava | 40 | 4,520.300 | 113.000 | B |
| 8a1ef4584527fff | Centar Sarajevo | Betanija | 13 | 1,469.900 | 113.100 | B |
| 8a1ef4582a47fff | Centar Sarajevo | Hrastovi-Mrkovići | 68 | 7,689.900 | 113.100 | B |
| 8a1ef45b041ffff | Vogošća | Vogošća | 34 | 3,845.100 | 113.100 | B |
| 8a1ef4580db7fff | Centar Sarajevo | Betanija | 22 | 2,488.400 | 113.100 | B |
| 8a1ef45b3807fff | Vogošća | Hotonj | 35 | 3,959.500 | 113.100 | B |
| 8a1ef45b3c4ffff | Vogošća | Ugorsko | 11 | 1,245.600 | 113.200 | B |
| 8a1ef45b2ccffff | Novi Grad Sarajevo | Reljevo | 77 | 8,719.700 | 113.200 | A |
| 8a1ef45866cffff | Centar Sarajevo | Koševsko Brdo | 215 | 24,356.100 | 113.300 | B |
| 8a1ea92ddb77fff | Ilidža | Lipe | 11 | 1,246.300 | 113.300 | B |
| 8a1ef4580d07fff | Centar Sarajevo | Pionirska Dolina | 30 | 3,398.900 | 113.300 | B |
| 8a1ef45b04a7fff | Vogošća | Vogošća | 20 | 2,266.300 | 113.300 | B |
| 8a1ea92ce7a7fff | Ilidža | Lipe | 10 | 1,133.200 | 113.300 | B |
| 8a1ef45b03a7fff | Vogošća | Blagovac | 31 | 3,513.000 | 113.300 | B |
| 8a1ef45b3c67fff | Vogošća | Ugorsko | 10 | 1,133.300 | 113.300 | B |
| 8a1ef4592c1ffff | Novi Grad Sarajevo | Dobrinja A | 133 | 15,073.100 | 113.300 | A |
| 8a1ef4590027fff | Novi Grad Sarajevo | Alipašin Most III | 171 | 19,380.000 | 113.300 | A |
| 8a1ef4582767fff | Centar Sarajevo | Mejtaš-Bjelave | 147 | 16,661.100 | 113.300 | B |
| 8a1ea92e9257fff | Vogošća | Semizovac | 15 | 1,700.300 | 113.400 | B |
| 8a1ef45830c7fff | Stari Grad Sarajevo | Mošćanica | 20 | 2,267.200 | 113.400 | A |
| 8a1ef45b6777fff | Vogošća | Krivoglavci | 10 | 1,134.000 | 113.400 | B |
| 8a1ef45b0337fff | Vogošća | Blagovac | 25 | 2,835.400 | 113.400 | B |
| 8a1ef4583717fff | Stari Grad Sarajevo | Vratnik | 131 | 14,859.100 | 113.400 | A |
| 8a1ef45869affff | Vogošća | Hotonj | 24 | 2,722.300 | 113.400 | B |
| 8a1ef45b60effff | Vogošća | Krivoglavci | 14 | 1,588.000 | 113.400 | B |
| 8a1ef4586577fff | Vogošća | Kobilja Glava | 35 | 3,971.000 | 113.500 | B |
| 8a1ea92e924ffff | Vogošća | Semizovac | 28 | 3,177.000 | 113.500 | B |
| 8a1ef45b06dffff | Vogošća | Uglješići | 17 | 1,929.100 | 113.500 | B |
| 8a1ef45b441ffff | Vogošća | Ljubina-Poturovići | 19 | 2,156.200 | 113.500 | B |
| 8a1ef4596607fff | Ilidža | Stupsko Brdo | 81 | 9,194.700 | 113.500 | B |
| 8a1ef4584d4ffff | Centar Sarajevo | Nahorevo | 13 | 1,476.500 | 113.600 | B |
| 8a1ef458450ffff | Centar Sarajevo | Betanija | 10 | 1,135.900 | 113.600 | B |
| 8a1ef45b3af7fff | Vogošća | Hotonj | 22 | 2,499.000 | 113.600 | B |
| 8a1ef6964d37fff | Ilidža | Plandište | 71 | 8,065.100 | 113.600 | B |
| 8a1ef459cd57fff | Centar Sarajevo | Skenderija-Podtekija | 210 | 23,862.200 | 113.600 | B |
| 8a1ef4586c8ffff | Vogošća | Kobilja Glava | 32 | 3,637.300 | 113.700 | B |
| 8a1ea92e920ffff | Vogošća | Semizovac | 16 | 1,818.700 | 113.700 | B |
| 8a1ef45b38c7fff | Vogošća | Ugorsko | 18 | 2,046.200 | 113.700 | B |
| 8a1ea92c8c9ffff | Novi Grad Sarajevo | Dobroševići | 89 | 10,118.900 | 113.700 | A |
| 8a1ef4582167fff | Centar Sarajevo | Koševo II | 119 | 13,530.600 | 113.700 | B |
| 8a1ef4590177fff | Novi Grad Sarajevo | Alipašin Most III | 157 | 17,852.100 | 113.700 | A |
| 8a1ef6965127fff | Ilidža | Ilidža | 19 | 2,160.600 | 113.700 | B |
| 8a1ef45b6067fff | Vogošća | Krivoglavci | 27 | 3,070.400 | 113.700 | B |
| 8a1ef45918c7fff | Novo Sarajevo | Željeznička | 127 | 14,442.800 | 113.700 | B |
| 8a1ef45b0077fff | Vogošća | Blagovac | 21 | 2,388.500 | 113.700 | B |
| 8a1ef4586437fff | Vogošća | Kobilja Glava | 34 | 3,867.300 | 113.700 | B |
| 8a1ef6961847fff | Ilidža | Donji Kotorac | 13 | 1,478.700 | 113.700 | B |
| 8a1ef45b0067fff | Vogošća | Blagovac | 21 | 2,389.200 | 113.800 | B |
| 8a1ef45b32cffff | Vogošća | Kobilja Glava | 12 | 1,366.000 | 113.800 | B |
| 8a1ef4582b77fff | Centar Sarajevo | Hrastovi-Mrkovići | 81 | 9,220.700 | 113.800 | B |
| 8a1ef45b4c87fff | Vogošća | Semizovac | 17 | 1,935.400 | 113.800 | B |
| 8a1ea92c972ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 47 | 5,351.200 | 113.900 | A |
| 8a1ef4583da7fff | Centar Sarajevo | Hrastovi-Mrkovići | 90 | 10,249.300 | 113.900 | B |
| 8a1ef45b3a0ffff | Vogošća | Hotonj | 27 | 3,075.800 | 113.900 | B |
| 8a1ef4582c5ffff | Centar Sarajevo | Koševsko Brdo | 127 | 14,469.600 | 113.900 | B |
| 8a1ef4582867fff | Centar Sarajevo | Koševo II | 65 | 7,405.800 | 113.900 | B |
| 8a1ea92cb6dffff | Ilidža | Pejton | 129 | 14,699.000 | 113.900 | B |
| 8a1ef45b3b57fff | Vogošća | Hotonj | 30 | 3,418.600 | 114.000 | B |
| 8a1ef45b0c47fff | Vogošća | Vogošća | 18 | 2,051.800 | 114.000 | B |
| 8a1ef458342ffff | Stari Grad Sarajevo | Sumbuluša | 197 | 22,458.300 | 114.000 | A |
| 8a1ea92ddb67fff | Ilidža | Lipe | 12 | 1,368.200 | 114.000 | B |
| 8a1ef4584097fff | Centar Sarajevo | Nahorevo | 19 | 2,166.400 | 114.000 | B |
| 8a1ef4580ca7fff | Centar Sarajevo | Pionirska Dolina | 49 | 5,587.300 | 114.000 | B |
| 8a1ea92cb8e7fff | Ilidža | Doglodi | 11 | 1,254.600 | 114.100 | B |
| 8a1ef458275ffff | Centar Sarajevo | Mejtaš-Bjelave | 164 | 18,712.600 | 114.100 | B |
| 8a1ef4586cb7fff | Vogošća | Hotonj | 31 | 3,537.400 | 114.100 | B |
| 8a1ef45958f7fff | Vogošća | Kobilja Glava | 12 | 1,369.400 | 114.100 | B |
| 8a1ef45b639ffff | Vogošća | Krivoglavci | 24 | 2,739.200 | 114.100 | B |
| 8a1ea92e9297fff | Vogošća | Svrake | 14 | 1,598.200 | 114.200 | B |
| 8a1ef4580c4ffff | Centar Sarajevo | Pionirska Dolina | 11 | 1,256.300 | 114.200 | B |
| 8a1ef6965937fff | Ilidža | Pejton | 17 | 1,941.700 | 114.200 | B |
| 8a1ef45828c7fff | Centar Sarajevo | Koševo II | 211 | 24,102.800 | 114.200 | B |
| 8a1ea92c9187fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 32 | 3,655.900 | 114.200 | A |
| 8a1ea92e9277fff | Vogošća | Semizovac | 14 | 1,599.500 | 114.200 | B |
| 8a1ef45b3167fff | Vogošća | Ugorsko | 16 | 1,828.300 | 114.300 | B |
| 8a1ef4586c17fff | Vogošća | Kobilja Glava | 28 | 3,200.200 | 114.300 | B |
| 8a1ef4591a67fff | Centar Sarajevo | Marijin Dvor | 167 | 19,088.300 | 114.300 | B |
| 8a1ef45929b7fff | Novi Grad Sarajevo | Saraj Polje | 59 | 6,743.900 | 114.300 | A |
| 8a1ef45b3ad7fff | Vogošća | Hotonj | 16 | 1,829.500 | 114.300 | B |
| 8a1ef45b6857fff | Vogošća | Svrake | 20 | 2,287.300 | 114.400 | B |
| 8a1ef45b0a0ffff | Vogošća | Blagovac | 18 | 2,059.100 | 114.400 | B |
| 8a1ef45b032ffff | Vogošća | Blagovac | 27 | 3,089.800 | 114.400 | B |
| 8a1ef69648c7fff | Ilidža | Vreoca | 10 | 1,144.500 | 114.400 | B |
| 8a1ef45b04affff | Vogošća | Vogošća | 24 | 2,748.000 | 114.500 | B |
| 8a1ef6965acffff | Ilidža | Stupsko Brdo | 61 | 6,987.700 | 114.600 | B |
| 8a1ef4596c0ffff | Novi Grad Sarajevo | Briješće | 16 | 1,833.300 | 114.600 | A |
| 8a1ef4580a27fff | Centar Sarajevo | Betanija | 17 | 1,948.100 | 114.600 | B |
| 8a1ef6965b4ffff | Ilidža | Stupsko Brdo | 16 | 1,834.100 | 114.600 | B |
| 8a1ef458338ffff | Stari Grad Sarajevo | Mošćanica | 18 | 2,063.500 | 114.600 | A |
| 8a1ef45b0a37fff | Vogošća | Blagovac | 14 | 1,605.100 | 114.600 | B |
| 8a1ef45b638ffff | Vogošća | Krivoglavci | 33 | 3,784.100 | 114.700 | B |
| 8a1ea92c938ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 29 | 3,325.500 | 114.700 | A |
| 8a1ef45b3a8ffff | Vogošća | Hotonj | 26 | 2,981.900 | 114.700 | B |
| 8a1ef45b0a2ffff | Vogošća | Blagovac | 14 | 1,605.700 | 114.700 | B |
| 8a1ef4582467fff | Centar Sarajevo | Ciglane | 318 | 36,475.800 | 114.700 | B |
| 8a1ef45b6047fff | Vogošća | Krivoglavci | 29 | 3,326.700 | 114.700 | B |
| 8a1ef4586b57fff | Centar Sarajevo | Betanija | 28 | 3,213.500 | 114.800 | B |
| 8a1ef4582a8ffff | Centar Sarajevo | Breka | 133 | 15,264.400 | 114.800 | B |
| 8a1ef45862cffff | Centar Sarajevo | Betanija | 169 | 19,398.200 | 114.800 | B |
| 8a1ef4583667fff | Stari Grad Sarajevo | Mošćanica | 22 | 2,525.700 | 114.800 | A |
| 8a1ef45b2867fff | Vogošća | Vogošća | 10 | 1,148.100 | 114.800 | B |
| 8a1ef4586d07fff | Vogošća | Hotonj | 26 | 2,985.200 | 114.800 | B |
| 8a1ef4592d37fff | Novi Grad Sarajevo | Saraj Polje | 54 | 6,201.400 | 114.800 | A |
| 8a1ef45b605ffff | Vogošća | Krivoglavci | 25 | 2,871.100 | 114.800 | B |
| 8a1ef45a22d7fff | Centar Sarajevo | Nahorevo | 15 | 1,724.000 | 114.900 | B |
| 8a1ef45b11b7fff | Vogošća | Vogošća | 12 | 1,379.300 | 114.900 | B |
| 8a1ef4580587fff | Centar Sarajevo | Pionirska Dolina | 60 | 6,900.300 | 115.000 | B |
| 8a1ef45b3a6ffff | Vogošća | Hotonj | 32 | 3,681.600 | 115.000 | B |
| 8a1ea92e9847fff | Vogošća | Donja Vogošća | 18 | 2,071.200 | 115.100 | B |
| 8a1ef45b3b8ffff | Vogošća | Hotonj | 34 | 3,913.100 | 115.100 | B |
| 8a1ea92ce4dffff | Ilidža | Lipe | 11 | 1,266.000 | 115.100 | B |
| 8a1ef4582637fff | Centar Sarajevo | Džidžikovac-Koševo I | 232 | 26,705.600 | 115.100 | B |
| 8a1ef45b3a47fff | Vogošća | Hotonj | 32 | 3,684.000 | 115.100 | B |
| 8a1ef4584957fff | Centar Sarajevo | Nahorevo | 13 | 1,496.800 | 115.100 | B |
| 8a1ef45b680ffff | Vogošća | Svrake | 19 | 2,187.800 | 115.100 | B |
| 8a1ef45b311ffff | Vogošća | Ugorsko | 12 | 1,381.900 | 115.200 | B |
| 8a1ef45b03b7fff | Vogošća | Blagovac | 41 | 4,723.300 | 115.200 | B |
| 8a1ef458665ffff | Centar Sarajevo | Džidžikovac-Koševo I | 101 | 11,637.900 | 115.200 | B |
| 8a1ef6965877fff | Ilidža | Naselje Bulevar | 24 | 2,765.900 | 115.200 | B |
| 8a1ea92c976ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 42 | 4,840.500 | 115.200 | A |
| 8a1ef4595947fff | Vogošća | Kobilja Glava | 21 | 2,420.800 | 115.300 | B |
| 8a1ea92ddaa7fff | Ilidža | Lipe | 14 | 1,613.800 | 115.300 | B |
| 8a1ef45b44d7fff | Vogošća | Ljubina-Poturovići | 26 | 2,997.300 | 115.300 | B |
| 8a1ea92c070ffff | Ilidža | Rakovica | 10 | 1,152.900 | 115.300 | B |
| 8a1ef45b16d7fff | Vogošća | Hotonj | 23 | 2,651.700 | 115.300 | B |
| 8a1ef4586367fff | Centar Sarajevo | Betanija | 17 | 1,960.100 | 115.300 | B |
| 8a1ef45b3b6ffff | Vogošća | Hotonj | 33 | 3,805.400 | 115.300 | B |
| 8a1ef4583d37fff | Centar Sarajevo | Hrastovi-Mrkovići | 62 | 7,149.800 | 115.300 | B |
| 8a1ef458656ffff | Vogošća | Kobilja Glava | 27 | 3,114.700 | 115.400 | B |
| 8a1ef4586927fff | Centar Sarajevo | Betanija | 29 | 3,346.400 | 115.400 | B |
| 8a1ea92e976ffff | Vogošća | Svrake | 12 | 1,384.800 | 115.400 | B |
| 8a1ea92c900ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 43 | 4,963.400 | 115.400 | A |
| 8a1ef4580d1ffff | Centar Sarajevo | Pionirska Dolina | 33 | 3,809.300 | 115.400 | B |
| 8a1ef4586877fff | Centar Sarajevo | Betanija | 22 | 2,539.700 | 115.400 | B |
| 8a1ef6964d4ffff | Ilidža | Plandište | 11 | 1,270.300 | 115.500 | B |
| 8a1ef45906cffff | Novo Sarajevo | Hrasno Brdo | 23 | 2,656.200 | 115.500 | B |
| 8a1ef4582887fff | Centar Sarajevo | Džidžikovac-Koševo I | 250 | 28,872.800 | 115.500 | B |
| 8a1ef45866effff | Centar Sarajevo | Koševsko Brdo | 62 | 7,160.700 | 115.500 | B |
| 8a1ef4583327fff | Stari Grad Sarajevo | Mošćanica | 15 | 1,732.800 | 115.500 | A |
| 8a1ef45b009ffff | Vogošća | Vogošća | 57 | 6,585.700 | 115.500 | B |
| 8a1ef45b6147fff | Vogošća | Krivoglavci | 23 | 2,657.400 | 115.500 | B |
| 8a1ef45b3b9ffff | Vogošća | Hotonj | 28 | 3,235.600 | 115.600 | B |
| 8a1ea92e90c7fff | Vogošća | Svrake | 10 | 1,155.800 | 115.600 | B |
| 8a1ef45b06d7fff | Vogošća | Uglješići | 16 | 1,849.400 | 115.600 | B |
| 8a1ef4582757fff | Centar Sarajevo | Džidžikovac-Koševo I | 143 | 16,531.200 | 115.600 | B |
| 8a1ea92c93b7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 39 | 4,509.100 | 115.600 | A |
| 8a1ea92e995ffff | Vogošća | Donja Vogošća | 12 | 1,387.500 | 115.600 | B |
| 8a1ea92cb66ffff | Ilidža | Pejton | 20 | 2,312.500 | 115.600 | B |
| 8a1ef459c8a7fff | Centar Sarajevo | Skenderija-Podtekija | 184 | 21,275.000 | 115.600 | B |
| 8a1ef458685ffff | Centar Sarajevo | Betanija | 25 | 2,890.800 | 115.600 | B |
| 8a1ef4582a57fff | Centar Sarajevo | Hrastovi-Mrkovići | 76 | 8,790.200 | 115.700 | B |
| 8a1ef45b6977fff | Vogošća | Svrake | 23 | 2,661.100 | 115.700 | B |
| 8a1ef4584c17fff | Centar Sarajevo | Betanija | 21 | 2,430.700 | 115.700 | B |
| 8a1ef458659ffff | Vogošća | Kobilja Glava | 35 | 4,051.300 | 115.800 | B |
| 8a1ef4586ce7fff | Vogošća | Kobilja Glava | 18 | 2,083.600 | 115.800 | B |
| 8a1ea92e9867fff | Vogošća | Donja Vogošća | 15 | 1,736.400 | 115.800 | B |
| 8a1ef4583d07fff | Centar Sarajevo | Hrastovi-Mrkovići | 81 | 9,379.100 | 115.800 | B |
| 8a1ef45861b7fff | Vogošća | Kobilja Glava | 13 | 1,505.400 | 115.800 | B |
| 8a1ef45b036ffff | Vogošća | Blagovac | 15 | 1,737.300 | 115.800 | B |
| 8a1ea92c98dffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 50 | 5,791.000 | 115.800 | A |
| 8a1ef45b38affff | Vogošća | Ugorsko | 15 | 1,737.700 | 115.800 | B |
| 8a1ef459c9a7fff | Centar Sarajevo | Trg oslobođenja-Centar | 212 | 24,565.900 | 115.900 | B |
| 8a1ef45b006ffff | Vogošća | Blagovac | 32 | 3,708.500 | 115.900 | B |
| 8a1ef458389ffff | Stari Grad Sarajevo | Sedrenik | 86 | 9,968.500 | 115.900 | A |
| 8a1ea92dd207fff | Ilidža | Blažuj | 13 | 1,507.000 | 115.900 | B |
| 8a1ef45805a7fff | Centar Sarajevo | Pionirska Dolina | 54 | 6,260.200 | 115.900 | B |
| 8a1ef45b0c77fff | Vogošća | Vogošća | 13 | 1,507.600 | 116.000 | B |
| 8a1ef45823b7fff | Centar Sarajevo | Park-Višnjik | 117 | 13,569.900 | 116.000 | B |
| 8a1ef45b030ffff | Vogošća | Blagovac | 30 | 3,480.800 | 116.000 | B |
| 8a1ef4582137fff | Centar Sarajevo | Džidžikovac-Koševo I | 135 | 15,665.700 | 116.000 | B |
| 8a1ef45854e7fff | Centar Sarajevo | Betanija | 10 | 1,160.500 | 116.100 | B |
| 8a1ef459d187fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 29 | 3,365.700 | 116.100 | A |
| 8a1ef4582647fff | Centar Sarajevo | Trg oslobođenja-Centar | 167 | 19,381.700 | 116.100 | B |
| 8a1ef458274ffff | Centar Sarajevo | Mejtaš-Bjelave | 151 | 17,526.900 | 116.100 | B |
| 8a1ea92c988ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 27 | 3,134.200 | 116.100 | A |
| 8a1ef45958b7fff | Vogošća | Kobilja Glava | 18 | 2,089.500 | 116.100 | B |
| 8a1ef458670ffff | Centar Sarajevo | Šip | 175 | 20,316.700 | 116.100 | B |
| 8a1ef45b3b47fff | Vogošća | Hotonj | 36 | 4,179.500 | 116.100 | B |
| 8a1ef459c997fff | Centar Sarajevo | Trg oslobođenja-Centar | 200 | 23,223.600 | 116.100 | B |
| 8a1ef45864a7fff | Vogošća | Kobilja Glava | 31 | 3,599.700 | 116.100 | B |
| 8a1ef45822b7fff | Centar Sarajevo | Mejtaš-Bjelave | 154 | 17,883.000 | 116.100 | B |
| 8a1ef4584847fff | Centar Sarajevo | Nahorevo | 11 | 1,277.500 | 116.100 | B |
| 8a1ef45b4567fff | Vogošća | Ljubina-Poturovići | 13 | 1,510.100 | 116.200 | B |
| 8a1ea92ca5affff | Ilidža | Blažuj | 73 | 8,480.400 | 116.200 | B |
| 8a1ea92c906ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 38 | 4,414.500 | 116.200 | A |
| 8a1ef45b3037fff | Vogošća | Ugorsko | 12 | 1,394.300 | 116.200 | B |
| 8a1ef459c9b7fff | Centar Sarajevo | Trg oslobođenja-Centar | 222 | 25,800.000 | 116.200 | B |
| 8a1ea92c916ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 42 | 4,882.900 | 116.300 | A |
| 8a1ea92dda77fff | Ilidža | Lipe | 13 | 1,511.600 | 116.300 | B |
| 8a1ef45b16c7fff | Vogošća | Hotonj | 18 | 2,093.100 | 116.300 | B |
| 8a1ef4592d77fff | Novi Grad Sarajevo | Saraj Polje | 55 | 6,397.000 | 116.300 | A |
| 8a1ef45826dffff | Centar Sarajevo | Trg oslobođenja-Centar | 185 | 21,517.200 | 116.300 | B |
| 8a1ea92c9647fff | Novi Grad Sarajevo | Briješće | 29 | 3,373.000 | 116.300 | A |
| 8a1ef458294ffff | Centar Sarajevo | Koševo II | 145 | 16,865.700 | 116.300 | B |
| 8a1ef45844c7fff | Centar Sarajevo | Betanija | 12 | 1,395.800 | 116.300 | B |
| 8a1ef4586a77fff | Centar Sarajevo | Betanija | 29 | 3,373.800 | 116.300 | B |
| 8a1ef459591ffff | Vogošća | Kobilja Glava | 17 | 1,977.900 | 116.300 | B |
| 8a1ef4582657fff | Centar Sarajevo | Trg oslobođenja-Centar | 321 | 37,352.800 | 116.400 | B |
| 8a1ef45b5227fff | Vogošća | Tihovići | 10 | 1,163.800 | 116.400 | B |
| 8a1ef4584ccffff | Centar Sarajevo | Betanija | 19 | 2,211.700 | 116.400 | B |
| 8a1ef45b011ffff | Vogošća | Vogošća | 28 | 3,259.600 | 116.400 | B |
| 8a1ef45b665ffff | Vogošća | Vogošća | 13 | 1,513.500 | 116.400 | B |
| 8a1ea92c9a97fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 33 | 3,842.500 | 116.400 | A |
| 8a1ef4582ceffff | Centar Sarajevo | Koševsko Brdo | 187 | 21,778.400 | 116.500 | B |
| 8a1ea92dd927fff | Ilidža | Gladno polje | 13 | 1,514.400 | 116.500 | B |
| 8a1ef45b6947fff | Vogošća | Svrake | 17 | 1,980.600 | 116.500 | B |
| 8a1ea92e996ffff | Vogošća | Donja Vogošća | 14 | 1,631.200 | 116.500 | B |
| 8a1ef458085ffff | Centar Sarajevo | Betanija | 22 | 2,563.700 | 116.500 | B |
| 8a1ea92c0737fff | Ilidža | Rakovica | 10 | 1,165.300 | 116.500 | B |
| 8a1ef45b614ffff | Vogošća | Krivoglavci | 21 | 2,447.400 | 116.500 | B |
| 8a1ef4586d47fff | Vogošća | Hotonj | 19 | 2,215.700 | 116.600 | B |
| 8a1ef4582697fff | Centar Sarajevo | Marijin Dvor | 160 | 18,658.300 | 116.600 | B |
| 8a1ef4580b5ffff | Centar Sarajevo | Betanija | 12 | 1,399.400 | 116.600 | B |
| 8a1ef45b3a87fff | Vogošća | Hotonj | 26 | 3,032.200 | 116.600 | B |
| 8a1ef45b0087fff | Vogošća | Vogošća | 51 | 5,949.700 | 116.700 | B |
| 8a1ea92c92e7fff | Novi Grad Sarajevo | Briješće | 19 | 2,216.600 | 116.700 | A |
| 8a1ef45b3847fff | Vogošća | Ugorsko | 38 | 4,433.400 | 116.700 | B |
| 8a1ef45b01b7fff | Vogošća | Vogošća | 30 | 3,500.100 | 116.700 | B |
| 8a1ef45b686ffff | Vogošća | Semizovac | 28 | 3,266.900 | 116.700 | B |
| 8a1ef4582a87fff | Centar Sarajevo | Breka | 351 | 40,955.200 | 116.700 | B |
| 8a1ef69638effff | Ilidža | Hrasnica | 86 | 10,034.900 | 116.700 | B |
| 8a1ef4582617fff | Centar Sarajevo | Džidžikovac-Koševo I | 245 | 28,592.100 | 116.700 | B |
| 8a1ef45b161ffff | Vogošća | Hotonj | 28 | 3,268.000 | 116.700 | B |
| 8a1ef45b0377fff | Vogošća | Blagovac | 27 | 3,151.500 | 116.700 | B |
| 8a1ef4580537fff | Centar Sarajevo | Pionirska Dolina | 54 | 6,304.200 | 116.700 | B |
| 8a1ef4586b47fff | Centar Sarajevo | Betanija | 27 | 3,152.100 | 116.700 | B |
| 8a1ef45b6077fff | Vogošća | Krivoglavci | 25 | 2,918.800 | 116.800 | B |
| 8a1ef458228ffff | Centar Sarajevo | Mejtaš-Bjelave | 156 | 18,215.000 | 116.800 | B |
| 8a1ef45b00f7fff | Vogošća | Vogošća | 45 | 5,255.000 | 116.800 | B |
| 8a1ef45b0417fff | Vogošća | Vogošća | 40 | 4,671.700 | 116.800 | B |
| 8a1ef45b2b77fff | Vogošća | Vogošća | 14 | 1,635.300 | 116.800 | B |
| 8a1ea92cd5a7fff | Novi Grad Sarajevo | Dobroševići | 13 | 1,518.600 | 116.800 | A |
| 8a1ef4595827fff | Vogošća | Kobilja Glava | 23 | 2,687.000 | 116.800 | B |
| 8a1ef459cd6ffff | Centar Sarajevo | Skenderija-Podtekija | 162 | 18,926.300 | 116.800 | B |
| 8a1ef45964b7fff | Ilidža | Naselje Bulevar | 19 | 2,220.400 | 116.900 | B |
| 8a1ef45834a7fff | Stari Grad Sarajevo | Kovači | 109 | 12,738.000 | 116.900 | A |
| 8a1ef45b634ffff | Vogošća | Vogošća | 10 | 1,168.700 | 116.900 | B |
| 8a1ef45b005ffff | Vogošća | Blagovac | 39 | 4,558.500 | 116.900 | B |
| 8a1ea92e936ffff | Vogošća | Nebočaj | 14 | 1,636.500 | 116.900 | B |
| 8a1ef6961cf7fff | Ilidža | Sokolović-kolonija | 11 | 1,286.200 | 116.900 | B |
| 8a1ef45b3ab7fff | Vogošća | Hotonj | 24 | 2,806.400 | 116.900 | B |
| 8a1ef45b12dffff | Centar Sarajevo | Betanija | 19 | 2,222.300 | 117.000 | B |
| 8a1ef459598ffff | Vogošća | Kobilja Glava | 11 | 1,286.800 | 117.000 | B |
| 8a1ea92ddad7fff | Ilidža | Lipe | 15 | 1,754.800 | 117.000 | B |
| 8a1ea92cba8ffff | Ilidža | Azići | 10 | 1,170.100 | 117.000 | B |
| 8a1ef45b06affff | Vogošća | Uglješići | 30 | 3,511.100 | 117.000 | B |
| 8a1ef6963a8ffff | Ilidža | Lasica | 42 | 4,916.200 | 117.100 | B |
| 8a1ea92c9777fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 55 | 6,438.100 | 117.100 | A |
| 8a1ef4582b5ffff | Centar Sarajevo | Hrastovi-Mrkovići | 65 | 7,609.300 | 117.100 | B |
| 8a1ef45846cffff | Centar Sarajevo | Betanija | 25 | 2,928.600 | 117.100 | B |
| 8a1ef4583757fff | Stari Grad Sarajevo | Mošćanica | 15 | 1,757.200 | 117.100 | A |
| 8a1ef459d937fff | Stari Grad Sarajevo | Mošćanica | 18 | 2,108.900 | 117.200 | A |
| 8a1ef45b00e7fff | Vogošća | Vogošća | 45 | 5,273.200 | 117.200 | B |
| 8a1ef45b0197fff | Vogošća | Vogošća | 28 | 3,281.300 | 117.200 | B |
| 8a1ef45b3aa7fff | Vogošća | Hotonj | 37 | 4,336.200 | 117.200 | B |
| 8a1ea92e9a07fff | Vogošća | Nebočaj | 13 | 1,523.800 | 117.200 | B |
| 8a1ef45b1697fff | Vogošća | Hotonj | 36 | 4,220.100 | 117.200 | B |
| 8a1ef4583a8ffff | Stari Grad Sarajevo | Mošćanica | 20 | 2,345.600 | 117.300 | A |
| 8a1ef6965b1ffff | Ilidža | Naselje Bulevar | 23 | 2,698.100 | 117.300 | B |
| 8a1ef4592d17fff | Novi Grad Sarajevo | Saraj Polje | 77 | 9,033.100 | 117.300 | A |
| 8a1ef45b63affff | Vogošća | Krivoglavci | 27 | 3,168.800 | 117.400 | B |
| 8a1ef6965ae7fff | Ilidža | Naselje Bulevar | 23 | 2,699.900 | 117.400 | B |
| 8a1ef6965a27fff | Ilidža | Naselje Bulevar | 21 | 2,465.400 | 117.400 | B |
| 8a1ef45b16b7fff | Vogošća | Hotonj | 36 | 4,226.800 | 117.400 | B |
| 8a1ea92e9a27fff | Vogošća | Nebočaj | 14 | 1,643.800 | 117.400 | B |
| 8a1ef45b615ffff | Vogošća | Krivoglavci | 25 | 2,935.600 | 117.400 | B |
| 8a1ef4586a0ffff | Centar Sarajevo | Betanija | 33 | 3,875.800 | 117.400 | B |
| 8a1ef45b12c7fff | Centar Sarajevo | Betanija | 65 | 7,634.700 | 117.500 | B |
| 8a1ef459690ffff | Novi Grad Sarajevo | Briješće | 23 | 2,702.100 | 117.500 | A |
| 8a1ef45b0ad7fff | Vogošća | Blagovac | 25 | 2,937.300 | 117.500 | B |
| 8a1ef45b6397fff | Vogošća | Krivoglavci | 25 | 2,937.300 | 117.500 | B |
| 8a1ef4583d17fff | Centar Sarajevo | Hrastovi-Mrkovići | 85 | 9,989.300 | 117.500 | B |
| 8a1ea92e921ffff | Vogošća | Semizovac | 22 | 2,585.700 | 117.500 | B |
| 8a1ef4582b07fff | Centar Sarajevo | Hrastovi-Mrkovići | 66 | 7,758.300 | 117.500 | B |
| 8a1ef4596957fff | Novi Grad Sarajevo | Briješće | 26 | 3,057.200 | 117.600 | A |
| 8a1ef458460ffff | Centar Sarajevo | Betanija | 10 | 1,176.100 | 117.600 | B |
| 8a1ea92ce727fff | Ilidža | Lipe | 11 | 1,293.900 | 117.600 | B |
| 8a1ef45b286ffff | Vogošća | Vogošća | 19 | 2,235.200 | 117.600 | B |
| 8a1ea92e994ffff | Vogošća | Donja Vogošća | 21 | 2,470.600 | 117.600 | B |
| 8a1ef45b0a57fff | Vogošća | Blagovac | 13 | 1,529.700 | 117.700 | B |
| 8a1ef6965c6ffff | Ilidža | Ilidža | 20 | 2,353.500 | 117.700 | B |
| 8a1ef458285ffff | Centar Sarajevo | Koševo II | 94 | 11,062.300 | 117.700 | B |
| 8a1ea92cb2e7fff | Ilidža | Azići | 74 | 8,709.100 | 117.700 | B |
| 8a1ef45b63b7fff | Vogošća | Krivoglavci | 37 | 4,355.000 | 117.700 | B |
| 8a1ef4596b9ffff | Novi Grad Sarajevo | Briješće | 27 | 3,178.200 | 117.700 | A |
| 8a1ef459650ffff | Ilidža | Stup | 21 | 2,472.200 | 117.700 | B |
| 8a1ef45966effff | Novi Grad Sarajevo | Saraj Polje | 68 | 8,008.800 | 117.800 | A |
| 8a1ea92c9057fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 49 | 5,771.900 | 117.800 | A |
| 8a1ea92cc25ffff | Novi Grad Sarajevo | Dobroševići | 15 | 1,767.200 | 117.800 | A |
| 8a1ef45b6827fff | Vogošća | Svrake | 24 | 2,827.800 | 117.800 | B |
| 8a1ef4585547fff | Centar Sarajevo | Betanija | 10 | 1,178.500 | 117.900 | B |
| 8a1ef45b6b07fff | Vogošća | Semizovac | 26 | 3,064.800 | 117.900 | B |
| 8a1ea92ddb1ffff | Ilidža | Lipe | 13 | 1,532.400 | 117.900 | B |
| 8a1ef45b0387fff | Vogošća | Blagovac | 49 | 5,776.200 | 117.900 | B |
| 8a1ef45b0cc7fff | Vogošća | Vogošća | 21 | 2,475.800 | 117.900 | B |
| 8a1ea92c8177fff | Novi Grad Sarajevo | Dobroševići | 13 | 1,532.700 | 117.900 | A |
| 8a1ea925b99ffff | Vogošća | Gora | 10 | 1,179.000 | 117.900 | B |
| 8a1ef45b0207fff | Vogošća | Blagovac | 43 | 5,069.800 | 117.900 | B |
| 8a1ef45b3c1ffff | Vogošća | Ugorsko | 10 | 1,179.100 | 117.900 | B |
| 8a1ef45b52f7fff | Vogošća | Tihovići | 10 | 1,179.100 | 117.900 | B |
| 8a1ef45b44f7fff | Vogošća | Ljubina-Poturovići | 21 | 2,476.500 | 117.900 | B |
| 8a1ef45b0427fff | Vogošća | Vogošća | 57 | 6,722.700 | 117.900 | B |
| 8a1ea92c92affff | Novi Grad Sarajevo | Briješće | 13 | 1,534.100 | 118.000 | A |
| 8a1ef45b0527fff | Vogošća | Vogošća | 17 | 2,006.100 | 118.000 | B |
| 8a1ef4586cc7fff | Vogošća | Kobilja Glava | 29 | 3,422.700 | 118.000 | B |
| 8a1ea92c9177fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 56 | 6,611.000 | 118.100 | A |
| 8a1ef4595997fff | Vogošća | Kobilja Glava | 16 | 1,888.900 | 118.100 | B |
| 8a1ef45b2c5ffff | Vogošća | Krivoglavci | 18 | 2,125.100 | 118.100 | B |
| 8a1ef6965137fff | Ilidža | Ilidža | 11 | 1,298.700 | 118.100 | B |
| 8a1ef4584807fff | Centar Sarajevo | Nahorevo | 16 | 1,889.100 | 118.100 | B |
| 8a1ef4583627fff | Stari Grad Sarajevo | Mošćanica | 40 | 4,723.100 | 118.100 | A |
| 8a1ea92c9307fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 35 | 4,133.100 | 118.100 | A |
| 8a1ef459676ffff | Ilidža | Stupsko Brdo | 23 | 2,716.500 | 118.100 | B |
| 8a1ef4586987fff | Vogošća | Hotonj | 16 | 1,889.800 | 118.100 | B |
| 8a1ef4586407fff | Centar Sarajevo | Šip | 52 | 6,142.800 | 118.100 | B |
| 8a1ea925a587fff | Vogošća | Donja Vogošća | 13 | 1,535.800 | 118.100 | B |
| 8a1ef4592d8ffff | Novi Grad Sarajevo | Dobrinja A | 98 | 11,579.200 | 118.200 | A |
| 8a1ef459cd47fff | Centar Sarajevo | Skenderija-Podtekija | 221 | 26,114.400 | 118.200 | B |
| 8a1ef4582797fff | Centar Sarajevo | Crni Vrh-Gorica | 141 | 16,661.700 | 118.200 | B |
| 8a1ef45b002ffff | Vogošća | Blagovac | 21 | 2,482.200 | 118.200 | B |
| 8a1ef45b04cffff | Vogošća | Vogošća | 25 | 2,955.500 | 118.200 | B |
| 8a1ef4586547fff | Vogošća | Kobilja Glava | 46 | 5,439.100 | 118.200 | B |
| 8a1ef45865affff | Vogošća | Kobilja Glava | 39 | 4,611.500 | 118.200 | B |
| 8a1ef45b0037fff | Vogošća | Vogošća | 35 | 4,139.300 | 118.300 | B |
| 8a1ef458654ffff | Vogošća | Kobilja Glava | 56 | 6,623.800 | 118.300 | B |
| 8a1ef45b001ffff | Vogošća | Vogošća | 26 | 3,075.800 | 118.300 | B |
| 8a1ea92cc247fff | Novi Grad Sarajevo | Dobroševići | 14 | 1,656.300 | 118.300 | A |
| 8a1ef45959affff | Vogošća | Kobilja Glava | 13 | 1,538.100 | 118.300 | B |
| 8a1ea92c9147fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 54 | 6,389.200 | 118.300 | A |
| 8a1ef4580daffff | Centar Sarajevo | Pionirska Dolina | 29 | 3,431.600 | 118.300 | B |
| 8a1ea92c9767fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 57 | 6,745.900 | 118.300 | A |
| 8a1ea92c9167fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 57 | 6,745.900 | 118.300 | A |
| 8a1ea92c966ffff | Novi Grad Sarajevo | Briješće | 26 | 3,077.100 | 118.300 | A |
| 8a1ef69656e7fff | Ilidža | Butmir | 12 | 1,420.400 | 118.400 | B |
| 8a1ef45b109ffff | Vogošća | Hotonj | 18 | 2,130.800 | 118.400 | B |
| 8a1ef45a264ffff | Centar Sarajevo | Nahorevo | 10 | 1,183.800 | 118.400 | B |
| 8a1ef45b06cffff | Vogošća | Vogošća | 21 | 2,486.500 | 118.400 | B |
| 8a1ef45b19b7fff | Vogošća | Tihovići | 12 | 1,420.900 | 118.400 | B |
| 8a1ef4580a0ffff | Centar Sarajevo | Betanija | 17 | 2,013.000 | 118.400 | B |
| 8a1ef4582627fff | Centar Sarajevo | Džidžikovac-Koševo I | 259 | 30,680.200 | 118.500 | B |
| 8a1ef45b1d97fff | Vogošća | Blagovac | 10 | 1,184.900 | 118.500 | B |
| 8a1ea92e92e7fff | Vogošća | Semizovac | 17 | 2,014.400 | 118.500 | B |
| 8a1ef45b38dffff | Vogošća | Ugorsko | 16 | 1,896.000 | 118.500 | B |
| 8a1ef45968c7fff | Novi Grad Sarajevo | Briješće | 28 | 3,318.300 | 118.500 | A |
| 8a1ef6961a1ffff | Ilidža | Donji Kotorac | 100 | 11,851.600 | 118.500 | B |
| 8a1ef45b162ffff | Vogošća | Hotonj | 17 | 2,015.400 | 118.600 | B |
| 8a1ea92cd467fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,186.000 | 118.600 | A |
| 8a1ea92e92b7fff | Vogošća | Svrake | 22 | 2,609.700 | 118.600 | B |
| 8a1ef69611a7fff | Ilidža | Butmir | 10 | 1,186.300 | 118.600 | B |
| 8a1ef4596867fff | Novi Grad Sarajevo | Briješće | 27 | 3,203.500 | 118.600 | A |
| 8a1ef45b6b1ffff | Vogošća | Ljubina-Poturovići | 16 | 1,898.500 | 118.700 | B |
| 8a1ef45b4527fff | Vogošća | Semizovac | 16 | 1,898.500 | 118.700 | B |
| 8a1ef45828affff | Centar Sarajevo | Džidžikovac-Koševo I | 113 | 13,409.700 | 118.700 | B |
| 8a1ef4582c57fff | Centar Sarajevo | Koševsko Brdo | 141 | 16,735.000 | 118.700 | B |
| 8a1ef45b01affff | Vogošća | Vogošća | 29 | 3,442.500 | 118.700 | B |
| 8a1ef45857b7fff | Centar Sarajevo | Betanija | 12 | 1,424.700 | 118.700 | B |
| 8a1ef458089ffff | Centar Sarajevo | Betanija | 12 | 1,424.700 | 118.700 | B |
| 8a1ea92c881ffff | Novi Grad Sarajevo | Dobroševići | 14 | 1,663.100 | 118.800 | A |
| 8a1ef45b296ffff | Vogošća | Vogošća | 27 | 3,207.500 | 118.800 | B |
| 8a1ef45b6387fff | Vogošća | Krivoglavci | 37 | 4,395.700 | 118.800 | B |
| 8a1ef4591b47fff | Centar Sarajevo | Marijin Dvor | 210 | 24,949.300 | 118.800 | B |
| 8a1ef4583b07fff | Stari Grad Sarajevo | Mošćanica | 12 | 1,425.700 | 118.800 | A |
| 8a1ef45b3147fff | Vogošća | Ugorsko | 17 | 2,020.000 | 118.800 | B |
| 8a1ef4586d2ffff | Vogošća | Hotonj | 32 | 3,802.800 | 118.800 | B |
| 8a1ef45b336ffff | Vogošća | Hotonj | 32 | 3,803.100 | 118.800 | B |
| 8a1ef458358ffff | Stari Grad Sarajevo | Kovači | 102 | 12,123.300 | 118.900 | A |
| 8a1ef459cd77fff | Centar Sarajevo | Skenderija-Podtekija | 270 | 32,093.900 | 118.900 | B |
| 8a1ef45b14affff | Vogošća | Hotonj | 44 | 5,230.300 | 118.900 | B |
| 8a1ef4580c0ffff | Centar Sarajevo | Pionirska Dolina | 37 | 4,399.700 | 118.900 | B |
| 8a1ea925a48ffff | Vogošća | Nebočaj | 12 | 1,427.100 | 118.900 | B |
| 8a1ef45b2ba7fff | Vogošća | Vogošća | 17 | 2,022.100 | 118.900 | B |
| 8a1ea92ca95ffff | Ilidža | Dolovi | 10 | 1,190.100 | 119.000 | B |
| 8a1ef45b0477fff | Vogošća | Vogošća | 75 | 8,927.500 | 119.000 | B |
| 8a1ef4595877fff | Vogošća | Kobilja Glava | 16 | 1,905.000 | 119.100 | B |
| 8a1ef696026ffff | Ilidža | Sokolović-kolonija | 10 | 1,190.700 | 119.100 | B |
| 8a1ef45b0497fff | Vogošća | Vogošća | 20 | 2,381.500 | 119.100 | B |
| 8a1ef4586557fff | Vogošća | Kobilja Glava | 54 | 6,431.300 | 119.100 | B |
| 8a1ea92c8887fff | Novi Grad Sarajevo | Dobroševići | 16 | 1,906.000 | 119.100 | A |
| 8a1ef45b6957fff | Vogošća | Svrake | 35 | 4,170.500 | 119.200 | B |
| 8a1ef45b3aaffff | Vogošća | Hotonj | 37 | 4,409.300 | 119.200 | B |
| 8a1ea92ddb57fff | Ilidža | Lipe | 15 | 1,787.600 | 119.200 | B |
| 8a1ef45b160ffff | Vogošća | Hotonj | 18 | 2,145.200 | 119.200 | B |
| 8a1ef45b1db7fff | Vogošća | Blagovac | 13 | 1,549.500 | 119.200 | B |
| 8a1ea92e9227fff | Vogošća | Semizovac | 11 | 1,311.200 | 119.200 | B |
| 8a1ef45b0327fff | Vogošća | Blagovac | 38 | 4,530.400 | 119.200 | B |
| 8a1ef45b694ffff | Vogošća | Semizovac | 34 | 4,054.100 | 119.200 | B |
| 8a1ef45b14e7fff | Vogošća | Hotonj | 40 | 4,770.100 | 119.300 | B |
| 8a1ea92ddba7fff | Ilidža | Lipe | 11 | 1,311.800 | 119.300 | B |
| 8a1ef45b14d7fff | Vogošća | Hotonj | 54 | 6,441.500 | 119.300 | B |
| 8a1ef45b129ffff | Centar Sarajevo | Betanija | 14 | 1,670.000 | 119.300 | B |
| 8a1ef69648f7fff | Ilidža | Kamenjača | 12 | 1,431.500 | 119.300 | B |
| 8a1ef45b1417fff | Vogošća | Hotonj | 40 | 4,772.200 | 119.300 | B |
| 8a1ea92c9047fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 50 | 5,965.600 | 119.300 | A |
| 8a1ef45b042ffff | Vogošća | Vogošća | 70 | 8,352.100 | 119.300 | B |
| 8a1ef45862d7fff | Centar Sarajevo | Betanija | 73 | 8,710.300 | 119.300 | B |
| 8a1ef4586c87fff | Vogošća | Hotonj | 36 | 4,296.500 | 119.300 | B |
| 8a1ea92c912ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 53 | 6,325.700 | 119.400 | A |
| 8a1ef45b146ffff | Vogošća | Hotonj | 32 | 3,820.200 | 119.400 | B |
| 8a1ef45b1747fff | Vogošća | Hotonj | 12 | 1,433.100 | 119.400 | B |
| 8a1ea925a59ffff | Vogošća | Donja Vogošća | 10 | 1,194.500 | 119.400 | B |
| 8a1ef4582c27fff | Centar Sarajevo | Donji Velešići | 89 | 10,631.200 | 119.500 | B |
| 8a1ea92cb0d7fff | Ilidža | Otes | 10 | 1,194.600 | 119.500 | B |
| 8a1ef4592d9ffff | Novi Grad Sarajevo | Dobrinja A | 86 | 10,274.300 | 119.500 | A |
| 8a1ef4582387fff | Centar Sarajevo | Mejtaš-Bjelave | 182 | 21,745.100 | 119.500 | B |
| 8a1ef4592997fff | Novi Grad Sarajevo | Saraj Polje | 74 | 8,844.500 | 119.500 | A |
| 8a1ea92c9387fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 50 | 5,976.500 | 119.500 | A |
| 8a1ef458658ffff | Vogošća | Kobilja Glava | 45 | 5,379.300 | 119.500 | B |
| 8a1ef45b62f7fff | Vogošća | Vogošća | 13 | 1,554.000 | 119.500 | B |
| 8a1ea92c974ffff | Novi Grad Sarajevo | Briješće | 39 | 4,662.800 | 119.600 | A |
| 8a1ea92e9857fff | Vogošća | Donja Vogošća | 10 | 1,195.700 | 119.600 | B |
| 8a1ea92cb2d7fff | Ilidža | Azići | 22 | 2,630.900 | 119.600 | B |
| 8a1ef45a229ffff | Centar Sarajevo | Nahorevo | 11 | 1,315.500 | 119.600 | B |
| 8a1ef4586867fff | Centar Sarajevo | Betanija | 24 | 2,870.400 | 119.600 | B |
| 8a1ef45b4537fff | Vogošća | Semizovac | 20 | 2,392.100 | 119.600 | B |
| 8a1ef45b682ffff | Vogošća | Svrake | 37 | 4,425.800 | 119.600 | B |
| 8a1ef6960a77fff | Ilidža | Sokolović-kolonija | 147 | 17,586.400 | 119.600 | B |
| 8a1ef4586d9ffff | Vogošća | Hotonj | 39 | 4,666.000 | 119.600 | B |
| 8a1ef6965ab7fff | Ilidža | Naselje Bulevar | 19 | 2,273.600 | 119.700 | B |
| 8a1ef4592d07fff | Novi Grad Sarajevo | Saraj Polje | 74 | 8,855.200 | 119.700 | A |
| 8a1ef4592ccffff | Novi Grad Sarajevo | Dobrinja A | 110 | 13,165.200 | 119.700 | A |
| 8a1ef4586caffff | Vogošća | Kobilja Glava | 37 | 4,428.900 | 119.700 | B |
| 8a1ef45b179ffff | Vogošća | Hotonj | 35 | 4,189.700 | 119.700 | B |
| 8a1ef4583407fff | Stari Grad Sarajevo | Kovači | 99 | 11,851.000 | 119.700 | A |
| 8a1ef4595977fff | Vogošća | Kobilja Glava | 33 | 3,951.000 | 119.700 | B |
| 8a1ef4595957fff | Vogošća | Kobilja Glava | 29 | 3,472.400 | 119.700 | B |
| 8a1ef45b6877fff | Vogošća | Svrake | 40 | 4,789.500 | 119.700 | B |
| 8a1ef6961047fff | Ilidža | Donji Kotorac | 13 | 1,557.100 | 119.800 | B |
| 8a1ef6965957fff | Ilidža | Naselje Bulevar | 17 | 2,036.300 | 119.800 | B |
| 8a1ef45b0c4ffff | Vogošća | Vogošća | 17 | 2,036.400 | 119.800 | B |
| 8a1ef4582297fff | Centar Sarajevo | Mejtaš-Bjelave | 227 | 27,192.600 | 119.800 | B |
| 8a1ef45b3b5ffff | Vogošća | Hotonj | 43 | 5,151.900 | 119.800 | B |
| 8a1ef45b32d7fff | Vogošća | Kobilja Glava | 26 | 3,115.400 | 119.800 | B |
| 8a1ef45a2287fff | Centar Sarajevo | Nahorevo | 10 | 1,198.400 | 119.800 | B |
| 8a1ea92c0637fff | Ilidža | Rakovica | 11 | 1,318.800 | 119.900 | B |
| 8a1ef45b6967fff | Vogošća | Svrake | 27 | 3,237.900 | 119.900 | B |
| 8a1ef45b3a27fff | Vogošća | Hotonj | 47 | 5,636.500 | 119.900 | B |
| 8a1ef45b0547fff | Vogošća | Vogošća | 68 | 8,154.900 | 119.900 | B |
| 8a1ef4584557fff | Centar Sarajevo | Betanija | 12 | 1,439.400 | 119.900 | B |
| 8a1ef459670ffff | Ilidža | Stupsko Brdo | 31 | 3,719.400 | 120.000 | B |
| 8a1ef45b0aa7fff | Vogošća | Blagovac | 25 | 2,999.700 | 120.000 | B |
| 8a1ef45b0ca7fff | Vogošća | Vogošća | 15 | 1,800.000 | 120.000 | B |
| 8a1ef45b0c0ffff | Vogošća | Vogošća | 23 | 2,760.000 | 120.000 | B |
| 8a1ef45b2b37fff | Vogošća | Vogošća | 39 | 4,681.800 | 120.000 | B |
| 8a1ea92e922ffff | Vogošća | Semizovac | 18 | 2,160.900 | 120.000 | B |
| 8a1ef4580b87fff | Centar Sarajevo | Betanija | 10 | 1,200.600 | 120.100 | B |
| 8a1ef45b331ffff | Vogošća | Grahovište | 10 | 1,200.800 | 120.100 | B |
| 8a1ef45b21affff | Novi Grad Sarajevo | Zabrđe | 12 | 1,441.200 | 120.100 | A |
| 8a1ea92c914ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 57 | 6,846.900 | 120.100 | A |
| 8a1ef6964887fff | Ilidža | Kamenjača | 12 | 1,441.500 | 120.100 | B |
| 8a1ef459581ffff | Vogošća | Kobilja Glava | 14 | 1,681.800 | 120.100 | B |
| 8a1ea92e9a97fff | Vogošća | Semizovac | 18 | 2,162.800 | 120.200 | B |
| 8a1ef4582207fff | Centar Sarajevo | Bardakčije | 125 | 15,020.300 | 120.200 | B |
| 8a1ef45966d7fff | Novi Grad Sarajevo | Saraj Polje | 71 | 8,531.700 | 120.200 | A |
| 8a1ef4595837fff | Vogošća | Kobilja Glava | 18 | 2,163.000 | 120.200 | B |
| 8a1ea92ca2d7fff | Ilidža | Osjek | 10 | 1,201.800 | 120.200 | B |
| 8a1ef459d19ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 31 | 3,727.400 | 120.200 | A |
| 8a1ef45b328ffff | Vogošća | Kobilja Glava | 19 | 2,284.600 | 120.200 | B |
| 8a1ef45b14f7fff | Vogošća | Hotonj | 55 | 6,614.400 | 120.300 | B |
| 8a1ef45b1787fff | Vogošća | Hotonj | 31 | 3,728.400 | 120.300 | B |
| 8a1ef4595d6ffff | Vogošća | Kobilja Glava | 17 | 2,044.600 | 120.300 | B |
| 8a1ef459299ffff | Novi Grad Sarajevo | Saraj Polje | 66 | 7,939.300 | 120.300 | A |
| 8a1ea92c9357fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 37 | 4,451.100 | 120.300 | A |
| 8a1ef458049ffff | Centar Sarajevo | Hrastovi-Mrkovići | 73 | 8,784.100 | 120.300 | B |
| 8a1ea92cb68ffff | Ilidža | Pejton | 86 | 10,348.800 | 120.300 | B |
| 8a1ea92e986ffff | Vogošća | Donja Vogošća | 17 | 2,045.900 | 120.300 | B |
| 8a1ef6960367fff | Ilidža | Sokolović-kolonija | 16 | 1,926.200 | 120.400 | B |
| 8a1ea92e9a37fff | Vogošća | Nebočaj | 15 | 1,806.300 | 120.400 | B |
| 8a1ef45b4d97fff | Vogošća | Nebočaj | 20 | 2,409.000 | 120.400 | B |
| 8a1ef45b00b7fff | Vogošća | Vogošća | 75 | 9,035.200 | 120.500 | B |
| 8a1ea92dd907fff | Ilidža | Gladno polje | 14 | 1,686.800 | 120.500 | B |
| 8a1ef45b1d87fff | Vogošća | Blagovac | 20 | 2,409.800 | 120.500 | B |
| 8a1ef45b145ffff | Vogošća | Hotonj | 31 | 3,735.300 | 120.500 | B |
| 8a1ef45b0cf7fff | Vogošća | Vogošća | 25 | 3,013.200 | 120.500 | B |
| 8a1ef458698ffff | Vogošća | Hotonj | 22 | 2,651.700 | 120.500 | B |
| 8a1ea92e938ffff | Vogošća | Semizovac | 11 | 1,326.000 | 120.500 | B |
| 8a1ef6963ab7fff | Ilidža | Lasica | 12 | 1,446.600 | 120.600 | B |
| 8a1ef45b0737fff | Vogošća | Vogošća | 78 | 9,403.000 | 120.600 | B |
| 8a1ef45841affff | Centar Sarajevo | Nahorevo | 26 | 3,134.300 | 120.600 | B |
| 8a1ef45b084ffff | Vogošća | Vogošća | 13 | 1,567.600 | 120.600 | B |
| 8a1ef45b054ffff | Vogošća | Vogošća | 82 | 9,889.200 | 120.600 | B |
| 8a1ef4584cc7fff | Centar Sarajevo | Betanija | 10 | 1,206.100 | 120.600 | B |
| 8a1ef45b0227fff | Vogošća | Blagovac | 49 | 5,913.300 | 120.700 | B |
| 8a1ea92e90dffff | Vogošća | Svrake | 13 | 1,568.900 | 120.700 | B |
| 8a1ea92c93a7fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 52 | 6,276.900 | 120.700 | A |
| 8a1ea925b137fff | Vogošća | Gora | 15 | 1,810.700 | 120.700 | B |
| 8a1ef45b3d4ffff | Vogošća | Ugorsko | 14 | 1,690.300 | 120.700 | B |
| 8a1ef45b16dffff | Vogošća | Hotonj | 42 | 5,071.900 | 120.800 | B |
| 8a1ea92cbd5ffff | Ilidža | Doglodi | 10 | 1,207.600 | 120.800 | B |
| 8a1ef45b0cd7fff | Vogošća | Vogošća | 31 | 3,743.600 | 120.800 | B |
| 8a1ef45b0a6ffff | Vogošća | Blagovac | 19 | 2,294.600 | 120.800 | B |
| 8a1ef4592caffff | Novi Grad Sarajevo | Dobrinja A | 118 | 14,250.800 | 120.800 | A |
| 8a1ef459668ffff | Novi Grad Sarajevo | Saraj Polje | 76 | 9,178.500 | 120.800 | A |
| 8a1ef4583067fff | Stari Grad Sarajevo | Mošćanica | 15 | 1,811.600 | 120.800 | A |
| 8a1ef45945a7fff | Novi Grad Sarajevo | Briješće | 19 | 2,294.700 | 120.800 | A |
| 8a1ef45b0557fff | Vogošća | Vogošća | 77 | 9,300.300 | 120.800 | B |
| 8a1ef459c987fff | Centar Sarajevo | Trg oslobođenja-Centar | 286 | 34,550.600 | 120.800 | B |
| 8a1ef4586c97fff | Vogošća | Hotonj | 35 | 4,228.700 | 120.800 | B |
| 8a1ef4582747fff | Centar Sarajevo | Mejtaš-Bjelave | 136 | 16,432.500 | 120.800 | B |
| 8a1ef45b0a8ffff | Vogošća | Blagovac | 31 | 3,747.000 | 120.900 | B |
| 8a1ef45b1797fff | Vogošća | Hotonj | 42 | 5,076.700 | 120.900 | B |
| 8a1ef45b1477fff | Vogošća | Hotonj | 16 | 1,934.200 | 120.900 | B |
| 8a1ef45b32dffff | Vogošća | Kobilja Glava | 33 | 3,989.300 | 120.900 | B |
| 8a1ef45b0a9ffff | Vogošća | Blagovac | 42 | 5,077.400 | 120.900 | B |
| 8a1ea92c9397fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 61 | 7,374.500 | 120.900 | A |
| 8a1ef45b012ffff | Vogošća | Vogošća | 20 | 2,418.200 | 120.900 | B |
| 8a1ef45b049ffff | Vogošća | Vogošća | 28 | 3,385.800 | 120.900 | B |
| 8a1ea92c88f7fff | Novi Grad Sarajevo | Dobroševići | 18 | 2,177.000 | 120.900 | A |
| 8a1ef45b140ffff | Vogošća | Hotonj | 33 | 3,991.800 | 121.000 | B |
| 8a1ef45b3b67fff | Vogošća | Hotonj | 51 | 6,169.500 | 121.000 | B |
| 8a1ef69649a7fff | Ilidža | Kamenjača | 18 | 2,177.500 | 121.000 | B |
| 8a1ea92e9237fff | Vogošća | Semizovac | 33 | 3,993.000 | 121.000 | B |
| 8a1ef4580417fff | Centar Sarajevo | Pionirska Dolina | 75 | 9,075.400 | 121.000 | B |
| 8a1ef45b6b27fff | Vogošća | Ljubina-Poturovići | 40 | 4,840.800 | 121.000 | B |
| 8a1ef45b3007fff | Vogošća | Ugorsko | 16 | 1,936.400 | 121.000 | B |
| 8a1ea92ca60ffff | Ilidža | Kamenjača | 12 | 1,452.300 | 121.000 | B |
| 8a1ea92c920ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 42 | 5,084.000 | 121.000 | A |
| 8a1ef4582a2ffff | Centar Sarajevo | Hrastovi-Mrkovići | 78 | 9,443.300 | 121.100 | B |
| 8a1ef696106ffff | Ilidža | Donji Kotorac | 19 | 2,300.500 | 121.100 | B |
| 8a1ea92e93affff | Vogošća | Semizovac | 16 | 1,937.400 | 121.100 | B |
| 8a1ef4586527fff | Vogošća | Kobilja Glava | 39 | 4,722.400 | 121.100 | B |
| 8a1ef45b2b07fff | Vogošća | Vogošća | 32 | 3,875.200 | 121.100 | B |
| 8a1ea92cc64ffff | Novi Grad Sarajevo | Dobroševići | 13 | 1,575.000 | 121.200 | A |
| 8a1ef45b144ffff | Vogošća | Hotonj | 35 | 4,241.100 | 121.200 | B |
| 8a1ea92c93affff | Novi Grad Sarajevo | Naselje heroja Sokolje | 57 | 6,907.600 | 121.200 | A |
| 8a1ef45b6287fff | Vogošća | Krivoglavci | 36 | 4,362.700 | 121.200 | B |
| 8a1ea92e926ffff | Vogošća | Semizovac | 38 | 4,605.600 | 121.200 | B |
| 8a1ef45b171ffff | Vogošća | Hotonj | 19 | 2,302.900 | 121.200 | B |
| 8a1ea92e92c7fff | Vogošća | Svrake | 42 | 5,090.800 | 121.200 | B |
| 8a1ef4584c9ffff | Centar Sarajevo | Betanija | 11 | 1,333.400 | 121.200 | B |
| 8a1ef45b1da7fff | Vogošća | Blagovac | 14 | 1,697.400 | 121.200 | B |
| 8a1ef4595907fff | Vogošća | Kobilja Glava | 23 | 2,789.400 | 121.300 | B |
| 8a1ea92e9b17fff | Vogošća | Donja Vogošća | 13 | 1,576.600 | 121.300 | B |
| 8a1ef45b6baffff | Vogošća | Semizovac | 20 | 2,426.400 | 121.300 | B |
| 8a1ef45b046ffff | Vogošća | Vogošća | 96 | 11,647.200 | 121.300 | B |
| 8a1ef4592cc7fff | Novi Grad Sarajevo | Dobrinja A | 119 | 14,438.600 | 121.300 | A |
| 8a1ef45966cffff | Novi Grad Sarajevo | Saraj Polje | 75 | 9,102.000 | 121.400 | A |
| 8a1ea92c931ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 57 | 6,917.600 | 121.400 | A |
| 8a1ef45850dffff | Centar Sarajevo | Betanija | 48 | 5,826.700 | 121.400 | B |
| 8a1ef45b2997fff | Vogošća | Vogošća | 19 | 2,306.700 | 121.400 | B |
| 8a1ea92cd4cffff | Novi Grad Sarajevo | Dobroševići | 11 | 1,335.900 | 121.400 | A |
| 8a1ef45b4c8ffff | Vogošća | Semizovac | 22 | 2,671.900 | 121.400 | B |
| 8a1ef4586acffff | Centar Sarajevo | Betanija | 32 | 3,886.900 | 121.500 | B |
| 8a1ef45b2b17fff | Vogošća | Vogošća | 43 | 5,223.700 | 121.500 | B |
| 8a1ea92c904ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 54 | 6,560.400 | 121.500 | A |
| 8a1ea92c8d4ffff | Novi Grad Sarajevo | Dobroševići | 12 | 1,458.100 | 121.500 | A |
| 8a1ef45b28affff | Vogošća | Vogošća | 21 | 2,551.700 | 121.500 | B |
| 8a1ea92caad7fff | Ilidža | Bjelaće | 10 | 1,215.200 | 121.500 | B |
| 8a1ef458214ffff | Centar Sarajevo | Koševo II | 223 | 27,098.500 | 121.500 | B |
| 8a1ef6965347fff | Ilidža | Stupsko Brdo | 14 | 1,701.700 | 121.500 | B |
| 8a1ea92e928ffff | Vogošća | Svrake | 31 | 3,768.100 | 121.600 | B |
| 8a1ea92cc2effff | Novi Grad Sarajevo | Dobroševići | 15 | 1,823.600 | 121.600 | A |
| 8a1ea92c922ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 36 | 4,376.600 | 121.600 | A |
| 8a1ef45b000ffff | Vogošća | Blagovac | 52 | 6,321.900 | 121.600 | B |
| 8a1ea92cb257fff | Ilidža | Azići | 20 | 2,432.600 | 121.600 | B |
| 8a1ea92cd717fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,216.400 | 121.600 | A |
| 8a1ef45836e7fff | Stari Grad Sarajevo | Babića bašča | 17 | 2,068.400 | 121.700 | A |
| 8a1ef6964b97fff | Ilidža | Vreoca | 12 | 1,460.300 | 121.700 | B |
| 8a1ef45b0c6ffff | Vogošća | Vogošća | 13 | 1,582.200 | 121.700 | B |
| 8a1ef4596977fff | Novi Grad Sarajevo | Briješće | 34 | 4,138.400 | 121.700 | A |
| 8a1ef45b684ffff | Vogošća | Semizovac | 19 | 2,313.300 | 121.800 | B |
| 8a1ea92c9747fff | Novi Grad Sarajevo | Briješće | 38 | 4,626.800 | 121.800 | A |
| 8a1ef458402ffff | Centar Sarajevo | Nahorevo | 25 | 3,044.000 | 121.800 | B |
| 8a1ef6961b8ffff | Ilidža | Donji Kotorac | 20 | 2,435.300 | 121.800 | B |
| 8a1ef696074ffff | Ilidža | Kovači (Ilidža) | 10 | 1,217.700 | 121.800 | B |
| 8a1ef45b1557fff | Vogošća | Hotonj | 20 | 2,435.400 | 121.800 | B |
| 8a1ef45b38b7fff | Vogošća | Ugorsko | 17 | 2,070.200 | 121.800 | B |
| 8a1ef45b3a4ffff | Vogošća | Hotonj | 31 | 3,775.600 | 121.800 | B |
| 8a1ef696552ffff | Ilidža | Ilidža | 18 | 2,192.500 | 121.800 | B |
| 8a1ea92cb307fff | Ilidža | Azići | 11 | 1,340.200 | 121.800 | B |
| 8a1ea92dd32ffff | Ilidža | Lipe | 18 | 2,193.200 | 121.800 | B |
| 8a1ef45b2baffff | Vogošća | Vogošća | 30 | 3,655.400 | 121.800 | B |
| 8a1ef45b0097fff | Vogošća | Vogošća | 96 | 11,699.000 | 121.900 | B |
| 8a1ef4580d2ffff | Centar Sarajevo | Pionirska Dolina | 39 | 4,754.100 | 121.900 | B |
| 8a1ea92e9a2ffff | Vogošća | Nebočaj | 10 | 1,219.300 | 121.900 | B |
| 8a1ef4586d77fff | Vogošća | Hotonj | 48 | 5,854.600 | 122.000 | B |
| 8a1ef45b14cffff | Vogošća | Hotonj | 53 | 6,465.800 | 122.000 | B |
| 8a1ef45b692ffff | Vogošća | Svrake | 34 | 4,147.900 | 122.000 | B |
| 8a1ea92c921ffff | Novi Grad Sarajevo | Briješće | 27 | 3,294.500 | 122.000 | A |
| 8a1ef45b1447fff | Vogošća | Hotonj | 43 | 5,246.700 | 122.000 | B |
| 8a1ef45b169ffff | Vogošća | Hotonj | 51 | 6,224.900 | 122.100 | B |
| 8a1ea92c9097fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 43 | 5,249.200 | 122.100 | A |
| 8a1ef69652dffff | Ilidža | Butmir | 59 | 7,203.600 | 122.100 | B |
| 8a1ef45b06c7fff | Vogošća | Uglješići | 31 | 3,785.400 | 122.100 | B |
| 8a1ef6965d67fff | Ilidža | Pejton | 25 | 3,053.000 | 122.100 | B |
| 8a1ea92e974ffff | Vogošća | Svrake | 26 | 3,176.000 | 122.200 | B |
| 8a1ef459592ffff | Vogošća | Kobilja Glava | 44 | 5,375.600 | 122.200 | B |
| 8a1ef45b2b57fff | Vogošća | Vogošća | 16 | 1,955.200 | 122.200 | B |
| 8a1ef45b0027fff | Vogošća | Vogošća | 41 | 5,014.100 | 122.300 | B |
| 8a1ea92c962ffff | Novi Grad Sarajevo | Briješće | 31 | 3,791.400 | 122.300 | A |
| 8a1ef45b284ffff | Vogošća | Vogošća | 39 | 4,769.900 | 122.300 | B |
| 8a1ef45b28a7fff | Vogošća | Vogošća | 34 | 4,158.700 | 122.300 | B |
| 8a1ef45b3367fff | Vogošća | Hotonj | 26 | 3,180.300 | 122.300 | B |
| 8a1ef6961187fff | Ilidža | Butmir | 16 | 1,957.500 | 122.300 | B |
| 8a1ea92cc287fff | Novi Grad Sarajevo | Dobroševići | 11 | 1,345.800 | 122.300 | A |
| 8a1ef458216ffff | Centar Sarajevo | Breka | 117 | 14,314.400 | 122.300 | B |
| 8a1ef4582317fff | Centar Sarajevo | Park-Višnjik | 152 | 18,597.100 | 122.300 | B |
| 8a1ea92cad8ffff | Ilidža | Lipe | 16 | 1,957.600 | 122.400 | B |
| 8a1ef4586c0ffff | Vogošća | Kobilja Glava | 20 | 2,447.400 | 122.400 | B |
| 8a1ef45b141ffff | Vogošća | Hotonj | 52 | 6,363.400 | 122.400 | B |
| 8a1ef4582b37fff | Centar Sarajevo | Hrastovi-Mrkovići | 77 | 9,423.200 | 122.400 | B |
| 8a1ef6964257fff | Ilidža | Lužani | 12 | 1,468.600 | 122.400 | B |
| 8a1ea92c9677fff | Novi Grad Sarajevo | Briješće | 36 | 4,405.800 | 122.400 | A |
| 8a1ea92e9ad7fff | Vogošća | Nebočaj | 12 | 1,468.700 | 122.400 | B |
| 8a1ea92d9a27fff | Ilidža | Blažuj | 10 | 1,224.000 | 122.400 | B |
| 8a1ef45b0a97fff | Vogošća | Blagovac | 44 | 5,386.500 | 122.400 | B |
| 8a1ef45b14c7fff | Vogošća | Hotonj | 55 | 6,733.600 | 122.400 | B |
| 8a1ea92c930ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 56 | 6,856.100 | 122.400 | A |
| 8a1ef45b322ffff | Vogošća | Grahovište | 14 | 1,714.300 | 122.500 | B |
| 8a1ef459c837fff | Stari Grad Sarajevo | Ferhadija | 161 | 19,716.900 | 122.500 | A |
| 8a1ef45b0ab7fff | Vogošća | Blagovac | 40 | 4,898.700 | 122.500 | B |
| 8a1ef45b45affff | Vogošća | Semizovac | 16 | 1,960.300 | 122.500 | B |
| 8a1ef45b45b7fff | Vogošća | Semizovac | 45 | 5,514.100 | 122.500 | B |
| 8a1ef458694ffff | Centar Sarajevo | Betanija | 57 | 6,988.600 | 122.600 | B |
| 8a1ef4596d57fff | Novi Grad Sarajevo | Briješće | 33 | 4,046.800 | 122.600 | A |
| 8a1ea92cba9ffff | Ilidža | Azići | 69 | 8,464.400 | 122.700 | B |
| 8a1ef45b1687fff | Vogošća | Hotonj | 55 | 6,748.000 | 122.700 | B |
| 8a1ef4586997fff | Vogošća | Hotonj | 37 | 4,540.100 | 122.700 | B |
| 8a1ef4586d0ffff | Vogošća | Hotonj | 51 | 6,258.100 | 122.700 | B |
| 8a1ef696528ffff | Ilidža | Butmir | 13 | 1,595.300 | 122.700 | B |
| 8a1ef4596ba7fff | Novi Grad Sarajevo | Briješće | 47 | 5,768.100 | 122.700 | A |
| 8a1ea92e9877fff | Vogošća | Donja Vogošća | 24 | 2,945.500 | 122.700 | B |
| 8a1ea92c044ffff | Ilidža | Rakovica | 12 | 1,472.900 | 122.700 | B |
| 8a1ea92e9287fff | Vogošća | Svrake | 30 | 3,682.900 | 122.800 | B |
| 8a1ef45b3b0ffff | Vogošća | Hotonj | 68 | 8,351.200 | 122.800 | B |
| 8a1ef45b010ffff | Vogošća | Vogošća | 34 | 4,175.800 | 122.800 | B |
| 8a1ef45b3a67fff | Vogošća | Hotonj | 58 | 7,124.800 | 122.800 | B |
| 8a1ef45b2937fff | Vogošća | Vogošća | 31 | 3,808.400 | 122.900 | B |
| 8a1ea92cc30ffff | Novi Grad Sarajevo | Dobroševići | 13 | 1,597.300 | 122.900 | A |
| 8a1ef4586757fff | Centar Sarajevo | Šip | 84 | 10,323.800 | 122.900 | B |
| 8a1ef45b0adffff | Vogošća | Blagovac | 42 | 5,162.900 | 122.900 | B |
| 8a1ef45b16effff | Vogošća | Hotonj | 22 | 2,704.500 | 122.900 | B |
| 8a1ef6961947fff | Ilidža | Donji Kotorac | 19 | 2,335.800 | 122.900 | B |
| 8a1ef6961d27fff | Ilidža | Sokolović-kolonija | 14 | 1,721.500 | 123.000 | B |
| 8a1ef4580c17fff | Centar Sarajevo | Pionirska Dolina | 40 | 4,918.800 | 123.000 | B |
| 8a1ef45b0ae7fff | Vogošća | Blagovac | 35 | 4,304.200 | 123.000 | B |
| 8a1ef6965cb7fff | Ilidža | Lužani | 88 | 10,823.100 | 123.000 | B |
| 8a1ef4582b17fff | Centar Sarajevo | Hrastovi-Mrkovići | 83 | 10,209.100 | 123.000 | B |
| 8a1ea925b9affff | Vogošća | Gora | 12 | 1,476.100 | 123.000 | B |
| 8a1ef45b0407fff | Vogošća | Vogošća | 102 | 12,548.000 | 123.000 | B |
| 8a1ea92c9067fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 71 | 8,734.400 | 123.000 | A |
| 8a1ea92cd4effff | Novi Grad Sarajevo | Dobroševići | 15 | 1,846.600 | 123.100 | A |
| 8a1ea92c964ffff | Novi Grad Sarajevo | Briješće | 43 | 5,293.700 | 123.100 | A |
| 8a1ef4596927fff | Novi Grad Sarajevo | Briješće | 34 | 4,186.400 | 123.100 | A |
| 8a1ea92ddb47fff | Ilidža | Lipe | 11 | 1,354.400 | 123.100 | B |
| 8a1ef45b044ffff | Vogošća | Vogošća | 104 | 12,805.400 | 123.100 | B |
| 8a1ef45958affff | Vogošća | Kobilja Glava | 28 | 3,450.400 | 123.200 | B |
| 8a1ef458286ffff | Centar Sarajevo | Koševo II | 165 | 20,343.200 | 123.300 | B |
| 8a1ea92cc6d7fff | Novi Grad Sarajevo | Dobroševići | 11 | 1,356.200 | 123.300 | A |
| 8a1ea92c9c6ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 43 | 5,302.300 | 123.300 | A |
| 8a1ef6961b17fff | Ilidža | Donji Kotorac | 15 | 1,849.700 | 123.300 | B |
| 8a1ea92e9247fff | Vogošća | Semizovac | 35 | 4,316.800 | 123.300 | B |
| 8a1ef45b1757fff | Vogošća | Hotonj | 14 | 1,727.300 | 123.400 | B |
| 8a1ef69618e7fff | Ilidža | Donji Kotorac | 15 | 1,850.700 | 123.400 | B |
| 8a1ef45b0a87fff | Vogošća | Blagovac | 40 | 4,935.100 | 123.400 | B |
| 8a1ef4582a5ffff | Centar Sarajevo | Hrastovi-Mrkovići | 92 | 11,351.300 | 123.400 | B |
| 8a1ef45b0af7fff | Vogošća | Blagovac | 36 | 4,444.400 | 123.500 | B |
| 8a1ef45b10f7fff | Vogošća | Hotonj | 11 | 1,358.100 | 123.500 | B |
| 8a1ea92e9b8ffff | Vogošća | Nebočaj | 14 | 1,728.500 | 123.500 | B |
| 8a1ef4591b5ffff | Centar Sarajevo | Marijin Dvor | 159 | 19,630.900 | 123.500 | B |
| 8a1ea92cb4effff | Ilidža | Otes | 56 | 6,914.500 | 123.500 | B |
| 8a1ea92e9a17fff | Vogošća | Nebočaj | 15 | 1,852.100 | 123.500 | B |
| 8a1ef45b0a5ffff | Vogošća | Blagovac | 28 | 3,458.200 | 123.500 | B |
| 8a1ea92ddac7fff | Ilidža | Lipe | 22 | 2,717.100 | 123.500 | B |
| 8a1ef45b0a17fff | Vogošća | Blagovac | 34 | 4,199.300 | 123.500 | B |
| 8a1ef45b0a1ffff | Vogošća | Blagovac | 36 | 4,447.100 | 123.500 | B |
| 8a1ea92ce4f7fff | Ilidža | Lipe | 10 | 1,235.700 | 123.600 | B |
| 8a1ef459590ffff | Vogošća | Kobilja Glava | 44 | 5,438.200 | 123.600 | B |
| 8a1ef6961d0ffff | Ilidža | Sokolović-kolonija | 73 | 9,022.700 | 123.600 | B |
| 8a1ef6964a2ffff | Ilidža | Vreoca | 36 | 4,449.700 | 123.600 | B |
| 8a1ea92cc6effff | Novi Grad Sarajevo | Dobroševići | 11 | 1,359.800 | 123.600 | A |
| 8a1ef4582667fff | Centar Sarajevo | Mejtaš-Bjelave | 199 | 24,601.900 | 123.600 | B |
| 8a1ea92cd58ffff | Novi Grad Sarajevo | Dobroševići | 16 | 1,978.100 | 123.600 | A |
| 8a1ef459449ffff | Novi Grad Sarajevo | Briješće | 26 | 3,214.800 | 123.600 | A |
| 8a1ea92c88c7fff | Novi Grad Sarajevo | Dobroševići | 17 | 2,102.200 | 123.700 | A |
| 8a1ea92ca6cffff | Ilidža | Plandište | 13 | 1,607.800 | 123.700 | B |
| 8a1ea92c954ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 39 | 4,824.100 | 123.700 | A |
| 8a1ef45b00a7fff | Vogošća | Vogošća | 87 | 10,762.300 | 123.700 | B |
| 8a1ef45b1cb7fff | Vogošća | Blagovac | 30 | 3,712.200 | 123.700 | B |
| 8a1ef45b16cffff | Vogošća | Hotonj | 52 | 6,434.900 | 123.700 | B |
| 8a1ef45b08dffff | Vogošća | Vogošća | 13 | 1,608.800 | 123.800 | B |
| 8a1ef459692ffff | Novi Grad Sarajevo | Briješće | 34 | 4,208.200 | 123.800 | A |
| 8a1ef45b335ffff | Vogošća | Grahovište | 24 | 2,970.600 | 123.800 | B |
| 8a1ef4596677fff | Novi Grad Sarajevo | Saraj Polje | 88 | 10,893.900 | 123.800 | A |
| 8a1ef4580b07fff | Centar Sarajevo | Betanija | 15 | 1,857.000 | 123.800 | B |
| 8a1ef4586d6ffff | Vogošća | Hotonj | 35 | 4,333.800 | 123.800 | B |
| 8a1ea925b89ffff | Vogošća | Gora | 20 | 2,477.000 | 123.800 | B |
| 8a1ea92c9247fff | Novi Grad Sarajevo | Briješće | 21 | 2,600.800 | 123.800 | A |
| 8a1ef6965a47fff | Novi Grad Sarajevo | Saraj Polje | 71 | 8,793.400 | 123.900 | A |
| 8a1ef4582b0ffff | Centar Sarajevo | Hrastovi-Mrkovići | 77 | 9,538.000 | 123.900 | B |
| 8a1ef45b458ffff | Vogošća | Semizovac | 25 | 3,097.600 | 123.900 | B |
| 8a1ef4586d67fff | Vogošća | Hotonj | 50 | 6,195.700 | 123.900 | B |
| 8a1ea92c9297fff | Novi Grad Sarajevo | Briješće | 33 | 4,089.300 | 123.900 | A |
| 8a1ef6964a07fff | Ilidža | Vreoca | 13 | 1,611.000 | 123.900 | B |
| 8a1ef4595927fff | Vogošća | Kobilja Glava | 46 | 5,704.300 | 124.000 | B |
| 8a1ef459696ffff | Novi Grad Sarajevo | Briješće | 34 | 4,216.300 | 124.000 | A |
| 8a1ef45b450ffff | Vogošća | Ljubina-Poturovići | 22 | 2,728.200 | 124.000 | B |
| 8a1ef45b44b7fff | Vogošća | Semizovac | 60 | 7,441.500 | 124.000 | B |
| 8a1ef459588ffff | Vogošća | Kobilja Glava | 16 | 1,985.000 | 124.100 | B |
| 8a1ef45b4c9ffff | Vogošća | Semizovac | 43 | 5,334.800 | 124.100 | B |
| 8a1ef458348ffff | Stari Grad Sarajevo | Kovači | 106 | 13,153.000 | 124.100 | A |
| 8a1ef45b3acffff | Vogošća | Hotonj | 20 | 2,482.600 | 124.100 | B |
| 8a1ea92c065ffff | Ilidža | Rakovica | 13 | 1,613.800 | 124.100 | B |
| 8a1ef6965d07fff | Ilidža | Pejton | 32 | 3,973.600 | 124.200 | B |
| 8a1ef4594597fff | Novi Grad Sarajevo | Briješće | 32 | 3,974.600 | 124.200 | A |
| 8a1ef4596b37fff | Novi Grad Sarajevo | Briješće | 34 | 4,223.100 | 124.200 | A |
| 8a1ef4582ae7fff | Centar Sarajevo | Hrastovi-Mrkovići | 97 | 12,048.600 | 124.200 | B |
| 8a1ef4598177fff | Stari Grad Sarajevo | Širokača | 17 | 2,112.000 | 124.200 | A |
| 8a1ea92cb21ffff | Ilidža | Azići | 55 | 6,833.400 | 124.200 | B |
| 8a1ef4592ce7fff | Novi Grad Sarajevo | Dobrinja A | 135 | 16,774.500 | 124.300 | A |
| 8a1ef6964adffff | Ilidža | Lužani | 14 | 1,739.600 | 124.300 | B |
| 8a1ef45b0b9ffff | Vogošća | Blagovac | 24 | 2,983.200 | 124.300 | B |
| 8a1ef4582b47fff | Centar Sarajevo | Hrastovi-Mrkovići | 73 | 9,078.500 | 124.400 | B |
| 8a1ea92c31a7fff | Ilidža | Gladno polje | 10 | 1,244.100 | 124.400 | B |
| 8a1ef4586a07fff | Centar Sarajevo | Betanija | 29 | 3,608.100 | 124.400 | B |
| 8a1ef45b691ffff | Vogošća | Svrake | 30 | 3,732.800 | 124.400 | B |
| 8a1ef4592cdffff | Novi Grad Sarajevo | Dobrinja A | 136 | 16,922.300 | 124.400 | A |
| 8a1ef45848affff | Centar Sarajevo | Nahorevo | 20 | 2,489.200 | 124.500 | B |
| 8a1ef458051ffff | Centar Sarajevo | Pionirska Dolina | 74 | 9,210.000 | 124.500 | B |
| 8a1ef6965b0ffff | Ilidža | Naselje Bulevar | 32 | 3,982.900 | 124.500 | B |
| 8a1ef4596b07fff | Novi Grad Sarajevo | Briješće | 30 | 3,734.400 | 124.500 | A |
| 8a1ea92cb6e7fff | Ilidža | Pejton | 21 | 2,614.700 | 124.500 | B |
| 8a1ef45b604ffff | Vogošća | Krivoglavci | 63 | 7,845.100 | 124.500 | B |
| 8a1ea92cc207fff | Novi Grad Sarajevo | Dobroševići | 13 | 1,618.900 | 124.500 | A |
| 8a1ef4582b57fff | Centar Sarajevo | Hrastovi-Mrkovići | 81 | 10,089.900 | 124.600 | B |
| 8a1ea92cd40ffff | Novi Grad Sarajevo | Dobroševići | 14 | 1,744.700 | 124.600 | A |
| 8a1ea92cc277fff | Novi Grad Sarajevo | Dobroševići | 13 | 1,620.400 | 124.600 | A |
| 8a1ef45b2a37fff | Vogošća | Vogošća | 28 | 3,490.200 | 124.700 | B |
| 8a1ef696540ffff | Ilidža | Ilidža | 16 | 1,994.400 | 124.700 | B |
| 8a1ea92cc0d7fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,246.500 | 124.700 | A |
| 8a1ef6965117fff | Ilidža | Ilidža | 18 | 2,243.900 | 124.700 | B |
| 8a1ea92ddb27fff | Ilidža | Lipe | 10 | 1,246.700 | 124.700 | B |
| 8a1ea92c9227fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 61 | 7,607.800 | 124.700 | A |
| 8a1ef45b391ffff | Vogošća | Hotonj | 62 | 7,733.800 | 124.700 | B |
| 8a1ea92c8d67fff | Novi Grad Sarajevo | Dobroševići | 12 | 1,497.000 | 124.800 | A |
| 8a1ef45b0b8ffff | Vogošća | Blagovac | 19 | 2,370.700 | 124.800 | B |
| 8a1ea92cb387fff | Ilidža | Azići | 11 | 1,372.500 | 124.800 | B |
| 8a1ea92ddb8ffff | Ilidža | Lipe | 20 | 2,495.500 | 124.800 | B |
| 8a1ea92c8b37fff | Novi Grad Sarajevo | Dobroševići | 15 | 1,872.200 | 124.800 | A |
| 8a1ef45b12d7fff | Centar Sarajevo | Betanija | 23 | 2,870.800 | 124.800 | B |
| 8a1ef6965b07fff | Ilidža | Naselje Bulevar | 30 | 3,744.600 | 124.800 | B |
| 8a1ea92c956ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 59 | 7,364.400 | 124.800 | A |
| 8a1ef45b52d7fff | Vogošća | Tihovići | 29 | 3,620.300 | 124.800 | B |
| 8a1ef459c927fff | Centar Sarajevo | Mejtaš-Bjelave | 217 | 27,094.400 | 124.900 | B |
| 8a1ea92c072ffff | Ilidža | Rakovica | 11 | 1,373.500 | 124.900 | B |
| 8a1ef45b31b7fff | Vogošća | Ugorsko | 12 | 1,498.500 | 124.900 | B |
| 8a1ef45b051ffff | Vogošća | Vogošća | 78 | 9,742.800 | 124.900 | B |
| 8a1ef6965a67fff | Novi Grad Sarajevo | Saraj Polje | 45 | 5,621.900 | 124.900 | A |
| 8a1ea92e9217fff | Vogošća | Semizovac | 39 | 4,873.800 | 125.000 | B |
| 8a1ea92c9077fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 82 | 10,248.600 | 125.000 | A |
| 8a1ef45969b7fff | Novi Grad Sarajevo | Briješće | 55 | 6,874.100 | 125.000 | A |
| 8a1ea92e92cffff | Vogošća | Svrake | 31 | 3,874.700 | 125.000 | B |
| 8a1ef45b3cdffff | Vogošća | Ugorsko | 12 | 1,500.200 | 125.000 | B |
| 8a1ef4594497fff | Novi Grad Sarajevo | Briješće | 41 | 5,126.400 | 125.000 | A |
| 8a1ea92cb20ffff | Ilidža | Azići | 19 | 2,375.700 | 125.000 | B |
| 8a1ef6965aa7fff | Ilidža | Naselje Bulevar | 28 | 3,501.400 | 125.000 | B |
| 8a1ef6965b27fff | Ilidža | Naselje Bulevar | 33 | 4,127.100 | 125.100 | B |
| 8a1ea92c0727fff | Ilidža | Rakovica | 13 | 1,626.000 | 125.100 | B |
| 8a1ef45968affff | Novi Grad Sarajevo | Briješće | 36 | 4,502.700 | 125.100 | A |
| 8a1ea92e92f7fff | Vogošća | Svrake | 49 | 6,129.000 | 125.100 | B |
| 8a1ea92e916ffff | Vogošća | Donja Vogošća | 13 | 1,626.300 | 125.100 | B |
| 8a1ef45b459ffff | Vogošća | Semizovac | 51 | 6,380.300 | 125.100 | B |
| 8a1ef4596697fff | Ilidža | Stupsko Brdo | 27 | 3,378.000 | 125.100 | B |
| 8a1ea92e984ffff | Vogošća | Donja Vogošća | 31 | 3,878.900 | 125.100 | B |
| 8a1ea92cb8a7fff | Ilidža | Doglodi | 17 | 2,128.000 | 125.200 | B |
| 8a1ef45b014ffff | Vogošća | Blagovac | 37 | 4,631.700 | 125.200 | B |
| 8a1ef4594587fff | Novi Grad Sarajevo | Briješće | 33 | 4,131.900 | 125.200 | A |
| 8a1ea92cdd97fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,252.100 | 125.200 | A |
| 8a1ea92cb69ffff | Ilidža | Pejton | 94 | 11,772.300 | 125.200 | B |
| 8a1ef6961a27fff | Ilidža | Donji Kotorac | 18 | 2,254.600 | 125.300 | B |
| 8a1ef45b2967fff | Vogošća | Vogošća | 50 | 6,263.500 | 125.300 | B |
| 8a1ef45b288ffff | Vogošća | Vogošća | 29 | 3,633.400 | 125.300 | B |
| 8a1ef6964b8ffff | Ilidža | Vreoca | 23 | 2,882.000 | 125.300 | B |
| 8a1ef6960a2ffff | Ilidža | Sokolović-kolonija | 74 | 9,273.200 | 125.300 | B |
| 8a1ef69658dffff | Ilidža | Ilidža | 25 | 3,135.700 | 125.400 | B |
| 8a1ea92c2377fff | Ilidža | Rakovica | 11 | 1,379.700 | 125.400 | B |
| 8a1ef45967a7fff | Ilidža | Stupsko Brdo | 31 | 3,889.100 | 125.500 | B |
| 8a1ef4592cf7fff | Novi Grad Sarajevo | Dobrinja A | 151 | 18,944.800 | 125.500 | A |
| 8a1ef4583ac7fff | Stari Grad Sarajevo | Mošćanica | 15 | 1,882.500 | 125.500 | A |
| 8a1ea92e9667fff | Vogošća | Svrake | 20 | 2,510.500 | 125.500 | B |
| 8a1ef4595937fff | Vogošća | Grahovište | 14 | 1,757.400 | 125.500 | B |
| 8a1ef45b1547fff | Vogošća | Hotonj | 17 | 2,134.000 | 125.500 | B |
| 8a1ea92c92cffff | Novi Grad Sarajevo | Briješće | 38 | 4,770.400 | 125.500 | A |
| 8a1ea92c8b27fff | Novi Grad Sarajevo | Dobroševići | 20 | 2,511.300 | 125.600 | A |
| 8a1ef6964277fff | Ilidža | Lužani | 18 | 2,260.300 | 125.600 | B |
| 8a1ef6960ab7fff | Ilidža | Sokolović-kolonija | 67 | 8,418.600 | 125.700 | B |
| 8a1ea92cb047fff | Ilidža | Doglodi | 11 | 1,382.200 | 125.700 | B |
| 8a1ef6964d6ffff | Ilidža | Plandište | 12 | 1,509.400 | 125.800 | B |
| 8a1ef4596857fff | Novi Grad Sarajevo | Briješće | 44 | 5,534.400 | 125.800 | A |
| 8a1ea92cc2cffff | Novi Grad Sarajevo | Dobroševići | 15 | 1,886.800 | 125.800 | A |
| 8a1ef45b0a07fff | Vogošća | Blagovac | 41 | 5,158.500 | 125.800 | B |
| 8a1ef459cd07fff | Centar Sarajevo | Skenderija-Podtekija | 81 | 10,192.600 | 125.800 | B |
| 8a1ef696560ffff | Ilidža | Butmir | 20 | 2,516.800 | 125.800 | B |
| 8a1ef459645ffff | Ilidža | Stup | 35 | 4,405.200 | 125.900 | B |
| 8a1ef4596837fff | Novi Grad Sarajevo | Briješće | 56 | 7,049.700 | 125.900 | A |
| 8a1ef6960ad7fff | Ilidža | Sokolović-kolonija | 12 | 1,511.000 | 125.900 | B |
| 8a1ea92cb10ffff | Ilidža | Doglodi | 10 | 1,259.300 | 125.900 | B |
| 8a1ef45b1627fff | Vogošća | Hotonj | 32 | 4,030.200 | 125.900 | B |
| 8a1ef45b034ffff | Vogošća | Blagovac | 41 | 5,163.800 | 125.900 | B |
| 8a1ea92cb0e7fff | Ilidža | Doglodi | 12 | 1,511.400 | 125.900 | B |
| 8a1ef4584c8ffff | Centar Sarajevo | Betanija | 14 | 1,763.500 | 126.000 | B |
| 8a1ea92e9747fff | Vogošća | Svrake | 10 | 1,260.600 | 126.100 | B |
| 8a1ef4596bb7fff | Novi Grad Sarajevo | Briješće | 57 | 7,185.300 | 126.100 | A |
| 8a1ef4592cb7fff | Ilidža | Stupsko Brdo | 26 | 3,278.400 | 126.100 | B |
| 8a1ef45944b7fff | Novi Grad Sarajevo | Briješće | 35 | 4,414.200 | 126.100 | A |
| 8a1ef4584617fff | Centar Sarajevo | Betanija | 27 | 3,405.800 | 126.100 | B |
| 8a1ea92c0677fff | Ilidža | Rakovica | 11 | 1,388.000 | 126.200 | B |
| 8a1ef69619a7fff | Ilidža | Butmir | 24 | 3,028.600 | 126.200 | B |
| 8a1ea92c338ffff | Ilidža | Gladno polje | 16 | 2,019.900 | 126.200 | B |
| 8a1ef4596507fff | Ilidža | Stup | 28 | 3,535.000 | 126.300 | B |
| 8a1ef6961a77fff | Ilidža | Donji Kotorac | 12 | 1,515.400 | 126.300 | B |
| 8a1ef4584897fff | Centar Sarajevo | Nahorevo | 15 | 1,894.800 | 126.300 | B |
| 8a1ea92c822ffff | Novi Grad Sarajevo | Briješće | 15 | 1,895.000 | 126.300 | A |
| 8a1ef6964a77fff | Ilidža | Pejton | 12 | 1,516.200 | 126.300 | B |
| 8a1ef4584c4ffff | Centar Sarajevo | Nahorevo | 20 | 2,527.400 | 126.400 | B |
| 8a1ea92cd44ffff | Novi Grad Sarajevo | Dobroševići | 18 | 2,274.900 | 126.400 | A |
| 8a1ea92ddb2ffff | Ilidža | Lipe | 15 | 1,895.800 | 126.400 | B |
| 8a1ef45b3ccffff | Vogošća | Ugorsko | 10 | 1,264.600 | 126.500 | B |
| 8a1ea92cc6c7fff | Novi Grad Sarajevo | Dobroševići | 11 | 1,391.500 | 126.500 | A |
| 8a1ef6965b5ffff | Novi Grad Sarajevo | Saraj Polje | 40 | 5,060.400 | 126.500 | A |
| 8a1ea925b98ffff | Vogošća | Gora | 25 | 3,165.700 | 126.600 | B |
| 8a1ea92ca877fff | Ilidža | Dolovi | 12 | 1,519.800 | 126.700 | B |
| 8a1ea92e9307fff | Vogošća | Semizovac | 14 | 1,773.500 | 126.700 | B |
| 8a1ea92c30d7fff | Ilidža | Gladno polje | 11 | 1,393.700 | 126.700 | B |
| 8a1ef6965d4ffff | Ilidža | Ilidža | 30 | 3,801.000 | 126.700 | B |
| 8a1ef45833a7fff | Stari Grad Sarajevo | Mošćanica | 20 | 2,534.600 | 126.700 | A |
| 8a1ef6965367fff | Ilidža | Stupsko Brdo | 30 | 3,804.100 | 126.800 | B |
| 8a1ef6965b67fff | Ilidža | Naselje Bulevar | 32 | 4,058.000 | 126.800 | B |
| 8a1ef45b32c7fff | Vogošća | Kobilja Glava | 36 | 4,566.400 | 126.800 | B |
| 8a1ef4596937fff | Novi Grad Sarajevo | Briješće | 50 | 6,342.900 | 126.900 | A |
| 8a1ef45830cffff | Stari Grad Sarajevo | Mošćanica | 22 | 2,791.100 | 126.900 | A |
| 8a1ea92cb99ffff | Ilidža | Doglodi | 17 | 2,157.400 | 126.900 | B |
| 8a1ef4583a17fff | Stari Grad Sarajevo | Mošćanica | 20 | 2,538.300 | 126.900 | A |
| 8a1ea92c9547fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 53 | 6,726.900 | 126.900 | A |
| 8a1ef4596827fff | Novi Grad Sarajevo | Briješće | 53 | 6,727.600 | 126.900 | A |
| 8a1ef45968effff | Novi Grad Sarajevo | Briješće | 67 | 8,505.500 | 126.900 | A |
| 8a1ea92ca46ffff | Ilidža | Blažuj | 13 | 1,650.400 | 127.000 | B |
| 8a1ef6964267fff | Ilidža | Lužani | 126 | 15,999.100 | 127.000 | B |
| 8a1ea92c9277fff | Novi Grad Sarajevo | Briješće | 38 | 4,825.700 | 127.000 | A |
| 8a1ea92cb34ffff | Ilidža | Azići | 16 | 2,031.900 | 127.000 | B |
| 8a1ea92cc327fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,270.200 | 127.000 | A |
| 8a1ea92cc36ffff | Novi Grad Sarajevo | Dobroševići | 19 | 2,413.800 | 127.000 | A |
| 8a1ea92c884ffff | Novi Grad Sarajevo | Dobroševići | 15 | 1,906.200 | 127.100 | A |
| 8a1ea92c96affff | Novi Grad Sarajevo | Briješće | 16 | 2,033.300 | 127.100 | A |
| 8a1ef458481ffff | Centar Sarajevo | Nahorevo | 11 | 1,398.400 | 127.100 | B |
| 8a1ea92ce017fff | Ilidža | Lipe | 12 | 1,525.600 | 127.100 | B |
| 8a1ef459680ffff | Novi Grad Sarajevo | Briješće | 62 | 7,882.700 | 127.100 | A |
| 8a1ef45b4ad7fff | Vogošća | Kremeš | 10 | 1,271.800 | 127.200 | B |
| 8a1ea92cc2b7fff | Novi Grad Sarajevo | Dobroševići | 15 | 1,907.800 | 127.200 | A |
| 8a1ea925a4d7fff | Vogošća | Nebočaj | 12 | 1,526.500 | 127.200 | B |
| 8a1ef45b4587fff | Vogošća | Semizovac | 65 | 8,268.700 | 127.200 | B |
| 8a1ef45b431ffff | Vogošća | Kremeš | 12 | 1,526.600 | 127.200 | B |
| 8a1ef6965af7fff | Ilidža | Naselje Bulevar | 34 | 4,328.800 | 127.300 | B |
| 8a1ea92c0747fff | Ilidža | Rakovica | 10 | 1,273.400 | 127.300 | B |
| 8a1ea92c008ffff | Ilidža | Rakovica | 11 | 1,401.100 | 127.400 | B |
| 8a1ea92c8d5ffff | Novi Grad Sarajevo | Dobroševići | 11 | 1,401.300 | 127.400 | A |
| 8a1ef459684ffff | Novi Grad Sarajevo | Briješće | 57 | 7,263.900 | 127.400 | A |
| 8a1ef4586b0ffff | Centar Sarajevo | Betanija | 26 | 3,314.000 | 127.500 | B |
| 8a1ea92caceffff | Ilidža | Blažuj | 11 | 1,403.200 | 127.600 | B |
| 8a1ea92ca277fff | Ilidža | Osjek | 10 | 1,276.700 | 127.700 | B |
| 8a1ea92c30cffff | Ilidža | Gladno polje | 14 | 1,787.600 | 127.700 | B |
| 8a1ea92c9757fff | Novi Grad Sarajevo | Briješće | 62 | 7,917.400 | 127.700 | A |
| 8a1ea92cd497fff | Novi Grad Sarajevo | Dobroševići | 13 | 1,660.100 | 127.700 | A |
| 8a1ea92dda27fff | Ilidža | Lipe | 20 | 2,554.100 | 127.700 | B |
| 8a1ea92c32affff | Ilidža | Gladno polje | 16 | 2,043.300 | 127.700 | B |
| 8a1ef4586947fff | Centar Sarajevo | Betanija | 42 | 5,365.000 | 127.700 | B |
| 8a1ea92c06effff | Ilidža | Rakovica | 12 | 1,532.900 | 127.700 | B |
| 8a1ef4596877fff | Novi Grad Sarajevo | Briješće | 55 | 7,026.400 | 127.800 | A |
| 8a1ea92c9657fff | Novi Grad Sarajevo | Briješće | 68 | 8,688.200 | 127.800 | A |
| 8a1ea92cd447fff | Novi Grad Sarajevo | Dobroševići | 20 | 2,555.600 | 127.800 | A |
| 8a1ea92ddbaffff | Ilidža | Lipe | 13 | 1,661.200 | 127.800 | B |
| 8a1ea92c8107fff | Novi Grad Sarajevo | Dobroševići | 15 | 1,917.300 | 127.800 | A |
| 8a1ef4583b97fff | Stari Grad Sarajevo | Mošćanica | 10 | 1,278.300 | 127.800 | A |
| 8a1ea92ce7b7fff | Ilidža | Lipe | 16 | 2,045.900 | 127.900 | B |
| 8a1ef4596b17fff | Novi Grad Sarajevo | Briješće | 52 | 6,650.300 | 127.900 | A |
| 8a1ea92cc347fff | Novi Grad Sarajevo | Dobroševići | 19 | 2,429.900 | 127.900 | A |
| 8a1ef459c937fff | Centar Sarajevo | Mejtaš-Bjelave | 161 | 20,592.400 | 127.900 | B |
| 8a1ef4580b17fff | Centar Sarajevo | Betanija | 25 | 3,197.900 | 127.900 | B |
| 8a1ef6960a0ffff | Ilidža | Sokolović-kolonija | 23 | 2,942.700 | 127.900 | B |
| 8a1ef45b3187fff | Vogošća | Ugorsko | 17 | 2,175.300 | 128.000 | B |
| 8a1ea92c00d7fff | Ilidža | Rakovica | 12 | 1,535.800 | 128.000 | B |
| 8a1ef6960657fff | Ilidža | Kovači (Ilidža) | 19 | 2,431.800 | 128.000 | B |
| 8a1ea92c888ffff | Novi Grad Sarajevo | Dobroševići | 25 | 3,200.800 | 128.000 | A |
| 8a1ea92cc39ffff | Novi Grad Sarajevo | Dobroševići | 15 | 1,920.700 | 128.000 | A |
| 8a1ea92c328ffff | Ilidža | Gladno polje | 15 | 1,921.800 | 128.100 | B |
| 8a1ef6961a47fff | Ilidža | Donji Kotorac | 11 | 1,409.400 | 128.100 | B |
| 8a1ef4594437fff | Novi Grad Sarajevo | Briješće | 22 | 2,819.100 | 128.100 | A |
| 8a1ea92c8ba7fff | Novi Grad Sarajevo | Dobroševići | 12 | 1,538.500 | 128.200 | A |
| 8a1ea92c9ceffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 78 | 10,000.500 | 128.200 | A |
| 8a1ef458461ffff | Centar Sarajevo | Betanija | 17 | 2,180.400 | 128.300 | B |
| 8a1ef69658f7fff | Ilidža | Ilidža | 32 | 4,105.900 | 128.300 | B |
| 8a1ef4596967fff | Novi Grad Sarajevo | Briješće | 45 | 5,774.200 | 128.300 | A |
| 8a1ef6963347fff | Ilidža | Lasica | 10 | 1,284.000 | 128.400 | B |
| 8a1ea92cbbaffff | Ilidža | Doglodi | 22 | 2,825.200 | 128.400 | B |
| 8a1ef6965a07fff | Ilidža | Naselje Bulevar | 35 | 4,496.000 | 128.500 | B |
| 8a1ef4596917fff | Novi Grad Sarajevo | Briješće | 63 | 8,093.500 | 128.500 | A |
| 8a1ef6965a8ffff | Ilidža | Naselje Bulevar | 99 | 12,719.800 | 128.500 | B |
| 8a1ea92cd49ffff | Novi Grad Sarajevo | Dobroševići | 19 | 2,442.100 | 128.500 | A |
| 8a1ef4586aeffff | Centar Sarajevo | Betanija | 50 | 6,427.500 | 128.600 | B |
| 8a1ef458349ffff | Stari Grad Sarajevo | Baščaršija | 122 | 15,683.900 | 128.600 | A |
| 8a1ea92ccadffff | Novi Grad Sarajevo | Dobroševići | 13 | 1,671.400 | 128.600 | A |
| 8a1ea92cb707fff | Ilidža | Otes | 16 | 2,057.800 | 128.600 | B |
| 8a1ef4596947fff | Novi Grad Sarajevo | Briješće | 57 | 7,335.200 | 128.700 | A |
| 8a1ef6965b37fff | Ilidža | Naselje Bulevar | 35 | 4,506.500 | 128.800 | B |
| 8a1ef459610ffff | Novi Grad Sarajevo | Briješće | 30 | 3,864.600 | 128.800 | A |
| 8a1ea92c89a7fff | Novi Grad Sarajevo | Dobroševići | 18 | 2,318.900 | 128.800 | A |
| 8a1ef696566ffff | Ilidža | Butmir | 22 | 2,834.300 | 128.800 | B |
| 8a1ea92c975ffff | Novi Grad Sarajevo | Briješće | 54 | 6,957.300 | 128.800 | A |
| 8a1ea92cc11ffff | Novi Grad Sarajevo | Dobroševići | 10 | 1,288.700 | 128.900 | A |
| 8a1ef45b4487fff | Vogošća | Semizovac | 129 | 16,629.000 | 128.900 | B |
| 8a1ef69655affff | Ilidža | Lužani | 55 | 7,091.300 | 128.900 | B |
| 8a1ea92c0777fff | Ilidža | Rakovica | 12 | 1,547.400 | 129.000 | B |
| 8a1ea92c928ffff | Novi Grad Sarajevo | Briješće | 44 | 5,673.900 | 129.000 | A |
| 8a1ea92cc257fff | Novi Grad Sarajevo | Dobroševići | 20 | 2,580.200 | 129.000 | A |
| 8a1ea925b827fff | Vogošća | Gora | 13 | 1,678.100 | 129.100 | B |
| 8a1ea92ca467fff | Ilidža | Blažuj | 19 | 2,453.300 | 129.100 | B |
| 8a1ef6965a37fff | Ilidža | Naselje Bulevar | 33 | 4,261.700 | 129.100 | B |
| 8a1ea92cc6cffff | Novi Grad Sarajevo | Dobroševići | 15 | 1,937.200 | 129.100 | A |
| 8a1ea92c92f7fff | Novi Grad Sarajevo | Briješće | 53 | 6,844.800 | 129.100 | A |
| 8a1ef6960727fff | Ilidža | Kovači (Ilidža) | 12 | 1,550.100 | 129.200 | B |
| 8a1ea92cc70ffff | Novi Grad Sarajevo | Dobroševići | 13 | 1,679.300 | 129.200 | A |
| 8a1ea92d9967fff | Ilidža | Blažuj | 10 | 1,291.800 | 129.200 | B |
| 8a1ef4583b9ffff | Stari Grad Sarajevo | Mošćanica | 16 | 2,066.900 | 129.200 | A |
| 8a1ea92c0477fff | Ilidža | Rakovica | 11 | 1,421.100 | 129.200 | B |
| 8a1ef45830effff | Stari Grad Sarajevo | Mošćanica | 25 | 3,231.600 | 129.300 | A |
| 8a1ef45969a7fff | Novi Grad Sarajevo | Briješće | 71 | 9,179.600 | 129.300 | A |
| 8a1ef459694ffff | Novi Grad Sarajevo | Briješće | 64 | 8,278.200 | 129.300 | A |
| 8a1ef6964997fff | Ilidža | Kamenjača | 21 | 2,716.800 | 129.400 | B |
| 8a1ea92cb26ffff | Ilidža | Azići | 29 | 3,752.700 | 129.400 | B |
| 8a1ef6961b57fff | Ilidža | Donji Kotorac | 15 | 1,941.800 | 129.500 | B |
| 8a1ea92c925ffff | Novi Grad Sarajevo | Briješće | 34 | 4,401.600 | 129.500 | A |
| 8a1ef459c977fff | Stari Grad Sarajevo | Logavina | 202 | 26,157.000 | 129.500 | A |
| 8a1ef45b170ffff | Vogošća | Hotonj | 20 | 2,590.200 | 129.500 | B |
| 8a1ea92ca597fff | Ilidža | Blažuj | 10 | 1,295.300 | 129.500 | B |
| 8a1ef45965b7fff | Ilidža | Azići | 30 | 3,888.600 | 129.600 | B |
| 8a1ea92c0757fff | Ilidža | Rakovica | 16 | 2,074.100 | 129.600 | B |
| 8a1ef459685ffff | Novi Grad Sarajevo | Briješće | 74 | 9,594.100 | 129.700 | A |
| 8a1ea92c9667fff | Novi Grad Sarajevo | Briješće | 63 | 8,168.400 | 129.700 | A |
| 8a1ea92c8c1ffff | Novi Grad Sarajevo | Dobroševići | 18 | 2,334.000 | 129.700 | A |
| 8a1ea92c9557fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 55 | 7,131.800 | 129.700 | A |
| 8a1ef45964d7fff | Ilidža | Naselje Bulevar | 40 | 5,189.200 | 129.700 | B |
| 8a1ef4596847fff | Novi Grad Sarajevo | Briješće | 60 | 7,788.200 | 129.800 | A |
| 8a1ea92c929ffff | Novi Grad Sarajevo | Briješće | 58 | 7,528.900 | 129.800 | A |
| 8a1ef458364ffff | Stari Grad Sarajevo | Mošćanica | 25 | 3,245.900 | 129.800 | A |
| 8a1ef45840affff | Centar Sarajevo | Nahorevo | 13 | 1,689.000 | 129.900 | B |
| 8a1ef45817a7fff | Stari Grad Sarajevo | Mošćanica | 12 | 1,559.100 | 129.900 | A |
| 8a1ea92cc20ffff | Novi Grad Sarajevo | Dobroševići | 21 | 2,729.000 | 130.000 | A |
| 8a1ea92c3c0ffff | Ilidža | Rakovica | 14 | 1,819.800 | 130.000 | B |
| 8a1ea92ca0cffff | Ilidža | Osjek | 16 | 2,080.400 | 130.000 | B |
| 8a1ef4582a4ffff | Centar Sarajevo | Hrastovi-Mrkovići | 102 | 13,263.200 | 130.000 | B |
| 8a1ea92ce45ffff | Ilidža | Lipe | 17 | 2,210.700 | 130.000 | B |
| 8a1ea92c9257fff | Novi Grad Sarajevo | Briješće | 51 | 6,632.200 | 130.000 | A |
| 8a1ea92c3217fff | Ilidža | Gladno polje | 17 | 2,210.900 | 130.100 | B |
| 8a1ea92c3037fff | Ilidža | Gladno polje | 16 | 2,081.000 | 130.100 | B |
| 8a1ea92c8907fff | Novi Grad Sarajevo | Dobroševići | 13 | 1,690.900 | 130.100 | A |
| 8a1ef6965b77fff | Ilidža | Naselje Bulevar | 41 | 5,334.100 | 130.100 | B |
| 8a1ea92c00affff | Ilidža | Rakovica | 11 | 1,431.300 | 130.100 | B |
| 8a1ea92c31affff | Ilidža | Gladno polje | 13 | 1,691.700 | 130.100 | B |
| 8a1ea92c8357fff | Novi Grad Sarajevo | Briješće | 33 | 4,294.900 | 130.100 | A |
| 8a1ef459d14ffff | Stari Grad Sarajevo | Mošćanica | 13 | 1,692.600 | 130.200 | A |
| 8a1ea92cc367fff | Novi Grad Sarajevo | Dobroševići | 12 | 1,562.600 | 130.200 | A |
| 8a1ef459c907fff | Stari Grad Sarajevo | Ferhadija | 155 | 20,183.500 | 130.200 | A |
| 8a1ea92c3ce7fff | Ilidža | Rakovica | 18 | 2,344.300 | 130.200 | B |
| 8a1ef4596487fff | Ilidža | Naselje Bulevar | 33 | 4,298.500 | 130.300 | B |
| 8a1ea92c3187fff | Ilidža | Gladno polje | 14 | 1,823.900 | 130.300 | B |
| 8a1ea92c06d7fff | Ilidža | Rakovica | 16 | 2,085.100 | 130.300 | B |
| 8a1ef4596907fff | Novi Grad Sarajevo | Briješće | 67 | 8,731.300 | 130.300 | A |
| 8a1ef459686ffff | Novi Grad Sarajevo | Briješće | 58 | 7,558.700 | 130.300 | A |
| 8a1ef45846e7fff | Centar Sarajevo | Betanija | 27 | 3,518.800 | 130.300 | B |
| 8a1ea92cbba7fff | Ilidža | Doglodi | 15 | 1,955.300 | 130.400 | B |
| 8a1ea92ce0affff | Ilidža | Lipe | 13 | 1,694.900 | 130.400 | B |
| 8a1ea92c924ffff | Novi Grad Sarajevo | Briješće | 33 | 4,303.800 | 130.400 | A |
| 8a1ef4596807fff | Novi Grad Sarajevo | Briješće | 78 | 10,175.600 | 130.500 | A |
| 8a1ea92cc08ffff | Novi Grad Sarajevo | Dobroševići | 10 | 1,304.600 | 130.500 | A |
| 8a1ea92ddb0ffff | Ilidža | Lipe | 22 | 2,870.200 | 130.500 | B |
| 8a1ef4583b57fff | Stari Grad Sarajevo | Mošćanica | 21 | 2,739.800 | 130.500 | A |
| 8a1ea92cca47fff | Novi Grad Sarajevo | Dobroševići | 11 | 1,435.200 | 130.500 | A |
| 8a1ef6961d97fff | Ilidža | Sokolović-kolonija | 92 | 12,011.900 | 130.600 | B |
| 8a1ef6960a07fff | Ilidža | Sokolović-kolonija | 22 | 2,873.000 | 130.600 | B |
| 8a1ea92c92d7fff | Novi Grad Sarajevo | Briješće | 56 | 7,313.200 | 130.600 | A |
| 8a1ef6961917fff | Ilidža | Butmir | 29 | 3,789.000 | 130.700 | B |
| 8a1ea92cc6dffff | Novi Grad Sarajevo | Dobroševići | 16 | 2,090.700 | 130.700 | A |
| 8a1ef45b0847fff | Vogošća | Kremeš | 10 | 1,306.700 | 130.700 | B |
| 8a1ef696575ffff | Ilidža | Butmir | 27 | 3,528.400 | 130.700 | B |
| 8a1ef6961167fff | Ilidža | Donji Kotorac | 19 | 2,484.400 | 130.800 | B |
| 8a1ea92dd237fff | Ilidža | Lipe | 14 | 1,831.200 | 130.800 | B |
| 8a1ea92c92dffff | Novi Grad Sarajevo | Briješće | 55 | 7,194.200 | 130.800 | A |
| 8a1ea92cd517fff | Novi Grad Sarajevo | Dobroševići | 31 | 4,055.100 | 130.800 | A |
| 8a1ea92c0707fff | Ilidža | Rakovica | 16 | 2,093.100 | 130.800 | B |
| 8a1ea92c8cf7fff | Novi Grad Sarajevo | Dobroševići | 24 | 3,139.900 | 130.800 | A |
| 8a1ea92ce457fff | Ilidža | Lipe | 18 | 2,354.900 | 130.800 | B |
| 8a1ea92dda6ffff | Ilidža | Lipe | 19 | 2,485.800 | 130.800 | B |
| 8a1ea92cb337fff | Ilidža | Azići | 20 | 2,616.800 | 130.800 | B |
| 8a1ef458310ffff | Stari Grad Sarajevo | Mošćanica | 33 | 4,318.300 | 130.900 | A |
| 8a1ef4594517fff | Novi Grad Sarajevo | Briješće | 27 | 3,534.800 | 130.900 | A |
| 8a1ea92c9567fff | Novi Grad Sarajevo | Naselje heroja Sokolje | 109 | 14,270.400 | 130.900 | A |
| 8a1ea92ca59ffff | Ilidža | Blažuj | 17 | 2,226.300 | 131.000 | B |
| 8a1ef69655b7fff | Ilidža | Lužani | 10 | 1,310.100 | 131.000 | B |
| 8a1ea92ca967fff | Ilidža | Dolovi | 12 | 1,572.600 | 131.100 | B |
| 8a1ef4584817fff | Centar Sarajevo | Nahorevo | 30 | 3,931.800 | 131.100 | B |
| 8a1ef6965aaffff | Ilidža | Naselje Bulevar | 35 | 4,588.600 | 131.100 | B |
| 8a1ef4586a57fff | Centar Sarajevo | Betanija | 51 | 6,686.600 | 131.100 | B |
| 8a1ea92c8947fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,311.200 | 131.100 | A |
| 8a1ef45b3997fff | Vogošća | Ugorsko | 12 | 1,573.500 | 131.100 | B |
| 8a1ea92c8b2ffff | Novi Grad Sarajevo | Dobroševići | 11 | 1,442.800 | 131.200 | A |
| 8a1ea92ca6b7fff | Ilidža | Blažuj | 13 | 1,705.200 | 131.200 | B |
| 8a1ea92cc31ffff | Novi Grad Sarajevo | Dobroševići | 15 | 1,967.600 | 131.200 | A |
| 8a1ef6964d67fff | Ilidža | Plandište | 13 | 1,705.800 | 131.200 | B |
| 8a1ea92c88b7fff | Novi Grad Sarajevo | Dobroševići | 21 | 2,755.800 | 131.200 | A |
| 8a1ef696114ffff | Ilidža | Donji Kotorac | 26 | 3,412.000 | 131.200 | B |
| 8a1ef6961baffff | Ilidža | Donji Kotorac | 20 | 2,625.600 | 131.300 | B |
| 8a1ea92ca767fff | Ilidža | Osjek | 19 | 2,495.300 | 131.300 | B |
| 8a1ea92c89affff | Novi Grad Sarajevo | Dobroševići | 28 | 3,677.800 | 131.300 | A |
| 8a1ea92cd457fff | Novi Grad Sarajevo | Dobroševići | 19 | 2,495.900 | 131.400 | A |
| 8a1ea92c8817fff | Novi Grad Sarajevo | Dobroševići | 30 | 3,941.300 | 131.400 | A |
| 8a1ea92dd167fff | Ilidža | Lipe | 15 | 1,971.200 | 131.400 | B |
| 8a1ef45945affff | Novi Grad Sarajevo | Briješće | 60 | 7,888.300 | 131.500 | A |
| 8a1ef4583437fff | Stari Grad Sarajevo | Kovači | 105 | 13,810.700 | 131.500 | A |
| 8a1ef458e92ffff | Stari Grad Sarajevo | Mošćanica | 11 | 1,447.000 | 131.500 | A |
| 8a1ef459682ffff | Novi Grad Sarajevo | Briješće | 80 | 10,524.000 | 131.600 | A |
| 8a1ef6965287fff | Ilidža | Butmir | 22 | 2,895.400 | 131.600 | B |
| 8a1ea92cb397fff | Ilidža | Azići | 22 | 2,895.700 | 131.600 | B |
| 8a1ef45945b7fff | Novi Grad Sarajevo | Briješće | 57 | 7,503.600 | 131.600 | A |
| 8a1ea92cac37fff | Ilidža | Lipe | 11 | 1,448.300 | 131.700 | B |
| 8a1ea92c3c5ffff | Ilidža | Rakovica | 14 | 1,843.700 | 131.700 | B |
| 8a1ef6963aa7fff | Ilidža | Lasica | 20 | 2,635.600 | 131.800 | B |
| 8a1ef6961a37fff | Ilidža | Donji Kotorac | 20 | 2,635.800 | 131.800 | B |
| 8a1ea92ca327fff | Ilidža | Bjelaće | 14 | 1,845.700 | 131.800 | B |
| 8a1ea92cc21ffff | Novi Grad Sarajevo | Dobroševići | 22 | 2,900.900 | 131.900 | A |
| 8a1ef4582127fff | Centar Sarajevo | Džidžikovac-Koševo I | 175 | 23,077.800 | 131.900 | B |
| 8a1ef6961997fff | Ilidža | Butmir | 24 | 3,166.400 | 131.900 | B |
| 8a1ef6961b1ffff | Ilidža | Donji Kotorac | 19 | 2,508.600 | 132.000 | B |
| 8a1ea92cc227fff | Novi Grad Sarajevo | Dobroševići | 19 | 2,509.200 | 132.100 | A |
| 8a1ef696385ffff | Ilidža | Hrasnica | 12 | 1,586.200 | 132.200 | B |
| 8a1ef458305ffff | Stari Grad Sarajevo | Mošćanica | 26 | 3,436.900 | 132.200 | A |
| 8a1ef459c867fff | Stari Grad Sarajevo | Baščaršija | 152 | 20,095.400 | 132.200 | A |
| 8a1ea92cd097fff | Novi Grad Sarajevo | Dobroševići | 14 | 1,851.400 | 132.200 | A |
| 8a1ea92cc3a7fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,322.500 | 132.200 | A |
| 8a1ea92cc04ffff | Novi Grad Sarajevo | Dobroševići | 12 | 1,587.200 | 132.300 | A |
| 8a1ef696424ffff | Ilidža | Lužani | 18 | 2,381.000 | 132.300 | B |
| 8a1ea92caba7fff | Ilidža | Dolovi | 14 | 1,851.900 | 132.300 | B |
| 8a1ef459c957fff | Stari Grad Sarajevo | Baščaršija | 151 | 19,975.400 | 132.300 | A |
| 8a1ef6965537fff | Ilidža | Lužani | 17 | 2,249.100 | 132.300 | B |
| 8a1ea92c046ffff | Ilidža | Rakovica | 10 | 1,323.100 | 132.300 | B |
| 8a1ea92cd42ffff | Novi Grad Sarajevo | Dobroševići | 17 | 2,249.500 | 132.300 | A |
| 8a1ea92cd417fff | Novi Grad Sarajevo | Dobroševići | 17 | 2,249.600 | 132.300 | A |
| 8a1ea92cca57fff | Novi Grad Sarajevo | Dobroševići | 13 | 1,720.400 | 132.300 | A |
| 8a1ea92ca067fff | Ilidža | Bjelaće | 14 | 1,852.700 | 132.300 | B |
| 8a1ef696198ffff | Ilidža | Butmir | 33 | 4,367.600 | 132.400 | B |
| 8a1ea92cc35ffff | Novi Grad Sarajevo | Dobroševići | 25 | 3,308.900 | 132.400 | A |
| 8a1ea92ca427fff | Ilidža | Blažuj | 21 | 2,780.100 | 132.400 | B |
| 8a1ea92c89b7fff | Novi Grad Sarajevo | Dobroševići | 19 | 2,515.400 | 132.400 | A |
| 8a1ea92ca797fff | Ilidža | Blažuj | 16 | 2,119.400 | 132.500 | B |
| 8a1ea92c2b67fff | Ilidža | Rudnik | 10 | 1,325.100 | 132.500 | B |
| 8a1ea92c364ffff | Ilidža | Gladno polje | 21 | 2,782.700 | 132.500 | B |
| 8a1ef696565ffff | Ilidža | Butmir | 29 | 3,843.200 | 132.500 | B |
| 8a1ef45830e7fff | Stari Grad Sarajevo | Mošćanica | 18 | 2,385.500 | 132.500 | A |
| 8a1ea92ca6a7fff | Ilidža | Plandište | 17 | 2,253.200 | 132.500 | B |
| 8a1ea92ddaf7fff | Ilidža | Lipe | 16 | 2,120.800 | 132.500 | B |
| 8a1ea92cc66ffff | Novi Grad Sarajevo | Dobroševići | 22 | 2,916.200 | 132.600 | A |
| 8a1ea92c0617fff | Ilidža | Rakovica | 18 | 2,386.500 | 132.600 | B |
| 8a1ea92ca74ffff | Ilidža | Osjek | 20 | 2,651.900 | 132.600 | B |
| 8a1ef696425ffff | Ilidža | Lužani | 18 | 2,387.500 | 132.600 | B |
| 8a1ea92cb647fff | Ilidža | Pejton | 34 | 4,510.500 | 132.700 | B |
| 8a1ea92cc017fff | Novi Grad Sarajevo | Dobroševići | 13 | 1,724.600 | 132.700 | A |
| 8a1ea92dda2ffff | Ilidža | Lipe | 22 | 2,918.600 | 132.700 | B |
| 8a1ea92ca337fff | Ilidža | Bjelaće | 19 | 2,520.900 | 132.700 | B |
| 8a1ea92cb46ffff | Ilidža | Otes | 19 | 2,520.900 | 132.700 | B |
| 8a1ea92ddb17fff | Ilidža | Lipe | 17 | 2,255.900 | 132.700 | B |
| 8a1ea92ccac7fff | Novi Grad Sarajevo | Dobroševići | 15 | 1,990.500 | 132.700 | A |
| 8a1ea92c071ffff | Ilidža | Rakovica | 15 | 1,990.900 | 132.700 | B |
| 8a1ea92ca44ffff | Ilidža | Blažuj | 16 | 2,123.700 | 132.700 | B |
| 8a1ea92c812ffff | Novi Grad Sarajevo | Dobroševići | 18 | 2,389.200 | 132.700 | A |
| 8a1ea92c8997fff | Novi Grad Sarajevo | Dobroševići | 29 | 3,850.000 | 132.800 | A |
| 8a1ea92c8c6ffff | Novi Grad Sarajevo | Dobroševići | 26 | 3,453.500 | 132.800 | A |
| 8a1ef459d15ffff | Stari Grad Sarajevo | Mošćanica | 18 | 2,392.300 | 132.900 | A |
| 8a1ea92cc657fff | Novi Grad Sarajevo | Dobroševići | 19 | 2,525.500 | 132.900 | A |
| 8a1ef6961b07fff | Ilidža | Donji Kotorac | 26 | 3,456.400 | 132.900 | B |
| 8a1ef6965b57fff | Novi Grad Sarajevo | Saraj Polje | 58 | 7,711.200 | 133.000 | A |
| 8a1ea92cbb8ffff | Novi Grad Sarajevo | Briješće | 34 | 4,520.400 | 133.000 | A |
| 8a1ea92dda9ffff | Ilidža | Lipe | 14 | 1,861.400 | 133.000 | B |
| 8a1ea92caa9ffff | Ilidža | Bjelaće | 16 | 2,127.600 | 133.000 | B |
| 8a1ef6961867fff | Ilidža | Donji Kotorac | 15 | 1,994.600 | 133.000 | B |
| 8a1ea92c885ffff | Novi Grad Sarajevo | Dobroševići | 14 | 1,861.800 | 133.000 | A |
| 8a1ea92cd4c7fff | Novi Grad Sarajevo | Dobroševići | 32 | 4,255.800 | 133.000 | A |
| 8a1ea92cdc27fff | Novi Grad Sarajevo | Dobroševići | 13 | 1,729.000 | 133.000 | A |
| 8a1ef458411ffff | Centar Sarajevo | Nahorevo | 36 | 4,788.100 | 133.000 | B |
| 8a1ef6961c67fff | Ilidža | Butmir | 76 | 10,109.700 | 133.000 | B |
| 8a1ea92c06f7fff | Ilidža | Rakovica | 16 | 2,128.800 | 133.100 | B |
| 8a1ea92c8857fff | Novi Grad Sarajevo | Dobroševići | 29 | 3,858.700 | 133.100 | A |
| 8a1ea92cdd9ffff | Novi Grad Sarajevo | Dobroševići | 18 | 2,395.400 | 133.100 | A |
| 8a1ea92cc24ffff | Novi Grad Sarajevo | Dobroševići | 29 | 3,860.300 | 133.100 | A |
| 8a1ef69658e7fff | Ilidža | Naselje Bulevar | 42 | 5,590.900 | 133.100 | B |
| 8a1ea92cdc97fff | Novi Grad Sarajevo | Dobroševići | 26 | 3,461.100 | 133.100 | A |
| 8a1ef6965867fff | Ilidža | Naselje Bulevar | 40 | 5,324.900 | 133.100 | B |
| 8a1ef6964c1ffff | Ilidža | Vrelo Bosne | 15 | 1,997.100 | 133.100 | B |
| 8a1ef6965847fff | Ilidža | Naselje Bulevar | 45 | 5,991.200 | 133.100 | B |
| 8a1ea92cd59ffff | Novi Grad Sarajevo | Dobroševići | 20 | 2,663.100 | 133.200 | A |
| 8a1ea92cbc47fff | Ilidža | Doglodi | 15 | 1,997.800 | 133.200 | B |
| 8a1ea92c889ffff | Novi Grad Sarajevo | Dobroševići | 28 | 3,729.700 | 133.200 | A |
| 8a1ef6963aaffff | Ilidža | Lasica | 22 | 2,930.600 | 133.200 | B |
| 8a1ef4583027fff | Stari Grad Sarajevo | Mošćanica | 30 | 3,996.300 | 133.200 | A |
| 8a1ea92c880ffff | Novi Grad Sarajevo | Dobroševići | 24 | 3,197.300 | 133.200 | A |
| 8a1ea92dd227fff | Ilidža | Lipe | 29 | 3,863.600 | 133.200 | B |
| 8a1ea92cc65ffff | Novi Grad Sarajevo | Dobroševići | 26 | 3,464.300 | 133.200 | A |
| 8a1ef69649affff | Ilidža | Kamenjača | 29 | 3,864.300 | 133.300 | B |
| 8a1ea92cd4f7fff | Novi Grad Sarajevo | Dobroševići | 31 | 4,131.500 | 133.300 | A |
| 8a1ef696564ffff | Ilidža | Butmir | 26 | 3,465.800 | 133.300 | B |
| 8a1ea92cd0b7fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,333.100 | 133.300 | A |
| 8a1ea92cac17fff | Ilidža | Lipe | 20 | 2,666.400 | 133.300 | B |
| 8a1ef696558ffff | Ilidža | Lužani | 13 | 1,733.600 | 133.400 | B |
| 8a1ea92ca85ffff | Ilidža | Dolovi | 14 | 1,867.100 | 133.400 | B |
| 8a1ea92dd84ffff | Ilidža | Lipe | 14 | 1,867.400 | 133.400 | B |
| 8a1ea92cace7fff | Ilidža | Blažuj | 19 | 2,534.600 | 133.400 | B |
| 8a1ea92ca077fff | Ilidža | Osjek | 15 | 2,001.500 | 133.400 | B |
| 8a1ea92ca8b7fff | Ilidža | Dolovi | 10 | 1,334.300 | 133.400 | B |
| 8a1ef6965a97fff | Ilidža | Naselje Bulevar | 23 | 3,069.300 | 133.400 | B |
| 8a1ea92c899ffff | Novi Grad Sarajevo | Dobroševići | 34 | 4,537.800 | 133.500 | A |
| 8a1ef458329ffff | Stari Grad Sarajevo | Mošćanica | 24 | 3,203.900 | 133.500 | A |
| 8a1ef4599d1ffff | Stari Grad Sarajevo | Širokača | 10 | 1,335.000 | 133.500 | A |
| 8a1ea92cc267fff | Novi Grad Sarajevo | Dobroševići | 31 | 4,138.800 | 133.500 | A |
| 8a1ea92cb907fff | Ilidža | Doglodi | 15 | 2,003.100 | 133.500 | B |
| 8a1ef459651ffff | Ilidža | Stup | 43 | 5,742.400 | 133.500 | B |
| 8a1ef696399ffff | Ilidža | Hrasnica | 27 | 3,606.800 | 133.600 | B |
| 8a1ef45967affff | Ilidža | Stupsko Brdo | 51 | 6,812.800 | 133.600 | B |
| 8a1ea92cc297fff | Novi Grad Sarajevo | Dobroševići | 23 | 3,072.600 | 133.600 | A |
| 8a1ea92cb0f7fff | Ilidža | Doglodi | 12 | 1,603.200 | 133.600 | B |
| 8a1ef4580027fff | Centar Sarajevo | Hrastovi-Mrkovići | 19 | 2,539.700 | 133.700 | B |
| 8a1ea92dd92ffff | Ilidža | Gladno polje | 18 | 2,407.100 | 133.700 | B |
| 8a1ea92c88e7fff | Novi Grad Sarajevo | Dobroševići | 40 | 5,351.000 | 133.800 | A |
| 8a1ef6965617fff | Ilidža | Butmir | 18 | 2,408.100 | 133.800 | B |
| 8a1ef69642c7fff | Ilidža | Lužani | 11 | 1,472.500 | 133.900 | B |
| 8a1ea92ca2b7fff | Ilidža | Osjek | 21 | 2,811.700 | 133.900 | B |
| 8a1ea92cdcb7fff | Novi Grad Sarajevo | Dobroševići | 24 | 3,213.900 | 133.900 | A |
| 8a1ea92c8917fff | Novi Grad Sarajevo | Dobroševići | 22 | 2,947.100 | 134.000 | A |
| 8a1ef696490ffff | Ilidža | Kamenjača | 27 | 3,617.600 | 134.000 | B |
| 8a1ef459679ffff | Ilidža | Stupsko Brdo | 47 | 6,298.100 | 134.000 | B |
| 8a1ea92cd51ffff | Novi Grad Sarajevo | Dobroševići | 33 | 4,422.600 | 134.000 | A |
| 8a1ef696190ffff | Ilidža | Butmir | 33 | 4,424.200 | 134.100 | B |
| 8a1ef696195ffff | Ilidža | Donji Kotorac | 32 | 4,290.800 | 134.100 | B |
| 8a1ef69610d7fff | Ilidža | Butmir | 10 | 1,341.000 | 134.100 | B |
| 8a1ea92cb947fff | Ilidža | Doglodi | 18 | 2,414.900 | 134.200 | B |
| 8a1ef6964aa7fff | Ilidža | Vreoca | 28 | 3,759.800 | 134.300 | B |
| 8a1ea92c882ffff | Novi Grad Sarajevo | Dobroševići | 13 | 1,745.700 | 134.300 | A |
| 8a1ea92cc6a7fff | Novi Grad Sarajevo | Dobroševići | 11 | 1,477.200 | 134.300 | A |
| 8a1ea92cb4e7fff | Ilidža | Otes | 19 | 2,552.300 | 134.300 | B |
| 8a1ea92c0717fff | Ilidža | Rakovica | 14 | 1,881.400 | 134.400 | B |
| 8a1ef6960067fff | Ilidža | Kovači (Ilidža) | 21 | 2,822.500 | 134.400 | B |
| 8a1ea92cc79ffff | Novi Grad Sarajevo | Dobroševići | 12 | 1,613.300 | 134.400 | A |
| 8a1ea92c3717fff | Ilidža | Gladno polje | 12 | 1,613.300 | 134.400 | B |
| 8a1ef4581657fff | Stari Grad Sarajevo | Mošćanica | 11 | 1,478.900 | 134.400 | A |
| 8a1ea92c8ce7fff | Novi Grad Sarajevo | Dobroševići | 31 | 4,167.900 | 134.400 | A |
| 8a1ea92cca87fff | Novi Grad Sarajevo | Dobroševići | 12 | 1,613.400 | 134.500 | A |
| 8a1ef696508ffff | Ilidža | Butmir | 26 | 3,495.800 | 134.500 | B |
| 8a1ea92cba87fff | Ilidža | Azići | 25 | 3,362.400 | 134.500 | B |
| 8a1ea92cb6affff | Ilidža | Pejton | 44 | 5,918.100 | 134.500 | B |
| 8a1ea92ccad7fff | Novi Grad Sarajevo | Dobroševići | 15 | 2,018.100 | 134.500 | A |
| 8a1ea92cb98ffff | Ilidža | Doglodi | 20 | 2,691.100 | 134.600 | B |
| 8a1ef6961877fff | Ilidža | Donji Kotorac | 26 | 3,499.100 | 134.600 | B |
| 8a1ef696115ffff | Ilidža | Donji Kotorac | 14 | 1,884.700 | 134.600 | B |
| 8a1ea92cc22ffff | Novi Grad Sarajevo | Dobroševići | 22 | 2,961.900 | 134.600 | A |
| 8a1ea92cd4d7fff | Novi Grad Sarajevo | Dobroševići | 37 | 4,982.400 | 134.700 | A |
| 8a1ef6961a87fff | Ilidža | Donji Kotorac | 32 | 4,310.300 | 134.700 | B |
| 8a1ea92ca19ffff | Ilidža | Blažuj | 89 | 11,992.100 | 134.700 | B |
| 8a1ea92ca497fff | Ilidža | Blažuj | 14 | 1,887.200 | 134.800 | B |
| 8a1ea92ca557fff | Ilidža | Blažuj | 19 | 2,561.900 | 134.800 | B |
| 8a1ef6964a27fff | Ilidža | Vreoca | 13 | 1,753.000 | 134.800 | B |
| 8a1ea92cb94ffff | Ilidža | Doglodi | 15 | 2,022.900 | 134.900 | B |
| 8a1ea92cb6b7fff | Ilidža | Pejton | 34 | 4,585.300 | 134.900 | B |
| 8a1ef4583ae7fff | Stari Grad Sarajevo | Mošćanica | 22 | 2,967.500 | 134.900 | A |
| 8a1ef6961b27fff | Ilidža | Donji Kotorac | 23 | 3,103.300 | 134.900 | B |
| 8a1ea92ca55ffff | Ilidža | Blažuj | 22 | 2,969.200 | 135.000 | B |
| 8a1ef6961a17fff | Ilidža | Donji Kotorac | 31 | 4,184.100 | 135.000 | B |
| 8a1ea92cbd6ffff | Ilidža | Doglodi | 19 | 2,564.800 | 135.000 | B |
| 8a1ef6965bb7fff | Ilidža | Naselje Bulevar | 44 | 5,940.500 | 135.000 | B |
| 8a1ef4583aaffff | Stari Grad Sarajevo | Mošćanica | 23 | 3,105.300 | 135.000 | A |
| 8a1ea92c849ffff | Ilidža | Dolovi | 18 | 2,430.300 | 135.000 | B |
| 8a1ea92c3207fff | Ilidža | Gladno polje | 17 | 2,296.300 | 135.100 | B |
| 8a1ef6965b9ffff | Ilidža | Naselje Bulevar | 39 | 5,268.400 | 135.100 | B |
| 8a1ea92caaf7fff | Ilidža | Bjelaće | 13 | 1,756.500 | 135.100 | B |
| 8a1ef6965b47fff | Ilidža | Naselje Bulevar | 46 | 6,216.200 | 135.100 | B |
| 8a1ea92ccbb7fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,351.700 | 135.200 | A |
| 8a1ea92dd837fff | Ilidža | Gladno polje | 23 | 3,109.500 | 135.200 | B |
| 8a1ea92ca627fff | Ilidža | Osjek | 23 | 3,109.800 | 135.200 | B |
| 8a1ea92ce4effff | Ilidža | Lipe | 24 | 3,246.300 | 135.300 | B |
| 8a1ea92cdd0ffff | Novi Grad Sarajevo | Dobroševići | 10 | 1,352.700 | 135.300 | A |
| 8a1ef6960ac7fff | Ilidža | Sokolović-kolonija | 27 | 3,653.000 | 135.300 | B |
| 8a1ef4596637fff | Ilidža | Stupsko Brdo | 50 | 6,765.200 | 135.300 | B |
| 8a1ea92c3a97fff | Ilidža | Gladno polje | 12 | 1,623.800 | 135.300 | B |
| 8a1ea92ca22ffff | Ilidža | Osjek | 14 | 1,894.900 | 135.300 | B |
| 8a1ea92cc117fff | Novi Grad Sarajevo | Dobroševići | 11 | 1,489.300 | 135.400 | A |
| 8a1ef6960747fff | Ilidža | Kovači (Ilidža) | 15 | 2,031.100 | 135.400 | B |
| 8a1ea92cb11ffff | Ilidža | Doglodi | 13 | 1,760.800 | 135.400 | B |
| 8a1ea92ca517fff | Ilidža | Blažuj | 15 | 2,032.100 | 135.500 | B |
| 8a1ef69656effff | Ilidža | Butmir | 29 | 3,929.200 | 135.500 | B |
| 8a1ea92ca727fff | Ilidža | Osjek | 11 | 1,491.100 | 135.600 | B |
| 8a1ef6965677fff | Ilidža | Butmir | 35 | 4,745.400 | 135.600 | B |
| 8a1ef45964dffff | Ilidža | Naselje Bulevar | 49 | 6,644.700 | 135.600 | B |
| 8a1ef458288ffff | Centar Sarajevo | Džidžikovac-Koševo I | 131 | 17,766.600 | 135.600 | B |
| 8a1ea92cc047fff | Novi Grad Sarajevo | Dobroševići | 15 | 2,034.300 | 135.600 | A |
| 8a1ea92cca0ffff | Novi Grad Sarajevo | Dobroševići | 13 | 1,763.400 | 135.600 | A |
| 8a1ea92caca7fff | Ilidža | Lipe | 20 | 2,714.000 | 135.700 | B |
| 8a1ef4583af7fff | Stari Grad Sarajevo | Mošćanica | 21 | 2,850.700 | 135.700 | A |
| 8a1ea92ca317fff | Ilidža | Osjek | 22 | 2,986.500 | 135.800 | B |
| 8a1ea92cc0affff | Novi Grad Sarajevo | Dobroševići | 11 | 1,494.000 | 135.800 | A |
| 8a1ea92c8c47fff | Novi Grad Sarajevo | Dobroševići | 29 | 3,939.700 | 135.900 | A |
| 8a1ea92c068ffff | Ilidža | Rakovica | 18 | 2,445.400 | 135.900 | B |
| 8a1ea92cac0ffff | Ilidža | Lipe | 11 | 1,494.500 | 135.900 | B |
| 8a1ea92cb347fff | Ilidža | Azići | 25 | 3,397.200 | 135.900 | B |
| 8a1ea92cb677fff | Ilidža | Pejton | 24 | 3,261.600 | 135.900 | B |
| 8a1ea92c075ffff | Ilidža | Rakovica | 15 | 2,038.500 | 135.900 | B |
| 8a1ef459d517fff | Stari Grad Sarajevo | Hrid-Jarčedoli | 34 | 4,620.700 | 135.900 | A |
| 8a1ea92cc2a7fff | Novi Grad Sarajevo | Dobroševići | 20 | 2,718.300 | 135.900 | A |
| 8a1ef45b2527fff | Novi Grad Sarajevo | Reljevo | 23 | 3,126.800 | 135.900 | A |
| 8a1ea92c3667fff | Ilidža | Gladno polje | 13 | 1,767.500 | 136.000 | B |
| 8a1ef696596ffff | Ilidža | Naselje Bulevar | 29 | 3,943.000 | 136.000 | B |
| 8a1ef69618a7fff | Ilidža | Butmir | 44 | 5,983.100 | 136.000 | B |
| 8a1ef6964b87fff | Ilidža | Vreoca | 29 | 3,943.900 | 136.000 | B |
| 8a1ef69648affff | Ilidža | Kamenjača | 21 | 2,856.100 | 136.000 | B |
| 8a1ea92cd477fff | Novi Grad Sarajevo | Dobroševići | 26 | 3,537.700 | 136.100 | A |
| 8a1ef696484ffff | Ilidža | Vreoca | 20 | 2,721.400 | 136.100 | B |
| 8a1ea92ccacffff | Novi Grad Sarajevo | Dobroševići | 23 | 3,129.600 | 136.100 | A |
| 8a1ea92cc38ffff | Novi Grad Sarajevo | Dobroševići | 18 | 2,450.100 | 136.100 | A |
| 8a1ef696489ffff | Ilidža | Plandište | 18 | 2,450.300 | 136.100 | B |
| 8a1ea92ca8affff | Ilidža | Dolovi | 12 | 1,633.900 | 136.200 | B |
| 8a1ea92ddb5ffff | Ilidža | Lipe | 26 | 3,540.100 | 136.200 | B |
| 8a1ef4580baffff | Centar Sarajevo | Betanija | 19 | 2,587.100 | 136.200 | B |
| 8a1ea92ca3a7fff | Ilidža | Osjek | 24 | 3,268.400 | 136.200 | B |
| 8a1ef6965aeffff | Ilidža | Stupsko Brdo | 54 | 7,354.200 | 136.200 | B |
| 8a1ef6961807fff | Ilidža | Donji Kotorac | 32 | 4,358.200 | 136.200 | B |
| 8a1ea92cb447fff | Ilidža | Otes | 20 | 2,725.500 | 136.300 | B |
| 8a1ea92c8d47fff | Novi Grad Sarajevo | Dobroševići | 22 | 2,998.200 | 136.300 | A |
| 8a1ea92cb657fff | Ilidža | Pejton | 32 | 4,361.000 | 136.300 | B |
| 8a1ea92cdc9ffff | Novi Grad Sarajevo | Dobroševići | 24 | 3,271.900 | 136.300 | A |
| 8a1ea92ca657fff | Ilidža | Kamenjača | 18 | 2,454.200 | 136.300 | B |
| 8a1ef6964a17fff | Ilidža | Vreoca | 32 | 4,363.000 | 136.300 | B |
| 8a1ea92cc7affff | Novi Grad Sarajevo | Dobroševići | 15 | 2,045.300 | 136.400 | A |
| 8a1ef696519ffff | Ilidža | Ilidža | 159 | 21,690.500 | 136.400 | B |
| 8a1ef6965b87fff | Ilidža | Naselje Bulevar | 41 | 5,593.700 | 136.400 | B |
| 8a1ef6960a37fff | Ilidža | Sokolović-kolonija | 25 | 3,411.300 | 136.500 | B |
| 8a1ef6960b8ffff | Ilidža | Sokolović-kolonija | 25 | 3,412.100 | 136.500 | B |
| 8a1ea92c88d7fff | Novi Grad Sarajevo | Dobroševići | 38 | 5,188.000 | 136.500 | A |
| 8a1ef69619affff | Ilidža | Butmir | 42 | 5,734.600 | 136.500 | B |
| 8a1ea92cad47fff | Ilidža | Lipe | 10 | 1,365.600 | 136.600 | B |
| 8a1ef459249ffff | Ilidža | Donji Kotorac | 21 | 2,867.700 | 136.600 | B |
| 8a1ea92c07b7fff | Ilidža | Rudnik | 11 | 1,502.500 | 136.600 | B |
| 8a1ea92d9b0ffff | Ilidža | Blažuj | 17 | 2,322.500 | 136.600 | B |
| 8a1ea92c886ffff | Novi Grad Sarajevo | Dobroševići | 31 | 4,236.200 | 136.700 | A |
| 8a1ea92cc647fff | Novi Grad Sarajevo | Dobroševići | 38 | 5,193.300 | 136.700 | A |
| 8a1ea92ca667fff | Ilidža | Osjek | 30 | 4,101.900 | 136.700 | B |
| 8a1ef6963307fff | Ilidža | Lasica | 14 | 1,914.200 | 136.700 | B |
| 8a1ea92cc727fff | Novi Grad Sarajevo | Dobroševići | 17 | 2,325.100 | 136.800 | A |
| 8a1ea92c339ffff | Ilidža | Gladno polje | 16 | 2,188.900 | 136.800 | B |
| 8a1ea92c85b7fff | Ilidža | Dolovi | 14 | 1,915.400 | 136.800 | B |
| 8a1ef6963d47fff | Ilidža | Hrasnica | 18 | 2,463.200 | 136.800 | B |
| 8a1ef696512ffff | Ilidža | Ilidža | 32 | 4,379.100 | 136.800 | B |
| 8a1ea92c8caffff | Novi Grad Sarajevo | Dobroševići | 12 | 1,642.300 | 136.900 | A |
| 8a1ea92cc8d7fff | Novi Grad Sarajevo | Dobroševići | 17 | 2,326.900 | 136.900 | A |
| 8a1ea92cb457fff | Ilidža | Otes | 20 | 2,737.900 | 136.900 | B |
| 8a1ea92c3227fff | Ilidža | Gladno polje | 11 | 1,506.000 | 136.900 | B |
| 8a1ea92c88affff | Novi Grad Sarajevo | Dobroševići | 51 | 6,983.200 | 136.900 | A |
| 8a1ea92cacaffff | Ilidža | Blažuj | 14 | 1,917.000 | 136.900 | B |
| 8a1ea92cbd4ffff | Ilidža | Doglodi | 20 | 2,738.700 | 136.900 | B |
| 8a1ea92cd537fff | Novi Grad Sarajevo | Dobroševići | 31 | 4,245.200 | 136.900 | A |
| 8a1ef696180ffff | Ilidža | Donji Kotorac | 26 | 3,561.100 | 137.000 | B |
| 8a1ef6965b2ffff | Ilidža | Naselje Bulevar | 49 | 6,713.800 | 137.000 | B |
| 8a1ef6965a1ffff | Ilidža | Naselje Bulevar | 50 | 6,851.100 | 137.000 | B |
| 8a1ef69648effff | Ilidža | Vreoca | 26 | 3,563.200 | 137.000 | B |
| 8a1ea92ca2dffff | Ilidža | Kamenjača | 22 | 3,015.200 | 137.100 | B |
| 8a1ea92cd4b7fff | Novi Grad Sarajevo | Dobroševići | 12 | 1,644.600 | 137.100 | A |
| 8a1ef6960037fff | Ilidža | Stojčevac | 10 | 1,370.700 | 137.100 | B |
| 8a1ea92c074ffff | Ilidža | Rakovica | 10 | 1,371.200 | 137.100 | B |
| 8a1ef4586a2ffff | Centar Sarajevo | Betanija | 59 | 8,092.500 | 137.200 | B |
| 8a1ea92dd31ffff | Ilidža | Lipe | 22 | 3,018.500 | 137.200 | B |
| 8a1ea92c00dffff | Ilidža | Rakovica | 11 | 1,509.500 | 137.200 | B |
| 8a1ef6964927fff | Ilidža | Osjek | 28 | 3,842.900 | 137.200 | B |
| 8a1ea92cb60ffff | Ilidža | Pejton | 36 | 4,941.500 | 137.300 | B |
| 8a1ef69651affff | Ilidža | Ilidža | 21 | 2,883.000 | 137.300 | B |
| 8a1ea92cc6affff | Novi Grad Sarajevo | Dobroševići | 14 | 1,922.300 | 137.300 | A |
| 8a1ef459608ffff | Ilidža | Stupsko Brdo | 31 | 4,256.500 | 137.300 | B |
| 8a1ea92ce497fff | Ilidža | Gladno polje | 17 | 2,334.200 | 137.300 | B |
| 8a1ea92cb32ffff | Ilidža | Azići | 25 | 3,432.900 | 137.300 | B |
| 8a1ea92ddb07fff | Ilidža | Lipe | 20 | 2,746.400 | 137.300 | B |
| 8a1ef696189ffff | Ilidža | Butmir | 32 | 4,394.600 | 137.300 | B |
| 8a1ef4583a5ffff | Stari Grad Sarajevo | Mošćanica | 13 | 1,785.700 | 137.400 | A |
| 8a1ea92c8d6ffff | Novi Grad Sarajevo | Dobroševići | 39 | 5,359.300 | 137.400 | A |
| 8a1ea92ddadffff | Ilidža | Lipe | 26 | 3,572.900 | 137.400 | B |
| 8a1ea92c0507fff | Ilidža | Kobiljača | 10 | 1,374.300 | 137.400 | B |
| 8a1ea92ca647fff | Ilidža | Kamenjača | 29 | 3,985.700 | 137.400 | B |
| 8a1ea92c8847fff | Novi Grad Sarajevo | Dobroševići | 37 | 5,085.400 | 137.400 | A |
| 8a1ea92dd2cffff | Ilidža | Blažuj | 19 | 2,611.600 | 137.500 | B |
| 8a1ea92c00a7fff | Ilidža | Rakovica | 11 | 1,512.000 | 137.500 | B |
| 8a1ea92c311ffff | Ilidža | Gladno polje | 13 | 1,787.500 | 137.500 | B |
| 8a1ea92cc667fff | Novi Grad Sarajevo | Dobroševići | 28 | 3,850.200 | 137.500 | A |
| 8a1ea92ca0f7fff | Ilidža | Osjek | 11 | 1,513.000 | 137.500 | B |
| 8a1ea92cb5affff | Ilidža | Donji Doglodi | 14 | 1,926.100 | 137.600 | B |
| 8a1ea92c374ffff | Ilidža | Gladno polje | 17 | 2,339.800 | 137.600 | B |
| 8a1ef6960a27fff | Ilidža | Sokolović-kolonija | 39 | 5,368.900 | 137.700 | B |
| 8a1ef6964817fff | Ilidža | Kamenjača | 26 | 3,579.400 | 137.700 | B |
| 8a1ef6963d4ffff | Ilidža | Hrasnica | 14 | 1,927.800 | 137.700 | B |
| 8a1ea92cb357fff | Ilidža | Azići | 30 | 4,131.100 | 137.700 | B |
| 8a1ea92caab7fff | Ilidža | Bjelaće | 17 | 2,341.100 | 137.700 | B |
| 8a1ea92ca96ffff | Ilidža | Dolovi | 13 | 1,790.300 | 137.700 | B |
| 8a1ea92cb22ffff | Ilidža | Azići | 32 | 4,407.800 | 137.700 | B |
| 8a1ef696304ffff | Ilidža | Lasica | 12 | 1,653.100 | 137.800 | B |
| 8a1ea92cc74ffff | Novi Grad Sarajevo | Dobroševići | 21 | 2,893.500 | 137.800 | A |
| 8a1ef6963107fff | Ilidža | Hrasnica | 18 | 2,480.300 | 137.800 | B |
| 8a1ea92c8127fff | Novi Grad Sarajevo | Dobroševići | 47 | 6,477.200 | 137.800 | A |
| 8a1ea92ca397fff | Ilidža | Osjek | 28 | 3,858.900 | 137.800 | B |
| 8a1ef6961977fff | Ilidža | Butmir | 42 | 5,788.600 | 137.800 | B |
| 8a1ef6963147fff | Ilidža | Lasica | 28 | 3,859.100 | 137.800 | B |
| 8a1ea92cb607fff | Ilidža | Pejton | 41 | 5,651.300 | 137.800 | B |
| 8a1ea92c3d87fff | Ilidža | Rakovica | 12 | 1,654.300 | 137.900 | B |
| 8a1ef69606effff | Ilidža | Kovači (Ilidža) | 29 | 3,997.900 | 137.900 | B |
| 8a1ea92cb227fff | Ilidža | Azići | 20 | 2,757.200 | 137.900 | B |
| 8a1ef6960b47fff | Ilidža | Sokolović-kolonija | 44 | 6,066.000 | 137.900 | B |
| 8a1ef6965947fff | Ilidža | Naselje Bulevar | 30 | 4,136.200 | 137.900 | B |
| 8a1ea92ca287fff | Ilidža | Osjek | 27 | 3,722.700 | 137.900 | B |
| 8a1ea92cb4cffff | Ilidža | Otes | 21 | 2,895.900 | 137.900 | B |
| 8a1ef696491ffff | Ilidža | Kamenjača | 33 | 4,550.700 | 137.900 | B |
| 8a1ea92ce4cffff | Ilidža | Lipe | 25 | 3,449.600 | 138.000 | B |
| 8a1ef6965667fff | Ilidža | Butmir | 36 | 4,967.700 | 138.000 | B |
| 8a1ea92c3067fff | Ilidža | Gladno polje | 12 | 1,656.200 | 138.000 | B |
| 8a1ef4596497fff | Ilidža | Naselje Bulevar | 43 | 5,934.600 | 138.000 | B |
| 8a1ea92c88a7fff | Novi Grad Sarajevo | Dobroševići | 49 | 6,765.000 | 138.100 | A |
| 8a1ea92ca707fff | Ilidža | Osjek | 19 | 2,623.400 | 138.100 | B |
| 8a1ea92cc707fff | Novi Grad Sarajevo | Dobroševići | 14 | 1,933.200 | 138.100 | A |
| 8a1ea92cb39ffff | Ilidža | Azići | 19 | 2,624.000 | 138.100 | B |
| 8a1ef6961837fff | Ilidža | Butmir | 48 | 6,629.800 | 138.100 | B |
| 8a1ea92ddb37fff | Ilidža | Lipe | 16 | 2,210.400 | 138.100 | B |
| 8a1ea92cb847fff | Ilidža | Doglodi | 16 | 2,210.700 | 138.200 | B |
| 8a1ef6961887fff | Ilidža | Butmir | 42 | 5,804.100 | 138.200 | B |
| 8a1ea92cc357fff | Novi Grad Sarajevo | Dobroševići | 25 | 3,455.200 | 138.200 | A |
| 8a1ef458470ffff | Centar Sarajevo | Betanija | 15 | 2,073.300 | 138.200 | B |
| 8a1ea92c0607fff | Ilidža | Rakovica | 21 | 2,902.700 | 138.200 | B |
| 8a1ef6964877fff | Ilidža | Vreoca | 29 | 4,009.100 | 138.200 | B |
| 8a1ef696380ffff | Ilidža | Hrasnica | 19 | 2,626.800 | 138.300 | B |
| 8a1ea92dd86ffff | Ilidža | Lipe | 15 | 2,073.900 | 138.300 | B |
| 8a1ef696016ffff | Ilidža | Sokolović-kolonija | 12 | 1,659.200 | 138.300 | B |
| 8a1ef69600dffff | Ilidža | Kovači (Ilidža) | 20 | 2,766.200 | 138.300 | B |
| 8a1ea92ccc67fff | Novi Grad Sarajevo | Dobroševići | 13 | 1,798.100 | 138.300 | A |
| 8a1ef696018ffff | Ilidža | Stojčevac | 19 | 2,628.400 | 138.300 | B |
| 8a1ef6965657fff | Ilidža | Butmir | 38 | 5,258.000 | 138.400 | B |
| 8a1ef69658d7fff | Ilidža | Ilidža | 49 | 6,780.800 | 138.400 | B |
| 8a1ea92cc307fff | Novi Grad Sarajevo | Dobroševići | 18 | 2,491.300 | 138.400 | A |
| 8a1ea92d9b67fff | Ilidža | Blažuj | 13 | 1,799.400 | 138.400 | B |
| 8a1ea92cc71ffff | Novi Grad Sarajevo | Dobroševići | 18 | 2,491.500 | 138.400 | A |
| 8a1ef696561ffff | Ilidža | Butmir | 23 | 3,183.900 | 138.400 | B |
| 8a1ea92cb8affff | Ilidža | Doglodi | 25 | 3,460.900 | 138.400 | B |
| 8a1ea92cb857fff | Ilidža | Doglodi | 17 | 2,354.300 | 138.500 | B |
| 8a1ea92cc16ffff | Novi Grad Sarajevo | Dobroševići | 17 | 2,355.000 | 138.500 | A |
| 8a1ef4580d57fff | Centar Sarajevo | Pionirska Dolina | 48 | 6,650.300 | 138.500 | B |
| 8a1ea92cb6d7fff | Ilidža | Pejton | 46 | 6,373.400 | 138.600 | B |
| 8a1ea92c06affff | Ilidža | Rakovica | 23 | 3,187.400 | 138.600 | B |
| 8a1ef696585ffff | Ilidža | Naselje Bulevar | 53 | 7,346.000 | 138.600 | B |
| 8a1ef696316ffff | Ilidža | Lasica | 32 | 4,436.700 | 138.600 | B |
| 8a1ea92cc26ffff | Novi Grad Sarajevo | Dobroševići | 40 | 5,545.900 | 138.600 | A |
| 8a1ea92cdc8ffff | Novi Grad Sarajevo | Dobroševići | 20 | 2,774.200 | 138.700 | A |
| 8a1ea92cd45ffff | Novi Grad Sarajevo | Dobroševići | 48 | 6,658.200 | 138.700 | A |
| 8a1ea92ce4affff | Ilidža | Lipe | 11 | 1,526.100 | 138.700 | B |
| 8a1ea92ce8dffff | Ilidža | Lipe | 11 | 1,526.900 | 138.800 | B |
| 8a1ef6961a07fff | Ilidža | Donji Kotorac | 24 | 3,331.500 | 138.800 | B |
| 8a1ef4583297fff | Stari Grad Sarajevo | Mošćanica | 28 | 3,887.000 | 138.800 | A |
| 8a1ea92cca5ffff | Novi Grad Sarajevo | Dobroševići | 12 | 1,666.000 | 138.800 | A |
| 8a1ea92c078ffff | Ilidža | Rakovica | 20 | 2,777.000 | 138.800 | B |
| 8a1ef6963a97fff | Ilidža | Lasica | 24 | 3,333.200 | 138.900 | B |
| 8a1ea92ca237fff | Ilidža | Osjek | 25 | 3,472.300 | 138.900 | B |
| 8a1ea92ca547fff | Ilidža | Blažuj | 22 | 3,056.400 | 138.900 | B |
| 8a1ef6964837fff | Ilidža | Kamenjača | 35 | 4,863.100 | 138.900 | B |
| 8a1ea92ca307fff | Ilidža | Osjek | 25 | 3,474.000 | 139.000 | B |
| 8a1ea92cc78ffff | Novi Grad Sarajevo | Dobroševići | 24 | 3,335.900 | 139.000 | A |
| 8a1ef6965417fff | Ilidža | Lužani | 16 | 2,224.700 | 139.000 | B |
| 8a1ef69642effff | Ilidža | Lužani | 16 | 2,225.000 | 139.100 | B |
| 8a1ea92cad37fff | Ilidža | Lipe | 10 | 1,390.700 | 139.100 | B |
| 8a1ef6964d57fff | Ilidža | Plandište | 32 | 4,450.200 | 139.100 | B |
| 8a1ef6964917fff | Ilidža | Kamenjača | 32 | 4,450.600 | 139.100 | B |
| 8a1ea92ca72ffff | Ilidža | Osjek | 26 | 3,616.200 | 139.100 | B |
| 8a1ea92dda17fff | Ilidža | Lipe | 20 | 2,781.900 | 139.100 | B |
| 8a1ea92c32a7fff | Ilidža | Gladno polje | 25 | 3,478.400 | 139.100 | B |
| 8a1ef459d987fff | Stari Grad Sarajevo | Mošćanica | 10 | 1,391.500 | 139.100 | A |
| 8a1ef6963a87fff | Ilidža | Lasica | 26 | 3,618.500 | 139.200 | B |
| 8a1ef459261ffff | Ilidža | Donji Kotorac | 20 | 2,783.600 | 139.200 | B |
| 8a1ea92ca2e7fff | Ilidža | Osjek | 19 | 2,645.000 | 139.200 | B |
| 8a1ef6960a17fff | Ilidža | Sokolović-kolonija | 24 | 3,341.500 | 139.200 | B |
| 8a1ef696381ffff | Ilidža | Hrasnica | 32 | 4,456.900 | 139.300 | B |
| 8a1ef69648a7fff | Ilidža | Kamenjača | 29 | 4,040.700 | 139.300 | B |
| 8a1ef6961087fff | Ilidža | Butmir | 21 | 2,926.100 | 139.300 | B |
| 8a1ea92cbab7fff | Ilidža | Doglodi | 24 | 3,344.500 | 139.400 | B |
| 8a1ef6965857fff | Ilidža | Naselje Bulevar | 57 | 7,943.500 | 139.400 | B |
| 8a1ef6961d2ffff | Ilidža | Sokolović-kolonija | 20 | 2,787.500 | 139.400 | B |
| 8a1ef6965ac7fff | Ilidža | Naselje Bulevar | 51 | 7,109.200 | 139.400 | B |
| 8a1ef696185ffff | Ilidža | Donji Kotorac | 21 | 2,927.900 | 139.400 | B |
| 8a1ef4583b67fff | Stari Grad Sarajevo | Mošćanica | 13 | 1,812.700 | 139.400 | A |
| 8a1ea92cb8f7fff | Ilidža | Doglodi | 30 | 4,183.500 | 139.400 | B |
| 8a1ea92cb09ffff | Ilidža | Otes | 22 | 3,067.900 | 139.400 | B |
| 8a1ea92c3307fff | Ilidža | Gladno polje | 16 | 2,231.600 | 139.500 | B |
| 8a1ea92ca607fff | Ilidža | Osjek | 26 | 3,627.000 | 139.500 | B |
| 8a1ea92c0d9ffff | Ilidža | Kobiljača | 12 | 1,674.200 | 139.500 | B |
| 8a1ef696481ffff | Ilidža | Kamenjača | 28 | 3,906.500 | 139.500 | B |
| 8a1ef4581d9ffff | Stari Grad Sarajevo | Mošćanica | 10 | 1,395.600 | 139.600 | A |
| 8a1ea92cada7fff | Ilidža | Lipe | 20 | 2,791.700 | 139.600 | B |
| 8a1ea92cb84ffff | Ilidža | Doglodi | 15 | 2,094.400 | 139.600 | B |
| 8a1ef69658cffff | Ilidža | Naselje Bulevar | 49 | 6,843.900 | 139.700 | B |
| 8a1ef6961ab7fff | Ilidža | Donji Kotorac | 44 | 6,145.700 | 139.700 | B |
| 8a1ef6960647fff | Ilidža | Kovači (Ilidža) | 27 | 3,771.200 | 139.700 | B |
| 8a1ef4583417fff | Stari Grad Sarajevo | Kovači | 122 | 17,040.900 | 139.700 | A |
| 8a1ea92dd2dffff | Ilidža | Blažuj | 13 | 1,815.900 | 139.700 | B |
| 8a1ea92cb89ffff | Ilidža | Doglodi | 29 | 4,051.000 | 139.700 | B |
| 8a1ea92ca66ffff | Ilidža | Osjek | 30 | 4,191.800 | 139.700 | B |
| 8a1ea92ca477fff | Ilidža | Blažuj | 25 | 3,493.200 | 139.700 | B |
| 8a1ef696019ffff | Ilidža | Stojčevac | 16 | 2,235.700 | 139.700 | B |
| 8a1ef4583a0ffff | Stari Grad Sarajevo | Mošćanica | 24 | 3,353.600 | 139.700 | A |
| 8a1ef6965647fff | Ilidža | Butmir | 37 | 5,170.300 | 139.700 | B |
| 8a1ef45b2cd7fff | Novi Grad Sarajevo | Reljevo | 38 | 5,310.200 | 139.700 | A |
| 8a1ef6961967fff | Ilidža | Donji Kotorac | 25 | 3,493.600 | 139.700 | B |
| 8a1ea92ca29ffff | Ilidža | Osjek | 31 | 4,332.200 | 139.700 | B |
| 8a1ea92c0627fff | Ilidža | Rakovica | 23 | 3,214.300 | 139.800 | B |
| 8a1ef45841a7fff | Centar Sarajevo | Nahorevo | 51 | 7,129.200 | 139.800 | B |
| 8a1ea92cb767fff | Ilidža | Otes | 22 | 3,075.600 | 139.800 | B |
| 8a1ef6965897fff | Ilidža | Ilidža | 45 | 6,291.100 | 139.800 | B |
| 8a1ea92ca5b7fff | Ilidža | Blažuj | 18 | 2,516.700 | 139.800 | B |
| 8a1ea92c8d77fff | Novi Grad Sarajevo | Dobroševići | 24 | 3,356.900 | 139.900 | A |
| 8a1ef6965adffff | Ilidža | Naselje Bulevar | 56 | 7,833.800 | 139.900 | B |
| 8a1ea92c3327fff | Ilidža | Gladno polje | 11 | 1,539.000 | 139.900 | B |
| 8a1ea92cb12ffff | Ilidža | Doglodi | 22 | 3,079.100 | 140.000 | B |
| 8a1ea92c8d2ffff | Novi Grad Sarajevo | Dobroševići | 11 | 1,539.800 | 140.000 | A |
| 8a1ef6964967fff | Ilidža | Kamenjača | 22 | 3,079.800 | 140.000 | B |
| 8a1ea92ca577fff | Ilidža | Blažuj | 26 | 3,640.300 | 140.000 | B |
| 8a1ea92cc637fff | Novi Grad Sarajevo | Dobroševići | 18 | 2,520.300 | 140.000 | A |
| 8a1ef6963047fff | Ilidža | Lasica | 11 | 1,540.400 | 140.000 | B |
| 8a1ea92cc0f7fff | Novi Grad Sarajevo | Dobroševići | 28 | 3,922.100 | 140.100 | A |
| 8a1ef4580667fff | Stari Grad Sarajevo | Sedrenik | 11 | 1,541.200 | 140.100 | A |
| 8a1ef69648e7fff | Ilidža | Kamenjača | 35 | 4,903.900 | 140.100 | B |
| 8a1ef6965a9ffff | Ilidža | Naselje Bulevar | 41 | 5,744.700 | 140.100 | B |
| 8a1ea92c0097fff | Ilidža | Rakovica | 19 | 2,662.600 | 140.100 | B |
| 8a1ea92ca0e7fff | Ilidža | Osjek | 18 | 2,522.800 | 140.200 | B |
| 8a1ea92c898ffff | Novi Grad Sarajevo | Dobroševići | 59 | 8,269.500 | 140.200 | A |
| 8a1ef458306ffff | Stari Grad Sarajevo | Mošćanica | 28 | 3,924.700 | 140.200 | A |
| 8a1ef696576ffff | Ilidža | Butmir | 31 | 4,346.200 | 140.200 | B |
| 8a1ea92ca777fff | Ilidža | Osjek | 26 | 3,645.600 | 140.200 | B |
| 8a1ea92ce637fff | Ilidža | Lipe | 26 | 3,645.900 | 140.200 | B |
| 8a1ea92ca2f7fff | Ilidža | Osjek | 22 | 3,085.100 | 140.200 | B |
| 8a1ea92ca38ffff | Ilidža | Osjek | 23 | 3,225.500 | 140.200 | B |
| 8a1ea92cb7b7fff | Ilidža | Otes | 31 | 4,347.500 | 140.200 | B |
| 8a1ea92cd48ffff | Novi Grad Sarajevo | Dobroševići | 51 | 7,152.900 | 140.300 | A |
| 8a1ea92c85affff | Ilidža | Dolovi | 10 | 1,402.700 | 140.300 | B |
| 8a1ea92ca14ffff | Ilidža | Bjelaće | 21 | 2,945.900 | 140.300 | B |
| 8a1ef69619b7fff | Ilidža | Butmir | 42 | 5,892.200 | 140.300 | B |
| 8a1ea92cacd7fff | Ilidža | Blažuj | 22 | 3,086.900 | 140.300 | B |
| 8a1ef4583ab7fff | Stari Grad Sarajevo | Mošćanica | 23 | 3,227.900 | 140.300 | A |
| 8a1ef6963027fff | Ilidža | Hrasnica | 12 | 1,684.200 | 140.300 | B |
| 8a1ea92cb2effff | Ilidža | Azići | 53 | 7,438.800 | 140.400 | B |
| 8a1ef6965a17fff | Ilidža | Naselje Bulevar | 52 | 7,298.500 | 140.400 | B |
| 8a1ea92ccc77fff | Novi Grad Sarajevo | Dobroševići | 24 | 3,368.600 | 140.400 | A |
| 8a1ea92ca387fff | Ilidža | Osjek | 29 | 4,071.600 | 140.400 | B |
| 8a1ea92cabaffff | Ilidža | Dolovi | 21 | 2,948.500 | 140.400 | B |
| 8a1ea92cb81ffff | Ilidža | Doglodi | 23 | 3,229.900 | 140.400 | B |
| 8a1ea92cca9ffff | Novi Grad Sarajevo | Dobroševići | 19 | 2,668.300 | 140.400 | A |
| 8a1ef6965907fff | Ilidža | Azići | 44 | 6,181.500 | 140.500 | B |
| 8a1ea92cb75ffff | Ilidža | Otes | 31 | 4,355.200 | 140.500 | B |
| 8a1ea92caccffff | Ilidža | Blažuj | 19 | 2,670.500 | 140.600 | B |
| 8a1ef696574ffff | Ilidža | Butmir | 33 | 4,638.600 | 140.600 | B |
| 8a1ea92cb61ffff | Ilidža | Pejton | 50 | 7,028.900 | 140.600 | B |
| 8a1ea92c32f7fff | Ilidža | Gladno polje | 20 | 2,812.000 | 140.600 | B |
| 8a1ea92d9a2ffff | Ilidža | Blažuj | 12 | 1,687.200 | 140.600 | B |
| 8a1ea92cc2f7fff | Novi Grad Sarajevo | Dobroševići | 29 | 4,077.800 | 140.600 | A |
| 8a1ea92cbc07fff | Ilidža | Donji Doglodi | 10 | 1,406.200 | 140.600 | B |
| 8a1ef69638b7fff | Ilidža | Hrasnica | 32 | 4,500.200 | 140.600 | B |
| 8a1ef696061ffff | Ilidža | Kovači (Ilidža) | 33 | 4,642.000 | 140.700 | B |
| 8a1ea92cac07fff | Ilidža | Lipe | 20 | 2,813.500 | 140.700 | B |
| 8a1ef6960667fff | Ilidža | Kovači (Ilidža) | 28 | 3,939.300 | 140.700 | B |
| 8a1ea92cc677fff | Novi Grad Sarajevo | Dobroševići | 46 | 6,473.900 | 140.700 | A |
| 8a1ef459d16ffff | Stari Grad Sarajevo | Mošćanica | 10 | 1,407.400 | 140.700 | A |
| 8a1ea92ccb97fff | Novi Grad Sarajevo | Dobroševići | 10 | 1,407.400 | 140.700 | A |
| 8a1ef696498ffff | Ilidža | Kamenjača | 34 | 4,785.200 | 140.700 | B |
| 8a1ef69658effff | Ilidža | Naselje Bulevar | 55 | 7,741.200 | 140.700 | B |
| 8a1ef45828f7fff | Centar Sarajevo | Koševo II | 198 | 27,869.900 | 140.800 | B |
| 8a1ea92caa2ffff | Ilidža | Bjelaće | 12 | 1,689.600 | 140.800 | B |
| 8a1ef6963857fff | Ilidža | Hrasnica | 23 | 3,239.400 | 140.800 | B |
| 8a1ef696192ffff | Ilidža | Butmir | 44 | 6,197.300 | 140.800 | B |
| 8a1ea92ca677fff | Ilidža | Osjek | 34 | 4,789.000 | 140.900 | B |
| 8a1ef6961857fff | Ilidža | Donji Kotorac | 37 | 5,212.300 | 140.900 | B |
| 8a1ef696516ffff | Ilidža | Naselje Bulevar | 44 | 6,198.800 | 140.900 | B |
| 8a1ea92ca3b7fff | Ilidža | Osjek | 26 | 3,663.500 | 140.900 | B |
| 8a1ea92cc34ffff | Novi Grad Sarajevo | Dobroševići | 47 | 6,623.600 | 140.900 | A |
| 8a1ea92cb6a7fff | Ilidža | Pejton | 47 | 6,625.000 | 141.000 | B |
| 8a1ea92cbc77fff | Ilidža | Donji Doglodi | 14 | 1,973.600 | 141.000 | B |
| 8a1ef696482ffff | Ilidža | Kamenjača | 33 | 4,652.500 | 141.000 | B |
| 8a1ef696004ffff | Ilidža | Kovači (Ilidža) | 23 | 3,242.600 | 141.000 | B |
| 8a1ef6960a47fff | Ilidža | Sokolović-kolonija | 53 | 7,473.200 | 141.000 | B |
| 8a1ea92ca0dffff | Ilidža | Osjek | 28 | 3,948.200 | 141.000 | B |
| 8a1ea92cacf7fff | Ilidža | Blažuj | 18 | 2,539.200 | 141.100 | B |
| 8a1ea92c0657fff | Ilidža | Rakovica | 24 | 3,385.700 | 141.100 | B |
| 8a1ea92cb88ffff | Ilidža | Doglodi | 27 | 3,809.800 | 141.100 | B |
| 8a1ea92ca45ffff | Ilidža | Blažuj | 21 | 2,964.100 | 141.100 | B |
| 8a1ea92cbb9ffff | Ilidža | Doglodi | 31 | 4,375.600 | 141.100 | B |
| 8a1ef6961ae7fff | Ilidža | Donji Kotorac | 23 | 3,246.800 | 141.200 | B |
| 8a1ea92ce617fff | Ilidža | Lipe | 33 | 4,658.400 | 141.200 | B |
| 8a1ef6961067fff | Ilidža | Donji Kotorac | 34 | 4,799.800 | 141.200 | B |
| 8a1ea92c045ffff | Ilidža | Rakovica | 16 | 2,258.800 | 141.200 | B |
| 8a1ef45b174ffff | Centar Sarajevo | Betanija | 14 | 1,976.500 | 141.200 | B |
| 8a1ef4596627fff | Ilidža | Stupsko Brdo | 61 | 8,613.000 | 141.200 | B |
| 8a1ea92cb0effff | Ilidža | Otes | 27 | 3,812.500 | 141.200 | B |
| 8a1ea92c2b47fff | Ilidža | Rudnik | 11 | 1,553.300 | 141.200 | B |
| 8a1ef4596537fff | Ilidža | Stup | 58 | 8,190.800 | 141.200 | B |
| 8a1ef6964347fff | Ilidža | Lužani | 40 | 5,649.900 | 141.200 | B |
| 8a1ef696480ffff | Ilidža | Kamenjača | 30 | 4,238.100 | 141.300 | B |
| 8a1ef4583a97fff | Stari Grad Sarajevo | Mošćanica | 25 | 3,531.900 | 141.300 | A |
| 8a1ea92cb637fff | Ilidža | Otes | 47 | 6,641.500 | 141.300 | B |
| 8a1ef696495ffff | Ilidža | Kamenjača | 27 | 3,815.800 | 141.300 | B |
| 8a1ef6960ceffff | Ilidža | Stojčevac | 11 | 1,554.600 | 141.300 | B |
| 8a1ef69658c7fff | Ilidža | Ilidža | 58 | 8,197.500 | 141.300 | B |
| 8a1ea92cb0cffff | Ilidža | Otes | 27 | 3,816.200 | 141.300 | B |
| 8a1ef459678ffff | Ilidža | Stupsko Brdo | 68 | 9,613.700 | 141.400 | B |
| 8a1ea92ce29ffff | Ilidža | Dolovi | 11 | 1,555.500 | 141.400 | B |
| 8a1ea92c8c4ffff | Novi Grad Sarajevo | Dobroševići | 68 | 9,616.100 | 141.400 | A |
| 8a1ea92cb887fff | Ilidža | Doglodi | 31 | 4,383.900 | 141.400 | B |
| 8a1ea92ca82ffff | Ilidža | Dolovi | 16 | 2,262.700 | 141.400 | B |
| 8a1ef696191ffff | Ilidža | Butmir | 49 | 6,933.900 | 141.500 | B |
| 8a1ea92c56affff | Ilidža | Zenik | 10 | 1,415.200 | 141.500 | B |
| 8a1ea92c8ceffff | Novi Grad Sarajevo | Dobroševići | 18 | 2,548.700 | 141.600 | A |
| 8a1ef6965747fff | Ilidža | Butmir | 31 | 4,389.800 | 141.600 | B |
| 8a1ef6961c87fff | Ilidža | Sokolović-kolonija | 29 | 4,108.400 | 141.700 | B |
| 8a1ef6963167fff | Ilidža | Lasica | 43 | 6,092.300 | 141.700 | B |
| 8a1ef69618f7fff | Ilidža | Donji Kotorac | 23 | 3,258.800 | 141.700 | B |
| 8a1ea92cd3b7fff | Novi Grad Sarajevo | Reljevo | 14 | 1,984.500 | 141.700 | A |
| 8a1ea92ca2a7fff | Ilidža | Osjek | 26 | 3,685.600 | 141.800 | B |
| 8a1ea92dd91ffff | Ilidža | Gladno polje | 30 | 4,253.200 | 141.800 | B |
| 8a1ea92c3337fff | Ilidža | Gladno polje | 18 | 2,552.000 | 141.800 | B |
| 8a1ef6963a9ffff | Ilidža | Lasica | 33 | 4,678.800 | 141.800 | B |
| 8a1ea92c321ffff | Ilidža | Gladno polje | 22 | 3,119.400 | 141.800 | B |
| 8a1ef6965377fff | Ilidža | Naselje Bulevar | 54 | 7,657.000 | 141.800 | B |
| 8a1ea92cb25ffff | Ilidža | Azići | 53 | 7,516.400 | 141.800 | B |
| 8a1ea92cb087fff | Ilidža | Otes | 13 | 1,844.500 | 141.900 | B |
| 8a1ea92ca31ffff | Ilidža | Osjek | 25 | 3,548.100 | 141.900 | B |
| 8a1ea92dd16ffff | Ilidža | Lipe | 39 | 5,538.600 | 142.000 | B |
| 8a1ef6961b0ffff | Ilidža | Donji Kotorac | 32 | 4,545.900 | 142.100 | B |
| 8a1ef4580d27fff | Centar Sarajevo | Betanija | 36 | 5,114.200 | 142.100 | B |
| 8a1ea92cc397fff | Novi Grad Sarajevo | Dobroševići | 20 | 2,842.100 | 142.100 | A |
| 8a1ea92ce087fff | Ilidža | Lipe | 28 | 3,979.100 | 142.100 | B |
| 8a1ef69639b7fff | Ilidža | Hrasnica | 43 | 6,111.800 | 142.100 | B |
| 8a1ef696492ffff | Ilidža | Kamenjača | 28 | 3,979.900 | 142.100 | B |
| 8a1ea92cdc2ffff | Novi Grad Sarajevo | Dobroševići | 11 | 1,564.000 | 142.200 | A |
| 8a1ef6964807fff | Ilidža | Kamenjača | 39 | 5,545.100 | 142.200 | B |
| 8a1ef696532ffff | Ilidža | Naselje Bulevar | 58 | 8,247.100 | 142.200 | B |
| 8a1ea92ca70ffff | Ilidža | Osjek | 34 | 4,835.400 | 142.200 | B |
| 8a1ef6965167fff | Ilidža | Ilidža | 49 | 6,970.100 | 142.200 | B |
| 8a1ea92cc68ffff | Novi Grad Sarajevo | Dobroševići | 14 | 1,991.600 | 142.300 | A |
| 8a1ea92ca75ffff | Ilidža | Osjek | 36 | 5,122.200 | 142.300 | B |
| 8a1ea92c372ffff | Ilidža | Gladno polje | 13 | 1,850.000 | 142.300 | B |
| 8a1ea92cb91ffff | Ilidža | Doglodi | 29 | 4,127.300 | 142.300 | B |
| 8a1ef6965917fff | Ilidža | Pejton | 41 | 5,835.100 | 142.300 | B |
| 8a1ea92caa07fff | Ilidža | Bjelaće | 20 | 2,846.600 | 142.300 | B |
| 8a1ea92ca2affff | Ilidža | Osjek | 32 | 4,554.600 | 142.300 | B |
| 8a1ef6960b57fff | Ilidža | Sokolović-kolonija | 52 | 7,401.500 | 142.300 | B |
| 8a1ef696389ffff | Ilidža | Hrasnica | 29 | 4,128.300 | 142.400 | B |
| 8a1ef6960077fff | Ilidža | Kovači (Ilidža) | 23 | 3,275.700 | 142.400 | B |
| 8a1ea92d994ffff | Ilidža | Blažuj | 18 | 2,563.600 | 142.400 | B |
| 8a1ea92c848ffff | Ilidža | Dolovi | 11 | 1,567.600 | 142.500 | B |
| 8a1ef45b2c87fff | Novi Grad Sarajevo | Reljevo | 12 | 1,710.400 | 142.500 | A |
| 8a1ef6964c2ffff | Ilidža | Plandište | 26 | 3,706.100 | 142.500 | B |
| 8a1ef6960b4ffff | Ilidža | Sokolović-kolonija | 53 | 7,554.900 | 142.500 | B |
| 8a1ef4583b6ffff | Stari Grad Sarajevo | Mošćanica | 11 | 1,568.100 | 142.600 | A |
| 8a1ea92ca227fff | Ilidža | Osjek | 31 | 4,419.500 | 142.600 | B |
| 8a1ef696066ffff | Ilidža | Kovači (Ilidža) | 21 | 2,993.900 | 142.600 | B |
| 8a1ef69606cffff | Ilidža | Hrasnica | 39 | 5,560.500 | 142.600 | B |
| 8a1ea92ca297fff | Ilidža | Osjek | 36 | 5,133.200 | 142.600 | B |
| 8a1ef696562ffff | Ilidža | Butmir | 40 | 5,704.000 | 142.600 | B |
| 8a1ea92cb8d7fff | Ilidža | Doglodi | 28 | 3,993.700 | 142.600 | B |
| 8a1ef6965c97fff | Ilidža | Lužani | 44 | 6,276.400 | 142.600 | B |
| 8a1ea92c8c8ffff | Novi Grad Sarajevo | Dobroševići | 47 | 6,707.700 | 142.700 | A |
| 8a1ea92ca407fff | Ilidža | Blažuj | 42 | 5,994.200 | 142.700 | B |
| 8a1ea92c32dffff | Ilidža | Gladno polje | 17 | 2,426.600 | 142.700 | B |
| 8a1ea92ca837fff | Ilidža | Dolovi | 10 | 1,427.500 | 142.800 | B |
| 8a1ef696119ffff | Ilidža | Butmir | 26 | 3,711.700 | 142.800 | B |
| 8a1ef6965767fff | Ilidža | Butmir | 23 | 3,283.800 | 142.800 | B |
| 8a1ea92cc717fff | Novi Grad Sarajevo | Dobroševići | 24 | 3,426.600 | 142.800 | A |
| 8a1ea92c009ffff | Ilidža | Rakovica | 21 | 2,998.700 | 142.800 | B |
| 8a1ea92cb05ffff | Ilidža | Azići | 23 | 3,284.700 | 142.800 | B |
| 8a1ea92cacc7fff | Ilidža | Blažuj | 29 | 4,141.700 | 142.800 | B |
| 8a1ea92cb327fff | Ilidža | Azići | 31 | 4,428.400 | 142.900 | B |
| 8a1ef6960157fff | Ilidža | Kovači (Ilidža) | 22 | 3,143.500 | 142.900 | B |
| 8a1ef6960a4ffff | Ilidža | Sokolović-kolonija | 54 | 7,717.700 | 142.900 | B |
| 8a1ea92cabb7fff | Ilidža | Dolovi | 10 | 1,429.200 | 142.900 | B |
| 8a1ea92ca737fff | Ilidža | Blažuj | 16 | 2,286.800 | 142.900 | B |
| 8a1ea92c3047fff | Ilidža | Gladno polje | 14 | 2,001.400 | 143.000 | B |
| 8a1ea92dd25ffff | Ilidža | Blažuj | 17 | 2,430.500 | 143.000 | B |
| 8a1ef6961927fff | Ilidža | Butmir | 39 | 5,576.200 | 143.000 | B |
| 8a1ef696488ffff | Ilidža | Kamenjača | 21 | 3,003.200 | 143.000 | B |
| 8a1ef6965a87fff | Ilidža | Naselje Bulevar | 48 | 6,864.600 | 143.000 | B |
| 8a1ef4583b27fff | Stari Grad Sarajevo | Mošćanica | 16 | 2,288.300 | 143.000 | A |
| 8a1ea92c0b97fff | Ilidža | Rakovica | 10 | 1,430.200 | 143.000 | B |
| 8a1ea92cb76ffff | Ilidža | Otes | 27 | 3,862.100 | 143.000 | B |
| 8a1ea92cc14ffff | Novi Grad Sarajevo | Dobroševići | 12 | 1,716.500 | 143.000 | A |
| 8a1ea92caae7fff | Ilidža | Bjelaće | 18 | 2,575.800 | 143.100 | B |
| 8a1ea92ccc2ffff | Novi Grad Sarajevo | Dobroševići | 17 | 2,433.000 | 143.100 | A |
| 8a1ef6960a87fff | Ilidža | Sokolović-kolonija | 39 | 5,582.000 | 143.100 | B |
| 8a1ef6960a67fff | Ilidža | Sokolović-kolonija | 56 | 8,016.300 | 143.100 | B |
| 8a1ef6961937fff | Ilidža | Butmir | 50 | 7,158.800 | 143.200 | B |
| 8a1ea92cb477fff | Ilidža | Otes | 24 | 3,436.600 | 143.200 | B |
| 8a1ea92cb72ffff | Ilidža | Otes | 23 | 3,293.900 | 143.200 | B |
| 8a1ef6960737fff | Ilidža | Kovači (Ilidža) | 13 | 1,861.900 | 143.200 | B |
| 8a1ea92cc737fff | Novi Grad Sarajevo | Dobroševići | 11 | 1,576.100 | 143.300 | A |
| 8a1ef6965607fff | Ilidža | Butmir | 40 | 5,731.300 | 143.300 | B |
| 8a1ef69652d7fff | Ilidža | Butmir | 36 | 5,158.500 | 143.300 | B |
| 8a1ea92ce737fff | Ilidža | Lipe | 23 | 3,295.900 | 143.300 | B |
| 8a1ea92c054ffff | Ilidža | Rakovica | 13 | 1,862.900 | 143.300 | B |
| 8a1ea92cab37fff | Ilidža | Dolovi | 27 | 3,869.700 | 143.300 | B |
| 8a1ef458339ffff | Stari Grad Sarajevo | Mošćanica | 26 | 3,726.500 | 143.300 | A |
| 8a1ea92c07affff | Ilidža | Rakovica | 21 | 3,009.900 | 143.300 | B |
| 8a1ea92ca04ffff | Ilidža | Osjek | 33 | 4,730.100 | 143.300 | B |
| 8a1ef6964a87fff | Ilidža | Vreoca | 24 | 3,440.100 | 143.300 | B |
| 8a1ea92ca64ffff | Ilidža | Kamenjača | 40 | 5,734.100 | 143.400 | B |
| 8a1ea92cb8dffff | Ilidža | Doglodi | 33 | 4,730.900 | 143.400 | B |
| 8a1ea92c316ffff | Ilidža | Gladno polje | 13 | 1,863.900 | 143.400 | B |
| 8a1ea92ce707fff | Ilidža | Lipe | 16 | 2,294.700 | 143.400 | B |
| 8a1ea92ce4d7fff | Ilidža | Lipe | 27 | 3,873.300 | 143.500 | B |
| 8a1ea92ddae7fff | Ilidža | Lipe | 43 | 6,170.500 | 143.500 | B |
| 8a1ef69652a7fff | Ilidža | Butmir | 32 | 4,594.900 | 143.600 | B |
| 8a1ea92cbc67fff | Ilidža | Doglodi | 28 | 4,020.700 | 143.600 | B |
| 8a1ea92ca54ffff | Ilidža | Blažuj | 26 | 3,733.900 | 143.600 | B |
| 8a1ea92ca80ffff | Ilidža | Dolovi | 12 | 1,723.500 | 143.600 | B |
| 8a1ea92cb417fff | Ilidža | Otes | 24 | 3,447.600 | 143.700 | B |
| 8a1ea92cb727fff | Ilidža | Otes | 30 | 4,310.000 | 143.700 | B |
| 8a1ea92cb167fff | Ilidža | Doglodi | 33 | 4,741.500 | 143.700 | B |
| 8a1ef69600e7fff | Ilidža | Kovači (Ilidža) | 16 | 2,299.100 | 143.700 | B |
| 8a1ef6960a5ffff | Ilidža | Sokolović-kolonija | 57 | 8,192.400 | 143.700 | B |
| 8a1ef6964ba7fff | Ilidža | Vreoca | 42 | 6,037.000 | 143.700 | B |
| 8a1ef696486ffff | Ilidža | Vreoca | 21 | 3,018.800 | 143.800 | B |
| 8a1ea92ce607fff | Ilidža | Lipe | 21 | 3,019.200 | 143.800 | B |
| 8a1ef696009ffff | Ilidža | Kovači (Ilidža) | 13 | 1,869.100 | 143.800 | B |
| 8a1ef69606dffff | Ilidža | Hrasnica | 29 | 4,169.700 | 143.800 | B |
| 8a1ef69606e7fff | Ilidža | Kovači (Ilidža) | 31 | 4,458.100 | 143.800 | B |
| 8a1ef6965baffff | Ilidža | Naselje Bulevar | 64 | 9,204.700 | 143.800 | B |
| 8a1ef69650effff | Ilidža | Butmir | 16 | 2,301.700 | 143.900 | B |
| 8a1ea92cb897fff | Ilidža | Doglodi | 27 | 3,884.300 | 143.900 | B |
| 8a1ea92ca377fff | Ilidža | Bjelaće | 30 | 4,316.900 | 143.900 | B |
| 8a1ef6960777fff | Ilidža | Kovači (Ilidža) | 27 | 3,886.000 | 143.900 | B |
| 8a1ef6960187fff | Ilidža | Stojčevac | 21 | 3,022.900 | 143.900 | B |
| 8a1ef6963d77fff | Ilidža | Hrasnica | 20 | 2,879.500 | 144.000 | B |
| 8a1ef69652b7fff | Ilidža | Butmir | 40 | 5,759.500 | 144.000 | B |
| 8a1ef6960b5ffff | Ilidža | Sokolović-kolonija | 61 | 8,783.300 | 144.000 | B |
| 8a1ea92cab8ffff | Ilidža | Bjelaće | 19 | 2,735.900 | 144.000 | B |
| 8a1ef6965687fff | Ilidža | Sokolović-kolonija | 26 | 3,744.100 | 144.000 | B |
| 8a1ef69601a7fff | Ilidža | Stojčevac | 16 | 2,305.500 | 144.100 | B |
| 8a1ef696529ffff | Ilidža | Butmir | 46 | 6,629.400 | 144.100 | B |
| 8a1ea92d925ffff | Ilidža | Vrelo Bosne | 13 | 1,874.100 | 144.200 | B |
| 8a1ef696530ffff | Ilidža | Naselje Bulevar | 39 | 5,623.400 | 144.200 | B |
| 8a1ef45868c7fff | Centar Sarajevo | Betanija | 25 | 3,605.700 | 144.200 | B |
| 8a1ea92ca047fff | Ilidža | Osjek | 24 | 3,464.900 | 144.400 | B |
| 8a1ef6961da7fff | Ilidža | Sokolović-kolonija | 52 | 7,509.400 | 144.400 | B |
| 8a1ef6965b97fff | Ilidža | Naselje Bulevar | 61 | 8,811.000 | 144.400 | B |
| 8a1ef6960327fff | Ilidža | Sokolović-kolonija | 30 | 4,333.700 | 144.500 | B |
| 8a1ea92c864ffff | Ilidža | Doglodi | 27 | 3,901.200 | 144.500 | B |
| 8a1ea92cbadffff | Ilidža | Azići | 29 | 4,190.400 | 144.500 | B |
| 8a1ef6960aa7fff | Ilidža | Sokolović-kolonija | 37 | 5,346.700 | 144.500 | B |
| 8a1ea92caac7fff | Ilidža | Bjelaće | 30 | 4,335.200 | 144.500 | B |
| 8a1ea92cb06ffff | Ilidža | Doglodi | 42 | 6,070.700 | 144.500 | B |
| 8a1ea92cb0c7fff | Ilidža | Doglodi | 23 | 3,325.400 | 144.600 | B |
| 8a1ea92cb917fff | Ilidža | Doglodi | 38 | 5,495.000 | 144.600 | B |
| 8a1ef6960717fff | Ilidža | Kovači (Ilidža) | 15 | 2,169.100 | 144.600 | B |
| 8a1ea92ca32ffff | Ilidža | Bjelaće | 31 | 4,483.600 | 144.600 | B |
| 8a1ef69606f7fff | Ilidža | Kovači (Ilidža) | 33 | 4,773.000 | 144.600 | B |
| 8a1ef6961987fff | Ilidža | Butmir | 56 | 8,100.200 | 144.600 | B |
| 8a1ef6964937fff | Ilidža | Kamenjača | 44 | 6,365.300 | 144.700 | B |
| 8a1ea92cb127fff | Ilidža | Doglodi | 31 | 4,484.700 | 144.700 | B |
| 8a1ef6964bb7fff | Ilidža | Vreoca | 42 | 6,076.200 | 144.700 | B |
| 8a1ea92c3767fff | Ilidža | Gladno polje | 31 | 4,486.700 | 144.700 | B |
| 8a1ef696118ffff | Ilidža | Butmir | 40 | 5,789.900 | 144.700 | B |
| 8a1ea92cb8cffff | Ilidža | Doglodi | 31 | 4,488.800 | 144.800 | B |
| 8a1ea92cb627fff | Ilidža | Otes | 42 | 6,082.100 | 144.800 | B |
| 8a1ef696062ffff | Ilidža | Kovači (Ilidža) | 37 | 5,358.200 | 144.800 | B |
| 8a1ea92ca567fff | Ilidža | Blažuj | 29 | 4,199.700 | 144.800 | B |
| 8a1ea92c002ffff | Ilidža | Rakovica | 10 | 1,448.200 | 144.800 | B |
| 8a1ef6964c8ffff | Ilidža | Vrelo Bosne | 11 | 1,593.300 | 144.800 | B |
| 8a1ef6961907fff | Ilidža | Butmir | 51 | 7,389.800 | 144.900 | B |
| 8a1ea92ca367fff | Ilidža | Bjelaće | 23 | 3,332.800 | 144.900 | B |
| 8a1ea92cb177fff | Ilidža | Doglodi | 33 | 4,782.400 | 144.900 | B |
| 8a1ef6963067fff | Ilidža | Lasica | 26 | 3,768.600 | 144.900 | B |
| 8a1ea92ca76ffff | Ilidža | Osjek | 35 | 5,073.600 | 145.000 | B |
| 8a1ef6961a97fff | Ilidža | Donji Kotorac | 51 | 7,393.400 | 145.000 | B |
| 8a1ea92cb41ffff | Ilidža | Otes | 32 | 4,639.100 | 145.000 | B |
| 8a1ea92cb9b7fff | Ilidža | Doglodi | 30 | 4,350.500 | 145.000 | B |
| 8a1ea92cb96ffff | Ilidža | Doglodi | 33 | 4,785.600 | 145.000 | B |
| 8a1ef6964897fff | Ilidža | Plandište | 24 | 3,481.100 | 145.000 | B |
| 8a1ea92c8587fff | Ilidža | Dolovi | 21 | 3,046.500 | 145.100 | B |
| 8a1ef6961daffff | Ilidža | Sokolović-kolonija | 52 | 7,547.400 | 145.100 | B |
| 8a1ef6964827fff | Ilidža | Kamenjača | 47 | 6,821.700 | 145.100 | B |
| 8a1ef696420ffff | Ilidža | Lužani | 20 | 2,903.200 | 145.200 | B |
| 8a1ea92cb8b7fff | Ilidža | Doglodi | 31 | 4,500.300 | 145.200 | B |
| 8a1ea92ccd07fff | Novi Grad Sarajevo | Dobroševići | 12 | 1,742.700 | 145.200 | A |
| 8a1ea92c865ffff | Ilidža | Doglodi | 23 | 3,340.200 | 145.200 | B |
| 8a1ef6960087fff | Ilidža | Kovači (Ilidža) | 21 | 3,050.000 | 145.200 | B |
| 8a1ef69654d7fff | Ilidža | Sokolović-kolonija | 39 | 5,664.400 | 145.200 | B |
| 8a1ef6963bb7fff | Ilidža | Lasica | 38 | 5,520.700 | 145.300 | B |
| 8a1ef696535ffff | Ilidža | Stupsko Brdo | 11 | 1,598.100 | 145.300 | B |
| 8a1ea92c3707fff | Ilidža | Gladno polje | 18 | 2,615.200 | 145.300 | B |
| 8a1ea92cbb87fff | Ilidža | Doglodi | 35 | 5,085.400 | 145.300 | B |
| 8a1ef69638f7fff | Ilidža | Hrasnica | 49 | 7,119.600 | 145.300 | B |
| 8a1ef6963997fff | Ilidža | Hrasnica | 41 | 5,957.600 | 145.300 | B |
| 8a1ef6960aeffff | Ilidža | Sokolović-kolonija | 57 | 8,283.600 | 145.300 | B |
| 8a1ea92ca057fff | Ilidža | Osjek | 32 | 4,651.400 | 145.400 | B |
| 8a1ef6964857fff | Ilidža | Vreoca | 41 | 5,960.100 | 145.400 | B |
| 8a1ef69618c7fff | Ilidža | Donji Kotorac | 44 | 6,398.500 | 145.400 | B |
| 8a1ea92cbd67fff | Ilidža | Doglodi | 27 | 3,926.400 | 145.400 | B |
| 8a1ea92cacdffff | Ilidža | Blažuj | 30 | 4,364.900 | 145.500 | B |
| 8a1ef6963807fff | Ilidža | Hrasnica | 25 | 3,638.100 | 145.500 | B |
| 8a1ea92ca20ffff | Ilidža | Osjek | 35 | 5,094.400 | 145.600 | B |
| 8a1ea92ca257fff | Ilidža | Osjek | 21 | 3,056.900 | 145.600 | B |
| 8a1ea92ce177fff | Ilidža | Lipe | 16 | 2,329.700 | 145.600 | B |
| 8a1ea92caa27fff | Ilidža | Bjelaće | 28 | 4,077.300 | 145.600 | B |
| 8a1ef696434ffff | Ilidža | Lužani | 57 | 8,300.200 | 145.600 | B |
| 8a1ea92ce60ffff | Ilidža | Lipe | 12 | 1,747.900 | 145.700 | B |
| 8a1ef696199ffff | Ilidža | Butmir | 64 | 9,322.900 | 145.700 | B |
| 8a1ef6961d87fff | Ilidža | Sokolović-kolonija | 48 | 6,992.800 | 145.700 | B |
| 8a1ea92ce78ffff | Ilidža | Lipe | 32 | 4,662.000 | 145.700 | B |
| 8a1ea92c3727fff | Ilidža | Gladno polje | 15 | 2,185.400 | 145.700 | B |
| 8a1ea92ca207fff | Ilidža | Osjek | 34 | 4,954.400 | 145.700 | B |
| 8a1ea92c376ffff | Ilidža | Gladno polje | 34 | 4,955.200 | 145.700 | B |
| 8a1ea92cb997fff | Ilidža | Doglodi | 33 | 4,810.000 | 145.800 | B |
| 8a1ea92c0087fff | Ilidža | Rakovica | 35 | 5,101.700 | 145.800 | B |
| 8a1ea92ca947fff | Ilidža | Dolovi | 23 | 3,353.000 | 145.800 | B |
| 8a1ef69618b7fff | Ilidža | Butmir | 56 | 8,163.900 | 145.800 | B |
| 8a1ef696499ffff | Ilidža | Kamenjača | 47 | 6,854.500 | 145.800 | B |
| 8a1ef6964c9ffff | Ilidža | Vrelo Bosne | 15 | 2,188.100 | 145.900 | B |
| 8a1ef69618dffff | Ilidža | Donji Kotorac | 54 | 7,877.700 | 145.900 | B |
| 8a1ef696065ffff | Ilidža | Kovači (Ilidža) | 37 | 5,398.500 | 145.900 | B |
| 8a1ef69600f7fff | Ilidža | Kovači (Ilidža) | 26 | 3,794.000 | 145.900 | B |
| 8a1ef696071ffff | Ilidža | Kovači (Ilidža) | 28 | 4,087.200 | 146.000 | B |
| 8a1ef696006ffff | Ilidža | Sokolović-kolonija | 41 | 5,985.100 | 146.000 | B |
| 8a1ef696108ffff | Ilidža | Butmir | 27 | 3,942.100 | 146.000 | B |
| 8a1ea92cb8c7fff | Ilidža | Doglodi | 38 | 5,548.900 | 146.000 | B |
| 8a1ef6960017fff | Ilidža | Kovači (Ilidža) | 24 | 3,506.500 | 146.100 | B |
| 8a1ef6963d6ffff | Ilidža | Hrasnica | 40 | 5,846.300 | 146.200 | B |
| 8a1ef6963177fff | Ilidža | Hrasnica | 47 | 6,869.500 | 146.200 | B |
| 8a1ef69600d7fff | Ilidža | Kovači (Ilidža) | 25 | 3,654.100 | 146.200 | B |
| 8a1ea92caa87fff | Ilidža | Bjelaće | 32 | 4,677.400 | 146.200 | B |
| 8a1ef6964ac7fff | Ilidža | Lužani | 40 | 5,847.400 | 146.200 | B |
| 8a1ea92cb297fff | Ilidža | Azići | 50 | 7,309.800 | 146.200 | B |
| 8a1ef696506ffff | Ilidža | Ilidža | 22 | 3,217.100 | 146.200 | B |
| 8a1ef696001ffff | Ilidža | Kovači (Ilidža) | 26 | 3,802.500 | 146.200 | B |
| 8a1ea92ca0b7fff | Ilidža | Blažuj | 33 | 4,826.800 | 146.300 | B |
| 8a1ea92c3c57fff | Ilidža | Rakovica | 26 | 3,803.600 | 146.300 | B |
| 8a1ef69610a7fff | Ilidža | Butmir | 36 | 5,267.700 | 146.300 | B |
| 8a1ea92ca417fff | Ilidža | Blažuj | 40 | 5,853.600 | 146.300 | B |
| 8a1ef69649b7fff | Ilidža | Kamenjača | 28 | 4,098.400 | 146.400 | B |
| 8a1ef6963337fff | Ilidža | Lasica | 35 | 5,123.100 | 146.400 | B |
| 8a1ef696000ffff | Ilidža | Kovači (Ilidža) | 26 | 3,806.100 | 146.400 | B |
| 8a1ea92ca757fff | Ilidža | Osjek | 43 | 6,295.800 | 146.400 | B |
| 8a1ef6965ad7fff | Ilidža | Naselje Bulevar | 75 | 10,982.300 | 146.400 | B |
| 8a1ea92c175ffff | Ilidža | Gladno polje | 13 | 1,904.300 | 146.500 | B |
| 8a1ef696034ffff | Ilidža | Sokolović-kolonija | 53 | 7,765.400 | 146.500 | B |
| 8a1ea92ca62ffff | Ilidža | Osjek | 45 | 6,593.700 | 146.500 | B |
| 8a1ef6964977fff | Ilidža | Kamenjača | 41 | 6,007.700 | 146.500 | B |
| 8a1ea92cb377fff | Ilidža | Azići | 47 | 6,888.500 | 146.600 | B |
| 8a1ea92ca84ffff | Ilidža | Dolovi | 31 | 4,544.700 | 146.600 | B |
| 8a1ef69638cffff | Ilidža | Hrasnica | 54 | 7,917.000 | 146.600 | B |
| 8a1ef69638a7fff | Ilidža | Hrasnica | 52 | 7,624.000 | 146.600 | B |
| 8a1ea92ca15ffff | Ilidža | Bjelaće | 18 | 2,639.400 | 146.600 | B |
| 8a1ea92cb8effff | Ilidža | Doglodi | 35 | 5,132.400 | 146.600 | B |
| 8a1ea92cb95ffff | Ilidža | Doglodi | 29 | 4,255.300 | 146.700 | B |
| 8a1ea92c00b7fff | Ilidža | Rakovica | 22 | 3,228.300 | 146.700 | B |
| 8a1ef6964847fff | Ilidža | Vreoca | 37 | 5,431.500 | 146.800 | B |
| 8a1ef6965697fff | Ilidža | Sokolović-kolonija | 70 | 10,279.800 | 146.900 | B |
| 8a1ef696060ffff | Ilidža | Kovači (Ilidža) | 42 | 6,167.900 | 146.900 | B |
| 8a1ef6963897fff | Ilidža | Hrasnica | 24 | 3,524.500 | 146.900 | B |
| 8a1ef69610affff | Ilidža | Butmir | 31 | 4,552.700 | 146.900 | B |
| 8a1ea92ca097fff | Ilidža | Blažuj | 31 | 4,552.900 | 146.900 | B |
| 8a1ea92caaeffff | Ilidža | Bjelaće | 25 | 3,671.900 | 146.900 | B |
| 8a1ea92cb9a7fff | Ilidža | Doglodi | 44 | 6,462.700 | 146.900 | B |
| 8a1ea92cb837fff | Ilidža | Doglodi | 32 | 4,700.300 | 146.900 | B |
| 8a1ef6961db7fff | Ilidža | Sokolović-kolonija | 59 | 8,666.700 | 146.900 | B |
| 8a1ea92ca86ffff | Ilidža | Dolovi | 31 | 4,554.500 | 146.900 | B |
| 8a1ea92ca28ffff | Ilidža | Osjek | 50 | 7,347.600 | 147.000 | B |
| 8a1ef4592c9ffff | Ilidža | Stupsko Brdo | 42 | 6,172.500 | 147.000 | B |
| 8a1ea92ca217fff | Ilidža | Osjek | 42 | 6,173.100 | 147.000 | B |
| 8a1ef6960a97fff | Ilidža | Sokolović-kolonija | 44 | 6,470.100 | 147.000 | B |
| 8a1ef69606c7fff | Ilidža | Kovači (Ilidža) | 42 | 6,176.900 | 147.100 | B |
| 8a1ea92c86cffff | Ilidža | Doglodi | 39 | 5,736.600 | 147.100 | B |
| 8a1ea92cbd2ffff | Ilidža | Doglodi | 20 | 2,941.900 | 147.100 | B |
| 8a1ef6964d17fff | Ilidža | Plandište | 41 | 6,033.800 | 147.200 | B |
| 8a1ea92cb437fff | Ilidža | Otes | 37 | 5,445.200 | 147.200 | B |
| 8a1ea92ce4b7fff | Ilidža | Gladno polje | 13 | 1,913.200 | 147.200 | B |
| 8a1ef6961d4ffff | Ilidža | Butmir | 61 | 8,979.300 | 147.200 | B |
| 8a1ea92cb817fff | Ilidža | Doglodi | 39 | 5,742.600 | 147.200 | B |
| 8a1ef6961d6ffff | Ilidža | Butmir | 58 | 8,540.700 | 147.300 | B |
| 8a1ef696015ffff | Ilidža | Kovači (Ilidža) | 37 | 5,449.700 | 147.300 | B |
| 8a1ef696035ffff | Ilidža | Sokolović-kolonija | 31 | 4,566.100 | 147.300 | B |
| 8a1ea92ccd2ffff | Novi Grad Sarajevo | Dobroševići | 11 | 1,620.300 | 147.300 | A |
| 8a1ef4596c9ffff | Ilidža | Azići | 70 | 10,311.300 | 147.300 | B |
| 8a1ef6961c97fff | Ilidža | Sokolović-kolonija | 50 | 7,366.200 | 147.300 | B |
| 8a1ea92cb427fff | Ilidža | Otes | 28 | 4,125.100 | 147.300 | B |
| 8a1ef6963987fff | Ilidža | Hrasnica | 52 | 7,661.200 | 147.300 | B |
| 8a1ea92c15affff | Ilidža | Kakrinje | 12 | 1,768.100 | 147.300 | B |
| 8a1ef69600affff | Ilidža | Kovači (Ilidža) | 25 | 3,683.600 | 147.300 | B |
| 8a1ef6960607fff | Ilidža | Kovači (Ilidža) | 37 | 5,452.600 | 147.400 | B |
| 8a1ea92ca3affff | Ilidža | Osjek | 45 | 6,631.800 | 147.400 | B |
| 8a1ea92c8597fff | Ilidža | Dolovi | 26 | 3,831.700 | 147.400 | B |
| 8a1ea92ca30ffff | Ilidža | Osjek | 35 | 5,158.300 | 147.400 | B |
| 8a1ef696388ffff | Ilidža | Hrasnica | 53 | 7,812.700 | 147.400 | B |
| 8a1ea92cb217fff | Ilidža | Azići | 38 | 5,603.000 | 147.400 | B |
| 8a1ef6965297fff | Ilidža | Butmir | 58 | 8,553.200 | 147.500 | B |
| 8a1ef6960a57fff | Ilidža | Sokolović-kolonija | 69 | 10,179.400 | 147.500 | B |
| 8a1ef6964d5ffff | Ilidža | Plandište | 37 | 5,460.300 | 147.600 | B |
| 8a1ef6965d27fff | Ilidža | Pejton | 92 | 13,577.300 | 147.600 | B |
| 8a1ef6960677fff | Ilidža | Kovači (Ilidža) | 50 | 7,379.700 | 147.600 | B |
| 8a1ef6960a9ffff | Ilidža | Sokolović-kolonija | 55 | 8,118.200 | 147.600 | B |
| 8a1ea92cb3b7fff | Ilidža | Azići | 43 | 6,347.500 | 147.600 | B |
| 8a1ef6964c07fff | Ilidža | Plandište | 37 | 5,462.800 | 147.600 | B |
| 8a1ea92cbd47fff | Ilidža | Doglodi | 30 | 4,430.100 | 147.700 | B |
| 8a1ea92c62b7fff | Ilidža | Rudnik | 10 | 1,476.900 | 147.700 | B |
| 8a1ef6963887fff | Ilidža | Hrasnica | 46 | 6,793.900 | 147.700 | B |
| 8a1ea92cb40ffff | Ilidža | Otes | 36 | 5,317.300 | 147.700 | B |
| 8a1ef6964907fff | Ilidža | Kamenjača | 45 | 6,647.700 | 147.700 | B |
| 8a1ea92ca39ffff | Ilidža | Osjek | 40 | 5,909.500 | 147.700 | B |
| 8a1ea92cbc6ffff | Ilidža | Doglodi | 33 | 4,875.900 | 147.800 | B |
| 8a1ef6961c1ffff | Ilidža | Sokolović-kolonija | 56 | 8,275.600 | 147.800 | B |
| 8a1ef6964d0ffff | Ilidža | Plandište | 49 | 7,241.200 | 147.800 | B |
| 8a1ef6963127fff | Ilidža | Hrasnica | 42 | 6,207.200 | 147.800 | B |
| 8a1ef69642e7fff | Ilidža | Lužani | 35 | 5,173.500 | 147.800 | B |
| 8a1ef6961caffff | Ilidža | Sokolović-kolonija | 50 | 7,391.000 | 147.800 | B |
| 8a1ef6964947fff | Ilidža | Kamenjača | 36 | 5,322.100 | 147.800 | B |
| 8a1ef69638affff | Ilidža | Hrasnica | 50 | 7,391.900 | 147.800 | B |
| 8a1ef6961897fff | Ilidža | Butmir | 69 | 10,201.900 | 147.900 | B |
| 8a1ef69638dffff | Ilidža | Hrasnica | 49 | 7,245.700 | 147.900 | B |
| 8a1ea92c32cffff | Ilidža | Gladno polje | 16 | 2,366.400 | 147.900 | B |
| 8a1ef696312ffff | Ilidža | Hrasnica | 42 | 6,212.400 | 147.900 | B |
| 8a1ea92c3877fff | Ilidža | Kakrinje | 10 | 1,479.200 | 147.900 | B |
| 8a1ea92cb407fff | Ilidža | Otes | 44 | 6,508.900 | 147.900 | B |
| 8a1ea92cb71ffff | Ilidža | Otes | 52 | 7,692.500 | 147.900 | B |
| 8a1ea92ca56ffff | Ilidža | Blažuj | 35 | 5,177.900 | 147.900 | B |
| 8a1ea92cb51ffff | Ilidža | Donji Doglodi | 33 | 4,883.300 | 148.000 | B |
| 8a1ef696569ffff | Ilidža | Sokolović-kolonija | 75 | 11,101.000 | 148.000 | B |
| 8a1ea92ca0affff | Ilidža | Osjek | 10 | 1,480.500 | 148.000 | B |
| 8a1ef6964957fff | Ilidža | Kamenjača | 56 | 8,292.100 | 148.100 | B |
| 8a1ef696002ffff | Ilidža | Kovači (Ilidža) | 40 | 5,923.300 | 148.100 | B |
| 8a1ea92dd287fff | Ilidža | Blažuj | 13 | 1,925.200 | 148.100 | B |
| 8a1ef6964247fff | Ilidža | Lužani | 54 | 7,998.400 | 148.100 | B |
| 8a1ea92cab27fff | Ilidža | Dolovi | 22 | 3,259.000 | 148.100 | B |
| 8a1ea92caacffff | Ilidža | Bjelaće | 40 | 5,926.000 | 148.200 | B |
| 8a1ef69654effff | Ilidža | Sokolović-kolonija | 46 | 6,815.100 | 148.200 | B |
| 8a1ef696310ffff | Ilidža | Hrasnica | 35 | 5,186.700 | 148.200 | B |
| 8a1ef6964af7fff | Ilidža | Vreoca | 59 | 8,745.300 | 148.200 | B |
| 8a1ef6961ad7fff | Ilidža | Donji Kotorac | 27 | 4,004.700 | 148.300 | B |
| 8a1ea92caa97fff | Ilidža | Bjelaće | 37 | 5,488.600 | 148.300 | B |
| 8a1ef6961d9ffff | Ilidža | Sokolović-kolonija | 64 | 9,497.400 | 148.400 | B |
| 8a1ef6961c6ffff | Ilidža | Butmir | 60 | 8,904.000 | 148.400 | B |
| 8a1ef6963d67fff | Ilidža | Hrasnica | 46 | 6,827.500 | 148.400 | B |
| 8a1ea92c00cffff | Ilidža | Rakovica | 19 | 2,820.300 | 148.400 | B |
| 8a1ef6963817fff | Ilidža | Hrasnica | 59 | 8,763.000 | 148.500 | B |
| 8a1ef6961c37fff | Ilidža | Sokolović-kolonija | 70 | 10,398.500 | 148.500 | B |
| 8a1ef6961c17fff | Ilidža | Sokolović-kolonija | 69 | 10,251.200 | 148.600 | B |
| 8a1ef696014ffff | Ilidža | Sokolović-kolonija | 56 | 8,321.000 | 148.600 | B |
| 8a1ea92cebaffff | Ilidža | Dolovi | 10 | 1,486.000 | 148.600 | B |
| 8a1ef6960707fff | Ilidža | Kovači (Ilidža) | 40 | 5,949.600 | 148.700 | B |
| 8a1ea92ca05ffff | Ilidža | Osjek | 51 | 7,587.900 | 148.800 | B |
| 8a1ef69601affff | Ilidža | Stojčevac | 26 | 3,868.300 | 148.800 | B |
| 8a1ea92ce05ffff | Ilidža | Lipe | 15 | 2,231.900 | 148.800 | B |
| 8a1ef69638d7fff | Ilidža | Hrasnica | 55 | 8,194.600 | 149.000 | B |
| 8a1ea92ca0effff | Ilidža | Osjek | 46 | 6,854.000 | 149.000 | B |
| 8a1ef6961d8ffff | Ilidža | Sokolović-kolonija | 64 | 9,540.900 | 149.100 | B |
| 8a1ef6964caffff | Ilidža | Vrelo Bosne | 24 | 3,578.100 | 149.100 | B |
| 8a1ef69638c7fff | Ilidža | Hrasnica | 68 | 10,138.300 | 149.100 | B |
| 8a1ea92cab0ffff | Ilidža | Dolovi | 33 | 4,920.500 | 149.100 | B |
| 8a1ef6960757fff | Ilidža | Kovači (Ilidža) | 40 | 5,964.300 | 149.100 | B |
| 8a1ea92cb777fff | Ilidža | Otes | 38 | 5,667.400 | 149.100 | B |
| 8a1ef69656b7fff | Ilidža | Sokolović-kolonija | 44 | 6,562.500 | 149.100 | B |
| 8a1ea92caadffff | Ilidža | Bjelaće | 39 | 5,820.400 | 149.200 | B |
| 8a1ef696306ffff | Ilidža | Lasica | 34 | 5,075.000 | 149.300 | B |
| 8a1ef69606d7fff | Ilidža | Kovači (Ilidža) | 29 | 4,331.500 | 149.400 | B |
| 8a1ea92cb987fff | Ilidža | Doglodi | 55 | 8,215.800 | 149.400 | B |
| 8a1ef6961a0ffff | Ilidža | Donji Kotorac | 46 | 6,872.100 | 149.400 | B |
| 8a1ef459c91ffff | Stari Grad Sarajevo | Ferhadija | 182 | 27,191.900 | 149.400 | A |
| 8a1ea92ca21ffff | Ilidža | Osjek | 44 | 6,575.200 | 149.400 | B |
| 8a1ea92cb757fff | Ilidža | Otes | 54 | 8,071.100 | 149.500 | B |
| 8a1ea92cb937fff | Ilidža | Doglodi | 34 | 5,082.700 | 149.500 | B |
| 8a1ef6960a8ffff | Ilidža | Sokolović-kolonija | 48 | 7,180.600 | 149.600 | B |
| 8a1ea92c86effff | Ilidža | Doglodi | 27 | 4,039.800 | 149.600 | B |
| 8a1ea92c0787fff | Ilidža | Rudnik | 35 | 5,237.000 | 149.600 | B |
| 8a1ef69650cffff | Ilidža | Butmir | 35 | 5,238.300 | 149.700 | B |
| 8a1ea92caa37fff | Ilidža | Bjelaće | 39 | 5,837.700 | 149.700 | B |
| 8a1ef69638e7fff | Ilidža | Hrasnica | 61 | 9,132.400 | 149.700 | B |
| 8a1ea92cb107fff | Ilidža | Doglodi | 36 | 5,390.000 | 149.700 | B |
| 8a1ef6961ca7fff | Ilidža | Sokolović-kolonija | 74 | 11,081.400 | 149.700 | B |
| 8a1ef696421ffff | Ilidža | Lužani | 32 | 4,793.900 | 149.800 | B |
| 8a1ef6961c07fff | Ilidža | Sokolović-kolonija | 64 | 9,590.300 | 149.800 | B |
| 8a1ea92cd72ffff | Novi Grad Sarajevo | Reljevo | 11 | 1,648.500 | 149.900 | A |
| 8a1ef4583a47fff | Stari Grad Sarajevo | Mošćanica | 16 | 2,398.500 | 149.900 | A |
| 8a1ef6961cb7fff | Ilidža | Sokolović-kolonija | 69 | 10,345.100 | 149.900 | B |
| 8a1ef696072ffff | Ilidža | Kovači (Ilidža) | 51 | 7,646.700 | 149.900 | B |
| 8a1ef696070ffff | Ilidža | Kovači (Ilidža) | 52 | 7,797.500 | 150.000 | B |
| 8a1ea92cab57fff | Ilidža | Bjelaće | 35 | 5,251.400 | 150.000 | B |
| 8a1ef6961c27fff | Ilidža | Sokolović-kolonija | 58 | 8,712.200 | 150.200 | B |
| 8a1ef6965327fff | Ilidža | Naselje Bulevar | 86 | 12,923.600 | 150.300 | B |
| 8a1ea92cb35ffff | Ilidža | Azići | 66 | 9,920.400 | 150.300 | B |
| 8a1ef696526ffff | Ilidža | Stupsko Brdo | 42 | 6,314.900 | 150.400 | B |
| 8a1ef696036ffff | Ilidža | Sokolović-kolonija | 68 | 10,224.200 | 150.400 | B |
| 8a1ef6960627fff | Ilidža | Kovači (Ilidža) | 46 | 6,918.400 | 150.400 | B |
| 8a1ef6960337fff | Ilidža | Sokolović-kolonija | 54 | 8,123.300 | 150.400 | B |
| 8a1ea92c0ca7fff | Ilidža | Kobiljača | 17 | 2,557.900 | 150.500 | B |
| 8a1ea92cb80ffff | Ilidža | Doglodi | 40 | 6,019.300 | 150.500 | B |
| 8a1ef4592697fff | Ilidža | Donji Kotorac | 37 | 5,568.600 | 150.500 | B |
| 8a1ef4583a37fff | Stari Grad Sarajevo | Mošćanica | 15 | 2,257.600 | 150.500 | A |
| 8a1ef6964aaffff | Ilidža | Vreoca | 67 | 10,090.400 | 150.600 | B |
| 8a1ef6966a27fff | Ilidža | Vrutci | 14 | 2,108.600 | 150.600 | B |
| 8a1ef6961d17fff | Ilidža | Sokolović-kolonija | 88 | 13,256.900 | 150.600 | B |
| 8a1ea92c3677fff | Ilidža | Gladno polje | 14 | 2,114.700 | 151.000 | B |
| 8a1ef6963157fff | Ilidža | Lasica | 56 | 8,460.300 | 151.100 | B |
| 8a1ef458179ffff | Stari Grad Sarajevo | Mošćanica | 15 | 2,266.300 | 151.100 | A |
| 8a1ef696075ffff | Ilidža | Kovači (Ilidža) | 48 | 7,255.900 | 151.200 | B |
| 8a1ea92cb9affff | Ilidža | Doglodi | 60 | 9,087.700 | 151.500 | B |
| 8a1ef6964c27fff | Ilidža | Plandište | 75 | 11,365.700 | 151.500 | B |
| 8a1ef6960ccffff | Ilidža | Stojčevac | 15 | 2,273.200 | 151.500 | B |
| 8a1ea92ce277fff | Ilidža | Dolovi | 17 | 2,576.300 | 151.500 | B |
| 8a1ef6965ceffff | Ilidža | Ilidža | 126 | 19,110.300 | 151.700 | B |
| 8a1ef4592507fff | Ilidža | Stupsko Brdo | 50 | 7,589.100 | 151.800 | B |
| 8a1ef696435ffff | Ilidža | Lužani | 84 | 12,751.300 | 151.800 | B |
| 8a1ef6961d1ffff | Ilidža | Sokolović-kolonija | 92 | 13,973.100 | 151.900 | B |
| 8a1ef459c95ffff | Stari Grad Sarajevo | Baščaršija | 162 | 24,608.500 | 151.900 | A |
| 8a1ea92cb137fff | Ilidža | Doglodi | 49 | 7,444.400 | 151.900 | B |
| 8a1ef6960007fff | Ilidža | Kovači (Ilidža) | 49 | 7,445.400 | 151.900 | B |
| 8a1ea92c86dffff | Ilidža | Doglodi | 52 | 7,902.200 | 152.000 | B |
| 8a1ea92cb067fff | Ilidža | Doglodi | 56 | 8,514.100 | 152.000 | B |
| 8a1ea92cb58ffff | Ilidža | Otes | 35 | 5,321.300 | 152.000 | B |
| 8a1ef696008ffff | Ilidža | Kovači (Ilidža) | 39 | 5,934.500 | 152.200 | B |
| 8a1ea92dd2affff | Ilidža | Blažuj | 25 | 3,805.200 | 152.200 | B |
| 8a1ea92cbad7fff | Ilidža | Azići | 68 | 10,350.900 | 152.200 | B |
| 8a1ea92ca197fff | Ilidža | Blažuj | 38 | 5,787.200 | 152.300 | B |
| 8a1ef6964d07fff | Ilidža | Plandište | 67 | 10,207.100 | 152.300 | B |
| 8a1ea92cb117fff | Ilidža | Doglodi | 43 | 6,551.200 | 152.400 | B |
| 8a1ef69639affff | Ilidža | Hrasnica | 92 | 14,038.700 | 152.600 | B |
| 8a1ea92c332ffff | Ilidža | Gladno polje | 15 | 2,289.000 | 152.600 | B |
| 8a1ea92d926ffff | Ilidža | Vrelo Bosne | 11 | 1,679.800 | 152.700 | B |
| 8a1ea92c86c7fff | Ilidža | Doglodi | 39 | 5,957.200 | 152.700 | B |
| 8a1ea92ca4dffff | Ilidža | Blažuj | 13 | 1,987.800 | 152.900 | B |
| 8a1ea92cbd77fff | Ilidža | Doglodi | 55 | 8,415.200 | 153.000 | B |
| 8a1ef696064ffff | Ilidža | Kovači (Ilidža) | 89 | 13,618.100 | 153.000 | B |
| 8a1ef69639a7fff | Ilidža | Hrasnica | 94 | 14,401.900 | 153.200 | B |
| 8a1ef6964d1ffff | Ilidža | Plandište | 86 | 13,194.900 | 153.400 | B |
| 8a1ef4581647fff | Stari Grad Sarajevo | Mošćanica | 12 | 1,842.000 | 153.500 | A |
| 8a1ea92cbc0ffff | Ilidža | Donji Doglodi | 54 | 8,297.600 | 153.700 | B |
| 8a1ef6960267fff | Ilidža | Sokolović-kolonija | 78 | 11,991.200 | 153.700 | B |
| 8a1ef4581787fff | Stari Grad Sarajevo | Mošćanica | 18 | 2,767.800 | 153.800 | A |
| 8a1ef459c94ffff | Stari Grad Sarajevo | Baščaršija | 176 | 27,124.200 | 154.100 | A |
| 8a1ef6960cdffff | Ilidža | Stojčevac | 27 | 4,163.800 | 154.200 | B |
| 8a1ef4583a4ffff | Stari Grad Sarajevo | Mošćanica | 11 | 1,698.300 | 154.400 | A |
| 8a1ef6963917fff | Ilidža | Hrasnica | 99 | 15,290.100 | 154.400 | B |
| 8a1ea92cab5ffff | Ilidža | Bjelaće | 19 | 2,938.900 | 154.700 | B |
| 8a1ef6965437fff | Ilidža | Lužani | 79 | 12,237.900 | 154.900 | B |
| 8a1ea92cd05ffff | Novi Grad Sarajevo | Reljevo | 15 | 2,331.000 | 155.400 | A |
| 8a1ea92c016ffff | Ilidža | Rakovica | 13 | 2,020.800 | 155.400 | B |
| 8a1ea92cd0effff | Novi Grad Sarajevo | Reljevo | 19 | 2,954.900 | 155.500 | A |
| 8a1ef459d49ffff | Stari Grad Sarajevo | Širokača | 112 | 17,496.800 | 156.200 | A |
| 8a1ea92cda67fff | Novi Grad Sarajevo | Reljevo | 15 | 2,343.400 | 156.200 | A |
| 8a1ef69650b7fff | Ilidža | Ilidža | 140 | 21,928.000 | 156.600 | B |
| 8a1ef45816b7fff | Stari Grad Sarajevo | Mošćanica | 14 | 2,197.100 | 156.900 | A |
| 8a1ea92dd2b7fff | Ilidža | Blažuj | 16 | 2,518.900 | 157.400 | B |
| 8a1ef45812c7fff | Stari Grad Sarajevo | Mošćanica | 10 | 1,575.900 | 157.600 | A |
| 8a1ef45b211ffff | Novi Grad Sarajevo | Reljevo | 10 | 1,580.900 | 158.100 | A |
| 8a1ea92cdb6ffff | Novi Grad Sarajevo | Reljevo | 11 | 1,745.300 | 158.700 | A |
| 8a1ea92cda47fff | Novi Grad Sarajevo | Reljevo | 10 | 1,592.000 | 159.200 | A |
| 8a1ef4583157fff | Stari Grad Sarajevo | Mošćanica | 24 | 3,826.500 | 159.400 | A |
| 8a1ea92cd0c7fff | Novi Grad Sarajevo | Reljevo | 13 | 2,077.800 | 159.800 | A |
| 8a1ef45b2cb7fff | Novi Grad Sarajevo | Reljevo | 24 | 3,844.700 | 160.200 | A |
| 8a1ef45b2c97fff | Novi Grad Sarajevo | Reljevo | 30 | 4,812.100 | 160.400 | A |
| 8a1ef6946447fff | Ilidža | Hrasnica | 11 | 1,768.800 | 160.800 | B |
| 8a1ef4583a07fff | Stari Grad Sarajevo | Mošćanica | 27 | 4,344.300 | 160.900 | A |
| 8a1ef4583b8ffff | Stari Grad Sarajevo | Mošćanica | 15 | 2,416.100 | 161.100 | A |
| 8a1ea92cd0cffff | Novi Grad Sarajevo | Reljevo | 26 | 4,188.800 | 161.100 | A |
| 8a1ea92cda77fff | Novi Grad Sarajevo | Reljevo | 12 | 1,935.400 | 161.300 | A |
| 8a1ef458366ffff | Stari Grad Sarajevo | Mošćanica | 35 | 5,651.800 | 161.500 | A |
| 8a1ef459d157fff | Stari Grad Sarajevo | Mošćanica | 10 | 1,614.900 | 161.500 | A |
| 8a1ef459c90ffff | Stari Grad Sarajevo | Baščaršija | 193 | 31,217.600 | 161.700 | A |
| 8a1ef45b2c0ffff | Novi Grad Sarajevo | Reljevo | 11 | 1,782.000 | 162.000 | A |
| 8a1ef45b2cc7fff | Novi Grad Sarajevo | Reljevo | 20 | 3,249.100 | 162.500 | A |
| 8a1ea92cdba7fff | Novi Grad Sarajevo | Reljevo | 11 | 1,791.500 | 162.900 | A |
| 8a1ef45b2ce7fff | Novi Grad Sarajevo | Reljevo | 10 | 1,628.900 | 162.900 | A |
| 8a1ef4583a87fff | Stari Grad Sarajevo | Mošćanica | 32 | 5,214.600 | 163.000 | A |
| 8a1ef4583a27fff | Stari Grad Sarajevo | Mošćanica | 25 | 4,083.400 | 163.300 | A |
| 8a1ea92cd06ffff | Novi Grad Sarajevo | Reljevo | 23 | 3,767.300 | 163.800 | A |
| 8a1ef4583b5ffff | Stari Grad Sarajevo | Mošćanica | 24 | 3,931.900 | 163.800 | A |
| 8a1ea92cda37fff | Novi Grad Sarajevo | Reljevo | 12 | 1,971.300 | 164.300 | A |
| 8a1ef4583a2ffff | Stari Grad Sarajevo | Mošćanica | 31 | 5,114.000 | 165.000 | A |
| 8a1ea92cd98ffff | Novi Grad Sarajevo | Reljevo | 12 | 1,984.500 | 165.400 | A |
| 8a1ef45b2c07fff | Novi Grad Sarajevo | Reljevo | 14 | 2,316.100 | 165.400 | A |
| 8a1ef45b2117fff | Novi Grad Sarajevo | Reljevo | 10 | 1,654.500 | 165.400 | A |
| 8a1ef459c82ffff | Stari Grad Sarajevo | Baščaršija | 188 | 31,145.900 | 165.700 | A |
| 8a1ef45812d7fff | Stari Grad Sarajevo | Mošćanica | 16 | 2,661.000 | 166.300 | A |
| 8a1ef4583a67fff | Stari Grad Sarajevo | Mošćanica | 18 | 2,995.400 | 166.400 | A |
| 8a1ef458315ffff | Stari Grad Sarajevo | Mošćanica | 20 | 3,337.800 | 166.900 | A |
| 8a1ef459c827fff | Stari Grad Sarajevo | Baščaršija | 205 | 34,255.600 | 167.100 | A |
| 8a1ef45b2c27fff | Novi Grad Sarajevo | Reljevo | 15 | 2,507.900 | 167.200 | A |
| 8a1ef4583aa7fff | Stari Grad Sarajevo | Mošćanica | 29 | 4,861.000 | 167.600 | A |
| 8a1ea92cda07fff | Novi Grad Sarajevo | Reljevo | 13 | 2,180.200 | 167.700 | A |
| 8a1ea92cdbaffff | Novi Grad Sarajevo | Reljevo | 13 | 2,181.000 | 167.800 | A |
| 8a1ef459c877fff | Stari Grad Sarajevo | Baščaršija | 166 | 27,853.000 | 167.800 | A |
| 8a1ea92cd857fff | Novi Grad Sarajevo | Reljevo | 11 | 1,847.700 | 168.000 | A |
| 8a1ef4583a9ffff | Stari Grad Sarajevo | Mošćanica | 33 | 5,549.500 | 168.200 | A |
| 8a1ef458304ffff | Stari Grad Sarajevo | Mošćanica | 34 | 5,724.300 | 168.400 | A |
| 8a1ea92cdb4ffff | Novi Grad Sarajevo | Reljevo | 15 | 2,531.400 | 168.800 | A |
| 8a1ea92cda2ffff | Novi Grad Sarajevo | Reljevo | 21 | 3,549.700 | 169.000 | A |
| 8a1ef4583337fff | Stari Grad Sarajevo | Mošćanica | 32 | 5,410.200 | 169.100 | A |
| 8a1ea92cd877fff | Novi Grad Sarajevo | Reljevo | 13 | 2,200.800 | 169.300 | A |
| 8a1ef458164ffff | Stari Grad Sarajevo | Mošćanica | 14 | 2,371.200 | 169.400 | A |
| 8a1ef459c807fff | Stari Grad Sarajevo | Baščaršija | 201 | 34,156.800 | 169.900 | A |
| 8a1ea92cd867fff | Novi Grad Sarajevo | Reljevo | 10 | 1,700.900 | 170.100 | A |
| 8a1ef4583a57fff | Stari Grad Sarajevo | Mošćanica | 30 | 5,103.900 | 170.100 | A |
| 8a1ef45814affff | Stari Grad Sarajevo | Mošćanica | 10 | 1,703.000 | 170.300 | A |
| 8a1ea92cda4ffff | Novi Grad Sarajevo | Reljevo | 10 | 1,706.800 | 170.700 | A |
| 8a1ef45b2d1ffff | Novi Grad Sarajevo | Reljevo | 21 | 3,588.000 | 170.900 | A |
| 8a1ea92cda17fff | Novi Grad Sarajevo | Reljevo | 22 | 3,770.300 | 171.400 | A |
| 8a1ea92cd9affff | Novi Grad Sarajevo | Reljevo | 18 | 3,096.100 | 172.000 | A |
| 8a1ef4583b0ffff | Stari Grad Sarajevo | Mošćanica | 26 | 4,483.300 | 172.400 | A |
| 8a1ef4583b2ffff | Stari Grad Sarajevo | Mošćanica | 25 | 4,326.300 | 173.100 | A |
| 8a1ea92cd337fff | Novi Grad Sarajevo | Reljevo | 21 | 3,648.200 | 173.700 | A |
| 8a1ea92cd04ffff | Novi Grad Sarajevo | Reljevo | 31 | 5,386.400 | 173.800 | A |
| 8a1ef458e90ffff | Stari Grad Sarajevo | Mošćanica | 10 | 1,760.200 | 176.000 | A |
| 8a1ef45b2caffff | Novi Grad Sarajevo | Reljevo | 15 | 2,692.500 | 179.500 | A |
| 8a1ef45817affff | Stari Grad Sarajevo | Mošćanica | 22 | 3,957.100 | 179.900 | A |
| 8a1ef45812dffff | Stari Grad Sarajevo | Mošćanica | 15 | 2,714.900 | 181.000 | A |
| 8a1ef4583a6ffff | Stari Grad Sarajevo | Mošćanica | 16 | 2,923.200 | 182.700 | A |
| 8a1ef458eda7fff | Stari Grad Sarajevo | Mošćanica | 10 | 1,829.200 | 182.900 | A |
| 8a1ef4583a77fff | Stari Grad Sarajevo | Mošćanica | 34 | 6,238.600 | 183.500 | A |
| 8a1ef4583b37fff | Stari Grad Sarajevo | Mošćanica | 17 | 3,124.200 | 183.800 | A |
| 8a1ef4583b77fff | Stari Grad Sarajevo | Mošćanica | 33 | 6,074.900 | 184.100 | A |
| 8a1ef458178ffff | Stari Grad Sarajevo | Mošćanica | 23 | 4,263.100 | 185.400 | A |
| 8a1ef458148ffff | Stari Grad Sarajevo | Mošćanica | 18 | 3,351.100 | 186.200 | A |
| 8a1ef4581697fff | Stari Grad Sarajevo | Mošćanica | 24 | 4,518.000 | 188.200 | A |
| 8a1ef458128ffff | Stari Grad Sarajevo | Mošćanica | 11 | 2,074.300 | 188.600 | A |
| 8a1ef45814d7fff | Stari Grad Sarajevo | Mošćanica | 24 | 4,642.100 | 193.400 | A |
| 8a1ef4581487fff | Stari Grad Sarajevo | Mošćanica | 12 | 2,352.600 | 196.000 | A |
| 8a1ef45830f7fff | Stari Grad Sarajevo | Mošćanica | 20 | 4,043.800 | 202.200 | A |
| 8a1ef4581567fff | Stari Grad Sarajevo | Mošćanica | 13 | 2,700.700 | 207.700 | A |
| 8a1ef458022ffff | Stari Grad Sarajevo | Mošćanica | 15 | 3,134.200 | 208.900 | A |
| 8a1ef4585777fff | Stari Grad Sarajevo | Mošćanica | 13 | 2,826.300 | 217.400 | A |
| 8a1ef4583acffff | Stari Grad Sarajevo | Mošćanica | 10 | 2,195.100 | 219.500 | A |
| 8a1ef4583b4ffff | Stari Grad Sarajevo | Mošćanica | 47 | 10,443.700 | 222.200 | A |
| 8a1ef45803affff | Stari Grad Sarajevo | Mošćanica | 14 | 3,154.700 | 225.300 | A |
| 8a1ef4580227fff | Stari Grad Sarajevo | Mošćanica | 13 | 2,996.600 | 230.500 | A |
| 8a1ef458332ffff | Stari Grad Sarajevo | Mošćanica | 10 | 2,368.400 | 236.800 | A |
| 8a1ef458c5affff | Stari Grad Sarajevo | Mošćanica | 12 | 2,954.200 | 246.200 | A |
| 8a1ef45802e7fff | Stari Grad Sarajevo | Mošćanica | 17 | 4,221.800 | 248.300 | A |
| 8a1ef45aab77fff | Stari Grad Sarajevo | Mošćanica | 11 | 2,979.700 | 270.900 | A |

## 5. Vizuelna provjera
Stanovnici u zonama gdje ih ne bi trebalo biti (aproksimacija: ravnomjerno po dijelu polja):

| vrsta | procijenjeno_stanovnika (površinski) |
|---|---|
| aerodrom | 1,340.000 |
| landuse=industrial | 10,174.000 |
| park | 7,148.000 |

Najgušće MZ (od 142 sa poznatim granicama):

| rang | opcina | mz | st | st_po_km2 |
|---|---|---|---|---|
| 1 | Novi Grad Sarajevo | Alipašino Polje BII | 3020 | 27,940.000 |
| 2 | Novi Grad Sarajevo | Alipašino Polje CI | 2024 | 24,502.000 |
| 3 | Novi Grad Sarajevo | Alipašino Polje CII | 2299 | 24,327.000 |
| 4 | Novi Grad Sarajevo | Alipašino Polje BI | 3646 | 22,893.000 |
| 5 | Novo Sarajevo | Malta | 4167 | 21,577.000 |
| 6 | Novo Sarajevo | Trg heroja | 4927 | 18,807.000 |
| 7 | Novi Grad Sarajevo | Otoka | 2921 | 18,395.000 |
| 8 | Novi Grad Sarajevo | Čengić Vila | 3054 | 17,690.000 |
| 9 | Novo Sarajevo | Grbavica I | 5754 | 17,251.000 |
| 10 | Novo Sarajevo | Čengić Vila II | 1661 | 16,564.000 |
| 11 | Novo Sarajevo | Hrasno | 1785 | 16,295.000 |
| 12 | Novo Sarajevo | Grbavica II | 5782 | 14,812.000 |
| 13 | Novi Grad Sarajevo | Staro Hrasno | 3042 | 14,422.000 |
| 14 | Novi Grad Sarajevo | Alipašin Most III | 7603 | 13,807.000 |
| 15 | Novo Sarajevo | Čengić Vila I | 3880 | 13,097.000 |

Dobrinja, Alipašino Polje, Grbavica (očekivano visoko):

| rang | opcina | mz | st | st_po_km2 |
|---|---|---|---|---|
| 1 | Novi Grad Sarajevo | Alipašino Polje BII | 3020 | 27,940.000 |
| 2 | Novi Grad Sarajevo | Alipašino Polje CI | 2024 | 24,502.000 |
| 3 | Novi Grad Sarajevo | Alipašino Polje CII | 2299 | 24,327.000 |
| 4 | Novi Grad Sarajevo | Alipašino Polje BI | 3646 | 22,893.000 |
| 9 | Novo Sarajevo | Grbavica I | 5754 | 17,251.000 |
| 12 | Novo Sarajevo | Grbavica II | 5782 | 14,812.000 |
| 18 | Novi Grad Sarajevo | Dobrinja D | 4995 | 12,393.000 |
| 20 | Novi Grad Sarajevo | Alipašino Polje AII | 2763 | 11,028.000 |
| 27 | Novi Grad Sarajevo | Dobrinja C | 4655 | 9,278.000 |
| 29 | Novi Grad Sarajevo | Dobrinja A | 5644 | 9,026.000 |
| 30 | Novi Grad Sarajevo | Alipašino Polje AI | 2447 | 8,883.000 |
| 31 | Novi Grad Sarajevo | Dobrinja B | 5366 | 8,873.000 |

Karta za vizuelni pregled: `out/karta.html`.

## 6. Starosne grupe
Zbir grupa = ukupno u svakom polju: **OK** (0 polja odstupa).

Odstupanje zbira grupa po općini od FZS-a (posljedica zaokruživanja po polju):

| opcina | d0_14 | d15_64 | d65plus |
|---|---|---|---|
| Centar Sarajevo | -35 | 39 | -4 |
| Ilidža | -281 | -37 | 318 |
| Novi Grad Sarajevo | -61 | 64 | -3 |
| Novo Sarajevo | -22 | -17 | 39 |
| Stari Grad Sarajevo | -36 | 62 | -26 |
| Vogošća | 157 | 171 | -328 |

## Napomene o modelu
- **Stari Grad Sarajevo**: MZ zbirovi iz Grafa 3 (udjeli)
- **Novi Grad Sarajevo**: MZ: β=0.5·udio_2010 + (1−β)·udio_modela; nove MZ s matičnom: nema; bez matične: ['Alipašin Most III', 'Zabrđe']
- Pouzdanost polja: {'B': 18329, 'A': 2489, 'C': 1345}
