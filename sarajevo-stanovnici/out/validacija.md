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
| Dobrinja C | 0.003 | 0.042 | 0.084 | model < 2010 za >30%: provjeriti |
| Švrakino Selo I | 0.004 | 0.020 | 0.195 | model < 2010 za >30%: provjeriti |
| Aneks | 0.011 | 0.028 | 0.382 | model < 2010 za >30%: provjeriti |
| Alipašino Polje CI | 0.009 | 0.023 | 0.407 | model < 2010 za >30%: provjeriti |
| Švrakino Selo III | 0.011 | 0.018 | 0.593 | model < 2010 za >30%: provjeriti |
| Alipašin Most II | 0.016 | 0.025 | 0.649 | model < 2010 za >30%: provjeriti |
| Alipašino Polje AI | 0.016 | 0.023 | 0.704 |  |
| Alipašin Most I | 0.049 | 0.067 | 0.739 |  |
| Buća Potok | 0.034 | 0.045 | 0.764 |  |
| Alipašino Polje CII | 0.019 | 0.023 | 0.828 |  |
| Olimpijsko Selo | 0.019 | 0.023 | 0.829 |  |
| Švrakino Selo II | 0.034 | 0.040 | 0.851 |  |
| Dolac | 0.043 | 0.049 | 0.877 |  |
| Dobrinja D | 0.044 | 0.047 | 0.918 |  |
| Alipašino Polje BII | 0.024 | 0.027 | 0.919 |  |
| Alipašino Polje AII | 0.022 | 0.023 | 0.955 |  |
| Čengić Vila | 0.030 | 0.031 | 0.966 |  |
| Staro Hrasno | 0.025 | 0.024 | 1.033 |  |
| Alipašino Polje BI | 0.032 | 0.029 | 1.100 |  |
| Otoka | 0.029 | 0.025 | 1.125 |  |
| Dobrinja B | 0.062 | 0.050 | 1.249 |  |
| Reljevo | 0.011 | 0.008 | 1.351 | model > 2010 za >30%: nova gradnja? |
| Saraj Polje | 0.061 | 0.041 | 1.492 | model > 2010 za >30%: nova gradnja? |
| Naselje heroja Sokolje | 0.063 | 0.041 | 1.550 | model > 2010 za >30%: nova gradnja? |
| Dobrinja A | 0.066 | 0.039 | 1.690 | model > 2010 za >30%: nova gradnja? |
| Briješće | 0.065 | 0.037 | 1.747 | model > 2010 za >30%: nova gradnja? |
| Dobroševići | 0.074 | 0.029 | 2.504 | model > 2010 za >30%: nova gradnja? |
| Alipašin Most III | 0.055 | nan | nan | nova MZ (nema 2010) |
| Zabrđe | 0.068 | nan | nan | nova MZ (nema 2010) |

Konačni udjeli korišteni kao meko ograničenje: vidi `interim/raspodjela_info.json`.

## 4. Gustina poda (stambeni m² po stanovniku, očekivano 15–60)
Medijan (polja s ≥ 10 st.): 86.5 m²/st. Polja izvan raspona: **634** od 754. Polja sa stanovnicima a bez stambenih zgrada (pouzdanost C, samo WorldPop): **27**.

