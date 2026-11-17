# Zpráva ze zpracování a vizuální kontroly – `knihy/solms-1559`, Třetí kniha, Dávka 1 (`3-erb-solms`–`3-009v`)

Zpracováno všech **21 stran** Dávky 1 Třetí knihy Solmsova tisku (1559): `3-erb-solms`, `3-titul`, `3-titul-v`, `3-001r`–`3-009v` (skeny `250`–`270`), včetně tří dřevořezů (`drevorez-250.jpg`, `drevorez-251.jpg`, `drevorez-252.jpg`). Všech 21 stran má nastaveno `stav: zkontrolovano` a `overeno_clovekem: false`; všechny texty `de` byly slovo po slovu ověřeny proti staženým skenům `s250.jpg`–`s270.jpg` (a přechod proti `s271.jpg`).

Ověření skriptem `python -I nastroje/over_strany.py knihy/solms-1559 3-erb-solms 3-titul 3-titul-v 3-001r 3-001v 3-002r 3-002v 3-003r 3-003v 3-004r 3-004v 3-005r 3-005v 3-006r 3-006v 3-007r 3-007v 3-008r 3-008v 3-009r 3-009v --prisne`:
- **21 stran, 0 chyb, 0 varování**.

---

## 1. Přehled stran a hlavních změn

