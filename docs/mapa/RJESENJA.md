# Inovativna rješenja — zaobilaznice za probleme mape

> Dopuna Fazi 1. Sve ideje su serverske (bez klijentskih modova), u skladu s fiksnim ograničenjima i Hypixelovim uslovima. Za svaku: šta iskorištava · dokaz u API-ju · rizik · kako testirati.
> Oznake sigurnosti kao u NALAZI.md: sigurno / vjerovatno / nepoznato.

## Polazna ideja vodilja

Nativna M mapa je **samo prikazivač pločica sa zumom i pomjeranjem**. Mi kontrolišemo pločice. Dakle kontrolišemo **cijelu sliku**, a glatki zum i pomjeranje dobijamo besplatno od klijenta. Ne treba nam vlastiti zum — treba nam kontrola nad onim što prikazivač crta. Većina rješenja ispod gradi na tome.

---

## R1 — Nativna mapa kao naše platno (ne crtamo "preko" terena, crtamo umjesto njega)

- **Problem:** glatki zum/pomjeranje + Hytale izgled, bez vlastitog UI-ja.
- **Ideja:** `IWorldMap.generate(...)` smije vratiti **bilo kakav** `MapImage` (paleta + pikseli). Ne moramo vraćati teren — vraćamo našu političku sliku (ispune fiefova, granice, šrafure) kao pločice. Nativni prikazivač ih zumira i pomjera kao da je teren.
  - Globalno: `WorldMapManager.setGenerator(IWorldMap)` → ista politička mapa za sve (rezerva).
  - Po igraču: `PacketAdapters.registerOutbound` presretne `UpdateWorldMap` i zamijeni `chunks[i].image` kompozitom iz keša **pogleda znanja tog igrača**.
- **Iskorištava:** činjenicu da je `MapImage` proizvoljan i da se `UpdateWorldMap` gradi po igraču (`WorldMapTracker.writeUpdatePacket`).
- **Dokaz:** `IWorldMap.generate → CompletableFuture<WorldMap>`; `WorldMap.getChunks(): Long2ObjectMap<MapImage>`; `PacketAdapters.registerOutbound(PlayerPacketFilter)`. (sigurno za potpise; vjerovatno za ponašanje filtera)
- **Rizik:** filter mora smjeti izmijeniti paket; ne dirati zajednički `MapImage` iz keša (praviti nove). Osvježavanje: `WorldMapTracker.clearChunks(LongSet)`.
- **Test:** S3' iz NALAZI.md.

## R2 — Server-autoritativni "semantički zum" (preokret ograničenja)

- **Problem:** server ne zna zum klijenta → ne može raditi level-of-detail, natpisi se gomilaju.
- **Ideja:** ne boriti se protiv ograničenja — **preuzeti zum**. `UpdateWorldMapSettings` ima `minScale/maxScale/defaultScale` po igraču. Postavimo `min == max == default` i time **zakujemo** klijent na tačno jednu skalu. Dugmad +/− u anchor panelu mijenjaju tu skalu kroz nekoliko nivoa (kontinent → regija → fief → ulica). Pošto server bira nivo, **server tačno zna zum** i za svaki nivo šalje drugačije pločice (grube granice izdaleka, imena izbliza). Savršen LOD, nula gomilanja.
- **Iskorištava:** to što server **postavlja** opseg zuma po igraču.
- **Dokaz:** `UpdateWorldMapSettings.defaultScale/minScale/maxScale` (ID 240); `AnchorActionModule.register(action, handler)`. (sigurno)
- **Kompromis:** gubi se slobodni pinch-zum; dobija se diskretni, "Google-Maps" zum. Za komandnu tablu je to često **bolje** od slobodnog zuma. Može se ostaviti i uski slobodni opseg oko svakog nivoa (min<max malo) za mekši osjećaj, a LOD vezati za zadnji nivo s dugmeta.
- **Nepoznato:** da li klijent animira prelaz kad se promijeni `defaultScale` (treperenje?). → test S12.
- **Hibrid s R1:** svaki nivo = drugi set pločica iz generatora.

## R3 — "Ratni sto" kamerom: prava interaktivna mapa, 100% serverski (veliki ulog)

- **Problem:** nema hovera, server ne zna gdje kursor gleda, panel je mali — sve odjednom.
- **Ključni nalaz:** u custom-kamera modu klijent **šalje poziciju kursora serveru**. `MouseInteraction` (klijent→server) nosi `screenPoint` (Vector2fc, normalizovan kursor) **i** `worldInteraction.blockPosition` (blok na koji kursor pokazuje). `ServerCameraSettings.sendMouseMotion = true` + `mouseInputType = LookAtPlane` + `planeNormal` → kursor se projektuje na ravan i šalje kontinuirano.
- **Ideja:** "Mapa" nije M mapa, nego **top-down kamera iznad ravne površine** (naš politički teren kao tekstura/blokovi, po mogućnosti u instanci — "umanjeni svijet"/opcija D). Tada dobijamo:
  - **pravi hover** — server zna poziciju kursora na ravni svakog frejma → istakni fief pod mišem, prikaži karticu;
  - **zum i pomjeranje koje server zna** — jer server postavlja `distance`/`position` kamere (+/− i WASD → `canMoveType`/`applyMovementType`);
  - **klik** — `MouseInteraction.mouseButton` + `blockPosition` = koja ćelija;
  - **Hytale izgled** — pravi 3D teren/blokovi, ne pikseli.
