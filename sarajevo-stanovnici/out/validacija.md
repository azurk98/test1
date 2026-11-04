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

**MAPE po MZ: 16.4%** (glavna mjera kvaliteta modela)

| mz | graf3_udio | model_udio | rel_greska |
|---|---|---|---|
| Mošćanica | 0.116 | 0.178 | 0.544 |
| Mahmutovac | 0.056 | 0.033 | 0.414 |
| Kovači | 0.040 | 0.050 | 0.267 |
| Bistrik | 0.083 | 0.065 | 0.221 |
| Baščaršija | 0.056 | 0.066 | 0.167 |
| Medrese | 0.086 | 0.072 | 0.161 |
| Babića bašča | 0.043 | 0.036 | 0.159 |
| Sumbuluša | 0.038 | 0.033 | 0.143 |
| Mjedenica | 0.018 | 0.021 | 0.131 |
| Vratnik | 0.087 | 0.076 | 0.129 |
| Ferhadija | 0.029 | 0.032 | 0.088 |
| Toka-Džeka | 0.043 | 0.041 | 0.048 |
| Širokača | 0.068 | 0.065 | 0.045 |
| Sedrenik | 0.082 | 0.079 | 0.040 |
| Hrid-Jarčedoli | 0.065 | 0.067 | 0.033 |
| Logavina | 0.091 | 0.088 | 0.032 |

## 3. Novi Grad: model bez MZ ograničenja vs udjeli 2010
Udjeli 2010 preskalirani na dio općine bez novih MZ. Odstupanje > 30% je označeno; veće udjele u modelu obično objašnjava nova gradnja nakon 2010.

| mz | model_udio | udio_2010 | omjer | oznaka |
|---|---|---|---|---|
| Alipašino Polje CI | 0.010 | 0.023 | 0.422 | model < 2010 za >30%: provjeriti |
| Alipašin Most II | 0.012 | 0.025 | 0.487 | model < 2010 za >30%: provjeriti |
| Švrakino Selo I | 0.011 | 0.020 | 0.580 | model < 2010 za >30%: provjeriti |
| Čengić Vila | 0.019 | 0.031 | 0.619 | model < 2010 za >30%: provjeriti |
| Alipašino Polje CII | 0.015 | 0.023 | 0.660 | model < 2010 za >30%: provjeriti |
| Alipašino Polje AI | 0.016 | 0.024 | 0.682 | model < 2010 za >30%: provjeriti |
| Aneks | 0.020 | 0.028 | 0.709 |  |
| Alipašin Most I | 0.048 | 0.067 | 0.710 |  |
| Buća Potok | 0.035 | 0.045 | 0.767 |  |
| Dobrinja B | 0.039 | 0.050 | 0.776 |  |
| Olimpijsko Selo | 0.018 | 0.023 | 0.779 |  |
| Švrakino Selo II | 0.032 | 0.040 | 0.810 |  |
| Otoka | 0.021 | 0.026 | 0.823 |  |
| Švrakino Selo III | 0.015 | 0.018 | 0.826 |  |
| Dobrinja D | 0.040 | 0.048 | 0.832 |  |
| Alipašino Polje BII | 0.024 | 0.027 | 0.892 |  |
| Dobrinja C | 0.039 | 0.042 | 0.921 |  |
| Dolac | 0.046 | 0.050 | 0.922 |  |
| Alipašino Polje AII | 0.021 | 0.023 | 0.945 |  |
| Staro Hrasno | 0.026 | 0.024 | 1.062 |  |
| Alipašino Polje BI | 0.031 | 0.029 | 1.075 |  |
| Dobrinja A | 0.054 | 0.039 | 1.397 | model > 2010 za >30%: nova gradnja? |
| Naselje heroja Sokolje | 0.059 | 0.041 | 1.431 | model > 2010 za >30%: nova gradnja? |
| Saraj Polje | 0.061 | 0.041 | 1.475 | model > 2010 za >30%: nova gradnja? |
| Briješće | 0.077 | 0.037 | 2.057 | model > 2010 za >30%: nova gradnja? |
| Dobroševići | 0.066 | 0.030 | 2.231 | model > 2010 za >30%: nova gradnja? |
| Reljevo | 0.027 | 0.008 | 3.197 | model > 2010 za >30%: nova gradnja? |
| Alipašin Most III | 0.059 | nan | nan | nova MZ (nema 2010) |
| Zabrđe | 0.060 | nan | nan | nova MZ (nema 2010) |

Konačni udjeli korišteni kao meko ograničenje: vidi `interim/raspodjela_info.json`.

## 4. Gustina poda (stambeni m² po stanovniku, očekivano 15–60)
Medijan (polja s ≥ 10 st.): 87.9 m²/st. Polja izvan raspona: **615** od 729. Polja sa stanovnicima a bez stambenih zgrada (pouzdanost C, samo WorldPop): **23**.

