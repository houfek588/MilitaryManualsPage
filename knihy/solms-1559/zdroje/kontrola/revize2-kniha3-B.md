# 2. revize – Solms 1559, dávka „kniha3-B“ (`3-013v`–`3-025r`, skeny 278–301)

Revize podle `zdroje/ZADANI_REVIZE2.md` (plynulost „středně“, *Oberst* = plukovník). Struktura bloků, `sken`, `id`,
`stav: zkontrolovano` a `overeno_clovekem: false` beze změny. Sousedé `3-013r` a `3-025v` jen čteni (návaznost
`3-013r` → `3-013v` a `3-025r` → `3-025v` sedí).

Ověření: `python -I nastroje/over_strany.py knihy/solms-1559 3-013v … 3-025r --prisne` → **24 stran, 0 chyb, 0 varování**.

Postup: strojové porovnání `de` s OCR (`zdroje/ocr_bsb/0278–0301.txt`) po slovech; odchylky a sporná místa ověřena ve
skenech BSB IIIF (`bsb00085168_00281, 282, 285, 287, 294–301`). Všechny početní přehledy (váhy, koule, vozy, koně)
přepočítány řádek po řádku.

## 1. Opravy originálu (`de`) podle skenu

| Strana | Bylo | Nyní (podle skenu) | Pozn. |
|---|---|---|---|
| `3-015r` | `zu legern zu ordnen` | `zu legern / zu ordnen` | virgule v tisku |
| `3-017r` | `Ich bin ein Wagner` | `Ich bin ein Wager` | tisková chyba, nová pozn. 1 |
| `3-017r` | `zum kleinen stück` | `zum keinen stück` | tisková chyba (sken i OCR), nová pozn. 4 |
| `3-018r` | `in besatzung` | `in beschatzung` | tisková chyba za *besatzung*, nová pozn. 2 |
| `3-018r` | `sein anschlag darüber hören` (2. výskyt) | `… dariber hören` | tisková chyba, v pozn. 2 |
| `3-021v` | `Viertel Schlangen` (tabulka) | `Vierteil Schlangen` | i v `cs` `{…}` |
| `3-022r` | `ein Monat aufflauffen` | `ein Monat aufflauffend` | |
| `3-022r` | nadpis `im fall der notturfft` | `im fall der nottufft` | tisková chyba, uvedeno v pozn. 1 |
| `3-022v` | `Derohalben sie` | `Derhalben sie` | tisk *Der-|halben* |
| `3-022v` | `Das brengt auff die 4. wagen` | `Das brengt den 4. wagen` | |
| `3-022v` | `mit füret / Darumb daß` | `mit füret? Darumb daß` | otázka v tisku – změněn i překlad (viz níže) |
| `3-023r` | `thůt Wagen 2.` | `thůt Wägen 2.` | |
| `3-023r` | `VIer Nachtigaln oder doppel Cartaun 4.` | `GVter Nachtigaln …` | **chybná iniciála**: tisk má zdobné *G* (*Guter*), OCR „Vter“; překlad „Dobří slavíci …, 4 kusy“ |
| `3-024r` | `Zu disen 4. Notschlangen` | `… Notschlagen` | tisková chyba, v pozn. 1 |
| `3-024v` | `gefäß vnd fuer` | `gefäß vnd füer` | |
| `3-025r` | `vnd seiner zugehörigen Kugeln` | `vnd seiner zugehörung Kugeln` | |
| `3-025r` | `Darzů soll mann antworten /` | `… antworten?` | otazník v tisku jako dvojtečka, pozn. 3 |