| Strana | List | Sken | Stav | Bloky | Poznámky | Hlavní úpravy a obsah |
|---|---|---:|---|---:|---:|---|
| `3-erb-solms` | erb | 250 | `zkontrolovano` | 2 | 1 | Ponecháno `frontispis: true`, přeložen úvodní titul autora, doplněn popis `drevorez-250.jpg` a poznámka `[^1]` o Reinhardu ze Solmsu. |
| `3-titul` | titulní list 3. knihy | 251 | `zkontrolovano` | 3 | 0 | Doplněno `Das dritte Bůch.`, opraveno `Vortrefflichen`, `Herren`, `halten/ was er wissen`, `regiern`, `nützlich/ krefftig vnd hitzig wirt.`; druhý červenočerný blok *Deßgleichen…* oddělen jako `odstavec`; odstraněn falešný text `PLVS ALTRE`; doplněn popis `drevorez-251.jpg`. |
| `3-titul-v` | rub titulního listu 3. knihy | 252 | `zkontrolovano` | 1 | 0 | Prohlédnut `drevorez-252.jpg` a doplněn podrobný popis jezdce v plné plátové zbroji se signaturou `1545 HD` (Hans Döring). |
| `3-001r` | 1 | 253 | `zkontrolovano` | 8 | 0 | Nadpis `Das drit Buch von der Arcolorei.` (`uroven: 2`), iniciála `DIeweil`, odstavce rozděleny na 7 bloků přesně dle tisku; `versuch-` přesunuto celé na `3-001v`; odstraněno `00085166` a `Aa ij`. |
| `3-001v` | 1 | 254 | `zkontrolovano` | 3 | 0 | `pokracovani: true` se slovem `versuchten`; rozděleno na 3 odstavce; zásadní opravy OCR (`spil seltzam`, `nit erschrecken`); odstraněno záhlaví a kustod `Beuelch-`. |
| `3-002r` | 2 | 255 | `zkontrolovano` | 2 | 1 | `pokracovani: true`, 2 odstavce; opravy `nit gůt`, `zu lernen` (ne `lermen`), `anschläg`, `Rathschläg`; poznámka `[^1]` (*vngesichlichkeit*, *Rahthschlag*); odstraněno záhlaví, folio `2` a `Aa iij`. |
| `3-002v` | 2 | 256 | `zkontrolovano` | 2 | 2 | `pokracovani: true`, 2 odstavce; oprava `durch die vil Rathschläg erindert`; slovo `wöl-` přesunuto celé na `3-003r`; poznámky `[^1]` (*weiteterm*) a `[^2]` (*berathschlag*); odstraněno záhlaví a kustod `ten`. |
| `3-003r` | 3 | 257 | `zkontrolovano` | 2 | 1 | `pokracovani: true` se slovem `wölten`; 2 odstavce; opravy `ein sachen`, `nit wissen`, `sagen`, `jrr machen`; poznámka `[^1]` (*geschlicklicheit*); odstraněno `00085168`, záhlaví, folio `3` a `Aa iiij`. |
| `3-003v` | 3 | 258 | `zkontrolovano` | 2 | 1 | Nadpis `uroven: 2` (*Des Zeugmeisters ampt…*), iniciála `ES`; opravy `giessen`, `verstehe`, `HERREN`; poznámka `[^1]` (*Arcololei*, *gerodnet*); odstraněno záhlaví a kustod `soll`. |
| `3-004r` | 4 | 259 | `zkontrolovano` | 3 | 0 | `pokracovani: true`, podnadpis `uroven: 3` (*Was eins Zeugmeisters beuelch…*); opravy `Büchsenmeistern`, `nit ansehen`, `vor` (místo OCR `002`); odstraněno `00085188`, záhlaví, folio `4` a kustod `dañ`. |
| `3-004v` | 4 | 260 | `zkontrolovano` | 14 | 2 | `pokracovani: true` + 13 samostatných bodů (`Zum ersten`–`Zum dreizehenden`); opravy `Zum zehenden`, `eilfften`; poznámky `[^1]` (zdvojené *glaubhafftig*) a `[^2]` (*Feurwerck* v 9. bodě); odstraněno záhlaví a kustod `allwegen`. |
| `3-005r` | 5 | 261 | `zkontrolovano` | 8 | 1 | `pokracovani: true` + body 14–20; poznámka `[^1]` k závěru 17. bodu; odstraněno `00085168`, záhlaví, folio `5` a kustod `in`. |
| `3-005v` | 5 | 262 | `zkontrolovano` | 3 | 2 | `pokracovani: true` + body 21–22; opravy `nit ein kleins/ daß sie tregt`, `dañ`, `gůter`, `Fontieren`; poznámky `[^1]` (*fessen*) a `[^2]` (*Fontieren*); odstraněno záhlaví a kustod `Zum`. |
| `3-006r` | 6 | 263 | `zkontrolovano` | 6 | 3 | Body 23–27 + závěrečný odstavec; poznámky `[^1]` (*mit werckleut*), `[^2]` (*in 5. theil*) a `[^3]` (*quastitores vber schantzer*); odstraněno `00085188`, záhlaví, folio `6` a `Bb`. |
| `3-006v` | 6 | 264 | `zkontrolovano` | 1 | 2 | `pokracovani: true`; opravy `vrsachen` (ne `besathen`), `stück`, `besteht/`; poznámky `[^1]` (*Oberkeit*) a `[^2]` (*außgerich*); odstraněno záhlaví a kustod `desto`. |
| `3-007r` | 7 | 265 | `zkontrolovano` | 4 | 0 | `pokracovani: true`; rozděleno na 4 odstavce podle odsazení tisku; opravy `nimer`, `Beuelchsleut`, `Ämptern`, `kein`; odstraněno `00085168`, záhlaví, folio `7` a `Bb ij`. |
| `3-007v` | 7 | 266 | `zkontrolovano` | 3 | 1 | `pokracovani: true`, podnadpis `uroven: 3` (*Des Leutenants Befelch…*), iniciála `DEr`; opravy `stiffte`, `Schmiden`, `alle`; poznámka `[^1]` (*Salpeter* = ledkaři); odstraněno záhlaví a kustod `Er`. |
| `3-008r` | 8 | 267 | `zkontrolovano` | 8 | 0 | 1. odstavec bez `pokracovani` (předchozí strana končila tečkou), 3 podnadpisy `uroven: 3` (*Der Edelleut…*, *Der Zeugschreiber.*, *Der Büchsenmeister beuelch.*), doplněny iniciály `DIe`, `DEr`, `ITem`; odstraněno `00085188`, záhlaví, folio `8` a `Bb iij`. |
| `3-008v` | 8 | 268 | `zkontrolovano` | 6 | 1 | `pokracovani: true`, 3 podnadpisy `uroven: 3`, iniciály `DIe`, `IN`; poznámka `[^1]` (*kein* za *klein*); ověřen vlepený korekturní proužek na závěrečném nadpisu (`ren/ bedörffe.`); odstraněno záhlaví a kustod `Es`. |
| `3-009r` | 9 | 269 | `zkontrolovano` | 3 | 2 | Iniciála `ES`; rozděleno na 3 odstavce včetně doplněného závěrečného řádku z vlepeného opravného proužku (`Zum andern/ so mann dann also besonder personen hat/ so mag`), jenž v OCR zcela chyběl; poznámky `[^1]` (*persein*) a `[^2]` (korekturní proužek); odstraněno záhlaví a folio `9`. |
| `3-009v` | 9 | 270 | `zkontrolovano` | 2 | 0 | `pokracovani: true`, 2 odstavce; opravy `notturfft`, `dieselbigen`, `darfür stehen/`; odstraněno záhlaví a kustod `sie`. |

---

