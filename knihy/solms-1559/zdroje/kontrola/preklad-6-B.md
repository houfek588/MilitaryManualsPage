# Překlad – dávka 6-B (Šestá kniha, skeny 510–527, 6-009v … 6-018r)

Datum: 2026-11-18. Všech 18 stran má originál přepsaný ze skenu (BSB IIIF, výřezy ve vyšším rozlišení u sporných čísel a jmen)
a překlad; `stav: prelozeno`, `overeno_clovekem: false`. `over_strany.py … --prisne`: 18 stran, 0 chyb, 0 varování.
Sousední strany 6-009r a 6-018v jsou zatím kostry (`chybi_original`), jen přečteny ze skenu/OCR kvůli návaznosti.

## Přehled stran
| Strana | Sken | Obsah |
|---|---|---|
| 6-009v | 510 | konec přehlídkového lístku Henickena von Bortzfelt (položky 10–12, součty: 1434 zl.); nadpis + lístek Helwecka von Rückerßhausen a Daniela Scheurschloße (28. 5. 1544), položky 1–10 |
| 6-010r | 511 | konec lístku Rückerßhausen/Scheurschloß (nota o Rotenhausen, jednokoní jezdci, 2220 zl.); celkový součet přehlídky (10662 zl.); knížecí stav vévody Mořice (položky 1–8, 1865 zl.) |
| 6-010v | 512 | stav položky 9–12 (290 zl., stav celkem 2155 zl., celkem 12817 zl., 713 koní…); nadpis (úr. 2) *Register des Anreitens* – komisaři Reinhart ze Solmsu a Christoffel von Schawenburg; příjezdné Andrese Pflüga, položky 1–4 |
| 6-011r–6-012v | 513–516 | příjezdné saských jezdců, položky 5–30, závěrečné součty (290 koní, 2262 zl. 3 bac.) |
| 6-013r–6-013v | 517–518 | odečet za trénní koně (zbytek 2194 zl. 13 bac.); příjezdné Henickena von Bortzfelt (Hildesheim, Brunšvik…), součet 610 zl. 1½ bac. |
| 6-014r–6-015v | 519–522 | odečet (602 zl. 12 bac.); nadpis (úr. 3) příjezdné Helwicka von Rückerßhausen a Daniela Scheurschloße, položky 1–25, zbytek 423 zl. 14 bac.; nadpis (úr. 3) příjezdné vévody Mořice, položky 1–5 |
| 6-016r–6-016v | 523–524 | příjezdné Mořicovy družiny, položky 6–14 (vachmistr, jednokoní jezdci, trubači); rekapitulace všech zbytků 4606 zl. |
| 6-017r–6-018r | 525–527 | nadpis (úr. 2) *Brandenburg. Wir Karl* – služební list Karla V. pro markraběte Albrechta Alkibiada na 1000 koní, články 1–25 (výzbroj kopiníků a střelců, korouhve, žold úřadů, trénní koně, vozy, příjezdné, nemocní a zajatí, doba služby) |

## Zvolená forma
- Rejstříky a výpočty jako `tabulka` se 3 sloupci: číslo položky / „Summa lat.“ | položka (jméno, text) | počet nebo částka;
  souhrnné výpočty se 2 sloupci (text | částka). Dvousloupcová sazba (6-009v, 6-010r) je převedena čtením nejprve levého,
  pak pravého sloupce – tomu odpovídají i tištěné mezisoučty. Svorka „Summa lat.“ stojí v prvním sloupci první položky skupiny.
- Jména osob v `cs` ponechána v podobě tisku (jen *vnd* → *a*, lomítka → čárky; hrabě/pan přeloženo); dnešní podoby rodů v poznámkách.
- Každá strana kromě 6-017r začíná `pokracovani: true` (rejstřík nebo služební list pokračují z předchozí strany; 6-010v a 6-013r
  pokračují souvislým výpočtem). 6-009v navazuje na položku „Jost von Velten.“ na konci 6-009r (sken 509).
- Kustody (*11 Gerüster*, *summa*, *Item*, *Hie*, *Branden.*, *9 Item*) a signatury (*C ij*, *C iij*, *C iiij*, *D*) vynechány.
- Mince: *flo./fl./gulden* → zl./zlatý, *batzen* → bac./bacen, *Kreutzer* → krejcar; čísla beze změny (kontrolní skript ověřil shodu čísel v DE a CS).

## Ověřená čtení ze skenu (OCR bylo u tabulek zcela rozházené)
- 6-009v: „Hanß Wolff von der Dañ“ → *Dann* (rozepsaná tilda); „Frantz von Krān“ → *Kran* (na 6-014r tištěno *Kran* bez znaménka); „Vrff“, „Gotzenrade“, „Merben“, „Merlen“ podle tisku; mezisoučet pravého sloupce tištěn „6“ (správně 46).
- 6-010r: „7 Drabantē“ → *Drabanten*, „eiñ gulden“ → *einen gulden*; „Leibartz/Wundartz“, „Komormeister“, „Fürsten doffel“.
- 6-010v: „58½“ vozů, „Vñ laufft sich die samma“ (tisk *samma*), „Commiſſarien“ (OCR *Commiffarten*).
- 6-011r: „36 flo. 9 batzen“ a „mit 14 pferden“ skutečně v tisku (viz sporná místa).
- 6-013v: „Jost von Altar Mandelsa“ přesně podle tisku.
- 6-015v: číslování položek „14“ a „25“ místo 24 a 25; „Summa latr.“; jméno „Hantgelt von Maltitz“.
- 6-017r: titulatura a výčet zbroje přečteny z výřezů 1400 px; 6-018r „vberentzige“ (OCR *oberentzige*).

