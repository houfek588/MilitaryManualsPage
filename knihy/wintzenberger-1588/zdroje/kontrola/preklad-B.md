# Překlad – dávka B (Wintzenberger 1588)

Strany: `012r`–`014r` (skeny 27–31) a `015v`–`022v` (skeny 34–48), celkem 20 stran, všechny `stav: prelozeno`,
`overeno_clovekem: false`. Skeny 32–33 (`014v`, `015r`) do dávky nepatří. Každá strana byla přepsána podle skenu
(BSB bsb00032546, 1600 px, sporná místa výřezem); OCR posloužilo jen jako předloha.
`over_strany.py … --prisne`: 0 chyb, 3 varování. Všechna tři jsou plané: „fein ordentlich“ / „wie auch fein angezeigt“
je správné slovo *fein*, a krátký blok „haben / dardurch …“ na `018r` má přirozeně nepoměr délek.

## Obsah
- **012r–013v** – dokončení rad k ustanovení nejvyššího hejtmana (vrchního velitele): úředníky a podřízené hejtmany
  přijímá sám velitel, ne panovník; vybírat zkušené muže bez ohledu na stav. Za 4.: prvního lid brát k přísaze
  na artikulní list po malých houfech. Pán má v soudu dosadit 6–8 vlastních placených přísedících. Rychtář má mít drabanty
  a soudního písaře, soudit obden až jednou týdně, s artikulním listem na stole. Odkaz na druhý díl (profous, 42 artikulů).
- **014r** – kapitola „Ordnung eines Zugs“: velikost vojska (10 000 pěších, 1 500 koní) a pořadí pochodu od předvojové
  korouhve po zadní voj. Věta končí neúplná (kustos „wie“), pokračování v exempláři chybí. Je to vyznačeno v poznámce 3.
- **015v–016v** – výčet výzbroje a náčiní: hákovnice, licí pánve, olovo, zvedací kozy, mosty, náhradní kola a nápravy,
  útočné žebříky, řemeslníci, lana, hřeby, nářadí, zbraně, osvětlení. Dále pořadí těžkých děl v pochodu.
  Poznámka 1 na `015v` uvádí, že text navazuje na chybějící list.
- **017r–018v** – rady zbrojmistrovi při obléhání: šancovní koše, řetězy k odvlečení děl, nestřílet zbytečně, správné
  koule a prach, kožená vědra, výsada dělostřelectva. Na `018v` začíná kapitola „Eine Schlachtordnung …“:
  široký šik (třikrát širší než hluboký) proti čtvercovému.
- **019r–021r** – pokračování o širokém šiku, dřevořez Maxmiliána I., „běžci“ (Leuffer, 300 mužů proti
  nepřátelským dělům), „přikrytý pokrm“ (500 mužů do boku). Dále ztracený houf o 3 000 mužích, útoky rychle za sebou,
  pochodové pořadí šiku a utajení lsti.
- **021r–022v** – kapitola „Ein vnterricht Ordnung des Reisigen zeugs“ (1 500 koní): dřevořez jezdecké srážky, tři houfy
  (600/600/300), korouhve po 200 koních a velitel útočící až naposled. Dále výhody mnoha malých houfů a varování
  před manévrováním „o slunce a vítr“.

## Návaznost na sousední dávky (důležité)
- `012r` začíná slovem **„Zeugmeister“** – v tisku je rozdělené přes hranici stran (*Zeug-|meister*, kustos „meister/“).
  Podle pravidel patří celé na `012r`, takže strana `011v` (dávka A) má končit „… es sey Reuter oder Fusknecht /“.
  Ověřte to při revizi dávky A.
- `022v` končí „… das die“; slovo *ge-|schrey* patří celé na `023r` („geschrey vnd vortheil …“).
- Další dělená slova na hranicích stran uvnitř dávky (podle pravidla): `017r`/`017v` *Büchssenmeister*, `017v`/`018r` *haben*,
  `019v`/`020r` *Schlachtordnung*, `020v`/`021r` *angehangen* (ten začíná až na `021r`).

## Nejistá čtení ověřená ve skenu
- `020v` **„800. Knechte“** (OCR „soo“) – výřez ukazuje 800. Odpovídá to součtu 300 běžců a 500 mužů „přikrytého pokrmu“.
- `017r` **„den Dros“** – ve skenu je skutečně D (dobová varianta *Tross*), ne zaměněné H. Ponecháno.
- V celé dávce jde *Hauptman, Herr, Hals* atd. o glyf H, který vypadá jako D. OCR ho čte „Dauptman, Derr, Dals“.
  Všude opraveno na H. Stejně tak *R* (OCR „X/K“: *Ros, Reuter, Regiment*) a *K* (OCR „B“: *Krieg, König*).
- Tiskové chyby ponechané v `de` a vysvětlené v poznámce: `013r` *ordnug*, `021v` *wirp* (= wird),
  `019v` *zustreitenden* (patrně za *zustrewten*), `016r` *gestellet* (patrně *gestählet*), `015v` chybějící *haben*.
