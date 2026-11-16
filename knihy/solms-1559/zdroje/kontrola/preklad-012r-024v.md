# Zpráva z překladu a vizuální revize – `knihy/solms-1559` (Dávka 2: `012r`–`024v`)

Zpracováno všech **26 stran** (`012r`–`024v`, skeny `115`–`140`), včetně obou celostránkových dřevořezů (`014v`, `024v`). Všech 26 stran má nastaveno `stav: prelozeno` a `overeno_clovekem: false`.

Ověření skriptem `python -I nastroje/over_strany.py knihy/solms-1559 012r … 024v --prisne`:
- **26 stran, 0 chyb, 0 varování**.

---

## 1. Přehled změn po stranách

| Strana | List | Sken | Počet bloků | Poznámky | Hlavní úpravy podle skenů a překlad |
|---|---|---:|---:|---:|---|
| `012r` | 12r | 115 | 5 | 2 | `pokracovani: true`, opravy OCR (`letb`→`leib`, `sollen jedes`→`Auch soll ein jedes`, `Kustung`→`Rüstung` aj.), překlad + poznámky (*Barschen*, *Gestrengen vnd Ehrnuesten*). |
| `012v` | 12v | 116 | 4 | 0 | `pokracovani: true`, opravy OCR (`wöll`, `Derhalben`, `Rittern`, `Räth`, `Ads mische`→`Römische`), odstraněn kustod `Dars`. |
| `013r` | 13r | 117 | 5 | 0 | Opravy OCR (`wöl`, `vnchristlich`, `Römis. Keyser. Maiest.`, `forch`), překlad. |
| `013v` | 13v | 118 | 6 | 0 | `pokracovani: true`, odstraněno záhlaví `Das ander Bachy` z 1. bloku, opravy OCR (`ehlich`→`ehrlich`, `ein̄`→`einen`, `Kreigsuolck`→`Kriegsuolck`), odstraněn kustod `des` na konci (patří na `014r`). |
| `014r` | 14r | 119 | 4 | 0 | `pokracovani: true`, nadpis `uroven: 2` pro kapitolu o nejvyšším polním hejtmanovi, rozep. `etc.`, oprava `gute eh : liche`→`gůte ehrliche`. |
| `014v` | 14v | 120 | 1 | 0 | Doplněn podrobný popis dřevořezu `drevorez-120.jpg` (HD 1545 – nejvyšší polní hejtman). |
| `015r` | 15r | 121 | 6 | 0 | Doplněna ozdobná iniciála `E` (`EIn`), opravy OCR (`mit allein`→`nit allein`, `friger`→`jrriger`, `Proutantmeister`→`Prouiantmeister`), rozdělení 6 odstavců dle tisku. |
| `015v` | 15v | 122 | 7 | 1 | `pokracovani: true`, opravy OCR (`Kenfanen`→`Renfanen`, `eni`→`einen`, `müglich`→`möglich`), rozdělení 7 odstavců, odstraněn kustod `Dann`, poznámka k `oder jr bedarff`. |
| `016r` | 16r | 123 | 6 | 1 | Opravy OCR (`site gen`→`zügen`, `plans`→`platzs`), rozdělení 6 odstavců, odstraněn kustod `In`, poznámka k tiskové zkratce `der Ober`. |
| `016v` | 16v | 124 | 3 | 0 | Opravy OCR (`verachten`→`verrichten`, `orsacher`→`vrsächer`, `schuldigiyi`→`schuldig ist`), rozdělení 3 odstavců, odstraněn kustod `daß`. |
| `017r` | 17r | 125 | 6 | 1 | `pokracovani: true`, opravy OCR (`bafß`→`daß`, `personens`→`personen`), rozdělení 6 odstavců, odstraněn kustod `Kein`, poznámka k vyhlášení nepřátelství (*verwaren*). |
| `017v` | 17v | 126 | 6 | 0 | Opravy OCR (`obergleich`→`oder gleich`, `Chaftliche`→`Christliche`, `Waldstate`→`Waldstatt`), rozdělení 6 odstavců, odstraněn kustod `fluche` (`flucht`). |
| `018r` | 18r | 127 | 4 | 0 | `pokracovani: true`, opravy OCR (`nitmut`→`nit mit`, `ey ?`→`ehr`, `Wagen`→`Wägen`), rozdělení 4 odstavců, odstraněn zbytek signatury `۵`. |
| `018v` | 18v | 128 | 7 | 0 | `pokracovani: true`, oprava `verachtlich leger`→`verächtlich lege`, slovo `ler-men` přesunuto celé na `019r`. |
| `019r` | 19r | 129 | 5 | 0 | `pokracovani: true`, slovo `lermen` doplněno z `018v` (bez `*`), oprava `ein ond oder`→`ein vnd vber`, slovo `Ober-sten` přesunuto celé na `019v`, rozděleno 5 odstavců. |
| `019v` | 19v | 130 | 5 | 0 | `pokracovani: true`, odstraněno záhlaví `Dasander Buch`, připojeno celé `Obersten`, oprava `fermes`→`ferr es`, `erfarnen`→`erfaren`, odstraněn kustod `des`, 5 odstavců. |
| `020r` | 20r | 131 | 5 | 1 | `pokracovani: true`, oprava `Roßmålen`→`Roßmülen`, `Bach`→`Bäch`, `ge-melt` přesunuto celé na `020v`, 5 odstavců, poznámka k *Darzas*. |
| `020v` | 20v | 132 | 3 | 0 | `pokracovani: true`, připojeno celé `gemelt)`, oprava `Xustung`→`Rüstung`, `strcychwehren`→`streychwehren`, 3 odstavce, odstraněn kustod `Wann`. |
| `021r` | 21r | 133 | 6 | 0 | Opravy OCR (`begeru`→`begern`, `geivint`→`gewint`, `x .`→`etc.`), rozep. `gemein̄`→`gemeinen`, 6 odstavců. |
| `021v` | 21v | 134 | 5 | 2 | `pokracovani: true`, oprava `silbergeschwz`→`silbergeschirr`, `abztehe`→`abziehen`, odstraněn kustod `nemen /`, 5 odstavců, poznámky k `Feldhaupt` a *weiße Stäblein*. |
| `022r` | 22r | 135 | 8 | 0 | `pokracovani: true`, opravy OCR (`ficher Hett`→`sicher-heit`, `kriegsuoltketiwan`→`kriegsuolck etwan`, `rüß`→`růß`), rozděleno 8 odstavců, odstraněn kustod `Der`. |
| `022v` | 22v | 136 | 8 | 0 | Odstraněno záhlaví `Dasander Buch`, opravy OCR (`Papporten`→`Paßporten`, `Grantmeister`→`Brantmeister`, `laſſen verachten`→`lassen verrichten`, `mit recht`→`nit recht`), 8 odstavců, odstraněn kustod `Alle`. |
| `023r` | 23r | 137 | 8 | 1 | Opravy OCR (`Herolts`→`Herolt /`, `Arke`→`Artzt`, `Secretariu`→`Secretarium`, rozep. `fürgesetzē` / `gebürlichē`), odstraněn kustod `als`, poznámka k *Potentaten*. |
| `023v` | 23v | 138 | 5 | 1 | `pokracovani: true`, oprava `schand 1`→`schantzen`, `roff oft fufz`→`roß vnd fuß`, doplněny závorky `(wie gehört)`, odstraněn kustod `belegert /`, poznámka k *am anzug*. |
| `024r` | 24r | 139 | 4 | 1 | `pokracovani: true`, opravy OCR (`wölber`→`wöl bei`, `gab`→`gib`, `2 .`→`etc.`), rozděleny 4 odstavce, poznámka k *Memorial*. |
| `024v` | 24v | 140 | 1 | 0 | Doplněn podrobný popis dřevořezu `drevorez-140.jpg` (HD 1545 – polní maršálek před kapitolou `025r`). |

