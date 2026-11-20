# 2. revize – Šestá kniha, dávka 6-B (skeny 510–527, 6-009v … 6-018r)

Datum: 2026-11-19. Podklad: `ZADANI_REVIZE2.md` (vč. oddílu o knihách 6–9) a zpráva překladatele `preklad-6-B.md`.
Všech 18 stran porovnáno se skeny BSB IIIF (1400 px, sporná místa výřezy 1800 px); všechny rejstříky a tabulky
zkontrolovány řádek po řádku (jména, počty, částky) a přepočítány (15 bacenů = 1 zl.; denní sazby 6 / 3 / 12 bacenů
za koně / trénního koně / vůz). Všem stranám nastaveno `stav: zkontrolovano`, `overeno_clovekem: false`.
`python -I nastroje/over_strany.py knihy/solms-1559 6-009v … 6-018r --prisne` → 18 stran, 0 chyb, 0 varování.
Sousední strany 6-009r a 6-018v jen přečteny (návaznost „Jost von Velten.“ → položka 10 a čl. 25 → 26 sedí).

## Výsledek kontroly přepisu (`de`) proti skenu
Přepis tabulek je velmi dobrý – ve všech rejstřících (6-009v až 6-016v) souhlasí každé jméno, číslo položky, počet
i částka se skenem. Opravy jen v souvislém textu služebního listu:
- 6-017r čl. 2: *Haupthärneschen* → **Hauptharneschen** (tisk bez přehlásky; opraveno i v `{…}` v cs);
  *mit stehlen Krägen* → **mit steheln Krägen** (tisk; o dva řádky níže tisk skutečně „stehlen“).
- 6-017v čl. 12: *Hufschmidt* → **Huffschmidt** (i v `{…}`).
- 6-018r: čl. 19 *gůt pferd* → **gut pferd**; čl. 20 *vier vnd zwentzig* / *acht vnd zwentzig* → **viervndzwentzig** /
  **achtvndzwentzig** (v tisku jedním slovem); čl. 23 *Fürst Margraff* → **Furst Margraff** (tisk bez přehlásky).
- 6-016v: *Daniel Scheurschloß* v rekapitulaci → **Daniel scheurschloß** (tisk malým s).
- Ověřeno beze změny: 6-009v „Dann“, „Kran“, mezisoučet „6“; 6-011r „36 flo. 9 batzen“, „14 pferden“; 6-013v
  „Jost von Altar Mandelsa“; 6-015r „gudlen“, „gulten“ (tiskové chyby tisku); 6-015v „14“/„25“, „Summa latr.“,
  „Hantgelt“; 6-017r „Parssen“, „Dielüngen“, „Hendschůch“; 6-017v „bestümder gemusterder“; kustody a signatury vynechány správně.

## Hlavní změny po stranách
- **6-009v**: pozn. 2 zkrácena (výklad trénního koně opakoval glosář; ponechána jen sazba 6 vs. 12 zl.).
- **6-010r**: beze změny textu (aritmetika stavu 1865 zl. a součtů 152/12/13 ověřena).
- **6-010v**: *fendrichen* „praporečníci“ → **„korouhevníci“** (rozhodnutí pro knihy 6–9); nadpis „Rejstřík příjezdu“ →
  **„Rejstřík příjezdného“** (glosář); nová pozn. 2: vůz u položky 1 tištěn za 12 dní (9 zl. 9 bac.), ne za 13 (10 zl. 6 bac.);
  poznámky přečíslovány podle pořadí v textu.
- **6-011r**: beze změny (tiskové chyby a jejich opravy v pozn. potvrzeny výpočtem i součtem strany 282 zl. 9 bac.).
- **6-011v**, **6-012v**: „činí suma“ → „činí celkem“; z pozn. 2 na 6-011v vypuštěn výklad míle (je v glosáři).
- **6-012r**: pozn. 2 doplněna – u položky 23 (22 dní) odpovídají trénní kůň a vůz 23 dnům.
- **6-013r**: pozn. 1 zpřesněna – jednotlivé položky trénních koní Pflügova rejstříku dávají (s opravou položky 6) přesně
  tištěných 67 zl. 8 bac.; odečítá se o 3 bac. méně.
