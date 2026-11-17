# Zpráva ze zpracování a vizuální kontroly – `knihy/solms-1559`, Třetí kniha, Dávka 4 (`3-032r`–`3-043v`)

Zpracováno všech **24 stran** Dávky 4 Třetí knihy Solmsova tisku (1559): `3-032r`–`3-043v` (skeny `315`–`338`). Všech 24 stran má nastaveno `stav: zkontrolovano` a `overeno_clovekem: false`; všechny texty `de` byly slovo po slovu ověřeny proti náhledům skenů `s315.jpg`–`s338.jpg` (a hraničním skenům `s314.jpg` a `s339.jpg`). Na stranách Dávky 4 se nevyskytují žádné dřevořezy ani tabulky; dvě rýmované skladby na `3-042r`–`3-042v` byly zpracovány jako bloky typu `verse`.

Ověření skriptem `python -I nastroje/over_strany.py knihy/solms-1559 3-032r 3-032v 3-033r 3-033v 3-034r 3-034v 3-035r 3-035v 3-036r 3-036v 3-037r 3-037v 3-038r 3-038v 3-039r 3-039v 3-040r 3-040v 3-041r 3-041v 3-042r 3-042v 3-043r 3-043v --prisne`:
- **24 stran, 0 chyb, 4 varování** (všechna 4 varování jsou falešně pozitivní shody regexu na platném dobovém slově *fein* – „pěkně, jemně, hladce“ na `3-034v`, `3-037r`, `3-038v` a `3-042v`, vizuálně potvrzeném ve skenech).

---

## 1. Přehled stran, foliace a hlavních změn

Foliace lícních stran (`32` až `43`) byla na všech skenech vizuálně ověřena – **číslování listů v tisku je v celém rozsahu `32`–`43` bezchybné** (čísla `59` na `3-039r` a `48` na `3-041r` v BSB OCR byla pouhou chybou rozpoznání frakturních číslic `39` a `41`).