---

## 2. Významnější opravy OCR ověřené ze skenů (`s115.jpg`–`s140.jpg`)

- **Ozdobná iniciála**: `015r` (`s121.jpg`) `In jeder` → `EIn jeder` (velké zdobené `E` + `In`).
- **Záměny smyslu v OCR**:
  - `012r`: `Auch sollen jedes Fendlin` → ve skenu `Auch soll ein jedes Fendlin`; `letb` → `leib`; `on dire` → `vnd jre`; `Kustung` → `Rüstung`.
  - `012v`: `will` → ve skenu `wöll`; `Derhaben` → `Derhalben`; `Xattern` → `Rittern`; `Ads mische` → `Römische`.
  - `013r`: `wil` → `wöl`; `on chaftlich` → `vnchristlich`; `Komis , Keyser . Marest` → `Römis. Keyser. Maiest.`.
  - `013v`: `ehlich` → `ehrlich`; `Kreigsuolck` → `Kriegsuolck`; `ein hohen … ein geringen` → ve skenu se zkracovací čárkou `ein̄` → `einen`.
  - `015r`: `mit allein` → `nit allein` (zásadní obrat významu!); `friger` → `jrriger`; `Proutantmeister` → `Prouiantmeister`.
  - `015v`: `Kenfanen` → `Renfanen`; `kreigsleuten` (v tisku opravdu takto, zachováno); `müglich` → `möglich`.
  - `016r`: `site gen` → `zü-gen`; `plans` → `platzs`; `odenlich` → `ordenlich`.
  - `016v`: `verachten` → ve skenu `verrichten` (zásadní obrat významu!); `orsacher` → `vrsächer`; `schuldigiyi` → `schuldig ist`.
  - `017r`: `personens` → `personen`; `bafß` → `daß`.
  - `017v`: `obergleich` → `oder gleich`; `Waldstate` → `Waldstatt`.
  - `018r`: `nitmut` → `nit mit`; `ey ?` → `ehr`; `Wagen` → `Wägen`.
  - `018v`: `verachtlich leger` → ve skenu `verächtlich lege`.
  - `019r`: `ein ond oder geben` → ve skenu `ein vnd vber geben`; doplněno `(` před `wie er dann beuelch hat)`.
  - `019v`: `fermes` → `ferr es`; `erfarnen` → `erfaren`; `D berfter` → `Oberster`.
  - `020r`: `Roßmålen` → `Roßmülen`; `Erkknappen` → `Ertzknappen`; `Bach` → `Bäch`.
  - `021r`: `begeru` → `begern`; `x .` → `etc.`.
  - `021v`: `silbergeschwz` → `silbergeschirr`; `abztehe` → `abziehen`.
  - `022r`: `ficher Hett` → `sicher-heit`; `kriegsuoltketiwan` → `kriegsuolck etwan`.
  - `022v`: `Papporten` → `Paßporten`; `Grantmeister` → `Brantmeister`; `laſſen verachten` → ve skenu `lassen verrichten`; `mit recht` → ve skenu `nit recht` (dvojitá oprava smyslu!).
  - `023r`: `ein Herolts Trommeter` → ve skenu `ein̄ Herolt / Trommeter`; `Feldvn leib Arke` → `Feld vn̄ leib Artzt`; `fürgesetze … gebürlicht` → rozep. `fürgesetzten … gebürlichen`.
  - `023v`: `schand 1` → `schan-tzen`; `roff oft fufz` → `roß vnd fuß`; doplněny závorky `(wie gehört)`.
  - `024r`: `wölber dem Fanensterben` → ve skenu `wöl bei dem Fanen sterben`; `Ich gab dir` → `Ich gib dir`; `2 .` → `etc.`.
