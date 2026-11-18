# 2. revize – Čtvrtá kniha (`4-erb-solms`, `4-titul`, `4-001r` … `4-023v`, skeny 386–434)

Rozsah: 41 stran (skeny 388, 396, 397, 400, 405, 409, 412 a 417 jsou prázdné a v edici nejsou).
Sousedé `3-067r` a `5-titul` jen čteny; navázání sedí (Třetí kniha končí celým odstavcem, `5-titul` začíná nadpisem).
Plynulost „středně“ podle `ZADANI_REVIZE2.md`: dlouhá souvětí rozdělena na věty v rámci bloků. Struktura bloků,
`sken`, `id`, `stav: zkontrolovano` a `overeno_clovekem: false` beze změny. Přechody `pokracovani: true`
(4-010r → 4-010v, 4-014r → 4-014v, 4-023r → 4-023v) dál sedí s originálem.

Kontrola: `python -I nastroje/over_strany.py knihy/solms-1559 <41 stran> --prisne` → **0 chyb, 1 varování**
(4-014v: *fein* = autentické příslovce „pěkně“, ověřeno ve skenu 416, opravit nelze).

## Celkové úpravy
- **Archaismy:** `jest` → `je` (94 výskytů, sjednoceno s revidovanou První knihou), `neb` → `neboť`,
  méně „jakož i“, „týž“, „veliký“.
- **`{Termín}` jen při prvním výskytu na straně:** odstraněny opakované závorky (4-001r, 4-002r, 4-017r, 4-020r,
  4-021r, 4-023r).
- **Terminologie podle glosáře:** *Artolorei/Arkolorei* = „dělostřelectvo“ (dříve „artilerie“); *Geschütz* = „děla“
  (dříve „malé dělostřelectvo“); *Reisigen* = „jízda“ (dříve „jízdní“); *Sturm/stürmen* jednotně „útok“ (dříve
  střídavě „zteč“); *Scharpffemetzen* = „šarfmece“ (dříve „šarfmecy“); *Artoloreimeister* = „zbrojmistr“ (4-023v);
  ve dvojici *Zeugmeister oder Artoloreimeister* (4-013r) je ponecháno „zbrojmistr neboli mistr dělostřelectva“.
- **Kladky vs. kotouče:** *Scheiben* u kladkostrojů (4-019r, 4-021r) = „kladky“ (dříve „kotouče“, což vedlo na heslo
  `kotouc` – nízké dělové kolo); *wendscheiblein* = „otočný kotouček“. *Stül* na 4-021r = „podstavce“ (dříve
  „stolice“, což vedlo na heslo moždířové stolice).
- **Hřídel** sjednocen v mužském rodě (hřídelem, hřídeli); *Zogbaum* = „tažný hřídel“ (dříve „naviják“, který
  patří heslu *Haspel*).

## Hlavní změny po stranách (před → po)
- **4-titul** – „k dělostřelectvu {Geschütz} a artilerii {Artolorei}“ → „k dělům {Geschütz} a dělostřelectvu
  {Artolorei}“; *Büchsen* s `{…}`.
- **4-001r** – posunutý podmět: „aby se přední řady knechtů rozestoupily, vypálily v druhý šik nepřítele“ → „knechti
  se vpředu rozestoupí, nechají [kusy] vypálit do druhého [tj. nepřátelského] šiku“ (střílejí děla, ne knechti);
  „hmotností koule střílet 2 libry železa“ → „střílet železnou kouli o váze 2 liber“.
- **4-002r** – chybné přiřazení: „Nástroj, jenž stojí v moždíři označený písmenem E“ → „Nástroj označený písmenem E,
  který stojí v moždíři“; „nic nepřekáží výhledu“ → „stolice, která nic nezakrývá“; *liecht* = „otevřená“.
- **4-003r** – *wel oder Zogbaum*: „hřídel neboli naviják“ → „hřídel neboli tažný hřídel“.
- **4-004r** – souvětí rozděleno na 5 vět; *Ploderwerck* „planý blikot“ → „plápolavý oheň“; doplněk „[nepřítele]“
  v hranatých závorkách; *Feuerwerck* = „ohňostroj“ (dříve „ohňostrojné střelivo“).
- **4-007r** – odstraněn přidaný výraz „toto tajemství“ (*Ich wil es … bei mir behalten* = „chci si to ponechat
  u sebe“); věta rozdělena na 6 vět.
- **4-008r** – *ledig ligen* „samostatně leží“ → „leží volně [bez lafet]“; *lingen* = „čáry“; přeformulováno
  měřítko 1 : 10 („skutečná koule má být desetkrát vyšší než každá z malých koulí“); *schawstück* = „kusy na
  podívanou“.
