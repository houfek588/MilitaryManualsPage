# Zpráva z překladu a vizuální revize – `knihy/solms-1559`, Třetí kniha, Dávka 2 (`3-010r`–`3-020v`)

Zpracováno všech **22 stran** Třetí knihy (`3-010r`–`3-020v`, skeny `271`–`292`). Všechny strany byly zkontrolovány podle stažených náhledů skenů (`s271.jpg`–`s292.jpg`, plus hraniční skeny `s270.jpg` a `s293.jpg`), rozděleny do bloků 1 : 1 přesně podle tisku, doplněny o ozdobné iniciály, vyčištěny od chyb OCR i netextových prvků (záhlaví, čísla listů, signatury archů `Cc`–`Dd iij`, kustody, čárové kódy) a plynule přeloženy do češtiny podle `glosar.yaml` a `PRAVIDLA_PREKLADU.md`. Všech 22 stran má nastaveno `stav: zkontrolovano` a `overeno_clovekem: false`.

Ověření skriptem `python -I nastroje/over_strany.py knihy/solms-1559 3-010r 3-010v 3-011r 3-011v 3-012r 3-012v 3-013r 3-013v 3-014r 3-014v 3-015r 3-015v 3-016r 3-016v 3-017r 3-017v 3-018r 3-018v 3-019r 3-019v 3-020r 3-020v --prisne`:
- **22 stran, 0 chyb, 0 varování**.

---

## 1. Přehled změn po stranách

