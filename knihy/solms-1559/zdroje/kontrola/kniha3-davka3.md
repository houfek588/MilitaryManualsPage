# Kontrola a překlad – `knihy/solms-1559`, Třetí kniha, Dávka 3 (`3-021r`–`3-031v`)

Zpracováno všech **22 stran** Třetí knihy (`3-021r`–`3-031v`, skeny `293`–`314`): závěr 24 článků zkoušení puškařů, rozsáhlý úvod a 1. kapitola popisu zbrojnice s devíti druhy průlomových a polních děl, rozpočet odlití děl (včetně zakázky Gregora Löfflera z r. 1542), štítové a útočné vozy vozové hradby a úvod do nauky o moždířích a zápalných/výbušných kulích. Všem 22 stranám byl nastaven `stav: zkontrolovano` a ponecháno `overeno_clovekem: false`.

Ověření skriptem `python -I nastroje/over_strany.py knihy/solms-1559 3-021r 3-021v 3-022r 3-022v 3-023r 3-023v 3-024r 3-024v 3-025r 3-025v 3-026r 3-026v 3-027r 3-027v 3-028r 3-028v 3-029r 3-029v 3-030r 3-030v 3-031r 3-031v --prisne`:
- **22 stran, 0 chyb, 1 varování** (`3-027v`, blok 2: falešně pozitivní varování na autentické příslovce *fein* ve vazbě *geht als fein lustig zu*, ověřeno ve skenu `s306.jpg`).

---

## 1. Přehled změn po stranách