| h3_id | opcina | mz | stanovnici | stambeni_m2 | m2_po_st | pouzdanost |
|---|---|---|---|---|---|---|
| 891ea92cd6fffff | Novi Grad Sarajevo | Zabrđe | 12 | 38.400 | 3.200 | A |
| 891ef459c77ffff | Stari Grad Sarajevo | Širokača | 20 | 145.900 | 7.300 | C |
| 891ef4596abffff | Novi Grad Sarajevo | Briješće | 122 | 971.800 | 8.000 | C |
| 891ef45866bffff | Centar Sarajevo | Gornji Velešići | 51 | 567.700 | 11.100 | B |
| 891ef45919bffff | Novo Sarajevo | Željeznička | 492 | 29,685.600 | 60.300 | B |
| 891ef4590a7ffff | Novo Sarajevo | Malta | 2018 | 121,846.900 | 60.400 | B |
| 891ef4592a3ffff | Novi Grad Sarajevo | Švrakino Selo II | 102 | 6,166.000 | 60.500 | A |
| 891ef45831bffff | Stari Grad Sarajevo | Sedrenik | 239 | 14,454.700 | 60.500 | A |
| 891ef459103ffff | Novo Sarajevo | Grbavica I | 1888 | 114,637.100 | 60.700 | B |
| 891ea92c943ffff | Novi Grad Sarajevo | Briješće | 190 | 11,558.800 | 60.800 | A |
| 891ef459023ffff | Novi Grad Sarajevo | Staro Hrasno | 1814 | 110,771.200 | 61.100 | A |
| 891ef4594c7ffff | Novi Grad Sarajevo | Zabrđe | 16 | 977.100 | 61.100 | A |
| 891ef45806fffff | Stari Grad Sarajevo | Sedrenik | 97 | 5,936.900 | 61.200 | A |
| 891ef459d57ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 33 | 2,029.100 | 61.500 | A |
| 891ef458203ffff | Centar Sarajevo | nan | 455 | 28,254.100 | 62.100 | B |
| 891ea92c96bffff | Novi Grad Sarajevo | Briješće | 124 | 7,702.900 | 62.100 | A |
| 891ef45960bffff | Novi Grad Sarajevo | Briješće | 15 | 933.100 | 62.200 | A |
| 891ef4591abffff | Novo Sarajevo | Kovačići | 1839 | 115,010.900 | 62.500 | B |
| 891ef45857bffff | Centar Sarajevo | Mošćanica | 20 | 1,265.900 | 63.300 | B |
| 891ef459487ffff | Novi Grad Sarajevo | Zabrđe | 12 | 760.400 | 63.400 | A |
| 891ef45844fffff | Centar Sarajevo | nan | 27 | 1,711.400 | 63.400 | B |
| 891ea92c853ffff | Novi Grad Sarajevo | Dobroševići | 13 | 826.800 | 63.600 | A |
| 891ef459cc7ffff | Centar Sarajevo | Širokača | 315 | 20,038.700 | 63.600 | B |
| 891ea92c94bffff | Novi Grad Sarajevo | Briješće | 46 | 2,933.000 | 63.800 | A |
| 891ea92cd2bffff | Novi Grad Sarajevo | Zabrđe | 447 | 28,507.700 | 63.800 | A |
| 891ef45928bffff | Novi Grad Sarajevo | Dobrinja A | 2132 | 136,013.600 | 63.800 | A |
| 891ef459c17ffff | Stari Grad Sarajevo | Bistrik | 776 | 49,634.200 | 64.000 | A |
| 891ef459dbbffff | Stari Grad Sarajevo | Mošćanica | 15 | 961.900 | 64.100 | A |
| 891ef4592abffff | Novi Grad Sarajevo | Dobrinja C | 176 | 11,287.700 | 64.100 | A |
| 891ea92cb97ffff | Novi Grad Sarajevo | Briješće | 29 | 1,869.400 | 64.500 | A |
| 891ef4590a3ffff | Novo Sarajevo | Pofalići II | 778 | 50,221.300 | 64.600 | B |
| 891ef45b203ffff | Novi Grad Sarajevo | Zabrđe | 21 | 1,356.300 | 64.600 | A |
| 891ef4595afffff | Novo Sarajevo | Velešići | 93 | 6,017.400 | 64.700 | B |
| 891ef459ca7ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 273 | 17,708.000 | 64.900 | A |
| 891ef458493ffff | Centar Sarajevo | nan | 34 | 2,218.400 | 65.200 | B |
| 891ef45844bffff | Centar Sarajevo | nan | 30 | 1,963.000 | 65.400 | B |
| 891ea92c833ffff | Novi Grad Sarajevo | Dobroševići | 52 | 3,409.300 | 65.600 | A |
| 891ef459013ffff | Novi Grad Sarajevo | Alipašin Most III | 1736 | 113,971.900 | 65.700 | A |
| 891ef459cb7ffff | Stari Grad Sarajevo | Babića bašča | 443 | 29,187.900 | 65.900 | A |
| 891ef458623ffff | Centar Sarajevo | nan | 29 | 1,920.700 | 66.200 | B |
| 891ef45825bffff | Novo Sarajevo | Velešići | 316 | 20,939.000 | 66.300 | B |
| 891ef459017ffff | Novo Sarajevo | Kvadrant | 1723 | 114,469.900 | 66.400 | B |
| 891ea92c9c3ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 252 | 16,749.000 | 66.500 | A |
| 891ef459107ffff | Novo Sarajevo | Grbavica I | 1612 | 107,197.100 | 66.500 | B |
| 891ef459dcbffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 101 | 6,767.000 | 67.000 | A |
| 891ef4592a7ffff | Novi Grad Sarajevo | Švrakino Selo II | 35 | 2,345.100 | 67.000 | A |
| 891ef45861bffff | Centar Sarajevo | nan | 19 | 1,273.400 | 67.000 | B |
| 891ef45912fffff | Novo Sarajevo | Gornji Kovačići | 28 | 1,877.800 | 67.100 | B |
| 891ea92c837ffff | Novi Grad Sarajevo | Briješće | 124 | 8,329.200 | 67.200 | A |
| 891ef45958bffff | Novi Grad Sarajevo | Dolac | 13 | 874.300 | 67.300 | A |
| 891ea92c817ffff | Novi Grad Sarajevo | Dobroševići | 40 | 2,690.300 | 67.300 | A |
| 891ef458407ffff | Centar Sarajevo | nan | 10 | 672.800 | 67.300 | B |
| 891ef4595dbffff | Novi Grad Sarajevo | Dolac | 39 | 2,626.400 | 67.300 | A |
| 891ef459603ffff | Novi Grad Sarajevo | Briješće | 361 | 24,312.900 | 67.300 | A |
| 891ef459c07ffff | Stari Grad Sarajevo | Mahmutovac | 610 | 41,293.900 | 67.700 | A |
| 891ea92c90bffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 201 | 13,608.500 | 67.700 | A |
| 891ef459433ffff | Novi Grad Sarajevo | Dolac | 58 | 3,929.400 | 67.700 | A |
| 891ef4591bbffff | Novo Sarajevo | Kovačići | 411 | 27,975.700 | 68.100 | B |
| 891ef459ddbffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 184 | 12,542.800 | 68.200 | A |
| 891ef45956bffff | Novo Sarajevo | Pofalići II | 1108 | 75,596.100 | 68.200 | B |
| 891ea92cd2fffff | Novi Grad Sarajevo | Zabrđe | 289 | 19,788.700 | 68.500 | A |
| 891ef458253ffff | Novo Sarajevo | Velešići | 985 | 67,508.100 | 68.500 | B |
| 891ef458143ffff | Stari Grad Sarajevo | Mošćanica | 17 | 1,165.800 | 68.600 | A |
| 891ef45824bffff | Centar Sarajevo | Velešići | 487 | 33,481.900 | 68.800 | B |
| 891ef459607ffff | Novi Grad Sarajevo | Saraj Polje | 767 | 52,926.400 | 69.000 | A |
| 891ef4590bbffff | Novo Sarajevo | Pofalići II | 440 | 30,416.000 | 69.100 | B |
| 891ef45830bffff | Stari Grad Sarajevo | Vratnik | 185 | 12,835.700 | 69.400 | A |
| 891ef458377ffff | Stari Grad Sarajevo | Mošćanica | 68 | 4,725.600 | 69.500 | A |
| 891ea92c8dbffff | Novi Grad Sarajevo | Dobroševići | 19 | 1,325.500 | 69.800 | A |
| 891ea92cd1bffff | Novi Grad Sarajevo | Dobroševići | 28 | 1,954.900 | 69.800 | A |
| 891ef459177ffff | Novo Sarajevo | Vraca | 74 | 5,169.700 | 69.900 | B |
| 891ea92ea6fffff | Novi Grad Sarajevo | Dobroševići | 16 | 1,123.600 | 70.200 | A |
| 891ef459c8fffff | Stari Grad Sarajevo | Bistrik | 744 | 52,385.300 | 70.400 | A |
| 891ef459667ffff | Novi Grad Sarajevo | Saraj Polje | 1801 | 127,024.300 | 70.500 | A |
| 891ef459543ffff | Novi Grad Sarajevo | Dolac | 267 | 18,947.300 | 71.000 | A |
| 891ef45868bffff | Centar Sarajevo | nan | 23 | 1,632.700 | 71.000 | B |
| 891ea92ceb7ffff | Novi Grad Sarajevo | Dobroševići | 19 | 1,353.600 | 71.200 | A |
| 891ef45836fffff | Stari Grad Sarajevo | Babića bašča | 36 | 2,566.800 | 71.300 | A |
| 891ef4596a3ffff | Novi Grad Sarajevo | Alipašin Most I | 400 | 28,640.800 | 71.600 | A |
| 891ef4586bbffff | Centar Sarajevo | nan | 38 | 2,728.700 | 71.800 | B |
| 891ef459073ffff | Novi Grad Sarajevo | Švrakino Selo I | 680 | 48,876.100 | 71.900 | A |
| 891ef4596a7ffff | Novi Grad Sarajevo | Alipašin Most I | 847 | 60,968.800 | 72.000 | A |
| 891ef45b25bffff | Novi Grad Sarajevo | Zabrđe | 187 | 13,476.200 | 72.100 | A |
| 891ef459193ffff | Novo Sarajevo | Pofalići I | 375 | 27,031.700 | 72.100 | B |
| 891ef459077ffff | Novi Grad Sarajevo | Švrakino Selo III | 647 | 46,672.900 | 72.100 | A |
| 891ef459477ffff | Novi Grad Sarajevo | Alipašin Most I | 255 | 18,421.900 | 72.200 | A |
| 891ef458073ffff | Centar Sarajevo | nan | 49 | 3,540.100 | 72.200 | B |
| 891ef4596b7ffff | Novi Grad Sarajevo | Alipašin Most I | 531 | 38,424.200 | 72.400 | A |
| 891ef4583cfffff | Stari Grad Sarajevo | Medrese | 551 | 39,960.500 | 72.500 | A |
| 891ef4599d3ffff | Stari Grad Sarajevo | Širokača | 10 | 728.200 | 72.800 | A |
| 891ef45907bffff | Novi Grad Sarajevo | Švrakino Selo I | 521 | 37,942.800 | 72.800 | A |
| 891ef45909bffff | Novi Grad Sarajevo | Buća Potok | 623 | 45,956.000 | 73.800 | A |
| 891ef45b277ffff | Novi Grad Sarajevo | Zabrđe | 23 | 1,696.700 | 73.800 | A |
| 891ef459157ffff | Novo Sarajevo | Vraca | 750 | 55,559.700 | 74.100 | B |
| 891ea92eb07ffff | Novi Grad Sarajevo | Reljevo | 26 | 1,928.700 | 74.200 | A |
| 891ef4590b7ffff | Novo Sarajevo | Pofalići II | 155 | 11,512.200 | 74.300 | B |
| 891ef4582d7ffff | Centar Sarajevo | nan | 394 | 29,281.600 | 74.300 | B |
| 891ef459c0fffff | Stari Grad Sarajevo | Toka-Džeka | 295 | 21,936.400 | 74.400 | A |
| 891ef45b167ffff | Centar Sarajevo | nan | 12 | 893.500 | 74.500 | B |
| 891ef4590d3ffff | Novi Grad Sarajevo | Alipašin Most I | 775 | 57,769.300 | 74.500 | A |
| 891ea92c96fffff | Novi Grad Sarajevo | Briješće | 191 | 14,309.700 | 74.900 | A |
| 891ef459127ffff | Centar Sarajevo | Gornji Kovačići | 135 | 10,126.400 | 75.000 | B |
| 891ef45946fffff | Novi Grad Sarajevo | Buća Potok | 655 | 49,154.100 | 75.000 | A |
| 891ef458363ffff | Stari Grad Sarajevo | Vratnik | 147 | 11,043.900 | 75.100 | A |
| 891ef458627ffff | Centar Sarajevo | nan | 110 | 8,284.500 | 75.300 | B |
| 891ef45840fffff | Centar Sarajevo | nan | 11 | 828.800 | 75.300 | B |
| 891ef459257ffff | Novi Grad Sarajevo | Dobrinja B | 660 | 49,878.100 | 75.600 | A |
| 891ef459c73ffff | Stari Grad Sarajevo | Širokača | 66 | 4,996.700 | 75.700 | A |
| 891ea92c8bbffff | Novi Grad Sarajevo | Dobroševići | 106 | 8,033.700 | 75.800 | A |
| 891ef458443ffff | Centar Sarajevo | nan | 39 | 2,957.300 | 75.800 | B |
| 891ef45847bffff | Centar Sarajevo | nan | 41 | 3,117.400 | 76.000 | B |
| 891ef459c1bffff | Stari Grad Sarajevo | Širokača | 359 | 27,328.600 | 76.100 | A |
| 891ef458357ffff | Stari Grad Sarajevo | Sumbuluša | 554 | 42,282.500 | 76.300 | A |
| 891ef459dd7ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 82 | 6,268.400 | 76.400 | A |
| 891ef458573ffff | Centar Sarajevo | Mošćanica | 18 | 1,376.100 | 76.500 | B |
| 891ef459ca3ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 646 | 49,478.200 | 76.600 | A |
| 891ef459c27ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 57 | 4,366.300 | 76.600 | A |
| 891ea92c947ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 74 | 5,673.900 | 76.700 | A |
| 891ea92ccb3ffff | Novi Grad Sarajevo | Dobroševići | 28 | 2,150.400 | 76.800 | A |
| 891ef459cbbffff | Stari Grad Sarajevo | Bistrik | 1034 | 79,576.500 | 77.000 | A |
| 891ef45824fffff | Centar Sarajevo | nan | 486 | 37,422.900 | 77.000 | B |
| 891ef45845bffff | Centar Sarajevo | nan | 14 | 1,078.300 | 77.000 | B |
| 891ef45834fffff | Stari Grad Sarajevo | Vratnik | 529 | 40,784.600 | 77.100 | A |
| 891ef459173ffff | Novo Sarajevo | Vraca | 317 | 24,486.700 | 77.200 | B |
| 891ef4582d3ffff | Centar Sarajevo | Gornji Velešići | 179 | 13,827.100 | 77.200 | B |
| 891ea92c9b7ffff | Novi Grad Sarajevo | Zabrđe | 42 | 3,246.700 | 77.300 | A |
| 891ef459c37ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 243 | 18,836.300 | 77.500 | A |
| 891ef45944fffff | Novi Grad Sarajevo | Alipašin Most I | 540 | 41,902.400 | 77.600 | A |
| 891ef45918fffff | Novo Sarajevo | Željeznička | 702 | 54,473.100 | 77.600 | B |
| 891ef45929bffff | Novi Grad Sarajevo | Saraj Polje | 635 | 49,324.000 | 77.700 | A |
| 891ef459447ffff | Novi Grad Sarajevo | Alipašin Most I | 405 | 31,511.300 | 77.800 | A |
| 891ef459473ffff | Novi Grad Sarajevo | Alipašin Most I | 447 | 34,789.200 | 77.800 | A |
| 891ef4583c3ffff | Stari Grad Sarajevo | Sedrenik | 447 | 34,837.400 | 77.900 | A |
| 891ef45946bffff | Novi Grad Sarajevo | Alipašin Most I | 652 | 50,879.200 | 78.000 | A |
| 891ef459463ffff | Novi Grad Sarajevo | Alipašin Most I | 480 | 37,465.100 | 78.100 | A |
| 891ef4583cbffff | Stari Grad Sarajevo | Medrese | 746 | 58,286.900 | 78.100 | A |
| 891ea92c99bffff | Novi Grad Sarajevo | Zabrđe | 114 | 8,913.100 | 78.200 | A |
| 891ea92eb87ffff | Novi Grad Sarajevo | Reljevo | 35 | 2,747.000 | 78.500 | A |
| 891ef4595b7ffff | Centar Sarajevo | Gornji Velešići | 171 | 13,435.300 | 78.600 | B |
| 891ef458063ffff | Centar Sarajevo | Sedrenik | 55 | 4,324.400 | 78.600 | B |
| 891ef45b2cfffff | Novi Grad Sarajevo | Reljevo | 386 | 30,367.700 | 78.700 | A |
| 891ea92eb53ffff | Novi Grad Sarajevo | Dobroševići | 19 | 1,496.300 | 78.800 | A |
| 891ea92c8d3ffff | Novi Grad Sarajevo | Dobroševići | 61 | 4,807.100 | 78.800 | A |
| 891ef45947bffff | Novi Grad Sarajevo | Alipašin Most I | 720 | 56,817.800 | 78.900 | A |
| 891ef459153ffff | Novo Sarajevo | Hrasno Brdo | 822 | 64,933.500 | 79.000 | B |
| 891ef4590b3ffff | Novo Sarajevo | Pofalići II | 250 | 19,749.500 | 79.000 | B |
| 891ef459d8bffff | Stari Grad Sarajevo | Babića bašča | 17 | 1,343.000 | 79.000 | A |
| 891ef459097ffff | Novi Grad Sarajevo | Dolac | 488 | 38,693.900 | 79.300 | A |
| 891ef459527ffff | Novo Sarajevo | Velešići | 523 | 41,529.600 | 79.400 | B |
| 891ef458667ffff | Centar Sarajevo | nan | 160 | 12,718.200 | 79.500 | B |
| 891ea92c973ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 286 | 22,751.600 | 79.600 | A |
| 891ef45961bffff | Novi Grad Sarajevo | Briješće | 310 | 24,714.800 | 79.700 | A |
| 891ef459cc3ffff | Centar Sarajevo | nan | 466 | 37,194.900 | 79.800 | B |
| 891ef45902bffff | Novi Grad Sarajevo | Aneks | 690 | 55,107.900 | 79.900 | A |
| 891ef459c13ffff | Stari Grad Sarajevo | Širokača | 679 | 54,262.500 | 79.900 | A |
| 891ea92eb17ffff | Novi Grad Sarajevo | Reljevo | 11 | 879.900 | 80.000 | A |
| 891ef45914fffff | Novo Sarajevo | Vraca | 52 | 4,161.300 | 80.000 | B |
| 891ef4592c7ffff | Novi Grad Sarajevo | Dobrinja A | 740 | 59,271.300 | 80.100 | A |
| 891ef458207ffff | Centar Sarajevo | nan | 506 | 40,542.800 | 80.100 | B |
| 891ef459cb3ffff | Stari Grad Sarajevo | Babića bašča | 977 | 78,299.100 | 80.100 | A |
| 891ef458173ffff | Stari Grad Sarajevo | Mošćanica | 15 | 1,202.800 | 80.200 | A |
| 891ef458683ffff | Centar Sarajevo | nan | 68 | 5,473.700 | 80.500 | B |
| 891ef459d9bffff | Stari Grad Sarajevo | Mošćanica | 37 | 2,980.800 | 80.600 | A |
| 891ef45920bffff | Novi Grad Sarajevo | Dobrinja B | 916 | 73,952.200 | 80.700 | A |
| 891ea92cd57ffff | Novi Grad Sarajevo | Dobroševići | 30 | 2,425.800 | 80.900 | A |
| 891ef45910bffff | Novo Sarajevo | Vraca | 819 | 66,320.800 | 81.000 | B |
| 891ef45906bffff | Novi Grad Sarajevo | Švrakino Selo II | 273 | 22,144.000 | 81.100 | A |
| 891ef459c57ffff | Stari Grad Sarajevo | Širokača | 200 | 16,223.500 | 81.100 | A |
| 891ea92c9a7ffff | Novi Grad Sarajevo | Zabrđe | 158 | 12,818.000 | 81.100 | A |
| 891ef4583d7ffff | Stari Grad Sarajevo | Sedrenik | 297 | 24,127.900 | 81.200 | A |
| 891ef45954fffff | Novo Sarajevo | Pofalići II | 214 | 17,396.100 | 81.300 | B |
| 891ef458647ffff | Centar Sarajevo | nan | 286 | 23,290.200 | 81.400 | B |
| 891ef45b24fffff | Novi Grad Sarajevo | Zabrđe | 29 | 2,364.600 | 81.500 | A |
| 891ef458243ffff | Centar Sarajevo | Velešići | 575 | 46,890.100 | 81.500 | B |
| 891ef459083ffff | Novi Grad Sarajevo | Buća Potok | 737 | 60,190.300 | 81.700 | A |
| 891ef4591afffff | Centar Sarajevo | Kovačići | 446 | 36,503.000 | 81.800 | B |
| 891ef459817ffff | Stari Grad Sarajevo | Širokača | 24 | 1,965.900 | 81.900 | A |
| 891ef4586b3ffff | Centar Sarajevo | nan | 72 | 5,907.000 | 82.000 | B |
| 891ea92c957ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 605 | 49,636.100 | 82.000 | A |
| 891ef459567ffff | Novo Sarajevo | Pofalići I | 619 | 50,831.900 | 82.100 | B |
| 891ef4582dbffff | Novo Sarajevo | Gornji Velešići | 297 | 24,413.800 | 82.200 | B |
| 891ea92c963ffff | Novi Grad Sarajevo | Briješće | 238 | 19,573.400 | 82.200 | A |
| 891ef4582c3ffff | Novo Sarajevo | Gornji Velešići | 422 | 34,720.000 | 82.300 | B |
| 891ef45b20bffff | Novi Grad Sarajevo | Zabrđe | 56 | 4,620.600 | 82.500 | A |
| 891ef45836bffff | Stari Grad Sarajevo | Vratnik | 140 | 11,570.700 | 82.600 | A |
| 891ea92cc1bffff | Novi Grad Sarajevo | Dobroševići | 68 | 5,626.000 | 82.700 | A |
| 891ef459dc3ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 210 | 17,376.200 | 82.700 | A |
| 891ef45940fffff | Novi Grad Sarajevo | Dolac | 158 | 13,091.500 | 82.900 | A |
| 891ef459027ffff | Novo Sarajevo | Hrasno Brdo | 805 | 66,800.200 | 83.000 | B |
| 891ef458353ffff | Stari Grad Sarajevo | Medrese | 947 | 78,637.300 | 83.000 | A |
| 891ef458663ffff | Centar Sarajevo | nan | 498 | 41,353.900 | 83.000 | B |
| 891ef459c53ffff | Centar Sarajevo | Širokača | 107 | 8,890.400 | 83.100 | B |
| 891ef4591b3ffff | Centar Sarajevo | Željeznička | 969 | 80,588.400 | 83.200 | B |
| 891ef459533ffff | Novo Sarajevo | Velešići | 76 | 6,323.600 | 83.200 | B |
| 891ef4584cbffff | Centar Sarajevo | nan | 44 | 3,664.400 | 83.300 | B |
| 891ef45832fffff | Stari Grad Sarajevo | Mošćanica | 34 | 2,833.600 | 83.300 | A |
| 891ea92eb0bffff | Novi Grad Sarajevo | Reljevo | 15 | 1,250.700 | 83.400 | A |
| 891ef4592b7ffff | Novi Grad Sarajevo | Švrakino Selo II | 407 | 33,964.800 | 83.500 | A |
| 891ef459c03ffff | Stari Grad Sarajevo | Toka-Džeka | 508 | 42,408.400 | 83.500 | A |
| 891ea92c9cfffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 295 | 24,630.400 | 83.500 | A |
| 891ef459563ffff | Novo Sarajevo | Pofalići II | 433 | 36,227.300 | 83.700 | B |
| 891ea92c983ffff | Novi Grad Sarajevo | Zabrđe | 257 | 21,505.700 | 83.700 | A |
| 891ef45904fffff | Novi Grad Sarajevo | Švrakino Selo II | 615 | 51,469.200 | 83.700 | A |
| 891ef4583dbffff | Stari Grad Sarajevo | Sedrenik | 505 | 42,281.500 | 83.700 | A |
| 891ef45804fffff | Centar Sarajevo | nan | 211 | 17,688.400 | 83.800 | B |
| 891ef459393ffff | Novi Grad Sarajevo | Aneks | 571 | 47,973.700 | 84.000 | A |
| 891ef459dc7ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 85 | 7,143.100 | 84.000 | A |
| 891ef458283ffff | Centar Sarajevo | nan | 497 | 41,924.300 | 84.400 | B |
| 891ef459573ffff | Novo Sarajevo | Pofalići II | 682 | 57,589.800 | 84.400 | B |
| 891ef458417ffff | Centar Sarajevo | nan | 42 | 3,552.300 | 84.600 | B |
| 891ef4594dbffff | Novi Grad Sarajevo | Zabrđe | 184 | 15,567.400 | 84.600 | A |
| 891ef6965a7ffff | Novi Grad Sarajevo | Saraj Polje | 357 | 30,332.000 | 85.000 | A |
| 891ea92c913ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 264 | 22,454.700 | 85.100 | A |
| 891ef459d97ffff | Stari Grad Sarajevo | Mošćanica | 16 | 1,363.000 | 85.200 | A |
| 891ef459063ffff | Novi Grad Sarajevo | Švrakino Selo III | 608 | 51,834.200 | 85.300 | A |
| 891ef45848fffff | Centar Sarajevo | nan | 37 | 3,155.800 | 85.300 | B |
| 891ef45b257ffff | Novi Grad Sarajevo | Zabrđe | 58 | 4,953.600 | 85.400 | A |
| 891ef458273ffff | Centar Sarajevo | nan | 769 | 65,835.600 | 85.600 | B |
| 891ef4580b7ffff | Centar Sarajevo | nan | 14 | 1,199.500 | 85.700 | B |
| 891ef459067ffff | Novi Grad Sarajevo | Švrakino Selo III | 560 | 47,983.200 | 85.700 | A |
| 891ef45942fffff | Novi Grad Sarajevo | Dolac | 675 | 57,860.000 | 85.700 | A |
| 891ef45943bffff | Novi Grad Sarajevo | Dolac | 145 | 12,432.700 | 85.700 | A |
| 891ea92c987ffff | Novi Grad Sarajevo | Zabrđe | 513 | 44,091.600 | 85.900 | A |
| 891ef45b12bffff | Centar Sarajevo | nan | 35 | 3,010.700 | 86.000 | B |
| 891ef458067ffff | Stari Grad Sarajevo | Sedrenik | 25 | 2,151.000 | 86.000 | A |
| 891ef458637ffff | Centar Sarajevo | nan | 56 | 4,819.400 | 86.100 | B |
| 891ef45955bffff | Novi Grad Sarajevo | Dolac | 828 | 71,276.600 | 86.100 | A |
| 891ea92c903ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 320 | 27,604.300 | 86.300 | A |
| 891ef45b20fffff | Novi Grad Sarajevo | Zabrđe | 36 | 3,105.700 | 86.300 | A |
| 891ea92c823ffff | Novi Grad Sarajevo | Briješće | 41 | 3,539.700 | 86.300 | A |
| 891ef459523ffff | Novo Sarajevo | Velešići | 261 | 22,551.100 | 86.400 | B |
| 891ef458603ffff | Centar Sarajevo | nan | 16 | 1,382.900 | 86.400 | B |
| 891ef45968bffff | Novi Grad Sarajevo | Briješće | 64 | 5,535.100 | 86.500 | A |
| 891ef45b127ffff | Centar Sarajevo | nan | 31 | 2,682.000 | 86.500 | B |
| 891ef459547ffff | Novo Sarajevo | Pofalići II | 102 | 8,832.300 | 86.600 | B |
| 891ef4595a7ffff | Novo Sarajevo | Gornji Velešići | 77 | 6,677.300 | 86.700 | B |
| 891ef458547ffff | Centar Sarajevo | nan | 42 | 3,645.200 | 86.800 | B |
| 891ef4595b3ffff | Centar Sarajevo | Velešići | 91 | 7,903.800 | 86.900 | B |
| 891ef459133ffff | Novo Sarajevo | Gornji Kovačići | 470 | 40,902.200 | 87.000 | B |
| 891ea92cc8bffff | Novi Grad Sarajevo | Dobroševići | 90 | 7,832.600 | 87.000 | A |
| 891ef45864fffff | Centar Sarajevo | nan | 326 | 28,386.600 | 87.100 | B |
| 891ef459cdbffff | Centar Sarajevo | nan | 560 | 48,843.100 | 87.200 | B |
| 891ef45826bffff | Centar Sarajevo | nan | 719 | 62,761.900 | 87.300 | B |
| 891ef4582afffff | Centar Sarajevo | nan | 452 | 39,472.500 | 87.300 | B |
| 891ef458313ffff | Stari Grad Sarajevo | Sedrenik | 308 | 26,909.600 | 87.400 | A |
| 891ef4591a7ffff | Centar Sarajevo | nan | 520 | 45,490.100 | 87.500 | B |
| 891ef459577ffff | Novo Sarajevo | Pofalići I | 665 | 58,221.300 | 87.600 | B |
| 891ef45849bffff | Centar Sarajevo | nan | 31 | 2,715.700 | 87.600 | B |
| 891ef458237ffff | Centar Sarajevo | Logavina | 634 | 55,542.500 | 87.600 | B |
| 891ef458693ffff | Centar Sarajevo | nan | 96 | 8,426.200 | 87.800 | B |
| 891ef4581dbffff | Stari Grad Sarajevo | Mošćanica | 24 | 2,109.800 | 87.900 | A |
| 891ef458057ffff | Centar Sarajevo | nan | 97 | 8,531.400 | 88.000 | B |
| 891ef458087ffff | Centar Sarajevo | nan | 17 | 1,495.500 | 88.000 | B |
| 891ef4592c3ffff | Novi Grad Sarajevo | Dobrinja A | 878 | 77,267.200 | 88.000 | A |
| 891ef459ccfffff | Centar Sarajevo | Širokača | 330 | 29,045.600 | 88.000 | B |
| 891ef4584d7ffff | Centar Sarajevo | nan | 10 | 881.000 | 88.100 | B |
| 891ef459137ffff | Centar Sarajevo | Gornji Kovačići | 360 | 31,773.900 | 88.300 | B |
| 891ef4596d7ffff | Novi Grad Sarajevo | Briješće | 68 | 6,003.000 | 88.300 | A |
| 891ef45807bffff | Centar Sarajevo | nan | 145 | 12,807.800 | 88.300 | B |
| 891ef4595c3ffff | Novi Grad Sarajevo | Dolac | 13 | 1,148.900 | 88.400 | A |
| 891ef458453ffff | Centar Sarajevo | nan | 60 | 5,304.600 | 88.400 | B |
| 891ef45833bffff | Stari Grad Sarajevo | Mošćanica | 112 | 9,905.000 | 88.400 | A |
| 891ef459443ffff | Novi Grad Sarajevo | Alipašin Most I | 96 | 8,490.300 | 88.400 | A |
| 891ef459507ffff | Novo Sarajevo | Pofalići I | 73 | 6,456.400 | 88.400 | B |
| 891ef4580cbffff | Centar Sarajevo | nan | 163 | 14,431.300 | 88.500 | B |
| 891ef459093ffff | Novi Grad Sarajevo | Dolac | 902 | 79,897.000 | 88.600 | A |
| 891ea92eb13ffff | Novi Grad Sarajevo | Reljevo | 21 | 1,861.000 | 88.600 | A |
| 891ef45910fffff | Novo Sarajevo | Vraca | 435 | 38,564.500 | 88.700 | B |
| 891ef45866fffff | Centar Sarajevo | nan | 332 | 29,458.200 | 88.700 | B |
| 891ef45805bffff | Centar Sarajevo | nan | 281 | 24,937.800 | 88.700 | B |
| 891ef4594cbffff | Novi Grad Sarajevo | Zabrđe | 35 | 3,106.400 | 88.800 | A |
| 891ea92eb8bffff | Novi Grad Sarajevo | Reljevo | 10 | 887.900 | 88.800 | A |
| 891ef4596c3ffff | Novi Grad Sarajevo | Briješće | 40 | 3,561.300 | 89.000 | A |
| 891ea92c98bffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 210 | 18,706.300 | 89.100 | A |
| 891ef45b24bffff | Novi Grad Sarajevo | Zabrđe | 253 | 22,548.000 | 89.100 | A |
| 891ef459467ffff | Novi Grad Sarajevo | Dolac | 575 | 51,273.800 | 89.200 | A |
| 891ef459123ffff | Novo Sarajevo | Gornji Kovačići | 117 | 10,439.900 | 89.200 | B |
| 891ef4595a3ffff | Novo Sarajevo | Velešići | 136 | 12,141.100 | 89.300 | B |
| 891ef45848bffff | Centar Sarajevo | nan | 66 | 5,896.600 | 89.300 | B |
| 891ef4584abffff | Centar Sarajevo | nan | 23 | 2,055.300 | 89.400 | B |
| 891ea92c8c3ffff | Novi Grad Sarajevo | Dobroševići | 66 | 5,898.600 | 89.400 | A |
| 891ef45a267ffff | Centar Sarajevo | nan | 18 | 1,613.000 | 89.600 | B |
| 891ea92c9d7ffff | Novi Grad Sarajevo | Zabrđe | 145 | 12,998.000 | 89.600 | A |
| 891ef45952fffff | Novo Sarajevo | Pofalići I | 459 | 41,183.500 | 89.700 | B |
| 891ef4583c7ffff | Stari Grad Sarajevo | Sedrenik | 452 | 40,600.500 | 89.800 | A |
| 891ef458473ffff | Centar Sarajevo | nan | 38 | 3,416.600 | 89.900 | B |
| 891ef45820fffff | Centar Sarajevo | nan | 763 | 68,719.700 | 90.100 | B |
| 891ef45912bffff | Novo Sarajevo | Gornji Kovačići | 53 | 4,783.800 | 90.300 | B |
| 891ea92c9bbffff | Novi Grad Sarajevo | Zabrđe | 377 | 34,032.800 | 90.300 | A |
| 891ea92c9afffff | Novi Grad Sarajevo | Zabrđe | 113 | 10,211.000 | 90.400 | A |
| 891ef459c0bffff | Stari Grad Sarajevo | Širokača | 385 | 34,789.700 | 90.400 | A |
| 891ef45906fffff | Novo Sarajevo | Hrasno Brdo | 172 | 15,560.300 | 90.500 | B |
| 891ef458303ffff | Stari Grad Sarajevo | Mošćanica | 124 | 11,221.200 | 90.500 | A |
| 891ea92c9b3ffff | Novi Grad Sarajevo | Zabrđe | 219 | 19,835.300 | 90.600 | A |
| 891ea92cd23ffff | Novi Grad Sarajevo | Zabrđe | 379 | 34,351.000 | 90.600 | A |
| 891ef4582bbffff | Centar Sarajevo | nan | 511 | 46,380.100 | 90.800 | B |
| 891ef45867bffff | Centar Sarajevo | nan | 469 | 42,625.000 | 90.900 | B |
| 891ea92eb4bffff | Novi Grad Sarajevo | Dobroševići | 18 | 1,637.300 | 91.000 | A |
| 891ef458247ffff | Centar Sarajevo | nan | 877 | 79,813.000 | 91.000 | B |
| 891ef458347ffff | Stari Grad Sarajevo | Vratnik | 864 | 78,657.200 | 91.000 | A |
| 891ef4580c7ffff | Centar Sarajevo | nan | 12 | 1,093.300 | 91.100 | B |
| 891ea92c937ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 64 | 5,836.900 | 91.200 | A |
| 891ef458227ffff | Stari Grad Sarajevo | Logavina | 890 | 81,292.800 | 91.300 | A |
| 891ef459553ffff | Novi Grad Sarajevo | Dolac | 221 | 20,187.700 | 91.300 | A |
| 891ef459427ffff | Novi Grad Sarajevo | Dolac | 357 | 32,612.100 | 91.400 | A |
| 891ea92cd37ffff | Novi Grad Sarajevo | Reljevo | 33 | 3,015.400 | 91.400 | A |
| 891ef459557ffff | Novi Grad Sarajevo | Dolac | 73 | 6,671.800 | 91.400 | A |
| 891ef45953bffff | Novo Sarajevo | Pofalići I | 257 | 23,491.000 | 91.400 | B |
| 891ef458077ffff | Centar Sarajevo | Sedrenik | 22 | 2,010.900 | 91.400 | B |
| 891ef4580c3ffff | Centar Sarajevo | nan | 128 | 11,706.000 | 91.500 | B |
| 891ef45837bffff | Stari Grad Sarajevo | Vratnik | 773 | 70,704.400 | 91.500 | A |
| 891ea92c9c7ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 829 | 75,841.000 | 91.500 | A |
| 891ef459c8bffff | Stari Grad Sarajevo | Mjedenica | 846 | 77,474.500 | 91.600 | B |
| 891ea92c997ffff | Novi Grad Sarajevo | Zabrđe | 411 | 37,648.000 | 91.600 | A |
| 891ef45957bffff | Novo Sarajevo | Pofalići II | 400 | 36,643.900 | 91.600 | B |
| 891ef458013ffff | Centar Sarajevo | nan | 47 | 4,307.100 | 91.600 | B |
| 891ef4582cbffff | Novo Sarajevo | Gornji Velešići | 685 | 62,781.600 | 91.700 | B |
| 891ea92c91bffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 537 | 49,284.500 | 91.800 | A |
| 891ea92cdc7ffff | Novi Grad Sarajevo | Dobroševići | 23 | 2,113.900 | 91.900 | A |
| 891ef45804bffff | Centar Sarajevo | nan | 372 | 34,288.800 | 92.200 | B |
| 891ef45902fffff | Novo Sarajevo | Hrasno Brdo | 542 | 50,006.800 | 92.300 | B |
| 891ea92c9a3ffff | Novi Grad Sarajevo | Zabrđe | 261 | 24,082.300 | 92.300 | A |
| 891ef459423ffff | Novi Grad Sarajevo | Dolac | 525 | 48,465.900 | 92.300 | A |
| 891ef458217ffff | Centar Sarajevo | nan | 689 | 63,653.400 | 92.400 | B |
| 891ef458643ffff | Centar Sarajevo | nan | 176 | 16,261.800 | 92.400 | B |
| 891ef4584cfffff | Centar Sarajevo | nan | 45 | 4,168.500 | 92.600 | B |
| 891ef458457ffff | Centar Sarajevo | nan | 25 | 2,316.800 | 92.700 | B |
| 891ea92c90fffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 315 | 29,192.200 | 92.700 | A |
| 891ef458403ffff | Centar Sarajevo | nan | 76 | 7,044.200 | 92.700 | B |
| 891ef45838bffff | Stari Grad Sarajevo | Sedrenik | 242 | 22,441.800 | 92.700 | A |
| 891ef458497ffff | Centar Sarajevo | nan | 37 | 3,432.700 | 92.800 | B |
| 891ef458213ffff | Centar Sarajevo | nan | 631 | 58,628.700 | 92.900 | B |
| 891ef459147ffff | Novo Sarajevo | Vraca | 384 | 35,736.900 | 93.100 | B |
| 891ef45b247ffff | Novi Grad Sarajevo | Zabrđe | 66 | 6,149.700 | 93.200 | A |
| 891ef459613ffff | Novi Grad Sarajevo | Briješće | 149 | 13,916.700 | 93.400 | A |
| 891ef45820bffff | Centar Sarajevo | nan | 1158 | 108,469.500 | 93.700 | B |
| 891ef45b253ffff | Novi Grad Sarajevo | Zabrđe | 183 | 17,144.500 | 93.700 | A |
| 891ef45a35bffff | Centar Sarajevo | nan | 14 | 1,313.500 | 93.800 | B |
| 891ef45942bffff | Novi Grad Sarajevo | Dolac | 626 | 58,771.000 | 93.900 | A |
| 891ef459397ffff | Novo Sarajevo | Hrasno Brdo | 242 | 22,753.800 | 94.000 | B |
| 891ef458297ffff | Centar Sarajevo | nan | 475 | 44,672.800 | 94.000 | B |
| 891ef45869bffff | Centar Sarajevo | nan | 14 | 1,320.100 | 94.300 | B |
| 891ef45914bffff | Novo Sarajevo | Hrasno Brdo | 148 | 13,962.200 | 94.300 | B |
| 891ef4592d7ffff | Novi Grad Sarajevo | Saraj Polje | 503 | 47,462.100 | 94.400 | A |
| 891ef4591b7ffff | Centar Sarajevo | nan | 812 | 76,756.600 | 94.500 | B |
| 891ef4580dbffff | Centar Sarajevo | nan | 110 | 10,423.000 | 94.800 | B |
| 891ef4582c7ffff | Centar Sarajevo | nan | 602 | 57,072.400 | 94.800 | B |
| 891ef4582cfffff | Centar Sarajevo | Velešići | 1033 | 97,943.700 | 94.800 | B |
| 891ef45821bffff | Centar Sarajevo | nan | 986 | 93,498.700 | 94.800 | B |
| 891ef4595abffff | Novo Sarajevo | Velešići | 74 | 7,035.100 | 95.100 | B |
| 891ea92c98fffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 183 | 17,420.400 | 95.200 | A |
| 891ef45952bffff | Novo Sarajevo | Pofalići I | 562 | 53,587.900 | 95.400 | B |
| 891ea92eb1bffff | Novi Grad Sarajevo | Reljevo | 24 | 2,289.200 | 95.400 | A |
| 891ef4586b7ffff | Centar Sarajevo | nan | 115 | 10,976.900 | 95.500 | B |
| 891ef45913bffff | Novo Sarajevo | Gornji Kovačići | 330 | 31,545.900 | 95.600 | B |
| 891ea92cca3ffff | Novi Grad Sarajevo | Dobroševići | 51 | 4,877.600 | 95.600 | A |
| 891ea92c9abffff | Novi Grad Sarajevo | Zabrđe | 235 | 22,526.500 | 95.900 | A |
| 891ef458293ffff | Centar Sarajevo | nan | 178 | 17,066.300 | 95.900 | B |
| 891ef459537ffff | Novo Sarajevo | Velešići | 427 | 40,974.400 | 96.000 | B |
| 891ef458447ffff | Centar Sarajevo | nan | 29 | 2,784.600 | 96.000 | B |
| 891ef45822fffff | Stari Grad Sarajevo | Logavina | 950 | 91,265.400 | 96.100 | A |
| 891ef459ccbffff | Centar Sarajevo | nan | 487 | 47,140.300 | 96.800 | B |
| 891ef459d0bffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 14 | 1,358.600 | 97.000 | A |
| 891ef45854fffff | Centar Sarajevo | nan | 76 | 7,376.500 | 97.100 | B |
| 891ef45939bffff | Novo Sarajevo | Hrasno Brdo | 132 | 12,823.900 | 97.200 | B |
| 891ef458373ffff | Stari Grad Sarajevo | Vratnik | 528 | 51,312.600 | 97.200 | A |
| 891ef45950fffff | Novo Sarajevo | Pofalići II | 322 | 31,321.900 | 97.300 | B |
| 891ef459dcfffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 151 | 14,695.200 | 97.300 | A |
| 891ef458257ffff | Centar Sarajevo | nan | 1271 | 123,801.500 | 97.400 | B |
| 891ea92eb73ffff | Novi Grad Sarajevo | Reljevo | 12 | 1,169.200 | 97.400 | A |
| 891ef459d93ffff | Stari Grad Sarajevo | Mošćanica | 41 | 3,998.900 | 97.500 | A |
| 891ef45846fffff | Centar Sarajevo | nan | 118 | 11,549.700 | 97.900 | B |
| 891ef459d53ffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 47 | 4,620.700 | 98.300 | A |
| 891ef4596cbffff | Novi Grad Sarajevo | Briješće | 40 | 3,935.900 | 98.400 | A |
| 891ef4583d3ffff | Centar Sarajevo | Sedrenik | 433 | 42,629.200 | 98.500 | B |
| 891ef45915bffff | Novo Sarajevo | Hrasno Brdo | 541 | 53,311.900 | 98.500 | B |
| 891ef458487ffff | Centar Sarajevo | nan | 23 | 2,268.200 | 98.600 | B |
| 891ef458673ffff | Centar Sarajevo | nan | 635 | 63,093.700 | 99.400 | B |
| 891ef459d1bffff | Stari Grad Sarajevo | Hrid-Jarčedoli | 113 | 11,235.300 | 99.400 | A |
| 891ef459143ffff | Novo Sarajevo | Vraca | 566 | 56,312.200 | 99.500 | B |
| 891ef4592dbffff | Novi Grad Sarajevo | Dobrinja A | 710 | 70,657.000 | 99.500 | A |
| 891ea92cd3bffff | Novi Grad Sarajevo | Reljevo | 26 | 2,589.600 | 99.600 | A |
| 891ef458043ffff | Centar Sarajevo | nan | 272 | 27,115.000 | 99.700 | B |
| 891ef4596bbffff | Novi Grad Sarajevo | Briješće | 287 | 28,613.900 | 99.700 | A |
| 891ef4584c7ffff | Centar Sarajevo | nan | 48 | 4,787.500 | 99.700 | B |
| 891ef45826fffff | Centar Sarajevo | nan | 1223 | 122,078.400 | 99.800 | B |
| 891ea92ebc7ffff | Novi Grad Sarajevo | Reljevo | 14 | 1,399.900 | 100.000 | A |
| 891ef45868fffff | Centar Sarajevo | nan | 61 | 6,100.400 | 100.000 | B |
| 891ea92ccb7ffff | Novi Grad Sarajevo | Dobroševići | 24 | 2,405.400 | 100.200 | A |
| 891ea92cdafffff | Novi Grad Sarajevo | Reljevo | 16 | 1,604.200 | 100.300 | A |
| 891ea92cbb7ffff | Novi Grad Sarajevo | Briješće | 15 | 1,506.900 | 100.500 | A |
| 891ef4580b3ffff | Centar Sarajevo | nan | 89 | 8,943.200 | 100.500 | B |
| 891ef458687ffff | Centar Sarajevo | nan | 117 | 11,763.600 | 100.500 | B |
| 891ea92cd43ffff | Novi Grad Sarajevo | Dobroševići | 110 | 11,074.900 | 100.700 | A |
| 891ef458223ffff | Centar Sarajevo | Logavina | 829 | 83,502.400 | 100.700 | B |
| 891ef458ec3ffff | Stari Grad Sarajevo | Mošćanica | 23 | 2,324.100 | 101.000 | A |
| 891ef458233ffff | Centar Sarajevo | nan | 793 | 80,245.600 | 101.200 | B |
| 891ef459d07ffff | Stari Grad Sarajevo | Mošćanica | 20 | 2,025.700 | 101.300 | A |
| 891ef4582a3ffff | Centar Sarajevo | nan | 497 | 50,343.300 | 101.300 | B |
| 891ef45840bffff | Centar Sarajevo | nan | 76 | 7,701.500 | 101.300 | B |
| 891ef45958fffff | Novo Sarajevo | Pofalići II | 14 | 1,421.700 | 101.600 | B |
| 891ea92cc77ffff | Novi Grad Sarajevo | Dobroševići | 67 | 6,813.300 | 101.700 | A |
| 891ef45944bffff | Novi Grad Sarajevo | Briješće | 243 | 24,729.000 | 101.800 | A |
| 891ef4580a3ffff | Centar Sarajevo | nan | 41 | 4,174.000 | 101.800 | B |
| 891ef458463ffff | Centar Sarajevo | nan | 77 | 7,855.300 | 102.000 | B |
| 891ef45835bffff | Stari Grad Sarajevo | Logavina | 1048 | 106,914.100 | 102.000 | A |
| 891ef45830fffff | Stari Grad Sarajevo | Mošćanica | 107 | 10,948.300 | 102.300 | A |
| 891ef45832bffff | Stari Grad Sarajevo | Mošćanica | 103 | 10,545.400 | 102.400 | A |
| 891ef6965a3ffff | Novi Grad Sarajevo | Saraj Polje | 22 | 2,252.500 | 102.400 | A |
| 891ef4580abffff | Centar Sarajevo | nan | 40 | 4,099.000 | 102.500 | B |
| 891ea92c813ffff | Novi Grad Sarajevo | Dobroševići | 285 | 29,222.300 | 102.500 | A |
| 891ef459cd3ffff | Centar Sarajevo | nan | 828 | 84,999.300 | 102.700 | B |
| 891ef458263ffff | Centar Sarajevo | nan | 1340 | 137,758.200 | 102.800 | B |
| 891ef45a22fffff | Centar Sarajevo | nan | 31 | 3,194.600 | 103.100 | B |
| 891ef4582abffff | Centar Sarajevo | nan | 1316 | 135,792.200 | 103.200 | B |
| 891ea92cc0fffff | Novi Grad Sarajevo | Dobroševići | 61 | 6,298.000 | 103.200 | A |
| 891ef45b2cbffff | Novi Grad Sarajevo | Reljevo | 170 | 17,591.500 | 103.500 | A |
| 891ef458677ffff | Centar Sarajevo | nan | 146 | 15,137.600 | 103.700 | B |
| 891ef45827bffff | Centar Sarajevo | nan | 958 | 99,334.100 | 103.700 | B |
| 891ef4584c3ffff | Centar Sarajevo | nan | 21 | 2,178.900 | 103.800 | B |
| 891ef458413ffff | Centar Sarajevo | nan | 109 | 11,382.400 | 104.400 | B |
| 891ea92cd03ffff | Novi Grad Sarajevo | Reljevo | 23 | 2,403.300 | 104.500 | A |
| 891ef458657ffff | Centar Sarajevo | nan | 47 | 4,923.700 | 104.800 | B |
| 891ea92cc8fffff | Novi Grad Sarajevo | Dobroševići | 40 | 4,195.000 | 104.900 | A |
| 891ef45968fffff | Novi Grad Sarajevo | Briješće | 283 | 29,698.200 | 104.900 | A |
| 891ef45862fffff | Centar Sarajevo | nan | 498 | 52,296.500 | 105.000 | B |
| 891ef458697ffff | Centar Sarajevo | nan | 142 | 14,948.000 | 105.300 | B |
| 891ef458003ffff | Centar Sarajevo | nan | 32 | 3,370.800 | 105.300 | B |
| 891ef4592d3ffff | Novi Grad Sarajevo | Saraj Polje | 473 | 49,935.300 | 105.600 | A |
| 891ef4596b3ffff | Novi Grad Sarajevo | Briješće | 196 | 20,723.600 | 105.700 | A |
| 891ef45966fffff | Novi Grad Sarajevo | Saraj Polje | 448 | 47,683.100 | 106.400 | A |
| 891ef4580bbffff | Centar Sarajevo | nan | 59 | 6,280.400 | 106.400 | B |
| 891ef458053ffff | Centar Sarajevo | nan | 358 | 38,141.000 | 106.500 | B |
| 891ef45969bffff | Novi Grad Sarajevo | Briješće | 319 | 34,006.100 | 106.600 | A |
| 891ea92cdcfffff | Novi Grad Sarajevo | Dobroševići | 18 | 1,920.900 | 106.700 | A |
| 891ef459c87ffff | Stari Grad Sarajevo | Bistrik | 1076 | 115,064.700 | 106.900 | A |
| 891ef458343ffff | Stari Grad Sarajevo | Kovači | 815 | 87,211.200 | 107.000 | A |
| 891ef45850fffff | Centar Sarajevo | Mošćanica | 54 | 5,783.400 | 107.100 | B |
| 891ea92cdb3ffff | Novi Grad Sarajevo | Reljevo | 33 | 3,541.400 | 107.300 | A |
| 891ef459cd7ffff | Centar Sarajevo | nan | 1348 | 145,147.700 | 107.700 | B |
| 891ef4582b7ffff | Centar Sarajevo | nan | 443 | 47,827.700 | 108.000 | B |
| 891ef45823bffff | Centar Sarajevo | nan | 1124 | 121,415.400 | 108.000 | B |
| 891ef458367ffff | Stari Grad Sarajevo | Mošćanica | 113 | 12,246.900 | 108.400 | A |
| 891ef458267ffff | Centar Sarajevo | nan | 1293 | 140,174.400 | 108.400 | B |
| 891ef459c9bffff | Centar Sarajevo | Ferhadija | 1524 | 165,402.600 | 108.500 | B |
| 891ef4586afffff | Centar Sarajevo | nan | 139 | 15,143.000 | 108.900 | B |
| 891ef45828fffff | Centar Sarajevo | nan | 1035 | 112,797.600 | 109.000 | B |
| 891ef4580d3ffff | Centar Sarajevo | nan | 208 | 22,716.300 | 109.200 | B |
| 891ef4592cbffff | Novi Grad Sarajevo | Dobrinja A | 262 | 28,696.100 | 109.500 | A |
| 891ef4592cfffff | Novi Grad Sarajevo | Dobrinja A | 970 | 106,253.300 | 109.500 | A |
| 891ef45834bffff | Stari Grad Sarajevo | Kovači | 797 | 87,324.500 | 109.600 | A |
| 891ef458483ffff | Centar Sarajevo | nan | 93 | 10,190.400 | 109.600 | B |
| 891ea92c907ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 451 | 49,418.400 | 109.600 | A |
| 891ef45966bffff | Novi Grad Sarajevo | Saraj Polje | 170 | 18,628.000 | 109.600 | A |
| 891ef45822bffff | Centar Sarajevo | nan | 1018 | 111,745.900 | 109.800 | B |
| 891ef458287ffff | Centar Sarajevo | nan | 644 | 70,772.600 | 109.900 | B |
| 891ef4582a7ffff | Centar Sarajevo | nan | 526 | 57,926.900 | 110.100 | B |
| 891ef458277ffff | Centar Sarajevo | nan | 1231 | 135,600.800 | 110.200 | B |
| 891ef45b64fffff | Novi Grad Sarajevo | Reljevo | 21 | 2,315.000 | 110.200 | A |
| 891ef459663ffff | Novi Grad Sarajevo | Saraj Polje | 122 | 13,452.800 | 110.300 | A |
| 891ea92c8cbffff | Novi Grad Sarajevo | Dobroševići | 211 | 23,268.300 | 110.300 | A |
| 891ea92c897ffff | Novi Grad Sarajevo | Dobroševići | 49 | 5,414.600 | 110.500 | A |
| 891ef4581cbffff | Stari Grad Sarajevo | Mošćanica | 34 | 3,758.700 | 110.600 | A |
| 891ea92cd5bffff | Novi Grad Sarajevo | Dobroševići | 78 | 8,630.500 | 110.600 | A |
| 891ea92cdd3ffff | Novi Grad Sarajevo | Dobroševići | 22 | 2,435.500 | 110.700 | A |
| 891ea92c8cfffff | Novi Grad Sarajevo | Dobroševići | 88 | 9,755.700 | 110.900 | A |
| 891ef4586a7ffff | Centar Sarajevo | nan | 129 | 14,301.800 | 110.900 | B |
| 891ef4582b3ffff | Centar Sarajevo | nan | 519 | 57,554.100 | 110.900 | B |
| 891ea92c933ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 234 | 26,054.800 | 111.300 | A |
| 891ea92cddbffff | Novi Grad Sarajevo | Dobroševići | 55 | 6,124.100 | 111.300 | A |
| 891ea92cc63ffff | Novi Grad Sarajevo | Dobroševići | 75 | 8,354.900 | 111.400 | A |
| 891ea92c917ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 380 | 42,443.800 | 111.700 | A |
| 891ef458e97ffff | Stari Grad Sarajevo | Mošćanica | 11 | 1,229.700 | 111.800 | A |
| 891ea92c923ffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 217 | 24,351.400 | 112.200 | A |
| 891ea92c93bffff | Novi Grad Sarajevo | Naselje heroja Sokolje | 336 | 37,836.400 | 112.600 | A |
| 891ea92cc13ffff | Novi Grad Sarajevo | Dobroševići | 54 | 6,090.800 | 112.800 | A |
| 891ef4586a3ffff | Centar Sarajevo | nan | 179 | 20,245.600 | 113.100 | B |
| 891ea92cd73ffff | Novi Grad Sarajevo | Dobroševići | 43 | 4,868.500 | 113.200 | A |
| 891ea92ccd7ffff | Novi Grad Sarajevo | Dobroševići | 20 | 2,272.500 | 113.600 | A |
| 891ef45841bffff | Centar Sarajevo | nan | 127 | 14,451.700 | 113.800 | B |
| 891ea92c967ffff | Novi Grad Sarajevo | Briješće | 401 | 45,734.400 | 114.100 | A |
| 891ef6965b7ffff | Novi Grad Sarajevo | Saraj Polje | 67 | 7,652.800 | 114.200 | A |
| 891ea92cd0bffff | Novi Grad Sarajevo | Dobroševići | 45 | 5,151.000 | 114.500 | A |
| 891ef4580d7ffff | Centar Sarajevo | nan | 80 | 9,157.700 | 114.500 | B |
| 891ef45b12fffff | Centar Sarajevo | nan | 114 | 13,054.500 | 114.500 | B |
| 891ef458163ffff | Stari Grad Sarajevo | Mošćanica | 29 | 3,323.400 | 114.600 | A |
| 891ea92ccc3ffff | Novi Grad Sarajevo | Dobroševići | 24 | 2,750.600 | 114.600 | A |
| 891ef45809bffff | Centar Sarajevo | nan | 40 | 4,603.500 | 115.100 | B |
| 891ef45a22bffff | Centar Sarajevo | nan | 20 | 2,309.700 | 115.500 | B |
| 891ea92eb03ffff | Novi Grad Sarajevo | Reljevo | 13 | 1,502.600 | 115.600 | A |
| 891ef459677ffff | Novi Grad Sarajevo | Saraj Polje | 52 | 6,012.200 | 115.600 | A |
| 891ef45b1a7ffff | Centar Sarajevo | nan | 11 | 1,273.000 | 115.700 | B |
| 891ea92c88fffff | Novi Grad Sarajevo | Dobroševići | 157 | 18,179.200 | 115.800 | A |
| 891ea92c8b3ffff | Novi Grad Sarajevo | Dobroševići | 54 | 6,259.600 | 115.900 | A |
| 891ef458ed3ffff | Stari Grad Sarajevo | Mošćanica | 36 | 4,177.300 | 116.000 | A |
| 891ea92c88bffff | Novi Grad Sarajevo | Dobroševići | 233 | 27,069.100 | 116.200 | A |
| 891ea92c977ffff | Novi Grad Sarajevo | Briješće | 406 | 47,409.100 | 116.800 | A |
| 891ef459453ffff | Novi Grad Sarajevo | Briješće | 32 | 3,743.600 | 117.000 | A |
| 891ef45828bffff | Centar Sarajevo | nan | 492 | 57,656.800 | 117.200 | B |
| 891ea92cdc3ffff | Novi Grad Sarajevo | Dobroševići | 34 | 3,989.500 | 117.300 | A |
| 891ef459693ffff | Novi Grad Sarajevo | Briješće | 337 | 39,596.000 | 117.500 | A |
| 891ef458317ffff | Stari Grad Sarajevo | Mošćanica | 111 | 13,053.900 | 117.600 | A |
| 891ea92cca7ffff | Novi Grad Sarajevo | Dobroševići | 52 | 6,121.400 | 117.700 | A |
| 891ea92cc03ffff | Novi Grad Sarajevo | Dobroševići | 44 | 5,215.100 | 118.500 | A |
| 891ea92c92bffff | Novi Grad Sarajevo | Briješće | 189 | 22,432.400 | 118.700 | A |
| 891ea92cc87ffff | Novi Grad Sarajevo | Dobroševići | 27 | 3,228.400 | 119.600 | A |
| 891ef45b177ffff | Centar Sarajevo | nan | 19 | 2,276.100 | 119.800 | B |
| 891ea92c893ffff | Novi Grad Sarajevo | Dobroševići | 63 | 7,547.800 | 119.800 | A |
| 891ea92c883ffff | Novi Grad Sarajevo | Dobroševići | 111 | 13,326.000 | 120.100 | A |
| 891ea92cd17ffff | Novi Grad Sarajevo | Reljevo | 12 | 1,441.300 | 120.100 | A |
| 891ef458edbffff | Stari Grad Sarajevo | Mošćanica | 16 | 1,925.800 | 120.400 | A |
| 891ef458e93ffff | Stari Grad Sarajevo | Mošćanica | 48 | 5,778.000 | 120.400 | A |
| 891ea92cd0fffff | Novi Grad Sarajevo | Reljevo | 140 | 16,903.200 | 120.700 | A |
| 891ea92c92fffff | Novi Grad Sarajevo | Briješće | 249 | 30,072.900 | 120.800 | A |
| 891ea92eb67ffff | Novi Grad Sarajevo | Reljevo | 28 | 3,401.100 | 121.500 | A |
| 891ea92cc33ffff | Novi Grad Sarajevo | Dobroševići | 66 | 8,023.300 | 121.600 | A |
| 891ef459697ffff | Novi Grad Sarajevo | Briješće | 329 | 40,050.300 | 121.700 | A |
| 891ef459683ffff | Novi Grad Sarajevo | Briješće | 407 | 49,550.200 | 121.700 | A |
| 891ea92cc2fffff | Novi Grad Sarajevo | Dobroševići | 98 | 11,938.100 | 121.800 | A |
| 891ea92cc6fffff | Novi Grad Sarajevo | Dobroševići | 82 | 10,002.600 | 122.000 | A |
| 891ea92ccabffff | Novi Grad Sarajevo | Dobroševići | 63 | 7,685.100 | 122.000 | A |
| 891ea92ccd3ffff | Novi Grad Sarajevo | Dobroševići | 31 | 3,786.700 | 122.200 | A |
| 891ef459687ffff | Novi Grad Sarajevo | Briješće | 410 | 50,222.100 | 122.500 | A |
| 891ef45945bffff | Novi Grad Sarajevo | Briješće | 252 | 30,868.500 | 122.500 | A |
| 891ef458147ffff | Stari Grad Sarajevo | Mošćanica | 20 | 2,456.400 | 122.800 | A |
| 891ea92c8c7ffff | Novi Grad Sarajevo | Dobroševići | 111 | 13,636.300 | 122.800 | A |
| 891ef459d17ffff | Stari Grad Sarajevo | Mošćanica | 65 | 8,027.200 | 123.500 | A |
| 891ea92c927ffff | Novi Grad Sarajevo | Briješće | 215 | 26,556.200 | 123.500 | A |
| 891ea92cd4fffff | Novi Grad Sarajevo | Dobroševići | 161 | 19,923.400 | 123.700 | A |
| 891ea92cd53ffff | Novi Grad Sarajevo | Dobroševići | 112 | 13,860.200 | 123.800 | A |
| 891ea92cc23ffff | Novi Grad Sarajevo | Dobroševići | 105 | 13,026.500 | 124.100 | A |
| 891ea92cc2bffff | Novi Grad Sarajevo | Dobroševići | 87 | 10,794.400 | 124.100 | A |
| 891ef458507ffff | Stari Grad Sarajevo | Mošćanica | 14 | 1,742.100 | 124.400 | A |
| 891ea92cc27ffff | Novi Grad Sarajevo | Dobroševići | 184 | 22,927.100 | 124.600 | A |
| 891ea92eb77ffff | Novi Grad Sarajevo | Reljevo | 13 | 1,623.500 | 124.900 | A |
| 891ea92cc0bffff | Novi Grad Sarajevo | Dobroševići | 36 | 4,504.000 | 125.100 | A |
| 891ea92cd4bffff | Novi Grad Sarajevo | Dobroševići | 137 | 17,146.200 | 125.200 | A |
| 891ea92eb8fffff | Novi Grad Sarajevo | Reljevo | 22 | 2,755.200 | 125.200 | A |
| 891ea92cd47ffff | Novi Grad Sarajevo | Dobroševići | 156 | 19,543.300 | 125.300 | A |
| 891ef459c93ffff | Stari Grad Sarajevo | Ferhadija | 1216 | 152,440.800 | 125.400 | A |
| 891ef458307ffff | Stari Grad Sarajevo | Mošćanica | 147 | 18,447.000 | 125.500 | A |
| 891ea92cc3bffff | Novi Grad Sarajevo | Dobroševići | 78 | 9,799.100 | 125.600 | A |
| 891ea92cbbbffff | Novi Grad Sarajevo | Briješće | 21 | 2,650.000 | 126.200 | A |
| 891ea92cc07ffff | Novi Grad Sarajevo | Dobroševići | 46 | 5,810.700 | 126.300 | A |
| 891ea92ccafffff | Novi Grad Sarajevo | Dobroševići | 79 | 9,987.800 | 126.400 | A |
| 891ea92c887ffff | Novi Grad Sarajevo | Dobroševići | 150 | 18,967.000 | 126.400 | A |
| 891ea92ccbbffff | Novi Grad Sarajevo | Dobroševići | 20 | 2,533.800 | 126.700 | A |
| 891ea92cdcbffff | Novi Grad Sarajevo | Dobroševići | 123 | 15,595.700 | 126.800 | A |
| 891ea92c89bffff | Novi Grad Sarajevo | Dobroševići | 210 | 26,654.300 | 126.900 | A |
| 891ea92cdabffff | Novi Grad Sarajevo | Reljevo | 27 | 3,428.200 | 127.000 | A |
| 891ef458103ffff | Stari Grad Sarajevo | Mošćanica | 17 | 2,160.200 | 127.100 | A |
| 891ea92cc17ffff | Novi Grad Sarajevo | Dobroševići | 46 | 5,848.400 | 127.100 | A |
| 891ea92cd8fffff | Novi Grad Sarajevo | Reljevo | 12 | 1,528.900 | 127.400 | A |
| 891ef458167ffff | Stari Grad Sarajevo | Mošćanica | 61 | 7,784.800 | 127.600 | A |
| 891ea92cc37ffff | Novi Grad Sarajevo | Dobroševići | 165 | 21,092.800 | 127.800 | A |
| 891ef459c97ffff | Stari Grad Sarajevo | Baščaršija | 1145 | 146,749.400 | 128.200 | A |
| 891ea92cc6bffff | Novi Grad Sarajevo | Dobroševići | 44 | 5,643.100 | 128.300 | A |
| 891ef45b213ffff | Novi Grad Sarajevo | Reljevo | 35 | 4,496.600 | 128.500 | A |
| 891ea92c8d7ffff | Novi Grad Sarajevo | Dobroševići | 140 | 18,002.100 | 128.600 | A |
| 891ef4583afffff | Stari Grad Sarajevo | Mošćanica | 98 | 12,607.700 | 128.600 | A |
| 891ea92cc67ffff | Novi Grad Sarajevo | Dobroševići | 209 | 27,053.100 | 129.400 | A |
| 891ef45811bffff | Stari Grad Sarajevo | Mošćanica | 25 | 3,247.200 | 129.900 | A |
| 891ef4583bbffff | Stari Grad Sarajevo | Mošćanica | 56 | 7,275.800 | 129.900 | A |
| 891ea92ccc7ffff | Novi Grad Sarajevo | Dobroševići | 64 | 8,335.900 | 130.200 | A |
| 891ea92cc73ffff | Novi Grad Sarajevo | Dobroševići | 112 | 14,589.400 | 130.300 | A |
| 891ea92cc7bffff | Novi Grad Sarajevo | Dobroševići | 66 | 8,616.900 | 130.600 | A |
| 891ef458327ffff | Stari Grad Sarajevo | Mošćanica | 20 | 2,633.500 | 131.700 | A |
| 891ef458ed7ffff | Stari Grad Sarajevo | Mošćanica | 34 | 4,477.200 | 131.700 | A |
| 891ef458333ffff | Stari Grad Sarajevo | Mošćanica | 83 | 11,029.400 | 132.900 | A |
| 891ea92cdb7ffff | Novi Grad Sarajevo | Reljevo | 44 | 5,856.300 | 133.100 | A |
| 891ea92cd93ffff | Novi Grad Sarajevo | Reljevo | 18 | 2,424.400 | 134.700 | A |
| 891ea92cd07ffff | Novi Grad Sarajevo | Reljevo | 98 | 13,208.800 | 134.800 | A |
| 891ea92cd83ffff | Novi Grad Sarajevo | Reljevo | 23 | 3,121.900 | 135.700 | A |
| 891ef458037ffff | Stari Grad Sarajevo | Mošćanica | 26 | 3,554.400 | 136.700 | A |
| 891ef45b2d3ffff | Novi Grad Sarajevo | Reljevo | 40 | 5,488.900 | 137.200 | A |
| 891ef458c5bffff | Stari Grad Sarajevo | Mošćanica | 25 | 3,466.000 | 138.600 | A |
| 891ea92cdbbffff | Novi Grad Sarajevo | Reljevo | 41 | 5,685.000 | 138.700 | A |
| 891ea92eb0fffff | Novi Grad Sarajevo | Reljevo | 14 | 1,944.300 | 138.900 | A |
| 891ef459c83ffff | Stari Grad Sarajevo | Baščaršija | 1096 | 152,747.600 | 139.400 | A |
| 891ef45803bffff | Stari Grad Sarajevo | Mošćanica | 44 | 6,139.100 | 139.500 | A |
| 891ea92cda7ffff | Novi Grad Sarajevo | Reljevo | 72 | 10,049.800 | 139.600 | A |
| 891ef45b2c3ffff | Novi Grad Sarajevo | Reljevo | 58 | 8,167.800 | 140.800 | A |
| 891ef45aa53ffff | Stari Grad Sarajevo | Mošćanica | 14 | 1,972.000 | 140.900 | A |
| 891ea92cda3ffff | Novi Grad Sarajevo | Reljevo | 92 | 13,007.900 | 141.400 | A |
| 891ea92cd87ffff | Novi Grad Sarajevo | Reljevo | 48 | 6,844.400 | 142.600 | A |
| 891ef45816fffff | Stari Grad Sarajevo | Mošćanica | 26 | 3,708.900 | 142.600 | A |
| 891ef45814fffff | Stari Grad Sarajevo | Mošćanica | 45 | 6,426.200 | 142.800 | A |
| 891ea92cd9bffff | Novi Grad Sarajevo | Reljevo | 37 | 5,287.600 | 142.900 | A |
| 891ea92cd33ffff | Novi Grad Sarajevo | Reljevo | 57 | 8,273.200 | 145.100 | A |
| 891ef459d4bffff | Stari Grad Sarajevo | Širokača | 84 | 12,198.200 | 145.200 | A |
| 891ef4583a3ffff | Stari Grad Sarajevo | Mošćanica | 168 | 24,490.200 | 145.800 | A |
| 891ef4583abffff | Stari Grad Sarajevo | Mošćanica | 198 | 29,611.100 | 149.600 | A |
| 891ef45812bffff | Stari Grad Sarajevo | Mošćanica | 33 | 4,967.700 | 150.500 | A |
| 891ef45812fffff | Stari Grad Sarajevo | Mošćanica | 56 | 8,441.800 | 150.700 | A |
| 891ef4581b3ffff | Stari Grad Sarajevo | Mošćanica | 17 | 2,564.700 | 150.900 | A |
| 891ef45817bffff | Stari Grad Sarajevo | Mošćanica | 105 | 15,917.800 | 151.600 | A |
| 891ef4583b3ffff | Stari Grad Sarajevo | Mošćanica | 107 | 16,234.100 | 151.700 | A |
| 891ef45816bffff | Stari Grad Sarajevo | Mošćanica | 67 | 10,283.900 | 153.500 | A |
| 891ef458e8bffff | Stari Grad Sarajevo | Mošćanica | 15 | 2,317.600 | 154.500 | A |
| 891ef45aa5bffff | Stari Grad Sarajevo | Mošćanica | 10 | 1,596.000 | 159.600 | A |
| 891ef45814bffff | Stari Grad Sarajevo | Mošćanica | 59 | 9,465.300 | 160.400 | A |
| 891ef4583a7ffff | Stari Grad Sarajevo | Mošćanica | 146 | 23,492.000 | 160.900 | A |
| 891ef458107ffff | Stari Grad Sarajevo | Mošćanica | 20 | 3,363.200 | 168.200 | A |
| 891ef45802bffff | Stari Grad Sarajevo | Mošćanica | 14 | 2,373.800 | 169.600 | A |
| 891ef45aa93ffff | Stari Grad Sarajevo | Mošćanica | 10 | 1,724.400 | 172.400 | A |
| 891ef4583b7ffff | Stari Grad Sarajevo | Mošćanica | 176 | 30,518.100 | 173.400 | A |
| 891ef458157ffff | Stari Grad Sarajevo | Mošćanica | 28 | 4,976.500 | 177.700 | A |
| 891ef458577ffff | Stari Grad Sarajevo | Mošćanica | 19 | 3,454.500 | 181.800 | A |
| 891ef45aa4fffff | Stari Grad Sarajevo | Mošćanica | 14 | 2,595.000 | 185.400 | A |
| 891ef45aacbffff | Stari Grad Sarajevo | Mošćanica | 11 | 2,043.500 | 185.800 | A |
| 891ef458023ffff | Stari Grad Sarajevo | Mošćanica | 49 | 9,376.300 | 191.400 | A |
| 891ef45853bffff | Stari Grad Sarajevo | Mošćanica | 15 | 2,926.700 | 195.100 | A |
| 891ef4580afffff | Stari Grad Sarajevo | Mošćanica | 17 | 3,336.300 | 196.300 | A |
| 891ef45802fffff | Stari Grad Sarajevo | Mošćanica | 22 | 4,767.300 | 216.700 | A |
| 891ef45a8cbffff | Stari Grad Sarajevo | Mošćanica | 10 | 2,366.900 | 236.700 | A |