| Strana | List | Sken | Bloky | Poznámky | Hlavní úpravy podle skenů a překlad |
|---|---|---:|---:|---:|---|
| `3-010r` | 10r | 271 | 3 | 2 | `pokracovani: true`, rozděleny 3 odstavce, zásadní oprava `nit tragen` (OCR `mittragen`), opravy `Herr`/`Herrn`/`Herren`, `Historien`, `vor`, `geschetzt`, `Aber`, `in vilen`, odstraněn kustod `Vol=`. |
| `3-010v` | 10v | 272 | 3 | 3 | Nadpis `uroven: 2` (`Volgen hernach andere Ampter…`) a `uroven: 3` (`Erstlich des Schantzmeisters Ampt…`), doplněna iniciála `EIn`, opravy `die Schantz` (OCR `Schan ថ្មី`), `Schantzer` (`Stranger`), `ligens` (`to-gens`), `nach gestellt` (`nach де`), `mit graß`, odstraněn kustod `will /`. |
| `3-011r` | 11r | 273 | 1 | 2 | `pokracovani: true`, ověřena správná foliace `11` ve skenu (OCR četlo `13`), zásadní oprava `Schůch` (OCR `Schach`), opravy `Schantzmeister`, `Rotmeister`, `Rotten`, ponechána tisková chyba `in 5. theil das 20. in eim theil seind` a tvar `deck` s poznámkami, odstraněn kustod `Der`. |
| `3-011v` | 11v | 274 | 5 | 1 | Nadpisy `uroven: 3` (`Der Schiffbrückenmeister.`, `Der Wagenburgmeister.`), doplněny iniciály `DEr`, opravy `vmb vnnd` (`vinbonnd`), `bei einander` (`einan , den`), poznámka k odlišnému znění oproti `050r` ve Druhé knize, odstraněn kustod `Zůuerord=`. |
| `3-012r` | 12r | 275 | 1 | 2 | `pokracovani: true`, opravy `zwentzig` (`z.renkig`), `wagen hinder` (`wogen hunder`), `wirt es`, `hindenher`, slovo `ge=|macht` přesunuto celé na `3-012v`, poznámky k `jhre halb Falconetlin` (vs. `052r`) a `dücken`, odstraněna signatura `Cc`. |
| `3-012v` | 12v | 276 | 4 | 1 | `pokracovani: true` se slovem `gemacht`, rozděleny 4 odstavce, opravy `ansehlich` (`anschlig`), `nicht` (`micht`), `ligen` (`legen`), `man ein` (`mancin`), poznámka ke štítovým vozům (`wagen mit schirmen`). |
| `3-013r` | 13r | 277 | 2 | 0 | Nadpis `uroven: 3` (`Der Wagenmeister.`), doplněna iniciála `EIn`, opravy `vnderrichten` (`vnderachten`), `zeucht` (`feucht`), `bescheit` (`bescheert`), `ordnung` (`ordnũg`), slovo `wa=|gen` přesunuto celé na `3-013v`, odstraněna signatura `Cc ij`. |
| `3-013v` | 13v | 278 | 9 | 2 | `pokracovani: true` se slovem `wagen`, nadpis `uroven: 2` (`Die Arcolorei mit jhren Büchsen vnd wagen.`), iniciála `DAs`, rozlišeno 6 krátkých odstavců rozdělení dělostřelectva, doplněno `jn` (`sollen jn ein eigen weg`), opravy `wirt`, `nit mehr`, ponechána přesmyčka `Schiffbürcken` s poznámkou, odstraněn kustod `kan`. |
| `3-014r` | 14r | 279 | 7 | 0 | `pokracovani: true`, nadpis `uroven: 2` (`Instruction…`), iniciála `SO`, rozděleno 5 odstavců (úvod + body 1–4), opravy `platz`, `nit`, `zeucht`, `achtung`, `auffsehung`, odstraněna signatura `Cc iij`. |
| `3-014v` | 14v | 280 | 13 | 2 | `pokracovani: true`, rozděleny odstavce bodů 5–16, opravy `vorzug`, `Wagenburg.` (`Wagenburga`), `darzů`, poznámky k heverům/kladkostrojům (`züg / Winden vnd hebzeug`) a kolíkům (`pflöck`), odstraněn kustod `Zum`. |
| `3-015r` | 15r | 281 | 9 | 2 | Rozděleno 9 odstavců (body 17–24 + závěrečná úvaha), opravy `zu fůren` (`fåren.`), `mit sampt`, `mög vbergeben`, `Herrn`, `schickt`, ponechány tiskové odchylky `schwerffen` a `Schiffbürcken` s poznámkami, odstraněna signatura `Cc iiij`. |
| `3-015v` | 15v | 282 | 5 | 1 | `pokracovani: true`, nadpis `uroven: 2` (`Fragstück eines Büchsenmeisters.`), iniciála `SO`, rozděleny 3 odstavce otázek, opravy `Paßpfort` (`Pasifport`), `Büchsenschützen`, poznámka k výrazu `Schnarger`, odstraněn kustod `bericht`. |
| `3-016r` | 16r | 283 | 20 | 6 | `pokracovani: true`, rozděleno 19 odstavců otázek (1.–17./18., 19., 20.), opravy `Ob` (`Oder`), `Ror` (`Nor`), `gantzen` (`ganken`), `vierdtzehen`, odborné poznámky ke *kern*, *gantze scheiben*, *plechwagen*, *zigböck*, *sturmzüg/dagreiffen* a *schalck*, odstraněn kustod `Ob`. |
| `3-016v` | 16v | 284 | 7 | 2 | Úvodní odstavec (nečíslované otázky 21–24), nadpis `uroven: 2` (`Antwort vnd vnderricht vff die artickel.`), doplněna iniciála `VOr`, opravy `nit` (`mit`), `pferden` (`fperden`), `platz`, `reissen`, ponecháno `sprich er ja` s poznámkou, odstraněn kustod `des`. |
| `3-017r` | 17r | 285 | 8 | 2 | `pokracovani: true`, rozděleny odstavce odpovědí 5–12, opravy `Wagner` (`Wager`), `Räder` (`Nader`), `nit` (`mit`), `11.` (`u.`), ponechána tisková chyba `so ler` (za *sol er*) a poznámka ke *gesteck*, odstraněn kustod `doch`. |
| `3-017v` | 17v | 286 | 9 | 0 | `pokracovani: true`, rozděleny odstavce odpovědí 12–21, zásadní oprava `nit recht` (`mit recht`), opravy `Der` (`Oer`), `hat` (`hak`), `nemen` (`nemet`), `thůt` (`khut`), odstraněn kustod `Der`. |
| `3-018r` | 18r | 287 | 3 | 3 | Rozděleny odstavce odpovědí 22–24, zásadní opravy `besatzung` (`beschatung`), `nit` (`mit`/`nie`), ponechána přesmyčka `schirfflich` a nejasné `Leudt` s poznámkami, odstraněna signatura `Dd`. |
| `3-018v` | 18v | 288 | 2 | 2 | `pokracovani: true`, opravy `haben / jn` (`habenjn`), `niemant` (`memant`), `auß gibt` (`auß giht`), `selbst` (`felst`), ponechány tvary `befleisset` a `gedecken` s poznámkami, odstraněn kustod `sonst`. |
| `3-019r` | 19r | 289 | 3 | 1 | `pokracovani: true`, nadpis `uroven: 2` (`Was der vnderscheit zwischen gutem vnd bösem Puluer ist.`), iniciála `ZVm`, opravy `můß` (`ntuz`), `lieben` (`heben`), `wüscht` (`wüchst`), `röß puluer` (`röppuluer`), poznámka k *röß*, odstraněna signatura `Dd ij`. |
| `3-019v` | 19v | 290 | 3 | 3 | `pokracovani: true`, odstraněno falešné OCR `L` v záhlaví, nadpis `uroven: 2` (`Nachteil des bösen Puluers.`), doplněna iniciála `ZVm` (OCR `Bm`), opravy `nit` (`mit`), `souil` (`sound`), `schwitzt` (`schwiß`), ponechány tvary `geleuter` a `Salpeters`, poznámka k *wetterleunisch*, odstraněn kustod `einander`. |
| `3-020r` | 20r | 291 | 1 | 2 | `pokracovani: true`, zásadní oprava `nit gůt` (`mit gut`), opravy `behent` (`hehent`), `weit` (`wert`), `schiessen` (`fchteffen`), `Kogel` ověřeno ve skenu, poznámky k *kat* a *schiffern*, odstraněna signatura `Dd iij`. |
| `3-020v` | 20v | 292 | 3 | 2 | Nadpis `uroven: 2` (`Von Salpeter / Schwefel vnd Koln / einem jeden insonderheit.`), zásadní oprava iniciály `ZVndt das an` + `jedes` (OCR `Vndtdas an` + `Sjedes`), opravy `mir` (`mur`), `hauß` (`Hausz`), `fürderlichsten` (`fårderlichsten`), odstraněn kustod `ein`. |

