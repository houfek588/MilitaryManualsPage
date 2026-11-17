# Zpráva z překladu a vizuální revize – `knihy/solms-1559`, První kniha, Dávka 1 (`1-001v`–`1-009v`)

Zpracováno všech **19 stran** První knihy (`1-001v`, `1-erb-cisare`, `1-jezdec`, `1-002r`–`1-009v`, skeny `10`–`28`), včetně tří celostránkových dřevořezů (`drevorez-010.jpg`, `drevorez-011.jpg`, `drevorez-012.jpg`). Všech 19 stran má nastaveno `stav: prelozeno` a `overeno_clovekem: false`.

Ověření skriptem `python -I nastroje/over_strany.py knihy/solms-1559 1-001v 1-erb-cisare 1-jezdec 1-002r 1-002v 1-003r 1-003v 1-004r 1-004v 1-005r 1-005v 1-006r 1-006v 1-007r 1-007v 1-008r 1-008v 1-009r 1-009v --prisne`:
- **19 stran, 0 chyb, 0 varování**.

---

## 1. Přehled změn po stranách

| Strana | List | Sken | Bloky | Poznámky | Hlavní úpravy podle skenů a překlad |
|---|---|---:|---:|---:|---|
| `1-001v` | 1v | 10 | 1 | 0 | Prohlédnut `drevorez-010.jpg` a `s010.jpg`; doplněn `popis` císařského znaku Karla V. s Herkulovými sloupy a nápisovými páskami `CAROLVS – PLVS. VLTRA – QVINTI – 15 – 44`. |
| `1-erb-cisare` | říšský znak | 11 | 1 | 0 | Prohlédnut `drevorez-011.jpg` a `s011.jpg`; doplněn `popis` znaku Karla V. v řetězu Zlatého rouna bez rámečku a bez textových stuh. |
| `1-jezdec` | jezdecký portrét | 12 | 1 | 0 | Prohlédnut `drevorez-012.jpg` a `s012.jpg`; doplněn `popis` jezdeckého portrétu vousatého velitele jedoucího vlevo pod klenbou větví. |
| `1-002r` | 2r | 13 | 2 | 1 | Věnování králi Filipu II. jako `nadpis` (`uroven: 2`), doplněna ozdobná iniciála `DVrchleuchtigster`, opravy OCR (`Großmechtigsten`, `Lützenburg`, `Seelandt`, `Osterreichischen`, `Maiestat`, `vnnütz`), rozpsány `vñ`→`vnd` a `ꝛc.`→`etc.`, odstraněno tužkové `3`, folio `2` a signatura `A ij`, přidána poznámka `[^1]` k titulatuře Filipa II. |
| `1-002v` | 2v | 14 | 2 | 2 | `pokracovani: true`, opravy OCR (`Mitthridate`, `zweivndzwentzig`, `erwelet`, `Krigshändel`, `Diener`, `Mün-tzenberg`), podpisová část oddělena jako 2. blok, poznámka `[^1]` (Cicero, Lucullus, Mithridatés) a `[^2]` (osamocená závorka `gnaden)` a tvary *wunderwarlichen*, *meinn Sönen*). |
| `1-003r` | 3r | 15 | 5 | 1 | Nadpisy `uroven: 2` (`Eingang der Kriegs ordnung.`, `Vorrede vnd eingang diser beschreibung…`), doplněna iniciála `DIe` (2×), opravy OCR (`Keiserlich Maiestat`, `ernstlichsten Rüstung`, `Römern`, `mann`), ponecháno tiskové `nachtheilt` s poznámkou `[^1]`, slovo `Be-uelch` přesunuto celé na `1-003v`, odstraněno záhlaví, tužkové `4`, folio `3` a signatura `A iij`. |
| `1-003v` | 3v | 16 | 7 | 1 | `pokracovani: true` se slovem `Beuelch/`, rozděleno přesně na 7 odstavců, opravy OCR (`im gebrauch`, `Keisern`, `dann`, `Regirung`, `Pollicei`, `Vnd`), ponechány tiskové odchylky `ordunng` a `bedach` s poznámkou `[^1]`, odstraněno záhlaví, zbloudilé `२` a kustod `vnd`. |
| `1-004r` | 4r | 17 | 5 | 1 | `pokracovani: true`, nadpis `uroven: 2` (`Volgt hernach… Meister vnd gewaltig.`), opravy OCR (`Vnd als dann`, `je`, `Römern`, správné pořadí řádků nadpisu oproti zkomolenému OCR), poznámka `[^1]` k tvaru *mischbreuch*, odstraněno záhlaví, tužkové `5`, folio `4` a kustod `Das`. |
| `1-004v` | 4v | 18 | 5 | 1 | Doplněna iniciála `DAs`, rozděleno na 5 odstavců, opravy OCR (`Cronica`, `satzt`, `sein`, `lieb`, `erholt`, doplněna lomítka), poznámka `[^1]` k Caesarovi (58 př. n. l.) a titulu *Hauptman vnd Meister*, odstraněno záhlaví a kustod `Teut-`. |
| `1-005r` | 5r | 19 | 7 | 0 | `pokracovani: true`, nadpis `uroven: 2` (`Der Teutschen Kriegsrüstung zu Roß vnd fůß.` – v OCR chybně `Deutschen`), doplněna iniciála `DIe`, opravy OCR (`Kriegsregirung`, `erkenne`, `die wal`, `bracht`), odstraněno záhlaví, tužkové `6`, folio `5` a kustod `gůt`. |
| `1-005v` | 5v | 20 | 8 | 1 | `pokracovani: true`, podnadpis `uroven: 3` (`Souil das fuß volck betrifft.`), doplněny iniciály `SO` a `DIe`, opravy OCR (`Nation`, `einige` bez duplicity `befinde`, `auß`, `kriegen`, `stettige`, `am tag`, `20000.`, `100000.`), poznámka `[^1]` k počítání jezdců na *Pferde*, odstraněno záhlaví a kustod `kriegs`. |
| `1-006r` | 6r | 21 | 2 | 2 | `pokracovani: true`, opravy OCR (`entplöst`, `jetzund`, `geschütz`, `einn`, `Chůr`, `vff`, `Sammet`, doplněno lomítko `7. Jar/`), poznámky `[^1]` (Konrád I. a Jindřich I. Saský) a `[^2]` (*zwei gůter mit rüstung*), odstraněno záhlaví, tužkové `7`, folio `6` a signatura `B`. |
| `1-006v` | 6v | 22 | 3 | 2 | `pokracovani: true`, opravy OCR (`mit`, `Lackeien`, `geritten`, `angehabt`, `kössen`, `Feld`, `tantz`, `mißfallen`), poznámky `[^1]` (*Junckern*) a `[^2]` (*Roßkeme raumeisen* vs. pantofle/kartáč/polštářek), odstraněno záhlaví a kustod `gůtem/`. |
| `1-007r` | 7r | 23 | 7 | 0 | `pokracovani: true`, opravy OCR (`Kriegßleuten`, `hergebrachten`, `Weiter`, `Harnisch`, `schwermerei`, `Kriegßampter`), rozděleno na 7 odstavců, odstraněno záhlaví, tužkové `8`, folio `7` a signatura `B ij`. |
| `1-007v` | 7v | 24 | 5 | 1 | `pokracovani: true`, doplněna iniciála `DVrchleuchtigster`, opravy OCR (`besetze`, `haß`, `Großmechtigster`, `Franckrich`, `Neapolis`, `Römische`, `geliebter`), poznámka `[^1]` k císaři Karlu V., odstraněno záhlaví, šum `000` a kustod `vnd`. |
| `1-008r` | 8r | 25 | 5 | 3 | `pokracovani: true`, opravy OCR (`Maiestat`, `Kriegßstück`, `den`, `gnaden`, `beschreibung`), ponechány tiskové odchylky `allergedigst`, `nit mehr/ wie sich gebürt/ Arbeit halben)` a `nit gůt thun werden` s poznámkami `[^1]`–`[^3]`, odstraněno záhlaví, tužkové `9`, folio `8` a signatura `B iij`. |
| `1-008v` | 8v | 26 | 6 | 1 | `pokracovani: true`, doplněna iniciála `DIeweil`, opravy OCR (`vnnd`, `sollen`, `jhre`, `Meuterei`, `der jrthumb`), ponecháno tiskové `aufferganene` s poznámkou `[^1]`, odstraněno záhlaví a kustod `vnd`. |
| `1-009r` | 9r | 27 | 5 | 0 | `pokracovani: true`, opravy OCR (`Kriegßuolck`, `Kriegßherrn`, `Kriegßuerstendigen`, `bei`, `vil`, `ist`, `zubeuelhen`), odstraněno záhlaví, tužkové `10`, folio `9` a signatura `B iiij`. |
| `1-009v` | 9v | 28 | 4 | 0 | Nový odstavec (bez `pokracovani`), nadpis `uroven: 2` (`Kriegs Ordnung.`), doplněna iniciála `DIeweil`, opravy OCR (`gemůt`, `verstandt`, `finantz`, `prouiantiern`, `gebrantschatzt`, `mit`), odstraněno záhlaví a kustod `schlecht/`. Rozdělené slovo `vnder-` přesunuto celé (`vnderschlecht`) na `1-010r` (již v Dávce 2). |