## 2. Významné opravy OCR ověřené ze skenů (`s250.jpg`–`s270.jpg`)

### Doplněné ozdobné iniciály
- `3-001r` (`s253`): `Jewcil` → `DIeweil`
- `3-003v` (`s258`): `S ist` → `ES ist`
- `3-007v` (`s266`): `Er Leutenant` → `DEr Leutenant`
- `3-008r` (`s267`): `Te Edelleut` → `DIe Edelleut`; `Er Zeugschreiber` → `DEr Zeugschreiber`; `Temdie ... I Leutenandt` → `ITem die ... Leutenandt`
- `3-008v` (`s268`): `Te werckleut` → `DIe werckleut`; `N diser` → `IN diser`
- `3-009r` (`s269`): `GS feind` → `ES seind`

### Zásadní věcné opravy OCR (výběr)
- `3-erb-solms` (`s250`): `Mingenburg / x .` + šum z dřevořezu → `Müntzenburg/ etc.`
- `3-titul` (`s251`): `Das dritte Bach` → `Das dritte Bůch.`; `Vo ? -` → `Vor-` (`Vortrefflichen/`); `Herzen` → `Herren`; `waserwaffen / vndwiccr` → `was er wissen/ vnd wie er`; `regtern` → `regiern`; `nişlich / krefftig vnd hilig wirt` → `nützlich/ krefftig vnd hitzig wirt.`; `PLVS ALTRE` odstraněno (text uvnitř dřevořezu).
- `3-001r` (`s253`): `Arcolorci` → `Arcolorei`; `schuk` → `schutz`; `beschteffen` → `beschiessen`; `Geschuk`/`Geschut`/`Geschus` → `Geschütz`; `Schwesel Kolen` → `Schwefel/ Kolen`.
- `3-001v` (`s254`): `pil felkamist` → `spil seltzam ist/`; `mit erschrecken` → `nit erschrecken/`; `fortte` → `fortteil`; `verstonden` → `verstünden`; `bedeuche` → `bedeucht`.
- `3-002r` (`s255`): `mit gůt` → `nit gůt`; `zu lermen` → `zu lernen`; `gtht` → `gibt`; `anschlag` → `anschläg`; `Xathschlag` → `Rathschlag`; `Herin` → `Herrn`.
- `3-002v` (`s256`): `durch die wil Rathschlägerindert` → `durch die vil Rathschläg erindert`; `Daft` → `Dann`; `wie wil` (`wie wöl-`) → `wie wölten`.
- `3-003r` (`s257`): `einfachen` → `ein sachen`; `rathscha-gen` → `rathschlagen`; `geschukt` → `geschickt`; `jagen` → `sagen`; `jremachen` → `jrr machen`.
- `3-003v` (`s258`): `zuuerseyen` → `zuuersehen`; `greffen` → `giessen/`; `ver-frehe` → `verstehe/`.
- `3-004r` (`s259`): `Bachsenmeistern` → `Büchsenmeistern/`; `mit ansehen` → `nit ansehen`; `allezeit 002 den feinden` → `allezeit vor den feinden` (inkoustová skvrna na okraji přečtená jako `002`).
- `3-004v` (`s260`): `Sum zehenden` → `Zum zehenden`; `calfften` → `eilfften`; `nik ein` → `nit ein`.
- `3-005r` (`s261`): `Momtion` → `Monition`; `abentsich` (s čárkou) → `abents sich`.
- `3-005v` (`s262`): `nik ein kleins / dat siekregi` → `nit ein kleins/ daß sie tregt`; `Schnuden` → `Schmiden`; `Xenten` → `Renten`; `greffer` → `giesser`.
- `3-006r` (`s263`): `Xotmeister` → `Rotmeister`; `mt todt` → `nit todt`; `Zeugmeisten` → `Zeugmeister`; `verstehn.fol` → `verstehn sol/`.
- `3-006v` (`s264`): `besathen` → `vrsachen`; `stick` → `stück`; `besteht )` → `besteht/`; `dejta` (kustod) → `desto`.
- `3-007r` (`s265`): `mimer` → `nimer`; `geyn` → `gehn`; `Anmptern` → `Ämptern`; `keit lust` → `kein lust`; `Besuelchs cut` → `Beuelchsleut`.
- `3-007v` (`s266`): `fluffte` → `stiffte`; `cans Firsten` → `eins Fürsten`; `it alle jar` → `nit alle jar`; `alte sachen` → `alle sachen`; `foldem` → `sol dem`.
- `3-008r` (`s267`): `anfelich zug` → `ansehlich züg`; `Zengſchreiber` → `Zeugschreiber`; `flerfſig` → `fleissig`.
- `3-008v` (`s268`): `warten` → `warten vnnd`; `vo : rat` → `vorrat`; `Wicuil` → `Wieuil`.
- `3-009r` (`s269`): `tyt` → `ist`; `tarauff` → `darauff`; `Zeugmen-fter` → `Zeugmeister/`; **doplněn celý závěrečný řádek z vlepeného proužku** (`Zum andern/ so mann dann also besonder personen hat/ so mag`), jenž v `0269.txt` úplně chyběl.
- `3-009v` (`s270`): `nottufft` → `notturfft`; `dieselbto-gen` → `dieselbigen`; `darfürstehen` → `dafür stehen/`.