---

## 2. Významné opravy OCR ověřené ze skenů a přechody na okrajích dávky

### A. Kontrola foliace ve skenech (`s271.jpg`–`s292.jpg`)
- Všechny lícové strany dávky nesou v tisku souvislé arabské číslování `10` (`3-010r`) až `20` (`3-020r`).
- Na `3-011r` (sken `273`) přečetlo BSB OCR číslo listu chybně jako `13`; vizuální prohlídka `s273.jpg` jednoznačně potvrzuje vytištěné `11` (na rozdíl od skutečného `13` na skenu `s277.jpg`).

### B. Ozdobné iniciály kapitol a oddílů doplněné podle skenů
- `3-010v` (`s272`): `In Schansmeister` → `EIn Schantzmeister` (velká zdobná iniciála `E`).
- `3-011v` (`s274`): `Der Schiffbrücken meister` → `DEr Schiffbrücken meister` (dvouřádková iniciála `D`); `Er Wagenburg meister` → `DEr Wagenburg meister` (velká zdobná iniciála `D`).
- `3-013r` (`s277`): `In Wagenmeister` → `EIn Wagenmeister` (velká zdobná iniciála `E`).
- `3-013v` (`s278`): `As geschuß` → `DAs geschütz` (dvouřádková iniciála `D`).
- `3-014r` (`s279`): `O ein Fürst` → `SO ein Fürst` (dvouřádková iniciála `S`).
- `3-015v` (`s282`): `O ein Zeugmeister` → `SO ein Zeugmeister` (dvouřádková iniciála `S`).
- `3-016v` (`s284`): `Or erst` → `VOr erst` (velká zdobná iniciála `V`).
- `3-019v` (`s290`): `Bm ersten` → `ZVm ersten` (dvouřádková iniciála `Z`).
- `3-020v` (`s292`): `Vndtdas an / ... Sjedes` → **`ZVndt das an / ... jedes`** (dvouřádková iniciála `Z` před `Vndt` a její spodní tah chybně přečtený jako `S` před `jedes` na následujícím řádku).