| Strana | List (sken) | Stav | Bloky | Pozn. | Hlavní úpravy a obsah |
|---|---|---|---:|---:|---|
| `3-032r` | `32` (`s315`) | `zkontrolovano` | 2 | 2 | `pokracovani: true` ze `3-031v`; opravy `daß mann`, `Möser` (ponecháno s `[^2]`), `geschüt`, `ist besser`, `war` (`[^1]`), `wöllen`; odstraněno záhlaví, folio `32` a signatura `Ff ij`. |
| `3-032v` | `32` (`s316`) | `zkontrolovano` | 7 | 2 | `pokracovani: true`; rozděleno na 7 odstavců dle tisku; `Kardetschen` přeloženo kontextově jako `prachová patrona` (`[^1]`); rozdělené `Pul-uer` přesunuto na `3-033r`; odstraněno záhlaví a kustod `uer`. |
| `3-033r` | `33` (`s317`) | `zkontrolovano` | 4 | 1 | `pokracovani: true` se slovem `Puluer`; opravy `Tonnen` (ne `Donnen`), `ferr`, `außgefüllt`; poznámka `[^1]` ke konstrukci prachové komory starých moždířů; odstraněno záhlaví, `33` a `Ff iiij`. |
| `3-033v` | `33` (`s318`) | `zkontrolovano` | 4 | 2 | Oddíl `uroven: 2` *Von Feurwerck.*; 6řádková iniciála `DIeweil`; odstraněno zdvojené `der` před `Apotecken`; poznámky `[^1]` (*Matrealien*) a `[^2]` (*sindt* za *findt*); odstraněno záhlaví, šum `000` a kustod `Nun`. |
| `3-034r` | `34` (`s319`) | `zkontrolovano` | 12 | 2 | Podnadpis `uroven: 3` + 11 receptů na plnicí směsi; 4řádková iniciála `ITem`; opravy `stücklin`, `ein ander`, `Gloriet` (`[^1]`), `Gummi Tragentum` (`[^2]`), `Inschlet`; odstraněno `000`, záhlaví a folio `34`. |
| `3-034v` | `34` (`s320`) | `zkontrolovano` | 6 | 1 | `pokracovani: true`; podnadpis `uroven: 3` a iniciála `DAs`; opravy `mit einem teil`, `hälßlin` (ne `hd plin`), `strick es`, `däffe`/`däff` (`[^1]`); rozdělené `geschri-ben` přesunuto na `3-035r`. |
| `3-035r` | `35` (`s321`) | `zkontrolovano` | 6 | 4 | `pokracovani: true` se slovem `geschriben`; opravy `schnürgebendt`, `Rörn` (ne `Körn`), `schnallen` (`[^2]`); poznámky `[^1]` (*Ein halb Kugel* za *hol Kugel*), `[^3]` (*schrieben*), `[^4]` (*Büchen* za *Büchsen*). |
| `3-035v` | `35` (`s322`) | `zkontrolovano` | 2 | 2 | `pokracovani: true`; opravy `an` (ne `on`), `anzinden`, `Puluer`, `Rör`, `vilfeltig`, `zint`; poznámky `[^1]` (*nit mehr anzindt*) a `[^2]` (*jhre geberden*); rozdělené `sprin-gete` přesunuto na `3-036r`. |
| `3-036r` | `36` (`s323`) | `zkontrolovano` | 3 | 1 | `pokracovani: true` se slovem `springete`; podnadpis `uroven: 3` + iniciála `ITem`; poznámka `[^1]` (*schmem* za *schwemm*); rozdělené `la-den` přesunuto na `3-036v`; odstraněno `00085168`, záhlaví, `36` a `Gg`. |
| `3-036v` | `36` (`s324`) | `zkontrolovano` | 9 | 2 | `pokracovani: true` se slovem `laden`; recepty na zápalné šípy rozděleny do 8 odstavců dle tisku; opravy `stein Kugel`, `nit`, `Colofamia` (`[^2]`); poznámka `[^1]` (`3. lang`). |
| `3-037r` | `37` (`s325`) | `zkontrolovano` | 5 | 2 | `pokracovani: true`; hlavní nadpis `uroven: 2` *Volgt ein ander Rüstung von Feurwerck/ zu einem Surm gehörig.* (`[^2]`), 7řádková iniciála `FVr`; poznámka `[^1]` (*Hirten teil* za *virten/dritten teil*); odstraněno `00085100`, `37` a `Gg ij`. |
| `3-037v` | `37` (`s326`) | `zkontrolovano` | 7 | 1 | 3 podnadpisy `uroven: 3` + iniciály `ITem`; opravy `bäumb` (ne `baums`), `Tonnen` (ne `Donnen`), `Ror` (ne `Xor`), `zerschlecht`; poznámka `[^1]` (*in den sack vnden*). |
| `3-038r` | `38` (`s327`) | `zkontrolovano` | 3 | 1 | `pokracovani: true`; podnadpis `uroven: 3` *Ein Bechring zumachen.* + iniciála `ITem`; oprava `Rörn` (ne `Körn`), `stürmen`, `Ring`; poznámka `[^1]` (*strohlams*); odstraněno záhlaví, `38` a `Gg iij`. |
| `3-038v` | `38` (`s328`) | `zkontrolovano` | 5 | 0 | 2 podnadpisy `uroven: 3` + iniciály `DEr`, `NIm`; opravy `Rörn` (ne `Körn`), `in ein`, `zündts`, `auß gehn`; odstraněno záhlaví a kustod `zeug`. |
| `3-039r` | `39` (`s329`) | `zkontrolovano` | 5 | 5 | `pokracovani: true`; ověřeno folio `39` (OCR četlo `59`); oddíl `uroven: 2` *Volgen die Apoteckischen Feur…* s 6řádkovou iniciálou `DIeweil`; Marcus Graecus (`[^1]`); ověření latinských látek (`[^2]`–`[^5]`); odstraněno `Gg iiij`. |
| `3-039v` | `39` (`s330`) | `zkontrolovano` | 8 | 6 | 4 podnadpisy `uroven: 3` + 4× iniciála `NIm`; zásadní opravy latinských názvů ze skenu (`Medule canne ferule`, `anatis`, `Balsam Olei.`, `Olei. Sulfur`, `etc.` místo `32.`/`22.`); poznámky `[^1]`–`[^6]`. |
| `3-040r` | `40` (`s331`) | `zkontrolovano` | 6 | 6 | 3 podnadpisy `uroven: 3` + 3× iniciála `NIm`; opravy `Lauri`, `Rör`, `einn Filtz`, `hitzige`; poznámky `[^1]`–`[^6]` k latinským látkám, Alexandrovi a Vergiliovi. |
| `3-040v` | `40` (`s332`) | `zkontrolovano` | 9 | 4 | 5 podnadpisů `uroven: 3` + iniciály `NIm`, `SO`; odstraněn šum `omni` z 1. nadpisu; opravy `Ollam`, `Regen`, `spißglaß`, `wann`; poznámky `[^1]`–`[^4]`. |
| `3-041r` | `41` (`s333`) | `zkontrolovano` | 9 | 5 | Ověřeno folio `41` (OCR četlo `48`); iniciály `NIm`, `WIlt`; klíčová oprava římských číslovek `ij.` (2) místo `11.`, `Ana.` (`[^1]`), `vorn` (`[^2]`), `etc.` místo `x .`, `verbernt` (`[^5]`); odstraněno `00085168`. |
| `3-041v` | `41` (`s334`) | `zkontrolovano` | 6 | 4 | 3 podnadpisy `uroven: 3` + iniciály `NIm`, `SO`; klíčová oprava `Rinderene plater` (místo `Kinderene`), `buhartz` (`[^1]`), `mag` (`[^2]`), `einn pfeil`; poznámky `[^3]`–`[^4]`. |
| `3-042r` | `42` (`s335`) | `zkontrolovano` | 7 | 5 | `pokracovani: true`; 2 rýmované básně převedeny jako bloky `typ: verse` (20 + 16 veršů); opravy `Mirren` (ne `Mirzen`), `Bintzen` (ne `Ginsen`), doplněn první verš 2. básně ze skenu; rozdělené `da-rin` přesunuto na `3-042v`; odstraněno `Hh`. |
| `3-042v` | `42` (`s336`) | `zkontrolovano` | 9 | 2 | `typ: verse` (`pokracovani: true`, 5 veršů se slovem `darin`); oprava duplicitního `trucknet`, `öl` (ne `il`), `Puluer`, `Ircomedis` (`[^2]`), `Weiern`; rozdělené `Salpe-ter` přesunuto na `3-043r`. |
| `3-043r` | `43` (`s337`) | `zkontrolovano` | 10 | 3 | `pokracovani: true` se slovem `Salpeter`; ze skenu doplněny celé vypadlé řádky OCR v 5. a 9. odstavci (`lebendigen Kalch/ vnd 5. pfundt eier...`, `zwei teil lebendigen Schwefel...`), oprava `gummen Arabicum`, `Leinölen`; odstraněno `00085168` a `Hh ij`. |
| `3-043v` | `43` (`s338`) | `zkontrolovano` | 7 | 5 | 3 podnadpisy `uroven: 3` + 4× iniciála `ITem`; opravy `Tůchern`, `so leufft es`, `katzen` (`[^2]`); poznámky `[^1]`–`[^5]` (mj. *1. Centener zulöschen wachs*, *Calonefemia*, *eichen feur* za *eichen ror*). |

