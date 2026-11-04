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
**Nije izračunato**: nazivi MZ na Grafu 3 (Strategija 2024–2027, str. 16) još nisu potvrđeni. Nakon čitanja grafikona spremiti `data/stari_grad_graf3.csv` (kolone `mz`, `stanovnici`) i ponoviti korake 05–06.

## 3. Novi Grad: model bez MZ ograničenja vs udjeli 2010
Udjeli 2010 preskalirani na dio općine bez novih MZ. Odstupanje > 30% je označeno; veće udjele u modelu obično objašnjava nova gradnja nakon 2010.

| mz | model_udio | udio_2010 | omjer | oznaka |
|---|---|---|---|---|
| Dobrinja C | 0.002 | 0.042 | 0.057 | model < 2010 za >30%: provjeriti |
| Švrakino Selo I | 0.005 | 0.020 | 0.275 | model < 2010 za >30%: provjeriti |
| Alipašino Polje CI | 0.007 | 0.023 | 0.286 | model < 2010 za >30%: provjeriti |
| Aneks | 0.014 | 0.028 | 0.513 | model < 2010 za >30%: provjeriti |
| Alipašino Polje CII | 0.013 | 0.024 | 0.562 | model < 2010 za >30%: provjeriti |
| Alipašino Polje BII | 0.015 | 0.027 | 0.577 | model < 2010 za >30%: provjeriti |
| Olimpijsko Selo | 0.014 | 0.023 | 0.610 | model < 2010 za >30%: provjeriti |
| Alipašino Polje AI | 0.014 | 0.024 | 0.612 | model < 2010 za >30%: provjeriti |
| Dobrinja D | 0.031 | 0.048 | 0.647 | model < 2010 za >30%: provjeriti |
| Alipašino Polje AII | 0.015 | 0.023 | 0.675 | model < 2010 za >30%: provjeriti |
| Alipašino Polje BI | 0.020 | 0.029 | 0.692 | model < 2010 za >30%: provjeriti |
| Švrakino Selo III | 0.013 | 0.018 | 0.705 |  |
| Staro Hrasno | 0.018 | 0.024 | 0.729 |  |
| Čengić Vila | 0.024 | 0.031 | 0.772 |  |
| Otoka | 0.021 | 0.026 | 0.808 |  |
| Buća Potok | 0.039 | 0.045 | 0.848 |  |
| Alipašin Most II | 0.021 | 0.025 | 0.854 |  |
| Alipašin Most I | 0.066 | 0.067 | 0.979 |  |
| Švrakino Selo II | 0.041 | 0.040 | 1.023 |  |
| Dobrinja B | 0.051 | 0.050 | 1.027 |  |
| Dolac | 0.054 | 0.050 | 1.081 |  |
| Saraj Polje | 0.059 | 0.041 | 1.421 | model > 2010 za >30%: nova gradnja? |
| Dobrinja A | 0.064 | 0.039 | 1.629 | model > 2010 za >30%: nova gradnja? |
| Naselje heroja Sokolje | 0.069 | 0.041 | 1.692 | model > 2010 za >30%: nova gradnja? |
| Reljevo | 0.015 | 0.008 | 1.769 | model > 2010 za >30%: nova gradnja? |
| Briješće | 0.084 | 0.038 | 2.239 | model > 2010 za >30%: nova gradnja? |
| Dobroševići | 0.093 | 0.030 | 3.144 | model > 2010 za >30%: nova gradnja? |
| Alipašin Most III | 0.041 | nan | nan | nova MZ (nema 2010) |
| Zabrđe | 0.075 | nan | nan | nova MZ (nema 2010) |

Konačni udjeli korišteni kao meko ograničenje: vidi `interim/raspodjela_info.json`.

## 4. Gustina poda (stambeni m² po stanovniku, očekivano 15–60)
Medijan (polja s ≥ 10 st.): 81.2 m²/st. Polja izvan raspona: **628** od 746. Polja sa stanovnicima a bez stambenih zgrada (pouzdanost C, samo WorldPop): **31**.