---

## 2. Významné opravy OCR ověřené ze skenů (`s010.jpg`–`s028.jpg`)

- **Doplněné ozdobné iniciály kapitol a oddílů**:
  - `1-002r` (`s013`): `Vrchleuchtigster` → `DVrchleuchtigster`
  - `1-003r` (`s015`): `Je weil` (2×) → `DIe weil` (2×)
  - `1-004v` (`s018`): `As aber` → `DAs aber`
  - `1-005r` (`s019`): `Je Teutschen` → `DIe Teutschen`
  - `1-005v` (`s020`): `befinde befinde…` (chyběla celá iniciála `SO`) → `SO befinde`; `Ote` → `DIe`
  - `1-007v` (`s024`): `Vrchleuchtigster` → `DVrchleuchtigster`
  - `1-008v` (`s026`): `Jeweil die` → `DIeweil die`
  - `1-009v` (`s028`): `Jewell die` → `DIeweil die`
- **Zásadní opravy smyslu v OCR**:
  - `1-002r` (`s013`): `G20 / 3mechtigsten` → `Großmechtigsten`; `Lukenbung` → `Lützenburg`; `Scelandt` → `Seelandt`; `Osterzeichischen` → `Osterreichischen`; `dieweilon zweiffeil` → `dieweil on zweiffel`.
  - `1-002v` (`s014`): `Matthridate` → `Mitthridate`; `ziwerondzwengig` → `zweivndzwentzig`; `Deiner` → `Diener`; `zusehen` → `zusetzen`; `Za Golms / MinEenberg` → `zu Solms / Müntzenberg`.
  - `1-003r` (`s015`): `Ketserlich Matestat` → `Keiserlich Maiestat`; `Nomern` → `Römern`; `vud` → `vnd`.
  - `1-003v` (`s016`): `am gebrauch` → `im gebrauch`; `Keafern` → `Keisern`; `pann` → `dann`; `Pollicet` → `Pollicei`; `Ind` → `Vnd`.
  - `1-004r` (`s017`): `wården…` (přeskočený řádek v OCR) zařazeno přesně podle sazby tisku; `liga` → `gewaltig.`
  - `1-004v` (`s018`): `Cro-Pnica` → `Cronica`; `fakt` → `satzt`; `feift` → `sein`; `lich` → `lieb`; `crholt` → `erholt`.
  - `1-005r` (`s019`): `Der Deutschen` → `Der Teutschen`; `Poracht` → `bracht`; `erkefne` → `erkenne`; `bie wal` → `die wal`.
  - `1-005v` (`s020`): `Ration` → `Nation`; `befinde befinde` → `SO befinde`; `auff dem Teuschlandt` → `auß dem Teutschlandt`; `frettige` → `stettige`; `im tag` → `am tag`.
  - `1-006r` (`s021`): `jekund` → `jetzund`; `geschuß` → `geschütz`; `Chür` → `Chůr`; `vff` (ne `off`); `Gammet` → `Sammet`.
  - `1-006v` (`s022`): `geraten` → `geritten`; `ange habe` → `angehabt`; `köffen` → `kössen`; `in das Geld` → `in das Feld`; `zu dem dank` → `zu dem tantz`; `mußfallen` → `mißfallen`.
  - `1-007r` (`s023`): `Harmsch` → `Harnisch`; `schwermeret` → `schwermerei`; `Kriegpampter` → `Kriegßampter`.
  - `1-007v` (`s024`): `besexe` → `besetze`; `G20st-mechtigster` → `Großmechtigster`; `Reapolis` → `Neapolis`; `Admische` → `Römische`; `gelichter` → `geliebter`.
  - `1-008r` (`s025`): `Kriegpstick` → `Kriegßstück`; `guaden` → `gnaden`; `Beschreibung` → `beschreibung`.
  - `1-008v` (`s026`): `Bonnd` → `vnnd`; `shre` → `jhre`; `Neuterei` → `Meuterei`; `ber jrthumb` → `der jrthumb`.
  - `1-009r` (`s027`): `wil` → `vil`; `aft` → `ist`; `zudeuelhen` → `zubeuelhen`.
  - `1-009v` (`s028`): `gemit` → `gemůt`; `verstande` → `verstandt`; `finank` → `finantz`; `nut gebürlicher` → `mit gebürlicher`.
