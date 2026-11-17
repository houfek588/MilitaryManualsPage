# Zpráva z překladu a vizuální revize – `knihy/solms-1559` (První kniha, Dávka 3: `1-020r`–`1-029v`)

Zpracováno všech **20 stran** (`1-020r`–`1-029v`, skeny `49`–`68`). Všech 20 stran má nastaveno `stav: prelozeno` a `overeno_clovekem: false`.

Ověření skriptem `python -I nastroje/over_strany.py knihy/solms-1559 1-020r … 1-029v --prisne`:
- **20 stran, 0 chyb, 1 varování** (`1-026r`, blok 5: falešně pozitivní varování na autentické německé příslovce *fein* ve vazbě *ein hauffen fein an sich hencken*, viz `s061.jpg` ř. 23).

---

## 1. Přehled změn po stranách

| Strana | List | Sken | Počet bloků | Poznámky | Hlavní úpravy podle skenů a obsah |
|---|---|---:|---:|---:|---|
| `1-020r` | 20r | 49 | 5 | 1 | Rozdělení 5 odstavců článků (14.–18. trestní artikul), opravy OCR (`auß dem Feld` místo `auff`, `zubesetzen` / `darbei setzen`, `Kriegßrecht`, `ritmeister`, rozep. `erkennt`), odstraněna signatura `D iij` a záhlaví. |
| `1-020v` | 20v | 50 | 8 | 2 | Rozdělení 8 odstavců (19.–24. artikul a závěrečné hodnocení německého soudnictví), opravy OCR (`Meutterei`, `Kriegßherrn`, `zwentzigsten`, `fliehen`, `vngůtem`, `biß`), odstraněn kustod `Dar=`, poznámky k meči a tisk. tvaru *puncken*. |
| `1-021r` | 21r | 51 | 5 | 1 | Rozdělení 5 odstavců o soudní knize (*Gerichßbůch*) a národním soudnictví, opravy OCR (`geschehenden`, `bei handen`, `vnderhaltung`, `Rath`, doplněné `/` před `kein Nation`), odstraněna signatura `D iiij`. |
| `1-021v` | 21v | 52 | 5 | 2 | Rozdělení 5 odstavců o jezdeckém soudu, opravy OCR (`SO dann`, `Reutter`, `herren`, `Kriegsräthen`, `Parthei`, `würd`), rozdělené slovo `Sen-\|tentz` přesunuto celé na `1-022r`, poznámky k *gerichs Rath* a formuli *hege / span oder ban*. |
| `1-022r` | 22r | 53 | 7 | 1 | `pokracovani: true` se slovem `Sententz`, rozdělení 7 odstavců (závěr soudnictví, přechod k proviantu a úřad proviantního pána), opravy OCR (`Veldober-ster`, `Kriegßuerstendigen`, `ein sach`, `hauptstück`), odstraněn kustod `auch`, poznámka s odkazy do Druhé knihy. |
| `1-022v` | 22v | 54 | 8 | 3 | `pokracovani: true`, rozdělení 8 odstavců (proviantní tržiště, volní dodavatelé, zmínka o Třetí knize o dělostřelectvu a zvláštní knize o podkopech), opravy OCR (`Prouiantherrn`, `od-der`, `ferrner`, `vnder Veldmarschalck`), odstraněn kustod `geordnet`. |
| `1-023r` | 23r | 55 | 6 | 3 | `pokracovani: true`, rozdělení 6 odstavců (pořádek v minci po letech 1552–1553, úvěrování u markytánů a vrubovky), opravy OCR (`Müntz`, `Holtzkerben`, `Kriegßherrn`, `Bůch`), odstraněn kustod `Reutern`, poznámky k *Patronen vnd visierungen*, *allhei* a *Holtzkerben*. |
| `1-023v` | 23v | 56 | 6 | 2 | `pokracovani: true`, rozdělení 4 odstavců + `nadpis` (`uroven: 2`: *Wie mann ein Leger schlagen soll.*) + úvod s ozdobnou iniciálou `DIeweil`, opravy OCR (`kösten`, `Rotmeister`, `können`, `Leger`), odstraněn kustod `Nemlich`. |
| `1-024r` | 24r | 57 | 4 | 3 | `pokracovani: true` (ř. 1 `Nemlich` bez odsazení), rozdělení 4 odstavců (úkoly čtyř úřadů při rozbíjení ležení), opravy OCR (`zubesetzen`, `stuck`, `fünfftzehen`), odstraněna signatura `E`, poznámky k *des dz*, *nit beschreiben* a nesouladu 15 vs. 12 bodů. |
| `1-024v` | 24v | 58 | 12 | 3 | `nadpis` (`uroven: 3`: *Zwelff puncten darauß ein Leger geschlagen sein wil.*) + 11 článků ležení (`odstavec`), opravy OCR (`schantzen`, `Büchsen`, doplněná `/`), odstraněn kustod `Zum`, poznámky k *gesechehen*, *gemachen vnd vergraben* a *freinen standt*. |
| `1-025r` | 25r | 59 | 15 | 0 | 12. článek ležení, 2 úvodní odstavce a 12 bodů agendy válečné rady (`odstavec`), opravy OCR (`nider setzen`, `souil`, `Commiß anzustellen`, `Müntz`), odstraněna signatura `E ij`. |
| `1-025v` | 25v | 60 | 5 | 1 | `odstavec` (`ALso seind…`), `nadpis` (`uroven: 2`: *Ein gebrauch vnd ordnung einer Wagenburg.*) a 3 odstavce s ozdobnou iniciálou `ES` (historické užití vozové hradby u Římanů, Čechů, Uhrů a Angličanů), opravy OCR (`ALso`, `Ein`, `schantzen`), odstraněn kustod `Warzu`. |
| `1-026r` | 26r | 61 | 6 | 0 | `nadpis` (`uroven: 2`: *Warzu ein Wagenburg zugebrauchen sein mag.*) a prvních 5 bodů užití vozové hradby s ozdobnou iniciálou `VOr`, opravy OCR (`vberrent`, `paß`, `vorziehens`), odstraněna signatura `E iij`. |
| `1-026v` | 26v | 62 | 6 | 1 | 6.–11. bod užití vozové hradby, opravy OCR (`möcht`, `zug`, `Meutterei`, `Rorschützen`), odstraněn kustod `bestelt`, poznámka k *Meutterei* ve smyslu zrady/žhářství. |
| `1-027r` | 27r | 63 | 6 | 1 | `pokracovani: true`, rozdělení 6 odstavců (zvláštní dělostřelecké a štítové vozy *Schirmwagen*), opravy OCR (`würden /`, `ein gebrauch`, `vnnd ge-brauchte`, `sollen`, `vff`), odstraněna signatura `E iiij`, poznámka k *Schirmwagen*. |
| `1-027v` | 27v | 64 | 4 | 4 | Rozdělení 4 odstavců (tažení vozové hradby a podřízenost žoldnéřských vozů mistru vozové hradby), opravy OCR (`darbei ich es allhie`), odstraněn kustod `Die=`, poznámky k *vor zwerg… streichen*, *in augenschein gerissen*, *soltwagen* a odkaz do Druhé knihy (`050r`–`052v`). |
| `1-028r` | 28r | 65 | 4 | 0 | Rozdělení 4 odstavců (kritika zasahování válečných komisařů do pravomoci vysokých úřadů), opravy OCR (`vnd etliche`, `Feldherrn`, `zuthůn`), odstraněn kustod `würde` a razítko `000851.68`. |
| `1-028v` | 28v | 66 | 5 | 1 | `pokracovani: true`, rozdělení 5 odstavců (vztah pána, komisařů a úředních osob), opravy OCR (`Ampts`, `Feldherr`, `Ampts personen`, `rath`, `jn`), odstraněn kustod `Practi=`, poznámka k *gebe*. |
| `1-029r` | 29r | 67 | 7 | 1 | `pokracovani: true`, rozdělení 7 odstavců (korupce a kupčení úřadů, varování před „pokojovými rady“ *stuben Räthen*), opravy OCR (`jre`, `dañ`, `vornemen`, odstraněno zdvojené `die` před `rath`), přesunuto rozdělené `Kriegs=\|räthen` na `1-029v`, poznámka k *stuben Räthen*. |
| `1-029v` | 29v | 68 | 4 | 1 | `pokracovani: true` se slovem `Kriegsräthen`, rozdělení 4 odstavců (odměňování a úcta úřadům), opravy OCR (`notturfft`, `nit` místo `mit`/`it`, `grössern`, `versehen /`, `gebrauch`, `gerůglich`), rozdělené `ha=\|ben` na konci přesunuto na `1-030r`, poznámka k *ampspersonen*. |

