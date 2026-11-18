# 2. revize – Druhá kniha, dávka D (038v … 053v)

Rozsah: 27 stran (skeny 164–190): konec kapitoly o proviantu (výdej chleba, masa, píce, tabulky dobytka a ovsa,
zásobování při průchodu zeměmi, podunajská plavba obilí do Budína), kapitoly *Oberster vber alle Reutter*,
*Von des Wagenburgmeisters Ampt* a začátek *Der Reuter Wachtmeister*. Sousedé `038r` a `054r` jen čteny
(navázání vět 038r→038v „… a | při koupi …“ a 053v→054r „… před nejvyšším | polním hejtmanem …“ sedí).

Plynulost „středně“ podle `ZADANI_REVIZE2.md`: dlouhá souvětí rozdělena v rámci bloků, struktura bloků, `id`,
`sken`, `overeno_clovekem: false` beze změny; přechody `pokracovani: true` (038v, 039v, 040r, 042r, 042v, 043r,
043v, 044r, 044v, 045r, 045v, 049r, 050v, 052r, 052v, 053v) zachovány a znovu sladěny (044v→045r přepsán).

Kontrola: `python -I nastroje/over_strany.py knihy/solms-1559 038v … 053v --prisne` → **0 chyb, 1 varování**
(050v blok 2 „fein“ – jde o tiskovou podobu *gegen dem fein* = *Feind*, ověřeno ve skenu 186, vysvětleno pozn. 1;
neopravitelné).

## Opravy `de` podle skenů (BSB IIIF)

| strana | bylo | tisk (sken) | pozn. |
|---|---|---|---|
| 042r | als were er der Ordnung nach **verzicht** | **verricht** (*verꝛicht*) | mění smysl: „jako by byl podle pořadí obsloužen“ (dříve „jako by se pořadí zřekl“) |
| 045v | die **von** Prelaten | **vor** | tisková chyba, nová pozn. 1 |
| 045v | wasser **abwerts** | **abwers** | tisková chyba, nová pozn. 3 |
| 046r | im **vorath** | **vorrath** (*voꝛrath*) | chyba OCR |
| 046v | tabulka vzdáleností `6.0`, `9.0` … (YAML float) | **6., 9., 20., 12., 15., 10., 10., 7., 15.** | čísla jako řetězce podle tisku |
| 050r | Kriegß**s**tendigen | **Kriegsstendigen** | pozn. 1 upravena |
| 050v | Krieg**ß**uolck; Fre**ü**nden (2×) | **Kriegsuolck; Freunden** | |
| 052r | zu **lägern** | **lägeln** | tisková chyba, nová pozn. 3 |
| 052r | Es soll **der** Feldmarschalck | **ber** | tisková chyba, nová pozn. 5 |

Ověřeno beze změny: *aucht thůn*, *gefllig* (042r, tiskové chyby – nová pozn. 1), *nicht gerechnet vnd geordnet*
(043r), *an der vñ desselben Fleckens*, *böse Zilen* (045v), *greydt*, *damit kein durchauß*, *gewich* (046r),
*Mechausen* (2×), *28000. Mann* (046v), *geriegen*, *gegen dem fein* (050v), *Büchen*, *Wabenburg* (052r),
*die nach* (053r). Číslo listu na skenu 187 je „52“ (ID 052r sedí). V 043r tisk možná čte *sölliche straffen*
místo *strassen* – v rozlišení skenu nerozhodnutelné, ponecháno *strassen* (smysl).

Tabulky dobytka (039r–040v) a ovsa (041v–042r) přepočítány: součty sedí s poznámkami o tiskových chybách,
poznámky ponechány. Hlavičky dílčích tabulek sjednoceny na „Na jeden den / týden / měsíc“ (040r, 040v).

## Hlavní změny překladu po stranách

- **038v** – „nepochybně se totiž stává“ → „Když se totiž veze do ležení, nikdy to nechybí: strhne se tlačenice…“
  (*es felhet nicht*); věta o pořadí výdeje rozdělena („Na který by se nedostalo… u toho se má druhého dne začít
  znovu“); poslední blok zpřirozen („aby se řádně platilo tak, jak je to u každého praporce… stanoveno“).
- **039r** – rozdělen blok o potvrzeních proviantního pána; překlep „k dopraveni“ a „pokud je je vůbec“ opraveny;
  *Regiment* = „řízení“ bez `{Regiment}` (odkazovalo by na heslo *pluk*); „mnohem více“ → „více“ (*etwas für*).