### C. Zásadní opravy smyslu v OCR
- `3-010r` (`s271`): **`nit tragen`** (OCR `mittragen` – „které neunese“, nikoli „spolunést“); `Herr` / `Herrn` / `Herren` (OCR `Herz` / `Heren` / `Herzen`); `Historien` (`Hihorien`); `in vilen` (`th vilen`); `vor jn` (`vo ? jn`); `geschetzt` (`geschez`).
- `3-010v` (`s272`): **`die Schantz`** (OCR khmerské znaky `die Schan ថ្មី`); **`nach gestellt`** (OCR cyrilice `nach де ftellt`); **`Schantzer`** (OCR `Stranger`); **`ligens`** (OCR `togens`); **`mit graß`** (OCR `nit graff`); `Schantzmeyster` (`Schankneyier`).
- `3-011r` (`s273`): **`Schůch`** (OCR `Schach` – „až na dobrou stopu k dělům“, nikoli „šach“); `Schantzer` (`Schanker`); `Rotmeister` (`Xotmeister`); `abgangen` (`abgangen` s koncovkami `Rotten`).
- `3-011v` (`s274`): **`vmb vnnd`** (OCR `vinbonnd`); **`bei einander`** (OCR `einan , den`); `vnder` (`ondcr`).
- `3-012r` (`s275`): **`zwentzig`** (OCR `z.renkig`, `zwenkig`, `zwengig`); **`wagen hinder`** (OCR `wogen hunder`); `hindenher` (`hundenher`); `wirt es` (`wirtes`).
- `3-012v` (`s276`): **`ansehlich`** (OCR `anſchlig`); **`nicht`** (OCR `micht`); **`ligen`** (OCR `legen`); `man ein` (`mancin`).
- `3-013r` (`s277`): **`vnderrichten`** (OCR `vnderachten`); **`zeucht`** (OCR `feucht`); **`bescheit`** (OCR `bescheert`).
- `3-013v` (`s278`): **`sollen jn ein eigen weg`** (OCR vynechalo `jn`); **`nit mehr`** (OCR `mit mehr`); `wirt` (`wirk`).
- `3-014r` (`s279`): **`platz`** (`plat`), **`nit`** (`mit`), **`zeucht`** (`seucht`), **`achtung`** (`achtun g`), **`auffsehung`** (`auff , ehung`).
- `3-014v` (`s280`): **`Wagenburg.`** (`Wagenburga`), `vorzug` (`vozug`).
- `3-015r` (`s281`): `zu fůren` (`fåren.`), `mit sampt` (`mit sam ot`), `mög vbergeben` (`mög.vbergeben`).
- `3-015v` (`s282`): `Paßpfort` (`Pasifport`), `Büchsenschützen` (`Büchsenschuken`).
- `3-016r` (`s283`): **`Ob`** (`Oder`), **`Ror`** (`Nor`), `gantzen` (`ganken`), `vierdtzehen` (`vierdbehen`).
- `3-016v` (`s284`): **`nit`** (`mit` – „nechci se najmout natrvalo“), `pferden` (`fperden`), `reissen` (`reiffen`), `platz` (`plas`).
- `3-017r` (`s285`): `Wagner` (`Wager`), `Räder` (`Nader`), `nit` (`mit`), `11.` (`u.`), `stůck` (`ftu.k`).
- `3-017v` (`s286`): **`nit recht`** (OCR `mit recht` – převrácený význam!), `Der` (`Oer`), `hat` (`hak`), `nemen` (`nemet`).
- `3-018r` (`s287`): **`besatzung`** (OCR `beschatung`), **`nit`** (OCR `mit` a `nie`), `tver` → `wer`.
- `3-018v` (`s288`): **`haben / jn`** (`habenjn`), **`niemant`** (`memant`), `auß gibt` (`auß giht`), `selbst` (`felst`).
- `3-019r` (`s289`): **`můß`** (`ntuz`), **`lieben`** (`heben`), **`wüscht`** (`wüchst`), **`röß puluer`** (`röppuluer`).
- `3-019v` (`s290`): odstraněno falešné `L` pod záhlavím, **`nit`** (`mit`), **`souil`** (`sound`), `schwitzt` (`schwiß`), `wüten` (`wåten`).
- `3-020r` (`s291`): **`nit gůt`** (OCR `mit gut` – převrácený smysl!), **`behent`** (`hehent`), **`weit`** (`wert`), `schiessen` (`fchteffen`).
- `3-020v` (`s292`): **`ZVndt das an / ... jedes`** (OCR `Vndtdas an / ... Sjedes`), `mir` (`mur`), `hauß` (`Hausz`).