---

## 2. Významné opravy OCR ověřené ze skenů (`s315.jpg`–`s338.jpg`)

### Doplněné ozdobné iniciály
- `3-033v` (`s318`): `Jeweil` → `DIeweil` (6řádková iniciála)
- `3-034r` (`s319`): `Tem` → `ITem` (4řádková iniciála)
- `3-034v` (`s320`): `As` (zdvojené v OCR) → `DAs`
- `3-036r` (`s323`): `Tem` → `ITem`
- `3-037r` (`s325`): `Vr` → `FVr` (7řádková iniciála)
- `3-037v` (`s326`): `Tem` (3×) → `ITem`
- `3-038r` (`s327`): `FTem` → `ITem`
- `3-038v` (`s328`): `Er` → `DEr`, `Im` → `NIm`
- `3-039r` (`s329`): `Jeweil` → `DIeweil` (6řádková iniciála)
- `3-039v` (`s330`): `Im` (4. recept) → `NIm`
- `3-040r` (`s331`): `Im` (3. recept) → `NIm`
- `3-040v` (`s332`): `O man` → `SO man`
- `3-041r` (`s333`): `Ilt` → `WIlt`
- `3-041v` (`s334`): `O nim` (2×) → `SO nim`
- `3-042r` (`s335`): `O nim` → `SO nim`, `Jerinn` → `HIerinn`
- `3-042v` (`s336`): `Tem` (3×) → `ITem`
- `3-043r` (`s337`): `Tem` (4×) → `ITem`
- `3-043v` (`s338`): `Tem` (4×) → `ITem`