| h3_id | opcina | mz | stanovnici | stambeni_m2 | m2_po_st | pouzdanost |
|---|---|---|---|---|---|---|
| 891ea92cd6fffff | Novi Grad Sarajevo | Zabrđe | 18 | 38.400 | 2.100 | A |
| 891ef459c77ffff | Stari Grad Sarajevo | Širokača | 17 | 145.900 | 8.600 | C |
| 891ef4596abffff | Novi Grad Sarajevo | Alipašin Most I | 76 | 971.800 | 12.800 | A |
| 891ef45923bffff | Novi Grad Sarajevo | Dobrinja B | 626 | 37,704.300 | 60.200 | A |
| 891ef45919bffff | Novo Sarajevo | Željeznička | 492 | 29,685.600 | 60.300 | B |
| 891ef45802fffff | Stari Grad Sarajevo | Mošćanica | 79 | 4,767.300 | 60.300 | B |
| 891ef4590a7ffff | Novo Sarajevo | Malta | 2018 | 121,846.900 | 60.400 | B |
| 891ef4594c3ffff | Novi Grad Sarajevo | Zabrđe | 63 | 3,804.800 | 60.400 | A |
| 891ef458e43ffff | Stari Grad Sarajevo | Mošćanica | 16 | 969.600 | 60.600 | B |
| 891ef45a8cbffff | Stari Grad Sarajevo | Mošćanica | 39 | 2,366.900 | 60.700 | B |
| 891ef459103ffff | Novo Sarajevo | Grbavica I | 1888 | 114,637.100 | 60.700 | B |
| 891ef45900bffff | Novi Grad Sarajevo | Otoka | 1117 | 67,961.700 | 60.800 | A |
| 891ef45aab7ffff | Stari Grad Sarajevo | Mošćanica | 38 | 2,317.500 | 61.000 | B |
| 891ef4594c7ffff | Novi Grad Sarajevo | Zabrđe | 16 | 977.100 | 61.100 | A |
| 891ea92c94bffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 48 | 2,933.000 | 61.100 | A |
| 891ef45aec3ffff | Stari Grad Sarajevo | Mošćanica | 13 | 794.300 | 61.100 | B |
| 891ef459223ffff | Novi Grad Sarajevo | Dobrinja B | 190 | 11,665.000 | 61.400 | A |
| 891ef459067ffff | Novi Grad Sarajevo | Aneks | 779 | 47,983.200 | 61.600 | A |
| 891ef459077ffff | Novi Grad Sarajevo | Švrakino Selo III | 757 | 46,672.900 | 61.700 | A |
| 891ef4581c7ffff | Stari Grad Sarajevo | Mošćanica | 12 | 743.000 | 61.900 | B |
| 891ef459c23ffff | Stari Grad Sarajevo | Mahmutovac | 10 | 619.100 | 61.900 | B |
| 891ef45aedbffff | Stari Grad Sarajevo | Mošćanica | 14 | 870.200 | 62.200 | B |
| 891ea92cb97ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 30 | 1,869.400 | 62.300 | A |
| 891ef458047ffff | Centar Sarajevo | nan | 32 | 1,999.700 | 62.500 | B |
| 891ef458c43ffff | Stari Grad Sarajevo | Mošćanica | 11 | 687.700 | 62.500 | B |
| 891ef4591abffff | Novo Sarajevo | Kovačići | 1839 | 115,010.900 | 62.500 | B |
| 891ea92cd2bffff | Novi Grad Sarajevo | Zabrđe | 455 | 28,507.700 | 62.700 | A |
| 891ef45800fffff | Centar Sarajevo | nan | 10 | 628.300 | 62.800 | B |
| 891ef458077ffff | Stari Grad Sarajevo | Sedrenik | 32 | 2,010.900 | 62.800 | B |
| 891ef459603ffff | Novi Grad Sarajevo | Briješće | 386 | 24,312.900 | 63.000 | A |
| 891ea92c853ffff | Novi Grad Sarajevo | Dobroševići | 13 | 826.800 | 63.600 | A |
| 891ef45b167ffff | Centar Sarajevo | nan | 14 | 893.500 | 63.800 | B |
| 891ef45aacbffff | Stari Grad Sarajevo | Mošćanica | 32 | 2,043.500 | 63.900 | B |
| 891ef459013ffff | Novi Grad Sarajevo | Alipašin Most III | 1777 | 113,971.900 | 64.100 | A |
| 891ea92cd37ffff | Novi Grad Sarajevo | Reljevo | 47 | 3,015.400 | 64.200 | A |
| 891ef4590a3ffff | Novo Sarajevo | Pofalići II | 778 | 50,221.300 | 64.600 | B |
| 891ef459287ffff | Novi Grad Sarajevo | Švrakino Selo II | 499 | 32,219.000 | 64.600 | A |
| 891ea92c943ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 179 | 11,558.800 | 64.600 | A |
| 891ef45908bffff | Novi Grad Sarajevo | Alipašin Most II | 841 | 54,392.600 | 64.700 | A |
| 891ef4595afffff | Novo Sarajevo | Velešići | 93 | 6,017.400 | 64.700 | B |
| 891ef45824bffff | Centar Sarajevo | Velešići | 517 | 33,481.900 | 64.800 | B |
| 891ef459277ffff | Novi Grad Sarajevo | Dobrinja B | 1269 | 82,337.300 | 64.900 | A |
| 891ef458493ffff | Centar Sarajevo | nan | 34 | 2,218.400 | 65.200 | B |
| 891ef45868bffff | Centar Sarajevo | nan | 25 | 1,632.700 | 65.300 | B |
| 891ef459d57ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 31 | 2,029.100 | 65.500 | B |
| 891ef458573ffff | Centar Sarajevo | Mošćanica | 21 | 1,376.100 | 65.500 | B |
| 891ef4595dbffff | Novi Grad Sarajevo | Dolac | 40 | 2,626.400 | 65.700 | A |
| 891ef45921bffff | Novi Grad Sarajevo | Dobrinja D | 1490 | 98,131.700 | 65.900 | A |
| 891ef459017ffff | Novo Sarajevo | Kvadrant | 1729 | 114,469.900 | 66.200 | B |
| 891ef459d9bffff | Stari Grad Sarajevo | Mošćanica | 45 | 2,980.800 | 66.200 | B |
| 891ef45825bffff | Novo Sarajevo | Velešići | 316 | 20,939.000 | 66.300 | B |
| 891ef458203ffff | Centar Sarajevo | nan | 426 | 28,254.100 | 66.300 | B |
| 891ef459107ffff | Novo Sarajevo | Grbavica I | 1612 | 107,197.100 | 66.500 | B |
| 891ef45853bffff | Stari Grad Sarajevo | Mošćanica | 44 | 2,926.700 | 66.500 | B |
| 891ef459433ffff | Novi Grad Sarajevo | Dolac | 59 | 3,929.400 | 66.600 | A |
| 891ef458ed7ffff | Stari Grad Sarajevo | Mošćanica | 67 | 4,477.200 | 66.800 | B |
| 891ef459063ffff | Novi Grad Sarajevo | Švrakino Selo II | 774 | 51,834.200 | 67.000 | A |
| 891ef458507ffff | Stari Grad Sarajevo | Mošćanica | 26 | 1,742.100 | 67.000 | B |
| 891ef45912fffff | Novo Sarajevo | Gornji Kovačići | 28 | 1,877.800 | 67.100 | B |
| 891ef45ae33ffff | Stari Grad Sarajevo | Mošćanica | 13 | 873.900 | 67.200 | B |
| 891ef45958bffff | Novi Grad Sarajevo | Dolac | 13 | 874.300 | 67.300 | A |
| 891ef45845bffff | Centar Sarajevo | nan | 16 | 1,078.300 | 67.400 | B |
| 891ef4590d7ffff | Novi Grad Sarajevo | Alipašin Most II | 447 | 30,175.600 | 67.500 | A |
| 891ef459d07ffff | Stari Grad Sarajevo | Mošćanica | 30 | 2,025.700 | 67.500 | B |
| 891ef45928bffff | Novi Grad Sarajevo | Dobrinja A | 2008 | 136,013.600 | 67.700 | A |
| 891ef458087ffff | Centar Sarajevo | nan | 22 | 1,495.500 | 68.000 | B |
| 891ef4580afffff | Stari Grad Sarajevo | Mošćanica | 49 | 3,336.300 | 68.100 | B |
| 891ef45956bffff | Novo Sarajevo | Pofalići II | 1108 | 75,596.100 | 68.200 | B |
| 891ef4580c7ffff | Centar Sarajevo | nan | 16 | 1,093.300 | 68.300 | B |
| 891ef45844fffff | Centar Sarajevo | nan | 25 | 1,711.400 | 68.500 | B |
| 891ef4592a3ffff | Novi Grad Sarajevo | Švrakino Selo II | 90 | 6,166.000 | 68.500 | A |
| 891ef459607ffff | Novi Grad Sarajevo | Saraj Polje | 772 | 52,926.400 | 68.600 | A |
| 891ef4591a3ffff | Centar Sarajevo | Kovačići | 297 | 20,391.200 | 68.700 | B |
| 891ef45ae57ffff | Stari Grad Sarajevo | Mošćanica | 13 | 892.800 | 68.700 | B |
| 891ef459dbbffff | Stari Grad Sarajevo | Mošćanica | 14 | 961.900 | 68.700 | B |
| 891ea92eb07ffff | Novi Grad Sarajevo | Dobroševići | 28 | 1,928.700 | 68.900 | A |
| 891ea92cd2fffff | Novi Grad Sarajevo | Zabrđe | 287 | 19,788.700 | 69.000 | A |
| 891ef4590bbffff | Novo Sarajevo | Pofalići II | 441 | 30,416.000 | 69.000 | B |
| 891ef4592a7ffff | Novi Grad Sarajevo | Švrakino Selo II | 34 | 2,345.100 | 69.000 | A |
| 891ef45a327ffff | Stari Grad Sarajevo | Mošćanica | 22 | 1,517.600 | 69.000 | B |
| 891ea92c817ffff | Novi Grad Sarajevo | Dobroševići | 39 | 2,690.300 | 69.000 | A |
| 891ef4591b3ffff | Centar Sarajevo | Željeznička | 1168 | 80,588.400 | 69.000 | B |
| 891ef458253ffff | Novo Sarajevo | Velešići | 976 | 67,508.100 | 69.200 | B |
| 891ef458067ffff | Stari Grad Sarajevo | Sedrenik | 31 | 2,151.000 | 69.400 | B |
| 891ea92c90bffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 196 | 13,608.500 | 69.400 | A |
| 891ef459263ffff | Novi Grad Sarajevo | Dobrinja B | 11 | 765.300 | 69.600 | A |
| 891ea92c833ffff | Novi Grad Sarajevo | Dobroševići | 49 | 3,409.300 | 69.600 | A |
| 891ef45849bffff | Centar Sarajevo | nan | 39 | 2,715.700 | 69.600 | B |
| 891ef459d4bffff | Stari Grad Sarajevo | Širokača | 175 | 12,198.200 | 69.700 | B |
| 891ea92c8dbffff | Novi Grad Sarajevo | Dobroševići | 19 | 1,325.500 | 69.800 | A |
| 891ea92cd1bffff | Novi Grad Sarajevo | Dobroševići | 28 | 1,954.900 | 69.800 | A |
| 891ef459177ffff | Novo Sarajevo | Vraca | 74 | 5,169.700 | 69.900 | B |
| 891ef458147ffff | Stari Grad Sarajevo | Mošćanica | 35 | 2,456.400 | 70.200 | B |
| 891ea92ea6fffff | Novi Grad Sarajevo | Dobroševići | 16 | 1,123.600 | 70.200 | A |
| 891ea92eb87ffff | Novi Grad Sarajevo | Dobroševići | 39 | 2,747.000 | 70.400 | A |
| 891ea92c96fffff | Novi Grad Sarajevo | Briješće | 203 | 14,309.700 | 70.500 | A |
| 891ef4580b7ffff | Centar Sarajevo | nan | 17 | 1,199.500 | 70.600 | B |
| 891ef459667ffff | Novi Grad Sarajevo | Saraj Polje | 1797 | 127,024.300 | 70.700 | A |
| 891ef458c5bffff | Stari Grad Sarajevo | Mošćanica | 49 | 3,466.000 | 70.700 | B |
| 891ef45832fffff | Stari Grad Sarajevo | Mošćanica | 40 | 2,833.600 | 70.800 | B |
| 891ef458487ffff | Centar Sarajevo | nan | 32 | 2,268.200 | 70.900 | B |
| 891ef45aa93ffff | Stari Grad Sarajevo | Mošćanica | 24 | 1,724.400 | 71.900 | B |
| 891ef459193ffff | Novo Sarajevo | Pofalići I | 375 | 27,031.700 | 72.100 | B |
| 891ef458667ffff | Centar Sarajevo | nan | 176 | 12,718.200 | 72.300 | B |
| 891ef45b25bffff | Novi Grad Sarajevo | Zabrđe | 186 | 13,476.200 | 72.500 | A |
| 891ef45ae1bffff | Stari Grad Sarajevo | Mošćanica | 15 | 1,087.300 | 72.500 | B |
| 891ef458ec3ffff | Stari Grad Sarajevo | Mošćanica | 32 | 2,324.100 | 72.600 | B |
| 891ef4584c3ffff | Centar Sarajevo | nan | 30 | 2,178.900 | 72.600 | B |
| 891ef458603ffff | Centar Sarajevo | nan | 19 | 1,382.900 | 72.800 | B |
| 891ef459c83ffff | Stari Grad Sarajevo | Baščaršija | 2098 | 152,747.600 | 72.800 | B |
| 891ef459477ffff | Novi Grad Sarajevo | Alipašin Most I | 253 | 18,421.900 | 72.800 | A |
| 891ea92cd23ffff | Novi Grad Sarajevo | Zabrđe | 471 | 34,351.000 | 72.900 | A |
| 891ef458283ffff | Centar Sarajevo | nan | 573 | 41,924.300 | 73.200 | B |
| 891ef4581b3ffff | Stari Grad Sarajevo | Mošćanica | 35 | 2,564.700 | 73.300 | B |
| 891ea92eb17ffff | Novi Grad Sarajevo | Dobroševići | 12 | 879.900 | 73.300 | A |
| 891ef4584abffff | Centar Sarajevo | nan | 28 | 2,055.300 | 73.400 | B |
| 891ef4584d7ffff | Centar Sarajevo | nan | 12 | 881.000 | 73.400 | B |
| 891ea92c9c3ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 228 | 16,749.000 | 73.500 | A |
| 891ef459c87ffff | Stari Grad Sarajevo | Bistrik | 1565 | 115,064.700 | 73.500 | B |
| 891ef45b277ffff | Novi Grad Sarajevo | Zabrđe | 23 | 1,696.700 | 73.800 | A |
| 891ef4596a7ffff | Novi Grad Sarajevo | Alipašin Most I | 826 | 60,968.800 | 73.800 | A |
| 891ef4596a3ffff | Novi Grad Sarajevo | Alipašin Most I | 388 | 28,640.800 | 73.800 | A |
| 891ef459c27ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 59 | 4,366.300 | 74.000 | B |
| 891ef459157ffff | Novo Sarajevo | Vraca | 750 | 55,559.700 | 74.100 | B |
| 891ef4590b7ffff | Novo Sarajevo | Pofalići II | 155 | 11,512.200 | 74.300 | B |
| 891ef458157ffff | Stari Grad Sarajevo | Mošćanica | 67 | 4,976.500 | 74.300 | B |
| 891ef4591bbffff | Novo Sarajevo | Kovačići | 376 | 27,975.700 | 74.400 | B |
| 891ef458103ffff | Stari Grad Sarajevo | Mošćanica | 29 | 2,160.200 | 74.500 | B |
| 891ef459d8bffff | Stari Grad Sarajevo | Mošćanica | 18 | 1,343.000 | 74.600 | B |
| 891ef45830bffff | Stari Grad Sarajevo | Mošćanica | 172 | 12,835.700 | 74.600 | B |
| 891ef45861bffff | Centar Sarajevo | nan | 17 | 1,273.400 | 74.900 | B |
| 891ef45820bffff | Centar Sarajevo | nan | 1447 | 108,469.500 | 75.000 | B |
| 891ef45838fffff | Stari Grad Sarajevo | Sedrenik | 26 | 1,949.200 | 75.000 | B |
| 891ef45961bffff | Novi Grad Sarajevo | Briješće | 329 | 24,714.800 | 75.100 | A |
| 891ef458673ffff | Centar Sarajevo | nan | 839 | 63,093.700 | 75.200 | B |
| 891ea92ceb7ffff | Novi Grad Sarajevo | Dobroševići | 18 | 1,353.600 | 75.200 | A |
| 891ef4596b7ffff | Novi Grad Sarajevo | Alipašin Most I | 510 | 38,424.200 | 75.300 | A |
| 891ef4590d3ffff | Novi Grad Sarajevo | Alipašin Most I | 761 | 57,769.300 | 75.900 | A |
| 891ef45850fffff | Centar Sarajevo | Mošćanica | 76 | 5,783.400 | 76.100 | B |
| 891ef458e5bffff | Stari Grad Sarajevo | Mošćanica | 12 | 914.500 | 76.200 | B |
| 891ef458377ffff | Stari Grad Sarajevo | Mošćanica | 62 | 4,725.600 | 76.200 | B |
| 891ea92cdafffff | Novi Grad Sarajevo | Reljevo | 21 | 1,604.200 | 76.400 | A |
| 891ef459c93ffff | Stari Grad Sarajevo | Ferhadija | 1993 | 152,440.800 | 76.500 | B |
| 891ef459443ffff | Novi Grad Sarajevo | Alipašin Most I | 111 | 8,490.300 | 76.500 | A |
| 891ef45803bffff | Stari Grad Sarajevo | Mošćanica | 80 | 6,139.100 | 76.700 | B |
| 891ea92ccb3ffff | Novi Grad Sarajevo | Dobroševići | 28 | 2,150.400 | 76.800 | A |
| 891ef458023ffff | Stari Grad Sarajevo | Mošćanica | 122 | 9,376.300 | 76.900 | B |
| 891ef4582cfffff | Centar Sarajevo | Velešići | 1274 | 97,943.700 | 76.900 | B |
| 891ef45a22bffff | Centar Sarajevo | nan | 30 | 2,309.700 | 77.000 | B |
| 891ef458257ffff | Centar Sarajevo | nan | 1608 | 123,801.500 | 77.000 | B |
| 891ef45862fffff | Centar Sarajevo | nan | 678 | 52,296.500 | 77.100 | B |
| 891ef459173ffff | Novo Sarajevo | Vraca | 317 | 24,486.700 | 77.200 | B |
| 891ef45a35bffff | Centar Sarajevo | nan | 17 | 1,313.500 | 77.300 | B |
| 891ef4580a3ffff | Centar Sarajevo | nan | 54 | 4,174.000 | 77.300 | B |
| 891ea92c9b7ffff | Novi Grad Sarajevo | Zabrđe | 42 | 3,246.700 | 77.300 | A |
| 891ef4580abffff | Centar Sarajevo | nan | 53 | 4,099.000 | 77.300 | B |
| 891ea92cd03ffff | Novi Grad Sarajevo | Reljevo | 31 | 2,403.300 | 77.500 | A |
| 891ef45918fffff | Novo Sarajevo | Željeznička | 702 | 54,473.100 | 77.600 | B |
| 891ef45909bffff | Novi Grad Sarajevo | Buća Potok | 592 | 45,956.000 | 77.600 | A |
| 891ef45929bffff | Novi Grad Sarajevo | Saraj Polje | 634 | 49,324.000 | 77.800 | A |
| 891ef45a22fffff | Centar Sarajevo | nan | 41 | 3,194.600 | 77.900 | B |
| 891ea92c8bbffff | Novi Grad Sarajevo | Dobroševići | 103 | 8,033.700 | 78.000 | A |
| 891ef459097ffff | Novi Grad Sarajevo | Dolac | 496 | 38,693.900 | 78.000 | A |
| 891ea92eb0bffff | Novi Grad Sarajevo | Dobroševići | 16 | 1,250.700 | 78.200 | A |
| 891ea92c99bffff | Novi Grad Sarajevo | Zabrđe | 114 | 8,913.100 | 78.200 | A |
| 891ea92c837ffff | Novi Grad Sarajevo | Dobroševići | 106 | 8,329.200 | 78.600 | A |
| 891ef458073ffff | Centar Sarajevo | nan | 45 | 3,540.100 | 78.700 | B |
| 891ef4590b3ffff | Novo Sarajevo | Pofalići II | 251 | 19,749.500 | 78.700 | B |
| 891ea92eb53ffff | Novi Grad Sarajevo | Dobroševići | 19 | 1,496.300 | 78.800 | A |
| 891ef458ed3ffff | Stari Grad Sarajevo | Mošćanica | 53 | 4,177.300 | 78.800 | B |
| 891ef458037ffff | Stari Grad Sarajevo | Mošćanica | 45 | 3,554.400 | 79.000 | B |
| 891ef459153ffff | Novo Sarajevo | Hrasno Brdo | 822 | 64,933.500 | 79.000 | B |
| 891ef45940fffff | Novi Grad Sarajevo | Dolac | 165 | 13,091.500 | 79.300 | A |
| 891ef459463ffff | Novi Grad Sarajevo | Alipašin Most I | 472 | 37,465.100 | 79.400 | A |
| 891ef459527ffff | Novo Sarajevo | Velešići | 523 | 41,529.600 | 79.400 | B |
| 891ef45944fffff | Novi Grad Sarajevo | Alipašin Most I | 527 | 41,902.400 | 79.500 | A |
| 891ef45946bffff | Novi Grad Sarajevo | Alipašin Most I | 638 | 50,879.200 | 79.700 | A |
| 891ef459447ffff | Novi Grad Sarajevo | Alipašin Most I | 395 | 31,511.300 | 79.800 | A |
| 891ef45b203ffff | Novi Grad Sarajevo | Zabrđe | 17 | 1,356.300 | 79.800 | A |
| 891ef458327ffff | Stari Grad Sarajevo | Mošćanica | 33 | 2,633.500 | 79.800 | B |
| 891ef45b64fffff | Novi Grad Sarajevo | Reljevo | 29 | 2,315.000 | 79.800 | A |
| 891ea92c947ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 71 | 5,673.900 | 79.900 | A |
| 891ef45946fffff | Novi Grad Sarajevo | Buća Potok | 615 | 49,154.100 | 79.900 | A |
| 891ef459473ffff | Novi Grad Sarajevo | Alipašin Most I | 435 | 34,789.200 | 80.000 | A |
| 891ef45914fffff | Novo Sarajevo | Vraca | 52 | 4,161.300 | 80.000 | B |
| 891ef458623ffff | Centar Sarajevo | nan | 24 | 1,920.700 | 80.000 | B |
| 891ef45854fffff | Centar Sarajevo | nan | 92 | 7,376.500 | 80.200 | B |
| 891ef458557ffff | Centar Sarajevo | nan | 11 | 884.800 | 80.400 | B |
| 891ea92cdb3ffff | Novi Grad Sarajevo | Reljevo | 44 | 3,541.400 | 80.500 | A |
| 891ef4582abffff | Centar Sarajevo | nan | 1684 | 135,792.200 | 80.600 | B |
| 891ea92eb8bffff | Novi Grad Sarajevo | Dobroševići | 11 | 887.900 | 80.700 | A |
| 891ef4583afffff | Stari Grad Sarajevo | Mošćanica | 156 | 12,607.700 | 80.800 | B |
| 891ea92eb13ffff | Novi Grad Sarajevo | Dobroševići | 23 | 1,861.000 | 80.900 | A |
| 891ef45947bffff | Novi Grad Sarajevo | Alipašin Most I | 702 | 56,817.800 | 80.900 | A |
| 891ef45910bffff | Novo Sarajevo | Vraca | 819 | 66,320.800 | 81.000 | B |
| 891ef45b2cbffff | Novi Grad Sarajevo | Zabrđe | 217 | 17,591.500 | 81.100 | A |
| 891ef45aa4fffff | Stari Grad Sarajevo | Mošćanica | 32 | 2,595.000 | 81.100 | B |
| 891ea92c973ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 280 | 22,751.600 | 81.300 | A |
| 891ef45954fffff | Novo Sarajevo | Pofalići II | 214 | 17,396.100 | 81.300 | B |
| 891ef45826fffff | Centar Sarajevo | nan | 1501 | 122,078.400 | 81.300 | B |
| 891ea92c8d3ffff | Novi Grad Sarajevo | Dobroševići | 59 | 4,807.100 | 81.500 | A |
| 891ef45ae2bffff | Stari Grad Sarajevo | Mošćanica | 11 | 896.400 | 81.500 | B |
| 891ef45b24fffff | Novi Grad Sarajevo | Zabrđe | 29 | 2,364.600 | 81.500 | A |
| 891ef6965a7ffff | Novi Grad Sarajevo | Dobrinja A | 372 | 30,332.000 | 81.500 | A |
| 891ef458683ffff | Centar Sarajevo | nan | 67 | 5,473.700 | 81.700 | B |
| 891ef459c97ffff | Stari Grad Sarajevo | Baščaršija | 1794 | 146,749.400 | 81.800 | B |
| 891ef458297ffff | Centar Sarajevo | nan | 546 | 44,672.800 | 81.800 | B |
| 891ef459083ffff | Novi Grad Sarajevo | Buća Potok | 734 | 60,190.300 | 82.000 | A |
| 891ea92c98bffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 228 | 18,706.300 | 82.000 | A |
| 891ef459567ffff | Novo Sarajevo | Pofalići I | 619 | 50,831.900 | 82.100 | B |
| 891ef458443ffff | Centar Sarajevo | nan | 36 | 2,957.300 | 82.100 | B |
| 891ea92c9a7ffff | Novi Grad Sarajevo | Zabrđe | 156 | 12,818.000 | 82.200 | A |
| 891ef4582dbffff | Novo Sarajevo | Gornji Velešići | 297 | 24,413.800 | 82.200 | B |
| 891ea92c963ffff | Novi Grad Sarajevo | Briješće | 238 | 19,573.400 | 82.200 | A |
| 891ef459cafffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 167 | 13,755.300 | 82.400 | B |
| 891ef45b20bffff | Novi Grad Sarajevo | Zabrđe | 56 | 4,620.600 | 82.500 | A |
| 891ef45968bffff | Novi Grad Sarajevo | Briješće | 67 | 5,535.100 | 82.600 | A |
| 891ef45906bffff | Novi Grad Sarajevo | Švrakino Selo II | 268 | 22,144.000 | 82.600 | A |
| 891ef459d17ffff | Stari Grad Sarajevo | Mošćanica | 97 | 8,027.200 | 82.800 | B |
| 891ef45829bffff | Centar Sarajevo | nan | 35 | 2,901.700 | 82.900 | B |
| 891ef459027ffff | Novo Sarajevo | Hrasno Brdo | 805 | 66,800.200 | 83.000 | B |
| 891ef458063ffff | Centar Sarajevo | Sedrenik | 52 | 4,324.400 | 83.200 | B |
| 891ef459533ffff | Novo Sarajevo | Velešići | 76 | 6,323.600 | 83.200 | B |
| 891ef458143ffff | Stari Grad Sarajevo | Mošćanica | 14 | 1,165.800 | 83.300 | B |
| 891ef45943bffff | Novi Grad Sarajevo | Dolac | 149 | 12,432.700 | 83.400 | A |
| 891ef45942fffff | Novi Grad Sarajevo | Dolac | 693 | 57,860.000 | 83.500 | A |
| 891ea92cd3bffff | Novi Grad Sarajevo | Reljevo | 31 | 2,589.600 | 83.500 | A |
| 891ea92cd57ffff | Novi Grad Sarajevo | Dobroševići | 29 | 2,425.800 | 83.600 | A |
| 891ef458247ffff | Centar Sarajevo | nan | 954 | 79,813.000 | 83.700 | B |
| 891ef459563ffff | Novo Sarajevo | Pofalići II | 433 | 36,227.300 | 83.700 | B |
| 891ef45821bffff | Centar Sarajevo | nan | 1117 | 93,498.700 | 83.700 | B |
| 891ef45840bffff | Centar Sarajevo | nan | 92 | 7,701.500 | 83.700 | B |
| 891ef45955bffff | Novi Grad Sarajevo | Dolac | 850 | 71,276.600 | 83.900 | A |
| 891ef459467ffff | Novi Grad Sarajevo | Buća Potok | 611 | 51,273.800 | 83.900 | A |
| 891ea92c983ffff | Novi Grad Sarajevo | Zabrđe | 256 | 21,505.700 | 84.000 | A |
| 891ef458207ffff | Centar Sarajevo | nan | 482 | 40,542.800 | 84.100 | B |
| 891ef4581bbffff | Stari Grad Sarajevo | Mošćanica | 14 | 1,181.300 | 84.400 | B |
| 891ef4581dbffff | Stari Grad Sarajevo | Mošćanica | 25 | 2,109.800 | 84.400 | B |
| 891ea92c957ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 588 | 49,636.100 | 84.400 | A |
| 891ef459573ffff | Novo Sarajevo | Pofalići II | 682 | 57,589.800 | 84.400 | B |
| 891ef4596d7ffff | Novi Grad Sarajevo | Briješće | 71 | 6,003.000 | 84.500 | A |
| 891ef458417ffff | Centar Sarajevo | nan | 42 | 3,552.300 | 84.600 | B |
| 891ef4596c3ffff | Novi Grad Sarajevo | Briješće | 42 | 3,561.300 | 84.800 | A |
| 891ef45b213ffff | Novi Grad Sarajevo | Zabrđe | 53 | 4,496.600 | 84.800 | A |
| 891ef4583b7ffff | Stari Grad Sarajevo | Mošćanica | 359 | 30,518.100 | 85.000 | B |
| 891ef4592b7ffff | Novi Grad Sarajevo | Švrakino Selo II | 399 | 33,964.800 | 85.100 | A |
| 891ef45904fffff | Novi Grad Sarajevo | Švrakino Selo II | 604 | 51,469.200 | 85.200 | A |
| 891ea92cc1bffff | Novi Grad Sarajevo | Dobroševići | 66 | 5,626.000 | 85.200 | A |
| 891ef45b257ffff | Novi Grad Sarajevo | Zabrđe | 58 | 4,953.600 | 85.400 | A |
| 891ef459c8bffff | Centar Sarajevo | Mjedenica | 907 | 77,474.500 | 85.400 | B |
| 891ef45811bffff | Stari Grad Sarajevo | Mošćanica | 38 | 3,247.200 | 85.500 | B |
| 891ef4594dbffff | Novi Grad Sarajevo | Zabrđe | 182 | 15,567.400 | 85.500 | A |
| 891ea92c9cfffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 287 | 24,630.400 | 85.800 | A |
| 891ef45b20fffff | Novi Grad Sarajevo | Zabrđe | 36 | 3,105.700 | 86.300 | A |
| 891ef459093ffff | Novi Grad Sarajevo | Dolac | 926 | 79,897.000 | 86.300 | A |
| 891ea92c913ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 260 | 22,454.700 | 86.400 | A |
| 891ef459523ffff | Novo Sarajevo | Velešići | 261 | 22,551.100 | 86.400 | B |
| 891ef459547ffff | Novo Sarajevo | Pofalići II | 102 | 8,832.300 | 86.600 | B |
| 891ef45806bffff | Centar Sarajevo | nan | 32 | 2,773.700 | 86.700 | B |
| 891ef4595a7ffff | Novo Sarajevo | Gornji Velešići | 77 | 6,677.300 | 86.700 | B |
| 891ea92c987ffff | Novi Grad Sarajevo | Zabrđe | 507 | 44,091.600 | 87.000 | A |
| 891ef459133ffff | Novo Sarajevo | Gornji Kovačići | 470 | 40,902.200 | 87.000 | B |
| 891ef459ddbffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 144 | 12,542.800 | 87.100 | B |
| 891ef4582d7ffff | Centar Sarajevo | nan | 335 | 29,281.600 | 87.400 | B |
| 891ef45902fffff | Novo Sarajevo | Hrasno Brdo | 572 | 50,006.800 | 87.400 | B |
| 891ef458273ffff | Centar Sarajevo | nan | 753 | 65,835.600 | 87.400 | B |
| 891ef458217ffff | Centar Sarajevo | nan | 728 | 63,653.400 | 87.400 | B |
| 891ea92ebc7ffff | Novi Grad Sarajevo | Dobroševići | 16 | 1,399.900 | 87.500 | A |
| 891ef459577ffff | Novo Sarajevo | Pofalići I | 665 | 58,221.300 | 87.600 | B |
| 891ef458263ffff | Centar Sarajevo | nan | 1572 | 137,758.200 | 87.600 | B |
| 891ef459cd3ffff | Centar Sarajevo | nan | 967 | 84,999.300 | 87.900 | B |
| 891ea92cd0fffff | Novi Grad Sarajevo | Reljevo | 192 | 16,903.200 | 88.000 | A |
| 891ea92eb1bffff | Novi Grad Sarajevo | Dobroševići | 26 | 2,289.200 | 88.000 | A |
| 891ef459613ffff | Novi Grad Sarajevo | Briješće | 158 | 13,916.700 | 88.100 | A |
| 891ef45816fffff | Stari Grad Sarajevo | Mošćanica | 42 | 3,708.900 | 88.300 | B |
| 891ef45b253ffff | Novi Grad Sarajevo | Zabrđe | 194 | 17,144.500 | 88.400 | A |
| 891ef4595c3ffff | Novi Grad Sarajevo | Dolac | 13 | 1,148.900 | 88.400 | A |
| 891ef459507ffff | Novo Sarajevo | Pofalići I | 73 | 6,456.400 | 88.400 | B |
| 891ef45910fffff | Novo Sarajevo | Vraca | 435 | 38,564.500 | 88.700 | B |
| 891ef4594cbffff | Novi Grad Sarajevo | Zabrđe | 35 | 3,106.400 | 88.800 | A |
| 891ea92c903ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 311 | 27,604.300 | 88.800 | A |
| 891ef459553ffff | Novi Grad Sarajevo | Dolac | 227 | 20,187.700 | 88.900 | A |
| 891ef459557ffff | Novi Grad Sarajevo | Dolac | 75 | 6,671.800 | 89.000 | A |
| 891ef45834fffff | Stari Grad Sarajevo | Kovači | 458 | 40,784.600 | 89.000 | B |
| 891ef45847bffff | Centar Sarajevo | nan | 35 | 3,117.400 | 89.100 | B |
| 891ef459427ffff | Novi Grad Sarajevo | Dolac | 366 | 32,612.100 | 89.100 | A |
| 891ef458367ffff | Stari Grad Sarajevo | Mošćanica | 137 | 12,246.900 | 89.400 | B |
| 891ef458317ffff | Stari Grad Sarajevo | Mošćanica | 146 | 13,053.900 | 89.400 | B |
| 891ef458693ffff | Centar Sarajevo | nan | 94 | 8,426.200 | 89.600 | B |
| 891ef45952fffff | Novo Sarajevo | Pofalići I | 459 | 41,183.500 | 89.700 | B |
| 891ef45b24bffff | Novi Grad Sarajevo | Zabrđe | 251 | 22,548.000 | 89.800 | A |
| 891ea92eb73ffff | Novi Grad Sarajevo | Dobroševići | 13 | 1,169.200 | 89.900 | A |
| 891ef45b2d3ffff | Novi Grad Sarajevo | Zabrđe | 61 | 5,488.900 | 90.000 | A |
| 891ea92cc8bffff | Novi Grad Sarajevo | Dobroševići | 87 | 7,832.600 | 90.000 | A |
| 891ef458697ffff | Centar Sarajevo | nan | 166 | 14,948.000 | 90.000 | B |
| 891ea92cd17ffff | Novi Grad Sarajevo | Reljevo | 16 | 1,441.300 | 90.100 | A |
| 891ef459423ffff | Novi Grad Sarajevo | Dolac | 538 | 48,465.900 | 90.100 | A |
| 891ef45912bffff | Novo Sarajevo | Gornji Kovačići | 53 | 4,783.800 | 90.300 | B |
| 891ef458403ffff | Centar Sarajevo | nan | 78 | 7,044.200 | 90.300 | B |
| 891ea92c823ffff | Novi Grad Sarajevo | Dobroševići | 39 | 3,539.700 | 90.800 | A |
| 891ef459d97ffff | Stari Grad Sarajevo | Mošćanica | 15 | 1,363.000 | 90.900 | B |
| 891ef459dd3ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 27 | 2,453.400 | 90.900 | B |
| 891ef45b1a7ffff | Centar Sarajevo | nan | 14 | 1,273.000 | 90.900 | B |
| 891ef45906fffff | Novo Sarajevo | Hrasno Brdo | 171 | 15,560.300 | 91.000 | B |
| 891ef45820fffff | Centar Sarajevo | nan | 755 | 68,719.700 | 91.000 | B |
| 891ef458663ffff | Centar Sarajevo | nan | 454 | 41,353.900 | 91.100 | B |
| 891ef4582c3ffff | Novo Sarajevo | Gornji Velešići | 381 | 34,720.000 | 91.100 | B |
| 891ea92c9afffff | Novi Grad Sarajevo | Zabrđe | 112 | 10,211.000 | 91.200 | A |
| 891ef45866fffff | Centar Sarajevo | nan | 323 | 29,458.200 | 91.200 | B |
| 891ea92c9bbffff | Novi Grad Sarajevo | Zabrđe | 373 | 34,032.800 | 91.200 | A |
| 891ef459cd7ffff | Centar Sarajevo | nan | 1589 | 145,147.700 | 91.300 | B |
| 891ef45942bffff | Novi Grad Sarajevo | Dolac | 643 | 58,771.000 | 91.400 | A |
| 891ef45953bffff | Novo Sarajevo | Pofalići I | 257 | 23,491.000 | 91.400 | B |
| 891ea92c9b3ffff | Novi Grad Sarajevo | Zabrđe | 217 | 19,835.300 | 91.400 | A |
| 891ef459123ffff | Novo Sarajevo | Gornji Kovačići | 114 | 10,439.900 | 91.600 | B |
| 891ef45957bffff | Novo Sarajevo | Pofalići II | 400 | 36,643.900 | 91.600 | B |
| 891ef4582cbffff | Novo Sarajevo | Gornji Velešići | 685 | 62,781.600 | 91.700 | B |
| 891ea92cdc7ffff | Novi Grad Sarajevo | Dobroševići | 23 | 2,113.900 | 91.900 | A |
| 891ea92c8c3ffff | Novi Grad Sarajevo | Dobroševići | 64 | 5,898.600 | 92.200 | A |
| 891ea92c997ffff | Novi Grad Sarajevo | Zabrđe | 408 | 37,648.000 | 92.300 | A |
| 891ef458187ffff | Stari Grad Sarajevo | Mošćanica | 18 | 1,663.900 | 92.400 | B |
| 891ef458173ffff | Stari Grad Sarajevo | Mošćanica | 13 | 1,202.800 | 92.500 | B |
| 891ea92c937ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 63 | 5,836.900 | 92.600 | A |
| 891ef459c9bffff | Centar Sarajevo | Ferhadija | 1784 | 165,402.600 | 92.700 | B |
| 891ea92c9c7ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 818 | 75,841.000 | 92.700 | A |
| 891ef459c8fffff | Stari Grad Sarajevo | Bistrik | 565 | 52,385.300 | 92.700 | B |
| 891ef45b2c3ffff | Novi Grad Sarajevo | Zabrđe | 88 | 8,167.800 | 92.800 | A |
| 891ef459d93ffff | Stari Grad Sarajevo | Mošćanica | 43 | 3,998.900 | 93.000 | B |
| 891ef459147ffff | Novo Sarajevo | Vraca | 384 | 35,736.900 | 93.100 | B |
| 891ef4583d7ffff | Stari Grad Sarajevo | Sedrenik | 259 | 24,127.900 | 93.200 | B |
| 891ef459ca7ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 190 | 17,708.000 | 93.200 | B |
| 891ea92c9a3ffff | Novi Grad Sarajevo | Zabrđe | 258 | 24,082.300 | 93.300 | A |
| 891ef45833bffff | Stari Grad Sarajevo | Mošćanica | 106 | 9,905.000 | 93.400 | B |
| 891ea92c9d7ffff | Novi Grad Sarajevo | Zabrđe | 139 | 12,998.000 | 93.500 | A |
| 891ef45944bffff | Novi Grad Sarajevo | Alipašin Most I | 264 | 24,729.000 | 93.700 | A |
| 891ef4596cbffff | Novi Grad Sarajevo | Briješće | 42 | 3,935.900 | 93.700 | A |
| 891ef4592c3ffff | Novi Grad Sarajevo | Dobrinja A | 824 | 77,267.200 | 93.800 | A |
| 891ef459397ffff | Novo Sarajevo | Hrasno Brdo | 242 | 22,753.800 | 94.000 | B |
| 891ef4586bbffff | Centar Sarajevo | nan | 29 | 2,728.700 | 94.100 | B |
| 891ef4595a3ffff | Novo Sarajevo | Velešići | 129 | 12,141.100 | 94.100 | B |
| 891ef459cb3ffff | Stari Grad Sarajevo | Babića bašča | 831 | 78,299.100 | 94.200 | B |
| 891ef4580cbffff | Centar Sarajevo | nan | 153 | 14,431.300 | 94.300 | B |
| 891ef45914bffff | Novo Sarajevo | Hrasno Brdo | 148 | 13,962.200 | 94.300 | B |
| 891ea92c91bffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 522 | 49,284.500 | 94.400 | A |
| 891ef45b247ffff | Novi Grad Sarajevo | Zabrđe | 65 | 6,149.700 | 94.600 | A |
| 891ef459127ffff | Centar Sarajevo | Gornji Kovačići | 107 | 10,126.400 | 94.600 | B |
| 891ef45826bffff | Centar Sarajevo | nan | 663 | 62,761.900 | 94.700 | B |
| 891ef45920bffff | Novi Grad Sarajevo | Dobrinja B | 781 | 73,952.200 | 94.700 | A |
| 891ef459257ffff | Novi Grad Sarajevo | Dobrinja B | 526 | 49,878.100 | 94.800 | A |
| 891ef458243ffff | Centar Sarajevo | Velešići | 494 | 46,890.100 | 94.900 | B |
| 891ef45802bffff | Stari Grad Sarajevo | Mošćanica | 25 | 2,373.800 | 95.000 | B |
| 891ef459cdbffff | Centar Sarajevo | nan | 514 | 48,843.100 | 95.000 | B |
| 891ef45839bffff | Stari Grad Sarajevo | Sedrenik | 48 | 4,561.400 | 95.000 | B |
| 891ef4595abffff | Novo Sarajevo | Velešići | 74 | 7,035.100 | 95.100 | B |
| 891ef4592c7ffff | Novi Grad Sarajevo | Dobrinja A | 623 | 59,271.300 | 95.100 | A |
| 891ea92cdabffff | Novi Grad Sarajevo | Reljevo | 36 | 3,428.200 | 95.200 | A |
| 891ef4592d7ffff | Novi Grad Sarajevo | Saraj Polje | 498 | 47,462.100 | 95.300 | A |
| 891ef45952bffff | Novo Sarajevo | Pofalići I | 562 | 53,587.900 | 95.400 | B |
| 891ea92c90fffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 306 | 29,192.200 | 95.400 | A |
| 891ef459c1bffff | Stari Grad Sarajevo | Širokača | 286 | 27,328.600 | 95.600 | B |
| 891ef45aecbffff | Stari Grad Sarajevo | Mošćanica | 17 | 1,624.500 | 95.600 | B |
| 891ef45913bffff | Novo Sarajevo | Gornji Kovačići | 330 | 31,545.900 | 95.600 | B |
| 891ef458547ffff | Centar Sarajevo | nan | 38 | 3,645.200 | 95.900 | B |
| 891ef4591b7ffff | Centar Sarajevo | nan | 800 | 76,756.600 | 95.900 | B |
| 891ef459537ffff | Novo Sarajevo | Velešići | 427 | 40,974.400 | 96.000 | B |
| 891ef45830fffff | Stari Grad Sarajevo | Mošćanica | 114 | 10,948.300 | 96.000 | B |
| 891ef45864bffff | Centar Sarajevo | Velešići | 18 | 1,730.300 | 96.100 | B |
| 891ea92eb4bffff | Novi Grad Sarajevo | Dobroševići | 17 | 1,637.300 | 96.300 | A |
| 891ef45838bffff | Stari Grad Sarajevo | Sedrenik | 233 | 22,441.800 | 96.300 | B |
| 891ef459cbbffff | Stari Grad Sarajevo | Bistrik | 826 | 79,576.500 | 96.300 | B |
| 891ef458293ffff | Centar Sarajevo | nan | 177 | 17,066.300 | 96.400 | B |
| 891ef4583c3ffff | Stari Grad Sarajevo | Sedrenik | 361 | 34,837.400 | 96.500 | B |
| 891ef459dcbffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 70 | 6,767.000 | 96.700 | B |
| 891ea92c98fffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 180 | 17,420.400 | 96.800 | A |
| 891ef458363ffff | Stari Grad Sarajevo | Vratnik | 114 | 11,043.900 | 96.900 | B |
| 891ef4584cfffff | Centar Sarajevo | nan | 43 | 4,168.500 | 96.900 | B |
| 891ef4583bbffff | Stari Grad Sarajevo | Mošćanica | 75 | 7,275.800 | 97.000 | B |
| 891ea92c9abffff | Novi Grad Sarajevo | Zabrđe | 232 | 22,526.500 | 97.100 | A |
| 891ef45939bffff | Novo Sarajevo | Hrasno Brdo | 132 | 12,823.900 | 97.200 | B |
| 891ef45950fffff | Novo Sarajevo | Pofalići II | 322 | 31,321.900 | 97.300 | B |
| 891ea92cca3ffff | Novi Grad Sarajevo | Dobroševići | 50 | 4,877.600 | 97.600 | A |
| 891ef458473ffff | Centar Sarajevo | nan | 35 | 3,416.600 | 97.600 | B |
| 891ef45b647ffff | Novi Grad Sarajevo | Reljevo | 11 | 1,075.200 | 97.700 | A |
| 891ef4596b3ffff | Novi Grad Sarajevo | Briješće | 212 | 20,723.600 | 97.800 | A |
| 891ef4583cbffff | Stari Grad Sarajevo | Medrese | 596 | 58,286.900 | 97.800 | B |
| 891ef458013ffff | Centar Sarajevo | nan | 44 | 4,307.100 | 97.900 | B |
| 891ef459dd7ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 64 | 6,268.400 | 97.900 | B |
| 891ef458497ffff | Centar Sarajevo | nan | 35 | 3,432.700 | 98.100 | B |
| 891ef45831bffff | Stari Grad Sarajevo | Sedrenik | 147 | 14,454.700 | 98.300 | B |
| 891ef45915bffff | Novo Sarajevo | Hrasno Brdo | 541 | 53,311.900 | 98.500 | B |
| 891ef45832bffff | Stari Grad Sarajevo | Mošćanica | 107 | 10,545.400 | 98.600 | B |
| 891ea92cd07ffff | Novi Grad Sarajevo | Reljevo | 134 | 13,208.800 | 98.600 | A |
| 891ef4595b3ffff | Novo Sarajevo | Velešići | 80 | 7,903.800 | 98.800 | B |
| 891ef45816bffff | Stari Grad Sarajevo | Mošćanica | 104 | 10,283.900 | 98.900 | B |
| 891ef458267ffff | Centar Sarajevo | nan | 1417 | 140,174.400 | 98.900 | B |
| 891ef45806fffff | Stari Grad Sarajevo | Sedrenik | 60 | 5,936.900 | 98.900 | B |
| 891ef45968fffff | Novi Grad Sarajevo | Briješće | 300 | 29,698.200 | 99.000 | A |
| 891ea92cdb7ffff | Novi Grad Sarajevo | Reljevo | 59 | 5,856.300 | 99.300 | A |
| 891ef45828fffff | Centar Sarajevo | nan | 1136 | 112,797.600 | 99.300 | B |
| 891ef458303ffff | Stari Grad Sarajevo | Mošćanica | 113 | 11,221.200 | 99.300 | B |
| 891ef4580b3ffff | Centar Sarajevo | nan | 90 | 8,943.200 | 99.400 | B |
| 891ef459143ffff | Novo Sarajevo | Vraca | 566 | 56,312.200 | 99.500 | B |
| 891ef458353ffff | Stari Grad Sarajevo | Medrese | 788 | 78,637.300 | 99.800 | B |
| 891ef458373ffff | Stari Grad Sarajevo | Vratnik | 513 | 51,312.600 | 100.000 | B |
| 891ef459cc7ffff | Centar Sarajevo | Širokača | 200 | 20,038.700 | 100.200 | B |
| 891ea92ccb7ffff | Novi Grad Sarajevo | Dobroševići | 24 | 2,405.400 | 100.200 | A |
| 891ef459cb7ffff | Stari Grad Sarajevo | Babića bašča | 291 | 29,187.900 | 100.300 | B |
| 891ef45969bffff | Novi Grad Sarajevo | Briješće | 339 | 34,006.100 | 100.300 | A |
| 891ea92cbb7ffff | Novi Grad Sarajevo | Briješće | 15 | 1,506.900 | 100.500 | A |
| 891ea92cda7ffff | Novi Grad Sarajevo | Reljevo | 100 | 10,049.800 | 100.500 | A |
| 891ef458163ffff | Stari Grad Sarajevo | Mošćanica | 33 | 3,323.400 | 100.700 | B |
| 891ef4583cfffff | Stari Grad Sarajevo | Medrese | 396 | 39,960.500 | 100.900 | B |
| 891ef459cc3ffff | Centar Sarajevo | nan | 368 | 37,194.900 | 101.100 | B |
| 891ef458167ffff | Stari Grad Sarajevo | Mošćanica | 77 | 7,784.800 | 101.100 | B |
| 891ef458edbffff | Stari Grad Sarajevo | Mošćanica | 19 | 1,925.800 | 101.400 | B |
| 891ef459c13ffff | Stari Grad Sarajevo | Širokača | 535 | 54,262.500 | 101.400 | B |
| 891ef45958fffff | Novo Sarajevo | Pofalići II | 14 | 1,421.700 | 101.600 | B |
| 891ef4581cbffff | Stari Grad Sarajevo | Mošćanica | 37 | 3,758.700 | 101.600 | B |
| 891ef4584cbffff | Centar Sarajevo | nan | 36 | 3,664.400 | 101.800 | B |
| 891ef4596bbffff | Novi Grad Sarajevo | Briješće | 281 | 28,613.900 | 101.800 | A |
| 891ea92cd8fffff | Novi Grad Sarajevo | Reljevo | 15 | 1,528.900 | 101.900 | A |
| 891ef458227ffff | Stari Grad Sarajevo | Logavina | 797 | 81,292.800 | 102.000 | B |
| 891ef458463ffff | Centar Sarajevo | nan | 77 | 7,855.300 | 102.000 | B |
| 891ef459cabffff | Stari Grad Sarajevo | Mahmutovac | 366 | 37,469.100 | 102.400 | B |
| 891ef458e97ffff | Stari Grad Sarajevo | Mošćanica | 12 | 1,229.700 | 102.500 | B |
| 891ef459c0fffff | Stari Grad Sarajevo | Toka-Džeka | 213 | 21,936.400 | 103.000 | B |
| 891ef4591a7ffff | Centar Sarajevo | nan | 441 | 45,490.100 | 103.200 | B |
| 891ef45b127ffff | Centar Sarajevo | nan | 26 | 2,682.000 | 103.200 | B |
| 891ef458e93ffff | Stari Grad Sarajevo | Mošćanica | 56 | 5,778.000 | 103.200 | B |
| 891ef45844bffff | Centar Sarajevo | nan | 19 | 1,963.000 | 103.300 | B |
| 891ef45834bffff | Stari Grad Sarajevo | Kovači | 845 | 87,324.500 | 103.300 | B |
| 891ea92cdbbffff | Novi Grad Sarajevo | Reljevo | 55 | 5,685.000 | 103.400 | A |
| 891ea92cd43ffff | Novi Grad Sarajevo | Dobroševići | 107 | 11,074.900 | 103.500 | A |
| 891ef4591afffff | Centar Sarajevo | Kovačići | 352 | 36,503.000 | 103.700 | B |
| 891ef459dc3ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 167 | 17,376.200 | 104.000 | B |
| 891ea92cda3ffff | Novi Grad Sarajevo | Reljevo | 125 | 13,007.900 | 104.100 | A |
| 891ef459c73ffff | Stari Grad Sarajevo | Širokača | 48 | 4,996.700 | 104.100 | B |
| 891ef45812fffff | Stari Grad Sarajevo | Mošćanica | 81 | 8,441.800 | 104.200 | B |
| 891ef458307ffff | Stari Grad Sarajevo | Mošćanica | 177 | 18,447.000 | 104.200 | B |
| 891ef459c17ffff | Stari Grad Sarajevo | Bistrik | 476 | 49,634.200 | 104.300 | B |
| 891ef459d0bffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 13 | 1,358.600 | 104.500 | B |
| 891ef458213ffff | Centar Sarajevo | nan | 560 | 58,628.700 | 104.700 | B |
| 891ef4582d3ffff | Centar Sarajevo | Gornji Velešići | 132 | 13,827.100 | 104.800 | B |
| 891ea92cc77ffff | Novi Grad Sarajevo | Dobroševići | 65 | 6,813.300 | 104.800 | A |
| 891ef459ca3ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 472 | 49,478.200 | 104.800 | B |
| 891ef459dc7ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 68 | 7,143.100 | 105.000 | B |
| 891ef45822fffff | Stari Grad Sarajevo | Logavina | 867 | 91,265.400 | 105.300 | B |
| 891ea92cd87ffff | Novi Grad Sarajevo | Reljevo | 65 | 6,844.400 | 105.300 | A |
| 891ef45823bffff | Centar Sarajevo | nan | 1152 | 121,415.400 | 105.400 | B |
| 891ef4580c3ffff | Centar Sarajevo | nan | 111 | 11,706.000 | 105.500 | B |
| 891ea92c813ffff | Novi Grad Sarajevo | Dobroševići | 277 | 29,222.300 | 105.500 | A |
| 891ef458277ffff | Centar Sarajevo | nan | 1283 | 135,600.800 | 105.700 | B |
| 891ef459c37ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 178 | 18,836.300 | 105.800 | B |
| 891ef459c57ffff | Stari Grad Sarajevo | Širokača | 153 | 16,223.500 | 106.000 | B |
| 891ef458333ffff | Stari Grad Sarajevo | Mošćanica | 104 | 11,029.400 | 106.100 | B |
| 891ea92cd33ffff | Novi Grad Sarajevo | Reljevo | 78 | 8,273.200 | 106.100 | A |
| 891ef4583abffff | Stari Grad Sarajevo | Mošćanica | 279 | 29,611.100 | 106.100 | B |
| 891ef459c03ffff | Stari Grad Sarajevo | Toka-Džeka | 399 | 42,408.400 | 106.300 | B |
| 891ef458313ffff | Stari Grad Sarajevo | Sedrenik | 253 | 26,909.600 | 106.400 | B |
| 891ef45804bffff | Centar Sarajevo | nan | 322 | 34,288.800 | 106.500 | B |
| 891ef458357ffff | Stari Grad Sarajevo | Sumbuluša | 397 | 42,282.500 | 106.500 | B |
| 891ef45966fffff | Novi Grad Sarajevo | Saraj Polje | 447 | 47,683.100 | 106.700 | A |
| 891ef45835bffff | Stari Grad Sarajevo | Logavina | 1002 | 106,914.100 | 106.700 | B |
| 891ef458233ffff | Centar Sarajevo | nan | 752 | 80,245.600 | 106.700 | B |
| 891ea92cc0fffff | Novi Grad Sarajevo | Dobroševići | 59 | 6,298.000 | 106.700 | A |
| 891ef4592dbffff | Novi Grad Sarajevo | Dobrinja A | 661 | 70,657.000 | 106.900 | A |
| 891ef45824fffff | Centar Sarajevo | nan | 350 | 37,422.900 | 106.900 | B |
| 891ef45814fffff | Stari Grad Sarajevo | Mošćanica | 60 | 6,426.200 | 107.100 | B |
| 891ea92c967ffff | Novi Grad Sarajevo | Briješće | 427 | 45,734.400 | 107.100 | A |
| 891ef6965a3ffff | Novi Grad Sarajevo | Dobrinja A | 21 | 2,252.500 | 107.300 | A |
| 891ef458343ffff | Stari Grad Sarajevo | Kovači | 813 | 87,211.200 | 107.300 | B |
| 891ea92eb03ffff | Novi Grad Sarajevo | Dobroševići | 14 | 1,502.600 | 107.300 | A |
| 891ef458647ffff | Centar Sarajevo | nan | 217 | 23,290.200 | 107.300 | B |
| 891ea92cc8fffff | Novi Grad Sarajevo | Dobroševići | 39 | 4,195.000 | 107.600 | A |
| 891ea92cd83ffff | Novi Grad Sarajevo | Reljevo | 29 | 3,121.900 | 107.700 | A |
| 891ef459c07ffff | Stari Grad Sarajevo | Mahmutovac | 383 | 41,293.900 | 107.800 | B |
| 891ef458237ffff | Centar Sarajevo | Logavina | 515 | 55,542.500 | 107.800 | B |
| 891ea92cd73ffff | Novi Grad Sarajevo | Dobroševići | 45 | 4,868.500 | 108.200 | A |
| 891ef458347ffff | Stari Grad Sarajevo | Vratnik | 727 | 78,657.200 | 108.200 | B |
| 891ef4583a3ffff | Stari Grad Sarajevo | Mošćanica | 226 | 24,490.200 | 108.400 | B |
| 891ef45b177ffff | Centar Sarajevo | nan | 21 | 2,276.100 | 108.400 | B |
| 891ef4583dbffff | Stari Grad Sarajevo | Sedrenik | 389 | 42,281.500 | 108.700 | B |
| 891ef459c0bffff | Stari Grad Sarajevo | Širokača | 320 | 34,789.700 | 108.700 | B |
| 891ef459dcfffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 135 | 14,695.200 | 108.900 | B |
| 891ef4592d3ffff | Novi Grad Sarajevo | Saraj Polje | 458 | 49,935.300 | 109.000 | A |
| 891ef459d1bffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 103 | 11,235.300 | 109.100 | B |
| 891ef4582bbffff | Centar Sarajevo | nan | 425 | 46,380.100 | 109.100 | B |
| 891ef459c33ffff | Stari Grad Sarajevo | Mahmutovac | 246 | 26,848.100 | 109.100 | B |
| 891ef4583c7ffff | Stari Grad Sarajevo | Sedrenik | 372 | 40,600.500 | 109.100 | B |
| 891ef4595b7ffff | Centar Sarajevo | Gornji Velešići | 123 | 13,435.300 | 109.200 | B |
| 891ef45aa53ffff | Stari Grad Sarajevo | Mošćanica | 18 | 1,972.000 | 109.600 | B |
| 891ef4583b3ffff | Stari Grad Sarajevo | Mošćanica | 148 | 16,234.100 | 109.700 | B |
| 891ef45817bffff | Stari Grad Sarajevo | Mošćanica | 145 | 15,917.800 | 109.800 | B |
| 891ef459d53ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 42 | 4,620.700 | 110.000 | B |
| 891ef459453ffff | Novi Grad Sarajevo | Briješće | 34 | 3,743.600 | 110.100 | A |
| 891ea92cd93ffff | Novi Grad Sarajevo | Reljevo | 22 | 2,424.400 | 110.200 | A |
| 891ef45966bffff | Novi Grad Sarajevo | Saraj Polje | 169 | 18,628.000 | 110.200 | A |
| 891ef459663ffff | Novi Grad Sarajevo | Saraj Polje | 122 | 13,452.800 | 110.300 | A |
| 891ef459693ffff | Novi Grad Sarajevo | Briješće | 359 | 39,596.000 | 110.300 | A |
| 891ef458457ffff | Centar Sarajevo | nan | 21 | 2,316.800 | 110.300 | B |
| 891ef45812bffff | Stari Grad Sarajevo | Mošćanica | 45 | 4,967.700 | 110.400 | B |
| 891ef458627ffff | Centar Sarajevo | nan | 75 | 8,284.500 | 110.500 | B |
| 891ef45837bffff | Stari Grad Sarajevo | Vratnik | 639 | 70,704.400 | 110.600 | B |
| 891ef4583a7ffff | Stari Grad Sarajevo | Mošćanica | 212 | 23,492.000 | 110.800 | B |
| 891ef459c53ffff | Centar Sarajevo | Širokača | 80 | 8,890.400 | 111.100 | B |
| 891ef45814bffff | Stari Grad Sarajevo | Mošćanica | 85 | 9,465.300 | 111.400 | B |
| 891ef458107ffff | Stari Grad Sarajevo | Mošćanica | 30 | 3,363.200 | 112.100 | B |
| 891ea92c92bffff | Novi Grad Sarajevo | Briješće | 200 | 22,432.400 | 112.200 | A |
| 891ef45827bffff | Centar Sarajevo | nan | 885 | 99,334.100 | 112.200 | B |
| 891ef45945bffff | Novi Grad Sarajevo | Briješće | 274 | 30,868.500 | 112.700 | A |
| 891ef45848fffff | Centar Sarajevo | nan | 28 | 3,155.800 | 112.700 | B |
| 891ea92c907ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 438 | 49,418.400 | 112.800 | A |
| 891ea92cdcfffff | Novi Grad Sarajevo | Dobroševići | 17 | 1,920.900 | 113.000 | A |
| 891ea92eb67ffff | Novi Grad Sarajevo | Dobroševići | 30 | 3,401.100 | 113.400 | A |
| 891ea92c92fffff | Novi Grad Sarajevo | Briješće | 265 | 30,072.900 | 113.500 | A |
| 891ea92c8cbffff | Novi Grad Sarajevo | Dobroševići | 205 | 23,268.300 | 113.500 | A |
| 891ea92cd5bffff | Novi Grad Sarajevo | Dobroševići | 76 | 8,630.500 | 113.600 | A |
| 891ef458223ffff | Centar Sarajevo | Logavina | 735 | 83,502.400 | 113.600 | B |
| 891ef458057ffff | Centar Sarajevo | nan | 75 | 8,531.400 | 113.800 | B |
| 891ef45aa5bffff | Stari Grad Sarajevo | Mošćanica | 14 | 1,596.000 | 114.000 | B |
| 891ef459683ffff | Novi Grad Sarajevo | Briješće | 434 | 49,550.200 | 114.200 | A |
| 891ef6965b7ffff | Novi Grad Sarajevo | Saraj Polje | 67 | 7,652.800 | 114.200 | A |
| 891ea92c923ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 213 | 24,351.400 | 114.300 | A |
| 891ef459697ffff | Novi Grad Sarajevo | Briješće | 350 | 40,050.300 | 114.400 | A |
| 891ea92cc63ffff | Novi Grad Sarajevo | Dobroševići | 73 | 8,354.900 | 114.500 | A |
| 891ea92cd0bffff | Novi Grad Sarajevo | Dobroševići | 45 | 5,151.000 | 114.500 | A |
| 891ea92c977ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 414 | 47,409.100 | 114.500 | A |
| 891ea92c8cfffff | Novi Grad Sarajevo | Dobroševići | 85 | 9,755.700 | 114.800 | A |
| 891ea92c933ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 227 | 26,054.800 | 114.800 | A |
| 891ea92eb8fffff | Novi Grad Sarajevo | Dobroševići | 24 | 2,755.200 | 114.800 | A |
| 891ef45867bffff | Centar Sarajevo | nan | 371 | 42,625.000 | 114.900 | B |
| 891ef459687ffff | Novi Grad Sarajevo | Briješće | 437 | 50,222.100 | 114.900 | A |
| 891ea92c917ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 369 | 42,443.800 | 115.000 | A |
| 891ea92c897ffff | Novi Grad Sarajevo | Dobroševići | 47 | 5,414.600 | 115.200 | A |
| 891ef45a267ffff | Centar Sarajevo | nan | 14 | 1,613.000 | 115.200 | B |
| 891ea92cbbbffff | Novi Grad Sarajevo | Briješće | 23 | 2,650.000 | 115.200 | A |
| 891ef45846fffff | Centar Sarajevo | nan | 100 | 11,549.700 | 115.500 | B |
| 891ea92cddbffff | Novi Grad Sarajevo | Dobroševići | 53 | 6,124.100 | 115.500 | A |
| 891ef459677ffff | Novi Grad Sarajevo | Saraj Polje | 52 | 6,012.200 | 115.600 | A |
| 891ea92c93bffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 327 | 37,836.400 | 115.700 | A |
| 891ef4582afffff | Centar Sarajevo | nan | 341 | 39,472.500 | 115.800 | B |
| 891ef4586b3ffff | Centar Sarajevo | nan | 51 | 5,907.000 | 115.800 | B |
| 891ea92eb77ffff | Novi Grad Sarajevo | Dobroševići | 14 | 1,623.500 | 116.000 | A |
| 891ea92cdd3ffff | Novi Grad Sarajevo | Dobroševići | 21 | 2,435.500 | 116.000 | A |
| 891ef4582c7ffff | Centar Sarajevo | nan | 491 | 57,072.400 | 116.200 | B |
| 891ef45804fffff | Centar Sarajevo | nan | 152 | 17,688.400 | 116.400 | B |
| 891ea92cc13ffff | Novi Grad Sarajevo | Dobroševići | 52 | 6,090.800 | 117.100 | A |
| 891ea92c927ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 226 | 26,556.200 | 117.500 | A |
| 891ef458637ffff | Centar Sarajevo | nan | 41 | 4,819.400 | 117.500 | B |
| 891ef459137ffff | Centar Sarajevo | Gornji Kovačići | 270 | 31,773.900 | 117.700 | B |
| 891ef4592cfffff | Novi Grad Sarajevo | Dobrinja A | 902 | 106,253.300 | 117.800 | A |
| 891ef4592cbffff | Novi Grad Sarajevo | Dobrinja A | 243 | 28,696.100 | 118.100 | A |
| 891ef45864fffff | Centar Sarajevo | nan | 240 | 28,386.600 | 118.300 | B |
| 891ef4580d3ffff | Centar Sarajevo | nan | 192 | 22,716.300 | 118.300 | B |
| 891ef458043ffff | Centar Sarajevo | nan | 229 | 27,115.000 | 118.400 | B |
| 891ef45807bffff | Centar Sarajevo | nan | 108 | 12,807.800 | 118.600 | B |
| 891ea92c88fffff | Novi Grad Sarajevo | Dobroševići | 153 | 18,179.200 | 118.800 | A |
| 891ea92c88bffff | Novi Grad Sarajevo | Dobroševići | 227 | 27,069.100 | 119.200 | A |
| 891ef45805bffff | Centar Sarajevo | nan | 209 | 24,937.800 | 119.300 | B |
| 891ef4583d3ffff | Centar Sarajevo | Sedrenik | 357 | 42,629.200 | 119.400 | B |
| 891ea92ccc3ffff | Novi Grad Sarajevo | Dobroševići | 23 | 2,750.600 | 119.600 | A |
| 891ea92ccd7ffff | Novi Grad Sarajevo | Dobroševići | 19 | 2,272.500 | 119.600 | A |
| 891ef45869bffff | Centar Sarajevo | nan | 11 | 1,320.100 | 120.000 | B |
| 891ef459ccfffff | Centar Sarajevo | Širokača | 242 | 29,045.600 | 120.000 | B |
| 891ef458053ffff | Centar Sarajevo | nan | 317 | 38,141.000 | 120.300 | B |
| 891ef45848bffff | Centar Sarajevo | nan | 49 | 5,896.600 | 120.300 | B |
| 891ea92c8b3ffff | Novi Grad Sarajevo | Dobroševići | 52 | 6,259.600 | 120.400 | A |
| 891ef45b12bffff | Centar Sarajevo | nan | 25 | 3,010.700 | 120.400 | B |
| 891ef458453ffff | Centar Sarajevo | nan | 44 | 5,304.600 | 120.600 | B |
| 891ef4580bbffff | Centar Sarajevo | nan | 52 | 6,280.400 | 120.800 | B |
| 891ea92cdc3ffff | Novi Grad Sarajevo | Dobroševići | 33 | 3,989.500 | 120.900 | A |
| 891ef458447ffff | Centar Sarajevo | nan | 23 | 2,784.600 | 121.100 | B |
| 891ef4586afffff | Centar Sarajevo | nan | 125 | 15,143.000 | 121.100 | B |
| 891ef45822bffff | Centar Sarajevo | nan | 922 | 111,745.900 | 121.200 | B |
| 891ea92cc03ffff | Novi Grad Sarajevo | Dobroševići | 43 | 5,215.100 | 121.300 | A |
| 891ef458643ffff | Centar Sarajevo | nan | 134 | 16,261.800 | 121.400 | B |
| 891ef4582b7ffff | Centar Sarajevo | nan | 393 | 47,827.700 | 121.700 | B |
| 891ea92c883ffff | Novi Grad Sarajevo | Dobroševići | 109 | 13,326.000 | 122.300 | A |
| 891ea92cca7ffff | Novi Grad Sarajevo | Dobroševići | 50 | 6,121.400 | 122.400 | A |
| 891ef4580dbffff | Centar Sarajevo | nan | 85 | 10,423.000 | 122.600 | B |
| 891ef458287ffff | Centar Sarajevo | nan | 574 | 70,772.600 | 123.300 | B |
| 891ef4586b7ffff | Centar Sarajevo | nan | 89 | 10,976.900 | 123.300 | B |
| 891ef45841bffff | Centar Sarajevo | nan | 117 | 14,451.700 | 123.500 | B |
| 891ef459ccbffff | Centar Sarajevo | nan | 381 | 47,140.300 | 123.700 | B |
| 891ea92c893ffff | Novi Grad Sarajevo | Dobroševići | 61 | 7,547.800 | 123.700 | A |
| 891ea92cc87ffff | Novi Grad Sarajevo | Dobroševići | 26 | 3,228.400 | 124.200 | A |
| 891ef458483ffff | Centar Sarajevo | nan | 82 | 10,190.400 | 124.300 | B |
| 891ea92cc6fffff | Novi Grad Sarajevo | Dobroševići | 80 | 10,002.600 | 125.000 | A |
| 891ef458687ffff | Centar Sarajevo | nan | 94 | 11,763.600 | 125.100 | B |
| 891ea92cc33ffff | Novi Grad Sarajevo | Dobroševići | 64 | 8,023.300 | 125.400 | A |
| 891ea92cc2fffff | Novi Grad Sarajevo | Dobroševići | 95 | 11,938.100 | 125.700 | A |
| 891ea92ccabffff | Novi Grad Sarajevo | Dobroševići | 61 | 7,685.100 | 126.000 | A |
| 891ef4584c7ffff | Centar Sarajevo | nan | 38 | 4,787.500 | 126.000 | B |
| 891ef4582a3ffff | Centar Sarajevo | nan | 399 | 50,343.300 | 126.200 | B |
| 891ea92ccd3ffff | Novi Grad Sarajevo | Dobroševići | 30 | 3,786.700 | 126.200 | A |
| 891ea92c8c7ffff | Novi Grad Sarajevo | Dobroševići | 108 | 13,636.300 | 126.300 | A |
| 891ea92cc23ffff | Novi Grad Sarajevo | Dobroševići | 103 | 13,026.500 | 126.500 | A |
| 891ea92ccbbffff | Novi Grad Sarajevo | Dobroševići | 20 | 2,533.800 | 126.700 | A |
| 891ea92cd4fffff | Novi Grad Sarajevo | Dobroševići | 157 | 19,923.400 | 126.900 | A |
| 891ea92cc2bffff | Novi Grad Sarajevo | Dobroševići | 85 | 10,794.400 | 127.000 | A |
| 891ef4582b3ffff | Centar Sarajevo | nan | 453 | 57,554.100 | 127.100 | B |
| 891ef45868fffff | Centar Sarajevo | nan | 48 | 6,100.400 | 127.100 | B |
| 891ea92cd53ffff | Novi Grad Sarajevo | Dobroševići | 109 | 13,860.200 | 127.200 | A |
| 891ef458677ffff | Centar Sarajevo | nan | 119 | 15,137.600 | 127.200 | B |
| 891ef4586a3ffff | Centar Sarajevo | nan | 159 | 20,245.600 | 127.300 | B |
| 891ef458413ffff | Centar Sarajevo | nan | 89 | 11,382.400 | 127.900 | B |
| 891ea92cc27ffff | Novi Grad Sarajevo | Dobroševići | 179 | 22,927.100 | 128.100 | A |
| 891ea92cd47ffff | Novi Grad Sarajevo | Dobroševići | 152 | 19,543.300 | 128.600 | A |
| 891ea92cc0bffff | Novi Grad Sarajevo | Dobroševići | 35 | 4,504.000 | 128.700 | A |
| 891ea92cd4bffff | Novi Grad Sarajevo | Dobroševići | 133 | 17,146.200 | 128.900 | A |
| 891ea92cc3bffff | Novi Grad Sarajevo | Dobroševići | 76 | 9,799.100 | 128.900 | A |
| 891ef458657ffff | Centar Sarajevo | nan | 38 | 4,923.700 | 129.600 | B |
| 891ea92eb0fffff | Novi Grad Sarajevo | Dobroševići | 15 | 1,944.300 | 129.600 | A |
| 891ef458003ffff | Centar Sarajevo | nan | 26 | 3,370.800 | 129.600 | B |
| 891ea92ccafffff | Novi Grad Sarajevo | Dobroševići | 77 | 9,987.800 | 129.700 | A |
| 891ea92c887ffff | Novi Grad Sarajevo | Dobroševići | 146 | 18,967.000 | 129.900 | A |
| 891ea92cdcbffff | Novi Grad Sarajevo | Dobroševići | 120 | 15,595.700 | 130.000 | A |
| 891ea92c89bffff | Novi Grad Sarajevo | Dobroševići | 205 | 26,654.300 | 130.000 | A |
| 891ef4582a7ffff | Centar Sarajevo | nan | 444 | 57,926.900 | 130.500 | B |
| 891ea92cc37ffff | Novi Grad Sarajevo | Dobroševići | 161 | 21,092.800 | 131.000 | A |
| 891ef4586a7ffff | Centar Sarajevo | nan | 109 | 14,301.800 | 131.200 | B |
| 891ea92cc6bffff | Novi Grad Sarajevo | Dobroševići | 43 | 5,643.100 | 131.200 | A |
| 891ef45809bffff | Centar Sarajevo | nan | 35 | 4,603.500 | 131.500 | B |
| 891ea92cc07ffff | Novi Grad Sarajevo | Dobroševići | 44 | 5,810.700 | 132.100 | A |
| 891ea92cd9bffff | Novi Grad Sarajevo | Dobroševići | 40 | 5,287.600 | 132.200 | A |
| 891ea92c8d7ffff | Novi Grad Sarajevo | Dobroševići | 136 | 18,002.100 | 132.400 | A |
| 891ea92cc7bffff | Novi Grad Sarajevo | Dobroševići | 65 | 8,616.900 | 132.600 | A |
| 891ef4580d7ffff | Centar Sarajevo | nan | 69 | 9,157.700 | 132.700 | B |
| 891ea92cc17ffff | Novi Grad Sarajevo | Dobroševići | 44 | 5,848.400 | 132.900 | A |
| 891ef45b12fffff | Centar Sarajevo | nan | 98 | 13,054.500 | 133.200 | B |
| 891ea92cc67ffff | Novi Grad Sarajevo | Dobroševići | 203 | 27,053.100 | 133.300 | A |
| 891ef45828bffff | Centar Sarajevo | nan | 431 | 57,656.800 | 133.800 | B |
| 891ea92cc73ffff | Novi Grad Sarajevo | Dobroševići | 109 | 14,589.400 | 133.800 | A |
| 891ea92ccc7ffff | Novi Grad Sarajevo | Dobroševići | 62 | 8,335.900 | 134.400 | A |