Ověřeno a ponecháno: `schwerffen` (`3-015r`), `Leudt` (`3-018r`), `vnd ein Brechgeschütz` (`3-021v`), `Monat / etc.`
(`3-023r`, `3-023v` – skutečně v tisku), `zusetzen` (OCR „zusehen“, `3-022v`–`3-023v`), `zuuerrichten` (OCR „zuuerachten“),
`war / gefäß` (`3-024v`), čísla `93` (`3-024r`), `25` a `104` (`3-024v`), `915` (`3-025r`). OCR soustavně čte *nit* jako „mit“ –
všude ponecháno *nit*. Nejisté: nadpis `3-021v` má v tisku patrně *Kriegßriſtungen* (tečky nad *ü* nezřetelné) – ponecháno
`Kriegßrüstungen`; `3-015v` *Paßpfort* neověřeno ve výřezu (OCR jednou „Pasifport“).

## 2. Hlavní změny překladu po stranách

- **`3-013v`**: *züg* „potahy“ → „kladkostroje“ (3×, sjednoceno s `3-014v`, `3-016v`, `3-018r`, `3-022v`–`3-025r`; pozn. 1 přepsána);
  „patří za hlavní houf a za něj zadní voj“ → „patří [s vozy] za hlavní houf a zadní voj až za něj“; „mezi nimi jdou šancíři“ → „Mezi tím“.
- **`3-014r`**: 4. článek rozdělen na věty a opravena shoda („zda se kusy zapřáhnou … aby zůstaly zapřaženy“, dříve „zapřaženi“);
  vypuštěno přidané „vhodnými [osobami]“; „to budou plukovníci dobře vědět, jak uspořádat“ → „jak to uspořádat, budou plukovníci dobře vědět“.
- **`3-014v`**: **věcná oprava 11. článku** *die geschwader zu roß vnd fůß zu schlagen*: „[děla dělí] mezi švadrony … k bitvě“ →
  „aby se jimi bilo do jízdních i pěších švadron, střílelo a útočilo“; „s mnoha i málo koňmi či oři“ → „pro více i méně koní {Rossen} či ořů {pferden}“; pozn. 1 bez spekulace o hřebenových heverech.
- **`3-015r`**: vozová hradba „rozbíjí“ → „staví“ kolem ležení; „švader“ → „švadron“; *Landtschafft* „zemské obci“ → „zemským stavům“;
  *verehren vnd wol halten* „uctít, dobře chovat“ → „obdarovat a dobře s ním zacházet“; *trost* „útěchu“ → „oporu“.
- **`3-015v`**: *arme leut* „chudý lid“ → „poddané“, *vnderhelt* „zachová si“ → „zaopatří“; *sich nit beschweren* „nezdráhat se / neobtěžovat se“ → „nemít za zlé“;
  *was einem Herrn auff eim Büchsenmeister steht* → „jak mnoho pánovi na puškaři záleží“; zbrojmistrova věta o „zaopatření sebe jako zbrojmistra“ srozumitelně.
- **`3-016r`**: „šarfmerci“ → „šarfmeci“ (glosář *šarfmece*, i `3-016v`, `3-017r`); doplněno `{halb Cartaun}`; *teilung* „rozdělení, šířce“ → „poměrech {teilung}, světlosti“;
  *plechwagen* „okované plošinové vozy“ → „kládové vozy“ (= *Blochwagen*, glosář `kladovy-vuz`), pozn. 3 přepsána; 20. článek přeskládán.
- **`3-016v`**: 5. článek (kovolijec, přebytečná tíha) rozdělen do vět; „kovina“ → „kov“ (sjednoceno s „na kovu“ v rozpočtech); „není radno jednat ani do zbrojnice“ → „není o službě ve zbrojnici co jednat“.
- **`3-017r`**: **věcné opravy** – 7. článek „nechť ukáže či předvede kus“ → „ukaž mu nějaký kus nebo mu jej nech prohlédnout“ (*laß jhn ein stück anzeigen oder sehn*);
  9. článek *speichen* „loukotě“ → „paprsky {speichen}“; *werckstück* „mistrovské dílo“ → „řemeslný kus“ (odlišeno od *Meisterstück* = mistrovský kus, i `3-018r`);
  „[plošinový vůz]“ → „[kládový vůz]“; nové pozn. 1 (*Wager*) a 4 (*keinen*), přečíslováno.
