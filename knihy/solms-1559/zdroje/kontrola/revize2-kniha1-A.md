# 2. revize – Solms 1559, dávka „kniha1-A“ (`titul-svazek`, `1-001v`, `1-erb-cisare`, `1-jezdec`, `1-002r`–`1-010v`)

Revize podle `zdroje/ZADANI_REVIZE2.md` (plynulost „středně“). Struktura bloků, `sken`, `id`, `stav: zkontrolovano`
a `overeno_clovekem: false` beze změny. Soused `1-011r` jen čten (návaznost `1-010v` → `1-011r` sedí).

Ověření: `python -I nastroje/over_strany.py knihy/solms-1559 titul-svazek 1-001v 1-erb-cisare 1-jezdec 1-002r … 1-010v --prisne`
→ **22 stran, 0 chyb, 0 varování**.

Postup: strojové porovnání `de` s OCR (`zdroje/ocr_bsb/0009–0030.txt`), u všech odchylek a sporných míst kontrola
ve skenech BSB IIIF (`bsb00085168_00009`–`_00030`, u s. 14 a 25 i výřezy v rozlišení 2800 px).

## 1. Opravy originálu (`de`) podle skenu

Předchozí kontrola na několika místech „opravila“ tisk, nebo naopak ponechala chybu OCR jako domnělou tiskovou chybu:

| Strana | Bylo | Nyní (podle skenu) | Pozn. |
|---|---|---|---|
| `titul-svazek` | `Das erst Buch.` | `Das erst Bůch.` | tisk má *ů* |
| `1-002v` | `willigsten Diener/` | `willigsten Deiner/` | tisková přesmyčka (OCR četlo správně), vysvětleno v pozn. 2 |
| `1-002v` | `Graue zu Solms/ vnd Herr zu Müntzenberg.` | `Graue zů Solms/ vnd Herr zů Müntzenberg.` | |
| `1-003r` | `versehen vnd vertrawen/` | `versehen vnd vertrauen/` | tisk *vertrau-en* |
| `1-005r` | `jre Kriegsregirung`, `solche Kriegsregierung zuhalten` | `Kriegßregirung`, `Kriegßregierung` | |
| `1-005v` | `auß dem Teutschlandt … zu kriegen` | `auß dem Teuschlandt … zu kreigen` | tiskové chyby ponechány, nová pozn. 1 |
| `1-005v` | `DIe Kriegßleut` | `Die Kriegßleut` | v tisku obyčejné *D*, žádná iniciála |
| `1-006r` | `zwei gůter mit rüstung` | `zwei güter mit rüstung` | tisk má *ü* (≠ *gůt*) → *Güter* „statky“; změněn i překlad a pozn. 2 |
| `1-008r` | `nit mehr/ wie sich gebürt/ Arbeit halben)` | `nit mehr (wie sich gebürt/ Arbeit halben)` | levá závorka v tisku je; zrušena mylná pozn. o lomítku |
| `1-008r` | `nit gůt thun werden` | `mit gůt thun werden` | chyba OCR, ne tisku; pozn. přepsána |
| `1-008v` | `DIeweil die Römische` | `DIe weil die Römische` | tisk dělí *Je weil* |
| `1-010v` | `oder Hundert pferden` | `oder hundert pferden` | |

Ověřeno a ponecháno: iniciály `DVrchleuchtigster`, `DIe weil` (2× na `1-003r`), `DIe` (`1-005r`), `SO` (`1-005v`), `DIeweil` (`1-009v`), `VOr` (`1-010v`);
tiskové tvary `nachtheilt`, `allergedigst`, `außtürcklicher`, `gemach` (`1-004r`), `gnaden)` bez levé závorky (`1-002v`), `fürzusetzen`, `Mitthridate`;
na titulu dřevořez nese skutečně `PLVS – VLTRE`. Nejisté: `Müntzenberg` (tisk spíše *Min-tzenberg*, přehláska nečitelná – ponecháno);
na `1-006v` tisk píše patrně `Herꝛn`, v `de` stojí `Hern` (neměněno, k ověření).

## 2. Hlavní změny překladu po stranách

