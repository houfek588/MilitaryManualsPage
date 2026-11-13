# Překlad 023r – 029r (dávka T2)

Strany: 023r, 023v, 024r, 024v, 025r, 025v, 026r, 026v, 027r, 027v, 028r, 028v, 029r
Všechny mají `stav: prelozeno`. `over_strany.py … --prisne` → 0 chyb, 0 varování.
Německý text jsem u všech stran znovu sestavil podle skenů 53–65. OCR bylo hodně chybové (f/ſ, k = tz, chybějící iniciály).

## Obsah

- **023r** – konec reversu puškařů (přísaha, doba služby, žold, odchodné). Puškaři se najímají na celé tažení, někdy zvláštním služebním listem. Následují povinnosti puškařů: být stále u děla, mít oheň a zápalné šňůry, nocovat u dělostřelectva, při poplachu se hlásit u děla. Přejezd hluboké vody: záď děla zvednout a zápalný otvor zalepit. Při obléhání nemají od děl odcházet, stravu jim platí vrchnost.
- **023v** – nadpis oddílu „Stav, řád a zřízení nejvyššího zbrojmistra a osob dělostřelectva“ s dřevořezem (obrazek6). Nejvyšší polní zbrojmistr je třetím válečným radou, po nejvyšším polním hejtmanovi a polním maršálkovi. Jeho poručík se účastní válečných porad.
- **024r–024v** – předpoklady zbrojmistra (šlechtic, rozum) a rozdíl mezi zbrojmistrem zbrojnice (Haußzeugmeister) a polním zbrojmistrem. Kapitola „O úřadu zbrojmistra“: měsíční a „slepé“ přehlídky vozních koní, podvody vozků, zákaz převážet cizí náklad, denní odlehčování vozů, záložní vozní koně pod vozmistrem.
- **024v–025v** – kapitola „Úřad, velení a přísaha nejvyššího zbrojmistra“: co má znát (pořadí pochodu, lodní mosty, podkopy, ležení, šance, ohňostroje), kde má být na pochodu, dohled nad municí. Následuje znění přísahy (spory s válečným pánem rozhodují čestní válečníci).
- **026r** – vydržování nejvyššího zbrojmistra: 100 zlatých měsíčně, 6 zbrojných koní, tlumočník, vozy, kuchař, drabanti, kaplan, hudba, písaři, pokladník a ranhojič dělostřelectva.
- **026r–027r** – výsady: kořist munice a zbraní z dobytého místa patří zbrojmistrovi. Puškařům patří prach a koule v dělech a největší zvon na poplach (výkupné). Šancmistrovi patří dřevo ze šancí. Dělostřelectvo poskytuje útočiště tomu, kdo zabil bez úmyslu (24 kroků od děla). U dělostřelectva a v šanci je pod trestem smrti zakázáno tasit zbraň.
- **027r** – úřad a přísaha pokladníka (platebníka) dělostřelectva. Poručík zbrojmistra: v nepřítomnosti zbrojmistra má jeho moc, bere žold hejtmana pěchoty.
- **027v–028r** – úřad šancmistra: průzkum terénu před obléháním, kryt pro děla a puškaře, jízda napřed s jízdní korouhví a zvědy, opravy cest, šancovní koše. Žold jako hejtman pěchoty.
- **028r–029r** – šancíři: nejméně 400, roty po 12 s voleným rotmistrem, plátěný praporec s motykami a lopatami, bubeník bez pištce. Roty se tvoří podle nářadí. Žold 4 zlaté, jejich hejtman asi 4 žoldy.
- **029r** – kapitola „Velení, stav, úřad a žold zbrojního správce“: inventář, denní zápis spotřeby, stráž u vozů s prachem (vozová hradba), suché sudy, pořadí vozů na pochodu (pokračuje na 29v).

## Úpravy struktury

- 023r: první blok `pokracovani: true` (navazuje na 22v). `pokracovani` mají také 025r, 027r, 027v, 028r, 028v a 029r.
- Nadpisy, které byly v YAML jako `odstavec`, jsem změnil na `nadpis`.
  - **Úroveň 2:** 023v „Nuh folgt der Stath…“, 024r „Deß Zeugmeysters Ampt betreffent“, 024v „Deß Obersten Zeugmeysters Ampt/Befelch vnd Eyd“, 027r „Pfenningmeysters … Befelch vnd Ampt“, 027r „Zeugmeysters Leutenants befelch vnd Ampt“, 027v „Schantzmeysters Ampt…“, 028r „Der Schantzbawren … befelch/stath vnd besoldung“, 029r „Zeugwarts befelch…“ (byla již).
  - **Úroveň 3:** „Forma deß Zeugmeysters Eyd“, „… vnterhaltung“, „… freiheyt vnd gerechtigkeyt“ (4×), „Volgt jetzt … Pfenningmeysters … Eyd“.