- **4-008v** – *zwo kern lenge* „dvě délky jádra“ → „obě podélné čáry jádra“ + **nová pozn. 1** (vývrt, ne dráha
  střely); *abzögen odder absetzen* = „odsazení či stupně“.
- **4-010r** – přidaný výraz odstraněn: „žene plyn střelu“ → „zapálený střelný prach se … žene vpřed na kouli“;
  rozděleno na věty; „pytlík / sáček“ sjednoceno na „pytlík“.
- **4-010v** – „ať je jádro nebo dělo za tím sebevíc křivé“ → „… vzadu sebevíc křivé“ (*hinder sich*);
  *zünglin* = „střelka“; doplněno *{Ror}*.
- **4-012r** – rozdělení na 7 vět; *verzichten* „kteří tato vyobrazení přehlížejí“ → „ti, kdo je pomíjejí“ (pozn. 1
  ponechána).
- **4-013r** – úvod rozdělen; *Patron* = „vzory“, *kreiden* – pozn. 1 přepsána (dřívější domněnka *Grad* vypuštěna:
  „křídou vyznačené rysky“).
- **4-014r** – přidané „špatná kola“ → „[nevhodně]“ v závorce; „kolaře“ → „koláře“; *da es auff geht* „kde
  spočívá na zemi“ → „kde jede po zemi“; *verwarn* = „dobře zajistit“ (*verwahren*).
- **4-014v** – `de`: OCR *süekt* → **sückt** (sken 416); pozn. 1 upravena. „tím se náprava prosekaně zeslabí“ →
  „náprava se vysekáním zeslabí“; přidané „pro zákolník“ odstraněno.
- **4-016r** – rozdělení vět, „Zaprvé / Zadruhé…“ jednotně; tloušťka hřebu „[stejnou] tloušťku až po šířku palce od
  špičky“.
- **4-017r** – přidané „s krátkými paprsky“ a „plných“ odstraněno; *dengel* = „zakolíkovat“ (souvisí
  s *verdägeln* na 4-017v; dříve „pevně skovat“); *Nägel* jednotně „hřeby“ (dříve „čepy (hřeby)“), přidané
  „vnějších“ vypuštěno.
- **4-017v** – *gantz* = „plný“ kotouč; popis upraven (hřeby místo čepů).
- **4-019r** – vypuštěno vsuvkové „(trojnožka)“; *scheiben* = „kladky“; *schůch* = „brzdná bota“.
- **4-020r** – rozdělení, opakované `{…}` odstraněny; „uzpůsoben pro dvě části“ → „k rozdělení na dvě části“.
- **4-021r** – kladnice / kladky / otočný kotouček (viz výše); „pod dělo se postaví podložky“ → „podstavce se postaví
  pod dělo“; *winde* = „hever“, *griff* = „dráp“.
- **4-022r** – *stral* „železný hrot s ostny“ → „železný šíp“ (na dřevořezu je šíp s ostnatým hrotem); řetězy →
  „řetízky“; *an den leit* „ležící pod nimi“ → „ležící u nich“.
- **4-023r** – *pfel blöcher* „rohatiny“ → „špalky s křížem prostrčenými kůly“; přidané „obránce“, „útočníky“,
  „horké [směsi]“, „při odražení zteče“ odstraněny; *Sturm* = „útok“, „[obraně proti] útoku“ v závorce.
- **4-023v** – *Artoloreimeister* = „zbrojmistr“; *elen* = „loket {elen}“; „nepřátelský lid“ → „mezi lidi“.

## Popisy obrázků (otevřeny jen sporné)
- **4-018v (424)** – „čtyřkladkový kladkostroj“ a „třínohý dělový zvedák (jeřáb)“ zpřesněny: kladkostroj ze dvou
  kladnic po dvou kladkách se zvonovitým břemenem; brzdná bota; trojnohý dělový kladkostroj „8“.
- **4-019v (426)** – rozporné „na trojnožce (čtyři nohy …) se samostatnou pátou (odnímatelnou třetí) nohou“
  přepsáno: dva páry spojených noh s hřídeli a západkovými koly, kladnice s hákem, samostatná noha pro trojnohou
  sestavu; nářadí: krumpáč, sochor, sekera (dříve chybně „široká motyka“), rýč.
- **4-020v (428)** – „osm sad kladnic“ → „osm kladnic ve čtyřech párech“ (6+6, 4+4, 2+2, 2+1 podle 4-021r);
  „třírohý a čtyřrohý kozlík“ → „lichoběžníkový a se šikmo rozkročenými nohami“; hever s drápem, stojan s otvory.