### D. Přechody přes hranice stran a rozdělená slova
- **Před dávkou (`3-009v` → `3-010r`)**: Na konci `s270.jpg` (`3-009v`) je poslední slovo `durch` a kustod `sie` (slovo rozdělené není). Věta však plynule pokračuje na `3-010r` (`sie alle verseumpt wirt / …`), proto je na prvním bloku `3-010r` nastaveno `pokracovani: true`. Pro Dávku 1 na `3-009v` doporučujeme vynechat kustod `sie` a ukončit poslední větu před návazným začátkem `3-010r` (*„oni všichni zanedbají;“*), tj. např. *„… zodpovídat se z toho, co v té věci“*.
- **Uvnitř dávky**:
  - `3-010v` → `3-011r`: `s272.jpg` končí `da man zu schantzen anfahen` a pod posledním řádkem stojí kustod `will /`, přičemž `3-011r` začíná `will daselbst sein lassen /`. Kustod `will /` byl z `3-010v` odstraněn a `3-011r` začíná `will daselbst…` s `pokracovani: true`.
  - `3-012r` → `3-012v`: `das hinder gestel soll ge=` | `macht sein` → celé slovo `gemacht` přesunuto na `3-012v`.
  - `3-013r` → `3-013v`: `das mann die wa=` | `gen lest` → celé slovo `wagen` přesunuto na `3-013v`.
- **Za dávkou (`3-020v` → `3-021r`)**: Na konci `s292.jpg` (`3-020v`) stojí poslední řádek `wöllē die büchsen füllen wie` a pod ním kustod `ein` (žádné slovo není na hranici stran rozděleno). `s293.jpg` (`3-021r`) začíná `ein meelsack / dann gehn sie zu stücken /`. Český překlad `3-020v` končí slovy *„chtějí děla {büchsen} plnit jako“*, na což může Dávka 3 na `3-021r` s `pokracovani: true` plynule navázat slovy *„pytel mouky, a pak se rozletí na kusy.“*.

---

## 3. Sporná místa a tiskové chyby originálu (DE + CS)

1. **`3-010v` – `bei dem lermen eines Flecken odder Schloß`**:
   - **DE**: `auch soll der Schantzmeyster bei dem lermen eines Flecken odder Schloß sein`
   - **CS**: `Šancmistr má být rovněž při poplachu {lermen} před městečkem či zámkem,[^1]`
   - **Poznámka**: Doslovně „při poplachu“ (*Lärmen*), snad ve smyslu prvního znepokojení posádky před obležením, případně písařská či tiskařská obměna za *berennen* (průzkumné obklíčení pevnosti).
2. **`3-011r` – `in 5. theil das 20. in eim theil seind`**:
   - **DE**: `diesel-ben 500. sollen getheilt werden in 5. theil das 20. in eim theil seind`
   - **CS**: `těchto 500 má být rozděleno na 5 dílů, tak aby v jednom dílu bylo 20 osob;[^2]`
   - **Poznámka**: Ponecháno jako věrné znění tisku s poznámkou o početní nesrovnalosti (500 : 20 = 25 rot, ne 5). Na téže straně ponechán i tvar `so deck sie wol` (zkrácená shoda za *decken sie wol*).
3. **`3-011v` a `3-012r` – rozdíly proti Druhé knize (`050r` a `052r`)**:
   - Na `3-011v` tisk výslovně uvádí, že mistr vozové hradby *„steht dem Zeugmeister nicht zu“* a dělová vozba má být svěřena *vozmistrovi* (`dem Wagenmeister`), zatímco `050r` uvádí pravý opak (*„stehet den Zeugmeistern zů“* a *„dem wagenburgmeister“*).
   - Na `3-012r` tisk uvádí `jhre halb Falconetlin` („svá/jejich poloviční falkoneta“), kde `052r` má `drei halb Falckanetlein`. Věcné rozdíly zachyceny v poznámkách s proklikem na `[[050r|50r]]` a `[[052r|52r]]`.
4. **`3-013v`, `3-015r`, `3-016v`, `3-017r`, `3-018r`, `3-018v`, `3-019v` – drobné tiskové chyby ponechané v `de` s poznámkami**:
   - `3-013v`, `3-015r`: přesmyčka `Schiffbürcken` (místo *Schiffbrücken*).
   - `3-015r`: zkomolenina `schwerffen` (patrně kontaminace *schießen* a *werffen*).
   - `3-016v`: vypadlé *-t* ve `sprich er ja`.
   - `3-017r`: `so ler` (tisková chyba za *so sol er*).
   - `3-018r`: přesmyčka `schirfflich` (za *schrifftlich*) a nejasné `die nicht gantz wol Leudt ist` (snad *beleut* „lidnaté/osazené“, nářeční *leit* „leží“, či omyl za *bewart/gebauwt*).
   - `3-018v`: `befleisset` (za *befleissest*) a `gedecken` (vypadlé *n* za *gedencken*).
   - `3-019v`: `nit kern rein geleuter` (vypadlé *-t* / *ist*) a `der Salpeters` (přebytečné *-s*).