- 026r: soupis vydržování (12 krátkých položek „Item ein Koch.“ atd.) jsem převedl na `seznam`, podobně jako sazebník na 22r. Delší položky s celými větami (ranhojič, koně písařů) zůstaly jako `odstavec`.
- 028r: OCR rozdělilo odstavec „ITem zu der Arckelley … vierhundert Schantzbawren / also daß …“ na dva bloky. V tisku je to jeden odstavec, sloučil jsem ho.
- 029r: doplnil jsem 4 odstavce, které v YAML chyběly (Puluerwägen, Zeugdiener, sudy na prach, pořadí vozů). Stávající překlad jsem celý přepsal: používal zakázané termíny „zbrojíř“ a „zbrojní mistr“, „artilerie“ a „velitel vojska“ místo „válečný pán“.
- Dělení přes hranici stran: 027r/027v „befol-|hen“ → „befolhen“ celé na 27v. 027v/028r „Büch-|senmeyster“ → celé na 28r. 029r končí slovy „auch der nächst“ („hin-|den“ patří na 29v).
- **Mimo dávku:** 029v je `chybi_original`. Až se bude doplňovat, musí začínat `pokracovani: true` a slovy „hinden oder vor einer nit was der ander fürt …“ (cs: „za někým nebo před ním, neví, co veze ten druhý …“).
- 023v: obrázku 6 jsem doplnil `popis`.

## Místa ověřená ve skenu (sk. 53–65)

- Sk. 53: „Eydt“ (OCR „Endt“), „Büchßenmeyster“ (tisk s ß), „deß abzugs“, „Kriegßleuth“, „zündtrüten“, „Herꝛschafft“ → Herrschafft.
- Sk. 54: iniciála „EIn jeder“, tisk má „Deßglezchen“ (tisková chyba, ponecháno).
- Sk. 55: „Feldtzeugmeyster“, „besteſtelt“ (zdvojená slabika v tisku, ponecháno jako „bestestelt“), „beytroß“, „beytgüter“, „im einsetzen vnd fahren“.
- Sk. 56: „zertheylen“ (OCR „sathey len“), „Zeugwart/Musterherꝛ/Zeugmeyster“, „eygen leib“ (OCR „engen“).
- Sk. 57: „von od' zu den feindē“ → „von oder zu den feinden“, „mit gräben zunöhten“, „so dem ist es gar gůt“.
- Sk. 58: iniciála „WIewol“, „Amptleuth“, „was jeglicher kan“; v OCR chyběla část věty „gegeben wirdt / So folgt doch jetzt desselbigen vngefährlich ein gemeyne“.
- Sk. 59: „MAn bestelt“, „Eim Zeugmeyster“, „Troßpferdt“, „Tollmätschen“, „Küchenwagen“, „Wundartzet“, „deß Zeugs gebrauchen“ (OCR „Brugs“).
- Sk. 60: „drittheyl“, „Kriegßherrē“, „Först/Zöll“, „eroberūg“, „Gestreb/Ansetz“, „Hürt oder Brücken“. V YAML bylo zdvojené „auffgeben auffgeben ode“ a smetí „so ft/ fo follder soll der Zeugmeyster)“ – odstraněno.
- Sk. 61: iniciála „SEin befelch“, „vinantz oder vnerber practicken“, „gewer sein wölle“.
- Sk. 62: „noch ein pferdt oder zwen Trabanten“ (viz sporná místa), „wasserfäll in hohen wägen“, „vor Besatzungen“, „Rennfänlin“, „räncken“.
- Sk. 63: tisk má „Santzbawren“ (tisková chyba, ponecháno), „was sie ein gantzen Monat kosten“.
- Sk. 64: „mit vnd außgang deß Monats“ (sic), „Reuthawen“.
- Sk. 65: „vier Söld“ (OCR „view/vien Sold“), „gescharmützlet“, „darnach man sich dañ zurüsten wiß.“ (OCR „dari … wißerde“), „gehäben“, „geschwelten wasser“.

## Sporná místa