| Strana | List (tisk) | Sken | Bloky | Pozn. | Hlavní úpravy podle skenů a překlad |
|---|---|---:|---:|---:|---|
| `3-021r` | 21 (`21`, OCR `28`) | 293 | 3 | 2 | `pokracovani: true`, rozdělení 3 odstavců, opravy OCR (`wann`, `stossen`, `puluer so`, `ansetz kolben`, `zu sotern`, `fůgsamer`→`wüsch`, `vbel`, `wirt`, `Herr`, `schatz`, `vben`), odstraněno záhlaví, folio a signatura `Dd iiij`. |
| `3-021v` | 21v | 294 | 8 | 2 | Hlavní nadpis `uroven: 2` (*Beschreibung / wie eines Stathafftigen Fürsten…*), doplněna iniciála `ANfangs`, 4sloupcová tabulka přehledu děl (`7×4`), opravy OCR (`Herrn`, `Geschütz`, `Kriegßrüstungen`, `Notschlangen`, `stück`, `eisens`, `vorrat`), pozn. `[^1]` (*ein Brechgeschütz*) a `[^2]` (*Perchgeschütz*). |
| `3-022r` | 22 (`2` místo `22`) | 295 | 9 | 2 | Nadpis `uroven: 2` (*Volgts erst Capitel…*), doplněna iniciála `ITem`, opravy OCR (`zuuerrichten` místo `zuuerachten`, `aufflauffen` místo `aufflauffend`, `Herr`, `Kriegßrüstung`, `notturfft`), odstraněno `00085168`, chybné folio `2` a kustod `vil`, vydělena rubrika `Scharfermetzen 2.` do `[^1]`. |
| `3-022v` | 22v | 296 | 7 | 3 | `pokracovani: true`, opravy OCR (`zusetzen` místo `zusehen`, `vffzuladen`, `mit füret /` místo `?`, `Gefäß odder Lade`, opraveno přehozené pořadí řádků u `Wagen 7.` a `Zugpferdt 28.`), odstraněn kustod `welcher`, poznámky k zaokrouhlení koní (57), *drei teil* a *Zug* = kladkostroj. |
| `3-023r` | 23 | 297 | 13 | 3 | `pokracovani: true`, iniciála `VIer`, opravy OCR (`schleiniger`, `plechne Büchsen`, `Nachtigaln`, `wigt`), odstraněn kustod `Dar=`, vydělena rubrika `Nachtigal 4.` (`[^3]`), rozpis 190 vs. 178 koní (`[^2]`) a *einn Monat / etc.* (`[^1]`). |
| `3-023v` | 23v | 298 | 17 | 1 | Opravy OCR (`wie der`, `Scharpffenmetzen`, `auff laden`, `zusetzen`, doplněny vypadlé číslice `Wägen 11.` a `Wagen 11.`, srovnáno pořadí řádků u `Zugpferdt 44.`, `Mehrgemelte`, `notturfft`, `Wägen 29.`), odstraněn kustod `Vnd`. |
| `3-024r` | 24 | 299 | 22 | 5 | Tabulka souhrnu (`1×6`), iniciály `DEren` (2×), opravy OCR (`all einzusetzen`, srovnáno pořadí řádků u `Züg 3. / Ladschauffel 4. / Plechenbüchsen 12.`, `Notschlangen`, `kloben`), odstraněna signatura `Ee`, vyděleny rubriky `Notschlangen 4.` a `Cartaunen 8.`, pozn. k chybám počtů (`93`, `145` a vypadlým vozům na prach). |
| `3-024v` | 24v | 300 | 24 | 4 | Tabulka souhrnu (`1×6`), opravy OCR (`sampt`, `eim Roß drithalben`, `Sorten` místo `Corten`, `gezeug`), odstraněn kustod `Zug=`, poznámky k *war*, chybám `8 wagen`→`32` koní, `25` vs. `35` vozů a `104` vs. `85/95` vozů. |
| `3-025r` | 25 | 301 | 8 | 3 | Tabulka souhrnu (`1×8`), nadpis `uroven: 3` (*Hernach volgt das Feldgeschütz.*), iniciála `VNd`, opravy OCR (`Züg 11.`, `12. pfundt.`, `müssen`, `saumbseyl im`, `wagen 3.`), odstraněna signatura `Ee ij` a chybný kustod `gen 6.`, rubrika `Feldtschlangen 6.` (`[^2]`), odchylka koní `915` vs. `879` (`[^1]`). |
| `3-025v` | 25v | 302 | 18 | 3 | Dvě tabulky (`3×4`), iniciála `DEr`, opravy OCR (`pock`, `schweren Geschütz`, `zügen`, `am gewicht`, `12. Roß` místo `124`, `truhen`, `32.` místo `324`, `3.` místo `38`, `8` místo `&`), odstraněn kustod `Der`, rubrika `Halb Cartaunen 8.`, pozn. k `12` koním a chybě `20.` místo `200.` centů. |
| `3-026r` | 26 (`26`, OCR `86`) | 303 | 17 | 3 | Tabulka (`3×4`), iniciály `DEren` a `SO`, opravy OCR (`an der schwere`, `Ferner` místo `Fewer`, `zugehör`, `2. pfundt`), přesunuto rozdělené `an-dere` na `3-026v`, odstraněna signatura `Ee iij`, rubriky `Halbschlangen 10` a `Viertheil schlangen 10`, pozn. k chybě `133` vs. `333` koulí. |
| `3-026v` | 26v | 304 | 17 | 2 | `pokracovani: true` s připojeným `andere`, dvě tabulky (`2×6`), iniciála `DEr`, opravy OCR (`faß` místo `faz`, `Demnach`, `Wagen`, `an gewicht`, `3.` místo `30` dvakrát u vozů s koulemi a prachem, `Plechenbüchsen`), přesunuto `schwei-ben` na `3-027r`, rubrika `Falconetlin 20.`. |
| `3-027r` | 27 | 305 | 11 | 5 | `pokracovani: true` s připojeným `schweiben`, dvě tabulky (`2×6`), opravy OCR (`Kugeln` místo `Sugeln`, `jre zugehörige`, `Ferner`, `einem`, `noch schwerer`, `vnkusten`), odstraněno `00085160` a signatura `Ee iiij`, pozn. k *hölzen schweiben* a odchylkám `1800`→`1008`, `479`→`515`, `40`→`82`, `130`→`136`. |
| `3-027v` | 27v | 306 | 5 | 2 | `pokracovani: true`, iniciála `SO`, opravy OCR (`behender`, `schöß`, `erwigt`, `lüstigem`, `můß`, `vnderweilen`), odstraněn kustod `lassen`, ponechána tisková znění *stonst* a *vortheilt* (`[^1]`), rozbor poměru mědi a cínu 9 : 1 (`[^2]`). |
| `3-028r` | 28 | 307 | 15 | 4 | `pokracovani: true`, nadpis `uroven: 3` (*Hernach volgen halbe Falconetlein…*), iniciála `GVter`, opravy OCR (`pfenning`, `nützlichsten`, `26. Züg.` místo `1. ... 72. Züg.`, `höltzen`, `Mödel`, `scheiben`, `beileufftigem`, `handror`), rozbor Löfflerovy zakázky r. 1542 (`[^1]`). |
| `3-028v` | 28v | 308 | 14 | 3 | Opravy OCR (`Gůter`, `beschützung`, `sambt`, `schießlöcher`, `150.`, `mödel`, `noch` místo `nach`), odstraněn kustod `genom` (`mimesize genom .`), ponecháno tiskové *Zupferdt* (`[^2]`), pozn. k zadovkám (`[^1]`) a útočným vozům (`[^3]`). |
| `3-029r` | 29 | 309 | 7 | 1 | `pokracovani: true`, doplněna velká zdobná iniciála `DIeweil`, opravy OCR (`dise`, `stürm`, `kleinn`, `zusetzen`, `vorrat`, `Herrn` místo `Hermes`, `einn tag`, `bäw`), odstraněno `00085168` a kustod `Damit`, pozn. k vazbě *mit dem grossen Geschütz*. |
| `3-029v` | 29v | 310 | 6 | 1 | Opravy OCR (`kosten`, `erkürtzen /`, `Scharpffmetzen`, `ist` místo `yt`, `schantz`, `Wann nun`, `Morser`), přesunuto rozdělené `schies-sen` na `3-030r`, odstraněn kustod `sen`, pozn. k *nit an lange Leger*. |
| `3-030r` | 30 | 311 | 3 | 2 | `pokracovani: true` s připojeným `schiessen`, opravy OCR (`Prouiant`, `Möcht einer` místo `Nicht einer`, `Letzen` místo `Legen`, `mein Schantzen`, `12. vhren` místo `ohren`, `nit auff hörn` místo `mit`), odstraněna signatura `Ff` a kustod `also`. |
| `3-030v` | 30v | 312 | 3 | 2 | `pokracovani: true`, nadpis `uroven: 3` (*Vnderricht der mörser…*), zdobná iniciála `DIeweil`, opravy OCR (`kugeln /`, `nit anders`, `holtz`, `dann es`, `erfordert`, `so ferr`, `nit höher`, `das böß`, `das gůt`), odstraněn kustod `aber`, pozn. k *Vergleichung* a *Kern*. |
| `3-031r` | 31 (`32` místo `31`) | 313 | 3 | 3 | `pokracovani: true`, opravy OCR (`bogenschoß`, `falsch /`, `Mörser`, `mit den proben`, `keinn`, `nit meister` místo `mitmeister`, `stůl`, `stůllen` místo `stillen`, `dann` místo `dat`), odstraněna signatura `Ff ij` (`Sitf`) a kustod `Wie`, pozn. k chybnému foliu `32`. |
| `3-031v` | 31v | 314 | 3 | 3 | Nadpis `uroven: 3` (*Wie aber ich vermein / das die mörser…*), iniciála `ZVmersten`, opravy OCR (`steine`, `Küe`, `heut`, `nichts`, `also ferr hol`, `nit angehen` místo `mit angehen`, `in der eil` místo `in der til`, `gelegt /`), odstraněn kustod `teil`, pozn. k přechodu na `3-032r`. |