## 5. Vizuelna provjera
Stanovnici u zonama gdje ih ne bi trebalo biti (aproksimacija: ravnomjerno po dijelu polja):

| vrsta | procijenjeno_stanovnika (površinski) |
|---|---|
| aerodrom | 612.000 |
| landuse=industrial | 6,306.000 |
| park | 7,500.000 |

Najgušće MZ (od 62 sa poznatim granicama):

| rang | opcina | mz | st | st_po_km2 |
|---|---|---|---|---|
| 1 | Novi Grad Sarajevo | Alipašino Polje BII | 3130 | 28,958.000 |
| 2 | Novi Grad Sarajevo | Alipašino Polje CII | 2414 | 25,544.000 |
| 3 | Novi Grad Sarajevo | Alipašino Polje CI | 2041 | 24,708.000 |
| 4 | Novi Grad Sarajevo | Alipašino Polje BI | 3770 | 23,672.000 |
| 5 | Novo Sarajevo | Malta | 4396 | 22,763.000 |
| 6 | Novo Sarajevo | Trg heroja | 5200 | 19,850.000 |
| 7 | Novo Sarajevo | Grbavica I | 6221 | 18,651.000 |
| 8 | Novi Grad Sarajevo | Otoka | 2886 | 18,175.000 |
| 9 | Novi Grad Sarajevo | Čengić Vila | 3132 | 18,142.000 |
| 10 | Novo Sarajevo | Hrasno | 1854 | 16,925.000 |
| 11 | Novo Sarajevo | Čengić Vila II | 1506 | 15,018.000 |
| 12 | Novo Sarajevo | Grbavica II | 5778 | 14,801.000 |
| 13 | Novi Grad Sarajevo | Staro Hrasno | 3121 | 14,797.000 |
| 14 | Novo Sarajevo | Kovačići | 2593 | 13,655.000 |
| 15 | Novi Grad Sarajevo | Dobrinja D | 5424 | 13,458.000 |