1. **23r** „das geladen Geschütz/bey dem ansatz auff das höchst auffrichten … sonst schadet es nichts wie tieff das maul vornen in das wasser hange“ → „na zadním konci {ansatz} co nejvýš zdvihnout … jinak nevadí, jak hluboko visí ústí ve vodě“. Ansatz vykládám jako záď hlavně: vzduch uzavřený v hlavni nepustí vodu k náboji. Je k tomu poznámka.
2. **24r** „kauffen beytroß/schwach vnd kleyn“ → „podřadné koně {beytroß}“. Slovo jsem jinde nedoložil. Také „so geben sie auch etwann die besten Pferdt an die statt“ → „nejlepší koně dávají pryč a nahrazují jinými“ (smysl je nejistý).
3. **24r** „Haußzeugmeyster“ → „zbrojmistr zbrojnice“ (správce stálé zbrojnice), poznámka.
4. **26r** „Item ein Jungen zu der Fůßknecht rüstung“ → „pachole na pěší zbroj“ (patrně zbroj zbrojmistra pro boj pěšky).
5. **26v** „Gestreb/Ansetz“ → „vzpěry, nástavce“. „Ansetz“ je nejisté. „Hürt oder Brücken darauff man scheusset“ → „lísy nebo podlahy, z nichž se střílí“ (dělové plošiny).
6. **26v** „den drittheyl näher dann es … werth ist“ → „o třetinu levněji“.
7. **27r** „es were dann ein sonder person so ein Ampt bey der Arckelley hette“ – smysl výjimky je nejasný, viz poznámka.
8. **27v** „noch ein pferdt oder zwen Trabanten“ – podle obdobného místa o šancmistrovi (28r: „eins oder zwey gerüste Pferdt“) jde patrně o chybu tisku. Přeloženo podle tisku, s poznámkou.
9. **27v** „wasserfäll in hohen wägen“ → „vodní spády ve vysokých cestách“. Alternativní čtení „Wogen“ (vysoké vlny) je v poznámce.
10. **27v** „darumb můß man offt ander gewöhnliche weg suchen“ → „jiné, obvyklé cesty“ (tj. vyhnout se horským zkratkám). Formulace je sporná.
11. **28v** „mit vnd außgang deß Monats“ – patrně chybí „eingang“, poznámka.
12. **25v** „im vorzug vornen …, im nachzug … dahinden“ – Vorzug/Nachzug jsem přeložil podle glosáře jako předvoj a zadní voj („při tažení proti nepříteli vpředu v předvoji, při tažení od nepřítele vzadu v zadním voji“).
13. Přepis zkratek podle pokynu: vñ → vnd, dañ → dann, Hauptmañ → Hauptmann, Herꝛ → Herr. Zkratka ꝛc. se v dávce nevyskytla.

## Návrhy do glosáře

- `zbrojni-sluzebnik` – cs: zbrojní služebník; de: [Zeugdiener, zeugdiener, Zeugdienern]; kategorie: delostrelectvo; pozn: Nižší služebník dělostřelectva pod zbrojmistrem – roznáší rozkazy, pomáhá udržovat pořádek na pochodu, dohlíží na práce; jezdci písařů a úředníků slouží „jako ostatní zbrojní služebníci“.
- `zbrojni-pisar` – cs: zbrojní písař; de: [Zeugschreiber]; kategorie: delostrelectvo. Nyní je v hesle `pisar`, ale s ustáleným překladem „zbrojní písař“.
- `zbrojmistr-zbrojnice` – cs: zbrojmistr zbrojnice; de: [Haußzeugmeyster, Hauszeugmeister]; kategorie: delostrelectvo; pozn: Správce stálé zbrojnice v zemi; na rozdíl od polního zbrojmistra není válečným radou.
- `odchodne` – cs: odchodné; de: [abzug, Abzug]; kategorie: zold; pozn: Částka vyplácená žoldnéři při propuštění, zvl. před uplynutím smluvené doby.
- `zapalna-snura` – cs: zápalná šňůra; de: [Zündstrick, Zündtstrick, Zundtstrick]; kategorie: delostrelectvo; pozn: Doutnák – pomalu doutnající provaz k zapalování děl a ručnic.
- `zapalovaci-hul` – cs: zapalovací hůl; de: [zündtrüten, Zündrute]; kategorie: delostrelectvo (pilot 22r i 23r).
- `zbrojny-kun` – cs: zbrojný kůň; de: [gerüst Pferd, gerüste Pferdt, gerüster Pferdt]; kategorie: zold; pozn: Kůň s ozbrojeným jezdcem, za něhož se platí jako za jezdce.
- `vystroj-zeug` – „Zeug“ ve významu dělostřelectvo / výzbroj a vojenská hotovost (023r–029r často „bey dem Zeug“). Doporučuji doplnit pozn. k heslu `delostrelectvo` nebo `zbrojni-vuz`.
- `utociste` – cs: útočiště (výsada); de: [freiheyt, Freiheit]; kategorie: pravo; pozn: Právo azylu u dělostřelectva pro toho, kdo zabil bez úmyslu (26v–27r). V nadpisech „freiheyt vnd gerechtigkeyt“ = výsady a práva.
- `tlumocnik` – cs: tlumočník; de: [Tollmätsch, Tollmätschen]; kategorie: velitele.
- `sancir` – doplnit de: Schantzbawren, Schantzbawrn, Schantzbawr. `sancmistr` – doplnit de: Schantzmeyster, Schantzmeysters.
- `zalmistr` (platebník) – doplnit de: Zalschreibers, Zeug Zalschreiber.
- `bubenik` – cs: bubeník; de: [Trommenschlager]; kategorie: velitele (případně do hesla `hudba`).
- `motyka`, `krumpac`, `lopata` (Hawen, Bickel, Reuthawen, Schaufel) – zvážit jedno heslo „nářadí šancířů“ v kategorii opevneni.

## Osoby a místa pro rejstřík

V dávce nejsou žádná vlastní jména osob ani míst.