- **`3-017v`**: 14.–15. článek rozdělen, jasný podmět („Potom mu je má zbrojmistr dát vyrobit“); 17. článek „může se ho nechat udělat zkoušky“ → „lze ho časem nechat udělat zkoušky; zpočátku…“.
- **`3-018r`**: **věcná oprava** *ob mann auch das geschütz jhn ablauffen kön* „zda jim lze odsunout děla“ → „zda by jim [nepřítel] nemohl děla zteči a vzít“ (pozn. 4);
  *herauß schiessen* „ostřelovat“ → „nepřítele z něj vystřílet“; nová pozn. 2 (*beschatzung*, *dariber*); přečíslováno.
- **`3-018v`**: „svěřovat mu velení“ → „mnoho mu svěřovat“; „podbízet se“ (*lieben*) → „hledět si jich“; „nemá být žádné dítě a sám nic nevědět“ → „nemá být jako dítě, které samo nic neví“.
- **`3-019r`**: příklad s řemeslníkem rozdělen; „mistr se musí kořit jemu“ → „mistr si musí vážit jeho“ (*der meister muß jn achten*); úvod o prachu přepsán (*Nach* = noch, „starých“ = *der alten*);
  **obrácená příčinnost** „což působí to, že je sypký“ → „a to proto, že je sypký“; „dostřelí před krátkým“ → „přestřelí krátké“; *röß* jednotně „sypký“.
- **`3-019v`**, **`3-020r`**: *vbersetzt* „přesycen“ → „smíchán“ (sírou a uhlím); korelativní *so … so* → „čím déle …, tím déle“; 4. nevýhoda rozdělena na 5 vět; „Třetí je, že se třeba obávat“ (gramatika).
- **`3-020v`**: *Meisterstück* „mistrovské zásady“ → „mistrovské kusy“; *bei mir … sein lassen* „podle svého mínění uznat“ → „u sebe ponechat jako puškaře“.
- **`3-021r`**: *verstandt der Büchsenmeister* „schopnosti puškařů“ → „[ne]znalosti puškařů“; pozn. 2 bez zmínky o OCR.
- **`3-021v`**: úvodní odstavec o devateru druhů přeformulován (bez rozbité vsuvky).
- **`3-022r`**: *5000 schwern vnd ringen Pferden* „těžkými a lehkými koňmi“ → „koňmi těžké i lehké jízdy“; pozn. 2 (augšpurský cent) přesunuta k „augšpurské váhy“; pozn. 1 bez zmínky o razítku.
- **`3-022v`**: rétorická otázka *so mann doch … mit füret?* převedena na otázku a odpověď; „jeden kus může druhý nahradit“ → „jeden díl … druhý“ (kola, nápravy, kotouče {scheiben});
  „i s nich dolů“ → „a zase z nich skládat“; „vybrat nejsilnější koně“ → „přidělit větší náklady nejsilnějším koním“.
- **`3-023r`**: nová iniciála *GVter* (viz výše); věta o kladkostroji rozdělena; *nach gelegenheit* „podle ráže“ → „podle potřeby [svého kusu]“; pozn. 1 přepsána (ověřeno *Monat* ve skenu).
- **`3-023v`**: „koňů“ → „koní“; pozn. 1 bez OCR, jen kontrola součtu.
- **`3-024r`**–**`3-025r`**: drobné stylistické úpravy, „drží na železe“ → „váží“, pozn. k *war / füer* a *antworten?* upřesněny; zrušen mylný údaj o „kustodu *gen 6.*“ (jde o 2. řádek marginálie *Feldtschlan-gen 6.*).