- **039v** – „aby se neporazilo a nezkazilo“ → „aby se neporáželo příliš mnoho ani příliš málo“ (*abthů vnd schlage*).
- **041r** – „poloviční díl“ → „polovina předchozího řádu“; „neporážel najednou na jedné hromadě“ → „neporážel
  všechen najednou“; *nicht hoch an zufechten* „nemělo by se to příliš stíhat“ → „nemělo by se mu to příliš upírat“.
- **041v** – úvodní blok o korci/achtelu rozdělen do 4 vět.
- **042r** – *verricht* (viz výše); *mit glauben* „na dluh“ → „na úvěr“; „svobodný trh“ → „volný trh“, „drobnou
  drůbež“ → „drobný dobytek“ (*gering viehe* zahrnuje i husy); blok o soleném mase přestavěn, dvojí podmět
  „mistr vozové hradby a vozmistr… mají dohlédnout“; nová pozn. 1, poznámky přečíslovány podle textu.
- **042v** – blok o říšském tažení (2000 znaků) rozdělen na 9 vět; *biß zu dem Obersten* „až k plukovníkovi“.
- **043r** – „potravinami (viktualií)“ → „potravinami“; závěr „nemá být… přehlížen, nýbrž řádně uspořádán“
  (přidaný text) → „Toto se má v době, kdy se budou tažení nařizovat, započítat a uspořádat“ + pozn. 1 přepsána;
  *sein ansuchen fürzusetzen* = „předem ohlásit druhému svou žádost“ (dříve „vypomoci“).
- **043v** – blok o proviantním pánovi a pekařích rozdělen; *vnder meinem Regiment* = „pod svým velením“ bez
  `{Regiment}`; „tentýž“ nahrazen podmětem „Proviantní pán“.
- **044r** – drobné zpřirození („ujednat s městy řád“, „dohodnout se s jejich majiteli“).
- **044v** – „(salvagvardie)“ → `{Saluaguarden}`; „pán války“ → „válečný pán {Herr des Kriegs}“; *weitter
  darüber vornemen* = „dovolovat si ještě víc“; přechod na 045r opraven (dřív „pak by se | člověk v tom velice
  zmeškal“ – negramatické) → „pak by se | tím mnoho zameškalo“.
- **045r** – výčet podunajských měst a mandátů rozdělen na 5 vět; *beuelchsleut* knížecí správy = „pověření
  úředníci“ (bez `{…}`, heslo *velitelé* nesedí); `{pflegern}` doplněno; robotní odstavec zjednodušen.
- **045v** – *Kastenpfleger* chybně „aby k němu byl přidělen nejen týž proviantmistr, nýbrž i správce“ → „aby tam
  nebyl jen tento proviantmistr, nýbrž aby mu byl přidělen i správce sýpky {Kastenpfleger}“; nové pozn. 1 a 3.
- **046r** – blok o střídání lodí (2400 znaků) rozdělen na 12 vět; *nach des nechsten Flecken Schiffman* =
  „počínaje lodníkem nejbližšího městečka“ (dříve volně „kromě lodníka v posledním městě“).
- **046v** – tabulka vzdáleností: místo vymyšleného „Vzdálenosti“ odpovídá svorce *Von* české „z“ (řádky
  v 2. pádě, „Ostřihomi přes Vyšehrad do Budína“); pozn. 2 (Mechausen) opravena – Mauthausen leží pod Lincem,
  tedy nepřichází v úvahu.
- **048r** – „kryta hlídkami a zálohami“ → „projížděna hlídkami a střežena“ (*verstreiffen vnd verhalten*).
- **048v / 049r** – `{Oberster}` přesunuto k prvnímu výskytu; přímá řeč „ty máš mít tolik, druhý máš mít tolik“ →
  „ty máš mít tolik, ty druhý tolik, ty třetí tolik“; *sein pflicht darauff thůn lassen* „jeho závazek na to
  dát složit“ → „dát mu na to | složit přísežný závazek {pflicht}“; *sein feld bestellen* = „zařídit tažení“.
- **049r** – `{Reutter Obersten}` (glosář: „nejvyšší velitel jízdy“) nahrazeno „plukovníkovi {Obersten} jízdy {Reutter}“.
- **049v** – popis dřevořezu zpřesněn podle obrázku: velitelská hůl držená před hrudí (ne „oběma rukama se
  opírá“), dlouhý meč v pochvě, ostruha s hvězdicí, náprsní řemen a podocasník.
