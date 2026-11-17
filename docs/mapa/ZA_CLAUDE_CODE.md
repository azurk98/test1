# Mapa fiefova — sažetak istraživanja za Claude Code (IntelliJ)

> Samostalni brief. Sve je provjereno u **HytaleServer 0.7.7** (+ pogled u `0.8.0-pre.5`). Izvještaji na bosanskom, kod i identifikatori na engleskom. Detalji u `NALAZI.md`, `API_TABELA.md`, `RJESENJA.md` u istom folderu.

## 0. Status i dvije rupe koje treba popuniti

- **Faza 1 (provjera API-ja) je gotova.** Faza 2 (spike testovi) NIJE počela — čeka odobrenje i kod projekta.
- **Rupa 1: kod projekta "Živi svijet" nije bio dostupan** u okruženju gdje je rađeno istraživanje (bio je samo nevezan repo). Zato **ARB teritorija nije dokumentovana** (radijus oko bloka ili claim po chunku — naći u kodu projekta) i nije potvrđeno koju verziju servera projekt koristi (uzeto 0.7.7, najnovija release).
- **Rupa 2: dekompilacija jara je bila blokirana**, pa su čitani samo potpisi (`javap -p -constants`) i stringovi. Zato: **postojanje i potpisi = sigurno; ponašanje metoda = najviše "vjerovatno".** U IntelliJ-u s dekompajlerom (ili Vineflower/CFR) lako se podižu "vjerovatno" stavke na "sigurno".

**Prvi zadaci u IntelliJ-u:**
1. Potvrdi verziju servera koju projekt koristi (`build.gradle`/`pom.xml` → `com.hypixel.hytale:Server:<ver>`).
2. Nađi ARB u kodu projekta i dokumentuj kako definiše teritoriju.
3. Dekompajliraj taj jar i podigni "vjerovatno" → "sigurno" za tačke 3.2/3.3/3.9 i R3.

## 1. Kontekst (cilj mape)

Klikabilna mapa fiefova kao "komandna tabla": upravljanje fiefovima, vojna strategija, politika, orijentacija. Nativni Hytale izgled, glatki zum/pomjeranje, sve klikabilno, akcije i vidljivost po rangu. **Sigurnost znanja:** vlastiti fiefovi uživo, tuđi samo koliko je poznato (informacija ima starost i izvor). Klijent može poslati proizvoljne koordinate → sve čitati iz pogleda znanja, nikad iz stvarnog stanja.

## 2. Fiksna ograničenja (ne krše se)

- **Nema klijentskih modova** — sve ide sa servera. (Ni posredno "skini DLL kad uđeš": klijent ne pokreće kod koji mu server pošalje; Hypixel to ne dozvoljava.)
- Samo jedan plugin kontroliše mapu svijeta.
- Hytaleov ugrađeni UI nije izmjenjiv osim Anchor tačaka.
- Legacy `.ui` se gasi; dolazi NoesisGUI (XAML). UI sloj tanak i zamjenjiv (pisati kao **view-model**, ne kao `.ui` selektore).
- Panel/pločice/markeri NIKAD ne smiju otkriti stanje koje igrač ne zna.

## 3. Ključni potvrđeni API (0.7.7)

### Pločice (potpuno naša slika)
- `WorldMapManager.setGenerator(IWorldMap)` / `getGenerator()` — globalni generator.
- `IWorldMap.generate(World, int w, int h, LongSet chunks) → CompletableFuture<WorldMap>` — vraća **proizvoljne** `MapImage` (ne mora teren).
- `IWorldMapProvider.CODEC.register(...)`; ugrađeni ID-jevi `"WorldGen"`, `"Disabled"`; `ChunkWorldMap.INSTANCE`.
- `WorldMapManager.clearImages()` / `clearImagesInChunks(LongSet)`.
- `WorldMapTracker.clearChunks(LongSet)` — **per-igrač** ponovno slanje pločica (zvanično, bez `ClearWorldMap`).
- `MapImage(int width, int height, int[] palette, byte bitsPerIndex, byte[] packedIndices)` — paletizovano.
- `WorldMapSettings`: `worldMapArea (Box2D)`, `imageScale` (zadano 3.0 px/blok), `viewRadiusMin/Max`. Konstante: `DEFAULT_SCALE=128, MIN=32, MAX=175`, `ABSOLUTE_MAX_VIEW_RADIUS=512`.