- **`titul-svazek`**, **`1-erb-cisare`**: popis – heslo „PLVS – VLTRE (tak na dřevořezu)“; překlep *mnohopoleý* → *mnohopolý*.
- **`1-002r`**: věnování rozděleno do vět; „jimiž jsem byl po své dny hojně … užíván“ → „v jehož službách jsem strávil mnoho svých dní, a to ve vážných veleních“; „nemohl a neměl jsem opomenout“ → „Nemohl jsem a nesměl proto opomenout“.
- **`1-002v`**: Lucullova pasáž rozdělena na 6 vět; „(s udělením Boží milosti)“ → „(s pomocí Boží milosti)“, „spíše s ohledem na mé věrné srdce … než pro to, co jsem v něm snad dokázal“.
- **`1-003r`**: první odstavec (anakolut *DIe weil …*) rozdělen do 4 vět; „omilostnit“ → „obdařit“; *lengst vnd best Kriegsuolck* „nejstálejší“ → „nejdéle sloužící a nejlepší“; věta s visícím „Jelikož“ převedena na oznamovací.
- **`1-003v`**: dvě poznámky místo jedné dvakrát odkazované (*ordunng*, *bedach*); „v shromáždění vojsk všech národů“ → „ve vojsku sebraném ze všech národů“; *zwei mal thůn kan* nově „tolik jako s dvakrát větším válečným lidem“ (viz sporná místa); *kriegsuerstendigen* „znalci války“ → „znalci válečnictví {kriegsuerstendigen}“ (glosář).
- **`1-004r`**: „byť jako člověk nerozumný“ → „byť jsem v tom neznalý“ (zachována závorka originálu); *eingefallen mischbreuch* → „nešvary, které se vloudily“; dlouhé souvětí rozděleno.
- **`1-004v`**: Caesarův příběh rozčleněn na kratší věty, odstraněno opakované „takto“, „ho bolela“ za „se ho dotkla“.
- **`1-005r`**: nadpis „na koni i pěšky“ → „jízdy i pěchoty“; *herbracht* „si přinesli“ → „zachovávají“; řečnická otázka *wo mann bei jnen befindt …* převedena na otázku; *den Kriegen zum besten* → „k prospěchu válečnictví“.
- **`1-005v`**: „nenajdeš“ (2. os.) → „sotva najdeme“; „Zato však neshledávám“ (přidaný protiklad) → „Dosud jsem neshledal“; „vyčerpáno o válečný lid“ → „nezůstane bez / nebyly by zbaveny“ (návaznost na `1-006r` upravena); „více než kolik jich bude třeba dvakrát nebo třikrát“ → „že by jich bylo dvakrát i třikrát víc, než by bylo zapotřebí“.
- **`1-006r`**: dlouhý odstavec o volbě císaře rozdělen do 12 vět; *zwei güter* → „dva statky“; „se vylidnila“ → „nezůstala obnažena“.
- **`1-006v`**: rozděleno do vět; *hřebílka* → „hřbílka“ (i v poznámce); „za sebou rozjímali“ (*hinter vns gedechten*) → „pamatovali na minulost“; „se hnusí“ → „se nelíbí“ (*mißfallen*).
- **`1-007r`**: „nechtěli všichni být sami svými zemany“ → „chtěla být sama sobě pánem {Junckern}“ (shoda podmětu *lid*); „Já jsem ještě vídal“ → „Sám jsem viděl“.
- **`1-007v`**: rada králi rozčleněna; opraven nejasný podmět („udrží se a přivedou kázni o to lépe i ostatní národy“ → „lze o to lépe udržet v kázni a přimět k ní i ostatní národy“).
- **`1-008r`**: **věcná oprava** *wiewol ich derselbigen nit gnugsam verstendig wie noch gewest*: „tehdy ještě nebyl tak zběhlý jako později“ → „Ačkoli jsem jim nerozuměl dostatečně, jako jim nerozumím ani dosud“ (skromnostní topos); visící dativ v odst. 4 vyřešen „[a předložit je] Vašemu královskému Veličenstvu“; „rozmnožovat a rozšiřovat“ → „a navíc rozšiřovalo“ (*mit mehrer*); poznámky 2 a 3 nahrazeny jednou správnou.
- **`1-008v`**: anakolutické *DIe weil … / Vnd dieweil …* převedeno na samostatné oznamovací věty, hlavní věta zůstává v odst. 6.
- **`1-009r`**: *vor andern solches anzufechten* „se toho domáhal“ → „chtěl to před jinými napadat“; odst. 3 bez visícího „A jelikož“; *Kriegßuerstendigen* → „znalce válečnictví“.
- **`1-009v`**: *finantz* „finty“ → „peněžní machinace {finantz}“; *das ist eins* → „To je jedna [příčina].“; „toulavý houf“ (*schwermenden*) → „třeštící houf“ (v souladu se *schwermerei* = třeštění na `1-007r`).
- **`1-010r`**: „po celé válce“ (*im gantzen Krieg*) → „v celém válečnictví“; dlouhý odstavec rozdělen; poznámka 1 zkrácena.
- **`1-010v`**: zrušeny poznámky opakující glosář (*Spiesser*, *knecht*, *Einspenigen*); sjednoceno *Knecht* = „knecht“ v celé stránce (dříve „čeleď“ / „služebníci“); pozn. k *langen Reihen* označena jako nejistá.