| h3_id | opcina | mz | stanovnici | stambeni_m2 | m2_po_st | pouzdanost |
|---|---|---|---|---|---|---|
| 891ea92cd6fffff | Novi Grad Sarajevo | Zabrđe | 46 | 38.400 | 0.800 | A |
| 891ef4596abffff | Novi Grad Sarajevo | Alipašin Most I | 178 | 971.800 | 5.500 | A |
| 891ef45b243ffff | Novi Grad Sarajevo | Zabrđe | 30 | 227.900 | 7.600 | A |
| 891ef459c77ffff | Stari Grad Sarajevo | Širokača | 19 | 145.900 | 7.700 | C |
| 891ef4596d3ffff | Novi Grad Sarajevo | Briješće | 34 | 271.900 | 8.000 | A |
| 891ef4590dbffff | Novi Grad Sarajevo | Alipašin Most I | 196 | 1,885.500 | 9.600 | A |
| 891ef459183ffff | Novo Sarajevo | Željeznička | 342 | 3,339.500 | 9.800 | B |
| 891ef459187ffff | Novo Sarajevo | Željeznička | 226 | 2,411.600 | 10.700 | B |
| 891ef45866bffff | Centar Sarajevo | Gornji Velešići | 52 | 567.700 | 10.900 | B |
| 891ef45940bffff | Novi Grad Sarajevo | Alipašin Most I | 19 | 229.100 | 12.100 | A |
| 891ef45b2dbffff | Novi Grad Sarajevo | Zabrđe | 13 | 166.900 | 12.800 | A |
| 891ea92c827ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 23 | 313.900 | 13.600 | A |
| 891ef459397ffff | Novo Sarajevo | Hrasno Brdo | 379 | 22,753.800 | 60.000 | B |
| 891ef459567ffff | Novo Sarajevo | Pofalići I | 846 | 50,831.900 | 60.100 | B |
| 891ef459207ffff | Novi Grad Sarajevo | Dobrinja B | 1437 | 86,592.100 | 60.300 | A |
| 891ef45962fffff | Novi Grad Sarajevo | Alipašino Polje BII | 2465 | 148,556.400 | 60.300 | A |
| 891ef4591bbffff | Novo Sarajevo | Željeznička | 464 | 27,975.700 | 60.300 | B |
| 891ef45914bffff | Novo Sarajevo | Hrasno Brdo | 231 | 13,962.200 | 60.400 | B |
| 891ef4595abffff | Novo Sarajevo | Velešići | 116 | 7,035.100 | 60.600 | B |
| 891ef459623ffff | Novi Grad Sarajevo | Alipašino Polje AII | 1131 | 68,819.300 | 60.800 | A |
| 891ef45909bffff | Novi Grad Sarajevo | Buća Potok | 755 | 45,956.000 | 60.900 | A |
| 891ef4594c7ffff | Novi Grad Sarajevo | Zabrđe | 16 | 977.100 | 61.100 | A |
| 891ef458407ffff | Centar Sarajevo | nan | 11 | 672.800 | 61.200 | B |
| 891ef459097ffff | Novi Grad Sarajevo | Dolac | 632 | 38,693.900 | 61.200 | A |
| 891ef45902fffff | Novo Sarajevo | Hrasno Brdo | 815 | 50,006.800 | 61.400 | B |
| 891ef459043ffff | Novi Grad Sarajevo | Alipašino Polje CII | 1568 | 96,549.300 | 61.600 | A |
| 891ef45952bffff | Novo Sarajevo | Pofalići I | 870 | 53,587.900 | 61.600 | B |
| 891ef459157ffff | Novo Sarajevo | Grbavica II | 901 | 55,559.700 | 61.700 | B |
| 891ef4582c3ffff | Novo Sarajevo | Gornji Velešići | 563 | 34,720.000 | 61.700 | B |
| 891ef4595b3ffff | Novo Sarajevo | Velešići | 128 | 7,903.800 | 61.700 | B |
| 891ef45913bffff | Novo Sarajevo | Gornji Kovačići | 510 | 31,545.900 | 61.900 | B |
| 891ef45b24bffff | Novi Grad Sarajevo | Zabrđe | 363 | 22,548.000 | 62.100 | A |
| 891ef45958bffff | Novi Grad Sarajevo | Dolac | 14 | 874.300 | 62.400 | A |
| 891ef45906fffff | Novo Sarajevo | Hrasno Brdo | 249 | 15,560.300 | 62.500 | B |
| 891ef45824bffff | Centar Sarajevo | Velešići | 535 | 33,481.900 | 62.600 | B |
| 891ea92cbb7ffff | Novi Grad Sarajevo | Briješće | 24 | 1,506.900 | 62.800 | A |
| 891ef45943bffff | Novi Grad Sarajevo | Dolac | 198 | 12,432.700 | 62.800 | A |
| 891ef45906bffff | Novi Grad Sarajevo | Švrakino Selo II | 352 | 22,144.000 | 62.900 | A |
| 891ef45832fffff | Stari Grad Sarajevo | Mošćanica | 45 | 2,833.600 | 63.000 | B |
| 891ef45b2d3ffff | Novi Grad Sarajevo | Zabrđe | 87 | 5,488.900 | 63.100 | A |
| 891ef458173ffff | Stari Grad Sarajevo | Mošćanica | 19 | 1,202.800 | 63.300 | B |
| 891ef45844bffff | Centar Sarajevo | nan | 31 | 1,963.000 | 63.300 | B |
| 891ef459d9bffff | Stari Grad Sarajevo | Mošćanica | 47 | 2,980.800 | 63.400 | B |
| 891ef459283ffff | Novi Grad Sarajevo | Olimpijsko Selo | 1681 | 106,808.800 | 63.500 | A |
| 891ef459287ffff | Novi Grad Sarajevo | Švrakino Selo II | 507 | 32,219.000 | 63.500 | A |
| 891ef459027ffff | Novo Sarajevo | Hrasno Brdo | 1049 | 66,800.200 | 63.700 | B |
| 891ef45900bffff | Novi Grad Sarajevo | Otoka | 1067 | 67,961.700 | 63.700 | A |
| 891ea92c9afffff | Novi Grad Sarajevo | Zabrđe | 160 | 10,211.000 | 63.800 | A |
| 891ef459087ffff | Novi Grad Sarajevo | Buća Potok | 1064 | 67,955.900 | 63.900 | A |
| 891ef45908fffff | Novi Grad Sarajevo | Buća Potok | 1040 | 66,461.200 | 63.900 | A |
| 891ef459cc7ffff | Centar Sarajevo | Širokača | 313 | 20,038.700 | 64.000 | B |
| 891ea92c9d7ffff | Novi Grad Sarajevo | Zabrđe | 203 | 12,998.000 | 64.000 | A |
| 891ef459217ffff | Novi Grad Sarajevo | Dobrinja D | 1051 | 67,300.300 | 64.000 | A |
| 891ef4595dbffff | Novi Grad Sarajevo | Dolac | 41 | 2,626.400 | 64.100 | A |
| 891ef45918fffff | Novo Sarajevo | Željeznička | 850 | 54,473.100 | 64.100 | B |
| 891ef45939bffff | Novo Sarajevo | Hrasno Brdo | 200 | 12,823.900 | 64.100 | B |
| 891ef458047ffff | Centar Sarajevo | nan | 31 | 1,999.700 | 64.500 | B |
| 891ef459dd3ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 38 | 2,453.400 | 64.600 | B |
| 891ef45910bffff | Novo Sarajevo | Vraca | 1026 | 66,320.800 | 64.600 | B |
| 891ef459083ffff | Novi Grad Sarajevo | Buća Potok | 931 | 60,190.300 | 64.700 | A |
| 891ea92c9b3ffff | Novi Grad Sarajevo | Zabrđe | 306 | 19,835.300 | 64.800 | A |
| 891ef459d97ffff | Stari Grad Sarajevo | Mošćanica | 21 | 1,363.000 | 64.900 | B |
| 891ef4590c3ffff | Novi Grad Sarajevo | Alipašin Most III | 710 | 46,084.300 | 64.900 | A |
| 891ea92c9b7ffff | Novi Grad Sarajevo | Zabrđe | 50 | 3,246.700 | 64.900 | A |
| 891ef458393ffff | Stari Grad Sarajevo | Sedrenik | 12 | 779.400 | 64.900 | B |
| 891ef45b27bffff | Novi Grad Sarajevo | Zabrđe | 12 | 779.500 | 65.000 | A |
| 891ef459153ffff | Novo Sarajevo | Hrasno Brdo | 998 | 64,933.500 | 65.100 | B |
| 891ef45940fffff | Novi Grad Sarajevo | Dolac | 201 | 13,091.500 | 65.100 | A |
| 891ef4596b7ffff | Novi Grad Sarajevo | Alipašin Most I | 589 | 38,424.200 | 65.200 | A |
| 891ea92c993ffff | Novi Grad Sarajevo | Zabrđe | 421 | 27,541.100 | 65.400 | A |
| 891ef45929bffff | Novi Grad Sarajevo | Saraj Polje | 753 | 49,324.000 | 65.500 | A |
| 891ef459537ffff | Novo Sarajevo | Velešići | 624 | 40,974.400 | 65.700 | B |
| 891ea92cd73ffff | Novi Grad Sarajevo | Dobroševići | 74 | 4,868.500 | 65.800 | A |
| 891ef4581dbffff | Stari Grad Sarajevo | Mošćanica | 32 | 2,109.800 | 65.900 | B |
| 891ef45900fffff | Novi Grad Sarajevo | Otoka | 1473 | 97,151.200 | 66.000 | A |
| 891ef459023ffff | Novi Grad Sarajevo | Staro Hrasno | 1679 | 110,771.200 | 66.000 | A |
| 891ef45915bffff | Novo Sarajevo | Hrasno Brdo | 808 | 53,311.900 | 66.000 | B |
| 891ef458203ffff | Centar Sarajevo | nan | 427 | 28,254.100 | 66.200 | B |
| 891ef458623ffff | Centar Sarajevo | nan | 29 | 1,920.700 | 66.200 | B |
| 891ea92cdcfffff | Novi Grad Sarajevo | Dobroševići | 29 | 1,920.900 | 66.200 | A |
| 891ef4590a3ffff | Novo Sarajevo | Pofalići II | 758 | 50,221.300 | 66.300 | B |
| 891ea92c997ffff | Novi Grad Sarajevo | Zabrđe | 568 | 37,648.000 | 66.300 | A |
| 891ef4582d3ffff | Centar Sarajevo | Gornji Velešići | 208 | 13,827.100 | 66.500 | B |
| 891ef459503ffff | Novo Sarajevo | Pofalići II | 46 | 3,058.700 | 66.500 | B |
| 891ef45946fffff | Novi Grad Sarajevo | Buća Potok | 739 | 49,154.100 | 66.500 | A |
| 891ef459213ffff | Novi Grad Sarajevo | Dobrinja D | 1238 | 82,376.300 | 66.500 | A |
| 891ef459463ffff | Novi Grad Sarajevo | Alipašin Most I | 563 | 37,465.100 | 66.500 | A |
| 891ef458253ffff | Novo Sarajevo | Velešići | 1014 | 67,508.100 | 66.600 | B |
| 891ef45950fffff | Novo Sarajevo | Pofalići II | 470 | 31,321.900 | 66.600 | B |
| 891ea92cd67ffff | Novi Grad Sarajevo | Zabrđe | 305 | 20,343.500 | 66.700 | A |
| 891ef459577ffff | Novo Sarajevo | Pofalići I | 872 | 58,221.300 | 66.800 | B |
| 891ef45833bffff | Stari Grad Sarajevo | Mošćanica | 148 | 9,905.000 | 66.900 | B |
| 891ef45861bffff | Centar Sarajevo | nan | 19 | 1,273.400 | 67.000 | B |
| 891ef459143ffff | Novo Sarajevo | Vraca | 840 | 56,312.200 | 67.000 | B |
| 891ef4582cbffff | Novo Sarajevo | Gornji Velešići | 935 | 62,781.600 | 67.100 | B |
| 891ea92cdabffff | Novi Grad Sarajevo | Reljevo | 51 | 3,428.200 | 67.200 | A |
| 891ef45923bffff | Novi Grad Sarajevo | Dobrinja B | 560 | 37,704.300 | 67.300 | A |
| 891ef45b2c3ffff | Novi Grad Sarajevo | Zabrđe | 121 | 8,167.800 | 67.500 | A |
| 891ea92c98fffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 258 | 17,420.400 | 67.500 | A |
| 891ef459d57ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 30 | 2,029.100 | 67.600 | B |
| 891ef45b2cbffff | Novi Grad Sarajevo | Zabrđe | 260 | 17,591.500 | 67.700 | A |
| 891ef459cafffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 203 | 13,755.300 | 67.800 | B |
| 891ef4592b7ffff | Novi Grad Sarajevo | Švrakino Selo II | 500 | 33,964.800 | 67.900 | A |
| 891ea92c9a3ffff | Novi Grad Sarajevo | Zabrđe | 354 | 24,082.300 | 68.000 | A |
| 891ef45839bffff | Stari Grad Sarajevo | Sedrenik | 67 | 4,561.400 | 68.100 | B |
| 891ef6965a3ffff | Novi Grad Sarajevo | Dobrinja A | 33 | 2,252.500 | 68.300 | A |
| 891ef4596a7ffff | Novi Grad Sarajevo | Alipašin Most I | 893 | 60,968.800 | 68.300 | A |
| 891ef4590d3ffff | Novi Grad Sarajevo | Alipašin Most I | 845 | 57,769.300 | 68.400 | A |
| 891ef4590afffff | Novo Sarajevo | Čengić Vila I | 1396 | 95,468.600 | 68.400 | B |
| 891ef45904fffff | Novi Grad Sarajevo | Švrakino Selo II | 752 | 51,469.200 | 68.400 | A |
| 891ef45844fffff | Centar Sarajevo | nan | 25 | 1,711.400 | 68.500 | B |
| 891ea92cd37ffff | Novi Grad Sarajevo | Zabrđe | 44 | 3,015.400 | 68.500 | A |
| 891ef459467ffff | Novi Grad Sarajevo | Buća Potok | 746 | 51,273.800 | 68.700 | A |
| 891ef45806fffff | Stari Grad Sarajevo | Sedrenik | 86 | 5,936.900 | 69.000 | B |
| 891ef45840fffff | Centar Sarajevo | nan | 12 | 828.800 | 69.100 | B |
| 891ef45b273ffff | Novi Grad Sarajevo | Zabrđe | 28 | 1,934.600 | 69.100 | A |
| 891ef4594c3ffff | Novi Grad Sarajevo | Zabrđe | 55 | 3,804.800 | 69.200 | A |
| 891ea92c947ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 82 | 5,673.900 | 69.200 | A |
| 891ef6965a7ffff | Novi Grad Sarajevo | Dobrinja A | 438 | 30,332.000 | 69.300 | A |
| 891ea92cd2bffff | Novi Grad Sarajevo | Zabrđe | 409 | 28,507.700 | 69.700 | A |
| 891ea92c9abffff | Novi Grad Sarajevo | Zabrđe | 322 | 22,526.500 | 70.000 | A |
| 891ef4586bbffff | Centar Sarajevo | nan | 39 | 2,728.700 | 70.000 | B |
| 891ef4595b7ffff | Centar Sarajevo | Gornji Velešići | 192 | 13,435.300 | 70.000 | B |
| 891ef459ca7ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 253 | 17,708.000 | 70.000 | B |
| 891ef459007ffff | Novi Grad Sarajevo | Čengić Vila | 1442 | 101,021.700 | 70.100 | A |
| 891ef459433ffff | Novi Grad Sarajevo | Dolac | 56 | 3,929.400 | 70.200 | A |
| 891ef45956bffff | Novo Sarajevo | Pofalići II | 1076 | 75,596.100 | 70.300 | B |
| 891ef45b213ffff | Novi Grad Sarajevo | Zabrđe | 64 | 4,496.600 | 70.300 | A |
| 891ea92c98bffff | Novi Grad Sarajevo | Zabrđe | 266 | 18,706.300 | 70.300 | A |
| 891ef458e5bffff | Stari Grad Sarajevo | Mošćanica | 13 | 914.500 | 70.300 | B |
| 891ef45946bffff | Novi Grad Sarajevo | Alipašin Most I | 723 | 50,879.200 | 70.400 | A |
| 891ef45944fffff | Novi Grad Sarajevo | Alipašin Most I | 595 | 41,902.400 | 70.400 | A |
| 891ea92c9a7ffff | Novi Grad Sarajevo | Zabrđe | 182 | 12,818.000 | 70.400 | A |
| 891ea92cdc7ffff | Novi Grad Sarajevo | Dobroševići | 30 | 2,113.900 | 70.500 | A |
| 891ef45b247ffff | Novi Grad Sarajevo | Zabrđe | 87 | 6,149.700 | 70.700 | A |
| 891ef45917bffff | Novo Sarajevo | Vraca | 13 | 919.100 | 70.700 | B |
| 891ea92cd5bffff | Novi Grad Sarajevo | Dobroševići | 122 | 8,630.500 | 70.700 | A |
| 891ef4591afffff | Centar Sarajevo | Kovačići | 516 | 36,503.000 | 70.700 | B |
| 891ef458627ffff | Centar Sarajevo | nan | 117 | 8,284.500 | 70.800 | B |
| 891ea92c96fffff | Novi Grad Sarajevo | Briješće | 202 | 14,309.700 | 70.800 | A |
| 891ea92c987ffff | Novi Grad Sarajevo | Zabrđe | 621 | 44,091.600 | 71.000 | A |
| 891ef45958fffff | Novo Sarajevo | Pofalići II | 20 | 1,421.700 | 71.100 | B |
| 891ef4596b3ffff | Novi Grad Sarajevo | Briješće | 291 | 20,723.600 | 71.200 | A |
| 891ef459447ffff | Novi Grad Sarajevo | Alipašin Most I | 442 | 31,511.300 | 71.300 | A |
| 891ef459d93ffff | Stari Grad Sarajevo | Mošćanica | 56 | 3,998.900 | 71.400 | B |
| 891ef459473ffff | Novi Grad Sarajevo | Alipašin Most I | 487 | 34,789.200 | 71.400 | A |
| 891ef459033ffff | Novi Grad Sarajevo | Staro Hrasno | 1449 | 103,524.100 | 71.400 | A |
| 891ef458493ffff | Centar Sarajevo | nan | 31 | 2,218.400 | 71.600 | B |
| 891ea92c9bbffff | Novi Grad Sarajevo | Zabrđe | 475 | 34,032.800 | 71.600 | A |
| 891ef459293ffff | Novi Grad Sarajevo | Alipašino Polje BI | 2091 | 149,958.200 | 71.700 | A |
| 891ea92c973ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 317 | 22,751.600 | 71.800 | A |
| 891ef459127ffff | Centar Sarajevo | Gornji Kovačići | 141 | 10,126.400 | 71.800 | B |
| 891ef459dcbffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 94 | 6,767.000 | 72.000 | B |
| 891ea92c937ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 81 | 5,836.900 | 72.100 | A |
| 891ef45920bffff | Novi Grad Sarajevo | Dobrinja B | 1026 | 73,952.200 | 72.100 | A |
| 891ef45920fffff | Novi Grad Sarajevo | Dobrinja B | 974 | 70,270.200 | 72.100 | A |
| 891ef459573ffff | Novo Sarajevo | Pofalići II | 797 | 57,589.800 | 72.300 | B |
| 891ef459d07ffff | Stari Grad Sarajevo | Mošćanica | 28 | 2,025.700 | 72.300 | B |
| 891ef45921bffff | Novi Grad Sarajevo | Dobrinja D | 1354 | 98,131.700 | 72.500 | A |
| 891ef4590abffff | Novo Sarajevo | Čengić Vila I | 1378 | 99,883.500 | 72.500 | B |
| 891ef458ec3ffff | Stari Grad Sarajevo | Mošćanica | 32 | 2,324.100 | 72.600 | B |
| 891ef459273ffff | Novi Grad Sarajevo | Dobrinja B | 471 | 34,269.900 | 72.800 | A |
| 891ea92cd8fffff | Novi Grad Sarajevo | Reljevo | 21 | 1,528.900 | 72.800 | A |
| 891ef459103ffff | Novo Sarajevo | Grbavica I | 1574 | 114,637.100 | 72.800 | B |
| 891ef459613ffff | Novi Grad Sarajevo | Briješće | 191 | 13,916.700 | 72.900 | A |
| 891ef45824fffff | Centar Sarajevo | nan | 512 | 37,422.900 | 73.100 | B |
| 891ef4591cfffff | Novo Sarajevo | Grbavica II | 1540 | 112,595.400 | 73.100 | B |
| 891ef458363ffff | Stari Grad Sarajevo | Mošćanica | 151 | 11,043.900 | 73.100 | B |
| 891ef45966fffff | Novi Grad Sarajevo | Saraj Polje | 651 | 47,683.100 | 73.200 | A |
| 891ef459117ffff | Novo Sarajevo | Grbavica I | 1416 | 103,744.200 | 73.300 | B |
| 891ef459ddbffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 171 | 12,542.800 | 73.300 | B |
| 891ef4594dbffff | Novi Grad Sarajevo | Zabrđe | 212 | 15,567.400 | 73.400 | A |
| 891ef4591dbffff | Novo Sarajevo | Malta | 1511 | 111,122.900 | 73.500 | B |
| 891ea92c963ffff | Novi Grad Sarajevo | Briješće | 266 | 19,573.400 | 73.600 | A |
| 891ef45b21bffff | Novi Grad Sarajevo | Zabrđe | 203 | 14,956.300 | 73.700 | A |
| 891ef458073ffff | Centar Sarajevo | nan | 48 | 3,540.100 | 73.800 | B |
| 891ef45918bffff | Novo Sarajevo | Željeznička | 1406 | 103,739.400 | 73.800 | B |
| 891ea92cddbffff | Novi Grad Sarajevo | Dobroševići | 83 | 6,124.100 | 73.800 | A |
| 891ea92cdd3ffff | Novi Grad Sarajevo | Dobroševići | 33 | 2,435.500 | 73.800 | A |
| 891ef45830fffff | Stari Grad Sarajevo | Mošćanica | 148 | 10,948.300 | 74.000 | B |
| 891ef458387ffff | Stari Grad Sarajevo | Mošćanica | 11 | 814.000 | 74.000 | B |
| 891ef4592d7ffff | Novi Grad Sarajevo | Saraj Polje | 640 | 47,462.100 | 74.200 | A |
| 891ef45832bffff | Stari Grad Sarajevo | Mošćanica | 142 | 10,545.400 | 74.300 | B |
| 891ef4582d7ffff | Centar Sarajevo | nan | 394 | 29,281.600 | 74.300 | B |
| 891ef4596bbffff | Novi Grad Sarajevo | Briješće | 385 | 28,613.900 | 74.300 | A |
| 891ef45947bffff | Novi Grad Sarajevo | Alipašin Most I | 764 | 56,817.800 | 74.400 | A |
| 891ef459553ffff | Novi Grad Sarajevo | Dolac | 271 | 20,187.700 | 74.500 | A |
| 891ef459d8bffff | Stari Grad Sarajevo | Babića bašča | 18 | 1,343.000 | 74.600 | B |
| 891ef45ae2bffff | Stari Grad Sarajevo | Mošćanica | 12 | 896.400 | 74.700 | B |
| 891ef45944bffff | Novi Grad Sarajevo | Alipašin Most I | 331 | 24,729.000 | 74.700 | A |
| 891ef45831bffff | Stari Grad Sarajevo | Sedrenik | 193 | 14,454.700 | 74.900 | B |
| 891ef459107ffff | Novo Sarajevo | Grbavica I | 1430 | 107,197.100 | 75.000 | B |
| 891ef45911bffff | Novo Sarajevo | Grbavica II | 1711 | 128,466.200 | 75.100 | B |
| 891ef459017ffff | Novo Sarajevo | Kvadrant | 1524 | 114,469.900 | 75.100 | B |
| 891ef459427ffff | Novi Grad Sarajevo | Dolac | 434 | 32,612.100 | 75.100 | A |
| 891ea92c853ffff | Novi Grad Sarajevo | Dobroševići | 11 | 826.800 | 75.200 | A |
| 891ef45962bffff | Novi Grad Sarajevo | Alipašino Polje BII | 2114 | 159,173.600 | 75.300 | A |
| 891ea92cdb3ffff | Novi Grad Sarajevo | Reljevo | 47 | 3,541.400 | 75.300 | A |
| 891ef4592d3ffff | Novi Grad Sarajevo | Saraj Polje | 662 | 49,935.300 | 75.400 | A |
| 891ef458243ffff | Centar Sarajevo | Velešići | 621 | 46,890.100 | 75.500 | B |
| 891ea92cd63ffff | Novi Grad Sarajevo | Zabrđe | 70 | 5,302.400 | 75.700 | A |
| 891ef4594cbffff | Novi Grad Sarajevo | Zabrđe | 41 | 3,106.400 | 75.800 | A |
| 891ef459557ffff | Novi Grad Sarajevo | Dolac | 88 | 6,671.800 | 75.800 | A |
| 891ef45847bffff | Centar Sarajevo | nan | 41 | 3,117.400 | 76.000 | B |
| 891ea92cdb7ffff | Novi Grad Sarajevo | Reljevo | 77 | 5,856.300 | 76.100 | A |
| 891ef4591abffff | Novo Sarajevo | Kovačići | 1509 | 115,010.900 | 76.200 | B |
| 891ef458303ffff | Stari Grad Sarajevo | Mošćanica | 147 | 11,221.200 | 76.300 | B |
| 891ef459113ffff | Novo Sarajevo | Grbavica I | 1800 | 137,417.900 | 76.300 | B |
| 891ef459037ffff | Novo Sarajevo | Hrasno | 1631 | 124,737.300 | 76.500 | B |
| 891ef4595c3ffff | Novi Grad Sarajevo | Dolac | 15 | 1,148.900 | 76.600 | A |
| 891ef4591cbffff | Novo Sarajevo | Trg heroja | 1857 | 142,389.000 | 76.700 | B |
| 891ef4591c7ffff | Novo Sarajevo | Željeznička | 1523 | 116,797.800 | 76.700 | B |
| 891ef4586b3ffff | Centar Sarajevo | nan | 77 | 5,907.000 | 76.700 | B |
| 891ef45b647ffff | Novi Grad Sarajevo | Reljevo | 14 | 1,075.200 | 76.800 | A |
| 891ef458e97ffff | Stari Grad Sarajevo | Mošćanica | 16 | 1,229.700 | 76.900 | B |
| 891ef459093ffff | Novi Grad Sarajevo | Dolac | 1038 | 79,897.000 | 77.000 | A |
| 891ef45b2cfffff | Novi Grad Sarajevo | Zabrđe | 394 | 30,367.700 | 77.100 | A |
| 891ef459cc3ffff | Centar Sarajevo | nan | 482 | 37,194.900 | 77.200 | B |
| 891ef459257ffff | Novi Grad Sarajevo | Dobrinja B | 646 | 49,878.100 | 77.200 | A |
| 891ef458367ffff | Stari Grad Sarajevo | Mošćanica | 158 | 12,246.900 | 77.500 | B |
| 891ef458647ffff | Centar Sarajevo | nan | 300 | 23,290.200 | 77.600 | B |
| 891ea92c90fffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 376 | 29,192.200 | 77.600 | A |
| 891ef45868bffff | Centar Sarajevo | nan | 21 | 1,632.700 | 77.700 | B |
| 891ef45960bffff | Novi Grad Sarajevo | Briješće | 12 | 933.100 | 77.800 | A |
| 891ef45830bffff | Stari Grad Sarajevo | Vratnik | 165 | 12,835.700 | 77.800 | B |
| 891ef458443ffff | Centar Sarajevo | nan | 38 | 2,957.300 | 77.800 | B |
| 891ea92eb73ffff | Novi Grad Sarajevo | Dobroševići | 15 | 1,169.200 | 77.900 | A |
| 891ef45b22fffff | Novi Grad Sarajevo | Zabrđe | 21 | 1,637.100 | 78.000 | A |
| 891ef45942fffff | Novi Grad Sarajevo | Dolac | 742 | 57,860.000 | 78.000 | A |
| 891ef459cb7ffff | Stari Grad Sarajevo | Babića bašča | 374 | 29,187.900 | 78.000 | B |
| 891ef459663ffff | Novi Grad Sarajevo | Saraj Polje | 172 | 13,452.800 | 78.200 | A |
| 891ef4590a7ffff | Novo Sarajevo | Pofalići II | 1557 | 121,846.900 | 78.300 | B |
| 891ef45804fffff | Centar Sarajevo | nan | 226 | 17,688.400 | 78.300 | B |
| 891ef45966bffff | Novi Grad Sarajevo | Saraj Polje | 238 | 18,628.000 | 78.300 | A |
| 891ef4581cbffff | Stari Grad Sarajevo | Mošćanica | 48 | 3,758.700 | 78.300 | B |
| 891ea92ccd7ffff | Novi Grad Sarajevo | Dobroševići | 29 | 2,272.500 | 78.400 | A |
| 891ef45848fffff | Centar Sarajevo | nan | 40 | 3,155.800 | 78.900 | B |
| 891ea92eb2fffff | Novi Grad Sarajevo | Reljevo | 11 | 868.600 | 79.000 | A |
| 891ef459013ffff | Novi Grad Sarajevo | Alipašin Most III | 1442 | 113,971.900 | 79.000 | A |
| 891ef4595d3ffff | Novi Grad Sarajevo | Dolac | 31 | 2,452.900 | 79.100 | A |
| 891ea92cda7ffff | Novi Grad Sarajevo | Reljevo | 127 | 10,049.800 | 79.100 | A |
| 891ef459277ffff | Novi Grad Sarajevo | Dobrinja B | 1039 | 82,337.300 | 79.200 | A |
| 891ef45901bffff | Novi Grad Sarajevo | Alipašin Most III | 924 | 73,248.100 | 79.300 | A |
| 891ea92c913ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 282 | 22,454.700 | 79.600 | A |
| 891ef45b64fffff | Novi Grad Sarajevo | Reljevo | 29 | 2,315.000 | 79.800 | A |
| 891ef458063ffff | Centar Sarajevo | Sedrenik | 54 | 4,324.400 | 80.100 | B |
| 891ef459c53ffff | Centar Sarajevo | Širokača | 111 | 8,890.400 | 80.100 | B |
| 891ea92cdafffff | Novi Grad Sarajevo | Reljevo | 20 | 1,604.200 | 80.200 | A |
| 891ef458637ffff | Centar Sarajevo | nan | 60 | 4,819.400 | 80.300 | B |
| 891ef458ed3ffff | Stari Grad Sarajevo | Mošćanica | 52 | 4,177.300 | 80.300 | B |
| 891ef45836bffff | Stari Grad Sarajevo | Vratnik | 144 | 11,570.700 | 80.400 | B |
| 891ef459c27ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 54 | 4,366.300 | 80.900 | B |
| 891ef459137ffff | Centar Sarajevo | Gornji Kovačići | 392 | 31,773.900 | 81.100 | B |
| 891ef458163ffff | Stari Grad Sarajevo | Mošćanica | 41 | 3,323.400 | 81.100 | B |
| 891ea92eb77ffff | Novi Grad Sarajevo | Dobroševići | 20 | 1,623.500 | 81.200 | A |
| 891ef45942bffff | Novi Grad Sarajevo | Dolac | 724 | 58,771.000 | 81.200 | A |
| 891ea92cd77ffff | Novi Grad Sarajevo | Zabrđe | 429 | 34,824.900 | 81.200 | A |
| 891ef45b167ffff | Centar Sarajevo | nan | 11 | 893.500 | 81.200 | B |
| 891ea92c8b3ffff | Novi Grad Sarajevo | Dobroševići | 77 | 6,259.600 | 81.300 | A |
| 891ef45961bffff | Novi Grad Sarajevo | Briješće | 304 | 24,714.800 | 81.300 | A |
| 891ef45864fffff | Centar Sarajevo | nan | 349 | 28,386.600 | 81.300 | B |
| 891ef45b12bffff | Centar Sarajevo | nan | 37 | 3,010.700 | 81.400 | B |
| 891ef459453ffff | Novi Grad Sarajevo | Briješće | 46 | 3,743.600 | 81.400 | A |
| 891ef4591d3ffff | Novo Sarajevo | Malta | 2411 | 196,241.500 | 81.400 | B |
| 891ef4584cbffff | Centar Sarajevo | nan | 45 | 3,664.400 | 81.400 | B |
| 891ef459cabffff | Stari Grad Sarajevo | Mahmutovac | 459 | 37,469.100 | 81.600 | B |
| 891ea92c903ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 338 | 27,604.300 | 81.700 | A |
| 891ef4582afffff | Centar Sarajevo | nan | 482 | 39,472.500 | 81.900 | B |
| 891ef458207ffff | Centar Sarajevo | nan | 494 | 40,542.800 | 82.100 | B |
| 891ef4592c7ffff | Novi Grad Sarajevo | Dobrinja A | 722 | 59,271.300 | 82.100 | A |
| 891ef45807bffff | Centar Sarajevo | nan | 156 | 12,807.800 | 82.100 | B |
| 891ea92cd83ffff | Novi Grad Sarajevo | Reljevo | 38 | 3,121.900 | 82.200 | A |
| 891ef4591d7ffff | Novo Sarajevo | Željeznička | 1975 | 162,662.100 | 82.400 | B |
| 891ea92cd23ffff | Novi Grad Sarajevo | Zabrđe | 417 | 34,351.000 | 82.400 | A |
| 891ea92cdbbffff | Novi Grad Sarajevo | Reljevo | 69 | 5,685.000 | 82.400 | A |
| 891ef459dd7ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 76 | 6,268.400 | 82.500 | B |
| 891ef45834fffff | Stari Grad Sarajevo | Vratnik | 494 | 40,784.600 | 82.600 | B |
| 891ef458317ffff | Stari Grad Sarajevo | Mošćanica | 158 | 13,053.900 | 82.600 | B |
| 891ef45955bffff | Novi Grad Sarajevo | Dolac | 861 | 71,276.600 | 82.800 | A |
| 891ef45836fffff | Stari Grad Sarajevo | Babića bašča | 31 | 2,566.800 | 82.800 | B |
| 891ea92c96bffff | Novi Grad Sarajevo | Briješće | 93 | 7,702.900 | 82.800 | A |
| 891ef458057ffff | Centar Sarajevo | nan | 103 | 8,531.400 | 82.800 | B |
| 891ef45805bffff | Centar Sarajevo | nan | 301 | 24,937.800 | 82.800 | B |
| 891ea92cd03ffff | Novi Grad Sarajevo | Reljevo | 29 | 2,403.300 | 82.900 | A |
| 891ef458453ffff | Centar Sarajevo | nan | 64 | 5,304.600 | 82.900 | B |
| 891ef458683ffff | Centar Sarajevo | nan | 66 | 5,473.700 | 82.900 | B |
| 891ef45848bffff | Centar Sarajevo | nan | 71 | 5,896.600 | 83.100 | B |
| 891ef459c0fffff | Stari Grad Sarajevo | Toka-Džeka | 264 | 21,936.400 | 83.100 | B |
| 891ea92cdc3ffff | Novi Grad Sarajevo | Dobroševići | 48 | 3,989.500 | 83.100 | A |
| 891ef459423ffff | Novi Grad Sarajevo | Dolac | 583 | 48,465.900 | 83.100 | A |
| 891ef458663ffff | Centar Sarajevo | nan | 497 | 41,353.900 | 83.200 | B |
| 891ef4590c7ffff | Novi Grad Sarajevo | Alipašin Most III | 1003 | 83,492.100 | 83.200 | A |
| 891ef459c1bffff | Stari Grad Sarajevo | Širokača | 328 | 27,328.600 | 83.300 | B |
| 891ea92cd93ffff | Novi Grad Sarajevo | Dobroševići | 29 | 2,424.400 | 83.600 | A |
| 891ef45ae1bffff | Stari Grad Sarajevo | Mošćanica | 13 | 1,087.300 | 83.600 | B |
| 891ef458edbffff | Stari Grad Sarajevo | Mošćanica | 23 | 1,925.800 | 83.700 | B |
| 891ef458e93ffff | Stari Grad Sarajevo | Mošćanica | 69 | 5,778.000 | 83.700 | B |
| 891ef45b127ffff | Centar Sarajevo | nan | 32 | 2,682.000 | 83.800 | B |
| 891ef459603ffff | Novi Grad Sarajevo | Briješće | 290 | 24,312.900 | 83.800 | A |
| 891ef459003ffff | Novi Grad Sarajevo | Alipašin Most III | 1809 | 151,830.200 | 83.900 | A |
| 891ef6965b7ffff | Novi Grad Sarajevo | Saraj Polje | 91 | 7,652.800 | 84.100 | A |
| 891ef45968fffff | Novi Grad Sarajevo | Briješće | 353 | 29,698.200 | 84.100 | A |
| 891ea92cd07ffff | Novi Grad Sarajevo | Reljevo | 157 | 13,208.800 | 84.100 | A |
| 891ef459c8fffff | Stari Grad Sarajevo | Bistrik | 622 | 52,385.300 | 84.200 | B |
| 891ef459ccfffff | Centar Sarajevo | Širokača | 344 | 29,045.600 | 84.400 | B |
| 891ea92cda3ffff | Novi Grad Sarajevo | Reljevo | 154 | 13,007.900 | 84.500 | A |
| 891ef459d17ffff | Stari Grad Sarajevo | Mošćanica | 95 | 8,027.200 | 84.500 | B |
| 891ef459c73ffff | Stari Grad Sarajevo | Širokača | 59 | 4,996.700 | 84.700 | B |
| 891ef458147ffff | Stari Grad Sarajevo | Mošćanica | 29 | 2,456.400 | 84.700 | B |
| 891ef4591a7ffff | Centar Sarajevo | nan | 536 | 45,490.100 | 84.900 | B |
| 891ef45a267ffff | Centar Sarajevo | nan | 19 | 1,613.000 | 84.900 | B |
| 891ef45969bffff | Novi Grad Sarajevo | Briješće | 400 | 34,006.100 | 85.000 | A |
| 891ef459dc3ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 204 | 17,376.200 | 85.200 | B |
| 891ea92cd43ffff | Novi Grad Sarajevo | Dobroševići | 130 | 11,074.900 | 85.200 | A |
| 891ef458307ffff | Stari Grad Sarajevo | Mošćanica | 216 | 18,447.000 | 85.400 | B |
| 891ef458643ffff | Centar Sarajevo | nan | 190 | 16,261.800 | 85.600 | B |
| 891ef45867bffff | Centar Sarajevo | nan | 498 | 42,625.000 | 85.600 | B |
| 891ef4583c3ffff | Stari Grad Sarajevo | Sedrenik | 407 | 34,837.400 | 85.600 | B |
| 891ef459c17ffff | Stari Grad Sarajevo | Bistrik | 579 | 49,634.200 | 85.700 | B |
| 891ea92cd0bffff | Novi Grad Sarajevo | Dobroševići | 60 | 5,151.000 | 85.900 | A |
| 891ef459677ffff | Novi Grad Sarajevo | Saraj Polje | 70 | 6,012.200 | 85.900 | A |
| 891ef458667ffff | Centar Sarajevo | nan | 148 | 12,718.200 | 85.900 | B |
| 891ef458573ffff | Centar Sarajevo | Mošćanica | 16 | 1,376.100 | 86.000 | B |
| 891ef459dc7ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 83 | 7,143.100 | 86.100 | B |
| 891ea92c94bffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 34 | 2,933.000 | 86.300 | A |
| 891ef458103ffff | Stari Grad Sarajevo | Mošćanica | 25 | 2,160.200 | 86.400 | B |
| 891ef458167ffff | Stari Grad Sarajevo | Mošćanica | 90 | 7,784.800 | 86.500 | B |
| 891ef459ca3ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 572 | 49,478.200 | 86.500 | B |
| 891ef459cdbffff | Centar Sarajevo | nan | 564 | 48,843.100 | 86.600 | B |
| 891ef4583bbffff | Stari Grad Sarajevo | Mošćanica | 84 | 7,275.800 | 86.600 | B |
| 891ef458417ffff | Centar Sarajevo | nan | 41 | 3,552.300 | 86.600 | B |
| 891ea92cd0fffff | Novi Grad Sarajevo | Reljevo | 195 | 16,903.200 | 86.700 | A |
| 891ef4582bbffff | Centar Sarajevo | nan | 535 | 46,380.100 | 86.700 | B |
| 891ea92c893ffff | Novi Grad Sarajevo | Dobroševići | 87 | 7,547.800 | 86.800 | A |
| 891ef458547ffff | Centar Sarajevo | nan | 42 | 3,645.200 | 86.800 | B |
| 891ef45826bffff | Centar Sarajevo | nan | 723 | 62,761.900 | 86.800 | B |
| 891ef4583afffff | Stari Grad Sarajevo | Mošćanica | 145 | 12,607.700 | 86.900 | B |
| 891ea92c923ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 280 | 24,351.400 | 87.000 | A |
| 891ef459c13ffff | Stari Grad Sarajevo | Širokača | 622 | 54,262.500 | 87.200 | B |
| 891ea92c92bffff | Novi Grad Sarajevo | Briješće | 257 | 22,432.400 | 87.300 | A |
| 891ef458273ffff | Centar Sarajevo | nan | 754 | 65,835.600 | 87.300 | B |
| 891ef45b36fffff | Novi Grad Sarajevo | Dolac | 16 | 1,397.700 | 87.400 | A |
| 891ef458077ffff | Centar Sarajevo | Sedrenik | 23 | 2,010.900 | 87.400 | B |
| 891ef458473ffff | Centar Sarajevo | nan | 39 | 3,416.600 | 87.600 | B |
| 891ef4592c3ffff | Novi Grad Sarajevo | Dobrinja A | 881 | 77,267.200 | 87.700 | A |
| 891ef4583d7ffff | Stari Grad Sarajevo | Sedrenik | 275 | 24,127.900 | 87.700 | B |
| 891ea92cd87ffff | Novi Grad Sarajevo | Reljevo | 78 | 6,844.400 | 87.700 | A |
| 891ef4592cbffff | Novi Grad Sarajevo | Dobrinja A | 327 | 28,696.100 | 87.800 | A |
| 891ef45811bffff | Stari Grad Sarajevo | Mošćanica | 37 | 3,247.200 | 87.800 | B |
| 891ef458327ffff | Stari Grad Sarajevo | Mošćanica | 30 | 2,633.500 | 87.800 | B |
| 891ef4580cbffff | Centar Sarajevo | nan | 164 | 14,431.300 | 88.000 | B |
| 891ef45869bffff | Centar Sarajevo | nan | 15 | 1,320.100 | 88.000 | B |
| 891ef4580c3ffff | Centar Sarajevo | nan | 133 | 11,706.000 | 88.000 | B |
| 891ef4583cfffff | Stari Grad Sarajevo | Medrese | 454 | 39,960.500 | 88.000 | B |
| 891ef4583dbffff | Stari Grad Sarajevo | Sedrenik | 479 | 42,281.500 | 88.300 | B |
| 891ea92c933ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 295 | 26,054.800 | 88.300 | A |
| 891ef4580dbffff | Centar Sarajevo | nan | 118 | 10,423.000 | 88.300 | B |
| 891ef4586b7ffff | Centar Sarajevo | nan | 124 | 10,976.900 | 88.500 | B |
| 891ef459c57ffff | Stari Grad Sarajevo | Širokača | 183 | 16,223.500 | 88.700 | B |
| 891ef458693ffff | Centar Sarajevo | nan | 95 | 8,426.200 | 88.700 | B |
| 891ef45804bffff | Centar Sarajevo | nan | 386 | 34,288.800 | 88.800 | B |
| 891ea92ea2bffff | Novi Grad Sarajevo | Dobroševići | 10 | 888.700 | 88.900 | A |
| 891ef458333ffff | Stari Grad Sarajevo | Mošćanica | 124 | 11,029.400 | 88.900 | B |
| 891ef459607ffff | Novi Grad Sarajevo | Saraj Polje | 595 | 52,926.400 | 89.000 | A |
| 891ea92cd33ffff | Novi Grad Sarajevo | Reljevo | 93 | 8,273.200 | 89.000 | A |
| 891ea92cb97ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 21 | 1,869.400 | 89.000 | A |
| 891ef4592dbffff | Novi Grad Sarajevo | Dobrinja A | 793 | 70,657.000 | 89.100 | A |
| 891ef458457ffff | Centar Sarajevo | nan | 26 | 2,316.800 | 89.100 | B |
| 891ea92c917ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 476 | 42,443.800 | 89.200 | A |
| 891ef45866fffff | Centar Sarajevo | nan | 330 | 29,458.200 | 89.300 | B |
| 891ef459c37ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 211 | 18,836.300 | 89.300 | B |
| 891ef458237ffff | Centar Sarajevo | Logavina | 622 | 55,542.500 | 89.300 | B |
| 891ea92cc6fffff | Novi Grad Sarajevo | Dobroševići | 112 | 10,002.600 | 89.300 | A |
| 891ef4582c7ffff | Centar Sarajevo | nan | 639 | 57,072.400 | 89.300 | B |
| 891ef459817ffff | Stari Grad Sarajevo | Širokača | 22 | 1,965.900 | 89.400 | B |
| 891ef458ed7ffff | Stari Grad Sarajevo | Mošćanica | 50 | 4,477.200 | 89.500 | B |
| 891ea92c977ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 529 | 47,409.100 | 89.600 | A |
| 891ef459ccbffff | Centar Sarajevo | nan | 526 | 47,140.300 | 89.600 | B |
| 891ef458067ffff | Stari Grad Sarajevo | Sedrenik | 24 | 2,151.000 | 89.600 | B |
| 891ea92cc87ffff | Novi Grad Sarajevo | Dobroševići | 36 | 3,228.400 | 89.700 | A |
| 891ef458313ffff | Stari Grad Sarajevo | Sedrenik | 300 | 26,909.600 | 89.700 | B |
| 891ef458447ffff | Centar Sarajevo | nan | 31 | 2,784.600 | 89.800 | B |
| 891ef459c03ffff | Stari Grad Sarajevo | Toka-Džeka | 472 | 42,408.400 | 89.800 | B |
| 891ef45845bffff | Centar Sarajevo | nan | 12 | 1,078.300 | 89.900 | B |
| 891ef458213ffff | Centar Sarajevo | nan | 652 | 58,628.700 | 89.900 | B |
| 891ea92cc33ffff | Novi Grad Sarajevo | Dobroševići | 89 | 8,023.300 | 90.100 | A |
| 891ef459693ffff | Novi Grad Sarajevo | Briješće | 439 | 39,596.000 | 90.200 | A |
| 891ea92c92fffff | Novi Grad Sarajevo | Briješće | 333 | 30,072.900 | 90.300 | A |
| 891ef458497ffff | Centar Sarajevo | nan | 38 | 3,432.700 | 90.300 | B |
| 891ea92cc2fffff | Novi Grad Sarajevo | Dobroševići | 132 | 11,938.100 | 90.400 | A |
| 891ea92c93bffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 418 | 37,836.400 | 90.500 | A |
| 891ef458357ffff | Stari Grad Sarajevo | Sumbuluša | 467 | 42,282.500 | 90.500 | B |
| 891ea92c883ffff | Novi Grad Sarajevo | Dobroševići | 147 | 13,326.000 | 90.700 | A |
| 891ea92cc77ffff | Novi Grad Sarajevo | Dobroševići | 75 | 6,813.300 | 90.800 | A |
| 891ea92c967ffff | Novi Grad Sarajevo | Briješće | 503 | 45,734.400 | 90.900 | A |
| 891ef45820fffff | Centar Sarajevo | nan | 755 | 68,719.700 | 91.000 | B |
| 891ef458037ffff | Stari Grad Sarajevo | Mošćanica | 39 | 3,554.400 | 91.100 | B |
| 891ea92cc8fffff | Novi Grad Sarajevo | Dobroševići | 46 | 4,195.000 | 91.200 | A |
| 891ef458c5bffff | Stari Grad Sarajevo | Mošćanica | 38 | 3,466.000 | 91.200 | B |
| 891ef458013ffff | Centar Sarajevo | nan | 47 | 4,307.100 | 91.600 | B |
| 891ef458507ffff | Stari Grad Sarajevo | Mošćanica | 19 | 1,742.100 | 91.700 | B |
| 891ef459683ffff | Novi Grad Sarajevo | Briješće | 540 | 49,550.200 | 91.800 | A |
| 891ea92c897ffff | Novi Grad Sarajevo | Dobroševići | 59 | 5,414.600 | 91.800 | A |
| 891ef45945bffff | Novi Grad Sarajevo | Briješće | 336 | 30,868.500 | 91.900 | A |
| 891ef459497ffff | Novi Grad Sarajevo | Zabrđe | 46 | 4,228.300 | 91.900 | A |
| 891ef4584c7ffff | Centar Sarajevo | nan | 52 | 4,787.500 | 92.100 | B |
| 891ef459697ffff | Novi Grad Sarajevo | Briješće | 435 | 40,050.300 | 92.100 | A |
| 891ef458283ffff | Centar Sarajevo | nan | 455 | 41,924.300 | 92.100 | B |
| 891ef458603ffff | Centar Sarajevo | nan | 15 | 1,382.900 | 92.200 | B |
| 891ef4591b3ffff | Centar Sarajevo | Željeznička | 873 | 80,588.400 | 92.300 | B |
| 891ef45846fffff | Centar Sarajevo | nan | 125 | 11,549.700 | 92.400 | B |
| 891ef45868fffff | Centar Sarajevo | nan | 66 | 6,100.400 | 92.400 | B |
| 891ea92eb0fffff | Novi Grad Sarajevo | Dobroševići | 21 | 1,944.300 | 92.600 | A |
| 891ef458687ffff | Centar Sarajevo | nan | 127 | 11,763.600 | 92.600 | B |
| 891ef4584cfffff | Centar Sarajevo | nan | 45 | 4,168.500 | 92.600 | B |
| 891ef45816fffff | Stari Grad Sarajevo | Mošćanica | 40 | 3,708.900 | 92.700 | B |
| 891ea92c88fffff | Novi Grad Sarajevo | Dobroševići | 196 | 18,179.200 | 92.800 | A |
| 891ef4583cbffff | Stari Grad Sarajevo | Medrese | 628 | 58,286.900 | 92.800 | B |
| 891ea92cc2bffff | Novi Grad Sarajevo | Dobroševići | 116 | 10,794.400 | 93.100 | A |
| 891ea92cd1bffff | Novi Grad Sarajevo | Dobroševići | 21 | 1,954.900 | 93.100 | A |
| 891ef45814fffff | Stari Grad Sarajevo | Mošćanica | 69 | 6,426.200 | 93.100 | B |
| 891ef459c07ffff | Stari Grad Sarajevo | Toka-Džeka | 443 | 41,293.900 | 93.200 | B |
| 891ef458043ffff | Centar Sarajevo | nan | 290 | 27,115.000 | 93.500 | B |
| 891ef459687ffff | Novi Grad Sarajevo | Briješće | 537 | 50,222.100 | 93.500 | A |
| 891ea92c9c3ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 179 | 16,749.000 | 93.600 | A |
| 891ef4582a3ffff | Centar Sarajevo | nan | 538 | 50,343.300 | 93.600 | B |
| 891ea92c837ffff | Novi Grad Sarajevo | Dobroševići | 89 | 8,329.200 | 93.600 | A |
| 891ea92cc23ffff | Novi Grad Sarajevo | Dobroševići | 139 | 13,026.500 | 93.700 | A |
| 891ef459cb3ffff | Stari Grad Sarajevo | Babića bašča | 834 | 78,299.100 | 93.900 | B |
| 891ef45aa53ffff | Stari Grad Sarajevo | Mošćanica | 21 | 1,972.000 | 93.900 | B |
| 891ef4583a3ffff | Stari Grad Sarajevo | Mošćanica | 260 | 24,490.200 | 94.200 | B |
| 891ea92cd53ffff | Novi Grad Sarajevo | Dobroševići | 147 | 13,860.200 | 94.300 | A |
| 891ef4591b7ffff | Centar Sarajevo | nan | 814 | 76,756.600 | 94.300 | B |
| 891ef45834bffff | Stari Grad Sarajevo | Kovači | 925 | 87,324.500 | 94.400 | B |
| 891ea92cd4fffff | Novi Grad Sarajevo | Dobroševići | 211 | 19,923.400 | 94.400 | A |
| 891ef459c8bffff | Stari Grad Sarajevo | Mjedenica | 820 | 77,474.500 | 94.500 | B |
| 891ef459667ffff | Novi Grad Sarajevo | Saraj Polje | 1343 | 127,024.300 | 94.600 | A |
| 891ea92cbbbffff | Novi Grad Sarajevo | Briješće | 28 | 2,650.000 | 94.600 | A |
| 891ea92c907ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 521 | 49,418.400 | 94.900 | A |
| 891ef458227ffff | Stari Grad Sarajevo | Logavina | 857 | 81,292.800 | 94.900 | B |
| 891ef4581b3ffff | Stari Grad Sarajevo | Mošćanica | 27 | 2,564.700 | 95.000 | B |
| 891ef458217ffff | Centar Sarajevo | nan | 670 | 63,653.400 | 95.000 | B |
| 891ef459c0bffff | Stari Grad Sarajevo | Širokača | 366 | 34,789.700 | 95.100 | B |
| 891ef458247ffff | Centar Sarajevo | nan | 839 | 79,813.000 | 95.100 | B |
| 891ea92c8c3ffff | Novi Grad Sarajevo | Dobroševići | 62 | 5,898.600 | 95.100 | A |
| 891ea92cc13ffff | Novi Grad Sarajevo | Dobroševići | 64 | 6,090.800 | 95.200 | A |
| 891ef458403ffff | Centar Sarajevo | nan | 74 | 7,044.200 | 95.200 | B |
| 891ef458677ffff | Centar Sarajevo | nan | 159 | 15,137.600 | 95.200 | B |
| 891ea92c8c7ffff | Novi Grad Sarajevo | Dobroševići | 143 | 13,636.300 | 95.400 | A |
| 891ef45838bffff | Stari Grad Sarajevo | Sedrenik | 235 | 22,441.800 | 95.500 | B |
| 891ef4582cfffff | Centar Sarajevo | Velešići | 1025 | 97,943.700 | 95.600 | B |
| 891ef458413ffff | Centar Sarajevo | nan | 119 | 11,382.400 | 95.700 | B |
| 891ea92c823ffff | Novi Grad Sarajevo | Dobroševići | 37 | 3,539.700 | 95.700 | A |
| 891ef4583abffff | Stari Grad Sarajevo | Mošćanica | 309 | 29,611.100 | 95.800 | B |
| 891ea92cc0bffff | Novi Grad Sarajevo | Dobroševići | 47 | 4,504.000 | 95.800 | A |
| 891ef45822fffff | Stari Grad Sarajevo | Logavina | 952 | 91,265.400 | 95.900 | B |
| 891ef458293ffff | Centar Sarajevo | nan | 178 | 17,066.300 | 95.900 | B |
| 891ef459c33ffff | Stari Grad Sarajevo | Mahmutovac | 280 | 26,848.100 | 95.900 | B |
| 891ea92cc27ffff | Novi Grad Sarajevo | Dobroševići | 239 | 22,927.100 | 95.900 | A |
| 891ef45812fffff | Stari Grad Sarajevo | Mošćanica | 88 | 8,441.800 | 95.900 | B |
| 891ef459dcfffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 153 | 14,695.200 | 96.000 | B |
| 891ea92c927ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 276 | 26,556.200 | 96.200 | A |
| 891ef458353ffff | Stari Grad Sarajevo | Medrese | 817 | 78,637.300 | 96.300 | B |
| 891ef458003ffff | Centar Sarajevo | nan | 35 | 3,370.800 | 96.300 | B |
| 891ea92eb4bffff | Novi Grad Sarajevo | Dobroševići | 17 | 1,637.300 | 96.300 | A |
| 891ef459cbbffff | Stari Grad Sarajevo | Bistrik | 826 | 79,576.500 | 96.300 | B |
| 891ef4594bbffff | Novi Grad Sarajevo | Dolac | 15 | 1,445.200 | 96.300 | A |
| 891ef4583c7ffff | Stari Grad Sarajevo | Sedrenik | 421 | 40,600.500 | 96.400 | B |
| 891ef4583d3ffff | Centar Sarajevo | Sedrenik | 442 | 42,629.200 | 96.400 | B |
| 891ef458657ffff | Centar Sarajevo | nan | 51 | 4,923.700 | 96.500 | B |
| 891ef458e8bffff | Stari Grad Sarajevo | Mošćanica | 24 | 2,317.600 | 96.600 | B |
| 891ea92cc03ffff | Novi Grad Sarajevo | Dobroševići | 54 | 5,215.100 | 96.600 | A |
| 891ef4583b3ffff | Stari Grad Sarajevo | Mošćanica | 168 | 16,234.100 | 96.600 | B |
| 891ea92ceb7ffff | Novi Grad Sarajevo | Dobroševići | 14 | 1,353.600 | 96.700 | A |
| 891ea92cd47ffff | Novi Grad Sarajevo | Dobroševići | 202 | 19,543.300 | 96.700 | A |
| 891ef459d1bffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 116 | 11,235.300 | 96.900 | B |
| 891ef45849bffff | Centar Sarajevo | nan | 28 | 2,715.700 | 97.000 | B |
| 891ea92cc3bffff | Novi Grad Sarajevo | Dobroševići | 101 | 9,799.100 | 97.000 | A |
| 891ef459d0bffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 14 | 1,358.600 | 97.000 | B |
| 891ef45817bffff | Stari Grad Sarajevo | Mošćanica | 164 | 15,917.800 | 97.100 | B |
| 891ef458223ffff | Centar Sarajevo | Logavina | 860 | 83,502.400 | 97.100 | B |
| 891ea92cc63ffff | Novi Grad Sarajevo | Dobroševići | 86 | 8,354.900 | 97.100 | A |
| 891ea92cca7ffff | Novi Grad Sarajevo | Dobroševići | 63 | 6,121.400 | 97.200 | A |
| 891ef45812bffff | Stari Grad Sarajevo | Mošćanica | 51 | 4,967.700 | 97.400 | B |
| 891ea92cd4bffff | Novi Grad Sarajevo | Dobroševići | 176 | 17,146.200 | 97.400 | A |
| 891ef45803bffff | Stari Grad Sarajevo | Mošćanica | 63 | 6,139.100 | 97.400 | B |
| 891ea92ccbbffff | Novi Grad Sarajevo | Dobroševići | 26 | 2,533.800 | 97.500 | A |
| 891ef458343ffff | Stari Grad Sarajevo | Kovači | 894 | 87,211.200 | 97.600 | B |
| 891ea92c8cfffff | Novi Grad Sarajevo | Dobroševići | 100 | 9,755.700 | 97.600 | A |
| 891ef45ae13ffff | Stari Grad Sarajevo | Mošćanica | 10 | 978.200 | 97.800 | B |
| 891ef4592cfffff | Novi Grad Sarajevo | Dobrinja A | 1086 | 106,253.300 | 97.800 | A |
| 891ef4584abffff | Centar Sarajevo | nan | 21 | 2,055.300 | 97.900 | B |
| 891ef45816bffff | Stari Grad Sarajevo | Mošćanica | 105 | 10,283.900 | 97.900 | B |
| 891ea92eb13ffff | Novi Grad Sarajevo | Dobroševići | 19 | 1,861.000 | 97.900 | A |
| 891ef458233ffff | Centar Sarajevo | nan | 817 | 80,245.600 | 98.200 | B |
| 891ef459d53ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 47 | 4,620.700 | 98.300 | B |
| 891ea92cc0fffff | Novi Grad Sarajevo | Dobroševići | 64 | 6,298.000 | 98.400 | A |
| 891ea92c88bffff | Novi Grad Sarajevo | Dobroševići | 275 | 27,069.100 | 98.400 | A |
| 891ef4581bbffff | Stari Grad Sarajevo | Mošćanica | 12 | 1,181.300 | 98.400 | B |
| 891ea92c887ffff | Novi Grad Sarajevo | Dobroševići | 192 | 18,967.000 | 98.800 | A |
| 891ef459223ffff | Novi Grad Sarajevo | Dobrinja B | 118 | 11,665.000 | 98.900 | A |
| 891ea92ccafffff | Novi Grad Sarajevo | Dobroševići | 101 | 9,987.800 | 98.900 | A |
| 891ef45827bffff | Centar Sarajevo | nan | 1002 | 99,334.100 | 99.100 | B |
| 891ea92cdcbffff | Novi Grad Sarajevo | Dobroševići | 157 | 15,595.700 | 99.300 | A |
| 891ef458347ffff | Stari Grad Sarajevo | Vratnik | 790 | 78,657.200 | 99.600 | B |
| 891ef4580bbffff | Centar Sarajevo | nan | 63 | 6,280.400 | 99.700 | B |
| 891ef458087ffff | Centar Sarajevo | nan | 15 | 1,495.500 | 99.700 | B |
| 891ef45837bffff | Stari Grad Sarajevo | Vratnik | 709 | 70,704.400 | 99.700 | B |
| 891ef45aa5bffff | Stari Grad Sarajevo | Mošćanica | 16 | 1,596.000 | 99.800 | B |
| 891ef45821bffff | Centar Sarajevo | nan | 937 | 93,498.700 | 99.800 | B |
| 891ef45835bffff | Stari Grad Sarajevo | Logavina | 1071 | 106,914.100 | 99.800 | B |
| 891ef458053ffff | Centar Sarajevo | nan | 382 | 38,141.000 | 99.800 | B |
| 891ef458297ffff | Centar Sarajevo | nan | 447 | 44,672.800 | 99.900 | B |
| 891ef4580b7ffff | Centar Sarajevo | nan | 12 | 1,199.500 | 100.000 | B |
| 891ea92ebc7ffff | Novi Grad Sarajevo | Dobroševići | 14 | 1,399.900 | 100.000 | A |
| 891ea92c89bffff | Novi Grad Sarajevo | Dobroševići | 266 | 26,654.300 | 100.200 | A |
| 891ea92ccb7ffff | Novi Grad Sarajevo | Dobroševići | 24 | 2,405.400 | 100.200 | A |
| 891ef4580b3ffff | Centar Sarajevo | nan | 89 | 8,943.200 | 100.500 | B |
| 891ef458373ffff | Stari Grad Sarajevo | Vratnik | 510 | 51,312.600 | 100.600 | B |
| 891ef45814bffff | Stari Grad Sarajevo | Mošćanica | 94 | 9,465.300 | 100.700 | B |
| 891ef458463ffff | Centar Sarajevo | nan | 78 | 7,855.300 | 100.700 | B |
| 891ef4583a7ffff | Stari Grad Sarajevo | Mošćanica | 233 | 23,492.000 | 100.800 | B |
| 891ef4582b7ffff | Centar Sarajevo | nan | 474 | 47,827.700 | 100.900 | B |
| 891ef4582a7ffff | Centar Sarajevo | nan | 574 | 57,926.900 | 100.900 | B |
| 891ef4586a7ffff | Centar Sarajevo | nan | 141 | 14,301.800 | 101.400 | B |
| 891ef45aa93ffff | Stari Grad Sarajevo | Mošćanica | 17 | 1,724.400 | 101.400 | B |
| 891ea92ccc3ffff | Novi Grad Sarajevo | Dobroševići | 27 | 2,750.600 | 101.900 | A |
| 891ea92cc37ffff | Novi Grad Sarajevo | Dobroševići | 207 | 21,092.800 | 101.900 | A |
| 891ef458483ffff | Centar Sarajevo | nan | 100 | 10,190.400 | 101.900 | B |
| 891ef458107ffff | Stari Grad Sarajevo | Mošćanica | 33 | 3,363.200 | 101.900 | B |
| 891ea92cc07ffff | Novi Grad Sarajevo | Dobroševići | 57 | 5,810.700 | 101.900 | A |
| 891ea92c91bffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 483 | 49,284.500 | 102.000 | A |
| 891ef4586afffff | Centar Sarajevo | nan | 148 | 15,143.000 | 102.300 | B |
| 891ef458287ffff | Centar Sarajevo | nan | 691 | 70,772.600 | 102.400 | B |
| 891ef4582b3ffff | Centar Sarajevo | nan | 561 | 57,554.100 | 102.600 | B |
| 891ea92cc6bffff | Novi Grad Sarajevo | Dobroševići | 55 | 5,643.100 | 102.600 | A |
| 891ea92cc17ffff | Novi Grad Sarajevo | Dobroševići | 57 | 5,848.400 | 102.600 | A |
| 891ef45822bffff | Centar Sarajevo | nan | 1087 | 111,745.900 | 102.800 | B |
| 891ef4580d3ffff | Centar Sarajevo | nan | 220 | 22,716.300 | 103.300 | B |
| 891ef45820bffff | Centar Sarajevo | nan | 1048 | 108,469.500 | 103.500 | B |
| 891ea92eb1bffff | Novi Grad Sarajevo | Dobroševići | 22 | 2,289.200 | 104.100 | A |
| 891ef4580d7ffff | Centar Sarajevo | nan | 88 | 9,157.700 | 104.100 | B |
| 891ea92eb0bffff | Novi Grad Sarajevo | Dobroševići | 12 | 1,250.700 | 104.200 | A |
| 891ef459c87ffff | Stari Grad Sarajevo | Bistrik | 1104 | 115,064.700 | 104.200 | B |
| 891ef4586a3ffff | Centar Sarajevo | nan | 194 | 20,245.600 | 104.400 | B |
| 891ef45b12fffff | Centar Sarajevo | nan | 125 | 13,054.500 | 104.400 | B |
| 891ea92c8d7ffff | Novi Grad Sarajevo | Dobroševići | 172 | 18,002.100 | 104.700 | A |
| 891ea92c9cfffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 235 | 24,630.400 | 104.800 | A |
| 891ef4583b7ffff | Stari Grad Sarajevo | Mošćanica | 291 | 30,518.100 | 104.900 | B |
| 891ef45854fffff | Centar Sarajevo | nan | 70 | 7,376.500 | 105.400 | B |
| 891ea92cd9bffff | Novi Grad Sarajevo | Dobroševići | 50 | 5,287.600 | 105.800 | A |
| 891ef45823bffff | Centar Sarajevo | nan | 1148 | 121,415.400 | 105.800 | B |
| 891ef458157ffff | Stari Grad Sarajevo | Mošćanica | 47 | 4,976.500 | 105.900 | B |
| 891ef45841bffff | Centar Sarajevo | nan | 136 | 14,451.700 | 106.300 | B |
| 891ea92eb67ffff | Novi Grad Sarajevo | Dobroševići | 32 | 3,401.100 | 106.300 | A |
| 891ea92cc7bffff | Novi Grad Sarajevo | Dobroševići | 81 | 8,616.900 | 106.400 | A |
| 891ea92cc67ffff | Novi Grad Sarajevo | Dobroševići | 254 | 27,053.100 | 106.500 | A |
| 891ef45ae0bffff | Stari Grad Sarajevo | Mošćanica | 10 | 1,065.200 | 106.500 | B |
| 891ef459c97ffff | Stari Grad Sarajevo | Baščaršija | 1375 | 146,749.400 | 106.700 | B |
| 891ea92eb53ffff | Novi Grad Sarajevo | Dobroševići | 14 | 1,496.300 | 106.900 | A |
| 891ef45828bffff | Centar Sarajevo | nan | 539 | 57,656.800 | 107.000 | B |
| 891ef45809bffff | Centar Sarajevo | nan | 43 | 4,603.500 | 107.100 | B |
| 891ef458257ffff | Centar Sarajevo | nan | 1156 | 123,801.500 | 107.100 | B |
| 891ea92eb07ffff | Novi Grad Sarajevo | Dobroševići | 18 | 1,928.700 | 107.200 | A |
| 891ea92cc73ffff | Novi Grad Sarajevo | Dobroševići | 136 | 14,589.400 | 107.300 | A |
| 891ef459cd3ffff | Centar Sarajevo | nan | 792 | 84,999.300 | 107.300 | B |
| 891ea92eb03ffff | Novi Grad Sarajevo | Dobroševići | 14 | 1,502.600 | 107.300 | A |
| 891ef45aacbffff | Stari Grad Sarajevo | Mošćanica | 19 | 2,043.500 | 107.600 | B |
| 891ef45826fffff | Centar Sarajevo | nan | 1135 | 122,078.400 | 107.600 | B |
| 891ef458263ffff | Centar Sarajevo | nan | 1280 | 137,758.200 | 107.600 | B |
| 891ef45928bffff | Novi Grad Sarajevo | Dobrinja A | 1261 | 136,013.600 | 107.900 | A |
| 891ef45802bffff | Stari Grad Sarajevo | Mošćanica | 22 | 2,373.800 | 107.900 | B |
| 891ef458577ffff | Stari Grad Sarajevo | Mošćanica | 32 | 3,454.500 | 108.000 | B |
| 891ef458277ffff | Centar Sarajevo | nan | 1255 | 135,600.800 | 108.000 | B |
| 891ea92ccc7ffff | Novi Grad Sarajevo | Dobroševići | 77 | 8,335.900 | 108.300 | A |
| 891ea92cca3ffff | Novi Grad Sarajevo | Dobroševići | 45 | 4,877.600 | 108.400 | A |
| 891ef459c93ffff | Stari Grad Sarajevo | Ferhadija | 1406 | 152,440.800 | 108.400 | B |
| 891ef45840bffff | Centar Sarajevo | nan | 71 | 7,701.500 | 108.500 | B |
| 891ea92c9c7ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 699 | 75,841.000 | 108.500 | A |
| 891ea92c8bbffff | Novi Grad Sarajevo | Dobroševići | 74 | 8,033.700 | 108.600 | A |
| 891ef458267ffff | Centar Sarajevo | nan | 1288 | 140,174.400 | 108.800 | B |
| 891ef459c83ffff | Stari Grad Sarajevo | Baščaršija | 1403 | 152,747.600 | 108.900 | B |
| 891ef458697ffff | Centar Sarajevo | nan | 137 | 14,948.000 | 109.100 | B |
| 891ef45828fffff | Centar Sarajevo | nan | 1033 | 112,797.600 | 109.200 | B |
| 891ea92c8d3ffff | Novi Grad Sarajevo | Dobroševići | 44 | 4,807.100 | 109.300 | A |
| 891ef4580c7ffff | Centar Sarajevo | nan | 10 | 1,093.300 | 109.300 | B |
| 891ef45a35bffff | Centar Sarajevo | nan | 12 | 1,313.500 | 109.500 | B |
| 891ea92ccabffff | Novi Grad Sarajevo | Dobroševići | 70 | 7,685.100 | 109.800 | A |
| 891ea92c957ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 452 | 49,636.100 | 109.800 | A |
| 891ea92c833ffff | Novi Grad Sarajevo | Dobroševići | 31 | 3,409.300 | 110.000 | A |
| 891ea92eb8fffff | Novi Grad Sarajevo | Dobroševići | 25 | 2,755.200 | 110.200 | A |
| 891ef458673ffff | Centar Sarajevo | nan | 568 | 63,093.700 | 111.100 | B |
| 891ef45850fffff | Centar Sarajevo | Mošćanica | 52 | 5,783.400 | 111.200 | B |
| 891ea92ccd3ffff | Novi Grad Sarajevo | Dobroševići | 34 | 3,786.700 | 111.400 | A |
| 891ea92c813ffff | Novi Grad Sarajevo | Dobroševići | 262 | 29,222.300 | 111.500 | A |
| 891ef459cd7ffff | Centar Sarajevo | nan | 1301 | 145,147.700 | 111.600 | B |
| 891ef458023ffff | Stari Grad Sarajevo | Mošćanica | 84 | 9,376.300 | 111.600 | B |
| 891ea92cc8bffff | Novi Grad Sarajevo | Dobroševići | 70 | 7,832.600 | 111.900 | A |
| 891ef459c9bffff | Centar Sarajevo | Ferhadija | 1477 | 165,402.600 | 112.000 | B |
| 891ea92c817ffff | Novi Grad Sarajevo | Dobroševići | 24 | 2,690.300 | 112.100 | A |
| 891ef4582abffff | Centar Sarajevo | nan | 1209 | 135,792.200 | 112.300 | B |
| 891ef45853bffff | Stari Grad Sarajevo | Mošćanica | 26 | 2,926.700 | 112.600 | B |
| 891ef4580a3ffff | Centar Sarajevo | nan | 37 | 4,174.000 | 112.800 | B |
| 891ef45aa4fffff | Stari Grad Sarajevo | Mošćanica | 23 | 2,595.000 | 112.800 | B |
| 891ef458487ffff | Centar Sarajevo | nan | 20 | 2,268.200 | 113.400 | B |
| 891ef4580abffff | Centar Sarajevo | nan | 36 | 4,099.000 | 113.900 | B |
| 891ef45a22fffff | Centar Sarajevo | nan | 28 | 3,194.600 | 114.100 | B |
| 891ef458153ffff | Stari Grad Sarajevo | Mošćanica | 16 | 1,834.100 | 114.600 | B |
| 891ea92cc1bffff | Novi Grad Sarajevo | Dobroševići | 49 | 5,626.000 | 114.800 | A |
| 891ea92c943ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 100 | 11,558.800 | 115.600 | A |
| 891ef45862fffff | Centar Sarajevo | nan | 445 | 52,296.500 | 117.500 | B |
| 891ef458187ffff | Stari Grad Sarajevo | Mošćanica | 14 | 1,663.900 | 118.800 | B |
| 891ea92ccb3ffff | Novi Grad Sarajevo | Dobroševići | 18 | 2,150.400 | 119.500 | A |
| 891ef45b177ffff | Centar Sarajevo | nan | 19 | 2,276.100 | 119.800 | B |
| 891ea92c8dbffff | Novi Grad Sarajevo | Dobroševići | 11 | 1,325.500 | 120.500 | A |
| 891ef4584c3ffff | Centar Sarajevo | nan | 18 | 2,178.900 | 121.100 | B |
| 891ea92c8cbffff | Novi Grad Sarajevo | Dobroševići | 192 | 23,268.300 | 121.200 | A |
| 891ef4580afffff | Stari Grad Sarajevo | Mošćanica | 27 | 3,336.300 | 123.600 | B |
| 891ef45a8cbffff | Stari Grad Sarajevo | Mošćanica | 19 | 2,366.900 | 124.600 | B |
| 891ea92eb87ffff | Novi Grad Sarajevo | Dobroševići | 22 | 2,747.000 | 124.900 | A |
| 891ef45aecbffff | Stari Grad Sarajevo | Mošćanica | 13 | 1,624.500 | 125.000 | B |
| 891ef45802fffff | Stari Grad Sarajevo | Mošćanica | 38 | 4,767.300 | 125.500 | B |
| 891ef45a327ffff | Stari Grad Sarajevo | Mošćanica | 12 | 1,517.600 | 126.500 | B |
| 891ef459d4bffff | Stari Grad Sarajevo | Širokača | 96 | 12,198.200 | 127.100 | B |
| 891ef45b1a7ffff | Centar Sarajevo | nan | 10 | 1,273.000 | 127.300 | B |
| 891ef4581c3ffff | Stari Grad Sarajevo | Mošćanica | 14 | 1,792.100 | 128.000 | B |
| 891ef45a22bffff | Centar Sarajevo | nan | 18 | 2,309.700 | 128.300 | B |
| 891ef45aab7ffff | Stari Grad Sarajevo | Mošćanica | 18 | 2,317.500 | 128.800 | B |