---

## 2. Významnější opravy OCR ověřené ze skenů (`s293.jpg`–`s314.jpg`) a švy dávky

### A. Ozdobné iniciály kapitol a oddílů
- `3-021v` (`s294.jpg`): `Nfangs` → **`ANfangs`** (velká dřevořezová iniciála `A`).
- `3-022r` (`s295.jpg`): `Tem` → **`ITem`** (velká dřevořezová iniciála `I`).
- `3-023r` (`s297.jpg`): `Vter` → **`VIer`** (dvouřádková lombardská iniciála `V`).
- `3-024r` (`s299.jpg`): `DEren` (ve druhém případě OCR vynechalo `D`: `Eren` → **`DEren`**).
- `3-025r` (`s301.jpg`): `Nd` → **`VNd`** (dvouřádková iniciála `V`).
- `3-025v` (`s302.jpg`): `DEr` (ověřeno podle skenu).
- `3-026r` (`s303.jpg`): `Eren` → **`DEren`**; před dalším oddílem OCR zcela vynechalo **`SO`** (`soll nun` → **`SO soll nun`**).
- `3-026v` (`s304.jpg`): `Er stück` → **`DEr stück`**.
- `3-028r` (`s307.jpg`): `Vter Bter` → **`GVter`**.
- `3-029r` (`s309.jpg`): `Jeweil` → **`DIeweil`** (šestiřádková dřevořezová iniciála `D`).
- `3-030v` (`s312.jpg`): `Jeweil` → **`DIeweil`** (šestiřádková dřevořezová iniciála `D`).
- `3-031v` (`s314.jpg`): `ZVmersten` (ověřeno podle skenu).

