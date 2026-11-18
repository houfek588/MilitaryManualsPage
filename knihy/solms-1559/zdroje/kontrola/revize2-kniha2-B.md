# 2. revize – Druhá kniha, dávka B (013r … 023v)

Rozsah: 22 stran (skeny 117–138): závěr „Odpovědi“ císaři o rouhání a justici (013r–014r), dřevořez nejvyššího
polního hejtmana (014v) a kapitola o nejvyšším polním hejtmanovi (015r–023v). Sousedé `012v` a `024r` jen čteni,
návaznost vět přes hranice stran sedí (013r ← 012v, 023v → 024r „oblehl-li městečko / belegert …“).
Plynulost „středně“ podle `ZADANI_REVIZE2.md`: dlouhá souvětí dělena na věty v rámci bloků; struktura bloků, `sken`,
`id`, `stav`, `overeno_clovekem: false` beze změny; všechny přechody `pokracovani: true` dál sedí s tiskem.
Na stranách už byla před revizí (neodevzdaná pracovní změna) provedena záměna *Oberst/Oberster/Obersten* →
„plukovník“; revize ji zachovala a doplnila zbývající místa.

Kontrola: `python -I nastroje/over_strany.py knihy/solms-1559 013r … 023v --prisne` → **22 stran, 0 chyb, 0 varování**.

## Opravy `de` podle skenů (BSB IIIF, staženo 119, 122, 125, 126, 128, 130, 131, 132)

| strana | bylo | tisk (sken) | pozn. |
|---|---|---|---|
| 015v | zu rosß vnd fuß / außserhalb | **roß / ausserhalb** | artefakt OCR |
| 015v | bedörffen | **bedorffen** | |
| 017r | alle Kriegsherrn gewarnet | **Kriegsherren** (Kriegsherꝛen) | |
| 017r | zum abzucht | ponecháno | tisková chyba za *abzug*, nová pozn. 2 |
| 017v | **oder gleich** / wie am anfang gemelt | **ob er gleich** | mění smysl; cs „i kdyby měl … plnou moc“ tím potvrzeno |
| 017v | (wie … Kriegsleut auch gepflegt den | **gepflegt) den** | chybějící závorka |
| 018v | festen pasß | **paß** | |
| 018v | zuuersichtlichen abzugs | **zuuersichtiglichen** | |
| 020r | Darzas … dammen stende | **Darras** (Darꝛas) … **stendt** | pozn. 1 přepsána (OCR četlo ꝛ jako z) |
| 021v | zu rosß vnd fuß | **roß** | artefakt OCR (stejný jako 015v) |
| 022r | leib vn̄ leben | **vnd** | rozepsání zkratky |

Ověřeno beze změny: 014r *abkommmen* (tisk opravdu tři m), 018v *kan auh nicht* (tisk *auh*), 015v *kreigsleuten*
a *oder jr bedarff* (tisk), 020v *ein gewichter hauff* (tisk), 019v *brennen* ×2 (tisk; viz sporná místa),
dělení *Ober-|sten* 019r/019v a *ler-|men* 018v/019r správně na straně, kde slovo končí.

## Hlavní změny `cs` po stranách (ukázky)

- **013r** „klást své zlo a svou pýchu před Boha“ → „klást svou nepravost a svou čest výše než Boha“ (*ehr*, ne pýcha);
  souvětí o kazatelích rozděleno.
- **013v** „vzmáhající se zlo“ → „zlo, které se vloudilo“ (*eingebrochen*); titul „přísní a cti pevní“ → „stateční
  a slovutní“ (Gestrengen vnd Ehrnuesten – ustálený český kancelářský ekvivalent); dlouhé souvětí o šlechtě rozděleno.
