# API tabela — mapa svijeta i UI (HytaleServer 0.7.7)

**Izvor:** `com.hypixel.hytale:Server:0.7.7` s `maven.hytale.com/release` (SHA-1 `abf71e749465984d76a4db69f11505d846c66b4a`, `Implementation-Revision-Id: 12fc4656…`, kompajliran za Java 25).
**Metoda:** `javap -p -constants` (potpisi, polja, konstante) + pretraga stringova u constant poolu. **Tijela metoda nisu dekompajlirana** (vidi NALAZI.md §0), pa „potvrđeno" ovdje znači: *potpis postoji tačno ovakav*. Ponašanje je označeno posebno.

Legenda: ✅ potvrđeno · ⚠️ postoji, ali drugačije od hipoteze · ❌ ne postoji · 🆕 nije bilo u hipotezama

## Mapa svijeta — server

| Klasa | Član | Tačan potpis | Status | Napomena |
|---|---|---|---|---|
| `World` | `getWorldMapManager()` | — | ✅ (iz briefa, nije posebno provjereno) | |
| `WorldMapManager` | `getImageAsync` | `CompletableFuture<MapImage> getImageAsync(int x, int z)` / `(long index)` | ✅ | |
| | `getImageIfInMemory` | `MapImage getImageIfInMemory(int,int)` / `(long)` | ✅ | |
| | `clearImages` / `clearImagesInChunks` | `void clearImages()` / `void clearImagesInChunks(LongSet)` | ✅ | |
| | `setGenerator` / `getGenerator` | `void setGenerator(IWorldMap)` / `IWorldMap getGenerator()` | ✅ | |
| | `addMarkerProvider` | `void addMarkerProvider(String, WorldMapManager$MarkerProvider)` | ✅ | |
| | `getMarkerProviders` | `Map<String, MarkerProvider> getMarkerProviders()` | ✅ | Mutabilna mapa? — nepoznato |
| | `getWorldMapSettings` / `isWorldMapEnabled` | ✅ | ✅ | |
| | `addMarkerOverride` | `boolean addMarkerOverride(String, MapMarkerOverride)` | ✅ | |
| | `removeMarkerOverride` | `boolean removeMarkerOverride(String)` / `(String, MapMarkerOverride)`; `removeAllMarkerOverrides()` | ✅ | |
| | `handleUserCreateMarker` 🆕 | `void handleUserCreateMarker(PlayerRef, CreateUserMarker)` | 🆕 | Vanilla logika je javna → možemo je pozvati nakon vlastite provjere |
| | `handleUserRemoveMarker` 🆕 | `void handleUserRemoveMarker(PlayerRef, RemoveMapMarker)` | 🆕 | |
| | `getPointsOfInterest`, `generate()`, `sendSettings()`, `sendSettingsToAllWorlds()` 🆕 | | 🆕 | |
| | konstanta `MAX_GENERATIONS_PER_TICK` | private | — | vrijednost nije u constant poolu |
| `IWorldMap` | `getWorldMapSettings` | `WorldMapSettings getWorldMapSettings()` | ✅ | |
| | `generate` | `CompletableFuture<WorldMap> generate(World, int, int, LongSet)` | ✅ | |
| | `generatePointsOfInterest` | `CompletableFuture<Map<String, MapMarker>> generatePointsOfInterest(World)` | ✅ | |
| | `shutdown` 🆕 | `default void shutdown()` | 🆕 | |
| `IWorldMapProvider` | `CODEC` | `static final BuilderCodecMapCodec<IWorldMapProvider> CODEC` | ✅ | `register(...)` je na codecu — tačan potpis `register` nije provjeren |
| | `getGenerator` | `IWorldMap getGenerator(World) throws WorldMapLoadException` | ✅ | Ugrađeni ID-jevi: `"WorldGen"`, `"Disabled"` |
| `ChunkWorldMap` | `INSTANCE` | `public static final ChunkWorldMap INSTANCE` | ✅ | Ne-final klasa, `GeneratorChunkWorldMap` je nasljeđuje |
| `WorldMap` (`universe.world.map`) | | `WorldMap(int)`, `getChunks(): Long2ObjectMap<MapImage>`, `addPointOfInterest(...)`, `toPacket()` | ✅ | Rezultat generatora |
| `ImageBuilder` 🆕 | | vanilla crtač pločica (sjenčenje, fluidi, kvantizacija s Bayer ditheringom, `QUANTIZE_STEP=8`) | 🆕 | Interna klasa; ne zavisiti |
| `WorldMapSettings` | polja | `Box2D worldMapArea; float imageScale; float viewRadiusMultiplier; int viewRadiusMin, viewRadiusMax; UpdateWorldMapSettings settingsPacket` | ✅ | Konstruktor `(Box2D, float, float, int, int, UpdateWorldMapSettings)`; `getViewRadius(int)`, `withViewRadiusLimits(int,int)` |
| `WorldWorldMapConfig` 🆕 | konstante | `DEFAULT_IMAGE_SCALE=3.0`, `DEFAULT_SCALE=128`, `MIN_SCALE=32`, `MAX_SCALE=175`, `VIEW_RADIUS 3..32`, `DEFAULT_VIEW_RADIUS_MULTIPLIER=2.0` | 🆕 | `WorldMapConfig.ABSOLUTE_MAX_VIEW_RADIUS = 512` |
| `WorldMapTracker` | konstruktor | `public WorldMapTracker(Player)` | ✅ | Klasa nije `final` → može se naslijediti |
| | konstante | `MAX_IMAGE_GENERATION = 20`, `MAX_FRAME = 2621440`, `UPDATE_SPEED = 1.0f`, `EMPTY_UPDATE_WORLD_MAP_SIZE = 13` | ✅ | |
| | `setPlayerMapFilter` | `void setPlayerMapFilter(Predicate<PlayerRef>)` | ✅ | Filtrira samo **markere igrača**, ne pločice |
| | `clear()` / `clearChunks(LongSet)` 🆕 | `public void clearChunks(LongSet)` | 🆕 | Zvanični način da se **jednom igraču** ponovo pošalju određene pločice |
| | `sendSettings(World)` 🆕 | public | 🆕 | |
| | `setViewRadiusOverride(Integer)` / `getEffectiveViewRadius(World)` 🆕 | | 🆕 | Radijus mape po igraču |
| | `isAllowTeleportToCoordinates(PlayerRef, Player)` (static), `isAllowTeleportToMarkers(...)` 🆕 | | 🆕 | |
| | `discoverZone(s)` / `undiscoverZone(s)` 🆕 | | 🆕 | Otkrivanje zona po igraču (vanilla „fog") |
| | `copyFrom(WorldMapTracker)` 🆕 | | 🆕 | Postoji zbog prelaska između svjetova |
| | `getTransformComponent()` | public getter | ✅ | Explorers Map ga čita refleksijom — više ne treba |
| | privatno | `loadImages`, `writeUpdatePacket(List<MapChunk>)`, `loaded`, `pendingReloadChunks`, `markerTracker` | — | Interno |
| `Player` | `worldMapTracker` | `private final WorldMapTracker worldMapTracker`; samo `getWorldMapTracker()` | ✅ | **Nema settera ni fabrike** → zamjena moguća samo `Unsafe`-om |
| `MapMarkerTracker` | | `MapMarkerTracker(WorldMapTracker)`, `getSentMarkers()`, `sendMapMarker(MapMarker)`, `setPlayerMapFilter(...)`, `SMALL_MOVEMENTS_UPDATE_INTERVAL = 10.0f` | ✅ | |
| `WorldMapManager$MarkerProvider` | `update` | `void update(World, Player, MarkersCollector)` | ✅ | Poziva se **po igraču** |
| `MarkersCollector` | | `add(MapMarker)`, `addIgnoreViewDistance(MapMarker)`, `getPlayerMapFilter()`, `isInViewDistance(double,double)` | ✅ 🆕 | `addIgnoreViewDistance` = marker vidljiv bez obzira na udaljenost |
| `MapMarkerBuilder` 🆕 | | `(String id, String image, Transform)` + `withName(Message)`, `withCustomName`, `withIconSize`, `withCompassImage`, `withContextMenuItem`, `withComponent`, `build()` | 🆕 | |
| `MapMarkerOverride` | record | `(UUID id, String icon, String name, Boolean global)`; i `(String icon, String name, Boolean global)` | ⚠️ | Ima i `name` i `id`, ne samo `(icon, global)` |
| `DiscoverableMapMarkers` | | `isRevealed/reveal/hide(Player, String)`, `forEachMarkerInView(Player, ComponentAccessor, float, double, boolean, TriIntObjectConsumer<String>)`, `collectMarkersInView(...)` | ✅ | |
| `RevealMapMarkersInViewInteraction` | | postoji | ✅ | |

## Mapa svijeta — protokol

| Paket / tip | ID | Polja (tačno) | Status | Napomena |
|---|---|---|---|---|
| `UpdateWorldMapSettings` (S→K) | 240 | `enabled, allowTeleportToCoordinates, allowTeleportToMarkers, allowShowOnMapToggle, allowCompassTrackingToggle, allowCreatingMapMarkers, allowRemovingOtherPlayersMarkers` (bool), `defaultScale, minScale, maxScale` (float) | ⚠️ | **Server javlja klijentu dozvole za mapu** |
| `UpdateWorldMap` (S→K) | 241 | `MapChunk[] chunks, MapMarker[] addedMarkers, String[] removedMarkers` | ✅ | `IS_COMPRESSED = true` |
| `ClearWorldMap` (S→K) | 242 | — | ✅ | |
| `UpdateWorldMapVisible` (K→S) | 243 | `boolean visible` | ✅ | |
| `TeleportToWorldMapMarker` (K→S) | 244 | `String id` | ⚠️ | Polje je `id`, ne `markerId` |
| `TeleportToWorldMapPosition` (K→S) | 245 | `int x, int y` | ✅ | `y` = Z |
| `CreateUserMarker` (K→S) | 246 | `float x, float z, String name, String markerImage, Color tintColor, boolean shared` | ✅ | Limit 24 znaka nije u potpisu (u validatoru `UserMarkerValidator`) |
| `RemoveMapMarker` (K→S) | 119 | `String markerId` | ✅ | U paketu `packets.player` |
| `MapChunk` | — | `int chunkX, int chunkZ, MapImage image` | ✅ | |
| `MapImage` | — | `int width, int height, int[] palette, byte bitsPerIndex, byte[] packedIndices` | ✅ | Paleta potvrđena |
| `MapMarker` | — | `String id, FormattedMessage name, String markerImage, Transform transform, ContextMenuItem[] contextMenuItems, MapMarkerComponent[] components, MapMarkerIconSize iconSize, String compassImage` | ⚠️ 🆕 | Novo: `components`, `iconSize`, `compassImage` |
| `Transform` | — | `Position position, Direction orientation (yaw, pitch, roll)` | ✅ | Rotacija markera možda iz `yaw` (vidi NALAZI 3.6) |
| `ContextMenuItem` | — | `String name, String command` | ⚠️ | Polje je `name`, ne `label`; bez ikone i dozvole |
| `MapMarkerIconSize` 🆕 | — | `Default, Major` | 🆕 | |
| `MapMarkerComponent` 🆕 | — | podklase: `TintComponent(Color)`, `PlayerMarkerComponent(UUID)`, `PlacedByMarkerComponent(FormattedMessage, UUID)`, `HeightDeltaIconComponent(int upDelta, String upImage, int downDelta, String downImage)`, `CompassAlertComponent(String image, float durationSeconds, float timeoutSeconds, Color tint)` | 🆕 | **Boja markera nativno** (`TintComponent`) |

## Unos i presretanje paketa

| Klasa | Član | Tačan potpis | Status | Napomena |
|---|---|---|---|---|
| `IWorldPacketHandler<T>` | `handle` | `void handle(T, PlayerRef, Ref<EntityStore>, World, Store<EntityStore>)` | ✅ | |
| | `registerHandler` | `static void registerHandler(IPacketHandler, int, IWorldPacketHandler<T>)` + varijanta s `Predicate<PlayerRef>` | ✅ | |
| `SubPacketHandler` | | `void registerHandlers()` | ✅ | |
| `GamePacketHandler` | | `handleTeleportToWorldMapPosition`, `handleTeleportToWorldMapMarker`, `handleCreateUserMarker`, `handleRemoveMapMarker`, `handleUpdateWorldMapVisible` (svi `public`) | ✅ | |
| `PacketAdapters` 🆕 | `registerInbound` / `registerOutbound` | `static PacketFilter registerInbound(PlayerPacketFilter)`; isto za `PlayerPacketWatcher`, `PacketFilter`, `PacketWatcher`; `deregisterInbound/Outbound(PacketFilter)` | 🆕 | **Zvanični filter paketa u oba smjera, po igraču** |
| `PlayerPacketFilter` 🆕 | | `boolean test(PlayerRef, Packet)` | 🆕 | Značenje `true` (propusti/blokiraj) — provjeriti testom |
| `PacketHandler` | | `write(ToClientPacket)`, `write(ToClientPacket...)`, `writeNoCache(ToClientPacket)`, `writePacket(ToClientPacket, boolean)` | ✅ | |
| `HytalePermissions` | | `WORLD_MAP_COORDINATE_TELEPORT`, `WORLD_MAP_MARKER_TELEPORT` (`PermissionQuery`) | ✅ | Tačan string čvora nije u constant poolu ove klase |

## Anchor UI i legacy UI

| Klasa | Član | Tačan potpis | Status | Napomena |
|---|---|---|---|---|
| `AnchorActionModule` | | `static get()`, `register(String, AnchorActionHandler)`, `register(String, WorldThreadAnchorActionHandler)`, `unregister(String)`, `boolean tryHandle(PlayerRef, String)` | ✅ | |
| `AnchorActionHandler` | | `void handle(PlayerRef)` | ✅ | Akcija nosi samo ime |
| `UpdateAnchorUI` (S→K) | 235 | `String anchorId, boolean clear, CustomUICommand[] commands, CustomUIEventBinding[] eventBindings` | ✅ | |
| Anchor ID-jevi u serveru | | samo `"MapServerContent"` (`LeavePortalButtonUI`, `ReturnToHubButtonUI`) | ✅ | |
| `CustomUIEventBinding` | | `type, String selector, String data, boolean locksInterface` | ✅ | |
| `CustomUICommand` | | `type, String selector, String data, String text` | ✅ | |
| `CustomUICommandType` | | `Append, AppendInline, InsertBefore, InsertBeforeInline, Remove, Set, Clear` | ✅ | |
| `CustomUIEventBindingType` | | `Activating, RightClicking, DoubleClicking, MouseEntered, MouseExited, ValueChanged, ElementReordered, Validating, Dismissing, FocusGained, FocusLost, KeyDown, MouseButtonReleased, SlotClicking, SlotDoubleClicking, SlotMouseEntered, SlotMouseExited, DragCancelled, Dropped, SlotMouseDragCompleted, SlotMouseDragExited, SlotClickReleaseWhileDragging, SlotClickPressWhileDragging, SelectedTabChanged` | ✅ | |
| `UIEventBuilder` | `addEventBinding` | `(type, String)`, `(type, String, boolean)`, `(type, String, EventData)`, `(type, String, EventData, boolean)` | ✅ | |
| `EventData` | | record nad `Map<String,String>`; `of`, `append`, `put` | ✅ | |
| `CustomPage` (S→K) | 218 | `String key, boolean isInitial, boolean clear, CustomPageLifetime lifetime, commands, eventBindings` | ✅ | |
| `CustomHud` (S→K) | 217 | `String hudId, int zOrder, boolean clear, commands` | ✅ | |
| `CustomPageEvent` (K→S) | 219 | `CustomPageEventType type (Acknowledge, Data, Dismiss), String data` | ✅ | |
| `SetPage` (S→K) | 216 | `Page page, boolean canCloseThroughInteraction` | ✅ | |
| `Page` | | `None, Bench, Inventory, ToolsSettings, Map, MachinimaEditor, ContentCreation, Custom, Serverside, Chapters, ChapterRewards, PortalSummon, PortalActive, PortalError` | ⚠️ | Nove vrijednosti od `Serverside` |
| `PageManager` | | `setPage(Ref, Store, Page)`, `setPage(..., boolean)`, `openCustomPage(...)`, `closePage(...)`, `dev_setPage(Ref, Store, UIPage)` | ✅ | |
| `HudComponent` | | 26 vrijednosti, uklj. `Compass`, `BossBar`, `PortalPanel`, `Speedometer` | ⚠️ | 26, ne 24 |
| `HudManager` | | `setVisibleHudComponents`, `show/hideHudComponents`, `addCustomHud`, `removeCustomHud`, `dev_registerWidget(...)` | ✅ | |

## NoesisGUI (server-side UI) 🆕

| Klasa | Član | Potpis | Status | Napomena |
|---|---|---|---|---|
| `UIModule` | | `SERVERSIDE_NOESIS_UI_ENABLED` (private static final, nije compile-time konstanta), `requireServersideNoesisUi()`, `registerClassDefinition(...)`, `registerEnumDefinition(...)`, `defineClass(String)` | 🆕 | Poruka: *„Serverside Noesis UI is disabled. This feature is still in development and not available yet."* |
| `UISurface` / `UIPage` / `UIHudWidget` | | `UISurface(String id, String xaml)`, `registerCommand`, `setProperty(...)`, `setElementProperty(...)`, `insertItem`, `removeItem`, `beginBatch`, `onShow/onHide`; `UIHudWidget(id, xaml, HudWidgetSlot, int order)` | 🆕 | MVVM: XAML na klijentu + view-model sa servera |
| `UITypes` | | `Canvas`, `ScaleTransform`, `TranslateTransform`, `PathGeometry`, `ImageBrush`, `Viewbox`, `ScrollViewer`, `Storyboard`, ... | 🆕 | Svi gradivni blokovi za pravi map widget |
| `HudWidgetSlot` | | `Underlay, TopLeft…BottomRight, Overlay` | 🆕 | |
| Paketi | | `InitViewModelTypes`, `UpdateServersidePage`, `UpdateServersideHud`, `ExecuteServersidePageCommand` (K→S), `ExecuteServersideHudCommand` (K→S), `DismissServersidePage` (K→S), `SetPropertyServersideUICommand`, `InsertCollectionItemServersideUICommand`, ... | 🆕 | |
| Demo | | `ServersideUIDemoCommand`, `UI/Noesis/TestPage.xaml` | 🆕 | |

## Kamera, asseti, instance

| Klasa | Član | Potpis | Status | Napomena |
|---|---|---|---|---|
| `SetServerCamera` | 280 | `ClientCameraView clientCameraView, boolean isLocked, ServerCameraSettings cameraSettings` | ✅ | |
| `ServerCameraSettings` | | 34 polja, uklj. `distance, positionLerpSpeed, rotationLerpSpeed, displayCursor, mouseInputType, planeNormal, positionType, position, rotationType, rotation, sendMouseMotion, skipCharacterPhysics, canMoveType, baseFov, depthOfField` | ✅ | `PositionType: AttachedToPlusOffset, Custom` |
| `MouseInputType` | | `LookAtTarget, LookAtTargetBlock, LookAtTargetEntity, LookAtPlane` | ✅ | |
| `MouseInteraction` (K→S) | | `screenPoint, mouseButton, mouseMotion, worldInteraction (entityId, blockPosition, blockRotation)` | ✅ | Klikovi u `LookAtPlane` vjerovatno dolaze ovuda |
| `CameraSequenceBuilder`, `CinematicTeleport`, `PlayerCameraTopdownCommand` | | postoje | ✅ | Ugrađena „topdown" komanda kamere |
| `CommonAssetModule` 🆕 | | `sendAssetsToPlayer(PacketHandler, List<CommonAsset>, boolean)`, `sendAsset(CommonAsset, boolean)`, `sendRemoveAssets(...)`, `MAX_FRAME = 2621440` | 🆕 | **Javni API za slanje asseta jednom igraču** |
| `CommonAsset` | | `abstract`; `CommonAsset(String name, byte[] bytes)`, `(String, String hash, byte[])`, `getBlob0()` abstract | 🆕 | Može se naslijediti za PNG u memoriji |
| `AssetInitialize/AssetPart/AssetFinalize/RequestCommonAssetsRebuild` | 24/25/26/28 | `AssetPart.part: byte[]`, `AssetPart.MAX_SIZE = 4096006` | ✅ | |
| Texture Atlas API | | **nema klasa s „Atlas" u serveru** | ❌ | |
| `InstancesPlugin` | | `get()`, `spawnInstance(String, World, Transform)` (+2 varijante), `static teleportPlayerToInstance(Ref, ComponentAccessor, World, Transform)` | ✅ | |
