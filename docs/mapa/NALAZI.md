# Nalazi — Faza 1 (provjera API-ja)

Server: **HytaleServer 0.7.7** (`com.hypixel.hytale:Server:0.7.7`, najnovija verzija na `maven.hytale.com`, objavljena 2026-11-09). Detaljni potpisi: [`API_TABELA.md`](API_TABELA.md).

## 0. Metoda i ograničenja (pročitati prvo)

1. **U ovom repozitoriju nema koda projekta „Živi svijet".** `azurk98/test1` sadrži samo specifikaciju za procjenu stanovništva Sarajeva. Nijedan repozitorij kojem ova sesija ima pristup (`test1`, `test`, `Trziste`) nema Hytale kod. Zato:
   - nisam mogao utvrditi **koju verziju servera projekt koristi**: uzeo sam najnoviju (0.7.7);
   - nisam mogao pronaći **kako ARB definiše teritoriju** (pitanje 1 za MSTR-a ostaje otvoreno).
2. **Dekompilaciju (Vineflower) je blokirao sigurnosni sloj okruženja**, pa nisam mogao čitati tijela metoda. Umjesto toga koristio sam:
   - `javap -p -constants`: sve klase, polja, potpisi metoda i compile-time konstante;
   - pretragu stringova u constant poolu (npr. gdje se pojavljuje `"MapServerContent"`).

   Posljedica: **postojanje i potpise** mogu tvrditi sigurno. Za **ponašanje** (šta metoda tačno radi) mogu dati najviše ocjenu „vjerovatno". Ako želiš pune dokaze `klasa:linija`, pokreni dekompilaciju lokalno (`java -jar vineflower.jar Server-0.7.7.jar build/decompiled/`) ili dozvoli tu akciju u ovom okruženju.
