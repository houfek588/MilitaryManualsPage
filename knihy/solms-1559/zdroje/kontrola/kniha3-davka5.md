# Zpráva ze zpracování a vizuální kontroly – `knihy/solms-1559`, Třetí kniha, Dávka 5 (`3-044r`–`3-055v`)

Zpracováno všech **24 stran** Dávky 5 Třetí knihy Solmsova tisku (1559): `3-044r`–`3-055v` (skeny `339`–`362`). Všechny strany byly slovo po slovu ověřeny podle náhledů skenů (`s339.jpg`–`s362.jpg`, plus hraniční skeny `s338.jpg` a `s363.jpg`), rozděleny 1 : 1 podle odstavců, nadpisů a veršovaných receptů tisku, doplněny o vynechané ozdobné iniciály, vyčištěny od chyb BSB OCR a netextových prvků (záhlaví *Von der Artolorei.* / *Das dritte Bůch /* / *Das drit Bůch /*, čísla listů, signatury `Hh iij`–`Kk ij`, kustody) a plynule přeloženy do češtiny podle `PRAVIDLA_PREKLADU.md` a `knihy/solms-1559/glosar.yaml`. Všech 24 stran má nastaveno `stav: zkontrolovano` a `overeno_clovekem: false`.

Ověření skriptem `python -I nastroje/over_strany.py knihy/solms-1559 3-044r 3-044v 3-045r 3-045v 3-046r 3-046v 3-047r 3-047v 3-048r 3-048v 3-049r 3-049v 3-050r 3-050v 3-051r 3-051v 3-052r 3-052v 3-053r 3-053v 3-054r 3-054v 3-055r 3-055v --prisne`:
- **24 stran, 0 chyb, 0 varování**.

---

## 1. Přehled změn po stranách

| Strana | List | Sken | Bloky | Poznámky | Hlavní úpravy podle skenů a překlad |
|---|---|---:|---:|---:|---|
| `3-044r` | 44r | 339 | 4 | 6 | 2 nadpisy `uroven: 3` + 2 odstavce, iniciála `SO`, zásadní opravy `3. lot` (OCR `z .`), `weltz` (`welk`), `filtz` (`fils`), `nehe` (`neye`), `spitzigen holtz`, ponecháno `vrnes glaß`, `schessest`, `breit`, odstraněno `Hh iij`. |
| `3-044v` | 44v | 340 | 9 | 7 | 5 nadpisů `uroven: 3` + 4 odstavce, iniciály `SO`, `NIm` (`Im`), doplněno `1.` před `lot Auripigmentum`, opravy `Reguligar`, `zwei pfundt`, `thů` (`khu`), `herzlich`, ponecháno `Minimum`, `Alsponicum`/`Aspalcum`, `gerechen`, odstraněn kustod `Thů`. |
| `3-045r` | 45r | 341 | 6 | 7 | 2 nadpisy `uroven: 3` + 4 odstavce, iniciály `THů` (`Hudem`), `SO` (`Smach`), opravy `in soltu` (OCR `dar \| i soltu`), `thů dann` (`khir`), `löchlein` (`lschlein`), `putz`, ponecháno `holtz` (za *hol*), `drei driteil`, `Gummi Armeniacum`, odstraněno `00085168` a `Hh iiij`. |
| `3-045v` | 45v | 342 | 10 | 4 | 5 nadpisů `uroven: 3` + 5 odstavců, iniciály `SO` (`Onim`), `ITem` (`Tem`), opravy `darauß` (`darauff`), `wie daumen` (`wie wie`), `stecke jn`, ponechána tisková chyba `Saluter` (*Salpeter*), odstraněn kustod `das`. |
| `3-046r` | 46r | 343 | 8 | 5 | `pokracovani: true`, 4 nadpisy `uroven: 3` + 4 odstavce, iniciály `NEme` (`Eme` / `PEme`), doplněno `1.` před `Koln`, opravy `brennt` (`krent`), `knet` (`knoß`), `ziehe`, `hartz`, `schwemb er`, odstraněn kustod `Item`. |
| `3-046v` | 46v | 344 | 9 | 2 | Nadpis `uroven: 2` (*Von Büchsen / Feurpfeiln...*) + 4 nadpisy `uroven: 3` + 4 odstavce, iniciály `ITem`, `WIlt` (velká dřevořezová iniciála `W`), `SOll`, `NAch`, opravy `Schwämm` (`Schw.din`), `Ror` (`Nor`), `hawet` (`hawek`), odstraněn kustod `So`. |
| `3-047r` | 47r | 345 | 6 | 2 | 3 nadpisy `uroven: 3` + 3 odstavce, iniciály `SO` (`Onim`), `WIltu` (`Iltu`), opravy `verdorben` (`verdorden`), `klötzen` (`kliyen`), `Creutzweiß`, odstraněn kustod `Wiltu`. |
| `3-047v` | 47v | 346 | 5 | 4 | 2 nadpisy `uroven: 3` + 3 odstavce, iniciála `SO`, opravy `mann` (`maß`), `federkil` (`federkid`), `nim` (`nun`), `denn` (`det`), `hecket`, ponecháno `heffliche`, `des nachs`, odstraněno falešné `000` a kustod `Wiltu`. |
| `3-048r` | 48r | 347 | 10 | 7 | 5 nadpisů `uroven: 3` + 5 odstavců, iniciály `NIm`, `SO`, `ISt` (`FSt`), `SO` (`Omach`), opravy `Tarras Büchsen` (`Larras`), `Auß` (`Dusz`), `so lad` (`so ad`), `außgenomen` (`aufgenomen`), ponecháno `mit` a `nimder sich der schafft zu schlecht`, odstraněno `Ii`. |
| `3-048v` | 48v | 348 | 6 | 5 | `pokracovani: true`, 3 nadpisy `uroven: 3` + 3 odstavce, iniciály `SO`, `LAd` (`Ad`), opravy `haußpfeil` (`haufspfeil`), `setz` (`feß`), `leg die schirfferling`, ponecháno `Lolen` (*holen*), `brandt` (*randt*), `gescherpffte scheiben`. |
| `3-049r` | 49r | 349 | 8 | 1 | `pokracovani: true` (slovo `spunt` z `3-048v`), 4 nadpisy `uroven: 3` + 4 odstavce, iniciály `LAd` (`Ad` / `SAß`), `NIm` (`Im`), opravy `Tarras` (`Tarzas`), `10. oder 11.`, `Richtscheidt` (`Nichtscheidt`), odstraněno `Ii ij`. |
| `3-049v` | 49v | 350 | 7 | 4 | 3 nadpisy `uroven: 3` + 4 odstavce, iniciály `SO`, `OB`, `LAd`, `NIm`, zásadní opravy **`in einer schwere`** (`meiner`), **`Eyerstein`** (`Syerstein`), **`wie die Eier`** (`wie die Bier`), `stangen` (`frangen`), `tieffer` (`treffer`), ponecháno `seiel vnnd Pupillen`, odstraněn kustod `denn`. |
| `3-050r` | 50r | 351 | 8 | 4 | `pokracovani: true`, ověřeno chybné číslo listu **`70`** v tisku (`list: '50'`), 4 nadpisy `uroven: 3` + 4 odstavce, iniciály `WIltu`, `NIm`, `EIn`, opravy `röres` (`rores`), `öl` (`dl`), `zündt`, odstraněno `Ii iij`. |
| `3-050v` | 50v | 352 | 6 | 3 | 3 nadpisy `uroven: 3` + 3 odstavce, iniciály `DAs` (`As`), `NIm`, opravy `kertzlein` (`kerplein`), `sähe` (`fåhe`), `holtzwerck` (`holewerck`), ponechána přesmyčka `jelgiche`, odstraněn kustod `Nim`. |
| `3-051r` | 51r | 353 | 10 | 4 | Ověřeno chybné číslo listu **`71`** v tisku (v OCR chybělo), 5 nadpisů `uroven: 3`, **2 bloky `typ: verse`** (2 verše a 16 veršů), 3 odstavce, doplněno vypadlé `SO` před `mann vor einer Stat`, odstraněno falešné `Vottitor`, `Ein Alembic` (`Em`), odstraněno `Ii iiij`. |
| `3-051v` | 51v | 354 | 9 | 6 | 4 nadpisy `uroven: 3` + 5 odstavců, iniciály `ITem`, `NIm`, `WIltu`, zásadní oprava **`gar nutz`** (`gar nak`), opravy `von holtz` (`von hole`), `ferr` (`fer`), `dann` (`dat`), odstraněn kustod `Wie`. |
| `3-052r` | 52r | 355 | 9 | 6 | Ověřeno chybné číslo listu **`72`** v tisku (OCR `92`), 4 nadpisy `uroven: 3`, **2 bloky `typ: verse`** (20 a 16 veršů noční střelby a samozápalného děla), 3 odstavce, iniciály `SO`, `EIn`, zásadní opravy **`kalckstein`** (`falsestein`), `Solt den` (`deft`), `baß sehen`, `jnßlet`, `Burras`, ponecháno `os` (*so*), `weiloch`, odstraněn kustod `Wie`. |
| `3-052v` | 52v | 356 | 7 | 3 | 4 nadpisy `uroven: 3` + 3 odstavce, doplněno vypadlé `SO` (2×) a iniciála `WIltu`, opravy `Sonnen` (`Sollen`), `auß` (`auff`), `Hauß` (`Hauff`), `nimpt` (`mmpt`), `erretten` (`erecteten`), ponecháno `gorß` a `feindtlichem warm`, odstraněn kustod `Wiltu`. |
| `3-053r` | 53r | 357 | 6 | 4 | 3 nadpisy `uroven: 3` + 3 odstavce, iniciály `WIltu` (`MIltu`), `NEme` (odstraněno duplicitní `N` před `Koln`), `NIm` (`PIm`), zásadní opravy **`verfeuchtlich`** (`versuchtlich`), `Camforis` (`Caniforis`), `Arsenicum`, `dörrs`, `vil` (`oil`), odstraněn kustod `Ist`. |
| `3-053v` | 53v | 358 | 6 | 4 | 3 nadpisy `uroven: 3` + 3 odstavce, iniciály `WIltu` (`MIltu`), `ES` (`GS`), opravy `vnd es sich` (`ondes sich`), `heiß sieden` (`herz`), `heng` (`yeng`), `geschirr` (`gefchar2`), ponecháno `Capetel` a `Salpartica`, odstraněn kustod `Wilt=`. |
| `3-054r` | 54r | 359 | 4 | 3 | Ověřeno chybné číslo listu **`74`** v tisku (OCR `94`), 1 nadpis `uroven: 3` + 3 odstavce, iniciála `WIltu` (`MIltu`), zásadní oprava **`schwefel nit`** (`schwefel me`), `zwillichen` (`zwallichen`), `Tůchlin`, ponecháno `Büchenpuluer`, `Isponicum`, odstraněno `Kk`. |
| `3-054v` | 54v | 360 | 7 | 5 | 3 nadpisy `uroven: 3` + 4 odstavce, iniciála `WAnn` (OCR `SE \| An`), iniciály `WIltu` (2×), `SO` (`O du`), opravy `Quart` (`Ouart`), `Camforis` (`Caniforis`), `nutz` (`nus`), ponecháno `gar böß`, `garbs`, `stettit`, `bricht`, odstraněn kustod `vnd`. |
| `3-055r` | 55r | 361 | 5 | 2 | `pokracovani: true`, 2 nadpisy `uroven: 3` + 3 odstavce, iniciály `DV` (`DB`), `WIltu` (`MIltu`), doplněno vypadlé `1.` v **`in 1. pfundt`**, opravy `steht` (`sicht`), `gantzen Alchimei` (`gangen Alchtmet`), odstraněno `Kk ij`. |
| `3-055v` | 55v | 362 | 8 | 2 | 4 nadpisy `uroven: 3` + 4 odstavce, iniciály `SO` (`Oleg`), `NIm` (`NInr`), `WIltu` (`MIltu`), opravy `denn` (`det`), `netz` (`new`), `zusatz`, `Zündtpuluer`, odstraněn kustod `Weiß`. |

---

## 2. Významné opravy OCR, kontrola foliace a veršované bloky (`s339.jpg`–`s362.jpg`)

### A. Kontrola skutečných čísel listů ve skenech
V tisku došlo v arších `Ii` a `Kk` k výraznému sazečskému omylu při foliaci (záměna desítkové číslice `5` za `7` na čtyřech lících, což OCR dále zkreslilo):
- **`3-050r` (`s351.jpg`)**: v záhlaví je chybně vytištěno **`70`** (namísto `50`).
- **`3-051r` (`s353.jpg`)**: v záhlaví je drobně vytištěno **`71`** (namísto `51`; v BSB OCR `0353.txt` úplně chybělo).
- **`3-052r` (`s355.jpg`)**: v záhlaví je chybně vytištěno **`72`** (namísto `52`; BSB OCR četlo `92`).
- **`3-053r` (`s357.jpg`)**: v záhlaví je správně vytištěno **`53`**.
- **`3-054r` (`s359.jpg`)**: v záhlaví je chybně vytištěno **`74`** (namísto `54`; BSB OCR četlo `94`).
- **`3-055r` (`s361.jpg`)**: v záhlaví je správně vytištěno **`55`**.

Ve všech souborech je zachováno správné ediční číslo listu (`list: '50'` až `'55'`) a tisková odchylka je zdokumentována v `poznamky` na `3-050r`, `3-051r`, `3-052r` a `3-054r`.

### B. Veršované poučky (`typ: verse`) na `3-051r` a `3-052r`
Ačkoliv tisk sází verše do souvislých řádků oddělených lomítky `/`, jde o zřetelně rýmovaná dvojverší se sdruženým rýmem (`aabbcc...`) a velkými písmeny na začátku každého verše. Podle `PRAVIDLA_PREKLADU.md` byly převedeny na bloky `typ: verse`:
- **`3-051r` (`s353.jpg`)**:
  - `Von Büchsen schiessen.` → **2 verše** (*Zweier handt du Puluer nimm / Das ist der rechten Meister sinn.*).
  - `Wie mann ein Büchs mit wasser ledt.` → **16 veršů** (*EIn höfflich kunst sich hie entschleust / ... Wiltu des ölens werden fro.*).
- **`3-052r` (`s355.jpg`)**:
  - `Wie mann zu nacht scheust / etc.` → **20 veršů** (10 sdružených rýmů o noční střelbě svítící koulí obalenou kůží, voskem, prachem, pryskyřicí, lojem a sírou).
  - `Büchs sich selbs anzündet.` → **16 veršů** (8 sdružených rýmů o děle zapalujícím se bez ohně reakcí nehašeného vápna s vínem).

### C. Zásadní věcné opravy OCR a doplněné iniciály (výběr)
- **Doplněné či opravené iniciály a vynechaná slova**: `3-044r` `SO nim`; `3-044v` `SO nim`, `NIm secklin`; `3-045r` `THů dem` (OCR `Hudem`), `SO mach` (`Smach`); `3-045v` `SO nim` (`Onim`), `ITem` (`Tem`); `3-046r` `NEme` (`Eme`/`PEme`); `3-046v` `ITem`, `WIlt` (velká zdobná iniciála `W`), `SOll`, `NAch`; `3-047r` `SO nim`, `WIltu`; `3-047v` `SO nim`; `3-048r` `NIm`, `SO fül`, `ISt` (`FSt`), `SO mach` (`Omach`); `3-048v` `SO lad` (`Olad`), `LAd` (`Ad`); `3-049r` `LAd` (`Ad`/`SAß`), `NIm` (`Im`); `3-049v` `SO merck`, `OB die` (`B die`), `LAd` (`Ad`), `NIm` (`Im`); `3-050r` `WIltu`, `NIm`, `EIn`; `3-050v` `DAs` (`As`), `NIm`; `3-051r` **`SO mann`** před `vor einer Stat` (v OCR zcela vypadlo), `EIn`; `3-051v` `ITem`, `NIm`, `WIltu`; `3-052r` `SO lade`, `EIn`, `SO thů`; `3-052v` **`SO du wilt`** (2× v OCR zcela vypadlo), `WIltu`; `3-053r` `WIltu`, `NEme` (odstraněno duplicitní `N` před `Koln`), `NIm`; `3-053v` `WIltu`, `ES` (`GS`); `3-054r` `WIltu`; `3-054v` **`WAnn`** (`SE | An`), `WIltu`, `SO du`; `3-055r` `DV` (`DB`), `WIltu`; `3-055v` `SO leg` (`Oleg`), `NIm`, `WIltu`.
- **Kritické opravy čísel a smyslu**:
  - `3-044r`: **`3. lot Schwefel`** (OCR `z . lot`), **`weltz`** (OCR `welk`), **`filtz`** (OCR `fils`).
  - `3-044v`: doplněno **`1.`** před `lot Auripigmentum`.
  - `3-045r`: **`darin soltu`** (OCR `dar | i soltu`), **`thů dann`** (OCR `khir dan`).
  - `3-046r`: **`1. Koln`** (OCR vynechalo `1.`), **`brennt`** (OCR `krent`), **`knet`** (OCR `knoß`), **`schwemb er`** (OCR `schwember`).
  - `3-046v`: **`Schwämm`** (OCR `Schw.din`), **`Ror`** (OCR `Nor`).
  - `3-047v`: **`die mann`** (OCR `die maß`), **`nim`** (OCR `nun`), **`denn`** (OCR `det`).
  - `3-048r`: **`Auß einer Tarras Büchsen`** (OCR `Dusz einer Larras`), **`so lad sie denn`** (OCR `so ad fie`), **`außgenomen`** (OCR `aufgenomen`).
  - `3-049v`: **`in einer schwere`** (OCR `meiner`), **`Eyerstein`** (OCR `Syerstein`), **`wie die Eier`** (OCR **`wie die Bier`**!).
  - `3-050r`: **`röres`** (OCR `rores`), **`Schwefel öl`** (OCR `dl`).
  - `3-051r`: odstraněno falešné `Vottitor`, opraveno **`Ein Alembic`** (OCR `Em`), **`lest`** (OCR `lefit`).
  - `3-051v`: **`gar nutz`** (OCR **`gar nak`**!), **`von holtz`** (OCR `von hole`).
  - `3-052r`: **`kalckstein`** (OCR **`falsestein`**!), **`Solt den`** (OCR `Solt deft`), **`baß sehen`** (OCR `baßschen`), **`os bricht sie`** (OCR `of bricht sie`).
  - `3-052v`: **`Sonnen`** (OCR `Sollen`), **`auß`** (OCR `auff`), **`erretten`** (OCR `erecteten`).
  - `3-053r`: **`verfeuchtlich`** (OCR `versuchtlich`), **`Camforis`** (OCR `Caniforis`), **`Arsenicum`** (OCR `Arfemcum`), **`vil weniger`** (OCR `oil weniger`).
  - `3-053v`: **`vnd es sich`** (OCR `ondes sich`), **`heiß sieden`** (OCR `herz sieden`).
  - `3-054r`: **`schwefel nit`** (OCR `schwefel me` – převrácený význam!), **`zwillichen`** (OCR `zwallichen`).
  - `3-054v`: **`Quart`** (OCR `Ouart`), **`Camforis`** (OCR `Caniforis`).
  - `3-055r`: doplněno **`1.`** v **`in 1. pfundt`** (v OCR vypadlo), **`gantzen Alchimei`** (OCR `gangen Alchtmet`).
  - `3-055v`: **`netz`** (OCR `new`), **`denn`** (OCR `det`).

---

## 3. Hraniční přechody dávky (`3-043v` → `3-044r` a `3-055v` → `3-056r`) a přechody uvnitř dávky

- **Před dávkou (`3-043v` → `3-044r`)**:
  - Sken `s338.jpg` (`3-043v`) končí ukončenou větou `vnd also angezindt geht von keinem windt auß.` a dole má kustod `Wie`.
  - Na `3-044r` (`s339.jpg`) začíná nová podkapitola nadpisem `Wie mann gut Feur pfeil soll anrichten vnd machen.`. Přes hranici stran nepřechází žádné rozdělené slovo ani nedokončená věta (`pokracovani: true` se proto nenastavuje).
- **Uvnitř dávky**:
  - `3-045v` → `3-046r`: `3-045v` končí `thůs alles in ein geschir` (kustod `das`), `3-046r` má `pokracovani: true` (`das lauter new vnd rein sei…`).
  - `3-048r` → `3-048v`: `3-048r` končí `das dieselben pörsten in`, `3-048v` má `pokracovani: true` (`demselben Lolen ligen…`).
  - `3-048v` → `3-049r`: `3-048v` končí `vorn für den` (kustod `spunt`), `3-049r` má `pokracovani: true` (`spunt / das sie wol anligendt…`).
  - `3-049v` → `3-050r`: `3-049v` končí `vnnd vermach es` (kustod `denn`), `3-050r` má `pokracovani: true` (`denn aber mit dem vorgeschriben leim…`).
  - `3-054v` → `3-055r`: `3-054v` končí `ein halb Centner salpeter bricht 30. pfundt schwefels /` (kustod `vnd`), `3-055r` má `pokracovani: true` (`vnd dreizehent halb pfundt Koln…`).
  - Ostatní přechody mezi stranami v dávce končí tečkou nebo nadpisem (kustody odstraněny).
- **Za dávkou (`3-055v` → `3-056r`)**:
  - Sken `s362.jpg` (`3-055v`) končí ukončenou větou `denn laß wol trucken werden.` a dole má kustod `Weiß`.
  - Sken `s363.jpg` (`3-056r`) začíná novým nadpisem `Weis Puluer sol mañ also machen.`. Žádné rozdělené slovo ani neukončená věta nepřechází (pro Dávku 6 není potřeba `pokracovani: true` na `3-056r`).

---

## 4. Sporná místa a tiskové chyby předlohy (DE + CS)

1. **`3-044r` – `vrnes glaß` a `breit` (za *bereit*)**:
   - **DE**: `vnd 2. Quintat vrnes glaß` / `so ist es breit`
   - **CS**: `a 2 kvintlíky {Quintat}[^1] čistého skla,[^2]` / `čímž je připraven.[^6]`
   - **Poznámka**: *vrnes glaß* je zřejmá zkomolenina za *reines*, *grünes* či *firnes* („čisté/zelené/staré“) sklo; *breit* pak překlep za *bereit*.
2. **`3-044v` – `Minimum`, `Alsponicum`/`Aspalcum`, `gerechen`**:
   - **DE**: `1. lot Alsponicum / 1. lot Minimum` / `ein guten gerechen Feurpfeil`
   - **CS**: `1 lot asfaltu (*Alsponicum*),[^3] 1 lot suříku (*Minimum*)[^4]` / `dobrý spolehlivý ohnivý šíp[^6]`
   - **Poznámka**: Drobné alchymicko-písařské zkomoleniny (z *Asphaltum*, *Minium*, *gerechten*) ponechány v `de` a vysvětleny v poznámkách.
3. **`3-045r` – `holtz` (za *hol*) a `drei driteil`**:
   - **DE**: `nim drei driteil kolen / ein dritteil schwefels` / `Item der schlachende pfeil soll holtz sein`
   - **CS**: `vezmi tři třetiny uhlí,[^5]` / `třaskavý šíp má být dřevěný [správně: dutý][^6]`
   - **Poznámka**: Zjevné tiskové/písařské omyly (tři díly/čtvrtiny uhlí; dutý *hol* oproti dřevěný *holtz*, protože následující věta hovoří o plnění dutiny šípu prachem).
4. **`3-045v` – `Saluter` a nejasný větný předěl**:
   - **DE**: `4. pfundt wolgeleuterten Saluter` / `vnd laß es vorn bei dem spitzen darnach den schwefel zulassen`
   - **CS**: `4 libry dobře přečištěného ledku {Saluter},[^4]` / `a potom se nechá rozpustit síra v kelímku, ponoří se do ní šíp u hrotu[^3]`
5. **`3-047v` – `heffliche` a `des nachs`**:
   - **DE**: `ein gar heffliche kunst wie ein Meister des nachs schiessen soll`
   - **CS**: `velmi znamenité umění,[^4] jak má mistr střílet v noci`
   - **Poznámka**: Tiskové chyby předlohy za *höffliche* a *des nachts*.
6. **`3-048r` – `je nimder sich der schafft zu schlecht` a `mit` v nadpisu**:
   - **DE**: `so vmb geuß die Form mit als groß sie sein soll.` / `je nimder sich der schafft zu schlecht`
   - **CS**: `oblej formu tak velikou, jaká má být[^4]` / `tím méně se dřík roztříští.[^7]`
7. **`3-048v` – `Lolen`, `mit dem brandt`, `gescherpffte scheiben`**:
   - **DE**: `in demselben Lolen ligen` / `senck es mit dem brandt hinein` / `ein gescherpffte scheiben`
   - **CS**: `v těchže žlábcích[^1]` / `zasuň ji okrajem[^3] dovnitř` / `okovanou[^5] desku`
8. **`3-049v` – `seiel vnnd Pupillen`**:
   - **DE**: `der mit seiel vnnd Pupillen fasst wol gebert sei`
   - **CS**: `která je důkladně zpracovaná s vlákny a příměsmi;[^4]`
9. **`3-050v` – `jelgiche` a rozpor nadpis/text (*Feurpfeil* vs. *stein*)**:
   - **DE**: `ein jelgiche Kugel` / `Wie mann Feurpfeil auß einer Pleiden…`
   - **CS**: `každá[^1] koule` / `Jak se mají házet a střílet ohnivé šípy {Feurpfeil}[^3]`
10. **`3-051v` – `das ronde Puluers`, `biß mit vier Büchsen`**:
    - **DE**: `fül das ronde Puluers` / `damit wol bewarnet biß mit vier Büchsen`
    - **CS**: `naplň vývrt[^4] prachem` / `tím buď dobře opatřena až čtyřnásobně[^6]`
11. **`3-052r` – `verbissen`, `oder schütz`, `weiloch`, `os`**:
    - **DE**: `Solt sie stopffen vnd nit verbissen / Oder schütz wirdt dir zuuor wissen.` / `Wein zu dem weiloch ein laß` / `os bricht sie`
    - **CS**: `dobře ji utěsni a neopomeň,[^2] / aneb to střelec předem zvědět má hned.[^3]` / `nalej pak víno do otvoru,[^5]` / `a[^6] dělo praskne`
12. **`3-052v` – `gorß` a `mit feindtlichem warm sein`**:
    - **DE**: `wie gorß du die Ballen haben wilt` / `in einer stuben / mit feindtlichem warm sein`
    - **CS**: `tak velké, jak velké chceš mít koule.[^2]` / `ve světnici mírně teplé,[^3]`
13. **`3-054r` – `Büchenpuluer`, `Isponicum`**:
    - **DE**: `WIltu Büchenpuluer` / `thů darinn Isponicum vnd Galitzenstein`
    - **CS**: `Chceš-li oddělit od sebe puškový prach {Büchenpuluer},[^1]` / `přidej do něj španělskou sůl (*Isponicum*) a bílou skalici (*Galitzenstein*).[^3]`
14. **`3-054v` – `gar böß salpeter`, `garbs schwefel`, `stettit`, `bricht`**:
    - **DE**: `3. pfundt gar böß salpeter / 1. pfundt garbs schwefel / … ein halbs stettit Arsenicum album` / `bricht 30. pfundt schwefels`
    - **CS**: `3 libry velmi ostrého[^2] ledku, 1 libru čisté[^3] síry, … půl malého dílku[^4] bílého arzeniku` / `pojme[^5] 30 liber síry`

---

## 5. Návrhy do glosáře (`knihy/solms-1559/glosar.yaml`)

### A. Nová hesla navrhovaná do glosáře

```yaml
- id: ohnivy-sip
  cs: ohnivý šíp
  de:
  - Feurpfeil
  - Feur pfeil
  - Feurpfeiln
  kategorie: delostrelectvo
  pozn: Šíp opatřený na dříku pytlíčkem či těstem ze zápalné směsi (ledek, síra, uhlí, kafr, pryskyřice), vystřelovaný z kuší, ručnic i děl k zapalování střech a opevnění.

- id: tarasnice
  cs: tarasnice
  de:
  - Tarrasbüchse
  - Tarras Büchsen
  - Tarras Büchsen
  kategorie: delostrelectvo
  pozn: Dlouhé střední či lehčí polní a hradební dělo (Tarrasbüchse) na nízké lafetě či podstavci, užívané zpoza tarasů a hradeb.

- id: kamenometne-delo
  cs: kamenometné dělo
  de:
  - Steinbüchse
  - Steinbüchsen
  kategorie: delostrelectvo
  pozn: Těžké dělo široké ráže s užší prachovou komorou, určené ke střelbě velkých tesaných kamenných koulí.

- id: olovene-delo
  cs: olověné dělo
  de:
  - Bleyen Büchsen
  kategorie: delostrelectvo
  pozn: Speciální či zkušební hlaveň z olova (nebo olovem vyztužená) zmiňovaná v pyrotechnických návodech pro střelbu rozžhavených železných koulí.

- id: zatka
  cs: zátka
  de:
  - Klotz
  - Klötz
  - klotz
  - klotzen
  - klötzen
  - Büchsen klötz
  - spunt
  kategorie: delostrelectvo
  pozn: Dřevěný (zpravidla topolový) či hliněný válec nebo špunt zarážený před prachovou nálož za účelem utěsnění hlavně před kamennou koulí.

- id: zatravka
  cs: zátravka
  de:
  - Zintloch
  - Zündtloch
  - zündloch
  - zindtloch
  - anzintloch
  kategorie: delostrelectvo
  pozn: Tenký otvor na horní straně zadní části hlavně, kterým se zapaluje prachová nálož.

- id: zapalny-prach
  cs: zápalný prach
  de:
  - Zündtpuluer
  - zindt Puluer
  - anzindt Puluer
  kategorie: delostrelectvo
  pozn: Jemně mletý, rychle vzplanuvší prach bohatý na ledek, užívaný k naplnění zátravky a odpálení hlavní nálože.

- id: trhaci-prach
  cs: trhací prach
  de:
  - spring Puluer
  kategorie: delostrelectvo
  pozn: Vysoce účinný, ztužený či zesílený prach v koulích (Springpulver), vkládaný ke zvýšení průraznosti či k výbuchu.

- id: sira
  cs: síra
  de:
  - Schwefel
  - schwefel
  - Schwefels
  - schwefels
  kategorie: delostrelectvo
  pozn: Jedna ze tří základních složek střelného prachu a zápalných směsí vedle ledku a dřevěného uhlí.

- id: drevene-uhli
  cs: dřevěné uhlí
  de:
  - Kolen
  - Koln
  - koln
  - kolen
  - kolns
  kategorie: delostrelectvo
  pozn: Jemně utlučené dřevěné uhlí (z lipového, lískového, topolového či olšového dřeva nebo z plátna), jedna ze tří hlavních složek střelného prachu.

- id: kvintlik
  cs: kvintlík
  de:
  - Quintat
  - Quent
  - Quentlein
  kategorie: miry
  pozn: Stará lékárnická a váhová jednotka rovná čtvrtině lotu (cca 3,7–4,4 g).

- id: unce
  cs: unce
  de:
  - vntz
  - Vntz
  kategorie: miry
  pozn: Stará lékárnická a váhová jednotka rovná 2 lotům (asi 30 g).

- id: divoky-ohen
  cs: divoký oheň
  de:
  - wildes feur
  - wildes Feur
  - wilds Feur
  kategorie: delostrelectvo
  pozn: Dobové označení pro neuhasitelnou zápalnou směs (obdoba řeckého ohně), jež hoří i pod vodou nebo za vlhka.
```

### B. Nové pravopisné a tvarové varianty do stávajících hesel

- **`dela`**: přidat `Büchs`, `Büchsen`, `Hauptbüchsen`, `blei Kugel` (k `koule`), `stein` / `Büchsenstein` (kamenná koule).
- **`prach`**: přidat `Büchsen Puluer`, `Büchsenpuluer`, `Büchenpuluer`, `Püchsenpuluer`, `wag Puluer` (stopina).
- **`rucnice`**: přidat `Handtbüchsen`, `handt Büchsen`.
- **`hlaven`**: přidat `Ror`, `Rors`.
- **`koule`**: přidat `Kugeln`, `Kugel`, `Feur Kugel`, `feur Kugeln`, `blei Kugel`.
- **`ledek`**: přidat `Salpeters`, `salpeter`, `Saluter` (tisková chyba z `3-045v`).
- **`kartac`**: přidat `Hagel`, `hagel schos`, `Igel`, `schifferling`, `haußpfeil`.
- **`blida`**: přidat `Pleiden`.
- **`kvartyr` / `ctvrtka`**: přidat `vierling` (k `ctvrtka`).
- **`libra`**: přidat `pfundt`.
- **`lot`**: přidat `lot`, `lots`.
- **`maz`**: přidat `maß`.