---

## 2. Významnější opravy OCR ověřené ze skenů (`s049.jpg`–`s068.jpg`) a švy dávky

### A. Ozdobné iniciály kapitol
- `1-023v` (`s056.jpg`): `Jewerldan` → **`DIeweil dann`** (šestiřádková dřevořezová iniciála `D` + `Ieweil`).
- `1-025v` (`s060.jpg`): `ist` → **`ES ist`** (šestiřádková dřevořezová iniciála `E` + `S`).
- `1-026r` (`s061.jpg`): `Or das erst` → **`VOr das erst`** (šestiřádková dřevořezová iniciála `V` + `Or`).

### B. Zásadní opravy smyslu a frakturních záměn v BSB OCR
- `1-020r` (`s049.jpg`): `gebarliche` → `gebürliche`; `auff dem Feld` → **`auß dem Feld`**; `darberseken` → `darbei setzen`; `verantwortungſtat` → `verantwortung stat`; `red . lich` → `redlich`; `erkeñt` → `erkennt`; `vierdhehenden` / `sechfehenden` / `achgehenden` → `vierdtzehenden` / `sechszehenden` / `achtzehenden`.
- `1-020v` (`s050.jpg`): `Neut terei` → **`Meutterei`**; `Kriegspheren` → `Kriegßherrn`; `zirengigsten` → `zwentzigsten`; `fhehen` → **`fliehen`**; `bizz` → `biß`; `vñ` → `vnd`; doplněna virgule `haß / Lermen`.
- `1-021r` (`s051.jpg`): `gestehenden` → **`geschehenden`**; `ber handen` → **`bei handen`**; `Gerichßbůch` ověřeno v tisku bez *t*; `onder Haltund` → **`vnderhaltung`**; `Xath` → `Rath`; doplněna virgule `gehorsam / kein`.
- `1-021v` (`s052.jpg`): `Go` → `SO`; `Regio-ment` → `Regiment`; `Gottes (` → `Gottes /`; `Parther` → **`Parthei`**; `nokturfft` → `notturfft`; `gerichs Rath` ověřeno v tisku bez *t*.
- `1-022r` (`s053.jpg`): `Veldober / ber` → **`Veldoberster`**; `Kriegßuerstengigen` → `Kriegßuerstendigen`; `einfach` → **`ein sach`**; `hauptstick` → `hauptstück`; `mañ` → `mann`; `vñ` → `vnd`.
- `1-022v` (`s054.jpg`): `Prouianther ? n` → `Prouiantherrn`; `roßod der` → **`roß odder`**; `ferrner` ověřeno; `schand erlangen` odděleno.
- `1-023r` (`s055.jpg`): `Wung` → **`Müntz`**; `allhei` ověřeno v tisku jako sazečská přesmyčka; `Holkkerben` → `Holtzkerben`; `Bnd` → `Vnd`.
- `1-023v` (`s056.jpg`): `koſſen` → **`kösten`**; `Notmeister` / `sem Kot` → `Rotmeister` / `sein Rot`; `Keutern` → `Reutern`; `köien` → `können`; `oberscheken` → `vberschetzen`.
- `1-024r` (`s057.jpg`): `zubestehen` → **`zubesetzen`**; `des dz` rozvedeno na `des daß` (s poznámkou); `stack` → **`stuck`**; `Die` → `die`.
- `1-024v` (`s058.jpg`): `jchanken` → `schantzen`; `Buchsen` → `Büchsen`; doplněny virgule `musten /`; ověřeny tiskové podoby `gesechehen` a `freinen standt`.
- `1-025r` (`s059.jpg`): `idersehen` → **`nider setzen`**; `soil` → `souil`; `Commifanzustellen` → `Commiß anzustellen`; `Mung` → `Müntz`.
- `1-025v` (`s060.jpg`): `Mfo` → **`ALso`**; `Gin` → **`Ein`**; `fil` ověřeno v tisku; `schanker` → `schantzen`.
- `1-026r` (`s061.jpg`): `oberent` → `vberrent`; `paz` → `paß`; `vorzichens` → `vorziehens`; `darfür` a `jn` ověřeny.
- `1-026v` (`s062.jpg`): `miche` → **`möcht`**; `{ ug` → **`zug`**; `Neutterei` → **`Meutterei`**; `Korschuren` → **`Rorschützen`**; doplněny virgule za `würde /`, `rein /`, `zurichten /`.
- `1-027r` (`s063.jpg`): `mancherlct` → `mancherlei`; `eifi` → `ein`; `würden )` → `würden /`; vypuštěné `vnnd` doplněno před `gebrauchte`; `follett` → **`sollen`**; `off` → `vff`.
- `1-027v` (`s064.jpg`): `darber ich es allhte` → **`darbei ich es allhie`**; `klerliocher` → `klerlicher`.
- `1-028r` (`s065.jpg`): odstraněno knihovní razítko `000851.68`; `ondetliche` → `vnd etliche`; `zuihan` → `zuthůn`; `Feldhern` (`Feldherꝛn`) → `Feldherrn`.
- `1-028v` (`s066.jpg`): `Amps` → `Ampts`; `persoñ` → `personen`; `raty` → `rath`; `in selber` → `jn selber`.
- `1-029r` (`s067.jpg`): `pre` → `jre`; `daft` → `dann`; `vomemen` → `vornemen`; odstraněno falešné zdvojení `die die rath` (ve skenu jen `die rath`).
- `1-029v` (`s068.jpg`): `nottursffst` → `notturfft`; `das ist mit` → **`das ist nit`** (zásadní obrat významu!); `ein solchs kleines it` → **`ein solchs kleines nit`**; `verfchens` → `versehen /`; `gebraucht` → **`gebrauch`**; `gerůglich` ověřeno.