## 5. Vizuelna provjera
Stanovnici u zonama gdje ih ne bi trebalo biti (aproksimacija: ravnomjerno po dijelu polja):

| vrsta | procijenjeno_stanovnika (površinski) |
|---|---|
| aerodrom | 575.000 |
| landuse=industrial | 6,190.000 |
| park | 7,579.000 |

Najgušće MZ (od 62 sa poznatim granicama):

| rang | opcina | mz | st | st_po_km2 |
|---|---|---|---|---|
| 1 | Novi Grad Sarajevo | Dobrinja C | 2801 | 92,958.000 |
| 2 | Novi Grad Sarajevo | Alipašino Polje BII | 3161 | 29,065.000 |
| 3 | Novi Grad Sarajevo | Alipašino Polje BI | 3798 | 23,825.000 |
| 4 | Novo Sarajevo | Malta | 4396 | 22,763.000 |
| 5 | Novi Grad Sarajevo | Alipašino Polje CI | 2010 | 22,650.000 |
| 6 | Novo Sarajevo | Trg heroja | 5200 | 19,850.000 |
| 7 | Stari Grad Sarajevo | Ferhadija | 1743 | 18,941.000 |
| 8 | Novi Grad Sarajevo | Alipašino Polje CII | 2645 | 18,858.000 |
| 9 | Novi Grad Sarajevo | Staro Hrasno | 3062 | 18,670.000 |
| 10 | Novo Sarajevo | Grbavica I | 6221 | 18,651.000 |
| 11 | Stari Grad Sarajevo | Baščaršija | 3464 | 17,739.000 |
| 12 | Novo Sarajevo | Hrasno | 1854 | 16,925.000 |
| 13 | Novi Grad Sarajevo | Alipašin Most III | 6849 | 15,105.000 |
| 14 | Novo Sarajevo | Čengić Vila II | 1506 | 15,018.000 |
| 15 | Novo Sarajevo | Grbavica II | 5778 | 14,801.000 |