- **Rozdělená slova přes přelom stran**:
  - `1-003r` → `1-003v`: `Be-` | `uelch/` → celé `Beuelch/` přesunuto na `1-003v` s `pokracovani: true`.
  - `1-009v` → `1-010r`: `vnder-` + kustod `schlecht/` | `schlecht/` → z `1-009v` odstraněno `vnder=` i kustod `schlecht/`; celé slovo `vnderschlecht/` je již v `1-010r` (Dávka 2).

---

## 3. Sporná místa (DE + CS) k posouzení

1. **`1-002r` – Titulatura Filipa II. (`König zu Engellandt… Printzen in Hispanien…`)**:
   - **DE**: `Dem Durchleuchtigsten/ Großmechtigsten Fürsten vnnd Herren/ Herren Philipsen König zu Engellandt/ Franckreich/ Neapolis/ Hierusalem etc. Printzen in Hispanien/ Ertzhertzog zu Ostereich…`
   - **CS**: `Nejjasnějšímu, nejmocnějšímu knížeti a pánu, panu Filipovi, králi Anglie, Francie, Neapole, Jeruzaléma atd., princi španělskému, arcivévodovi rakouskému…[^1]`
   - **Poznámka**: Ačkoli tisk nese letopočet `Anno/ 1559`, dedikační formule používá titulaturu Filipa II. z let 1554–1558 (manžela anglické královny Marie I. a tehdy ještě španělského prince před plným převzetím titulů španělského krále). Vysvětleno v poznámce `[^1]`.