### C. Švy na okrajích dávky a uvnitř dávky
- **Začátek dávky (`1-019v` → `1-020r`)**: `1-019v` (`s048.jpg`) končí tečkou (`…verschafft werden.`) a kustodem `Zum`. `1-020r` začíná novým odsazeným odstavcem (`Zum vierdtzehenden…`), bez `pokracovani: true`.
- **Vnitřní přesahy rozdělených slov**:
  - `1-021v` → `1-022r`: `Sen-|tentz` přesunuto celé na `1-022r` (`pokracovani: true`).
  - `1-029r` → `1-029v`: `Kriegs=|räthen` přesunuto celé na `1-029v` (`pokracovani: true`).
- **Konec dávky (`1-029v` → `1-030r`)**: Poslední řádek `1-029v` (`s068.jpg`) končí rozděleným slovem `ha=` (kustod `ben`), přičemž `1-030r` (`s069.jpg`) začíná `ben mögen /…`. Podle pravidel byl zbytek `ha` z `1-029v` odstraněn (strana končí `einen freien zugang`). **Při revizi `1-030r` v další dávce je třeba první blok označit `pokracovani: true` a začít celým slovem `haben mögen`.**

---

## 3. Sporná místa DE + CS a zachované odchylky tisku

1. **`1-020r` – `mit seinem Fendlein vnd Reuttern`**:
   - **DE**: `so einer auß dem Feld mit seinem Fendlein vnd Reuttern … abziehen würd`
   - **CS**: `odtáhl-li by někdo z pole se svým praporcem {Fendlein}[^1] a jezdci {Reuttern}`
   - **Zdůvodnění**: V 1. knize Solms místy používá *Fendlein* i pro jízdní jednotku (v 2. knize již odlišuje pěší *Fendlein* a jezdeckou korouhev *Fahne*). Ponecháno závazné `praporec` podle glosáře s vysvětlující poznámkou `[^1]`.