- **Iskorištava:** kameru umjesto map sistema; `LookAtPlane` kao "graphics tablet" koji strima kursor.
- **Dokaz:** `SetServerCamera(ClientCameraView.Custom, isLocked, ServerCameraSettings)`; polja `sendMouseMotion, mouseInputType(LookAtPlane), planeNormal, displayCursor, position(Type), canMoveType`; `MouseInteraction.screenPoint/mouseMotion/worldInteraction.blockPosition`; `GamePacketHandler.handleMouseInteraction(...)`; `InstancesPlugin.spawnInstance`. (potpisi sigurno)
- **Nepoznato (mora test):**
  1. Da li `MouseInteraction` zaista stiže **kontinuirano** dok se miš miče (hover), ili samo na klik? `sendMouseMotion` + `MouseMotionEvent.relativeMotion` snažno impliciraju da — ali treba potvrditi.
  2. Je li `worldInteraction.blockPosition` popunjen tokom pokreta ili samo pri kliku.
  3. Učestalost (koliko paketa/s — mrežni trošak).
- **Rizik:** nije nativna M mapa (drugačiji ulaz: igrač otvara "sto", ne pritišće M); render scene košta; treba ravna površina (instanca). Ali je **jedino rješenje koje daje hover + poznatu poziciju + zum, bez ijednog haka**.
- **Test S13:** `/zs wartable` → `SetServerCamera` top-down iznad ploče 64×64 blokova; loguj svaki `MouseInteraction.screenPoint/blockPosition`. Uspjeh: pozicija stiže dok se miš miče (ne samo na klik).

## R4 — Nativna magla znanja za markere i zone (znanje bez vlastitog koda)

- **Problem:** "tuđe samo onoliko koliko je poznato"; sistem znanja sa starošću i izvorom.
- **Ideja:** koristiti ugrađenu per-igrač maglu:
  - `DiscoverableMapMarkers.reveal/hide/isRevealed(Player, id)` + `forEachMarkerInView(...)` + interakcija `RevealMapMarkersInView` → markeri (tuđe prijestolnice, vojske) vidljivi **samo kad ih igrač zna**. Osmatranje = `RevealMapMarkersInView` kad igrač gleda područje.
  - `WorldMapTracker.discoverZone/undiscoverZone(World, zona)` → politička boja regije se prikazuje **samo u otkrivenim zonama**.
- **Iskorištava:** nativni fog-of-war, koji već postoji po igraču.
- **Dokaz:** `DiscoverableMapMarkers` (sve statičke metode); `WorldMapTracker.discoverZone(s)/undiscoverZone(s)`. (sigurno za potpise)
- **Posljedica:** sistem znanja se ne gradi od nule — vežemo "ima li kraljevstvo informaciju" na `reveal/hide` i `discoverZone`. Starost/izvor idu u našu kešfeatures, a prikaz koristi nativnu maglu.

## R5 — Klikabilna teritorija bez poznavanja pomjeranja (dvostruki senzor)

- **Problem:** na M mapi server ne zna centar/pomjeranje, a ipak treba "klik na fief".
- **Ideja:** dva nativna signala daju tačku bez pan-a:
  1. **Desni klik na zemlju** → presretnut `TeleportToWorldMapPosition(x, y=Z)` = tačna (x,z) gdje je igrač kliknuo (ne teleport, nego "pogledaj"). To je JEDINO mjesto gdje klijent sam javi koordinatu s mape.
  2. **Marker po fiefu** s kontekstnim menijem → klik na grb fiefa = znamo fief + akcije. `MarkerProvider.update` se zove po igraču, pa stavke menija biramo po rangu.