### B. Zásadní opravy smyslu a čísel v BSB OCR
- **`3-021r` (`s293.jpg`)**: číslo listu `28` → **`21`**; `wüsch` místo chybného `wusch`; `gůtem`, `vbel`, `wirt`, `Herr`.
- **`3-021v` (`s294.jpg`)**: `Kriegsfristungen` → **`Kriegßrüstungen`**; `Rotſchlangen` → **`Notschlangen`**; `stick 64` / `stück 84` → **`stück 6.`** / **`stück 8.`** (OCR četlo tečku jako `4`); `ersens` → `eisens`.
- **`3-022r` (`s295.jpg`)**: `zuuerachten` („pohrdat“) → **`zuuerrichten`** („vykonat“); `aufflauffend` → **`aufflauffen`**; `Kriegsprüftung` → **`Kriegßrüstung`**; `Herꝛ` → `Herr`; ze středu odstavce odstraněny přimíchané zlomky okrajové rubriky `Scharfermetzen 2.` (`cha` / `2.`).
- **`3-022v` (`s296.jpg`)**: `zusehen` („vidět“) → **`zusetzen`** („zapřáhnout“); `mit füret ?` → **`mit füret /`**; `Gefäfsfodder Lade` → `Gefäß odder Lade`; srovnáno pořadí řádků `Wagen 7.` a `Zugpferdt 28.` na konci odstavců.
- **`3-023r` (`s297.jpg`)**: `fågsamer` → **`fůgsamer`**; `blechn e` → `plechne`; ze závěru odstraněny zlomky marginálie `Nachtigal 4.` (`lach`, `sigal`).
- **`3-023v` (`s298.jpg`)**: `Wågens` → **`Wägen 11.`** a `Wagen` → **`Wagen 11.`** (číslovka `11.` vypadla v OCR dvakrát!); srovnáno pořadí `Vnd für derselben einen zusetzen 4. Roß / thůt Zugpferdt 44.`.
- **`3-024r` (`s299.jpg`)**: `alleinzuseken` → **`all einzusetzen`**; `Mo / frer` → `jrer`; `loben` → **`kloben`**; `Notschlagen` → `Notschlangen`; odstraněny přimíchané zlomky marginálií `schlan / gen 4.` a `Car / taune / 8`.
- **`3-024v` (`s300.jpg`)**: `Corten` → **`Sorten`**; `Bezeug` → **`gezeug`**; `sam tanderer` → `sampt anderer`; `pren` → `jren`.
- **`3-025r` (`s301.jpg`)**: `Zug 11.` → `Züg 11.`; `Feldgefchug` → `Feldgeschütz`; odstraněny zlomky marginálie `Felde` / `leblan`; `saumbseyl um` → `saumbseyl im`.
- **`3-025v` (`s302.jpg`)**: `ange / wicht` → **`am gewicht`**; `124` → **`12.`**; `truyen` → **`truhen`**; `324` → **`32.`**; `Wagen 38` → **`Wagen 3.`**; `Ladschauffel &` → **`Ladschauffel 8`**; odstraněny zlomky marginálie `Halb / Cars / taune`.
- **`3-026r` (`s303.jpg`)**: číslo listu `86` → **`26`**; `Fewer` („oheň“) → **`Ferner`** („dále“); `zugehir` → `zugehör`; `cites` → `eines`; odstraněny zlomky marginálií `Halb / blan` a `vieres / thail` / `schlan / gen 10`.
- **`3-026v` (`s304.jpg`)**: `faz` → **`faß`**; `Dennach` → **`Demnach`**; `Bagen` → `Wagen`; **`Zugpferdt 30`** (2×) → **`Zugpferdt 3.`** (OCR četlo tečku za trojkou jako `0`!).
- **`3-027r` (`s305.jpg`)**: `Sugeln` → **`Kugeln`**; `fre zugehörig :` → **`jre zugehörige`**; `Ferier` → `Ferner`; `nach` → **`noch`**; `tft nie` → `ist nit`.
- **`3-027v` (`s306.jpg`)**: `liftigem` → **`lüstigem`**; `muff` → `můß`; `be / Hender` → `behender`.
- **`3-028r` (`s307.jpg`)**: **`1. Der zugeinen ... thun die 72. Züg .`** → **`Der züg einen ... thůn die 26. Züg.`** (zásadní oprava počtu kladkostrojů podle skenu i součtu z `3-027r`!); `pfēning` → `pfenning`; `hölken` → `höltzen`; `Model` → `Mödel`.
- **`3-028v` (`s308.jpg`)**: `1504` → **`150.`**; `fchießlich/er` → `schießlöcher`; `nach 25.` → **`noch 25.`**; odstraněno `mimesize genom .` (chybný kustod `genom`).
- **`3-029r` (`s309.jpg`)**: `Hermes` → **`Herrn`**; `vorzat` → `vorrat`; `Båw` → `Bäw`/`bäw`.
- **`3-029v` (`s310.jpg`)**: `Scharpff/megen` → `Scharpffmetzen`; `yt` → **`ist`**; `schant` → `schantz`; `erkürken )` → `erkürtzen /`.
- **`3-030r` (`s311.jpg`)**: **`Nicht einer sagen`** → **`Möcht einer sagen`** (obrácený smysl!); **`Legen`** → **`Letzen`** („stanoviště“); **`ohren`** („uši“) → **`vhren`** („hodin“); **`mit auff hörn`** → **`nit auff hörn`**; `meim` → `mein`.
- **`3-030v` (`s312.jpg`)**: `mit anders` → **`nit anders`**; **`mit höher`** → **`nit höher`**; `höß` → `böß`; `so fer ?` → **`so ferr`**.
- **`3-031r` (`s313.jpg`)**: **`mitmeister`** → **`nit meister`**; **`stillen`** → **`stůllen`** („dřevěné stolice moždířů“); `nut` → **`mit`**; `dat` → **`dann`**; odstraněno `Sitf` (signatura `Ff ij`).
- **`3-031v` (`s314.jpg`)**: **`mit angehen`** → **`nit angehen`** (obrácený smysl!); **`in der til`** → **`in der eil`** („spěšně“); `Kite` → `Küe`; `mchts` → `nichts`.