### Presretanje paketa (per-igrač, zvanično — zamjenjuje Unsafe/refleksiju)
- `PacketAdapters.registerOutbound(PlayerPacketFilter)` / `registerInbound(...)` (+ `PacketWatcher` varijante, `deregister*`).
- `PlayerPacketFilter.test(PlayerRef, Packet): boolean` — semantika `true` (propusti/blokiraj) **za test**.
- Alternativa: `IWorldPacketHandler.registerHandler(IPacketHandler, int packetId, handler[, Predicate<PlayerRef>])`.

### Paketi mape
| Paket | ID | Smjer | Polja |
|---|---|---|---|
| `UpdateWorldMapSettings` | 240 | S→K | `enabled, allowTeleportToCoordinates, allowTeleportToMarkers, allowShowOnMapToggle, allowCompassTrackingToggle, allowCreatingMapMarkers, allowRemovingOtherPlayersMarkers`; `defaultScale, minScale, maxScale` |
| `UpdateWorldMap` | 241 | S→K | `MapChunk[] chunks, MapMarker[] addedMarkers, String[] removedMarkers` (compressed) |
| `ClearWorldMap` | 242 | S→K | — |
| `UpdateWorldMapVisible` | 243 | K→S | `boolean visible` |
| `TeleportToWorldMapMarker` | 244 | K→S | `String id` |
| `TeleportToWorldMapPosition` | 245 | K→S | `int x, int y` (**y = Z**) |
| `CreateUserMarker` | 246 | K→S | `float x, z, String name, markerImage, Color tintColor, boolean shared` |
| `RemoveMapMarker` | 119 | K→S | `String markerId` |
| `MapChunk` | — | — | `int chunkX, chunkZ, MapImage image` |

### Markeri
- `MapMarker`: `id, FormattedMessage name, markerImage, Transform transform, ContextMenuItem[] contextMenuItems, MapMarkerComponent[] components, MapMarkerIconSize iconSize, String compassImage`.
- `MapMarkerBuilder(id, image, Transform)` + `withName/withCustomName/withIconSize/withCompassImage/withContextMenuItem/withComponent/build`.
- Komponente: `TintComponent(Color)` (**boja**), `PlayerMarkerComponent(UUID)`, `PlacedByMarkerComponent(name, UUID)`, `HeightDeltaIconComponent(up/down)`, `CompassAlertComponent(image, dur, timeout, tint)`.
- `MapMarkerIconSize`: `Default, Major`. `ContextMenuItem(String name, String command)`.
- `WorldMapManager$MarkerProvider.update(World, Player, MarkersCollector)` — **per-igrač**; `MarkersCollector.add(...)` / `addIgnoreViewDistance(...)`.
- Magla: `DiscoverableMapMarkers.reveal/hide/isRevealed(Player, id)`, `forEachMarkerInView(...)`; `WorldMapTracker.discoverZone/undiscoverZone(World, zona)`.

### Anchor / UI
- `AnchorActionModule.get().register(action, handler)` / `unregister(action)`; `AnchorActionHandler.handle(PlayerRef)`; `tryHandle(PlayerRef, action)`.
- `UpdateAnchorUI(235)`: `anchorId, clear, CustomUICommand[], CustomUIEventBinding[]` — **jedina anchor tačka u serveru: `"MapServerContent"`**.
- `CustomPage(218)`, `CustomHud(217)`, `CustomPageEvent(219)`, `SetPage(216)`; `Page`: `..., Custom, Serverside, ...`.
- `PageManager.setPage(ref, store, Page)`, `openCustomPage(...)`; `HudManager.addCustomHud(...)`. Jedna aktivna stranica → custom stranica i M mapa se vjerovatno isključuju.
- `CustomUIEventBindingType` uključuje `Activating, RightClicking, MouseEntered, MouseExited, ValueChanged, ...` (hover radi na **panel** elementima, ne na pločicama).
- Dozvole: `HytalePermissions.WORLD_MAP_COORDINATE_TELEPORT`, `WORLD_MAP_MARKER_TELEPORT`.