- **050r** – *sein eigen Regiment vnd versehung* „vlastní pluk a správu“ → „vlastní řízení a zaopatření“;
  „podléhá zbrojmistru“ → „zbrojmistrům“ (*den Zeugmeistern*); „podléhá pod něj“ → „patří pod něj“.
- **050v** – *es keme anders das Geschütz… gegen den Freunden zustreichen* chybně „ledaže by dělo stálo uvnitř…“ →
  „jinak by děla uvnitř vozové hradby postřelovala směrem k vlastním“; pozn. 2 rozšířena (*geriegen*).
- **052r** – *Wagen mit schirmen* = „štítové vozy {Wagen mit schirmen}“ (heslo glosáře `stitovy-vuz`); nové
  pozn. 3 a 5, přečíslování.
- **052v** – pozn. 1 přeformulována (*Wagenmeister* zřejmě za *Wagenburgmeister*).
- **053r** – `{Artickels}` odstraněno (heslo *artikulní list*, zde jde o „článek“); věta o trestu jako podmínka.
- **053v** – „ti v posádce nebo v táboře“ → „nepřátelé v posádce nebo v ležení“; *sonst liegen sie nider* =
  „jinak je přepadnou“; věta o Turcích zpřirozena.

## Sporná místa k rozhodnutí

1. **043r** – *Dasselbig soll zu der zeit so mann Zůege ordnen würde / nicht gerechnet vnd geordnet werden.*
   CS: „Toto se má v době, kdy se budou tažení nařizovat, započítat a uspořádat[^1].“ Tisk má jasně *nicht*
   (sken 173); doslovný překlad („nemá být počítáno“) odporuje smyslu, proto překlad podle čtení *mit gerechnet*.
2. **042r** – *gespart vnd nit gefürt biß zu der not* – CS „šetřil a nevezl [k výdeji] až do nouze“; *gefürt*
   může být i „spotřebováno“. Ponecháno doslovněji.
3. **042v** – *biß zu dem Obersten in ein Regiment vnd Ordnung annemen vnnd schweren ließ* – „až k plukovníkovi“
   lze chápat časově (do předání plukovníkovi) i jako „až po plukovníka“ (všechny stupně). CS: „nechal jej až
   k plukovníkovi přísahat v jednom pluku a řádu“.
4. **050v** – *gegen den Freunden* (2×) – výklad „směrem k vlastním“ (při útoku zezadu se zlomy obracejí); pokud by
   šlo o záměnu za *Feinden*, je třeba upravit pozn. 2.
5. **046v** – *Mechausen* mezi Pasovem a Lincem neztotožněno (Neuhaus / Aschach / Ottensheim?).

## Návrhy do glosáře (needitováno)

| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| `nejvyssi-velitel-jizdy` | sjednotit s rozhodnutím: **plukovník nade vší jízdou** (nebo heslo zrušit a de přesunout k `plukovnik`) | Oberster vber die Reutter, Reutter Obersten, Reuter Oberster | velitele | nyní koliduje s pozn. hesla `plukovnik` a s rozhodnutím Oberst = plukovník |
| `clanek` | článek | Artickel, Artickels (ve smyslu odstavce řádu, „des Obersten 25. Artickels“) | pravo | z hesla `artikulni-list` vyjmout samostatné *Artickel/Artickels* |
| `valecny-pan` | válečný pán | doplnit *Herr des Kriegs* | velitele | 044v |
| `spravce-sypky` | správce sýpky | Kastenpfleger | zold | 045v |
| `spravce` | správce (úředník) | Pfleger, pflegern | osoby | zeměpanský správce úřadu (045r) |
| `salvagvardie` | ochranný list (salvagvardie) | Saluaguarden | pravo | ochranný glejt či vyvěšený erb chránící místo před drancováním (044v); poté zkrátit pozn. 1 na 044v |
| `velitele` | – | – | – | u *beuelchsleut* doplnit do pozn., že v civilním kontextu (045r) jde o pověřené úředníky |
| `hlaven` | – | *Rorn* | – | „Schützen mit Rorn“ (050v) = střelci s ručnicemi; zvážit přesun *Rorn* k `rucnice` |
| `achtel` | – | – | miry | pozn. „dělená na 8 měřic“ nesedí s 041v (korec = achtel = 144 lb ovsa, 12 měřic) – doplnit |