### C. Švy na okrajích dávky a uvnitř dávky
- **Začátek dávky (`3-020v` → `3-021r`)**: rub `3-020v` (`s292.jpg`) končí neuzavřenou větou a celým slovem `wie` (kustod `ein`). První blok `3-021r` má nastaveno `pokracovani: true` a začíná `ein meelsack /...`.
- **Vnitřní rozdělená slova přes přelom stran**:
  - `3-026r` → `3-026v`: `an=` | `dere` → celé `andere` přesunuto na začátek `3-026v` (`pokracovani: true`).
  - `3-026v` → `3-027r`: `schwei=` | `ben` → celé `schweiben` přesunuto na začátek `3-027r` (`pokracovani: true`).
- **Chybný kustod uvnitř dávky (`3-025r`)**: na dolním okraji `s301.jpg` je pod sazbou chybně vytištěn kustod `gen 6.` (z marginálie *Feldtschlangen 6.*), ač rub `3-025v` začíná slovem `Doch`. Z `de` odstraněn a vysvětlen v poznámce `[^3]`.
- **Konec dávky (`3-031v` → `3-032r`)**: `3-031v` (`s314.jpg`) končí neuzavřenou větou `...so deckt dieselbig erdt die ander helfft / nemlich das halb` (pod sazbou kustod `teil`; nejde o rozdělené slovo, tisk píše `das halb | teil` bez rozdělovníku). **Pro další dávku (`3-032r`)**: první odstavec (`teil in das Erdrich gesenckt / vnd das halb theil außgeworffen…`) je nutno označit `pokracovani: true` (český text plynule naváže na `…totiž poloviční` slovem `díl zapuštěný do země…`).