2. **`1-002v`, `1-003r`, `1-003v`, `1-008r`, `1-008v` – Autentické tiskové odchylky ponechané v `de`**:
   - `1-002v`: `gnaden)` (osamocená pravá závorka bez levé závorky před *mit verleihung*); `wunderwarlichen` (za *wunderbarlichen*); `meinn Sönen` (*meinen Söhnen*).
   - `1-003r`: `nachtheilt` (za *nachtheil*).
   - `1-003v`: `ordunng` (přesmyčka za *ordnung*) a `bedach` (vypadlé *-t* u *bedacht*).
   - `1-008r`: `allergedigst` (vypadlé *-n-* u *allergnedigst*); `nit mehr/ wie sich gebürt/ Arbeit halben)` (lomítko místo levé závorky).
   - `1-008v`: `aufferganene` (vypadlé *-g-* u *auffergangene*).
3. **`1-008r` – `nit gůt thun werden`**:
   - **DE**: `…dieselbig zubeschirmen vnd vertheidigen/ vnd mit mehrer dieselbigen zu erweitern/ nit gůt thun werden.`
   - **CS**: `…je bude chránit a hájit, ba rozmnožovat a rozšiřovat a dobře to vykoná[^3].`
   - **Poznámka**: V kontextu slavnostní chvalořeči Filipu II. je zřejmé, že `nit gůt thun` je sazečská záměna *n/m* za *mit gůt thun* („se statky / dobře to vykonají“), příp. přehlédnutá záporka. Ponecháno v `de`, přeloženo kladně a vysvětleno v `[^3]`.
