# 2. revize – První kniha, dávka C (1-021r – 1-030v)

Rozsah: 20 stran, skeny 51–70 (BSB bsb00085168, staženy přes IIIF ve 1400 px, sporná místa zvětšena výřezem).
Sousedé 1-020v a 1-031r jen přečteni; návaznost vět na obou hranicích sedí.
Kontrola: `python -I nastroje/over_strany.py knihy/solms-1559 1-021r … 1-030v --prisne` → **0 chyb, 1 varování**.
Varování 1-026r („fein“) je falešné: tisk má *ein hauffen fein an sich hencken* (= obratně), opravit ho nelze.
Všechny strany: `stav: zkontrolovano`, `overeno_clovekem: false`.

Plynulost „středně“: dlouhá souvětí (… / so / vnd / dann …) jsou rozdělená na samostatné věty v rámci bloku.
Slovosled je přirozený, ubylo „takto/tak/tedy/totiž“, nejasné podměty jsou dopsané (příp. v [ ]). Autorova 1. osoba
(„nebudu popisovat“, „mám za to“) i dobový tón zůstávají.

## Opravy `de` podle skenu (OCR / dřívější přepis)

| strana | před | po (tisk) | pozn. |
|---|---|---|---|
| 1-021r | *geschehenden straffen* | *gestehenden straffen* | sken zřetelně *geſtehenden*; nová poznámka |
| 1-021r | *vnderhaltung* | *vnderhaltund* | tisková chyba, poznámka |
| 1-021v | *SO dann* | *So dann* | odstavec bez zdobné iniciály, obyčejná sazba |
| 1-021v | *Herren vnder der Nation* | *Herren von der Nation* | chyba přepisu |
| 1-022r | *Veldoberster*, *Kriegßuerstendigen* | *Veldoberber* (*Veldober-|ber*), *Kriegßuerstengigen* | tiskové chyby, poznámka |
| 1-022v | *zu roß odder fůß* | *zu roß odder fuß* | |
| 1-024r | *Lermenplatz darmit zubesetzen* | *zubeziehen* | chyba přepisu (OCR *zubestehen*) |
| 1-024r | *deßgleichen sein Platz* | *desgleichen* | |
| 1-024v | nadpis *Zwelff puncten* | *Zwelff puncken* | tisková chyba (srov. *puncken* na 1-020v), bez poznámky |
| 1-025v | *ALso seind* | *Also seind* | bez zdobné iniciály |
| 1-026v | *stucken*, *stuck* | *stücken*, *stück* | |
| 1-027r | *auff fütterung* | *auff füteruug* | převrácená litera, poznámka |
| 1-027v | *in schleusßt* | *in schleußt* | |
| 1-028r | *inn kurtzer Zeit* | *zeit* | |
| 1-028v | *die Ampts person handeln* | *die Amps person* | tisková zkratka, bez poznámky |
| 1-029r | *verhinderung ?* | *verhinderung?* | |
| 1-029v | *dieselbtgen*, *ampts uersehung*, *in gůter Regierung vnd gebrauch stehn*, *lustig* | *dieselbigen*, *amptsuersehung*, *gebraucht stehn*, *lüstig* | |
| 1-030r | *auff das Haupt*, *den Kriegßherrn die es angehet* | *haupt*, *Kriegßherren* | |
| 1-030v | *zu gluck oder zuuerlieren* | *zu glück oder zuuerheren* | **věcná oprava**: *verheeren* = zpustošit, ne *verlieren*; CS „ke zpustošení“ + poznámka |
| 1-030v | *sein landtuolck darzů*, *Fůßuolck*, *dz nit vorhin* | *landuolck*, *Fußuolck*, *das* (rozepsaná zkratka *dz*) | |

Ověřeno beze změny: hranice stran a kustody. *Sen-|tentz* je celé na 22r, *Kriegs-|räthen* na 29v, *ha-|ben* na 30r,
*Practi-|cken* na 29r a *Die-|weil* na 28r. Iniciály *DIeweil* (23v), *ES* (25v) a *VOr* (26r) sedí,
*Gerichßbůch*, *allhei*, *gesechehen*, *freinen*, *des dʒ* a *ampspersonen* jsou ve skenu skutečně tak.