Kontrola tabulek a rozpočtů (vše sedí s tiskem, chyby předlohy již vysvětleny v poznámkách): šarfmece 2 × 115 = 230 c., 200 koulí po 85 lb = 170 c., vozů 18, koní 178 (+12 = 190, pozn.);
slavíci 4 × 80 = 320 c., 400 × 70 lb = 280 c., vozů 29, koní 276; těžké kulveriny 4 × 66 = 264 c., 64 c. koulí, tisk 93 místo 132 koní (pozn.), vozů 13, koní 145;
kartouny 8 × 50 = 400 c., 360 c., tisk „8 vozů / 32 koní“ místo 12/48 a 25 místo 35 vozů (pozn.); souhrn 1214 / 874 / 874 c. sedí, 104 vozů a 915 koní nesedí (pozn.).
Tabulka `3-021v`: 2 + 4 + 4 + 8 = 18, 6 + 8 + 10 + 10 + 20 = 54, celkem 72 – souhlasí.

## 3. Sporná místa k rozhodnutí

1. **`3-023r`, `3-023v`** – *bedarff man einn Monat / etc. thůt Wägen 2.* CS „je třeba na jeden měsíc atd. – činí to 2 vozy“. Tisk skutečně má *Monat*; smysl nejasný.
2. **`3-016v`** – *geust er die so dick vber die recht theilung / daß sie halten muß / dann die vbrige schwere ist mit jm* → „On ji ale odlije tak silnou, nad správné poměry, aby jistě vydržela – přebytečná tíha jde přece jemu k dobru“. Lze číst i podmínkově („odlije-li…“).
3. **`3-018r`** – *Stadt die nicht gantz wol Leudt ist* → „není docela dobře opevněno“ (pozn. 3); *Leudt* ve skenu jisté, význam nejistý.
4. **`3-024v`** – *sein besonder war / gefäß vnd füer* → „zvláštní výstroj[?], lafeta a potah“; *war* nejasné.
5. **`3-014v`** – *hebzeug* přeloženo „zdvihadla“ bez `{…}`, protože glosář `kladkostroj` (Hebzeug) by splynul s *züg* „kladkostroje“ ve stejném výčtu.
6. **`3-017v`** – *Fewer* (z moždíře) „ohňostroje“ podle glosáře `ohnostroj`; výstižnější by bylo „ohně / zápalné náboje“.

## 4. Návrhy do glosáře

| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| `delovy-kladkostroj` (doplnit) | dělostřelecký kladkostroj | + züg, Züg, Zug, zügen, Zügen | delostrelectvo | **Kolize**: tvary *zug/züg* nyní vedou na `tazeni`; v 3. knize (l. 13v–25v) jde o kladkostroje (*Bock* + *kloben*). Odkazy `{züg}` na `3-014v`, `3-016v`, `3-018r` proto míří na „tažení“ – nutno rozhodnout. |
| `kartouna` (doplnit) | kartouna | + Cartaun, Cartaunen, doppel Cartaun | delostrelectvo | tvary z `3-016r`, `3-017v`, `3-021v`, `3-023r`, `3-024v` nyní bez odkazu |
| `kladovy-vuz` (doplnit) | kládový vůz | + plechwagen | delostrelectvo | `3-016r` (tisková podoba) |
| `kun` (doplnit) | kůň | + Roß, Rossen, Rosse | jednotky | `3-014v` a rozpočty |
| `pomery-dela` (nové) | poměry (dělení) | teilung, theilung | delostrelectvo | Soustava poměrů rozměrů děla (délka, síla stěn, světlost) odvozená od ráže koule; `3-016r`–`3-017r`. |
| `mistrovsky-kus` (nové) | mistrovský kus | Meisterstück, meister stück | osoby | Zkouška mistrovství puškaře (`3-017r`–`3-020v`); odlišit *werckstück* = řemeslný kus. |
| `zemske-stavy` (nové) | zemské stavy | Landtschafft | osoby | `3-015r`, `3-022r` (rada pánovi „mit seiner Landtschafft“). |
| `zeug` (pozn.) | – | zeug | delostrelectvo | V 3. knize též „dělovina, kov“ (*den zeug ob er gůt oder böß ist*, *an gezeug 230. Centner*); překládáno „kov“, bez `{…}`. |