### Zásadní věcné opravy OCR (výběr)
- `3-033r` (`s317`) a `3-037v` (`s326`): `Donnen` / `donen` → `Tonnen` / `tonnen` („sudy“); na `3-037v` `sozero schlechts` → `so zerschlecht es`.
- `3-033v` (`s318`): odstraněno duplicitní `der` v `auß der Apotecken`, `oben` → `vben`.
- `3-034v` (`s320`): `mit einem zeil/` → `mit einem teil/`; `hd plin` → `hälßlin` („krček, hrdélko“); `trick es` → `strick es`.
- `3-035r` (`s321`): `schmürgebendt` → `schnürgebendt`; `Körn` → `Rörn`.
- `3-035v` (`s322`): `Xor` → `Rör`; `bilfeltig` → `vilfeltig`; `sint` → `zint`.
- `3-037v` (`s326`): `baums` → `bäumb`; `Xor` → `Ror`.
- `3-038r`–`3-039r` (`s327`–`s329`): soustavně opravováno `Körn` / `Xörn` → `Rörn` („trubice“).
- `3-039r` (`s329`): opraveno folio `59` → `39`; `Materalien` → `Materialen`; `Seyfhduten` → `Geyßhäuten` („kozí kůže“); `erteich` → `erreich`.
- `3-039v` (`s330`): `Medule lanne ferule` → `Medule canne ferule`; `anakis` → `anatis`; `Balsam Glen.` / `Glen. Sulfur` → `Balsam Olei.` / `Olei. Sulfur`; `32.` a `22.` → `etc.`.
- `3-040v` (`s332`): odstraněno `omni` za nadpisem *Ein ander Feur.*; `Xegen` → `Regen`.
- `3-041r` (`s333`): opraveno folio `48` → `41`; `x .` → `etc.`; římské číslovky `ij.` (= 2) opraveny z OCR `11.` (*Calcis viue ij. pfundt*, *vnnd ij. Salpeter*); `dat` → `dañ` (`dann`).
- `3-041v` (`s334`): `Kinderene plater` → `Rinderene plater` („hovězí měchýř“).
- `3-042r` (`s335`): `Mirzen` → `Mirren` („myrha“); `Ginsen` → `Bintzen` („sítina“); `Orci` → `Drei`; zcela zkomolený první verš druhé básně `Herinn solle gehoren in dicke kang bardurch than foll` opraven ze skenu na dva verše `HIerinn solle gehören wol/ | Ein dicke stang dardurch thůn soll/`.
- `3-042v` (`s336`): `Daber ge / cin .` → `dabei gesein.`; odstraněno zdvojené `trucknet`; `il von Steinsalt` → `öl von Steinsaltz`; `Puiuer` → `Puluer`; `Spuluer` → `Puluer`; `bombschlasgen` → `vmbschlagen`; `Frcomedis` → `Ircomedis`.
- `3-043r` (`s337`): **doplněny celé vypadlé řádky z OCR** v 5. odstavci (`Flebendigenasiharapkerete` / `nat` → `lebendigen Kalch/ vnd 5. pfundt eier vnd reibe den Kalch/ das`) a v 9. odstavci (`zwei teil lebendigen Schwefel/ vnd ein teil Salpeter/ daß reib vor`); `growen` → `gummen`; `Leucolen` → `Leinölen`.
- `3-043v` (`s338`): `soleuffres` → `so leufft es`; `Tuchern` → `Tůchern`.