---

## 3. Sporná místa DE + CS, tiskové chyby a početní kontrola

### A. Chybné foliace a autentické tiskové tvary ponechané v `de`
- **`3-022r` (`s295.jpg`)**: v záhlaví tisku je vytištěno číslo listu `2` namísto `22`.
- **`3-031r` (`s313.jpg`)**: v záhlaví tisku je chybně vytištěno číslo listu `32` namísto `31` (totéž číslo `32` pak nese i `3-032r`).
- **Tiskové tvary ponechané v `de`**:
  - `3-021r`: `zu sotern`, `gůtem` (za *gůten*), `alles stück` (za *alle stück*).
  - `3-021v`: `vnd ein Brechgeschütz` (za *im Brechgeschütz*), `Perchgeschütz` (za *Prechgeschütz*).
  - `3-022r`: `Augpurgischs` (bez *-s-* v *Augspurg*), `gehalten werden.` (bez *sollen*).
  - `3-024r`: `Blechenbüchen` (vypadlé *-s-*).
  - `3-024v`: `sein besonder war / gefäß vnd fuer` (snad *lär gefäß*, *wagen* či *par*).
  - `3-025r`: `vnd zweien achsen` (místo *vff zweien achsen*).
  - `3-026v` / `3-027r`: `hölzen schweiben` (nářeční či tiskařská podoba *Scheiben*, případně záměna za *Schwellen*).
  - `3-027r`: `Augspurgischs gewichs` (bez *-t-*).
  - `3-027v`: `stonst` (za *sonst*), `vortheilt` (za *vortheil*).
  - `3-028v`: `Zupferdt` (vypadlé *-g-*).
  - `3-029v`: `nit an lange Leger` (*an* za *ein*).
  - `3-030v`: `steinen Büchsen vnd gebrant werden` (elipsa před *vnd gebrant*).
  - `3-031v`: `das die mörser sol` (singulár slovesa s plurálem).

### B. Úplná kontrola početních údajů zbrojnice (`3-021v`–`3-028r`)

| Druh děla | Počet | Váha kusu (ct) | Součet váhy (ct) | Koule (lb) | 100 koulí/kus (ct) | Prach (ct) | Vozy (rozpis / tisk) | Lafety | Koně (rozpis / tisk) | Kladkostroje | Lopatky | Plech. nádoby (rozpis / tisk) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Šarfmece (`3-022r`–`3-023r`) | 2 | 115 | 230 | 85 | 170 | 170 | 2+7+7+2 = **18** | 2 | 114+28+28+8 (+12 lafet?) = **178 / 190** | 2 | 2 | 6 |
| Slavíci (`3-023r`–`3-024r`) | 4 | 80 | 320 | 70 | 280 | 280 | 4+11+11+3 = **29** | 4 | 160+16+44+44+12 = **276** | 3 | 4 | 12 |
| Těžké kulveriny (`3-024r`) | 4 | 66 | 264 | 16 | 64 | 64 | 4+3+(3 prach vynechány)+3 = **13** | 4 | (4×33=132, tisk **93**)+16+12+12+12 = **145** | 3 | 4 | 12 |
| Kartouny (`3-024r`–`3-024v`) | 8 | 50 | 400 | 45 | 360 | 360 | 8+12+12+3 = **35 / tisk 25** | 8 | 160+32+(tisk 8×4=32, správně 48)×2+12 = **268 / 300** | 3 | 8 | 24 |
| **Součet bořičů hradeb** | **18** | — | **1214** | — | **874** | **874** | 18+29+13+25 = **85 (95)** / tisk **104** | **18** | 190+276+145+268 = **879** / tisk **915** (+36) | **11** | **18** | **54** |
| Kulveriny (`3-025r`–`3-025v`) | 6 | 40 | 240 | 12 | 72 | 72 | 3+3+3 = **9** | 6 | 78+12+12+12 = **114** | 3 | 6 | 18 |
| Poloviční kartouny (`3-025v`) | 8 | 36 | 288 | 25 | 200 (v textu chyba *20*) | 200 | 8+8+3 = **19** | 8 | (36:4=9, text *12*)×8=96+32+32+12 = **172** | 3 | 8 | 24 |
| Poloviční kulveriny (`3-026r`) | 10 | 24 | 240 | 7 | 70 | 70 | 3+3+3 = **9** (tisk *133* koulí místo *333*) | 10 | 60+12+12+9 = **93** | 3 | 10 | 10 |
| Čtvrteční kulveriny (`3-026r`–`3-026v`) | 10 | 12 | 120 | 2 | 20 | 20 | 1+1+3 = **5** | 10 | 40+3+3+12 = **58** | 3 | 10 | 10 |
| Falkonety (`3-026v`) | 20 | 6 | 120 | 1 | 20 | 20 | 1+1+3 = **5** | 20 | 60+3+3+12 = **78** | 3 | 20 | 20 |
| **Součet polních děl** | **54** | — | **1008** / tisk **1800** | — | **382** | **382** | **47** | **54** | 114+172+93+58+78 = **515** / tisk **479** (−36) | **15** | **54** | **82** / tisk **40** |
| **Celkový součet** (`3-027r`) | **72** | — | **2222** | — | **1256** | **1256** | **151** (= 104+47) | **72** | **1394** (= 915+479 i 879+515) | **26** | **72** | **136** / tisk **130** (na `3-028r` **216** = 72×3) |