- `016v` – syntakticky neúplná věta „Jhr müst diesen Zeug … so müst jhr bey dem Geschütz …“; překlad doplňuje „[mít takto]“.

## Sporná místa
| strana | DE | CS | proč |
|---|---|---|---|
| 012r/021v | der Oberste / oberster Hauptman / Oberste Feldhauptman / FeldOberste | vrchní velitel / nejvyšší hejtman / nejvyšší polní hejtman / polní plukovník | Všechny výrazy označují jednoho vrchního velitele. Ponechány glosářové ekvivalenty, totožnost osoby vysvětluje poznámka. *Oberste* bez dalšího = „vrchní velitel“ (podle poznámky v kniha.yaml). |
| 015v, 016r, 016v | Fürschlege | tažné nářadí | Význam nejistý: část postroje nebo předku, „da die Ros anziehen“. |
| 016r, 016v | Wogen / Wagen (zu den Pferden, wo eine zubrech) | vahadla | Podle ženského rodu a kontextu jde o *Wage* = vahadlo, ne o vůz. |
| 015v | Legeisen | ložná železa | Nejasné. |
| 016r | 100. Brücken (mezi lopatami a motykami) | mostnice | Nejasné, snad desky na přechody nebo tisková chyba. |
| 016v | Fuseysen / darauff man gehe | železné nášlapky | Snad mačky; „andere Fuseysen“ snad nášlapné bodce. |
| 019r | ehe mehr Leut zu der arbeit kommen können / je leichter es zugehet | … dřív, než se k té práci může dostat víc lidí – tím snáze to jde | Anakolut, smysl odhadnutý. |
| 019v | verdeckt Essen | přikrytý pokrm | Metafora pro skrytou lest. Doslovně, s poznámkou. |
| 020v | nach dem ein Fenlein vorziehen | táhnout za jedním praporcem | Možné i „nachdem“. |
| 021v | das einer des andern im treffen felen kan | aby se jeden ve střetnutí obešel bez druhého | Nejisté. |
| 020r | 6000. vnd 300. Knechte | 6000 a 300 knechtů | Autor nepočítá 500 mužů „přikrytého pokrmu“. Na `020v` však uvádí 800 připojených. Ponecháno. |

## Návrhy do glosáře
| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| bezci | běžci | Leuffer, verlorne Leuffer | jednotky | Lehký oddíl (zčásti střelců), který těsně před srážkou rozptýleně vyběhne na nepřátelská děla a vyžene puškaře. U Wintzenbergera 300 mužů za hlavním houfem a 200 za ztraceným. |
| liny-houf | líný houf | fauler hauffen | sluzba | Pomalý, neozbrojený doprovod vojska (nemocní, ženy, děti), táhne s trénem. |
| hlavni-houf | hlavní houf | gewaltiger hauffen, gewaltige hauffen zu Fus | jednotky | Hlavní voj pěchoty (Gewalthaufen), na rozdíl od ztraceného houfu. Lze přidat do hesla `cely-houf` nebo `sik`. |
| tezka-dela | těžká děla | gewaltige Geschütz | delostrelectvo | Obléhací a hlavní děla na rozdíl od polních (Feldgeschütz). |
| polni-dela | polní děla | Feldgeschütz, Feltgeschos, Feldtgeschütz | delostrelectvo | Lehčí děla doprovázející předvoj a šik. |
| sirsi-sik | široký šik | breite Ordnung | jednotky | Šik třikrát širší než hluboký, který Wintzenberger doporučuje místo čtvercového (gevierdte Ordnung). |
| sancovni-kos (doplnit de) | šancovní koš | Schantzkörbe | opevneni | Doplnit tvar *Schantzkörbe*. |
| hakovnice (doplnit de) | hákovnice | Hacken Büchssen, Hacken | zbrane | Doplnit tvary. |
| zakolnik | zákolník | Lönnegel | delostrelectvo | Kolík zastrčený do konce nápravy, aby kolo nespadlo. |
| tazne-naradi | tažné nářadí | Fürschlege | delostrelectvo | Nejisté: část postroje či předku vozu, za niž táhnou koně. |
| vahadlo (doplnit de) | vahadlo | Wogen, Wagen (zu den Pferden) | delostrelectvo | Doplnit tvary k heslu `vahadlo`. |
| arbeit | práce (boj) | arbeit, Erbeit | sluzba | Dobový výraz pro boj, srážku. |
| freyheit (doplnit de) | výsada | Keyserliche Freyheit | pravo | Doplnit tvar k heslu `vysada`. |
| klafter (doplnit de) | sáh | Klafftern, Klaffter | miry | Doplnit tvary k heslu `sah`. |

## Osoby a místa pro rejstřík
- Maxmilián I. (*Keyser Maximilianus Primus*), `019r` – text i dřevořez.
- Další osoby a místa se v dávce nevyskytují.

## Dřevořezy (bloky `obrazek`, soubory doplní správce)
- `019r` – `drevorez-41.jpg`: portrét Maxmiliána I. v ozdobném rámu.
- `021r` – `drevorez-45.jpg`: srážka jízdy.
