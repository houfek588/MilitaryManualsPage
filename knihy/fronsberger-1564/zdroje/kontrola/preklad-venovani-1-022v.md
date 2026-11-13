# Překlad venovani-1 – 022v (dávka T1, pilot)

Strany: venovani-1, venovani-2, predmluva-1, predmluva-2, 017v, 018r, 018v, 019r, 019v, 020r, 020v, 021r, 021v, 022r, 022v
Všechny mají `stav: prelozeno`; `over_strany.py … --prisne` → 0 chyb, 0 varování.

## Obsah

- **Věnování (sk. 3–4)** – Kryštofovi, vévodovi württemberskému a z Tecku, hraběti z Montbéliardu. Staří trávili volný čas rytířským cvičením nebo psaním knih. Autor podle vzoru Vegetia, Livia a Frontina popisuje současné válečné zvyklosti a zbraně, aby se zachovaly pro potomky. Dílo rozdělil na pět dílů. Věnování končí nedokončenou větou („als nemlich im ersten theil wie hernach volgt“), viz poznámka na venovani-2.
- **Předmluva ke čtenáři (sk. 5–6)** – Nikdo nevyhoví všem. Autor si poznámky o válečných věcech z doby Karla V. psal pro sebe, vydal je na naléhání přátel. Kritikům odpovídá, že z knihy se válčit nenaučí – je třeba praxe („železní komáři“ kolem uší). Za formální nedostatky prosí o shovívavost.
- **Skeny 7–8** jsou prázdné listy (jen prosvítající text a skvrny), ověřeno ve skenu. Věnování ani předmluva nepokračují.
- **017v–018r** – začátek Druhé knihy (dělostřelectvo): kolik a jakých děl vézt podle záměru tažení. Následuje převoz těžkých děl: hlaveň a lafeta zvlášť, počty koní.
- **018v–019r** – výpočet koulí a prachu, najímání vozků a koní, postroje. Kapitola „O nejvyšším polním hejtmanovi a zbrojmistrovi“: zvědové, utajení cesty tažení.
- **019v–021r** – kapitola „Jaké vozy jsou potřebné pro tažení“: podrobný soupis vozů s nářadím, materiálem, náhradními díly, zbraněmi a municí, ohnivými koulemi a stany.
- **021r–021v** – kapitola „O lodních mostech“ (30 lodí, vozy, rozměry). Dále polní mlýny a měděné pekařské pece „ze Saska“.
- **021v–022v** – kapitola „Jak se mají děla obsadit“: počty puškařů, jejich žold (v násobcích žoldu), koníci a pachole, zapůjčování puškařů. Následuje přísaha puškařů, zkoušení cizích uchazečů a reversní list (pokračuje na 23r).

## Úpravy struktury

- 017v: přepracován nadpis (cs), doplněn `popis` obrázku 5, doplněn a vyčištěn německý text, přeložen odstavec.
- Nadpisy (v YAML z OCR byly jako `odstavec`) jsem změnil na `nadpis` s úrovní 2: 19r „Den Obersten Feldthauptmann betreffendt…“, 19v „Was für Wägen…“, 21r „Die Schiff brücken belangend.“, 21v „Welcher massen die Büchsen besetzt werden sollen.“ Úroveň 2 jsem zvolil jako pro 29r („Zeugwarts befelch…“) – jde o hlavní oddíly Druhé knihy (viz připomínky).
- 22r: pět řádků platového sazebníku puškařů („Welcher … scheußt / den Monat … Söld“), které jsou v tisku jako samostatné odstavce, jsem převedl na `seznam`. OCR je v YAML chybně slučovalo do dvou bloků.
- 22v: smazán blok „fie auch mit handknechten“ (zbytek OCR, v tisku není).
- 21v, 22r: odstraněny zdvojené řádky z OCR („Campt feiner sugehörung ein enge gen Wagen…“, „die Tollen Klepper halten/damit sie“).
- `pokracovani: true`: venovani-2, predmluva-2, 018r, 019r, 021v.
- **Mimo dávku:** 023r začíná pokračováním věty z 22v („wie sie ihr Endt gethon…“), ale nemá `pokracovani: true` – je potřeba doplnit při překladu 23r.

## Místa ověřená ve skenu