- **6-013v**: pozn. 1 – nesrovnalost **rozřešena**: tištěný součet strany 139 zl. 6 bac. (pol. 3–6) je tisková chyba za
  237 zl. 9 bac.; potvrzuje to celkový součet 157 zl. 7½ + 237 zl. 9 + 139 zl. 6 + 75 zl. 9 bac. = 610 zl. 1½ bac.
- **6-014r**: pozn. 1 – položky trénních koní na 6-013r (2 zl. 6 + 2 zl. 10½ + 2 zl. 3 bac.) dávají přesně odečtených
  7 zl. 4½ bac.; chybný je tedy tištěný součet 7 zl. 7½ bac.
- **6-015r**: pol. 23 plynuleji: „měli na přehlídkové místo jízdy a stání, každý den…“ → „na jízdu na přehlídkové místo
  a stání měli každý den na koně 6 bacenů…“.
- **6-015v**: věcná oprava (viz níže „wägen = wegen“): „Za dvanáct vozů, do nichž byli započteni trénní koně, odečteno“ →
  **„Kvůli dvanácti trénním koním zahrnutým [mezi koně] odečteno“**; pozn. 2 přepsána; nová pozn. 3 (suma pol. 2
  61 zl. 6 bac. je tisková chyba za 61 zl. 3 bac. – potvrzeno součtem strany 389 zl. 3 bac.; pol. 5 počítána za 15 dní);
  Hantgelt → pozn. 4.
- **6-016r**: beze změny (výpočty pol. 6–11 i součty 382 zl. 12 a 327 zl. 9 bac. sedí).
- **6-016v**: „Z toho odečteno za vozy trénních koní“ → **„Z toho odečteno za trénní koně“**; pozn. 2 doplněna (odečítá se
  přesně 50 zl. = peníze za 14 trénních koní). Ověřeno: součty Mořicova příjezdného 1434 zl. 6 bac., 163 koní, 14 trénních,
  15½ vozu; celkem 4606 zl. s opravou 1384 zl. 6 bac.
- **6-017r**: nadpis cs „Brandenburg.“ → **„Braniborsko.“**; čl. 2 „opatřenými vším potřebným a silnými ranami“ →
  „… i silnými náboji“; čl. 5 *auff derselbigen Leutenant* = poručík markraběte (srov. 6-010r *Auff jrer G. Leutenant*):
  „na poručíka tohoto [vojska]“ → **„na jejího [Jeho Lásky] poručíka“**.
- **6-017v**: čl. 9 „praporečnického úřadu“ → **„korouhevnického úřadu“**; „čtyři a dvacet / pět a dvacet“ →
  „čtyřiadvacet / pětadvacet“ (archaismy střídmě); čl. 18 shoda s podmětem „pachole“ („přehlédnut, uznán a přijat“ →
  „přehlédnuto, uznáno a přijato“; „na ně a mezi nimi“ → „na ně ani mezi ně“).
- **6-018r**: jen opravy `de` (viz výše); překlad beze změny.

## Hlavní věcný nález: „wägen“ = „wegen“
Na 6-015v (*Von zwölffen vndergesteckter Drosser wägen abgezogen 31 flo.*) i 6-016v (*Hieuon abgezogen von der Drosser
Wägen 50 gulden*) jde o předložkovou vazbu *von … wegen* (kvůli), ne o „vozy“: na téže 6-016v stojí paralelně
*Abgezogen von der Drosser wegen*, na 6-014r *Von der Drosser wegen hieuon abgezogen*. Potvrzují to čísla: 50 zl. je přesně
řádek „Summarum aller Drosser ist 14/ thůn an gelt 50 gulden“ a 12 trénních koní uvádí přehlídkový lístek Rückerßhausena
a Scheurschloße (6-010r). Tím odpadá sporné místo překladatele č. 3 (*vndergesteckt* = zahrnutý mezi koně).