## Sporná místa a tiskové chyby (vše v poznámkách na stránkách)
- **Aritmetika rejstříků**: tiskové chyby jsou zachovány v `de` i `cs` a vysvětleny poznámkou, kde je oprava jistá z mezisoučtů:
  6-009v (6 → 46 koní), 6-011r (36 → 93 zl. 9 bac.; 14 → 6 koní; 1 zl. 10 → 12 bac.; suma 75 → 57 zl. 9 bac.), 6-011v (10½ dne → 9½;
  suma 95 → 59 zl. 7 bac.), 6-012r (27 → 21 zl. 9 bac.), 6-012v (součet strany 65 zl. 12 bac. → 669 zl. 9 bac.), 6-014v (21 → 11 koní),
  6-016v (115 → 118 zl. 12 bac.; zbytek 2384 → 1384 zl. 6 bac., potvrzeno celkem 4606 zl.). Nerozřešené nesrovnalosti: 6-013v
  (součet 139 zl. 6 bac. u položek 3–6), 6-014r, 6-014v (položky 12–13), 6-015r, 6-015v (drobné rozdíly v sumách).
- **Odečty za trénní koně** (6-013r, 6-014r): odečítá se o 3 bac. méně, než uvádějí předchozí součty (67 zl. 5 bac. vs. 67 zl. 8 bac.;
  7 zl. 4½ vs. 7 zl. 7½ bac.) – zbytky však s odečtenou částkou souhlasí.
- 6-015v *Von zwölffen vndergesteckter Drosser wägen abgezogen 31 flo.* – CS „Za dvanáct vozů, do nichž byli započteni trénní koně,
  odečteno“; smysl „vndergesteckt“ (zastrčený, započtený) nejistý.
- 6-016r *Georg Wachtmeister* – CS „Georg, vachmistr“; může jít i o příjmení.
- 6-017r *Kürisser mit gantzen Parssen* – „Parssen“ nejasné, přeloženo „v celé zbroji“ (poznámka); *Büglin* – „náloketníky“, nejisté.
- 6-010r položka 8 *Capellan/ Fürer vnd Schreiber* (CS „vůdce“ podle glosáře) vs. 6-017r čl. 7 *Caplon/ Furirer/ schreiber* (CS „furýr“) –
  v saském stavu jde možná také o furýra; ponecháno podle tvaru tisku.
- 6-010v *fendrichen* a 6-017v *Fenderichen* u jízdy – ponechán glosářový „praporečník“, ačkoli jde o nositele korouhví jízdy
  (*Fendlein* zde důsledně „korouhev“). K rozhodnutí: „korouhevník“?
- 6-017r *seiner lieb* – přeloženo dobově „Jeho Láska“ (knížecí oslovení *Liebden*); *Oheim* – „strýc“ (císařské oslovení knížat).

## Návrhy do glosáře
| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| trenni-kun (doplnit) | trénní kůň | Drosser, Droß, Droßpferd | sluzba | V přehlídkových rejstřících jezdců se platí 6 zl. měsíčně (polovina zbrojného koně), jeden na 12 zbrojných koní; příjezdné 3 bacenů denně. |
| soucet-strany | součet strany | Summa lat., Summa lateris, Summa latr. | zold | Mezisoučet úseku rejstříku (se svorkou), z nějž se skládá celkový součet. |
| prehlidkovy-listek | přehlídkový lístek | Musterzettel, Musterzetel | zold | Soupis jezdců jedné korouhve či rytmistra s počty koní, trénních koní a vozů ke dni přehlídky. |
| prijezdne (doplnit) | příjezdné | Anrit gelt, anritgelt, Anritgelt, Anreitens, zů oder anreitens | zold | Platí se po dnech „cesty a stání“ (gereist vnd stilgelegen): 6 bacenů (24 kr.) na koně, 3 bacenů na trénního koně, 12 bacenů na vůz denně. |
| dvorska-druzina | dvorská družina | Hoffgesind | jednotky | Dvořané a služebníci knížete, kteří s ním táhli do pole a byli přehlíženi zvlášť. |
| komornik | komorník | Komormeister | velitele | Správce pokladny a komory knížete či plukovníka jízdy (jeden z „6 vysokých úřadů“). |
| podkovar | podkovář | Huffschmidt, Hufschmidt | sluzba | Jeden na sto koní, s přeplatkem 12 zl. měsíčně. |
| jednokony-jezdec (doplnit) | jednokoní jezdec | Einspennig, Einspennigen, Einrosser | jednotky | – |
| krejcar | krejcar | Kreutzer | miry | 4 krejcary = 1 bacen, 60 krejcarů = 1 zlatý. |
| poselsky-kun | poselský kůň | Potenpferd | sluzba | Kůň pro posly, počítaný místo trénního koně. |
| kopi-s-prickou | kopí s příčkou | Knebelspieß, Knebelspiessen | zbrane | Lehčí jezdecké kopí s příčnou zarážkou, zbraň jízdních střelců. |
| hejtmansky-zlaty | hejtmanský zlatý | hauptmans gulden | zold | Jeden zlatý měsíčně veliteli na každého uznaného koně. |
| dedicna-smlouva | dědičná smlouva | Erbeinigung, Erbeinigungs verwanden | pravo | Dědičná jednota mezi knížecími rody (Hohenzollernové, Wettinové, Hesensko). |
| zbroj – části | prsní plát / zádový plát / ochrana paží / kroužkové rukávy / kolenice / stehenice / lebka | Krebs / Rücken / Armzeug / Pantzerermel, schurtzermel / Kniegbüglein / Dielüngen / Hauben | zbrane | Výčet jezdecké zbroje v braniborském služebním listu (6-017r). |