- **4-021v (430)** – „ostnatý oštěp“ → „železný šíp s ostnatým hrotem“, „zápalné pytle“ → „zápalné cáry“;
  přesnější rozmístění částí petardy.
- **4-022v (432)** – figura 24 nemá šňůrku, ale **dvě ouška** (sedí s textem *durch beide ohrn*); „zteč“ → „útok“.
- **4-023v (434)** – nápis na stuze „GRAEF“ → **„GRAFF“**, „MINCZE[N]“ → „MINCZEN“ (ověřeno na výřezu
  dřevořezu, shodné s 386).
- **4-005v** – „závažíovou skříň“ → „skříň protizávaží“.

## Ověřeno ve skenech
- Sken 416: *vnd sückt die in das Holtz* (OCR *fückt*, v datech chybně *süekt*) – opraveno v `de`; *fein gleich*,
  *fein gantz* – autentické.
- Dřevořezy 424, 426, 428, 430, 432, 434 (viz popisy výše).
- Beze změny ponecháno (OCR = tisk podle předchozí kontroly): *dengel*, *Legern*, *kern lenge(n)*, *verzeichet*,
  *verzichten*, *verdarressen*, *vngelechstem*, *vorgenenden*.

## Sporná místa k rozhodnutí
1. **4-017r** *noch zu bedencken* – přeloženo „obhlédnout“; může jít i o *bedecken* („zakrýt“). DE: *solches were
   nit zu laden/ abzusehen noch zu bedencken oder zu handeln*.
2. **4-001r** *vñ in die ander Ordnung gehen lassen* – vykládáno jako „nechají [kusy] vypálit do druhého
   [nepřátelského] šiku“; jiný možný výklad: „ustoupí do druhého (zadního) šiku“.
3. **4-012r** *die dise Figurn verzichten* – „kdo je pomíjejí“ (*verzichten* = zříci se), případně tisková chyba za
   *verrichten* („kdo s nimi pracují“); pozn. 1 uvádí obojí.
4. **4-017r** *auff den Legern* – „v leženích“ podle glosáře (`lezeni`); v dělostřeleckém smyslu může jít
   o „lože“ (podklad pro dělo).
5. **Rozepsané nosovky** (*vñ, mañ, dañ, eī, dz*) zůstávají v `de` celé 4. knihy (stejně jako ve 3. knize)
   v rozporu s § 2 PRAVIDEL; jde o rozhodnutí pro celou edici, neměněno.

## Návrhy do glosáře (glosář needitován)
- **id `jadro-vyvrtu`** – cs „jádro (vývrt)“, de *Kern, kern* (u kreslení a kontroly hlavně), kategorie
  `delostrelectvo`, pozn. „Vývrt hlavně a jeho osa; podle něj se kontroluje přímost hlavně (4-008v, 4-010r–v).“
  Současné heslo `jadro` (*jádrová dráha* = dráha střely) na 4. knihu nesedí; *Kern* z něj přesunout nebo heslo
  rozdělit.
- **id `zvedak`** – cs „zvedák“, de *Hebzeug, Hebzeugen, Hepzeug*, kategorie `delostrelectvo`, pozn. „Zvedací
  stojan nebo hever ke zvedání děl a náprav (4-013r, 4-021r).“ Z hesla `kladkostroj` tyto tvary vyjmout (nadpis
  4-013r staví *Zögen* = kladkostroje a *Hebzeugen* = zvedáky vedle sebe).
- **id `kladka`** – cs „kladka“, de *scheiben* (u kladkostrojů), kategorie `delostrelectvo`, pozn. „Otočné kolečko
  v kladnici; odlišit od `kotouc` (nízké dělové kolo).“
- **`otocny-kotouc`** – pozn. doplnit: u kladnic (*wendscheiblein*, 4-021r) jde o malou příčnou vodicí kladku pro
  lano, ne o zatáčecí prvek vozu.
- **`stolice`** – pozn. doplnit: *stül* na 4-021r = podstavce (kozlíky) pod dělo při mazání kol.
- **id `brzdna-bota`** – cs „brzdná bota“, de *schůch* (4-019r), kategorie `delostrelectvo`; tvar *schůch* je nyní
  v hesle `stopa` (míra) – kolize.
- **id `palec`** – cs „palec“, de *Zol, Zols, zol*, kategorie `miry`, pozn. „Zoll – asi 2,5 cm, dvanáctina stopy.“
- **id `spanelsky-jezdec`** – cs „břevno s kůly (španělský jezdec)“, de *pfel blöcher, geschrenckte pfel blöcher*,
  kategorie `opevneni`.