---

## 3. Hraniční přechody dávky

### A. Přechod před dávkou: `3-031v` (`s314`) → `3-032r` (`s315`)
- **Stav přechodu**: Poslední řádek textu na `3-031v` (`s314.jpg`) končí nedokončenou větou `so deckt dieselbig erdt die ander helfft/ nemlich das halb` a pod sazbou vpravo stojí kustod `teil`.
- **Dělené slovo**: Přes hranici `3-031v` → `3-032r` **nepřechází žádné rozdělené slovo**.
- **Návaznost**: První blok na `3-032r` má nastaveno `pokracovani: true` a začíná slovy `teil in das Erdrich gesenckt/…` (česky: `dílu zapustí do země a druhou polovinu vyháže…`).

### B. Přechod za dávkou: `3-043v` (`s338`) → `3-044r` (`s339`)
- **Stav přechodu**: Poslední řádek textu na `3-043v` (`s338.jpg`) řádně končí tečkou (`vnd also angezindt geht von keinem windt auß.`). Pod sazbou vpravo stojí kustod `Wie`, jenž byl z `3-043v` odstraněn.
- **Dělené slovo**: Přes hranici `3-043v` → `3-044r` **nepřechází žádné rozdělené slovo**.
- **Návaznost**: Následující strana `3-044r` (`s339.jpg`) začíná novým samostatným nadpisem `Wie mann gut Feur pfeil soll anrichten vnd machen.`, proto na `3-044r` první blok nebude mít `pokracovani: true`.

### C. Přesuny rozdělených slov uvnitř Dávky 4
1. `3-032v` → `3-033r`: `Pul-uer` přesunuto celé na `3-033r`.
2. `3-034v` → `3-035r`: `geschri-ben` přesunuto celé na `3-035r`.
3. `3-035v` → `3-036r`: `sprin-gete` přesunuto celé na `3-036r`.
4. `3-036r` → `3-036v`: `la-den` přesunuto celé na `3-036v`.
5. `3-042r` → `3-042v`: `da-rin` (v posledním verši) přesunuto celé na `3-042v`.
6. `3-042v` → `3-043r`: `Salpe-ter` přesunuto celé na `3-043r`.

---

## 4. Sporná místa (DE + CS) a tiskařské odchylky předlohy

1. **`3-032v` – `Kardetschen` jako plátěná prachová patrona**:
   - **DE**: `Aber soll von einem Tůch ein gůt summa Kardetschen gemacht haben/ das alweg in einem sack des Mörsers ladung eingefast wer/ vnd wider zugeneht…`
   - **CS**: `Také má mít z plátna naděláno hojně prachových patron {Kardetschen},[^1] tak aby do každého váčku byla vložena dávka do moždíře a váček opět zašit…`
   - **Zdůvodnění**: Ačkoliv glosář překládá *Hagel* jako `kartáč` (hromadná střela z broků/kamínků, viz též `3-042r`: `Lad sie wie mann thůt dem Hagel`), výraz *Kardetsche* (z ital. *cartoccio*) zde označuje plátěný váček naplněný odměřenou výmetnou dávkou střelného prachu do moždíře – tj. prachovou patronu (kartuš).