## 3. Sporná místa k rozhodnutí

1. **`1-003v`** – *da kan mann mit einem geringen hauffen souil außrichten als mit einem Kriegsuolck/ das vngehorsam … ist/ zwei mal thůn kan.*
   CS nyní: „lze s malým houfem vykonat tolik jako s dvakrát větším válečným lidem, který je neposlušný a špatně spravovaný.“
   Důvod: doslova „kolik válečný lid neposlušný … dvakrát udělat může“; předchozí „stěží dvakrát“ přidávalo význam. Možné i čtení „tolik, co neposlušný lid zvládne za dvakrát“.
2. **`1-008r`** – *… dieselbige zubeschirmen vnd vertheidigen/ vnd mit mehrer dieselbigen zu erweitern/ mit gůt thun werden.*
   CS: „… aby je chránilo a hájilo a navíc rozšiřovalo; to vše s dobrým výsledkem vykoná[^2].“ Smysl *mit gůt* nejistý („dobře“ × „statky, penězi“).
3. **`1-006r`** – *daß mann wol zwei güter mit rüstung daruon erhalten möchte* → „dva statky i s výzbrojí“. Čtení *Güter* opřeno o *ü* v tisku; alternativa „dva dobré [koně]“ zamítnuta.
4. **`1-010v`** – *das in alweg bei den schützen die langen Reihen anzunemen/ verhüt werden* → „zabránit přijímání dlouhých řad“ – význam nejasný (snad hromadné přijímání neprověřených sluhů).
5. **`1-010r`** – *Fendlin* u jízdy přeloženo „praporců“ (glosář `praporec` je pěchotní, u jízdy se jinak užívá `korouhev`). Ponecháno kvůli shodě s `1-010v` (*Fendlein* × *hundert pferden*); zvážit „korouhví“.
6. **`1-002v`** – podpis *Min-tzenberg*: přehláska v tisku nečitelná, ponecháno `Müntzenberg`.

## 4. Návrhy do glosáře

| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| `spravedlnost` (nové) | spravedlnost | Justitien, Justicien, Justitia | pravo | V 1. knize obecně „spravedlnost, soudnictví, výkon práva“ ve vojsku; nyní tyto tvary vedou na heslo `soud`, jehož poznámka (soud pluku pod rychtářem) se k úvodním kapitolám nehodí. |
| `znalec-valecnictvi` (úprava) | znalec válečnictví | + Kriegßuerstendigen, kriegsuerstendigen | velitele | Pozn. nyní popisuje jen srubové posádky 5. knihy; obecně „zkušený, války znalý muž, rádce válečného pána“. |
| `vbersold` (doplnění) | přeplatek | + vbersolden | zold | tvar z `1-010v` |
| `kun` (doplnění) | kůň | + Pferde | jednotky | `1-005v` (pak lze zrušit poznámku o počítání na koně) |
| `pluk` (pozn.) | pluk | Regiment | jednotky | doplnit: „Regiment halten / leiden = držet, snášet kázeň“ – v 1. knize překládáno „kázeň“. |
| `financ` (nové) | peněžní machinace | finantz | zold | Dobové *Finantz* = lichvářské, podvodné peněžní obchody (`1-009v`). |
| `pacholek` (nové) | pacholek | Buben | osoby | Jezdecký sluha, panoš (`1-006v`); odlišit od táborové čeledi *Huren vnd Buben*. |
| `sik` / `houf` | houf | hauffen | jednotky | Malá písmena *hauffen* nejsou v `de`; zvážit samostatné heslo „houf“ (obecně oddíl, zástup) odděleně od „šik“. |