- Sk. 3: „Mimpelgart/rc.“ (ne „zu.“), „dem Vegetio“ (OCR „dein“), „vnänlich“, „Thurnieren“ (OCR „Thurniere“).
- Sk. 4: zdvojené „in meinem gemüt dester“ v OCR (v tisku jen jednou), „fünff theil“, podpis „E. F. G. / Vntertheniger / Leonhart Fronsperger.“
- Sk. 5: „jedem recht zu thun“ (tisk „jedē“), „sachen“ (tisk „sachē“).
- Sk. 6: „Fechter“ (OCR „Hechter“), „singen“ (OCR „fingen“).
- Sk. 43: „sechtzehen Roß … achtzehen Roß … sechsthalben Centner“ (100 centů : 18 koní ≈ 5½), „Scharpffmetzen“, „deßt ehe zerbrechen“. Záhlaví listu XVIII chybně „Das erste Buch“ – vynecháno.
- Sk. 44: „mittelmäßigen“ (OCR „mitte mäßigen“), „Leutenandt“ (OCR „Ecutca nandt“), „erobert“ (OCR „nobert“), „das thůt man bey dem nechsten“.
- Sk. 45: „nit für schaden steh“ (kustoda „mit“ je jen tvar písmen), „Stränge“, „Deychselwägen … Landtwägen“.
- Sk. 46: „Munition wägen“ (tisk „wägē“, OCR „wagt“), „geyßfüß“, „Stoßbäwm“, „gestraub höltzer“, „Kantzwägen“, „holtz/äxten“.
- Sk. 47–48: „Pratzen Reder“, „Zilscheyter“, „gestroben/rester“, „Mödel“, „leheren“, „bescheyd“ (OCR „beschend“).
- Sk. 50: „hondten oder binnen“ (čtení „h“/„b“ nejisté), „Kipffblöck … Spauchen“, „Mawrbrächern“.
- Sk. 51–52: oddělené řádky sazebníku žoldu, „zündtrüten“, „paßieren lassen“, „Herrn“ (tisk „Herꝛ“).

## Sporná místa

1. **19r** „die geng/ring/vnd abweg zu verschrancken“ – „ring“ jsem přeložil jako „stezky“ s poznámkou. Význam je nejasný.
2. **19r** „gleicher gestalt sein die wägen“ – vykládám jako Waage = vahadlo (navazuje na postraňky), ne „vozy“. Je k tomu poznámka.
3. **19r** „Deychselwägen besser dann die Landtwägen“ – Landwagen vykládám jako vůz s ojnicemi a koni zapřaženými za sebou (vyplývá z kontextu).
4. **19v** „damit so man die Büchsen schmieden … heben soll“ → „když se mají děla kovat [nebo] zvedat“. „Schmieden“ v tomto kontextu nedává dobrý smysl, je k tomu poznámka. „Kantzwägen“ → „převozní vozy“ (odhad podle 21v).
5. **19v** „gestraub höltzer“ → „vzpěry“ (možná šroubové zvedáky).
6. **19v/20r** „Lunnen, Lannagel, Lannseyler, Lannstangen, Lannenbäwm“ – „Lanne“ vykládám jako ojnice (svory). „legeisen“ → „náhradní kování“ (nejisté).
7. **20r** „Zilscheyter“ → „zaměřovací klíny“; „Setzbäwmen/gestroben/rester“ → „podpěrné trámy, vzpěry, krokve“. Vše nejisté.
8. **20v** „Reyßspieß … Brechscheiben“ → „jezdecká kopí … chrániče rukou“. „leheren … dardurch man die kuglen der feind vnd freund geußt“ → „kalibry, podle nichž se lijí koule nepřátel i přátel“ (snad pro ukořistěná děla).
9. **21v** „Mülen als Roß/Windt/zug vnd treyb“ → „koňské, větrné, tažné a hnané“. Poslední dva druhy jsou nejasné.
10. **22v** „so mag jhne der Zeugmeyster paßieren lassen“ → „může ho nechat jít“ (tj. nepřijmout). Alternativně „nechat projít“ = přijmout na zkoušku; podle navazujícího odstavce (zkouška střelbou) je ale správnější první výklad.
11. **predmluva-2** „so darff demnach einer wol nicht halb soviel als hierinn begriffen/gewar werden“ – dvojí čtení, viz poznámka 2.
12. **predmluva-1** – věta „Darmit aber nicht jemand…“ je v originále anakolut. Zachoval jsem ji a doplnil poznámku.

## Návrhy do glosáře

- `lafeta` – cs: lafeta; de: [Gefäß, Gefeß, gefeß, gefessen]; kategorie: delostrelectvo; pozn: Dřevěné lože děla s koly, v němž dělo při střelbě leží; těžká děla se vezla bez lafety, hlaveň (Rohr) zvlášť na voze.
- `hlaven` – cs: hlaveň; de: [Rohr]; kategorie: delostrelectvo.
- `puskar` doplnit de: Büchßenmeyster (tvar s ß v této části tisku převládá).
- `ohnostroj` – cs: ohňostroj; de: [Fewrwerck, fewrwerck, Feuerwerk]; kategorie: delostrelectvo; pozn: Zápalné a výbušné prostředky pro válku (ohnivé koule, zápalné věnce, granáty), jejich výroba a vrhání; nikoli zábavní ohňostroj.
- `ohniva-koule` – cs: ohnivá koule; de: [Fewrkugel, fewrkuglen]; kategorie: delostrelectvo.
- `zvedy` – cs: zvěd; de: [Kundtschaffter, Kundschaffter]; kategorie: sluzba; pozn: Průvodce a vyzvědač, který zná cesty, brody a mosty; vede předvoj.
- `predvoj` / `zadni-voj` – cs: předvoj, zadní voj; de: [Vorzug] / [Nachzug]; kategorie: sluzba.
- `ztraceny-houf` – cs: ztracený houf; de: [verlorner Hauffen, verlornen hauffen]; kategorie: jednotky; pozn: Útočný předvoj pěchoty z dobrovolníků nebo vylosovaných, který jde do boje první.
- `vozka` – cs: vozka; de: [Fürmann, Fürleuth, Fuhrleuth, Wagenleuth]; kategorie: delostrelectvo.
- `zbrojni-vuz` – cs: zbrojní vůz; de: [Zeugwagen, Zeugwägen]; kategorie: delostrelectvo.
- `posadka` – rozšířit pozn: „… v Druhé knize často i obléhané opevněné místo (město, hrad) s posádkou.“ Případně přidat `hledat: 'obsazen\w* míst'`.
- `mozdir` – Feuerbüchse a Böller stojí v textu vedle sebe (18v, 22r). Navrhuji Feuerbüchse vyčlenit jako „ohnivý moždíř“ (já jsem tak překládal), nebo do pozn. vysvětlit rozdíl.
- `plukovnik` – do pozn. doplnit, že „die Obersten“ může znamenat i nejvyšší velitele obecně (19r = polní hejtman a zbrojmistr).