- **Záhlaví a kustody**: odstraněna záhlaví omylem vtažená do textu na `013v`, `019v`, `022v` a odstraněny kustody z konců `012v`, `015v`, `016r`, `016v`, `017r`, `017v`, `018r`, `020v`, `021v`, `022r`, `022v`, `023r`, `023v`, i zbytečný kustod `des` z konce `013v`.
- **Návaznost před začátkem dávky (`011v` → `012r`)**: V `011v.yaml` (mimo tuto dávku, ponecháno beze změny) zůstal na konci vtažen kustod `leib`, přestože slovo `leib` otevírá první řádek `012r` (`leib warten soll`). Doporučujeme při zpracování Dávky 1 kustod `leib` z `011v.yaml` odstranit.

---

## 3. Sporná místa DE + CS k rozhodnutí

1. **`012r` – `die Barschen` (`Barschen vnd schweren zeug`)**:
   - **DE**: `auch vermögen die pferdt nicht die Barschen vnd schweren zeug für vnd für zutragen`
   - **CS**: `rovněž koně nedokážou ustavičně nosit koňskou zbroj[^1] a těžkou výstroj {zeug}.`
   - **Poznámka**: Převedeno jako koňská zbroj / barda (z fr. *barde* / něm. *Barde*, *Barsche* = plátová či kroužková ochrana koně). Možná varianta: *koňské krunýře* nebo *bary/bardy*.