- **014r** „jsou zištní a v tom všem nekladou … před chamtivost“ → „hledí jen svého zisku a nekladou … nad chamtivost“.
- **015r** „(jichž má mít … rozumný plukovník dostatek)“ → „(a rozumné válečné rady má mít každý válečný pán či
  plukovník)“ – *verstendiger* patří k radám, „dostatek“ přidán; **obrácená logika** „mínění se uvádí proto, aby …
  nezískal přívržence“ → „proto, že … si získá přívržence a vytvoří labyrint“; „ptát se tak, že zamýšlí“ → „oznámit,
  že je odhodlán, a požádat o radu, jak to započít“.
- **015v** „jinak by šik nemohl zůstat v pořádku“ → „pochod“ (*zug*); „na rozkaz velitelů“ → „plukovníků {obersten}“.
- **016r** „hejtmana {hauptman} pro píci“ → „pícovacího hejtmana {Futer hauptman}“, „pícnění“ → „pícování“ (glosář);
  „čekat a navazovat“ (přidáno) → „dbát jeden na druhého“; blok o šarvátkách přestavěn: *erzeigen* patří k „povaze
  místa a nepřátel“, ne k „ukázat lid“; doplněno {Scharmützel}.
- **016v** dlouhé souvětí o strážích rozděleno; „je (heslo) nesmí dávat oznamovat“ → „ho nemá…“ (*soll*).
- **017r** „neboť poněvadž trén…“ přestavěno na samostatné věty; pětičlenný výčet „aby …, aby …“ převeden na řadu
  „má …; má …“; „útočným předním houfům“ → „běžícím houfům {lauffenden hauffen}“ (jednotně se 064v).
- **017v** „nezůstal bez hlavy a neztratil důvěru, z nedostatku vůdce“ → „s jistotou nezůstal bez hlavy, neboť když
  chybí hlava“ (přídavek odstraněn, „vůdce“ je glosářový termín pro *Fürer*); „útočné pohyblivé houfy“ → „běžící houfy“.
- **018r** „rozdělovač kořisti“ → „mistr kořisti“ (glosář *Beutmeister*, i 021r, 021v); „být zpitý“ zkráceno.
- **018v** „nadějného odchodu“ → „pravděpodobného odtahu“ (*zuuersichtiglich*); „nějaký velitel ležel“ → „plukovník“;
  „zatlouci a zničit“ → „zatlouci“ (přídavek).
- **019v** „plukovník {Oberster der Knecht} pěchoty“ → „plukovník knechtů {Oberster der Knecht}“; **„zapalování“ →
  „přiražení k městečku {brennen}“** (2×, nová pozn. 1 – viz sporná místa); souvětí rozdělena.
- **020r** „studny a prameny vedené žlaby“ → „přívody studní a kašen vedené žlaby“; „hloubením štol“ → „hloubením
  připraveno k odstřelu či k útoku“; „horníků k podkopávání a odstřelování“ → „k odstřelování“ (text má jen *sprengen*).
- **020v** „nechat provést odstřel ze všech houfů“ → „mít k útoku seřazeny [oddíly] ze všech houfů, dát odpálit
  [nálože]“; „v písmu“ → „písemně“; „střílejí do průlomu“ → „dovnitř“ (*hinein*); „držet pohotovost nad útokem“ →
  „během útoku držet stráž“ (*vber dem sturm halten*, jednotně i 021r místo „kryjí pole“).
- **021r** anakolut „Jakmile … rozdělí …, ostatní práva … se uvedou“ rozdělen; „nemá být činěna křivda“ → „nemá se
  dopouštět lsti“ (*gefahr gebrauchen*); „jednomu jezdci … jednomu pěšímu knechtovi“ → „jezdci … pěšímu knechtovi“.
- **021v** „bez úmyslné újmy“ → „v dobré víře“ (*vngefehrlich*).
- **022r** **„bývá takové jednání vždycky zarazeno“ → „rozhoduje se o nich vždy podle okolností“** (nová pozn. 1);
  „dopustí se násilí [znásilnění]“ → „znásilnění“; „Někteří plukovníci tvrdí“ → „chtějí“ (*wöllen*), „nezaviněného
  [náhodného]“ → „neúmyslného“; „Každý válečný pán nemá … přít se“ → „Žádný válečný pán se nemá přít“.