4. **`1-006r` – `zwei gůter mit rüstung`**:
   - **DE**: `so jetzt auff ein Pferdt gewant wirt/ daß mann wol zwei gůter mit rüstung daruon erhalten möchte`
   - **CS**: `jaké se dnes vynakládá na jediného koně, že by se z toho dali vydržovat snad dva dobří [koně] s výzbrojí[^2]`
   - **Poznámka**: Kontext proti *ein Pferdt* vede k významu „dva dobří [zbrojní koně] s výzbrojí“ (*zwei gute [Pferde] mit Rüstung*); zachyceno v poznámce `[^2]`.
5. **`1-006v` – `Roßkeme raumeisen`**:
   - **DE**: `haben die Buben Roßkeme raumeisen/ an jhren gürteln hangen`
   - **CS**: `nosívali pacholci {Buben} hřebílka a škrabáky na kopyta[^2] zavěšené u svých opasků`
   - **Poznámka**: Bezspojková dvojice termínů koňské péče (*Roßkämme* = hřebílka, *Räumeisen* = škrabáky/nože na čištění kopyt) v protikladu ke zhýčkaným *Panttoffel, Kerbörsten vnd ein Sammeten kössen* (pantofle, kartáč na šaty a sametový polštářek).

---

## 4. Návrhy do glosáře (`knihy/solms-1559/glosar.yaml`)

### A. Nová hesla navrhovaná do glosáře

```yaml
- id: valecny-rad
  cs: válečný řád
  de:
  - Kriegsordnung
  - Kriegßordnung
  - Kriegs ordnung
  kategorie: pravo
  hledat:
  - válečn\w* řád
  pozn: Souhrn předpisů pro kázeň, správu, úřady a právo ve vojsku (vedle artikulního listu a bojového řádu).
```

### B. Nové pravopisné a pádové varianty do stávajících hesel (z `{Termín}` v Dávce 1)

- **`valecny-pan`**: přidat `Kriegs Herr`, `Kriegßhern`
- **`valecny-lid`**: přidat `Kriegs Leut`, `Kriegs leut`, `Kriegßleut`, `Kriegßleuten`
- **`pechota`**: přidat `fuß volck`
- **`jizda`**: přidat `Reissigen zeuge`, `Reisigen zeugs`
- **`strelec`**: přidat `schützen`
- **`pacholek`**: přidat `Buben`
- **`sik`**: přidat `hauffen`
- **`pluk`**: přidat `regiment`
- **`dela`**: přidat `geschütz`
- **`zbroj`**: přidat `rüstung`
- **`lezeni`**: přidat `legers`, `Legers`
- **`tazeni`**: přidat `zügen`
- **`soud`**: přidat `Justicien`, `Justitia`
- **`vzpoura`**: přidat `auffruhr`
- **`artikulni-list`**: přidat `Artickels brieffe`
- **`finta`**: přidat `finantz`
- **`zold`**: přidat `besoldung`
- **`vypalne`**: přidat `gebrantschatzt`
- **`rimska-rise`**: přidat `Römisch Reich`, `römischen Reichs`