2. **`1-020r` / `1-021v` / `1-022r` / `1-028r` – `Feldoberster` a `oberster Feldherr`**:
   - Na `1-022r` Solms v sousedních odstavcích střídá *Veldoberster* a *Oberster Veldhauptman* pro tentýž nejvyšší polní úřad. V celé dávce sjednoceno na **`nejvyšší polní hejtman`** (`{Feldoberster}`, `{Obersten Veldhauptman}`), zatímco `oberster Feldherr` (`1-028r`, `1-028v`) přeloženo v souladu s `002v` jako **`nejvyšší polní pán`**.
3. **`1-021v` – `hege / span oder ban`**:
   - **DE**: `hege / span oder ban / wie mann das nach gebrauch vnd Keiserlichem gesetz … nennen mag`
   - **CS**: `že jej zahajuje, vyhlašuje a zapovídá[^2]`
   - **Zdůvodnění**: Tradiční staroněmecká formule slavnostního ustavení a ohraničení soudu (*Gericht hegen, spannen oder bannen*).
4. **`1-023v` / `1-024r` / `1-027v` – `Artoloreimeister`**:
   - V souladu s `glosar.yaml` (kde je již varianta `Artlereimeister` pod `zbrojmistr`) přeloženo jako **`zbrojmistr {Artoloreimeister}`** s poznámkou `[^2]` na `1-023v`.
