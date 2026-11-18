# 2. revize – Solms 1559, dávka „kniha5-B“ (`5-012v` – `5-026v`, skeny 460–490)

Revize podle `zdroje/ZADANI_REVIZE2.md` (plynulost „středně“). Soused `5-012r` jen čten; návaznost `5-012r` → `5-012v` sedí.
`sken`, `id`, `stav: zkontrolovano` a `overeno_clovekem: false` beze změny.

Ověření: `python -I nastroje/over_strany.py knihy/solms-1559 5-012v … 5-026v --prisne` → **31 stran, 0 chyb, 1 varování**.
Varování `5-026r` (foll/ift/fein) je plané: tisk má skutečně *fein ordenlich beschrieben* (= pěkně řádně), nejde o chybu OCR.

Skeny staženy z BSB IIIF (`bsb00085168_00460`–`_00490`); výřezy ve vyšším rozlišení u zlomků na s. 465, u přechodu stran 468/469,
u textu na rozkládacím listu 483 a u spodních řádků s. 488. Prohlédnuty všechny dřevořezy `drevorez-470` až `-487`.

## 1. Opravy originálu (`de`) a struktury podle skenu

| Strana | Bylo | Nyní | Pozn. |
|---|---|---|---|
| `5-012v` | `mit jren vn anderer` | `mit jren vnd anderer` | tisk *vñ* |
| `5-012v` | `alle walde/` | `alle wälde/` | |
| `5-013r` | `lassen rucken/` | `lassen rücken/` | |
| `5-015v` / `5-016r` | odstavec `… auff die ferr. Mit den Wagen … allezeit` | samostatný nový blok `Mit den Wagen vnd zu schaffung das vnd anders allezeit` (pokračuje `leichter/` na `5-016r`) | v tisku po *ferr.* krátký řádek a nový odstavec; jediná změna členění bloků |
| `5-016v` / `5-017r` | `das hat ein grossen onderscheidt/` + `scheidt/ nemlich` (slovo dvakrát) | `das hat ein grossen` + `vnderscheidt/ nemlich` | tisk *vnder-|scheidt*, slovo celé na stranu, kde končí |
| `5-018r` | `darzů` | `darzu` | |
| `5-019r` | `DIse … daraus mann auß … des Geschütz` | `Dise … daraus mann aus … des Geschützs` | tyto strany srubů nemají zdobnou iniciálu, jen větší písmo |
| `5-020r` | `DIe drit`, `darin gut`, `starcke Streichen` | `Die drit`, `darinn gut`, `stacker Streichen` | přesmyčku tisku *stacker* (tak i v `SPORNA_MISTA.md`) předchozí kontrola „opravila“; vrácena, poznámka |
| `5-022r` | `DAs fünfft` | `Das fünfft` | bez iniciály |
| `5-023r` | `DIse Figur`, `anzeigen thut.` | `Dise Figur`, `anzeigen thůt.` | |
| `5-024r` | `Das sibend Blochausz.`, `DIses Blochausz … Auszführung … Blochausz` | `Das sibend Blochauß.`, `Dises Blochauß … Außfürung … Blochauß` | ligatura ſz = ß jako na ostatních stranách; tisk *Außfürung* bez *h* |
| `5-025r` | `DIß … gross … Hauptblochauss … Blochauss` | `Diß … groß … Hauptblochauß … Blochauß` | |
| `5-025b-r` | `Das neundte Blochausz.`, `mit eynem kleinem`, `die Höhe` | `Das neundte Blochauß.`, `mit einem kleinem`, `die höhe` | zde iniciála *DIß* skutečně je |
| `5-026r` | `Krieg oder vberzug` | `Krieg oder vberzüg` | |

Ověřeno a ponecháno: všechna čísla na `5-012v`–`5-015v` (100000, 6000, 452000, 1461, 415260, 4152, 226, 904; zlomky 555½, 905½, 6½, 278, 452½, 28¼, 139, 226¼, 69½, 113, 12½, 34¾, 56½, 17, 28¼),
`452000 stcük`, `Zum dritten` bez předchozího *Zum andern* (`5-013r`), `die löch` (`5-017r`), `außgeuerdte` (`5-021r`), `witter die Gytter` (`5-025b-r`).
Nejisté: `vder` (`5-025b-r`) – první písmeno je nezřetelné, *o* i *v* možné, ponecháno; `Kozausca` (`5-013v`) – v tisku spíše *Rozausca* (R/K ve fraktuře), ponecháno.

## 2. Terminologie (celá dávka)