- **Poměr kovu a Löfflerova zakázka (`3-027v`–`3-028r`)**: Cín `222 ct 20 lb` je přesně `10 %` z `2222 ct`; měď `1980 ct` je `90 %` ze zaokrouhlených `2200 ct` (místo `1999,8 ct`). Přepočet augšpurských centů na vídeňské `2222 × 0,85 = 1888,70` (místo dělení `1,15 = 1932,17`), vynásobeno `13 zl.` dává `24 553,10 zl.`, kde `0,10 zl.` při `1 zl. = 210 pf.` činí přesně `21 feniků`.
- **Poloviční falkonety jako zadovky (`3-028v`)**: *zu halber zal / nemlich die 25.* – oproti 100 kusům z `3-028r` jde o čtvrtinu (snad z původně uvažovaných 50 kusů).

---

## 4. Návrhy do glosáře (`knihy/solms-1559/glosar.yaml`)

### A. Důležité upozornění ke kolizi homonym
- **`tazeni` (`Zug`)**: stávající heslo `tazeni` obsahuje tvar `Zug` / `Züg`. V Dávce 3 však `Zug` / `Züg` označuje převážně **kladkostroj / zvedací stroj** (*zdvihadlo s kozou a kladnicemi*). V překladu nebyl u kladkostroje tag `{Zug}` použit, aby se nepropojoval na `tažení`. Doporučujeme buď omezit `Zug` u `tazeni`, nebo v poznámce hesla upozornit na druhý význam.

### B. Nové pravopisné a pádové varianty do stávajících hesel
- **`sarfmece`**: přidat `Scharpffermetzen`, `Scharpffemetzen`, `Scharpffenmetzen`, `Scharpffmetz`
- **`slavik`**: přidat `Nachtigaln`
- **`kartouna`**: přidat `Cartaun`, `Cartaunen`, `Halb Cartaun`, `halb Cartaun`, `doppel Cartaun` (nebo zvážit samostatné heslo pro `poloviční kartouna` a `dvojitá kartouna`)
- **`hadovnice`** (`cs: kulverina`): přidat `Halbschlangen`, `Halb Schlangen`, `Viertel Schlangen`, `viertheil Schlangen`, `viertel Schlangen`, `vierteil Schlangen` (anebo vyčlenit samostatné heslo `ctvrtecni-kulverina`)
- **`falkona`**: přidat `Falconetlin`, `halb Falconetlein`, `halbe Falconetlein`, `Falconet`
- **`rucnice`**: přidat `Handtror`, `hantror`, `handror`
- **`borice-hradeb`**: přidat `Maurbrecher`
- **`ohnostroj`**: přidat `Feurwerck`
- **`ohniva-koule`**: přidat `Feurkugeln`
- **`zbroj`**: přidat `Kriegßrüstung`, `Kriegßrüstungen`
- **`valecne-urady`**: přidat `Kriegsampter`
- **`lafeta`**: přidat `Lade`, `laden`
- **`cent`**: přidat `Cen.`, `cent.`
- **`dela`**: přidat `Handtgeschütz`, `handtgeschütz`, `Wagenbürg geschütz`