## Struktura
- **1-024r**: odstraněno `pokracovani: true`. Ve skenu začíná *Nemlich* odsazeným řádkem jako nový odstavec,
  předchozí odstavec na 23v končí tečkou. Párování bloků se nemění.
- Úrovně nadpisů ponechány (23v, 25v, 26r = 2; 24v = 3).

## Hlavní změny překladu po stranách (výběr)
- **1-021r**: „nepokoje {auffruhr}“ → „vzpoury {auffruhr}“ (glosář: *auffruhr* = vzpoura). Souvětí o soudní knize je
  rozdělené. „kdykoli a jak často“ → „kdykoli“. *die die Justitien her gebracht haben*: „zdědili po předcích“ →
  „odedávna zachovávají“.
- **1-021v**: soudní formule polního maršálka je rozdělená na 3 věty. *was er für gůt leut darzů gebraucht*: „kteří
  jsou v tom zběhlí“ → „které k tomu obvykle přibírá“. *von der Nation* = „z téhož národa“.
- **1-022r**: *geschwinder fall* „ožehavý“ → „naléhavý“. Vztahy podmětů u milosti: „aby [odsouzený] … s čímž on
  [maršálek] i ostatní plně souhlasí“ (dříve podmíněné „jsou-li s tím srozuměni“, to byl posun významu).
  Konec strany: dřívější „…ani zabavováním; proto | a jakémukoli jinému násilí“ dával nesmysl. Nyní „…a tedy |
  ani žádným jiným bezprávným násilím“. Poznámka s odkazem na Knihu úřadů: kapitola polního maršálka je
  025r–027v, dříve chybně 25r–29r (na 028r začíná zbrojmistr).
- **1-022v**: oceňování proviantu je přeložené jasně: „Cenu proviantu má stanovit spolu s polním maršálkem
  a profousy…“. Dříve „Ten má … ocenit, a při tom má … zůstat“. Poznámka 3 už neuvádí smyšlený titul *Von der
  Artollerei*, místo toho odkazuje 3-titul (Třetí kniha).
- **1-023r**: nová věta „Jde totiž o to, co se často stává…“. „dodávky“ → „příděly“ (*liefferung*). Vypuštěn tag
  {Regiment} u významu „kázeň“: glosář ho vede jako „pluk“, odkaz by byl zavádějící. Vypuštěna poznámka
  o *Holtzkerben*, protože opakovala glosář (vrubovka). Poznámka 1 nově odkazuje na 5-titul (Pátou knihu) o podkopech.
- **1-023v**: rejstříky útrat jezdců (*kösten*) jsou přeformulované a poznámka zpřesněná. Úvod kapitoly o ležení je
  rozdělený na 3 věty.
- **1-024r**: odstraněn dvojí zápor „Nechci … neopisovat“, který obracel smysl. Nyní „Nebudu proto … popisovat …
  “. Je to totiž první věc…“. Úkoly zbrojmistra i mistra vozové hradby jsou rozdělené do vět.
- **1-024v / 1-025r**: drobné stylistické úpravy článků („s výhodou terénu“, „aby jedna část dávala pozor na druhou“
  pro *auff einander warten*, „noční klid“). Úvod 025r je zpřehledněný.
- **1-025v**: *gleich gnug sei* = „bylo už učiněno zadost“. *biß hernach* = „ještě nedávno“. Opravena shoda
  „jím … ho“ (zakopávání).
- **1-026r/v**: osm „Za …“ článků je rozdělených do vět. *ein hauffen fein an sich hencken* = „obratně navázat na sebe
  [nepřátelský] houf“. *Meutterei* = „vzpoura či spiknutí“, poznámka ponechána. *frembde Wacht* = „neobvyklá
  stráž“. Doplněn {Scharmützel} při prvním výskytu na 026r.
- **1-027r**: „Ba dokonce si to někteří vykládají“ → „Někdo by to snad chtěl vykládat“. Odstavec o štítových vozech
  je rozdělený do vět. Vypuštěna poznámka o *Schirmwagen* (duplikát glosáře) a nahrazena poznámkou k *füteruug*.
