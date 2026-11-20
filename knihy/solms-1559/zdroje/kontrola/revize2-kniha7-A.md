# 2. revize – Solms 1559, Sedmá kniha, dávka 7-A (skeny 546–565)

Strany: `7-erb-solms`, `7-titul`, `7-001r` – `7-009r` (19 stran; sken 548 = prázdný rub titulu).
Všechny strany: `stav: zkontrolovano`, `overeno_clovekem: false`.
Kontrola: `python -I nastroje/over_strany.py knihy/solms-1559 <19 stran> --prisne` → **0 chyb, 1 varování**
(7-003r blok 3: „fein“ – ve skenu skutečně *daß ers fein ordentlich … beschreib* = „pěkně“, falešný poplach, neopravitelné).
Sousedé 6-027r a 7-009v jen čteny (6-027r končí Šestou knihu, 7-009v začíná novými červenými kartami – žádná věta přes hranici dávky).
Skeny staženy z BSB IIIF (1400 px a 2400 px, výřezy) do scratchpadu `r7a/`.

## Ověření `de` proti skenům
- Přepis všech textových stran (549–554, 558) a nápisů na kartách (555, 559–562) souhlasí se skenem; žádná oprava `de` nebyla nutná.
- 7-001r: konec *vortheil hafftigs* má pod *s* drobné *t* → *hafftigst* správně; iniciála **IN** ověřena.
- 7-001v: *Vñ | wil* rozmazané (konec 1. a začátek 2. řádku), čtení podle smyslu potvrzeno; iniciály **ER**, **DIe** ověřeny; *Knech* je tisková chyba.
- 7-002r: duplicitní odstavec *Die andern 4000. Knecht…* je v exempláři skutečně orámován červenou tužkou; *aller zu gehörte gehn* tak opravdu stojí v tisku.
- 7-002v: *wann er … verdiessen* v tisku tak.
- 7-003r: iniciála **WAnn** ověřena; *Ja mag einer auch sagen…* je ve skenu součástí téhož odstavce (bez odsazení) – blokové členění správné.
- 7-006v: *fünffhūhert* (Bocchus) – nadtržené *ū* → *fünffhunhert* (tisková chyba) správně; u ostatních *fünffhūdert* → *fünffhundert*; *Pferdē spisser* → *Pferden spisser* správně.
- 7-006r: *Capi tander* (rozsypaná sazba), *Juiorta*, *veldhaptman*, *odder* – vše v tisku tak.
- 7-004v karta 9: místo čísla jen inkoustová skvrna a stopy písmen – potvrzeno. 7-008r: „100“ s poškozenou „1“, „50“ slabé, „25“ čitelné.
- 7-007v: *EDEL MĀ*, *CAPITĀ* (nadtržení) potvrzeno.
- Obrázek `drevorez-558.jpg` už v `obrazky/` existuje (celostránkový výřez se 4 kartami i vlepeným textem).

## Hlavní změny po stranách
- **7-erb-solms, 7-titul**: bez věcných změn (popisy erbu a císařského znaku sedí se skenem).
- **7-001r**: „a károu {Karn}“ → „a kárami {Karn}“ (plurál jako v dalším odstavci); „může svou karetní hru provozovat s potěšením a pro kratochvíli“ → „může při své karetní hře příjemně a pro kratochvíli trávit čas“ (*wol zu bringen*); „vezme všechna děla … a veškerou další výzbroj k tomu, jak k tomu patří“ → „vezme děla všeho druhu … a veškerou další výzbroj, která k nim patří a jaké je třeba“ (*von allerlei Geschütz*).
- **7-001v**: rozděleno souvětí o hlídkách; vypuštěna interpretační vsuvka „zatímco předvoj jede vpředu“ → „Potom ať nechá za sebou jet 2 koně, mezi sebou a předvojovou korouhví a předvojem vpředu…“ + nová pozn. 2 k nejasné syntaxi (*zwischen jm vnd dem Renfanen vnd vorzug dauorn*); pozn. 1 zpřesněna; poznámky přečíslovány (2→3, 3→4).
- **7-002r**: „To je správně řečeno. Je třeba tomu rozumět tak, že figury … znamenají“ → „Správně se na to odpovídá takto: figury … mají představovat“ (*ist recht daruon geredt … so sollen … sein*); „rozeznat“ → „zřetelně rozlišit“ (*vnderschidtlich*); „na čistou stranu na ně napiš“ → „na jejich čistou stranu napiš“.
- **7-002v**: bezslovesné odstavce doplněny: „Stejně tak [jména] všech plukovníků…“, „Rovněž [jména] plukovníků, kteří vedou pluky…“; „uspořádal na jménech“ → „k tomu použil jména“.
- **7-003r**: „má mít dobrou zkušenost“ → „má si dobře všímat“ (*gůt erfarung vnd auffsehens haben*); námitka hráče uhlazena („když karty stejně rozkládám zpaměti? Vždyť bych…“); „pěkně pořádně“ → „pěkně spořádaně“.
- **7-003v**: „Následující karty pak podávají zprávu“ → „Následující karty však ukazují“ (*Aber*).
- **7-004r**: popis karty 1 opraven podle skenu (žerď s korouhvičkou je uprostřed průvodu, v čele vpravo jezdec s chocholem, mezi koňmi pěší pacholci); „holi“ → „hole“.
- **7-005r**: „na nákladu sedí kohout“ → „v pozadí stany s praporky a štítky (na střeše jednoho sedí pták)“ – podle výřezu.
- **7-005v**: karta 2 – „dva vztyčené kyje či zahnuté hole“ → „nad houfem dvě zahnuté hole (snad biče či rohy)“.
- **7-006r**: „Himilkón, nejvyšší mistr dělostřelectva {oberster Artoloreimeister}“ → „nejvyšší zbrojmistr“ – glosář řadí *Artoloreimeister* pod heslo `zbrojmistr` (srov. i 7-001v *zeug oder Artolorei meister*).
- **7-006v**: popis obrázku opraven – pravý sloupec nemá „oddíl jízdních střelců“, ale pátého rytmistra (Bocchus) se střelci a pod ním tři karty děl; doplněna jména rytmistrů levého sloupce. „střelců s dlouhými hlavněmi {rohrn}“ → „s dlouhými ručnicemi“.
- **7-009r**: „prosvítají černé textové karty z rubu“ → „prosvítají (zrcadlově a šedě) červené textové karty z rubu listu (7-009v)“ – rub je tištěn červeně.
- **7-004v, 7-007r, 7-007v, 7-008r, 7-008v**: přepis i popisy karet ověřeny, beze změn kromě stavu.

