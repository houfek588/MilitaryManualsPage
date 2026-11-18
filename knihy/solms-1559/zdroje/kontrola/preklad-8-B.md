# Překlad dávky 8-B – Solms 1559, konec Osmé knihy (skeny 600–616)

Datum: 2026-11-18. Zadání: `zdroje/ZADANI_PREKLAD_6_9.md`. Rozsah: **8-006v … 8-014v** (17 stran). Původně šlo o
skeny 601–616; podle upřesnění koordinátora jsem doplnil i 8-006v (sken 600), které dávka 8-A nepřeložila.
Sousední strany 8-006r (z dávky 8-A) a 9-erb-solms jsem jen četl.
Všechny strany mají `stav: prelozeno` a `overeno_clovekem: false`.
`python -I nastroje/over_strany.py knihy/solms-1559 8-006v … 8-014v --prisne` → **17 stran, 0 chyb, 0 varování**.

Každou stranu jsem porovnal se skenem BSB (IIIF, šířka 1600 px, sporná čísla jsem si zvětšil výřezem).
Text 8-006v až 8-008v je téměř doslova převzatý z Druhé knihy (kapitola o proviantním pánovi, listy
[[040r]]–[[042r]]). Terminologii a znění překladu jsem proto sladil s tamním revidovaným překladem
(vůl / kráva / tele / skopec / ovce, cent {Centner}, libra {pfundt}, korec {Schäffel}, měřice {Metzen}, achtel).

## Přehled stran
| Strana | Sken | Obsah | Poznámka |
|---|---|---|---|
| 8-006v | 600 | maso pro 500 osob (týden, měsíc) a 1000 osob (den, týden, měsíc) – 5 tabulek | nový odstavec (*Item*), bez pokračování |
| 8-007r | 601 | maso pro 5000 a 10 000 osob (den, týden), 5 tabulek | |
| 8-007v | 602 | maso pro 10 000 osob na měsíc, záměna dobytka, snížené dávky, ukořistěný dobytek | |
| 8-008r | 603 | nadpis *Nůn volgt die Füterung auff die Pferde* (úr. 3), výpočet ovsa (korec = 144 liber = 12 měřic) | |
| 8-008v | 604 | oves pro 10 000 koní, víno, proviantmistr a placení, volný trh, solení masa, závěr výpočtů | odkaz na [[032v]] |
| 8-009r | 605 | řád posádky: plukovníkova řeč k válečnému lidu (přirovnání ke Kristu a sv. Janovi) | |
| 8-009v | 606 | pokračování řeči; nadpis *Innhalt der Ordnung …* (úr. 3); zásoby 1.–3. | `pokracovani` |
| 8-010r | 607 | zásoby 3.–16., výzva k bohoslužbě, zákaz klení | `pokracovani` (slovo *Puluer* přesunuto celé z 606) |
| 8-010v | 608 | trestání rouhání, články 2–5 (proviant, opilství, nevěstky a manželky, polní kuchaři) | `pokracovani` (*erlangen*) |
| 8-011r | 609 | články 6–10 (komis, pečení, mlýny, rotmistři, stráže a výčepy) | věta pokračuje na 8-012r |
| 8-011v | 610 | celostránkový dřevořez, figury 20–25 | doplněn `popis` |
| 8-012r | 611 | pokračování článku 10; fig. 20 – křížový ježek, zátaras; autorova zkušenost mistra dělostřelectva | `pokracovani` přes obrazovou stranu |
| 8-012v | 612 | výroba ježků; fig. 21 – vlněné pytle; fig. 22 – vápenný soudek | `pokracovani` |
| 8-013r | 613 | vápenné soudky se žlabem a pomalým prachem (fig. 22 a 25) | `pokracovani`; *auß-weisen* přesunuto celé na 614 |
| 8-013v | 614 | fig. 23 – smolné věnce; fig. 24 – pálená koule s hrdlem | `pokracovani` |
| 8-014r | 615 | dokončení koule; kožená vědra; vrhací stroje; píce; prach | `pokracovani` |
| 8-014v | 616 | rozdělení prachu na stanoviště; *Ende des achten Bůchs.* | `pokracovani` |