- **1-027v**: *bescheidenheit* = „umírněnost“. Vozy patří „k dělostřelectvu, které je má opatrovat“.
- **1-028r/v, 1-029r**: *obersten Feldherrn / oberst Feldherr / Feldherr*: „nejvyšší polní pán“ → „(nejvyšší) válečný
  pán“ podle glosáře (heslo `valecny-pan`). Přímé řeči správců jsou v uvozovkách. „pletich“ → „úkladů“
  (*Practicken*). „pokojovými rady, kteří … z tepla světnice“ → „světničními rady, kteří chtějí válce určovat
  míru“ (přidaný obrat vypuštěn). Neukončené souvětí tisku (*Dann wann die Ampter wol regiret…*) má novou poznámku.
- **1-029v / 1-030r**: *gerechtigkeit* = „práva a požitky“. „kšeft“ → „kupecký obchod“ (*Kauffhandel*, jednotně).
  *Kriegßleut* = „válečníci“ (glosář *valecny-lid*: „válečníci, vojáci“, `hledat: válečník`).
- **1-030v**: rozdělení na 5 a 7 vět. *bald in einen Krieg rathen* = „ukvapeně radit do války“. *so ein vertrawen
  haben* = „jen když jim lze důvěřovat“. Oprava *zuuerheren* viz výše.

## Sporná místa k rozhodnutí
1. **1-029r, struktura**: ve skenu začínají *Das ist aber recht…* a *Wann ein Herr dann mit allen…* na kraji řádku
   bez odsazení. Podle sazby jsou to pokračování předchozích odstavců (*Ja mann will…*, *Besonder sol mann…*),
   v datech jsou ale samostatné bloky. Strukturu jsem neměnil (zadání: neměnit bloky). Návrh: sloučit 3+4 a 5+6.
2. **1-024r, `pokracovani`** (odstraněno, viz výše). Pokud by správce chtěl zachovat přechod věty („Totiž
   prostřednictvím…“ navazuje obsahově na 23v), stačí příznak vrátit. Sazba ale ukazuje nový odstavec.
3. **1-024r** *nit beschreiben* vs. *mit beschreiben*: překlad drží tisk („nebudu popisovat“), poznámka obě čtení uvádí.
4. **1-021r** *gestehenden*: buď „uložené“ (od *gestehen* = stát, být uložen), nebo tisková chyba za *geschehenden*.
   Překlad „s udělenými tresty“ vyhovuje oběma čtením.
5. **Kriegßleut**: v dávce C jednotně „válečníci“. Sousední 1-031r (jiná dávka) má „vojáky {Kriegßleut}“, to je
   potřeba sjednotit v celé knize.
6. **1-023r / 1-023v / 1-029v „Regiment“ ve významu kázeň/pořádek** (*in Regiment halten*, *gůt Regiment halten*):
   tag vypuštěn, protože glosář `Regiment` = pluk. *Dann wann die Regiment wol versehen…* (029v) ponecháno jako
   „pluky {Regiment}“, i když jde možná o „správy“.

## Návrhy do glosáře (glosář needitován)
| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| zemske-stavy | zemské stavy | Landtschafft, landtschafft | osoby | Shromáždění stavů země, které pán svolává k poradě o válce a o penězích na ni (1-030v). |
| zemsky-lid | zemský lid | Landtuolck, landuolck, landtuolck, Lantßuolck | jednotky | Domácí poddaní povolaní ke zbrani, na rozdíl od najatého válečného lidu (1-030v – 1-031r). |
| znalec-valky | muž znalý války | Kriegßuerstendigen, Kriegßuerstendige | velitele | Zkušení válečníci, které válečný pán posazuje k radě (1-022r, 1-025r). |
| valecny-pan (doplnit) | – | Feldherrn, Krigßherrn | velitele | Doplnit tvary do `de`. |
| vzpoura (pozn.) | – | – | pravo | Doplnit: *Meutterei* může znamenat i spiknutí či záškodnictví (1-026v). |
| tazeni (doplnit) | – | zug, zügen, Zügen | sluzba | Malé tvary chybí; *zug* někdy = pochodový šik (1-026r). |