- **Iskorištava:** `TeleportToWorldMapPosition` kao "probe koordinate" + markere kao klikabilne tačke.
- **Dokaz:** `TeleportToWorldMapPosition.x/y`; `PacketAdapters.registerInbound`; `MapMarker.contextMenuItems`; `WorldMapManager$MarkerProvider.update(World, Player, MarkersCollector)`. (potpisi sigurno; da klijent šalje klik bez teleport-dozvole → test S1')

## R6 — Beskonačan panel: tri površine umjesto jedne

- **Problem:** anchor panel `MapServerContent` je mali.
- **Ideja:** slagati **tri nezavisne UI površine**:
  1. **Anchor panel** (`MapServerContent`) — stalni bočni panel uz mapu;
  2. **Kontekstni meni markera** — dodatni prostor po objektu (više stavki, info + akcije);
  3. **Custom stranica** (`Page.Custom`, cijeli ekran) — duboka administracija; + **`CustomHud`** za trajne widgete (porez koji ističe, status opsade) nezavisno od panela.
- **Iskorištava:** to što `CustomHud` i anchor rade istovremeno, a context menu je zaseban prostor.
- **Dokaz:** `UpdateAnchorUI`, `CustomHud` (ID 217), `CustomPage` (ID 218), `ContextMenuItem[]`. (sigurno)
- **Napomena:** custom stranica i M mapa se vjerovatno isključuju (jedna aktivna stranica) → prelaz mapa↔stranica je zatvori/otvori (test 3.8).

## R7 — Neizvjesnost kao šrafura u paleti (staro/sporno/nepoznato se vidi)

- **Problem:** "svježe / staro / nepoznato + izvor i starost" mora biti vidljivo na samoj mapi.
- **Ideja:** `MapImage` ima **paletu** (`palette`, `packedIndices`, `bitsPerIndex`). Staro znanje = iste boje ali s dither/šrafura uzorkom upisanim u pikseli; sporni teritorij = dijagonalne pruge dvije boje; nepoznato = prazno/maglovito. Sve je u pločici, pa radi na svakom zumu i bez dodatnih elemenata.
- **Iskorištava:** paletizovani format (jeftino: malo boja, uzorak je indeks).
- **Dokaz:** `MapImage(width, height, int[] palette, byte bitsPerIndex, byte[] packedIndices)`; vanilla `ImageBuilder` već koristi Bayer dithering (`QUANTIZE_STEP=8`) → uzorak je izvodljiv jeftino. (sigurno)
- **Budžet:** < 1 ms/pločica, spakovane slike (brief §7).

## R8 — Vektorski oštra politička mapa kroz PNG-asset

- **Problem:** granice/natpisi u pikselima pločica pri grubljem zumu nisu oštri.
- **Ideja:** server **unaprijed renderuje** PNG kraljevstva (granice, imena, grbovi — oštri) i šalje ga `CommonAssetModule.sendAssetsToPlayer(...)`. Dva prikaza:
  - kao tekstura na ploči u R3 (ratni sto), ili
  - kao `ImageBrush`/`Image` u NoesisGUI/custom stranici.
- **Iskorištava:** javni (nedokumentovani) API za slanje asseta jednom igraču; ime+hash po igraču rješava keš.
- **Dokaz:** `CommonAssetModule.sendAssetsToPlayer(PacketHandler, List<CommonAsset>, boolean)`; `CommonAsset(String name, byte[])`. (potpisi sigurno; trošak rebuild-a nepoznat → test S7)

---

## Dvije "velike" arhitekture (biraju se u Fazi 3)

### Put A — "Nativna mapa, ojačana" (nizak rizik, danas)
R1 + R2 + R4 + R5 + R6 + R7. Sve radi na 0.7.7 release, bez klijenta, bez haka (uz jedan za dinamičke .ui ako zatreba). Daje: Hytale izgled, glatki (ili semantički) zum, klik na fief, znanje, panele. **Slabost:** nema pravog hovera; LOD ovisi o R2.

### Put B — "Ratni sto" (visok plafon, treba test)
R3 + R8 + R4 + R6, po mogućnosti u instanci. Daje: **pravi hover, poznatu poziciju kursora, zum koji server zna, 3D Hytale izgled**, bez M mape i bez haka. **Slabost:** nije "pritisni M"; render košta; tri nepoznanice iz R3 moraju proći test S13.

### Put C — NoesisGUI (najviši plafon, kad izađe iz preview-a)
Čim S11 potvrdi `-Dhytale.serverside_ui_preview=true` na `0.8.0-pre.5`: Canvas + ScaleTransform + ImageBrush + hover + poligoni. Tada Put A/B postaju rezerva. UI od početka pišemo kao view-model da prelaz ne bude prepisivanje.

## Preporučeni redoslijed testova (prije odluke)
1. **S13** (R3) — streama li kamera poziciju kursora? Ako da, Put B je realan i mijenja sve.
2. **S11** (NoesisGUI) — radi li preview? Ako da, Put C vodi.
3. **S12** (R2) — animira li se promjena skale bez treperenja?
4. **S1'/S3'** (R5/R1) — klik bez dozvole + per-igrač pločice.

Dok se ovo ne izmjeri, baseline (Put A) je sigurna osnova za MVP.

## Granica (šta NE radimo)
Nema ubacivanja DLL-a ni koda u klijent, ni posrednog ("skini kad uđeš"). Klijent ne pokreće kod koji mu server pošalje, Hypixel to ne dozvoljava, i krši fiksna ograničenja. Sva rješenja iznad šalju samo **podatke** (pločice, markere, UI opis, assete) koje klijent sam prikazuje.