- **022v** „výběrčí výpalného“ → „výpalný mistr {Brantmeister}“; „žhářská korouhev“ → „paličský praporec {Brenfanen}“
  (oboje glosář); „vrchní výběrčí výpalného“ → „plukovníkův výpalný mistr“ (nová pozn. 1); „rady {Räth}“ → „porady“.
- **023r** **chybná vazba výčtu**: drabanti, tlumočníci a koně nejsou povinností válečného pána, nýbrž „pokud jde o
  drabanty …, koně a koníky {Kleppern} pro jeho osobu, postupuje se podle služebního listu“; „ručit“ → „zodpovídat
  se“; souvětí „Před vším tím … před tím má“ přestavěno.
- **023v** „dorážející na něj s plnou vážností“ → „usilovně dorážejí“; „útočným pohyblivým houfům“ → „běžícím houfům“.
- **014v** (dřevořez) popis ponechán.

## Sporná místa k rozhodnutí

1. **019v *brennen*** – DE: „Wiewol von brennen meldung geschicht … daß im brennen nur schadt empfangen“; dříve CS
   „zapalování“, nyní „přiražení k městečku“. Důvod: předchozí článek „mit den Schützen … berennen lassen“,
   následující „Als bald dann ein Fleck berent“; „schadt empfangen“ (škodu utrží útočník) nedává smysl u pálení.
2. **022r *abgeschafft*** – „wirt doch solches zu jeder zeit auch abgeschafft“; CS nyní „rozhoduje se o nich vždy
   podle okolností“. Alternativa „vždy se také zakazuje“ smyslově nesedí s výčtem způsobů kapitulace.
3. **022v *der Oberst Brantmeister*** – CS „plukovníkův výpalný mistr“; možné i „nejvyšší výpalný mistr“.
4. **015v *vff beuelch der obersten*** – podle rozhodnutí „plukovníků“; může jít obecně o „představené“.
5. **Oberst = vrchní velitel** – v celé kapitole (015r–023v) jde o nejvyššího polního hejtmana; podle rozhodnutí
   autora všude „plukovník“, což čtenáře může mást (např. 015r „plukovníci jsou co do postavení různí – knížata,
   hrabata“). Zvážit jednu poznámku na 015r, že *Oberst* zde označuje nejvyššího polního hejtmana.
6. **Brenfanen** – glosář „paličský praporec“; skládá se ze střelců, ale v kapitole o jízdě – rozhodnout, zda
   nepatří „paličská korouhev“ (pravidlo Fendlin/Fanen u jízdy = korouhev).
7. **021v *Reisigen vnd ringe Pferde*** – {ringe Pferde} odkazuje na heslo „lehká jízda“, zde jde o koně.

## Návrhy do glosáře

| id | cs | de | kategorie | pozn. |
|---|---|---|---|---|
| bezici-houf | běžící houf | lauffenden hauffen, lauffender Hauff | jednotky | jinak `ztraceny-houf` doplnit o tyto tvary (064v je ztotožňuje) |
| futerhauptman | (doplnit tvar) | Futer hauptman | velitele | tvar z 016r |
| vozka | (doplnit tvar) | Wagenman | osoby | 015v |
| prirazeni | přiražení (obklíčení) | berennen, berent, brennen | opevneni | rychlé obklíčení a prohlídka místa jízdou a střelci |
| klepr | koník (klepr) | Klepper, Kleppern, Klepperlin | zbrane | malý jezdecký či cestovní kůň |
| taras | taras | Darras, Tarras | opevneni | 020r |
| horník | horník | Ertzknappen | osoby | k odstřelování a podkopům |
| polni-lekar / osobni-lekar | (doplnit tvar) | Feld vnd leib Artzt | osoby | 023r |
| titul | stateční a slovutní | Gestrengen vnd Ehrnuesten | osoby | šlechtický predikát (013v) |