## Výpočty zásob (tabulky)
- Rozpisy masa jsou `typ: tabulka` o třech sloupcích jako v tisku: levá varianta | spojka *Oder mag nemen.* (v prostředním,
  třetím řádku, kde ji má tisk vedle složené závorky) | pravá varianta. Pět řádků v `de` i v `cs`, čísla přesně podle skenu.
- Výpočty ovsa (8-008r–8-008v) má tisk jako samostatné odsazené odstavce s celými větami („Ein Woch gehn auff … thůn an
  gewicht …“), proto zůstávají jako bloky `odstavec` 1 : 1 podle sazby. Tabulka by porušila zrcadlové párování.
- Všechny tabulky jsem přepočítal podle vah z 8-006r (vůl 300, kráva 150, tele 36, skopec 30, ovce 20 liber).
  Tiskové chyby jsem ponechal a vysvětlil v poznámkách:
  - 8-006v: 1000 osob/týden, vlevo „40 Schaaff“ (má být 14);
  - 8-007r: „370 Centner“ (má být 350); „130 Hämel“ (má být 35); 5000/měsíc vlevo „360 Schaaff“ – **přesmyk za 306**
    (306 má Druhá kniha a teprve s tímto číslem vychází přesně 1500 centů); vpravo „20 Schaaff“ (chybí 1000 ovcí);
    10 000/týden vlevo „130 Schaaff“ (má být 140);
  - 8-007v: 10 000/měsíc vpravo 1315 telat, 280 skopců a 413 ovcí (opakování čísel z týdne); záměny „5 Kälber oder 6 schaaff“
    a „3 Hämel 5 schaaff“ váhově nesedí (Druhá kniha má „drei Hämel vnd drei Schaaff“);
  - 8-008r: „33 schäffel“ (má být 83); „1500 schäffel“ za měsíc pro 1000 koní (má být 2500 – Druhá kniha má správně);
    „1500 metzen“ za měsíc pro 5000 koní (má být 150 000).

## Ověřená čtení ze skenu (OCR → tisk)
- 601: všechna čísla v tabulkách (149/452/745/152/360 | 118/364/600/600/20; 413, 315, 59, 45) ověřena výřezem.
- 602: „1315 Kälber“, „oder 3 Hämel 5 schaaff / od|der“ (→ *odder*), „hie oben“ (OCR *hteoben*).
- 603: „gennt“ (bez tildy; ponecháno, vysvětleno v poznámce), iniciála **ES**.
- 604: „nit bezalen“ (OCR *mit*), „Prouiantmeister“ (OCR *Proutantmeister*), „Veltzug“ (tak tisk).
- 605: „vorm eingang vnd verflichtung“ (tisk *verflichtung*, ponecháno), „befastung“ (tisk, ponecháno), „mit den Harn“.
- 606: „Beschatzung“ (tisková chyba za *Besatzung*, poznámka), iniciála **ERstlich**, „nit gemůt“, „die für sie sind“.
- 607: „darressen“ (tisk *darꝛessen*; OCR *darzessen / daressen*), „Moltern“, dvakrát „Zum fünfften“ (poznámka), „sochem“ (tisk).
- 608: „die nit eigen Köche“ (OCR *mit*), „gebürentes“, „Droß“.
- 609: „gůng“ (tisk, patrně za *gnůg*; poznámka), „Befestuug/Schauffelu/Schuor/Fütternng“ – obrácená litera *n/u* sjednocena na
  *Befestung, Schauffeln, Schnor, Fütterung* (jde o sazečský převrácený typ, ne o jiné slovo).
- 611: „Letzen“ (OCR *Leken*), „löcken“, „Pfalbaumen“ (tilda), „Artoloreimeister“, „brach hat“ (tisk, ponecháno).
- 613: „Trachteten“ (tisk; poznámka – rakety), „lufft“ (poznámka), „Kalcktonnen“ (tilda).
- 614: „mit zweien Rören“ (tisk; dle obrázku a dalšího textu spíš *Oren*, poznámka).
- 615: „in den röschen Zeug“ (OCR *dēröschen*), „dön von Zeug“, „Instroment“ (tilda), „Wacken“.

## Sporná místa k rozhodnutí
1. **Creutzhaspel / Creutzhespel** (8-012r, 8-012v, obrázek 8-011v): DE *Creutzhäspeln vnd Pfalbaumen* – CS „křížový ježek,
   kolový trám“. Glosářové heslo `navijak` (naviják a klika) obsahuje tvar *creutz Hespel*, takže web tu nabídne nesprávný
   odkaz. Navrhuji *Creutzhaspel* z `navijak` vyjmout a založit samostatné heslo (viz níže). Možnou alternativou je „španělský jezdec“,
   ten název je ale až ze 17. století.