## 5. Vizuelna provjera
Stanovnici u zonama gdje ih ne bi trebalo biti (aproksimacija: ravnomjerno po dijelu polja):

| vrsta | procijenjeno_stanovnika (površinski) |
|---|---|
| aerodrom | 523.000 |
| landuse=industrial | 6,145.000 |
| park | 6,306.000 |

Najgušće MZ (od 62 sa poznatim granicama):

| rang | opcina | mz | st | st_po_km2 |
|---|---|---|---|---|
| 1 | Novi Grad Sarajevo | Dobrinja C | 2754 | 91,398.000 |
| 2 | Novi Grad Sarajevo | Alipašino Polje BII | 2617 | 24,063.000 |
| 3 | Novi Grad Sarajevo | Alipašino Polje CI | 1851 | 20,858.000 |
| 4 | Novi Grad Sarajevo | Alipašino Polje BI | 3086 | 19,358.000 |
| 5 | Novo Sarajevo | Malta | 3263 | 16,896.000 |
| 6 | Novi Grad Sarajevo | Alipašino Polje CII | 2279 | 16,249.000 |
| 7 | Novi Grad Sarajevo | Staro Hrasno | 2627 | 16,018.000 |
| 8 | Novo Sarajevo | Trg heroja | 3918 | 14,956.000 |
| 9 | Novo Sarajevo | Grbavica I | 4769 | 14,298.000 |
| 10 | Novi Grad Sarajevo | Švrakino Selo I | 1570 | 13,830.000 |
| 11 | Novo Sarajevo | Hrasno | 1450 | 13,237.000 |
| 12 | Stari Grad Sarajevo | Ferhadija | 1179 | 12,812.000 |
| 13 | Novo Sarajevo | Čengić Vila II | 1267 | 12,635.000 |
| 14 | Stari Grad Sarajevo | Baščaršija | 2462 | 12,608.000 |
| 15 | Novo Sarajevo | Grbavica II | 4782 | 12,250.000 |