### Kamera (za "ratni sto" — vidi R3)
- `SetServerCamera(280)`: `ClientCameraView(FirstPerson/ThirdPerson/Custom), boolean isLocked, ServerCameraSettings`.
- `ServerCameraSettings` (34 polja): `distance, positionLerpSpeed, rotationLerpSpeed, displayCursor, sendMouseMotion, mouseInputType, planeNormal, positionType(AttachedToPlusOffset/Custom), position, rotationType, rotation, canMoveType, applyMovementType, baseFov, ...`.
- `MouseInputType`: `LookAtTarget, LookAtTargetBlock, LookAtTargetEntity, LookAtPlane`.
- **Povratni kanal:** `MouseInteraction` (K→S): `Vector2fc screenPoint, MouseButtonEvent mouseButton, MouseMotionEvent mouseMotion, WorldInteraction worldInteraction(entityId, BlockPosition blockPosition)`; `GamePacketHandler.handleMouseInteraction(...)`.
- `InstancesPlugin.get().spawnInstance(name, World, Transform)`, `teleportPlayerToInstance(...)`.

### Dinamičke slike
- `CommonAssetModule.get().sendAssetsToPlayer(PacketHandler, List<CommonAsset>, boolean)` / `sendAsset(CommonAsset, boolean)` — **javni API, per-igrač**.
- `CommonAsset(String name, byte[] bytes)` (apstraktan, naslijedi za PNG iz memorije). `AssetPart.MAX_SIZE=4096006`, `MAX_FRAME=2621440`. **Nema Texture Atlas API-ja.**

### NoesisGUI (server-side, isključen u release-u)
- `server.core.modules.ui`: `UIPage`, `UIHudWidget`, `UISurface`, `ViewModelTypeRegistry`, `Ui`, `UITypes` (`Canvas, ScaleTransform, TranslateTransform, PathGeometry, ImageBrush, Viewbox, ScrollViewer, Storyboard, ToolTip, ContextMenu`), demo `UI/Noesis/TestPage.xaml`.
- `UIModule.SERVERSIDE_NOESIS_UI_ENABLED` — isključen: *"Serverside Noesis UI is disabled. This feature is still in development and not available yet."* Metode u `PageManager`/`HudManager` imaju prefiks `dev_`.
- **U `0.8.0-pre.5`** `UIModule` čita `System.getProperty("hytale.serverside_ui_preview")` → zvanični preview prekidač: `-Dhytale.serverside_ui_preview=true`. Vjerovatno treba i pre-release klijent. (U 0.7.7 prekidača nema.)

## 4. Ispravke hipoteza iz originalnog briefa

`ContextMenuItem(name, command)` (ne `label`) · `TeleportToWorldMapMarker.id` (ne `markerId`) · `MapMarkerOverride(UUID id, String icon, String name, Boolean global)` · `HudComponent` ima 26 · `Page` ima i `Serverside, Chapters, Portal*` · `getTransformComponent()`/`getSentMarkers()` javni (manje refleksije) · nema Texture Atlasa · `MapMarker` ima i `components/iconSize/compassImage`.

## 5. Inovativna rješenja (detalji u RJESENJA.md)

- **R1 — Nativna mapa kao platno:** `setGenerator` + per-igrač `registerOutbound` zamjenjuje pikseli političkom slikom iz znanja; glatki zum besplatno. Osvježi `clearChunks`.
- **R2 — Server-autoritativni "semantički zum":** zakuj skalu (`min=max=default`), +/− dugmad mijenjaju nivo (kontinent→regija→fief→ulica) → server **zna** zum, savršen LOD, bez gomilanja natpisa.
- **R3 — "Ratni sto" kamerom (veliki ulog):** custom top-down kamera + `sendMouseMotion=true` + `LookAtPlane` → klijent **kontinuirano šalje poziciju kursora** (`MouseInteraction.screenPoint`/`worldInteraction.blockPosition`). Daje **pravi hover + poziciju koju server zna + zum koji server zna**, bez haka. Mora test (streama li i tačnost).
- **R4 — Nativna magla znanja:** `DiscoverableMapMarkers.reveal/hide` + `discoverZone` vežu sistem znanja na ugrađeni fog-of-war.
- **R5 — Klik bez pan-a:** `TeleportToWorldMapPosition` kao probe-koordinata (presretnut, bez teleporta) + markeri po fiefu s kontekstnim menijem po rangu.
- **R6 — Tri UI površine:** anchor panel + context menu + custom stranica/`CustomHud`.
- **R7 — Neizvjesnost kao šrafura** u paleti `MapImage` (staro/sporno/nepoznato vidljivo na svakom zumu).
- **R8 — Vektorski oštar PNG** preko `CommonAssetModule` (tekstura ploče ili `ImageBrush`).

## 6. Tri puta (odluka u Fazi 3)