## Osoby a místa pro rejstřík

- Kryštof Württemberský (Christoph, Herzog zu Württemberg und Teck, 1515–1568) – venovani-1
- Vegetius (Publius Flavius Vegetius Renatus) – venovani-1, venovani-2
- Titus Livius – venovani-1 (v glosáři je)
- Julius Frontinus (Sextus Iulius Frontinus) – venovani-1
- Karel V., císař – predmluva-1
- Württembersko, Teck, Montbéliard (Mömpelgart, v tisku „Mimpelgart“) – venovani-1
- Sasko (pekařské pece) – 021v

## Připomínky k pravidlům

1. **Úrovně nadpisů ve Druhé knize** – kniha.yaml rozlišuje „velké oddíly“ (2) a „dílčí oddíly“ (3), ale nepíše, co jsou kapitoly 2. knihy. Zvolil jsem úroveň 2 jako na 29r. Doporučuji v kniha.yaml výslovně uvést: „kapitoly uvnitř knih (nadpis v tisku větším písmem uprostřed) = 2, přísahy a podnadpisy = 3“.
2. **{} u termínů mimo glosář** – pravidla neříkají, zda závorky dávat i k technickým termínům, které v glosáři nejsou (Gefäß, Rennfändlin, Zilscheyter…). Dával jsem je u odborných a nejasných termínů, aby si je kontrolor mohl ověřit. Pokud web z každé {} dělá odkaz, vzniknou mrtvé odkazy. Navrhuji pravidlo upřesnit (např. {} jen pro hesla glosáře, ostatní originály v poznámce).
3. **Vlastní jména ve {}** – u osob a míst (Mimpelgart) jsem {} nepoužil a původní podobu dal do poznámky. Bylo by dobré to v pravidlech výslovně uvést.
4. **Glosář `dela` (Büchse/Stück)** – „Büchse“ v kontextu vojáka nebo ručnice („handbüchsen“, „mit spieß/büchsen“) není dělo. Do pozn. hesla doplnit, že u pěchoty jde o ruční palnou zbraň.
5. **`zbroj` = Rüstung** – v úvodních textech „Kriegsrüstung“ znamená výzbroj či válečné přípravy (záhlaví „Von allerhand Kriegßrüstung“), ne brnění. Překládal jsem „výzbroj“. Navrhuji do glosáře výjimku.
6. **`žold` = Besoldung** – u vozků a puškařů jsem „Besoldung“ překládal „žold“ (podle glosáře). U civilních vozků by přirozenější byl „plat“, ale držel jsem se glosáře.
7. **Seznam vs. odstavce** – pravidla mají přednostně párovat 1 : 1 odstavce tisku, ale zároveň „seznamy jako seznam“. U krátkých položek „Item ein Wagen mit…“ (19v–21r) jsem ponechal samostatné odstavce (každý je v tisku odsazený odstavec). Sazebník žoldu (22r) jsem dal jako `seznam`. Pravidlo by mohlo říct, kdy zvolit `seznam`, a kdy ponechat řadu krátkých odstavců.
8. **Zkratky „ꝛc.“, „vñ“, „Herꝛ“** – přepisoval jsem „rc.“, „vñ“ ponechal a „Herꝛ“ psal jako „Herr“. Ve stávajících stranách se vyskytuje i „2.“ a „2c.“ (chyby OCR za ꝛc.). Doporučuji do § 2 doplnit jednotný přepis (ꝛc. → rc.).
9. **Poznámka vs. heslo glosáře** – pravidlo „nepiš poznámku, když termín vysvětluje glosář“ vede v technických soupisech (19v–21r) k mnoha poznámkám, které by patřily do glosáře. Výše proto navrhuji několik nových hesel. Po jejich přijetí lze poznámky zkrátit.