---

## 3. Hraniční přechod `3-009v` → `3-010r` (pro Dávku 2)

- **Stav přechodu**: Poslední řádek textu na `3-009v` (`s270.jpg`) končí slovy `was derhalben durch`. Pod sazbou vpravo stojí pouze samostatný kustod `sie`, jenž byl z `3-009v` odstraněn.
- **Dělené slovo**: Přes hranici `3-009v` → `3-010r` **nepřechází žádné rozdělené slovo**.
- **Návaznost věty**: Věta přechází neukončená z `3-009v` na `3-010r` (`s271.jpg`), která začíná slovy `sie alle verseumpt wirt/ er soll jn das auch sagen…`. První blok na `3-010r` proto v Dávce 2 musí dostat `pokracovani: true` (český závěr `3-009v`: `…za vše, co tedy skrze`, na což `3-010r` naváže `ně všechny bude zanedbáno…`).

---

## 4. Sporná místa (DE + CS) k posouzení

1. **`3-002r` – `vngesichlichkeit` a `Rahthschlag`**:
   - **DE**: `trinckens vnd andere vngesichlichkeit sich meiden vnnd enthalten`
   - **CS**: `vyhýbat se a zdržovat se pití i jiné nešikovnosti[^1]`
   - **Poznámka**: V tisku jde o zjevný sazečský překlep za *vngeschicklichkeit* (chybí *-ch-* a *-k-*); ponecháno v `de` s poznámkou `[^1]`.
2. **`3-002v` – `weiteterm` a `berathschlag`**:
   - **DE**: `…zu weiteterm nach dencken verursacht…` / `so dann also wirt Ordnung berathschlag`
   - **Poznámka**: Autentická zdvojená slabika a vypadlé koncové *-t* v tisku ponechány v `de`, vysvětleno v poznámkách `[^1]` a `[^2]`.
3. **`3-003r` – `geschlicklicheit`**:
   - **DE**: `…was für vernunfft/ geschlicklicheit vnd fleiß hinder einem jeden ist…`
   - **Poznámka**: Sazečské vložení *-l-* za *geschicklicheit* ponecháno v `de` s poznámkou `[^1]`.
4. **`3-003v` – `Arcololei` a `gerodnet`**:
   - **DE**: `…so kan er nicht wol berathschlagt vnnd gerodnet werden on die Arcolorei…`
   - **Poznámka**: Na téže straně se střídá *Arcolorei* a *Arcololei*, a v závěru je přesmyčka *gerodnet* (*geordnet*). Ponecháno v `de`, vysvětleno v `[^1]`.
5. **`3-004v` – Opakované `glaubhafftig` a `Feurwerck` v 9. bodě**:
   - **DE**: `Zum andern soll er glaubhafftig/ vnd nit ein trunckner Man sein. / Zum dritten soll er glaubhafftig sein.` / `Zum neunden soll er sich des Feurwerck verstehn/ damit er wisse sein geschütz mit dem vorzug zu ordnen…`
   - **CS**: Přeloženo věrně s poznámkami `[^1]` a `[^2]`; v 9. bodě je *Feurwerck* téměř jistě omylem za *Fuhrwerck* („vozba/přeprava děl“) či *Feldwerck*, neboť celý bod pojednává o pochodu s předvojem a vyprošťování děl z pole.
6. **`3-005v` – `Brettern zu den fessen der Büchsen` a `Fontieren`**:
   - **DE**: `als mit Brettern zu den fessen der Büchsen` / `inn seines Herrn Landt vnd Fontieren`
   - **CS**: `jako prkny na lafety {fessen}[^1] děl {Büchsen}` / `po celé zemi a pohraničí[^2] svého pána`
   - **Poznámka**: *fessen* je tvar bez předpony za *gefessen* (*Gefäßen*, lafety); *Fontieren* je dobová podoba franc. *frontière*.
