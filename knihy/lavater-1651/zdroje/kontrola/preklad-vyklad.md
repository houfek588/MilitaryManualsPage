# Dávka L-T2 – výklad cizích slov a slovníček (vyklad-1 … vyklad-4, slovnicek-1, slovnicek-2)

Sken 9–14. Všechny strany byly prázdné (`chybi_original`), nově založeny, `stav: prelozeno`, `overeno_clovekem: false`.
`over_strany.py --prisne`: 0 chyb, 0 varování. Pole `de` zkontrolováno skriptem proti `zdroje/dta/0009–0014.txt`
(po odstranění „## “ a „- “) – shoda 1 : 1; jediná úprava: tisková zkratka „rc“ → „etc.“ (2×, vyklad-2) podle kniha.yaml.

## 1. Přehled stran

- **vyklad-1 až vyklad-4** – „Erklärung der frömbden Nammen vnd Wörteren“ (nadpis uroven 1): Lavaterův výklad
  57 opevňovacích a obléhacích termínů – německé heslo, latinské, francouzské, italské (španělské) ekvivalenty,
  v závorce „oder …“ výslovnost, odkazy na strany textu („liß das N. bl.“) a na mědirytiny („Kupffer, fig., písmeno“).
  Každé heslo = jeden blok `odstavec`. Heslo Hornwerck přechází z vyklad-3 na vyklad-4 (`pokracovani: true`).
- **slovnicek-1, slovnicek-2** – „Verdolmetschung“ (uroven 1), písmena abecedy uroven 3, 74 hesel cizích slov
  (franc./ital.) s německým výkladem; každé heslo = jeden `odstavec`. Na konci slovnicek-2 „Nota. Wie die Kupffer
  sollen eyngebunden werden“ – pokyny knihaři k vevázání mědirytin (dal jsem uroven 2 a 4 odstavce; není to část
  slovníčku, ale ani samostatná část předsádky – případně změnit na 1).

Formát překladu: `{německé heslo}`, cizí tvary v podobě z tisku, „(vyslov …)“ za Lavaterovo „(oder …)“
s výslovností, „–“ český termín podle glosáře, pak „Čti s. N; viz N. mědirytinu, fig. X, označeno …“.
Německé synonymní výrazy uvnitř hesla (sträb, schräge…; vnderwal, vnderstand…) ponechány v originále,
u srozumitelných přidán překlad v [hranatých závorkách]. Ve slovníčku: „Accord – mírové jednání.“; `{…}` jen
u hesel, která jsou (nebo mají být) v glosáři.

## 2. Sporná místa

| Strana | DE | CS | Proč sporné |
|---|---|---|---|
| všechny | „liß das 1. blat“, „das 1. bl.“ | „čti s. 1“ | „blat“ zde = strana tisku (kniha je stránkovaná; obsah odkazů sedí na s. 1–7). Vysvětleno v pozn. 1 na vyklad-1. |
| všechny | „(oder exteriür)“, „(oder Kortine/ korda …)“ | „(vyslov exteriür)“ | „oder“ v závorce uvádí výslovnost (výslovně u 1. hesla „wird außgesprochen“); kde „oder“ spojuje dva rovnocenné výrazy bez závorky („Couronnes oder Curonnes“, „Reduct, oder Corps degarde“), překládám „neboli“. |
| vyklad-1 | „Bollwerckspunet“ | {Bollwerckspunet} – špice bašty | Ve skenu skutečně „-punet“ = tisková chyba za -punct; v de ponecháno, pozn. |
| vyklad-2 | „mit ii, vnd 12. andeutet“ | „ukazují ii a 12“ | Ve skenu „i i“, pravděpodobně číslo 11 (číslice 1 v tisku podobná i); ponecháno dle DTA, pozn. |
| vyklad-2 | „(oder epole/ flanck/ rc)“, „Streychlinien/ rc.“ | „atd.“ | ꝛc. → etc. podle kniha.yaml (zadání zároveň žádá přesnou shodu s DTA – konflikt pravidel, zvoleno kniha.yaml). |
| vyklad-2 | „Groß Streychwinckel/ angle flanquant exterieur, angle de tenaille“ | velký obranný úhel | Podle s. 3–4 úhel, v němž se protínají prodloužená čela dvou bašt proti středu kurtiny; odkaz „mit 9.“ (= špice bašty) tomu na první pohled neodpovídá – ověřit na tab. 1. |
| vyklad-2 | „Streychwehr/ flanck/ … espaule, flanc, ala, spala, oreilon“ | flanka | Lavater slučuje flanku, plece a orillon; pozn. |
| vyklad-2 | „Blatte Bollwerck/ … plat Boulevart,) oder propugnakulum linie räckte.)“ | plochá bašta | Chybné závorky v tisku, ponechány v de. |
| vyklad-3 | „Kälpunct/ a ngle polygone“, „anglc, ou Centre“ | – | Tiskové chyby (angle; angle du centre), v de ponecháno, pozn. |
| vyklad-3 | „Berm/ zehen/ oder füß am Wal/ lisiere: margovalli“ | „zehen neboli füß am Wal [prsty neboli pata valu]“ | „margovalli“ = margo valli (tisk bez mezery), ponecháno. |
| vyklad-3 | „Faussebraye … chemin des rondes: runde weg“ | dolní val … obchozí cesta | Na s. 5–6 Lavater obojí rozlišuje (zeď vs. zemní předprseň), zde jako synonyma; pozn. |
| vyklad-3 | „Bedeckter weg/ … auch abusivè contrescarp“ | „nesprávně (abusivè) též contrescarp“ | Lavater označuje toto užití za zneužití slova – viz rozdíly vůči glosáři. |
| vyklad-3 | „Cavalieurs, Katzen/ Reuter“ | kavalíry | „Reuter“ = „jezdci“ (doslovný překlad cavalier), [kočky, jezdci] v závorce. |
| vyklad-4 | „Cronwerck/ opera Coronata: ouurages (oder vfrasches) Couronnes“ | – | „ouurages“ = ouvrages (u za v); „vfrasches“ = výslovnost [uvráš]; ponecháno. |
| vyklad-4 | „Fůßängel/ Minckers/ … tribuli chausses, trappes“ | nášlapné bodce | „Minckers“ nejasné (snad nizozemské/dialektní); „chausses, trappes“ = rozdělené chausse-trappes. Čeština pro caltrop: zvolil jsem „nášlapné bodce“, protože „ježek“ je v glosáři obsazen (šik). |
| vyklad-4 | „Schantzkörb/ Carbes loricales“ | šancovní koše | „Carbes“ zřejmě tisková chyba za Corbes; ponecháno. |
| vyklad-4 | „Tranchée, Tränschey/ eynschantzungen/ … es seind werck so im Feld ein gantz Läger vmbgeben“ | zákopy: díla, která v poli obklopují celé ležení | Lavater = obkličovací linie ležení, ne přibližovací zákop; pozn. |
| vyklad-4 | „Reduct, oder Corps degarde, Redoute: receptus“ | reduta | Ztotožnění reduty se strážnicí; pozn. |
| slovnicek-1 | „Casquet, Stechbelm.“ | kolčí přilba | DTA „Stechbelm“, ve skenu spíš „Stechhelm“ (b/h v lomeném písmu nejisté); věcně nepřesné (casquet = lehká otevřená přilba). V de ponecháno dle DTA. |
| slovnicek-1 | „Capitain des armes, Rüst oder Gewehrmeister.“ | správce zbroje neboli zbraní | Nechtěl jsem „zbrojmistr“ (= Zeugmeister, dělostřelectvo) ani „zbrojní mistr“ (nepouzivat). |
| slovnicek-1 | „Corporal, Rottmeister.“ | {Corporal} – rotmistr | Lavaterův výklad je „rotmistr“, glosář má Corporal = desátník – viz níže. |
| slovnicek-1 | „Galloppieren, oder / Calloppieren, } rennen.“ | „Galloppieren neboli Calloppieren – cválat.“ | Svorka v tisku; sloučeno do jednoho bloku (stejně „Neutral, Neutralitet, Vnpartheyisch.“). „rennen“ = cválat (u koně), ne „běžet“. |
| slovnicek-2 | „Particular, Gemein.“ | obyčejný | Smysl nejistý (soukromý / obecný); pozn. |
| slovnicek-2 | „Quartier geben/ Sicher gleit geben.“ | poskytnout bezpečný průvod | Věcně = dát pardon a bezpečné propuštění; pozn. |
| slovnicek-2 | „Die drey Kupffer der Exereitien“ | {Exereitien} | Tisk „Exereitien“ (= Exercitien), ponecháno. |