---

## 4. Návrhy do glosáře (`knihy/solms-1559/glosar.yaml`)

### A. Nová hesla navrhovaná do glosáře

```yaml
- id: mistr-lodniho-mostu
  cs: mistr lodního mostu
  de:
  - Schiffbrückenmeister
  - Schiffbrücken meister
  kategorie: velitele
  pozn: Velitel vozů s čluny a stavitel lodních (pontonových) mostů; podléhá zbrojmistrovi a táboří s ním u dělostřelectva a munice.

- id: puskovy-strelec
  cs: puškový střelec
  de:
  - Büchsenschützen
  - Büchsenschütze
  kategorie: jednotky
  pozn: Střelec z děla či ručnice nižšího postavení než vyučený mistr puškař (Büchsenmeister), který neumí samostatně konstruovat a rýsovat děla ani vyrábět ohňostroje a prach.

- id: zvedaci-koza
  cs: zvedací koza
  de:
  - zigböck
  - böcken
  kategorie: delostrelectvo
  pozn: Trojnohý zvedák či hever (Ziehbock) s kladkami a navijáky (Züge, Winden) ke zvedání těžkých dělových hlavní z vozů do lafet.

- id: zemedelci-usedlici
  cs: zemský usedlík
  de:
  - Landtsessen
  - Landsassen
  kategorie: osoby
  pozn: Domácí šlechtičtí a svobodní držitelé půdy v zemi panovníka, z nichž má válečný pán vychovávat vlastní odborníky pro zbrojnici a dělostřelectvo.

- id: mineralni-necistota
  cs: zemitá nečistota (Schalk)
  de:
  - Schalck
  - schalck
  kategorie: delostrelectvo
  pozn: Zemitá či hořká solná nečistota (vedle kuchyňské soli, kamence, louhu a mastnoty), která zůstává v nedostatečně vyčištěném ledku a kazí střelný prach.
```

*(Pozn.: Pro `plechwagen` a `gantze scheiben` lze rovněž uvážit hesla `okovaný plošinový vůz` a `plné kotoučové kolo`, případně je ponechat s výkladem v poznámkách překladatele, jak je provedeno na `3-016r`.)*

### B. Nové pravopisné a tvarové varianty do stávajících hesel

- **`delostrelectvo`**: přidat `Arcolorei` (toto je převažující pravopis Třetí knihy!)
- **`puskar`**: přidat `Büchsenmeisterei` (případně jako příbuzné heslo „puškařské umění“)
- **`sancmistr`**: přidat `Schantzmeyster`, `Schantzmeisters`
- **`sancir`**: přidat `Schantzer`, `Schantzern`, `Quastitorn`, `Quastitores`, `Quastores`
- **`vozova-hradba`**: přidat `Wagenburgk`
- **`mistr-vozove-hradby`**: přidat `Wagenburgkmeister`, `Wagenburgkmeisters`
- **`pontonovy-most`**: přidat `Schiffbürcken` (tisková přesmyčka z `3-013v` a `3-015r`)
- **`dela`**: přidat `Büchs`, `büchsen`, `stücks`, `stücken`, `geschütz`
- **`falkona`**: přidat `halb Falconetlin` (resp. zvážit samostatné heslo `falkonet` dle zadání pro 3. knihu)
- **`sarfmece`**: přidat `Scharpffmetz`
- **`kartouna`**: přidat `Cartaun`, `Cartaunen`, `halb Cartaun`
- **`hadovnice`**: přidat `Notschlang`, `Schlang`
- **`mozdir`**: přidat `halb Mörser`, `Mörsern`
- **`hakovnice`**: přidat `dopel hacken`, `doppelnhacken`, `Hacken`
- **`koule`**: přidat `Kogel`, `Kogeln`, `kugeln`, `kugel`
- **`rucnice`**: přidat `rorn`
- **`strelec`**: přidat `handtschützen`
- **`bastej`**: přidat `Pastei`, `pasteien`, `pastei`
- **`basta`**: přidat `Polwerck`
- **`bocni-obrana`**: přidat `streichwern`
- **`utok`**: přidat `storm`
- **`stitovy-vuz`**: přidat `wagen mit schirmen`
- **`pripijeni`**: přidat `zutrinck`
- **`zavazek`**: přidat `pflichten`
- **`vyterak`**: přidat `wüsch`
- **`zold`**: přidat `Besoldung`
- **`pechota`**: přidat `fůß`
- **`zadni-voj`**: přidat `nach zug`