- *Geschwader* „švadro/švader“ → **švadrona** (glosář), *reisigen Zeug* „jízdní sbor“ → **jízda**.
- *Fendlein* u pěchoty „korouhev“ → **praporec** (`5-012v`, `5-013r`, `5-013v`).
- *Knecht* „landsknechti / pěší“ → **knechti** (glosář `knecht`; *landsknecht* je zakázaný tvar).
- *Renfan/Renfanen* „útočná korouhev {Rennfanen}“ → **předvojová korouhev {Renfanen}**.
- *Brechgeschütz* „obléhací dělostřelectvo“ → **průlomová děla**; *Feurwerck* {Fewerwerck} → **ohňostroj {Feurwerck}**.
- *Schantz/Schantzen* „zákop“ → **šance** (vč. *zwerg Schantz* = příčná šance); *Hauptleger* „hlavní tábor“ → **hlavní ležení**; *Leger* všude „ležení“.
- *Streichen* „{Streichwehr}“ → **boční obrany {Streichen}** (tvar tisku; glosář `bocni-obrana` má *streichen*).
- *Befestung* stálo v `{…}` bez českého slova → **pevnost {befestung}**; *Stocket* „palisáda s proutěnými koši“ → **palisáda** (dřevořez 480 ukazuje jen kůly).
- *Kriegßleut* „vojáci“ → **válečníci** (`5-017r`); *Kriegßuerstendigen* → **znalci válečnictví**.
- *Hertzogthumb* → **vévodství**, *Fürstenthumb* → **knížectví** (`5-013v`); vlastní jména (*Kozausca*, *Ifflandt*, *Marck*) bez `{…}`.
- `{…}` sjednoceny na podobu z tisku dané strany (`{Blochauß}`, `{Blochäuser}`, `{peß}`, `{pfundt}`, `{hauffen}` …).

## 3. Hlavní změny překladu po stranách

- **`5-012v`**: „zvláštní oddíl pro ohňostrojné stroje“ → „zvláštní zařízení pro ohňostroje“; „zpravodajsky vyložit a ukázat v písmu“ → „srozumitelně sepsat a ukázat“; *vndergraben/sprengen* bez vymyšlených `{…}` (tisk má *zugraben/zusprengen*). Opraveno **zdvojení na hranici stran**: konec „kteří se po každém boku rozjedou do pole“ + začátek `5-013r` „po boku do pole“ → „a na každé straně se nechají | vedle nich vyrazit do pole“.
- **`5-013r`**: dlouhý odstavec o předstrážní poště rozdělen do vět; „spojovací stráž za přední hlídkou a před předvojem“ → „mezi sebou a předvojem“; *Losamenter einzunemen vnd zu quartirn* „zabírali a ubytovávali ležení“ → „zabírali a rozdělovali ubikace {Losamenter}“; poznámka nově vysvětluje *Zum dritten*.
- **`5-013v`**: „Moskva dokáže postavit“ → „Moskvan {Mosca} zmůže“; „nelze všechno vyvést“ → „nevyvádí ze země celý“; poznámka doplněna (*Chelsce* neurčeno, vévodství × knížectví).
- **`5-014r`**: věty zjednodušeny („na počet bochníků 452 000 kusů“ → „452 000 chlebů“); poznámka k chybnému *1461 Achtel* přepočítána (správně ≈ 2 511 achtelů, váha 415 260 liber odpovídá ≈ 2 548 achtelům).
- **`5-014v`**: *muß mit jhm handeln lassen* → „musí strpět, aby se s ním nakládalo“; *wüst machen* „zbavit zásob“ → „vyplenit“; *Fundieren* „hranice“ → „základny“; *entsetzten* → „vyprošťovat“.
- **`5-015r`**: rozčlenění souvětí; poznámka k výpočtu zpřesněna (u 10 000 chlebů by správně bylo ≈ 55½ achtelu).
- **`5-015v`**: *sonder darumb zu kauffen sindt was mann bedarff* „nýbrž se za ně musí dát koupit“ → „musí být také co za ně koupit“; „snadné jednání“ → „snadné dílo“.
- **`5-016r`**: markytánská smlouva rozdělena do vět; „{Marck} Braniborsko“ → „Marku [Braniborskou]“; *Schleusen* „stavidla {Schleusen}“; *vermecht* → „zajistila“.
- **`5-016v`**: „dlouho se před Římany zdržovali“ → „dlouho se drželi a bránili proti Římanům“; *Brücken* „ložné dřevěné podlahy“ → „podlahy {Brücken}“.
- **`5-017r`**: první druh srubů přeložen přesněji (*ligen in den Blochäusern haussen stercker dann sie darinn sind* → „venku ve srubech leží silnější houf, než jaký je uvnitř“); *biß die andern Blochäuser auch kommen* „dokud nepřijdou posily z ostatních srubů“ → „dokud nepřijdou i ostatní sruby“; námitka o čtverci jako přímá řeč; poznámka přepsána (dříve nesrozumitelná).
- **`5-018r`–`5-025r`** (popisy srubů): sjednoceno „šance“, „boční obrany“, „výběžek“ (*außfürung*), „čtverec“ (*vierung*); `5-022r` *gleich dem Platz* → „podle povahy místa“.
- **`5-025b-r`**: rozčleněno; *Gytter* „průsečíky“ → „mřížka“; poznámky přepsány.
- **`5-026r`**: „branci z řad poddaných“ (přidaný význam) → „tolik válečného lidu, kolik je třeba“; *kundtschafft* „zpravodajské zprávy“ → „zprávy od zvědů“.