5. **`1-024r` – `nit beschreiben` a `fünfftzehen` vs. `Zwelff puncten`**:
   - **DE**: `in dises Bůch vnd verzeichnuß des Kriegs anfangs Ordnung nit beschreiben / dann es ist das erst stuck … derhalben so wil ich etlich Artickel nemlich fünfftzehen anzeigen`
   - **CS**: `v této knize a zápisu o počátečním řádu války neopisovat zevrubně[^2] … totiž patnáct[^3]`
   - **Zdůvodnění**: Vzhledem k okolní větné stavbě (*souil die gelegenheit das geben vnnd leiden wil* + *dann es ist das erst stuck*) jde u *nit beschreiben* buď o elipsu („neopisovat zeširoka, uvést jen hlavní body“), nebo o tiskařský překlep za *mit beschreiben*; stejně tak oznamuje 15 článků, ale následující nadpis i výčet na `1-024v`–`1-025r` obsahují jen 12. Vše ponecháno v `de` a vyloženo v poznámkách.
6. **`1-024v` – `gesechehen`, `auch gemachen vnd vergraben`, `freinen standt`**:
   - Tiskové odchylky zachovány v `de` s poznámkami (`gesechehen` = *geschehen*, `freinen` = *freien*, `gemachen` = zřejmě *machen* či překlep za *vermachen*).
7. **`1-026v` – `Meutterei zurichten … daß die heimlich können angestecket werden`**:
   - Přeloženo `vzpouru či záškodnou zradu {Meutterei}[^1]`, protože kontext odkazuje nejen na vzpouru, ale i na tajné spiknutí a žhářství ve vesnicích.
8. **`1-027v` – `vor zwerg einzuziehen zu dem streichen`**:
   - Přeloženo `zatahují se tyto vozy napříč k bočnímu postřelování[^1]` (flankování štítovými vozy podél vozové hradby).
9. **`1-028v` – `gebe`, `1-029r` – `stuben Räthen`, `1-029v` – `ampspersonen`**:
   - Tiskové tvary ponechány v `de`; *stuben Räthen* přeloženo přiléhavě „pokojovými rady[^1]“ (úředníci bez polní zkušenosti).

---

## 4. Návrhy do glosáře (`knihy/solms-1559/glosar.yaml`)