2. **`012r`, `013v` – `die Gestrengen vnd Ehrnuesten`**:
   - **DE**: `Vnd daß der Adell den titel hat / die Gestrengen vnd Ehrnuesten`
   - **CS**: `„přísní a cti pevní“[^2]` (na `012r` s vysvětlující poznámkou, na `013v` bez opakování poznámky).
   - **Alternativa**: Tradiční dobový český ekvivalent *urození a stateční* nebo *stateční a cti pevní*.
3. **`013v` – `dardurcht` a `016r` – `der Ober` a `021v` – `Feldhaupt`**:
   - Tiskové zvláštnosti/zkratky v předloze ponechány v `de` (`dardurcht`, `der Ober`, `Feldhaupt`), u `der Ober` a `Feldhaupt` doplněna krátká poznámka v `cs`.
4. **`015v` – `oder jr bedarff` (přenesená negace)**:
   - **DE**: `Wann aber ein Oberster nit in der Wagenburg ziehen noch ligen wil / oder jr bedarff`
   - **CS**: `Nechce-li však nejvyšší velitel táhnout ani tábořit ve vozové hradbě, anebo jí ani nepotřebuje,[^1]`
   - **Zdůvodnění**: Zápor z `nit … noch` se přenáší i na `oder` (bez této elipsy záporu by nedávalo smysl následné *dannoch einen geschickten wagenmeister*).
5. **`017r` – `zum abzucht` a `018r` – `mit weitender / schneller / vnordnung`**:
   - V tisku stojí skutečně `abzucht` (doložená raně novohornoněmecká varianta k *Abzug*) a `weitender` (rozbíhající se do šíře / rozptylující se). Přeloženo jako `k ústupu` a `v rozptýleném, zbrklém nepořádku`.
6. **`020r` – `Darzas`**:
   - **DE**: `können auch an denselben orten nicht wol plätz / Darzas oder Paßteien verborgen sein / dammen stende`
   - **CS**: `prostranství, tarasy[^1] či bašty {Paßteien}, kde by obránci stáli`
   - **Poznámka**: *Darzas* (z *Tarras* / *Tarzas*, souvisí s čes. *taras*) = dřevěný či sypaný obranný val.