### Dřevořezy (`popis` přepsány podle obrázků)
Předchozí poznámky tvrdily, že texty a dřevořezy 3./4. a 6./7./8. srubu jsou „prohozeny“. **Nejsou**: každé vyobrazení stojí na rubu
listu a patří k textu na protějším líci (470→1., 472→2., 474→3. hranaté boční obrany, 476→4. okrouhlé boční obrany uprostřed stran,
478→5. kruhový srub se stanovišti uvnitř, 480→6. rondel s palisádou mezi šancemi, 482→7. čtverhranný výběžek na šanci, 484→8. srub napůl
ve vodě, 487→9. příčné šance 1–3). Mylné poznámky na `5-018r`, `5-021r`, `5-024r`, `5-025r` opraveny/odstraněny; popisy doplněny
o odkaz `[[…]]` na příslušný text. `5-025v` (vodní bašta, 486) nemá v tisku vlastní text. Popis `5-025a-v` dříve mluvil o „městské baště“ – na obrázku není.

## 4. Sporná místa k rozhodnutí

1. **`5-015v`/`5-016r`** – nový blok *Mit den Wagen …* (rozdělení odstavce podle skenu). Pokud má platit „neměnit strukturu bloků“ absolutně, lze vrátit; párování s tiskem je ale nyní přesné.
2. **`5-025b-r`** – *damit mann witter die Gytter der zwerg sehe* → „aby byla lépe vidět mřížka příčných šancí“. *Gytter* nejisté (mříž, síť průsečíků?).
3. **`5-025b-r`** – „9. a 10.“ vyobrazení: devátému odpovídá 487; které je desáté, není jasné (snad 486 na `5-025v`).
4. **`5-013v`** – *Kozausca* vs. tisk spíše *Rozausca*; *vder* (`5-025b-r`) – ponecháno, k ověření lidským okem.
5. **Úroveň nadpisů** *Das erst … neundte Blochauß* je `uroven: 2`; jako dílčí oddíly kapitoly o srubech by spíš patřily na `uroven: 3` (neměněno).
6. **`5-022r`** – *dieweil sie außwendig solche außfürung gleich dem Platz nit haben möchten* → „protože vně by podle povahy místa nemohla mít takové vysunutí“ (výklad *gleich dem Platz* nejistý).

## 5. Návrhy do glosáře

| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| `srub` (doplnit tvary) | srub | + Blochauß, Blochaus, Blochausz, Blochäuser, Blochäusern, Blochhäuser, Bloch oder Erdt Häuser | opevneni | Tvary tisku 5. knihy; bez nich `{Blochauß}`/`{Blochäuser}` nevedou na heslo. Pozn. rozšířit: u Solmse i velký zemní srub-pevnůstka (5. kniha), ne jen srubová stavba z trámů. |
| `stocket` (oprava cs) | palisáda | Stocket | opevneni | Dřevořez 480 ukazuje jen šikmé zašpičatělé kůly, žádné koše; cs „palisádové koše“ zavádějící. |
| `bocni-obrana` (cs) | boční obrana | + Streichen, streich | opevneni | V textu užíváno kratší „boční obrana“; plné „boční obranná stavba“ těžkopádné. |
| `stavidlo` (nové) | stavidlo | Schleusen, Schleusung, schleusen | opevneni | Stavidlo u srubu, jímž lze vzdouvat vodu a zaplavit kraj (`5-016r`, `5-019r`, `5-026v`). |
| `zasek` (nové) | zásek | verhegen, verhegung | opevneni | Zátaras z pokácených stromů v lesních průchodech (`5-016v`). |
| `pricna-sance` (doplnit k `sance`) | příčná šance | zwerg Schantz, Zwerchschantzen | opevneni | Šance kolmá k podélné, kryje ležení proti střelbě z výšiny (`5-025b-r`). |
| `ubikace` (nové) | ubikace | Losamenter, Losament | sluzba | Nocležiště knechtů v ležení přidělované po rotách (`5-013r`). |
| `bocni-straz` (nové) | boční stráž | seiten wart, seitenwart | sluzba | Jízdní stráž po boku pochodujícího vojska (`5-013r`). |
| `predni-hlidka` (nové) | přední hlídka | vorwart | sluzba | Nejpřednější jízdní hlídka před předvojem; s ním spojena „předstrážní poštou“ (`5-013r`). |
| `hlavni-houf` (nové) | hlavní houf | gewaltig hauff, gewaltigen hauffen | jednotky | Nyní pod heslem `sik`; v tažném řádu jde o hlavní voj mezi předvojem a zadním vojem. |