- **Put A — "Nativna mapa, ojačana"** (R1+R2+R4+R5+R6+R7): radi danas na 0.7.7, bez haka. Slabost: nema pravog hovera.
- **Put B — "Ratni sto"** (R3+R8+R4+R6, instanca): pravi hover + poznata pozicija + zum, 3D izgled. Slabost: nije "pritisni M", render košta, R3 nepoznanice.
- **Put C — NoesisGUI** (kad S11 prođe): Canvas/ScaleTransform/ImageBrush/hover/poligoni; Put A/B postaju rezerva.

## 7. Spike testovi (Faza 2) — redoslijed po važnosti

| # | Test | Uspjeh |
|---|---|---|
| **S13** (R3) | `/zs wartable`: `SetServerCamera` top-down iznad ploče 64×64, `sendMouseMotion=true`, loguj svaki `MouseInteraction` | Pozicija kursora stiže **dok se miš miče** (ne samo na klik); izmjeri učestalost/mrežu |
| **S11** (Noesis) | `0.8.0-pre.5` + `-Dhytale.serverside_ui_preview=true`, pre-release klijent, `/uidemo` | Otvori se XAML testna stranica (ne poruka "disabled") |
| **S12** (R2) | Mijenjaj `defaultScale` kroz 3 nivoa | Prelaz bez treperenja |
| **S1'** (R5) | Inbound `PlayerPacketFilter` loguje (x,z) iz `TeleportToWorldMapPosition` i blokira teleport; outbound postavi `allowTeleportToCoordinates=true` | Klik stiže bez teleporta; utvrdi semantiku `true/false` filtera |
| **S3'** (R1) | Outbound filter zamijeni 1 pločicu za 1 igrača; `clearChunks` je ponovo pošalje | Drugi igrač ne vidi; nema treperenja |
| S2 | Inbound filter "pojede" `CreateUserMarker` | Nema "duha" markera |
| S4 | `setGenerator` omotač (globalno) | Poredi s S3' |
| S5 | Anchor panel `MapServerContent`, 2 dugmeta | Akcija stiže; izmjeri kašnjenje; odsiječe li se |
| S6 | 500 pločica preko `clearChunks` | Vrijeme, treperenje, saobraćaj |
| S7 | PNG preko `sendAssetsToPlayer`, pa novi u isti slot | Štucanje? osvježi li se |
| S8 | Marker + context menu + `TintComponent` + `yaw` rotacija | Cijeli krug; boja i smjer |
| S9 | `setPage(Page.Map)` iz servera; stranica+mapa istovremeno | Šta se dešava |
| S10 | `SetServerCamera` 500 blokova od igrača | Crta li se teren izdaleka |

Za svaki test napisati uputstvo za ručni test u igri (koraci + šta treba vidjeti) za MSTR-a.

## 8. Arhitektura (prijedlog za kod)

- `zs-mapa-core` — bez Hytale importa, s testovima: pogled znanja, kompozicija slojeva, keš (chunk + režim + verzija znanja; promjena vlasnika poništava i 8 susjeda).
- `zs-mapa-hytale` — adapter: sav Hytale-specifičan kod (generator, filteri paketa, markeri, kamera, asseti) na jednom mjestu.
- `zs-ui` — tanak sloj kao **view-model** (stanje + komande), da prelaz na NoesisGUI bude zamjena prikaza, ne prepisivanje.
- **MVP:** obojeni fiefovi + desni klik → panel s informacijama (Put A).
- **Feature flag za svaki hak** i rezervni plan (globalni generator ako per-igrač padne).

## 9. Reference i licence (prije kopiranja provjeri i pitaj)

MIT (smije se, uz copyright): ExplorersMap, SimpleClaims, KtaleUI, ReactiveUI. GPL/AGPL (samo učiti, ne kopirati): HyperFactions, BetterMap. **HyLay = klijentski mod (DLL+WebView2), repo obrisan — NE koristiti.**

## 10. Pitanja za MSTR-a

1. Gdje je kod projekta i ARB (radijus oko bloka ili claim po chunku)?
2. Koju verziju servera koristimo (0.7.7? pre-release za NoesisGUI?)?
3. Rangovi i prava na mapi; ima li NPC jedinica; broj igrača i veličina svijeta?
4. Smijemo li na pre-release grani zbog NoesisGUI-ja (Put C), ili ciljamo Put A na stabilnoj?

**Ne implementirati puni sistem prije odobrenja.** Sljedeći korak: S13 i S11 (odlučuju put), pa preporuka u `PREPORUKA.md`.