## Sporná místa k rozhodnutí
1. **Droß / trén** – rozhodnutí 2026-11-17 stanoví pro knihy 6–9 *Drosser / Droß* = „trénní kůň“. V Sedmé knize jde ale o hromadné „trén“ (*neme den Droß von Reuttern vnd knechten*, *mit seinem Droß, Wagen vnd Geschütz*, *darauff soll der Droß ziehen*, *Geschütz/ Wagen/ Droß*). Ponecháno „trén {Droß}“; protože glosář má tvar *Droß* jen u hesla `trenni-kun`, vede odkaz na „trénní kůň“. Návrh: přidat *Droß* také k heslu `trén` (nebo v knize 7 psát {Troß}).
2. **7-001v** – *darnach 2. pferd nach vnd zwischen jm vnd dem Renfanen vnd vorzug dauorn ziehen lassen*: přeloženo neutrálně („mezi sebou a předvojovou korouhví a předvojem vpředu“) s poznámkou; možné i čtení, že předvojová korouhev s předvojem jede *dauorn* (vpředu) vůči hlavnímu houfu.
3. **7-006r / 7-009v** – *(oberster) Artoloreimeister*: v 7-A nyní „nejvyšší zbrojmistr“ podle glosáře; na 7-009v (dávka 7-B) stojí „mistr dělostřelectva {Artoloreimeister}“ – sjednotit.
4. **7-002r** – duplicitní odstavec a *aller zu gehörte gehn* ponechány doslova s poznámkou (viz zpráva překladatele).
5. **7-titul** – *Veldoberster* = „polní plukovník“: rozhodnuto heslem `polni-plukovnik` v glosáři, ponecháno.

## Návrhy do glosáře
| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| trén (doplnit) | trén | Droß | sluzba | hromadně trén vojska (7. kniha); nyní *Droß* jen u `trenni-kun` |
| zbrojmistr (doplnit) | zbrojmistr | oberster Artoloreimeister, Artolorei meister | delostrelectvo | tvary z karet 7. knihy |
| slechtic-od-del (opravit) | šlechtic dělostřelectva | – | velitele | kategorie: spíš `velitele` než `delostrelectvo` (úřad) |
| karetni-hra (opravit) | karetní hra | Kriegßkarten | sluzba | kategorie `osoby` je zjevně chybná; doplnit *Kriegßkarten* |
| kopinik (doplnit) | kopiník | spisser, Spiessern | jednotky | tvary z karet |
| lehka-jizda (doplnit) | lehká jízda / lehcí koně | geringe pferde, geringen pferd, leicht pferden | jednotky | |
| markytan (doplnit) | markytánský vůz | Marcatantenwagen, Macatanten wagen | zold | |
| kara | kára | Karn | zbrane | dvoukolý vozík na prach a koule |
| vozova-hradba (doplnit) | vůz vozové hradby | Wagenburgwagen, Rüstwagen | opevneni | |
| hlavni-houf | hlavní houf | gewaltig Hauff, mittelzug | jednotky | hlavní (střední) voj pochodového řádu |
| dvorska-celed | dvorská čeleď / služebníci | Hoffgesind, Hoffdiener, Hoffdiner | osoby | družina velitele (karty) |
| osoby (doplnit) | Himilkón, Hasdrubal, Syfax, Karthalo, Magón, Filip V. Makedonský, Juba I., Bocchus, Micipsa, Hiempsal, Saburra | Himilco, Astrubal, Syphax, Cartalo, Mago, Philippus Macidonie Rex, Juba, Pochus, Micipsa, Hiemsalem, Sabura | osoby | jména na kartách; k `jugurtha` doplnit *Juiorta*, ke `scipio` *Carnelius Scipio* |