7. **`3-006r` – `auch mit werckleut sindt`, `in 5. theil` a `quastitores vber schantzer`**:
   - **DE**: `dann so ein Zeugmeister gůt Büchsenmeister hat/ auch mit werckleut sindt/` … `vnd soll die 500. personn theiln in 5. theil/ das wern 20. person einen Rotmeister/` … `souil er dann der quastitores vber schantzer hat/`
   - **CS**: `kteří jsou zároveň řemeslníky[^1]` … `a těch 500 osob má rozdělit na 5 dílů, což činí 20 osob na jednoho rotmistra {Rotmeister}[^2]` … `kolik pak má kvastitorů {quastitores} nad šancíři[^3]`
   - **Poznámka**: Všech 500 : 20 = 25 (vypadlá číslice `2` v tisku); spojení `quastitores vber schantzer` i `auch mit werckleut sindt` vysvětleny v `[^1]`–`[^3]`.
8. **`3-006v` – `Oberkeit` místo *Erbarkeit* a `außgerich`**:
   - **DE**: `daß er sich der Oberkeit/ als trew/ glauben/ arbeit/ vnnd eins gůten wandels befleissen wöl` / `so soll ein Herr die Oberkeit der person ansehn`
   - **CS**: `co do počestnosti[^1] – totiž věrnosti, víry, pracovitosti a dobrých mravů` / `pohlédnout na počestnost té osoby`
   - **Poznámka**: Kontext výčtu ctností (*trew/ Glaub/ erbarkeit vnd arbeit* o několik řádků výše) jasně dokládá záměnu *Erbarkeit* → *Oberkeit*; vysvětleno v `[^1]`, vypadlé *-t* u *außgerich* v `[^2]`.
9. **`3-008v` a `3-009r` – `kein` (za *klein*), `persein` (za *person*) a vlepené opravné proužky**:
   - Na `3-008v` je spodní nadpis částečně tištěn na nalepeném proužku papíru a výše v textu je tisková chyba `kein` za *klein* (`[^1]`).
   - Na `3-009r` je v textu tisková chyba `persein` za *person* (`[^1]`) a poslední řádek strany (`Zum andern/ so mann dann also besonder personen hat/ so mag`) byl v originále doplněn na samostatně vlepeném proužku papíru (`[^2]`).

---

## 5. Návrhy do glosáře (`knihy/solms-1559/glosar.yaml`)

### A. Nová hesla navrhovaná do glosáře

```yaml
- id: utocne-naradi
  cs: útočné nářadí
  de:
  - Stormzeug
  - Sturmzeug
  kategorie: opevneni
  hledat:
  - útočn\w* nářad
  pozn: Obléhací a ztečové pomůcky (žebříky, berany, fošny, zápalné nástroje), které navrhuje a připravuje zbrojmistr.

- id: zemske-stavy
  cs: zemské stavy
  de:
  - Landtschafft
  - Landtsschafft
  kategorie: osoby
  hledat:
  - zemsk\w* stav
  pozn: Stavovské shromáždění země (rytířstvo, preláti, města), jež s knížetem schvaluje a financuje zemskou zbrojnici a válečné daně.
```

### B. Chybějící pravopisné a pádové varianty stávajících hesel (z `{Termín}` v této dávce)

- **`delostrelectvo`**: přidat `Arcolorei`, `Arcololei`
- **`zbrojmistr`**: přidat `Zeugmeisters`, `zeugmeister`
- **`podzbrojmistr`**: přidat `vnder Zeugmeister`
- **`munice`**: přidat `Monition`
- **`mozdir`**: přidat `Mörsern`
- **`ledek`**: přidat `Salpetter`, `Salpeter`
- **`zbroj`**: přidat `Kriegßrüstungen`, `rüstungen`, `rüstung`, `zurüstung`
- **`zved`**: přidat `kuntschafft`
- **`valecny-rada`**: přidat `Räthen`
- **`ohnostroj`**: přidat `Feurwerck`, `Feurwercken`, `Fewerwerck`
- **`sance`**: přidat `schantzens`, `Schantz`
- **`sancir`**: přidat `schantzer`, `quastitores`
- **`ranhojic`**: přidat `wundt artzten`
- **`koule`**: přidat `Kogeln`
- **`velitele`**: přidat `Befelchsleut`, `beuelchsleuten`
- **`dela`**: přidat `stück Büchsen`, `Stücken`
- **`vozka`**: přidat `Furleut`
- **`lafeta`**: přidat `fessen`
- **`tazeni`**: přidat `züg`, `zügen`
- **`zavazek`**: přidat `pflicht`