### C. Návrhy nových hesel

```yaml
- id: prulomova-dela
  cs: průlomová děla
  de:
  - Prechgeschütz
  - Brechgeschütz
  - Prech
  kategorie: delostrelectvo
  hledat:
  - průlomov\w* děl
  pozn: Těžká obléhací děla (bořiče hradeb: šarfmece, slavíci, těžké kulveriny a kartouny) určená k prorážení hradeb.

- id: ctvrtecni-kulverina
  cs: čtvrteční kulverina
  de:
  - Quartierschlange
  - Viertel Schlangen
  - viertheil Schlangen
  - viertel Schlangen
  - vierteil Schlangen
  kategorie: delostrelectvo
  hledat:
  - čtvrteční\w* kulverin
  pozn: Lehké dlouhé polní dělo (u Solmse váhy 12 centů, ráže 2 libry železa, délky 40 ráží).

- id: plechova-nadoba
  cs: plechová nádoba na prach
  de:
  - Plechenbüchsen
  - plechen Büchsen
  - plechne Büchsen
  - Blechen Büchsen
  - Blechenbüchen
  - Blechbüchen
  - Plechbüchsen
  - Plechnebüchsen
  - Plechnerbüchsen
  - Plechebüchsen
  kategorie: delostrelectvo
  hledat:
  - plechov\w* nádob
  pozn: Měděná odměrná nádoba na střelný prach (po 1, 2, 4, 5, 7 či 10 librách), z níž se přesně sypal prach do nabíjecí lopatky bez rozsypání.

- id: nabijak
  cs: nabiják
  de:
  - Ansetzkolben
  - ansetz kolben
  kategorie: delostrelectvo
  hledat:
  - \bnabijá[kc]
  pozn: Dřevěná tyč s hlavicí k zasouvání a utlačování prachu a ucpávky v hlavni děla.

- id: utocny-vuz
  cs: útočný vůz
  de:
  - Sturmwagen
  - sturmwagen
  kategorie: opevneni
  hledat:
  - útočn\w* v[ůo]z
  pozn: Zvláštní vůz vozové hradby s přední a zadní zásobní truhlou, osazený třemi polovičními falkonety na otočných čepech nebo čtyřmi dvojitými hákovnicemi.

- id: tazny-kun
  cs: tažný kůň
  de:
  - Zugpferdt
  - zugpferdt
  - Zupferdt
  - Ziehroß
  - Ziehpferden
  kategorie: delostrelectvo
  hledat:
  - tažn\w* (kon|koň|kůň)
  pozn: Kůň zapřahaný do dělostřeleckých vozů a lafet (zatížení 2–4 centy podle hmotnosti kusu a terénu).

- id: litec-del
  cs: litec děl
  de:
  - Büchsengiesser
  kategorie: delostrelectvo
  hledat:
  - lit(ec|ci|ců)\w* děl
  pozn: Řemeslný kovolitec specializovaný na odlévání bronzových (zvonovinových) děl z mědi a cínu.

- id: stolice
  cs: stolice
  de:
  - stůl
  - stůln
  - stůllen
  kategorie: delostrelectvo
  hledat:
  - stolic(e|i|í|ích)
  pozn: Těžké dřevěné lože bez kol (Stuhl), v němž byly uloženy velké moždíře (převáželo se na zvláštních zdvojených vozech).

- id: kamenne-delo
  cs: kamenné dělo
  de:
  - steinen Büchsen
  kategorie: delostrelectvo
  hledat:
  - kamenn\w* děl
  pozn: Kamennice – krátké dělo střílející kamenné nebo zápalné koule.

- id: fenik
  cs: fenik
  de:
  - pfenning
  - pfening
  kategorie: miry
  hledat:
  - \bfenik
  pozn: Drobná mince; v bavorsko-augšpurské oblasti platilo 210 feniků za 1 zlatý (7 šilinků po 30 fenicích).

- id: jadro
  cs: jádrová dráha
  de:
  - Kern
  - kerns
  kategorie: delostrelectvo
  hledat:
  - jádrov\w* dráh
  pozn: Přímá (nezkleslá) dráha střely navazující na osu vývrtu (Kernschuss), než střela začne klesat v oblouku.
```