2. **`3-032r` – `Möser` a `war`/`vermein`**:
   - Ponecháno v `de` jako autentické tiskařské odchylky (*Möser* bez *-r-* za *Mörser*, *war* za *wohin*, *vermein* za *vermeinen*), vysvětleno v `[^1]` a `[^2]`.
3. **`3-033v` – `sindt` a `Matrealien`**:
   - V tisku stojí `so er alles mehr sindt` (sazečská záměna *f* / *ſ* za *findt*) a `Matrealien` (*Materialien*); ponecháno v `de` s poznámkami `[^1]`, `[^2]`.
4. **`3-035r` – `Ein halb Kugel` a `Büchen`**:
   - Na přechodu `3-034v`/`3-035r` stojí *Ein halb Kugel*, avšak postup popisuje výrobu duté koule vysypané pískem (*so ist die kugel hol*), tedy zřejmě přeslech/obměna za *hol Kugel*; na konci `3-035r` stojí *Büchen* (vypadlé *-s-* za *Büchsen*).
5. **`3-037r` – `Hirten teil` a `Surm`**:
   - V textu stojí *mit einem Hirten teil eines weisen hartzs* (zjevný překlep za *virten* či *dritten* – „čtvrtý / třetí díl“) a v nadpisu *zu einem Surm gehörig* (vypadlé *-t-* za *Sturm*).
6. **`3-039r`–`3-043v` – Alchymicko-pyrotechnické názvy látek (Marcus Graecus aj.)**:
   - Solms přejímá německý překlad středověkých receptů (zejména *Liber ignium* Marka Řeka) se značně zkomolenými latinizovanými názvy: *Sandarial Purapur* (*sandaraca pura*), *Armonati liquidi* (*sal armoniacum / gummi ammoniacum liquidum*), *Architram Greci* / *Albitram* / *Alechimitram* (*alchitram*), *Limatura matris singularis* (*limaturae martis singulorum*), *Astrolalinum* (*astrolabium*), *Socytatella Albi Sarta*, *Ollam Collofemiam*, *Salutter*, *Ircomedis*, *Conuortet* / *Confurt* / *Confortet* / *Conforstetet*, *Calonefemia*. Všechny tvary byly ověřeny proti skenům, v `de` zachovány doslovně a vyloženy v poznámkách.
7. **`3-042r` – Veršované recepty a tiskové chyby (`Lieder`, `darduch`, `sie`)**:
   - Na `3-042r`–`3-042v` jsou oba rýmované recepty v tisku vysázeny do souvislého odstavce s lomítky a velkými písmeny na začátku veršů. Převedeny na bloky `typ: verse` (20 veršů prvního a 16 + 5 veršů druhého textu). V `de` ponechány tiskové odchylky `Lieder` (za *Liechter*, „svíce“), `darduch` (za *dardurch*) a `sie` (za *sei*) s poznámkami.
8. **`3-043v` – `1. Centener zulöschen wachs` a `in einem langen eichen feur`**:
   - V prvním receptu na `3-043v` stojí nadsazené či zkomolené `1. Centener zulöschen wachs` (srov. `3-041v` *ein vierteil wachs*); v předposledním receptu stojí sazečský omyl `in einem langen eichen feur` místo `in einem langen eichen ror` („v dlouhé dubové trubici“), jak ukazuje konec věty (*wo du daß Ror hinkerst*). Ponecháno v `de` a vysvětleno v poznámkách.

---

## 5. Návrhy do glosáře (`knihy/solms-1559/glosar.yaml`)

### A. Nová hesla navrhovaná do glosáře