Dobrinja, Alipašino Polje, Grbavica (očekivano visoko):

| rang | opcina | mz | st | st_po_km2 |
|---|---|---|---|---|
| 1 | Novi Grad Sarajevo | Dobrinja C | 2801 | 92,958.000 |
| 2 | Novi Grad Sarajevo | Alipašino Polje BII | 3161 | 29,065.000 |
| 3 | Novi Grad Sarajevo | Alipašino Polje BI | 3798 | 23,825.000 |
| 5 | Novi Grad Sarajevo | Alipašino Polje CI | 2010 | 22,650.000 |
| 8 | Novi Grad Sarajevo | Alipašino Polje CII | 2645 | 18,858.000 |
| 10 | Novo Sarajevo | Grbavica I | 6221 | 18,651.000 |
| 15 | Novo Sarajevo | Grbavica II | 5778 | 14,801.000 |
| 23 | Novi Grad Sarajevo | Alipašino Polje AII | 2733 | 10,760.000 |
| 24 | Novi Grad Sarajevo | Dobrinja D | 5650 | 10,511.000 |
| 27 | Novi Grad Sarajevo | Alipašino Polje AI | 2476 | 8,452.000 |
| 28 | Novi Grad Sarajevo | Dobrinja B | 6942 | 8,398.000 |
| 32 | Novi Grad Sarajevo | Dobrinja A | 6476 | 7,816.000 |

Karta za vizuelni pregled: `out/karta.html`.

## 6. Starosne grupe
Zbir grupa = ukupno u svakom polju: **OK** (0 polja odstupa).

Odstupanje zbira grupa po općini od FZS-a (posljedica zaokruživanja po polju):

| opcina | d0_14 | d15_64 | d65plus |
|---|---|---|---|
| Centar Sarajevo | -5 | 0 | 5 |
| Novi Grad Sarajevo | -16 | 9 | 7 |
| Novo Sarajevo | -7 | 1 | 6 |
| Stari Grad Sarajevo | 1 | 5 | -6 |

## Napomene o modelu
- **Stari Grad Sarajevo**: Graf 3 nije potvrđen; samo zbir općine
- **Novi Grad Sarajevo**: MZ: β=0.5·udio_2010 + (1−β)·udio_modela; nove MZ s matičnom: nema; bez matične: ['Alipašin Most III', 'Zabrđe']
- Pouzdanost polja: {'B': 960, 'A': 368, 'C': 63}