## 3. Ověřeno ve skenu (DTA 1600px, sken 9, 10, 12, 13)

- sken 9: „Bollwerckspunet“ (tisková chyba v originále), uspořádání odstavců hesel.
- sken 10: „mit i i, vnd 12.“ (patrně 11), zkratka ꝛc. („rc“) 2×, chybné závorky u „Blatte Bollwerck“.
- sken 12: „Carbes loricales“, „vfrasches“, „Echim“, „chausses,trappes“, „vnd vnd 75.“ – vše skutečně v tisku.
- sken 13: dvousloupcová sazba slovníčku; svorka „Galloppieren, oder / Calloppieren, } rennen.“; „Stechbelm/Stechhelm“ (nejisté); kustod „N. Neu-“ a signatura „)( )( ij“ vynechány.

## 4. Návrhy do glosáře

### 4a. Doplnění stávajících hesel (nové tvary `de` z výkladu a slovníčku)

| id | doplnit de | pozn. / úprava |
|---|---|---|
| pevnost | Munimentum, munitio, fortalitium, fort, forteresse, fortezza, fortificatione | – |
| val | vallum, riparo, terra plena, terraces, terre plein | Lavater řadí mezi synonyma valu i „contregarde“ (u pozdějších autorů samostatné vnější dílo – kontrgarda); nepřidávat jako de, jen zmínit v pozn. |
| predprsen | parapet, parapeta, thorax, lorica | – |
| banket | Banquet, statio, scamnum, scabellum, gradus ad loricam | – |
| kurtina | Cortin, Chorda, Cortina | – |
| flanka | flanc, espaule, ala, humerus propugnaculi, achsel, schulteren, flügel, streych | Lavater slučuje flanku s plecí (espaule) a orillonem (oreilon) – v pozn. upozornit. |
| basta | Boulevart, propugnaculum, Sporen | – |
| celo-basty | facies, frons, face, il fronte, gesichter, stirnen | – |
| hrdlo-basty | schlund, gorge, linea faucium | **Käl-linien / Källinien vyjmout** do nového hesla „linie hrdla“ (Lavater je odlišuje). |
| berma | lisiere, margo valli, zehen, füß am Wal | pozn.: Lavater ji nazývá i „pata valu“ (s. 5), šíře 4–8 stop. |
| faussebraie | fossebraye, Succinctus, vnderwal, vnderstand, vnderlauff | – |
| prikop | fosse, fossa | – |
| kontreskarpa | contrescarpa, acclivitas exterior, gegenschräg, gegenböschung, Contrascarpe | **pozn. upravit**: Lavater výslovně označuje užití „contrescarpe“ pro krytou cestu za nesprávné (abusivè). |
| kryta-cesta | Bedeckter weg, via cooperta, strada coperta, vallado | „spianade“ Lavater řadí ke kryté cestě, glosář ho má u glacis (Esplanade) – ponechat u glacis, zmínit v pozn. |
| ravelin | Ravellein, Castellum defixum, moles | **Rozdělit** – viz 4c (halber Mond zvlášť). |
| hornwerk | opera Cornuta, ouvrages à corne | – |
| korunni-dilo | opera Coronata, Couronnes | – |
| palisada | Palissades, sudes praepilatae | – |
| staketa | – | **pozn. upravit**: Lavater: „grosse höltzer vnd zäun vmb ein Wal“ – nic o tom, že by byl nižší a hustší než palisáda. |
| sturmhaspel | Barricades, cavaliers de Frises, Friesische Reuter, Echini | pozn. „španělský jezdec“ doplnit o „fríský jezdec“. |
| sancovni-kos | gabions, gabionatten, Schantzkörb | – |
| batterie | Batteries, agger tormentarius | – |
| aprose | Approches, Lauffgräben | – |
| zakop | Tränschey, eynschantzungen | **pozn.**: u Lavatera (s. 124–125) souvislé opevnění kolem celého ležení (obkličovací linie). |
| mina | cuniculi, vndergrabung, Sprenge | – |
| galerie | Schirmdach, vinea | – |
| kavalir | Cavalieurs, Reuter | Heslo „kocka“ (Katzen, Fronsperger) a „kavalir“ (Katz) se překrývají – u Lavatera „Katzen“ = kavalír. |
| retransement | Retranchieren, retrenche, verschantzungen | – |
| hlavni-straz | Corps de guarde | – |
| korporal | – | **Rozpor**: Lavater „Corporal, Rottmeister“, Lancepasade = „Vnder-Rottmeister“. Glosář: Corporal = desátník. Zvážit „korporál“ (s pozn. „u Lavatera = rotmistr“). |
| kompanie | – | Lavater „Compagnie, Ein Fendlein fůßvolck“ – v souladu s pozn. glosáře. |
| pikenyr | Picquenier | pozn.: Lavater pikenýra ztotožňuje s dvojžoldnéřem. |
| pika | Picques | – |
| vachmistr | Sergeant | **pozn.**: u Lavatera Wachtmeister = seržant kompanie (Sergeant), Obrist-Wachtmeister = major; glosářová pozn. (Fronsperger: velitel stráží) neplatí beze zbytku. |
| plukovnik | Collonell, Regiments-Oberst | – |
| musketa | Musquet, Lunden Rohr | – |
| delostrelectvo | Artillerie | – |
| dela | Canon | – |
| protipisar | Controlleurs | – |
| posadka | Garnison | – |
| konvoj | Convojieren | (už má convojieren) |
| proviant | Commiß, Vivres | – |

### 4b. Nová hesla – opevnění (kategorie `opevneni`)

| id | cs | de | pozn |
|---|---|---|---|
| real | real (královské dílo) | Real, Royal, Hauptschantz, Hauptwerck | Plné opevnění s baštami; Lavater/Freytag dělí na velký, střední a malý Real podle délky obranné linie (s. 1). Pracovní překlad 001 má „královská“. |
| vnejsi-polygon | vnější polygon | Polygonal-linien, vill-egk, polygone exterieur, Latus polygoni exterioris | Strana mnohoúhelníku spojující špice dvou sousedních bašt. |
| vnitrni-polygon | vnitřní polygon | Interieur polygone | Spojnice dvou bodů hrdla. |
| spice-basty | špice bašty | Bollwerckspunet, Bollwercksspitz, Punct des Bollwercks, angle flanqué, Angulus propugnaculi | Vrchol bašty, průsečík obou čel (s. 5). |
| polni-sance | polní šance | Feldschantz, Feldschantzen, Munitio Campestris, Castellum Campestre, fortino | Menší opevnění pod „malým Realem“ (s. 1). |
| vyska-valu | výška valu | Höhe des Wals, altitudo valli, Hauteur du rampart | (lze vynechat) |
| svah | svah | abdachung, Superficies, schräge, böschung, sträb, gäche, ablauff, abhang, docierung, bossierung, talud, acclivitas | Sklon valu, předprsně či příkopu; vnitřní a vnější. |
| ochoz-valu | ochoz valu | Walgang, vallum ambulacri, terreplein | Horní plocha valu za předprsní (terreplein). |
| druhotna-flanka | druhotná flanka | Affterstreych, Hinderstreych, secund-flanck, second flanc, ala secundaria, Streychplatz | Úsek kurtiny od flanky k bodu, odkud lze ostřelovat čelo protější bašty (s. 3). |
| velky-obranny-uhel | velký obranný úhel | Groß Streychwinckel, angle flanquant exterieur, angle de tenaille, Angulus defensionis major | Průsečík prodloužených čel dvou bašt proti středu kurtiny (s. 3–4). |
| maly-obranny-uhel | malý obranný úhel | klein Streychwinckel | Úhel mezi kurtinou a obrannou linií (s. 5). |
| uhel-plece | úhel plece | Winckel der Schulteren, espaule | Úhel mezi čelem a flankou, min. 105° (s. 5). |
| hlavni-linie | hlavní linie (kapitála) | Hauptlinien, ligne capitale, linea principalis | Od bodu hrdla ke špici bašty (s. 4). |
| plocha-basta | plochá bašta | Blatte Bollwerck, plat Boulevart, propugnaculum lineae rectae | Bašta na přímé linii (uprostřed dlouhé kurtiny). |
| mala-obranna-linie | malá obranná linie | klein Streychlinien, ligne de défense flanquante, linea defensionis minor/mobilis, defensiva stringens | Prodloužení čela k druhotné flance; palba „stírá“ čelo (rasantní). |
| velka-obranna-linie | velká (stálá) obranná linie | Groß Streychlinien, beständige Streychlinien, beständige defenslinien, angeheffte Streychlinien, ligne de défense fichante, linea defensionis affixa/major | Od styku kurtiny a flanky ke špici protější bašty; max. 60 prutů = dostřel muškety (s. 1, 4–5). **Pozn. ke stávajícímu heslu obranna-linie**: jeho pozn. popisuje spíš malou linii, údaj 60 prutů se ale týká velké – rozdělit nebo pozn. přepsat. |
| prodlouzeni-flanky | prodloužení flanky | Erlängerung der Streychen, flanc prolongé, ala humeri producta | – |
| bod-hrdla | bod hrdla | Kälpunct, Kälpuncten, angle polygone, angulus polygoni | Průsečík prodloužených kurtin, vrchol vnitřního polygonu (s. 5). |
| linie-hrdla | linie hrdla | Käl-linien, Källinien, Kälinie, linea faucium | Prodloužení kurtiny od flanky k bodu hrdla (pozdější „poloviční hrdlo“). |
| stredovy-uhel | středový úhel | eck Centri, Angulus ad Centrum, angle du centre | Úhel dvou poloměrů ve středu pevnosti. |
| maly-polomer | malý poloměr | klein halbe Diameter, Semi-Diameter polygoni interioris, petit demi-diamètre | Střed → bod hrdla. |
| velky-polomer | velký poloměr | groß halb Diameter, Semi-diameter polygoni exterioris, demi-diamètre le grand | Střed → špice bašty. |
| obchozi-cesta | obchozí cesta | Ronde-weg, runde weg, chemin des rondes, Chemin de Ronde | Rozšířená berma se zdí na vnější hraně (s. 5–6); se zemní předprsní = dolní val. **Pozor:** heslo „rond“ (obchůzka) má de „Ronde“ – hrozí kolize odkazů. |
| eskarpa | eskarpa | scarpa, acclivitas fossae interior, jnner abhang des Grabens | Vnitřní svah příkopu na straně valu. |
| predprsen-kryte-cesty | předprseň kryté cesty | Brustwehr des bedeckten wegs, parapet du chemin couvert | Podle s. 7 se 50–100 stop „ztrácí do pole“ – fakticky glacis. |
| pulmesic | půlměsíc | Halber Mon, halber Mond, demies lunes, demi-lune, luna dimidiata | **Odlišit od ravelinu**: u Lavatera malá bašta vně příkopu před baštou (ne před kurtinou). |
| klešte | kleště | Zang, tenaille, forcipula, tenaglia | Dílo s dovnitř zalomenou frontou. |
| clona | clona | Blendungen, Blendung, Chandeliers, Velamen | Rám s otýpkami/fašinami kryjící obléhatele. |
| naslapne-bodce | nášlapné bodce | Fůßängel, Fußangel, lämeysen, Minckers, Murices, tribuli, chausse-trappes | Čtyřhroté železné bodce; nepoužívat „ježek“ (obsazeno šikem). |
| strelecky-kosik | střelecký košík | Schützenkörblein, Corbeilles, corbulae | Malé koše se zeminou na předprsni, mezery = střílny. |
| protiaprose | protiaproše | Gegenlauffgräben, contre approches | – |
| prulom | průlom | Breche, Bresche, Ruina valli, bruch des Wals | – |
| protimina | protimina | Contremine, Contraminen, cuniculi reciproci | – |
| traverza | traverza | Travers, Trauers, Zwerchwäl, Loricae transversae | Příčný val proti boční palbě (s. 6, 18). |
| reduta | reduta | Reduct, Redoute, receptus | Malá uzavřená šance; Lavater ji ztotožňuje s corps de garde. |
| odriznuti | odříznutí | Abschnitt, abschnitt | Vnitřní příčné opevnění za průlomem nebo uvnitř díla; nyní v heslu retransement – lze ponechat tam. |

### 4c. Nová hesla – vojsko, úřady, dělostřelectvo (ze slovníčku)

| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| konstabl | konstábl | Constabel, Cannonier | delostrelectvo | Dělostřelec 17. stol., odpovídá puškaři (Büchsenmeister). |
| kartuse | kartuše | Cartusen, Patronen | delostrelectvo | Náboj v papírovém/plátěném obalu; u Lavatera s broky (kartáčová). |
| granat | granát | Granaden, Sprengkuglen | delostrelectvo | Výbušná koule. |
| lafeta | (doplnit) | Laffuyten, Stuck-Wägen | delostrelectvo | Doplnit do stávajícího hesla lafeta. |
| auditor | auditor | Auditeur | pravo | Vojenský soudce pluku. |
| major | nejvyšší vachmistr (major) | Major, Obrist-Wachtmeister | velitele | Zástupce plukovníka pro šikování a službu. |
| spravce-zbrani | správce zbraní | Capitain des armes, Rüstmeister, Gewehrmeister | velitele | Poddůstojník kompanie pro zbraně a zbroj. |
| lancepasade | podrotmistr | Lancepasade, Vnder-Rottmeister | velitele | Franc. anspessade, zástupce korporála. |
| kornet | korneta | Cornet | jednotky | Jízdní kompanie i její praporečník. |
| miner | minér | Mineurs | opevneni | „Mistr podkopávání“. |
| inzenyr | inženýr | Ingenieur, Jngenieur, Bawmeister | opevneni | Stavitel pevností (Freytag „der Jngenieur“, s. 1). |
| guverner | velitel pevnosti | Gouverneur | velitele | „Představený pevnosti“. |
| markytan | markytán | Marquitanter | zold | Dovozce proviantu do ležení. |
| pice | píce | Fourrage, Füterung | zold | – |
| dobrovolnik | dobrovolník | Voluntaire | jednotky | Slouží na vlastní náklad. |
| vypad | výpad | Sorties, außfäll, außfallen | sluzba | – |
| odlehceni | odlehčení (pomoc obleženým) | Secours, Entsatz, Secondieren | sluzba | – |
| kulaty-stit | kulatý štít (rondache) | Rondache, Ronde schilt | zbrane | Štít „Schilt“ ve cvičeních Třetího dílu. |

## 5. Osoby a místa

Na stranách dávky žádná vlastní jména (v poznámkách jen odkazy na Freytaga a Marolois ze s. 1 a 6 – osoby do rejstříku
patří k těmto stranám; Samuel Marolois zatím v glosáři chybí – navrhuji heslo `marolois`, „Samuel Marolois“,
de: Maralois, Marolois, kategorie osoby, pozn.: nizozemský matematik a autor příručky opevňování Fortification ou
architecture militaire, 1615).

## 6. Postřehy mimo dávku (needitováno)

- Strana 001 (pracovní překlad) má „Courtine“ → „cimbuří“, „Flancken oder Streychwehren“ → „boky nebo cimbuří“,
  „Gesichtlinien“ → „čelní linie“ – v rozporu s glosářem i s Lavaterovým výkladem; doporučuji revizi.
- Na stranách 3–7 se objevují termíny z bodu 4b (Affterstreych, klein/groß Streychwinckel, Källinien, Kälpunct,
  Ronde-weg, Contrascarpe/gegenschräg) – po doplnění glosáře sjednotit.