Dobrinja, Alipašino Polje, Grbavica (očekivano visoko):

| rang | opcina | mz | st | st_po_km2 |
|---|---|---|---|---|
| 1 | Novi Grad Sarajevo | Alipašino Polje BII | 3130 | 28,958.000 |
| 2 | Novi Grad Sarajevo | Alipašino Polje CII | 2414 | 25,544.000 |
| 3 | Novi Grad Sarajevo | Alipašino Polje CI | 2041 | 24,708.000 |
| 4 | Novi Grad Sarajevo | Alipašino Polje BI | 3770 | 23,672.000 |
| 7 | Novo Sarajevo | Grbavica I | 6221 | 18,651.000 |
| 12 | Novo Sarajevo | Grbavica II | 5778 | 14,801.000 |
| 15 | Novi Grad Sarajevo | Dobrinja D | 5424 | 13,458.000 |
| 20 | Novi Grad Sarajevo | Alipašino Polje AII | 2733 | 10,991.000 |
| 22 | Novi Grad Sarajevo | Dobrinja C | 4988 | 9,942.000 |
| 26 | Novi Grad Sarajevo | Dobrinja A | 5800 | 9,276.000 |
| 27 | Novi Grad Sarajevo | Dobrinja B | 5510 | 9,111.000 |
| 28 | Novi Grad Sarajevo | Alipašino Polje AI | 2456 | 8,915.000 |

Karta za vizuelni pregled: `out/karta.html`.

## 6. Starosne grupe
Zbir grupa = ukupno u svakom polju: **OK** (0 polja odstupa).

Odstupanje zbira grupa po općini od FZS-a (posljedica zaokruživanja po polju):

| opcina | d0_14 | d15_64 | d65plus |
|---|---|---|---|
| Centar Sarajevo | -2 | 1 | 1 |
| Novi Grad Sarajevo | -2 | 7 | -5 |
| Novo Sarajevo | -7 | 1 | 6 |
| Stari Grad Sarajevo | -3 | 7 | -4 |

## Napomene o modelu
- **Stari Grad Sarajevo**: MZ zbirovi iz Grafa 3 (udjeli)
- **Novi Grad Sarajevo**: MZ: β=0.5·udio_2010 + (1−β)·udio_modela; nove MZ s matičnom: nema; bez matične: ['Alipašin Most III', 'Zabrđe']
- Pouzdanost polja: {'B': 759, 'A': 569, 'C': 63}