3. Klijent nije dostupan (C#, native), pa sve što zavisi od klijenta ostaje za ručni test.
4. `build/` je dodan u `.gitignore`; jar i ispis potpisa nisu commitani.

## 1. Najvažnije u pet rečenica

1. **Postoji zvanični filter paketa po igraču** (`PacketAdapters.registerInbound/registerOutbound(PlayerPacketFilter)`). Njime vjerovatno možemo dobiti pločice različite za svakog igrača **bez `Unsafe` haka**: presretnemo izlazni `UpdateWorldMap` i zamijenimo slike. Također presrećemo ulazne klikove s mape bez zamjene `GamePacketHandler`-a.
2. **`WorldMapTracker.clearChunks(LongSet)` je javan.** To je zvaničan način da jednom igraču ponovo pošaljemo samo određene pločice (promjena znanja ili režima), bez `ClearWorldMap`.
3. **Server klijentu javlja dozvole za mapu** (`UpdateWorldMapSettings.allowTeleportToCoordinates`, `allowCreatingMapMarkers`, …) i opseg zuma (`minScale/maxScale/defaultScale`). Desni klik „bez dozvole" rješavamo tako da klijentu kažemo `true`, a stvarni teleport blokiramo na serveru.
4. **Markeri su bogatiji nego što smo mislili**: `TintComponent` (boja), `MapMarkerIconSize.Major`, `CompassAlertComponent`, `addIgnoreViewDistance`, `MapMarkerBuilder`.
5. **NoesisGUI je već u serveru** (`modules/ui`, XAML + view-model, `Canvas`, `ScaleTransform`, `ImageBrush` …), ali je **isključen**: *„Serverside Noesis UI is disabled. This feature is still in development and not available yet."* To je budući pravi map widget (opcija F). Danas se ne može koristiti.

## 2. Odgovori na pitanja iz Faze 1

### 3.1 Sve anchor tačke
- **Odgovor:** Server 0.7.7 koristi samo jednu anchor tačku, `"MapServerContent"`. Koriste je dva ugrađena dugmeta: `LeavePortalButtonUI` (`Hud/LeavePortalButton.ui`) i `ReturnToHubButtonUI` (`Hud/ReturnToHubButton.ui`). Oba šalju `UpdateAnchorUI` preko `writeNoCache` i registruju akciju u `AnchorActionModule` preko `WorldThreadAnchorActionHandler`. Nijedan drugi anchor ID ne postoji kao string u serveru. Klijent može imati i druge tačke, ali ih server ne spominje.
- **Dokaz:** pretraga stringova po svim `com/hypixel/hytale/**/*.class`: `MapServerContent` se nalazi samo u te dvije klase; `UpdateAnchorUI` samo u njima i u `PacketRegistry`. `AnchorActionHandler.handle(PlayerRef)` nema parametar za podatke.
- **Sigurnost:** sigurno za server; nepoznato za klijenta.
- **Posljedica:** panel na mapi = `MapServerContent`. Za inventar, tab meni i kompas nema anchora; HUD ide kroz `CustomHud`. Potvrđen je BetterMap obrazac: fiksni skup imena akcija i mapiranje slot → ID po igraču.

### 3.2 Desni klik bez dozvole
- **Odgovor:**
  - Server šalje klijentu `UpdateWorldMapSettings` sa `allowTeleportToCoordinates`, `allowTeleportToMarkers`, `allowCreatingMapMarkers`, `allowRemovingOtherPlayersMarkers`, `allowShowOnMapToggle` i `allowCompassTrackingToggle`.
  - `WorldMapTracker` sluša promjene dozvola i grupa (`PlayerPermissionChangeEvent`, `PlayerGroupEvent`, `GroupPermissionChangeEvent`) i ponovo šalje postavke. To znači da su postavke **po igraču** i izvedene iz `HytalePermissions.WORLD_MAP_COORDINATE_TELEPORT`.
  - Vjerovatno klijent ne nudi akciju (i ne šalje paket) kada je zastavica `false`. To treba potvrditi testom.
- **Rješenje bez stvarnog teleporta:**
  1. Izlaznim filterom (`PacketAdapters.registerOutbound`) postavi `allowTeleportToCoordinates = true` u `UpdateWorldMapSettings` za sve igrače.
  2. Ulaznim filterom (`registerInbound`) uhvati `TeleportToWorldMapPosition`. Ako igrač nije admin, ne propuštaj paket do `GamePacketHandler`-a, nego ga pretvori u događaj „pogledaj (x, z)".

  Za ovo **nije potrebno davati stvarnu dozvolu** niti zamjenjivati handler.
- **Dokaz:** polja `UpdateWorldMapSettings` (ID 240); `WorldMapTracker.isAllowTeleportToCoordinates(PlayerRef, Player)` (static) i `resendWorldMapSettings(UUID)`; `PacketAdapters` potpisi.
- **Sigurnost:**
  - postojanje zastavica i filtera: sigurno;
  - da klijent šuti kad je `false`: vjerovatno;
  - semantika povratne vrijednosti filtera (`true` = blokiraj ili propusti): nepoznato (test S1).
- **Posljedica:** baseline tačka 3 je izvodljiva bez haka. Rizik: klijentov tekst u meniju može glasiti „Teleport". To je kozmetika, provjeriti u S1.

### 3.3 Zvanična tačka za pločice po igraču
- **Odgovor:**
  - `Player.worldMapTracker` je `private final` i nema settera ni fabrike, pa je za zamjenu trackera i dalje potreban `Unsafe`.
  - `WorldMapTracker` **nije `final`** i ima javni konstruktor `(Player)`. Javni su i `getTransformComponent()` i `copyFrom(...)`, pa je dio refleksije iz Explorers Mapa sada nepotreban.
  - **Bolji put:** `PacketAdapters.registerOutbound(PlayerPacketFilter)`. Vanilla tracker i dalje sam odlučuje *koje* pločice šalje (spirala, radijus, budžet od 20 po ticku). Mi u izlaznom `UpdateWorldMap` za tog igrača zamijenimo `chunks[i]` novim `MapChunk(x, z, kompozit(vanilla, sloj znanja))`.
  - Za osvježavanje koristimo `getWorldMapTracker().clearChunks(LongSet)`.
  - `setPlayerMapFilter` filtrira **samo markere igrača**, ne pločice.
- **Dokaz:** `Player` polja (javap); `WorldMapTracker` potpisi; `PacketAdapters`, `PlayerPacketFilter.test(PlayerRef, Packet)`; `UpdateWorldMap` ima javna, mutabilna polja i konstruktor kopije.
- **Sigurnost:** vjerovatno. Treba potvrditi:
  - da filter smije mijenjati paket (ili ga blokirati i poslati izmijenjenu kopiju);
  - da se `UpdateWorldMap` gradi posebno za svakog igrača (`writeUpdatePacket` je u trackeru po igraču, dakle vjerovatno da);
  - da `write()` ne kešira serijalizovane bajtove prije filtera.

  **Nikad ne mijenjati zajednički `MapImage`**: on dolazi iz globalnog keša `WorldMapManager.images`.
- **Posljedica:** hak 3.3 (`Unsafe`) prelazi u rezervni plan. Glavni put postaje „outbound filter + `clearChunks`". Kompozit se mora praviti unaprijed (asinhrono). Filter samo zamjenjuje gotove slike iz keša. Ako slika nije spremna, šalje se vanilla pločica, a kad bude gotova poziva se `clearChunks`.

### 3.4 Nativni slojevi na mapi
- **Odgovor:**
  - Nema API-ja za linije, poligone, regije ni toplotne mape. Jedini nativni elementi su pločice (`MapChunk`/`MapImage`) i markeri.
  - Granica svijeta: `WorldMapSettings.worldMapArea` (`Box2D`) ograničava područje mape. BetterMap granicu skoro sigurno crta u pločicama ili markerima, jer drugog kanala nema.
  - „Oblasti questova" ne postoje kao sloj. Postoje `discoverZone(s)` (otkrivanje zona po igraču) i `CompassAlertComponent`.
- **Dokaz:** kompletan spisak klasa u `protocol/packets/worldmap` (vidi API tabelu); nema ničeg poput `Polygon`, `Line` ili `Region`.
- **Sigurnost:** sigurno (za protokol 0.7.7).
- **Posljedica:** granice, rute i uzorke crtamo u pločicama. Pločica je 32×32 chunka × `imageScale` (zadano 3,0 px/blok), dakle najviše 96 px po chunku. Linije su zato oštre samo do određenog zuma.

### 3.5 Zum i kadar klijenta
- **Odgovor:** Ne. Paketi od klijenta prema serveru vezani za mapu su samo `UpdateWorldMapVisible`, `TeleportToWorldMapMarker`, `TeleportToWorldMapPosition`, `CreateUserMarker` i `RemoveMapMarker`. Nijedan ne nosi skalu ni centar. Server može samo **ograničiti** zum po igraču (`defaultScale`, `minScale`, `maxScale`; zadano 128 / 32 / 175).
- **Sigurnost:** sigurno.
- **Posljedica:** potvrđena slabost iz baselinea (gužva natpisa). Ublažavanje: drugačiji opseg zuma po režimu, `MapMarkerIconSize` (`Default`/`Major`) za hijerarhiju, i manje markera na grubljim nivoima (biramo po rangu fiefa, ne po zumu).

### 3.6 Markeri
- **Odgovor:**
  - **Veličina:** enum `MapMarkerIconSize` = `Default`, `Major`. Proizvoljne veličine nema.
  - **Boja:** `TintComponent(Color)`. Postoji i `tintColor` u `CreateUserMarker`.
  - **Tekst:** `FormattedMessage name` (podržava prevode i formatiranje).
  - **Rotacija:** `Transform.orientation` (`yaw/pitch/roll`). Da li klijent rotira ikonu po `yaw`, nepoznato je (marker igrača se vjerovatno rotira).
  - **Ostale komponente:** `PlayerMarkerComponent`, `PlacedByMarkerComponent`, `HeightDeltaIconComponent` (druga ikona kad je meta iznad ili ispod), `CompassAlertComponent` (upozorenje na kompasu s trajanjem). Marker može imati i `compassImage` (pojavljuje se na kompasu).
  - **Vidljivost:** `MarkersCollector.add` poštuje udaljenost, `addIgnoreViewDistance` je ignoriše. Diff se šalje samo kad se marker promijeni (`doesMarkerNeedNetworkUpdate`). Male promjene pozicije šalju se svakih 10 s (`SMALL_MOVEMENTS_UPDATE_INTERVAL`).
  - **Maksimalan broj i prioritet prikaza:** nema konstante u serveru. Nepoznato (klijent).
- **Sigurnost:** polja sigurno; ponašanje rotacije, limita i prioriteta nepoznato.
- **Posljedica:**
  - Boja frakcije na markeru dolazi nativno, bez posebne ikone po boji.
  - Smjer vojske ide kroz `yaw` ako klijent to podržava, a u suprotnom kroz 8 ikona po smjeru.
  - Važne markere (prijestolnice, naredbe) šaljemo kao `Major` i preko `addIgnoreViewDistance`.

### 3.7 Kontekstni meni
- **Odgovor:**
  - `ContextMenuItem(String name, String command)`, a marker nosi **niz** stavki. Ikone i dozvole nema.
  - Komanda je proizvoljan string. Vjerovatno je klijent izvršava kao igrač, pa dozvole provjerava server pri izvršenju komande.
- **Sigurnost:** polja sigurno; izvršenje vjerovatno.
- **Posljedica:**
  - Stavke generišemo po igraču u `MarkerProvider.update` (provider se poziva po igraču), pa igrač vidi samo akcije koje smije.
  - U komandu stavljamo token verzije (`/zs map act <markerId> <akcija> <ver>`), a komanda ponovo provjerava pravo i svježinu.

### 3.8 Stranice i mapa
- **Odgovor:**
  - `Page.Map` postoji, a `PageManager.setPage(ref, store, Page.Map)` je javan. Vjerovatno server može otvoriti mapu.
  - `PageManager` drži **jednu** aktivnu stranicu (`legacyCustomPage` ili `serversidePage`), pa custom stranica i mapa vjerovatno ne mogu biti otvorene istovremeno.
  - Zato je anchor `MapServerContent` jedini način da imamo vlastiti sadržaj na mapi.
  - HUD dok je mapa otvorena: nepoznato.
- **Sigurnost:** vjerovatno.
- **Posljedica:**
  - Detaljna administracija (opcija B/7) je zasebna stranica. Prelaz „mapa → stranica → nazad na mapu" je moguć preko `setPage(Page.Map)`, ali uz zatvaranje i ponovno otvaranje mape.
  - **Ručni test S9:** komandom `/zs testmap` pozvati `setPage(Page.Map)`. Treba vidjeti da se mapa otvori. Zatim otvoriti custom stranicu i provjeriti da se mapa zatvori.

### 3.9 Dinamički asseti
- **Odgovor:**
  - **Postoji javni API**: `CommonAssetModule.get().sendAssetsToPlayer(PacketHandler, List<CommonAsset>, boolean)` i `sendAsset(CommonAsset, boolean)`. `CommonAsset` je apstraktan, s konstruktorom `(String name, byte[] bytes)`, pa PNG iz memorije šaljemo jednom igraču bez ručnog slaganja `AssetInitialize/Part/Finalize` paketa.
  - `boolean` je vjerovatno „pošalji `RequestCommonAssetsRebuild`" (provjeriti).
  - `MAX_FRAME = 2 621 440`, `AssetPart.MAX_SIZE = 4 096 006`.
  - **Texture Atlas API ne postoji** u serveru 0.7.7 (nema klasa s „Atlas").
  - Trošak rebuild-a i keširanje po hashu su na klijentu: nepoznato.
- **Sigurnost:** API sigurno; trošak nepoznat (test S7).
- **Posljedica:** hak 3.3/„dinamičke slike" postaje polu-zvaničan (javni API, ali nedokumentovan). Ime asseta po igraču + hash u imenu (`UI/zs/map/<uuid>/<hash>.png`) zaobilazi problem keširanja.

### 3.10 Kamera
- **Odgovor:**
  - `ServerCameraSettings` ima `positionType = Custom` + `position`, `rotationType` + `rotation`, `mouseInputType = LookAtPlane` + `planeNormal`, `displayCursor`, `sendMouseMotion`, `skipCharacterPhysics`, `canMoveType` i `baseFov`. Postoji i ugrađena komanda `PlayerCameraTopdownCommand`.
  - Klikovi stižu kroz `MouseInteraction` (`screenPoint`, `mouseButton`, `worldInteraction.blockPosition/entityId`).
  - Kamera se može postaviti daleko od igrača. Klijent ipak vjerovatno renderuje samo chunkove učitane oko igrača, pa daleki pogled zahtijeva instancu ili kopiju (opcija D).
- **Sigurnost:** polja sigurno; renderovanje udaljenih chunkova nepoznato.
- **Posljedica:** opcija D je izvodljiva za „ratni sto" u instanci (umanjena kopija), a ne za pogled na stvarni svijet izdaleka. **Ručni test S10:** `/camera topdown`, zatim podesiti `position` 500 blokova dalje i gledati da li se teren crta.

### 3.11 NoesisGUI
- **Odgovor:** Da, server ga ima, ali je isključen.
  - Paket `server.core.modules.ui`: `UIModule`, `UISurface`, `UIPage`, `UIHudWidget`, `ViewModelTypeRegistry`, `Ui`, `UITypes`, `ServersideUIDemoCommand` (`UI/Noesis/TestPage.xaml`).
  - Paketi: `InitViewModelTypes`, `UpdateServersidePage`, `UpdateServersideHud`, `ExecuteServersidePageCommand`, `ExecuteServersideHudCommand`, `DismissServersidePage`, `Set(Element)PropertyServersideUICommand`, `Insert/RemoveCollectionItemServersideUICommand`.
  - `Page.Serverside`, `HudWidgetSlot` (11 slotova uklj. `Underlay` i `Overlay`).
  - Metode u `PageManager` i `HudManager` imaju prefiks `dev_`.
  - `UIModule.SERVERSIDE_NOESIS_UI_ENABLED` je isključen, s porukom *„still in development and not available yet"*.
  - **Model:** XAML živi na klijentu kao asset, server šalje view-model (tipizirane vrijednosti, kolekcije, komande `ICommand`).
  - `UITypes` uključuje `Canvas`, `ScaleTransform`, `TranslateTransform`, `PathGeometry`, `ImageBrush`, `Viewbox`, `ScrollViewer`, `Storyboard`, `ToolTip` i `ContextMenu`. Sve što treba za pravi map widget s panom i zumom na klijentu, hoverom i poligonima, nalazi se tu.
- **Sigurnost:** postojanje sigurno; dostupnost danas: **ne**.
- **Posljedica:** UI sloj (`zs-ui`) projektovati kao view-model (stanje + komande), ne kao `.ui` selektore. Tada je kasniji prelaz na XAML zamjena prikaza, ne prepisivanje. Opcija F dobija ocjenu za budućnost, ne za MVP.

### 3.11a Dopuna: NoesisGUI u pre-release grani (0.8.0-pre.5)
- Na `maven.hytale.com/pre-release` postoji `Server-0.8.0-pre.5` (2026-11-12).
- U toj verziji `UIModule` u constant poolu ima `java/lang/System.getProperty` i string **`hytale.serverside_ui_preview`**. Zastavica `SERVERSIDE_NOESIS_UI_ENABLED` se dakle (vjerovatno) uključuje JVM svojstvom `-Dhytale.serverside_ui_preview=true`. To je zvanični „preview" prekidač, ne hak.
- U 0.7.7 (release) toga nema; tamo je isključeno bez prekidača.
- Proširen je i API: `ExecuteServersideUICommand`, `NotifyServersideUIPropertyChanged` (dvosmjerno vezivanje), `GlobalResourceRegistry`, demo stranice `Form`, `TwoWay`, `StaticResource`, `Bindings`.
- Vjerovatno treba i **pre-release klijent** kod igrača.
- **Sigurnost:** ime svojstva sigurno; tačna očekivana vrijednost (`true`) vjerovatno.
- **Ručni test S11:**
  1. Pokreni `Server-0.8.0-pre.5` sa `java -Dhytale.serverside_ui_preview=true -jar ...`.
  2. Uđi pre-release klijentom kao operator.
  3. Ukucaj `/uidemo page` (ili `/uidemo` → pogledaj podkomande).
  4. Treba vidjeti XAML testnu stranicu. Bez svojstva treba dobiti poruku „Serverside Noesis UI is disabled".

## 3. Ispravke hipoteza iz briefa

| Hipoteza | Stvarno (0.7.7) |
|---|---|
| `ContextMenuItem(label, command)` | `ContextMenuItem(name, command)` |
| `TeleportToWorldMapMarker.markerId` | polje je `id` (`RemoveMapMarker.markerId` je tačno) |
| `MapMarkerOverride(icon, global)` | `(UUID id, String icon, String name, Boolean global)` |
| `HudComponent` (24) | 26 (dodano npr. `PortalPanel`, `BossBar`) |
| `Page` enum završava sa `Custom` | dodano `Serverside, Chapters, ChapterRewards, PortalSummon, PortalActive, PortalError` |
| Dijelovi asseta ≤ 2 621 440 B | `MAX_FRAME = 2 621 440` i dalje važi; `AssetPart.MAX_SIZE = 4 096 006` |
| Za tracker trebaju refleksija na `transformComponent` i `markerTracker` | `getTransformComponent()` je javan; `getSentMarkers()` javan |
| Texture Atlas API (Update 6) | nema ga u serveru |
| Zum nije poznat serveru | tačno, ali server **postavlja** opseg zuma po igraču |
| `MapMarker` = id, name, image, transform, contextMenu | + `components[]`, `iconSize`, `compassImage` |

## 4. Nova opcija G (kandidat da pobijedi baseline)

**„Vanilla tracker + zvanični filteri"**:
- **Pločice po igraču:** `PacketAdapters.registerOutbound`. Zamjena slika u `UpdateWorldMap` kompozitom iz keša pogleda znanja; osvježavanje preko `WorldMapTracker.clearChunks`.
- **Klikovi na mapi:** `PacketAdapters.registerInbound` za `TeleportToWorldMapPosition` i `CreateUserMarker`, uz `UpdateWorldMapSettings` koji prepravimo na izlazu.
- **Markeri:** `MarkerProvider` po igraču + `TintComponent`/`Major`/kontekstni meni po rangu.
- **Panel:** anchor `MapServerContent`.
- **Slike u stranicama:** `CommonAssetModule.sendAssetsToPlayer`.

U odnosu na baseline, `Unsafe` i refleksija nestaju. Ostaju samo nedokumentovani, ali **javni** API-ji. Ovo nije konačna ocjena; ocjena dolazi u Fazi 3, nakon spike testova S1 i S3'.

## 5. Prijedlog za Fazu 2 (izmijenjeni spike testovi)

| # | Test | Šta se mijenja u odnosu na brief |
|---|---|---|
| S1' | Ulazni `PlayerPacketFilter` loguje (x, z) iz `TeleportToWorldMapPosition` i blokira teleport. Izlazni filter postavlja `allowTeleportToCoordinates=true` | Umjesto zamjene handlera; mjeri i semantiku `true/false` filtera |
| S2 | Ulazni filter guta `CreateUserMarker` | Provjeriti ima li „duha" markera |
| S3' | Izlazni filter mijenja jednu pločicu za jednog igrača; `clearChunks` je ponovo šalje nakon promjene | **Zamjenjuje `Unsafe` tracker**; S3 (Unsafe) ostaje samo ako S3' padne |
| S4 | `setGenerator` omotač (globalno) | bez promjene |
| S5 | Anchor `MapServerContent` | bez promjene |
| S6 | 500 pločica preko `clearChunks` umjesto `ClearWorldMap` | |
| S7 | PNG preko `CommonAssetModule.sendAssetsToPlayer` | umjesto ručnih `AssetPart` paketa |
| S8 | Marker + kontekstni meni + `TintComponent` + `yaw` | + boja i rotacija |
| S9 | `setPage(Page.Map)` iz servera; stranica i mapa istovremeno | novo (pitanje 3.8) |
| S10 | `SetServerCamera` s `positionType=Custom` 500 blokova dalje | novo (pitanje 3.10) |

Za svaki test ću uz kod napisati uputstvo za ručni test (koraci + šta treba vidjeti).

## 6. Otvorena pitanja za MSTR-a

1. **Gdje je kod projekta** (plugin, ARB)? U ovoj sesiji je samo `azurk98/test1`, koji ga ne sadrži. Bez njega ne mogu dokumentovati ARB (radijus oko bloka ili claim po chunku) i ne mogu napraviti spike testove u stvarnom projektu.
2. **Koju verziju servera koristimo?** Nalazi su za 0.7.7 (trenutno najnovija na Maven-u).
3. Smijem li **dekompajlirati** jar lokalno (ili ćeš ti pokrenuti Vineflower i dodati `build/decompiled/` u sesiju)? To bi dalo dokaze `klasa:linija` i riješilo „vjerovatno" stavke 3.2, 3.3 i 3.9.
4. Rangovi i prava na mapi, NPC jedinice, broj igrača i veličina svijeta: trebaće za Fazu 3.