2. **Garkoch** (8-010v, 8-011r): glosář → „polní kuchař“. V posádce města je přívlastek „polní“ trochu nepřesný (jde o kuchaře, který
   za úplatu vaří z komisních dávek). Ponechal jsem glosář, ke zvážení je „výdejní kuchař“.
3. **Regiment** v 8-009v a 8-010v znamená „řízení, řád“ (*ein Regiment vnd Ordnung*), ne „pluk“. Přeložil jsem to jako „řízení {Regiment}“ /
   „řád {Regiment}“. Odkaz na glosářové heslo `pluk` tu nesedí.
4. **Wolnsack** (8-012v): tisk střídá *Wolnsack – Wolseck – Wolsteck*; všude „vlněný pytel“, poslední tvar ponechán.
5. **Odkaz na vyobrazení vrhacího stroje** (8-014r: *hab ich hie … ein Abriß vnd Figur gestalt*) – v Osmé knize žádné takové
   vyobrazení není (po skenu 616 následuje erb 9. knihy). Je to uvedeno v poznámce.
6. **Sjednocení s dávkou 8-A** (8-006r): 8-A má spojku *Oder mag nemen.* v 1. řádku tabulky a píše *Küe*; já ji mám v prostředním
   řádku (jako tisk a Druhá kniha 039v–040v) a píšu *Kůe* (u s nadepsaným e jako v Druhé knize). Doporučuji sjednotit podle
   tisku. Strany 8-A jsem needitoval.

## Návrhy do glosáře
| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| krizovy-jezek | křížový ježek | Creutzhaspel, Creutzhäspel, Creutzhespel, Creutzhespeln, Creutzhäspeln | opevneni | trám s křížem prostrčenými zahrocenými kolíky; zátaras průlomů a příkopů (pozdější „španělský jezdec“); vyjmout *creutz Hespel* z hesla `navijak` |
| kolovy-tram | kolový trám | Pfalbaum, Pfalbaumen, pfalbäum | opevneni | synonymum křížového ježka |
| zataras | zátaras; tarasit | Dareß, Darreß, darressen, verdarressen | opevneni | narychlo postavená zábrana v průlomu (dřevo, hlína) |
| vlneny-pytel | vlněný pytel | Wolnsack, Wolseck, Wolsteck | opevneni | pytel s vlnou, senem či slámou zavěšený před zeď proti dělostřelbě |
| pricna-zed | příčná zeď | Zwergmauer, Zwergmauren, Zwergmaurn | opevneni | zeď vedená napříč (suchým) příkopem |
| slepy-prikop | slepý příkop | blinde Gräben, blinden Graben, verborgen Gräben | opevneni | skrytý příkop s nástrahami a zápalnými prostředky |
| parkan | parkán | Zwinger | opevneni | prostor mezi hradbami |
| trhaci-soudek | trhací soudek | Sprengton, Sprengfaß, Kalcktonnen | delostrelectvo | soudek s prachem a vápnem (dým) nebo kamením |
| trhaci-koule | trhací koule | Sprengkugel, Sprengkugeln | delostrelectvo | srov. pálená hliněná koule, 8-013v |
| zlab | žlab | Kendel | delostrelectvo | dřevěný žlab s pomalým prachem vedoucí oheň k soudkům |
| mistr-delostrelectva | mistr dělostřelectva | Artoloreimeister | velitele | Solmsova vlastní funkce (8-012r) |
| prachovy-mlyn | prachový mlýn | Puluermöln | delostrelectvo | |
| zentourovy-mlyn | žentourový mlýn | Roßmöln, Roßmöllen, Roß Möllen | zold | mlýn poháněný koňmi; ruční mlýn = Handtmöln |
| palec | palec | Zoll, Zöl | miry | délková míra (8-013v) |
| metadlo | metadlo | Schleudern | zbrane | vrhací stroj; *Schlengern* → prak (`prak`) |
| stanoviste (doplnit tvar) | stanoviště | Letzen | opevneni | heslo `letze` existuje, tvar je pokryt |