7. **`023r` – `Potentaten`**:
   - **DE**: `Alle befriedung / Potentaten / gewalt vnnd beuelch die Feinde betreffend`
   - **CS**: `Veškeré uzavírání míru, jednání s mocnostmi,[^1] plné moci a rozkazy týkající se nepřátel`
   - **Poznámka**: Může znamenat pravomoc jednat s cizími mocnáři (*Potentaten*), anebo jít o tiskařskou záměnu za *Patenten* (ochranné či zplnomocňovací patenty).
8. **`023v` – `am anzug` ve významu odtahu**:
   - **DE**: `Darumb soll der Oberst am anzug zum Renfanen vnd lauffenden hauffen / alleweg den mehrer theil zu roß vnd fuß … zu hinderst ordnen`
   - **CS**: `Proto má nejvyšší velitel při odtahu[^1] postavit k předvojové korouhvi {Renfanen} a útočným pohyblivým houfům vždy největší díl jízdy i pěchoty … úplně dozadu`
   - **Zdůvodnění**: V celém kontextu jde o ústup z ležení před nepřítelem a krytí týlu (*zu hinderst ordnen*); *anzug* zde znamená nástup k ústupovému pochodu (příp. tiskařskou záměnu za *abzug*).
9. **`024r` – `im Memorial` a `thůts`**:
   - `thůts` (tisková přesmyčka za `thůst`) ponecháno v `de`; odkaz `im Memorial` ponechán v `cs` jako `v pamětním spisu[^1]`.

---

## 4. Návrhy do glosáře (`knihy/solms-1559/glosar.yaml`)

### A. Nové termíny pro doplnění hesel

```yaml
- id: beutmeister
  cs: rozdělovač kořisti
  de:
  - Beutmeister
  - Beutmeistern
  - Beutmeisters
  kategorie: zold
  hledat:
  - rozdělovač\w* kořist
  pozn: Beutmeister – dočasně ustanovený úředník z jízdy i pěchoty, který po boji shromažďuje společnou kořist, zpeněžuje ji a spravedlivě rozděluje mezi vojáky.

- id: brantmeister
  cs: výběrčí výpalného
  de:
  - Brantmeister
  kategorie: zold
  hledat:
  - výběrčí\w* výpaln
  pozn: Brandmeister – úředník pověřený nejvyšším polním hejtmanem vybíráním a vyúčtováním výpalného od měst a obcí.

- id: brenfanen
  cs: žhářská korouhev
  de:
  - Brenfanen
  kategorie: jednotky
  hledat:
  - žhářsk\w* korouh
  pozn: Brennfahne – oddíl střelců pod vlastním hejtmanem, pověřený vypalováním na rozkaz velitele tam, kde obec nezaplatila výpalné.

- id: markytan
  cs: markytán
  de:
  - Mercatanten
  kategorie: zold
  hledat:
  - markytán
  pozn: Obchodník a zásobovatel táhnoucí s vojskem, jenž prodává potraviny a nápoje v ležení pod ochranou profouse.

- id: futerhauptman
  cs: pícnický hejtman
  de:
  - Futer hauptman
  kategorie: sluzba
  hledat:
  - pícnick\w* hejtman
  - hejtman\w* pro píci
  pozn: Hejtman ustanovený k organizovanému a spořádanému opatřování píce pro koně pod zvláštní korouhví.

- id: lermen
  cs: poplach
  de:
  - lermen
  kategorie: sluzba
  pozn: Doplnění malé varianty „lermen“ ke stávajícímu heslu `poplach`.

- id: mustrunk-mistr
  cs: přehlídkový mistr
  de:
  - Mustermeister
  kategorie: zold
  hledat:
  - přehlídkov\w* mistr
  pozn: Mustermeister – úředník pověřený prováděním přehlídek vojska (obdoba přehlídkového komisaře – Musterherr).
```

### B. Solmsovské pravopisné varianty pro doplnění stávajících hesel v `glosar.yaml`