```yaml
- id: prachova-patrona
  cs: prachová patrona
  de:
  - Kardetsche
  - Kardetschen
  - kardetschen
  kategorie: delostrelectvo
  hledat:
  - prachov\w* patron
  pozn: Plátěný váček s předem odměřenou a zašitou prachovou výmetnou náloží pro rychlé nabíjení moždíře či děla (z ital. cartoccio).

- id: smoleni
  cs: zápalná lázeň
  de:
  - däff
  - däffe
  - däffen
  - gedäfft
  - schmem
  - schmemen
  kategorie: delostrelectvo
  hledat:
  - zápaln\w* lázn
  - zápaln\w* potah
  pozn: Horno-německé „däffen“ (od täufen/taufen) – máčení či polévání ovázané ohnivé koule roztavenou směsí síry, smůly a pryskyřice.

- id: provazove-ovazani
  cs: provazové ovázání
  de:
  - schnürgebendt
  - schnürgebent
  - Gebendt
  kategorie: delostrelectvo
  hledat:
  - provazov\w* ovázán
  pozn: Síťovité ovinutí těla ohnivé koule pevnými šňůrami či provazy, jež brání roztržení náplně při výstřelu a zpevňuje vrstvy zápalného potahu.

- id: zapalny-sip
  cs: zápalný šíp
  de:
  - Feurpfeil
  - Feurpfeiln
  - Feur pfeil
  kategorie: delostrelectvo
  hledat:
  - zápaln\w* šíp
  pozn: Šíp či šipka opatřená váčkem se zápalnou směsí pro zapalování střech a dřevěných staveb z luku nebo kuše.

- id: ohniva-kocka
  cs: ohnivá kočka
  de:
  - katzen
  - feur Katzen
  kategorie: delostrelectvo
  hledat:
  - ohniv\w* kočk
  pozn: Dobový pyrotechnický název pro létající oheň či raketu klouzající po napnutém drátu (příp. kratochvilný i bojový běhoun).

- id: gloriat
  cs: benátský terpentýn
  de:
  - Gloriet
  - gloriat
  - Glaret
  kategorie: delostrelectvo
  hledat:
  - benátsk\w* terpentýn
  pozn: Gloriet (gloriat, glaret) – čištěná modřínová pryskyřice čili benátský terpentýn užívaný jako pojivo a hořlavina v pyrotechnice.

- id: kalafuna
  cs: kalafuna
  de:
  - Colofonia
  - Colofamia
  - Colofonie
  - Colofemie
  - Colifamia
  - Calofonie
  - Collofetam
  - Collofemiam
  kategorie: delostrelectvo
  hledat:
  - kalafun
  pozn: Řecká smůla (Colophonia, Griechisch Pech) – tvrdá pryskyřice používaná do zápalných směsí a prachových past.
```

### B. Chybějící pravopisné a pádové varianty stávajících hesel
- **`delostrelectvo`**: přidat `Artolorei`, `artolorei`
- **`mozdir`**: přidat `Mörsers`, `Möser`
- **`koule`**: přidat `kugeln`, `kugel`, `schlagende Kugeln`, `schlagenden Kugeln`
- **`ohniva-koule`**: přidat `Feurkugeln`, `feurkugel`
- **`prach`**: přidat `puluer`, `Büchsen Puluer`, `Büchsenpuluer`, `schießpuluer`, `Schießpuluer`, `Puluers`
- **`ledek`**: přidat `Salpeters`, `Salx Petrosi`, `Salutter`
- **`dela`**: přidat `geschütz`, `Büchs`, `Büchen`, `Büchßen`
- **`kartouna`**: přidat `Cartaunen`
- **`hadovnice`**: přidat `Schlangen`
- **`sance`**: přidat `schantz`, `Schantzen`
- **`sancovni-kos`**: přidat `Schantzkörb`
- **`lafeta`**: přidat `gefässen`
- **`kartac`**: přidat `Hagel`
- **`libra`**: přidat `pfund`, `pfundt`
- **`ctvrtka`**: přidat `vierling`, `Quertlin`
- **`stopa`**: přidat `Schůhen`
- **`mile`**: přidat `meil`
- **`maz`**: přidat `maß`
- **`lezeni`**: přidat `Leger`
- **`opevneni` / `Festung`**: (pokud ještě není heslo `pevnost`, lze doplnit pro `Festung` na `3-040v`)