## Sporná místa k rozhodnutí
1. **6-016r** *Georg Wachtmeister.* – CS „Georg, vachmistr“. Ve stavu vévody Mořice (6-010r) je vachmistr jedním
   z 6 vysokých úřadů; 27 koní ukazuje spíš na úřad než příjmení. Ponecháno.
2. **6-017r** *Kürisser mit gantzen Parssen* – „Parssen“ (tisk jasně) nejisté; CS „v celé zbroji“ + pozn. Ponecháno.
3. **6-017r** *Büglin* – „náloketníky“, nejisté (pozn. 3). Ponecháno.
4. **6-010r** *Capellan/ Fürer vnd Schreiber* (CS „vůdce“) vs. 6-017r *Caplon/ Furirer/ schreiber* (CS „furýr“) – tisk
   má na 6-010r skutečně „Fürer“; ponecháno podle tisku a glosáře.
5. **6-017r** *seiner lieb* – „Jeho Láska“ (dobové knížecí oslovení *Liebden*); v čl. 5 navazuje „jejího poručíka“.
   Alternativa „Jeho Milost“ by splynula s *F. G.* – doporučuji ponechat.
6. Nerozřešené drobné aritmetické nesrovnalosti tisku (6-011v pol. 11, 13, 14, 17; 6-013r pol. 5; 6-014r součty 62 zl.
   a 64 zl. 9 bac., pol. 1 vůz; 6-014v pol. 12–13; 6-015r součet 124 zl. 12 bac.; 6-015v celkem 454 zl. 14 bac. proti
   součtu stran 455 zl. 6 bac.; 6-012v Kitlitz 27 dní × 4 koně = 43 zl. 3 bac. proti 46 zl. 6 bac.) – v `de` i `cs`
   ponechány podle tisku, hlavní z nich vysvětleny v poznámkách.

## Návrhy do glosáře
| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| trenni-kun (doplnit de) | trénní kůň | Drosser, Droß, droß, Droßpferd | sluzba | V přehlídkových lístcích jízdy 6 zl. měsíčně (polovina zbrojného koně), v příjezdném 3 bacenů denně. |
| prijezdne (doplnit de) | příjezdné | Anreitens, zů oder anreitens, Anrit gelt | zold | Doplnit sazbu: 6 bacenů (24 kr.) na koně, 3 bac. na trénního koně, 12 bac. na vůz za den „cesty a stání“. |
| korouhevnik (nové) | korouhevník | Fendrich, Fenderich, fendrichen, Fenderichen (u jízdy) | velitele | Nositel korouhve jízdy; v knihách 6–9 podle rozhodnutí autora místo „praporečník“. |
| prehlidkovy-listek | přehlídkový lístek | Musterzettel, Musterzetel | zold | Soupis jezdců jednoho rytmistra s počty koní, trénních koní a vozů ke dni přehlídky. |
| dvorska-druzina | dvorská družina | Hoffgesind | jednotky | Dvořané a služebníci knížete přehlížení zvlášť. |
| komornik | komorník | Komormeister | velitele | Správce pokladny a komory knížete či plukovníka jízdy (jeden z „6 vysokých úřadů“). |
| krejcar | krejcar | Kreutzer | miry | 4 krejcary = 1 bacen. |
| poselsky-kun | poselský kůň | Potenpferd | sluzba | Kůň pro posly, počítaný místo trénního koně. |
| hejtmansky-zlaty | hejtmanský zlatý | hauptmans gulden | zold | Jeden zlatý měsíčně veliteli na každého uznaného koně. |
| osobni-lekar (doplnit de) | osobní lékař | Leibartz | velitele | Tvar z 6-010r a 6-017r chybí v `de`. |
| ranhojic (doplnit de) | ranhojič | Wundartz, wundtartz | velitele | Tvary z 6-010r a 6-017r. |
