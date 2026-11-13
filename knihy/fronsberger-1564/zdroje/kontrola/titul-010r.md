# Kontrola překladu – titul, 001r–010r (R1, pilot)

Kontrolováno 20 stran (titul, 001r–010r), kontext 010v jen čten. Všechny strany mají `stav: zkontrolovano`,
`over_strany.py` hlásí 0 chyb; 10 zbylých varování jsou falešná hlášení validátoru (viz Připomínky, bod 1).

U všech stran platí navíc: `de` přepsáno podle skenu (ſ→s, ond→vnd, Herz→Herr, k→tz, å→ä, ů ponecháno,
rozdělená slova spojena, kustody/záhlaví/signatury vypuštěny, „rc.“ → „etc.“, doplněny chybějící iniciály:
*ZVm, WEre, DAs, SEin, WO, WAs, DJß, VNter, ES, DEr*); *Item* jednotně „Dále“; terminologie podle glosáře
(nejvyšší polní hejtman, pokladník, přehlídkový komisař, polní maršálek, drabant, puškař, lodní most, jízda,
šikovatel trénu…); hvězdičkové značky vyřešeny; `pokracovani: true` doplněno u všech pokračujících bloků.

## Přehled stran

| Strana | Zásadní změny |
|---|---|
| titul | OCR titulu přepsán podle skenu („Yd Regiment/fampt … Xoffz“ → „KriegsOrdnung Vnd Regiment/sampt … Roß“); nadpis rozdělen jinak (nadpis = „KriegsOrdnung Vnd Regiment“, podtitul samostatně, „Durch“ připojeno k autorovi); rok opraven LXIIIL → LXIIII; poznámka k „Regiment“ a k dřevořezu. |
| 001r | Nadpis úvodu → `uroven: 1` (podle kniha.yaml). 3 české odstavce sloučeny do 1 bloku podle tisku. Opravy smyslu: „Bývá zmařeno mnoho nevinných vdov“ → „mnoho nevinných se stává vdovami a sirotky“; „nespravedlivé bezpráví činit“ → „nespravedlivě násilí páchat“; „zlá města“ (*böß*) → „nesnadná města“; *freundschafft/anhang* → příbuzenstvo, stoupenci. |
| 001v | 2 odstavce sloučeny; *Büchsenmeyster* „dělostřelci“ → puškaři; „pontonové mosty“ → lodní mosty; *Obersten* → plukovníci; odstraněn zbytek OCR „org/gr“, „n Fürsten“. |
| 002r | Přechod věty z 001v opraven; *Practicken* = úklady + poznámka; „hra, která slibně začala“ → „hra, kterou sám začal“ (*erstlich angefangen*); „jezdecká hotovost“ → jízda; *verzichten* → *verrichten* (sken). |
| 002v | Nadpis „generální polní kapitán“ → nejvyšší polní hejtman; doplněn popis obrázku 1. |
| 003r | Rozpárování opraveno: blok s `de: null` zrušen, 3 bloky podle tisku (pokr. / *Darzů were gůt* / *So gehört auch gedult*). Věcné opravy: „obojí je prospěšné i škodlivé“ → „nebezpečné a škodlivé“ (*sörglich vnd nachtheylig*); vypuštěna spekulace „[nebo lehkovážný]“; „rychle změny… přinucen k okamžité poradě“ zpřesněno; *Landsäß* = zeman. Slovo *erma-nen* přes hranici stran přesunuto celé na 003v. |
| 003v | Slity rozdělené odstavce; *fromm/frommkeyt* = řádný/řádnost + poznámka; „nepřivedl v niveč“ zpřesněno; *Musterherm* → *Musterherrn*; *Obersten vber alle Fůßknecht* = plukovník (ne „nejvyšší velitel“). |
| 004r | **Celá strana posunuta o 1 blok** (CS vždy u následujícího DE) – přepárováno; 1. a 2. DE blok byly jeden odstavec tisku („in an/Der weg“ = *in ander weg*) – sloučeny. *Spiel* = hudba (pozn.), *Reuers* (pozn.), jmenovací listina → služební list. |
| 004v | Nadpis „Der Kriegßräth vnd Musterherren / Befelch vnd Ampt“ sloučen do jednoho (byl rozdělen na 2 nadpisy); zdvojený řádek OCR odstraněn; mustermajstři → přehlídkoví komisaři. |
| 005r | *abzelen* (sken) místo „abges fen“; *finantzen* + *rachtungen* poznámky; *Fändlin* „roty“ → praporce; přísaha sloučena do 1 bloku; *Gegenschreiber* = protipísař (pozn.). |
| 005v | Pfennigmeyster → pokladník; *Glauben* = úvěr; odstraněn chybný doplněk „[auf gelt und wechsel]“; nadpis úřadu → `uroven: 2`; *Troßpferde* = koně pro trén. |
| 006r | DE blok „Besoldung… / Jhm werden gehalten…“ rozdělen na 2 odstavce podle tisku; 2 CS odstavce proviantmistra sloučeny; *gereysige Pferde* = jezdečtí koně (ne „se svými jezdci“). |
| 006v | *wölle* (sken, OCR „wie le“) doplněno; drobné stylistické úpravy. |
| 007r | Nadpis přeložen bez celého DE v {…}; generální polní kapitán → nejvyšší polní hejtman. |
| 007v | *hellen hauffen* + poznámka; *Oberster* = plukovník (jediný pluk pěchoty); *Knecht* = knechti, ne „žoldnéři“. |
| 008r | Levitenrock – poznámka; *berathschlagt* (sken); *Missiuen* – poznámka; trumpetista → trubač. |
| 008v | Doplněn popis obrázku 2; *Fändlin* „roty“ → praporce; *Zal oder Pfennigmeyster* = platebníci či pokladníci. |
| 009r | Seznamy rozděleny podle tisku: blok `odstavec` s odrážkami → 2 bloky `seznam` (7 + 3 položky) s vlastními nadpisy; „Item des General Obersten“ jako nadpis 3; „polní maršál“ → polní maršálek. |
| 009v | Seznam pěchoty z `odstavec` → `seznam` (15 = 15); poznámky tisku „gehören vnter den Schuldheyssen / Profosen“ (svorky) připojeny k poslední položce skupiny; *Die Schneller* = zvedači + pozn. (podle l. XXXIv); *Zeugwart* „zbrojíř“ → zbrojní správce; Hurnweybel „ubytovatel markytánek“ → šikovatel trénu. |
| 010r | Poznámka o *Fürer* přesunuta ke správnému místu a zpřesněna (podle popisu úřadu na skenu 101); *Ambesaten* + pozn.; *gemeyn Weybel* = obecní šikovatelé; *was der jeder befelch* (sken) – věta přeložena znovu. |