Dobrinja, Alipašino Polje, Grbavica (očekivano visoko):

| rang | opcina | mz | st | st_po_km2 |
|---|---|---|---|---|
| 1 | Novi Grad Sarajevo | Dobrinja C | 2754 | 91,398.000 |
| 2 | Novi Grad Sarajevo | Alipašino Polje BII | 2617 | 24,063.000 |
| 3 | Novi Grad Sarajevo | Alipašino Polje CI | 1851 | 20,858.000 |
| 4 | Novi Grad Sarajevo | Alipašino Polje BI | 3086 | 19,358.000 |
| 6 | Novi Grad Sarajevo | Alipašino Polje CII | 2279 | 16,249.000 |
| 9 | Novo Sarajevo | Grbavica I | 4769 | 14,298.000 |
| 15 | Novo Sarajevo | Grbavica II | 4782 | 12,250.000 |
| 23 | Novi Grad Sarajevo | Alipašino Polje AII | 2361 | 9,295.000 |
| 25 | Novi Grad Sarajevo | Dobrinja D | 4892 | 9,101.000 |
| 29 | Novi Grad Sarajevo | Alipašino Polje AI | 2360 | 8,056.000 |
| 31 | Novi Grad Sarajevo | Dobrinja A | 6382 | 7,703.000 |
| 33 | Novi Grad Sarajevo | Dobrinja B | 6305 | 7,627.000 |

Karta za vizuelni pregled: `out/karta.html`.

## 6. Starosne grupe
Zbir grupa = ukupno u svakom polju: **OK** (0 polja odstupa).

Odstupanje zbira grupa po općini od FZS-a (posljedica zaokruživanja po polju):

| opcina | d0_14 | d15_64 | d65plus |
|---|---|---|---|
| Centar Sarajevo | -5 | -1 | 6 |
| Novi Grad Sarajevo | 0 | 7 | -7 |
| Novo Sarajevo | 0 | -3 | 3 |
| Stari Grad Sarajevo | -6 | 15 | -9 |

## Napomene o modelu
- **Stari Grad Sarajevo**: Graf 3 nije potvrđen; samo zbir općine
- **Novi Grad Sarajevo**: MZ: β=0.5·udio_2010 + (1−β)·udio_modela; nove MZ s matičnom: nema; bez matične: ['Alipašin Most III', 'Zabrđe']
- Pouzdanost polja: {'B': 963, 'A': 368, 'C': 60}