### A. Nová hesla navrhovaná k doplnění

```yaml
- id: stitovy-vuz
  cs: štítový vůz
  de:
  - Schirmwagen
  kategorie: opevneni
  hledat:
  - štítov\w* v[ůo]z
  pozn: Speciální tříspřežní vůz vozové hradby s podélnou dřevěnou zástěnou a bočními stupátky, sloužící k rychlé přepravě a palebnému krytí střelců.

- id: proviantni-trziste
  cs: proviantní tržiště
  de:
  - Prouiantplatz
  - Prouiantpletzen
  - Proutant platz
  - Proutantpletzen
  kategorie: zold
  hledat:
  - proviantn\w* tržišt
  pozn: Vyhrazené a zvláštní ochranou (mírem) nadané místo vně ležení nebo v plukovním kvartýru, kam se sváží proviant k prodeji a oceňování.

- id: komisni-pan
  cs: komisní pán
  de:
  - Commißherrn
  kategorie: zold
  hledat:
  - komisní\w* pán
  pozn: Úředník pověřený dohledem nad komisem a zásobováním vojska vedle proviantního pána.

- id: vrubovka
  cs: vrubovka
  de:
  - Holtzkerben
  kategorie: zold
  hledat:
  - vrubov[ek]
  pozn: Dřevěná vrubová hůlka sloužící k záznamu dluhů vojáků za potraviny odebrané na úvěr od markytánů až do vyplacení žoldu.

- id: strelec-z-rucnice
  cs: střelec z ručnice
  de:
  - Rorschützen
  kategorie: jednotky
  hledat:
  - střel\w* z ručnic
  pozn: Pěší střelec vyzbrojený ručnicí (Handrohr), nasazovaný mj. k obraně vozové hradby.
```

### B. Solmsovské pravopisné a pádové varianty pro stávající hesla

- **`nejvyssi-polni-hejtman`**: doplnit `Feldoberster`, `Feldobersten`, `Veldoberster`, `Obersten Veldhauptman`, `oberst Feldherr`, `obersten Feldherrn`, `Feldherr`.
- **`polni-marsalek`**: doplnit `Veldmarschalck`.
- **`podmarsalek`**: doplnit `vnder Veldmarschalck`.
- **`zbrojmistr`**: doplnit `Artoloreimeister`.
- **`mistr-vozove-hradby`**: doplnit `wagenburgmeister`.
- **`delostrelectvo`**: doplnit `Artolorei`.
- **`dela`**: doplnit `geschütz`, `stucken`.
- **`hakovnice`**: doplnit `doppel Hacken`.
- **`falkona`**: doplnit `halb Falckonetlein`.
- **`stopa`**: doplnit `Schůchs`.
- **`jizda`**: doplnit `Reisigen zeuge`.
- **`strelec`**: doplnit `schützen`.
- **`valecny-lid`**: doplnit `Kriegßleuten`, `Volcks`.
- **`valecny-rada`**: doplnit `Kriegßrethen`, `Rath`.
- **`rytmistr`**: doplnit `Ritmeistern`.
- **`lezeni`**: doplnit `leger`, `Legers`.
- **`kvartyr`**: doplnit `Quartir`, `Quartirs`.
- **`straz`**: doplnit `wachten`.
- **`tazeni`**: doplnit `zug`, `zugs`, `zügen`.
- **`sik`**: doplnit `hauffen`.
- **`zadni-voj`**: doplnit `nachzug`.
- **`zbroj`**: doplnit `rüstung`.
- **`sance`**: doplnit `schantzen`, `beschantzen`.
- **`zold`**: doplnit `besoldung`.
- **`zavazek`**: doplnit `pflicht`.
- **`finta`**: doplnit `Finantzen`.
- **`vzpoura`**: doplnit `auffruhr`.
- **`pice`**: doplnit `Fütterung`, `fütterung`.
- **`losament`**: doplnit `losament`.
- **`soud`**: doplnit `Kriegßrecht`, `Reutter Recht`.
- **`hrdelni-vec`**: doplnit `peinliche sach`.