## Sporná místa (k rozhodnutí)

1. **003v** *„deren jeder erwehlet vnnd besetz/auch nachmals alle ämpter vnter sein Regiment gehörig … soll er … versehen“* –
   čteno jako „z nichž každý má být vybrán a dosazen. Potom má [nejvyšší hejtman] obsadit všechny úřady…“. Možné je i čtení
   „z nichž každý vybere a obsadí všechny úřady svého pluku“. Navrženo ponechat první čtení.
2. **003r** *„der jung zu viel mißgläubig“* – přeloženo „příliš nedůvěřivý“. Smysl (u mladého spíš lehkověrnost) naznačuje
   možnou tiskovou chybu za *leichtgläubig*; bez poznámky.
3. **005r** *„seltzam schnöde rachtungen … auffnemen“* – přeloženo „snášet podivné a nestoudné smlouvání“ (+ pozn.).
   *Rachtung* = narovnání/úmluva; alternativa „nestoudné nabídky na dohodu (úplatky)“.
4. **009v** Svorka *„gehören vnter den Profosen“* stojí u řádků Steckenknecht/Nachrichter; ze skenu nelze určit, zda zahrnuje i
   Hurnweybel a Stockmeyster. Česky ponecháno stejně nejednoznačně (u posledního řádku).
5. **titul** *„vor oder in Besatzungen“* – „před posádkami nebo v nich“ (= při obléhání i v posádce). Alternativa
   „při obléhání nebo v posádkách“ je srozumitelnější, ale interpretační.
6. **titul** „Regiment“ přeloženo podle `kniha.yaml` jako „pluk“; v titulu jde spíš o „zřízení, správu vojska“ (vysvětleno
   poznámkou). Zvážit název „Válečný řád a zřízení“.
7. **Chybějící dřevořezy**: na titulu, 004v (váleční radové – 4 muži v rozhovoru, pes) a 007r (nejvyšší profous s holí před
   ležením) jsou v tisku celostránkové dřevořezy, ale v `obrazky/` pro ně není soubor, takže nejsou v datech. Navrhuji je
   vyříznout ze skenů (obrazek13+…) a doplnit bloky `obrazek` – pravděpodobně se to týká i dalších úřadů v 1. knize.
8. **003v / 007r / 008r** *der Oberst* bez přívlastku označuje v 1. knize nejvyššího polního hejtmana (Generála), ne
   plukovníka; překládáno „nejvyšší [hejtman]“. Kde jde o velitele pluku (*Oberster der Fůßknecht*), „plukovník“.

## Návrhy do glosáře

| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| vudce | vůdce | Fürer, Furer | velitele | Poddůstojník praporce volený z obce; jde před šikem a vede knechty na pochodu, jinak pomáhá šikovatelům; u jízdy jezdec, který s kvartýrmistrem rozděluje ubytování. Bral dvojitý žold. |
| lanspesat | lanspesát | Ambesaten | jednotky | Z ital. *lancia spezzata* – zkušený voják s vyšším žoldem, zástupce rotmistra. |
| zvedac | zvedač | Schneller | delostrelectvo | Pomocník u dělostřelectva (8 mužů pod „zbrojmistrem zvedačů“): překládá těžká děla z vozu na vůz, maže je, nakládá a skládá munici. |
| protipisar | protipísař | Gegenschreiber | zold | Kontrolní písař pokladníka, vede druhý záznam příjmů a výdajů. |
| revers | revers | Reuers, Reuerß | pravo | Písemný závazek, jímž přijímaný úředník stvrzuje podmínky služebního listu. |
| trubac | trubač | Trommeter, Trometer | velitele | Polní trubač; doprovází herolda a troubí k utišení a signály. |
| hudba | hudba | Spiel, Pfeiffer vnd Trommenschlager | velitele | „Spiel“ – pištec a bubeník praporce či velitele. |
| uklady | úklady | Practicken, practicken | velitele (nebo nová kat. „politika“) | Tajná jednání, pletichy; u pokladníka též finanční jednání (*practicken auff gelt vnd wechsel*). |
| finta | finta | Finantz, finantzen | zold | Lest, podvod, lichva – zvl. podvody při přehlídce. |
| helly-hauf | celý houf | heller Hauff, hellen hauffen | jednotky | Veškeré shromážděné mužstvo, hlavní voj. |

Doplnit tvary `de` u existujících hesel: *nejvyssi-polni-hejtman* + „General Oberster, Obersten Feldthauptmann, General
Obersten Feldthauptmann“; *dvojity-zold* + „Toppelsöld, doppel sold“; *dvojzoldner* + „Toppelsöldner, Toppelsöldnern“;
*pokladnik* + „Zalmeyster“ (platebník; nebo samostatné heslo); *obecni-sikovatel* + „gemeyn Weybel“; *prehlidkovy-komisar*
\+ „Musterherrn“ (s -rrn); *profous* + „Oberster Feldtprofoß, Feldt Profosen“; *sik* – *heller Hauff* viz výše;
*jizda* + „gereysige“. U hesla *pluk* zmínit i titulní význam „zřízení“.

Rejstřík osob a míst: Johann Lechler (tiskař), Sigmund Feyerabend a Simon Hüter (nakladatelé), Frankfurt nad Mohanem (titul);
Titus Livius (003r, už v glosáři).

## Připomínky k pravidlům

1. **Validátor – falešná varování**: kontrola `nepouzivat` hledá i uvnitř `{…}` (hlásí *{Trabanten}*, *{Profosen}*) a
   „polní maršál“ nemá hranici slova na konci, takže chytá i správné „polní maršálek“. Navrhuji před kontrolou odstranit
   `{…}` a regex ukončit `\b`.
2. **Slovo dělené přes hranici stran** (*erma-nen*, *er-fordert*, *verzeychne*): pravidla to neřeší. Použil jsem
   „celé slovo patří na stranu, kde končí“ (tj. na následující). Prosím zapsat do § 1.
3. **Svorky a marginální poznámky v seznamech** (009v): `seznam` nemá jak zachytit „gehören vnter …“ pro skupinu položek.
   Připojil jsem text k poslední položce skupiny („– gehören vnter den Profosen.“). Buď to schválit, nebo zavést pole
   `pozn` u bloku.
4. **Iniciály**: OCR vynechává zdobnou iniciálu (*Ere, As, Ein*). Doplňoval jsem ji v podobě tisku s druhým velkým
   písmenem (*WEre, DAs, SEin*). Rozhodnout, zda normalizovat na *Were, Das, Sein*.
5. **Znaky tisku**: OCR „å“ = *a* s nadepsaným *e* → psal jsem *ä*; *ů* ponecháno; *rc.* → *etc.*; *ñ/ē* (vñ, gegē) →
   rozepsáno (vnd, gegen). Doporučuji zapsat do § 2, ať to kontroloři dělají shodně.
6. **{…} u seznamů úřadů**: v seznamu je každá položka termín; dával jsem `{…}` jen k prvnímu výskytu na stránce a u
   opakovaných („jeho poručík“) vynechal. Mohlo by se výslovně uvést.
7. **„Oberst“ bez přívlastku** – glosář ho mapuje jen na „plukovník“, ale v 1. knize jde často o nejvyššího polního
   hejtmana. Doplnit do pozn. hesla *plukovnik*, aby kontroloři nepřekládali mechanicky.
8. **Hesla glosáře `pacholek` (cs „pachole“, de Jung) a `profousuv-pacholek`** – *reysiger Knecht* (jezdecký čeledín)
   jsem přeložil „jízdní pacholek“, což se může plést s „pachole“. Zvážit sjednocení (pachole = Jung, pacholek = Knecht).
9. **Obrázky**: chybí soubory pro většinu dřevořezů 1. knihy (viz sporné místo 7); pravidla by měla říct, zda je kontrolor
   smí vyříznout ze skenu a přidat.
10. Úroveň nadpisů v 1. knize: kapitoly o úřadech jsem dal `uroven: 2`, přísahy a podnadpisy seznamů `uroven: 3`
    (souhlasí s kniha.yaml). „Item des General Obersten“ (velké písmo nad seznamem) jsem dal jako nadpis 3.