- `nejvyssi-polni-hejtman`: doplnit `Oberster Feldhauptman`, `Obersten Feldhauptman`, `Obersten Feldhauptmans`, `oberst Feldhauptman`, `ober Feldhauptman`, `oberster Feldhauptman`, `Feldhauptman`.
- `valecny-lid`: doplnit `Kriegsuolck`, `Kriegsuolcks`, `Kriegsleut`, `Kriegsleuten`, `Kriegsman`.
- `velitele`: doplnit `Beuelchßman`, `beuelchs Leute`, `beuelchsleuten`.
- `valecny-rada`: doplnit `Kriegßräth`, `Räth`.
- `valecny-knize`: doplnit `Kriegsfürsten`.
- `hejtman`: doplnit `Hauptleuten`, `hauptman`.
- `rytmistr` / `jizda`: doplnit `Reutern`, `Reisigen`, `Reyssigen`.
- `lehka-jizda`: doplnit `ringe Pferde`, `ringe pferd`.
- `prapornik`: doplnit `Fendrich`, `Fendrichen`.
- `praporec`: doplnit `Fendlein`, `fendlin`.
- `korouhev`: doplnit `Fanen`, `fanen`.
- `pechota`: doplnit `Fußuolck`, `fußuolck`, `Fußknecht`.
- `knecht`: doplnit `Knechten`, `Knecht`.
- `lancknecht`: doplnit `Landsknecht`, `landsknecht`.
- `strelec`: doplnit `Schützen`.
- `herold`: doplnit `Herolt`.
- `trubac`: doplnit `Trommeter`.
- `hudba`: doplnit `spil`, `Trommenschlager`.
- `kotlar`: doplnit `Heerpaucker`.
- `tlumocnik`: doplnit `Tolmetschen`.
- `zalmistr`: doplnit `Zalmeister`.
- `pisar`: doplnit `Musterschreiber`.
- `vozmistr`: doplnit `wagenmeister`.
- `mistr-vozove-hradby`: doplnit `Wagenburg meister`.
- `vozova-hradba`: doplnit `Wagenburg`.
- `lezeni`: doplnit `Leger`, `leger`.
- `straz`: doplnit `wacht`, `Wacht`.
- `stálá stráž` (`hlidka`): doplnit `Schiltwacht`.
- `heslo`: doplnit `Losung`, `losung`.
- `losament`: doplnit `Losament`.
- `pruvodni-list`: doplnit `Paßporten`.
- `sluzebni-list`: doplnit `bestellbrieff`, `bestallung`.
- `artikulni-list`: doplnit `Artickels Brieff`.
- `zavazek`: doplnit `pflicht`.
- `vymetani-truhel`: doplnit `Kisten fegen`.
- `vypalne`: doplnit `Brantschatzung`, `gebrantschatzt`.
- `prehlidka`: doplnit `musterung`.
- `proviant`: doplnit `Prouiant`, `prouiant`.
- `zold`: doplnit `besoldung`.
- `vzpoura`: doplnit `meuterei`.
- `zaloha`: doplnit `haltsteten`.
- `utok`: doplnit `Sturms`, `sturm`, `Stürmen`.
- `sik`: doplnit `hauffen`, `hauff`, `ordenungen`.
- `dela`: doplnit `geschütz`, `Feldgeschütz`, `Feld Geschütz`.
- `mozdir`: doplnit `Mörsser`.
- `puskar`: doplnit `Büchsenmeistern`, `Büchsenmeister`.
- `ohnostroj`: doplnit `Feuerwerck`.
- `rucnice`: doplnit `Handroren`, `handrorn`.
- `zbroj`: doplnit `Rüstung`, `Harnisch`.
- `basta`: doplnit `Paßteien`.
- `polni-sance` / `basta` (`bolverk`): doplnit `Polwerck`, `Polwercken` pod `basta` (`bolverk`).
- `bocni-obrana`: doplnit `streychwehren`.
- `zved`: doplnit `kundtschafft`.
- `tazeni`: doplnit `zug`, `züg`.
- `turci`: doplnit `Türcken`.
