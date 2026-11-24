# Překlad – dávka E (Wintzenberger 1588), strany 045r–056r (skeny 93–115)

Všech 23 stran má přepis podle skenu a překlad, `stav: prelozeno`, `overeno_clovekem: false`.
`over_strany.py … --prisne`: 0 chyb, 0 varování. Každou stranu jsem porovnal se skenem BSB (full/1600, sporná místa ve výřezu).

## Obsah
- **045r–047v (sk. 93–98) – otázky a odpovědi soudu.** Sedm otázek rychtáře přísedícím při zahájení hrdelního soudu (vhodnost dne, kolem se nese svátost, obsazení soudu, oheň a poplach, plukovník volá rychtáře, nemoc rychtáře, nepohoda), každá s ustálenou odpovědí („nálezem“). Závěr: soud lze zahájit pod pokutou 1 zl. ve zlatě.
- **047v–048v (sk. 98–100) – zahájení soudu.** Rychtář „zahajuje právo a napíná lavici“ šestkrát: jménem Boha, římského císaře, knížete N., plukovníka, všech přítomných a dlouhých pík.
- **048v–050r (sk. 100–103) – průběh řízení.** Profous a obžalovaný si berou řečníky („dobré druhy“), následují tři žaloby a tři odpovědi, svědci (poplatky soudnímu šikovateli, rychtáři a písaři), rozsudek a jeho přečtení.
- **050r–054r (sk. 103–111) – „Folget das Recht mit den langen Spiessen“ (19 bodů).** Právo dlouhých pík: obec přísahá, profous zatkne pachatele a žaluje v kruhu, praporečníci zapíchnou praporce do země, tři rady po čtyřiceti mužích, hlasování, ulička z pík, rozloučení, poprava, modlitba, salva a poučení obce. Narovnání v menších věcech, okovy během odpovědí.
- **054v (sk. 112)** – výhrada plukovníkovi a pluku, FINIS.
- **055r (sk. 113)** – „Zum Beschlus“: dřevořez a první čtyři verše básně.
- **055v (sk. 114)** – tiskařský znak a tiráž Gimela Bergena.
- **056r (sk. 115)** – zbytek básně (12 veršů, `pokracovani: true`).

## Členění
- „Nun Folgen frage vnd Antwort“, „Antwort.“, „Nun spricht der Schultheis.“, „Spricht der Schultheis:“ a čísla bodů (1.–19.) jsou nadpisy úrovně 3 podle `kniha.yaml`. „Folget das Recht mit den langen Spiessen“ a „Zum Beschlus“ jsou nadpisy úrovně 2. Krátké repliky („Der Schultheis: Ja.“, „Antworten sie beyde: Ja / Ja.“) jsou odstavce.
- Velkým písmem vysázený odstavec „Nun spandt der Schultheis die Banck … schlegt“ (047v → 048r) přechází přes hranici stran, proto je to odstavec, ne nadpis.
- Slova rozdělená přes hranici stran jsou na straně, kde končí: *versamlet* (050v), *hetten* (051r), *seine* (050r), *können* (051v).
- **Obrázky:** podle zadání jsem stáhl `obrazky/drevorez-114.jpg` (IIIF full/1400, celá strana). Stejně jsem stáhl `obrazky/drevorez-113.jpg` (celá strana s dřevořezem bitvy lancknechtů), protože zadání ho nezmiňuje, ale na skenu je. Zkontroluj prosím, zda ho chceš ponechat, nebo nahradit výřezem. Ozdobnou vinětu (maskaron) na sk. 112 a ozdobnou lištu na sk. 115 jsem jako obrázky nezakládal, jde o typografickou výzdobu.

## Nejistá čtení ze skenu
| strana | tisk / OCR | přepis | pozn. |
|---|---|---|---|
| 051v | „seine R…-\|…ener“ (OCR *Rabener*), rozmazané | *Redener* | podle „seinen Redener“ na 052r; poznámka 2 |
| 045r, 046v | *each* (OCR) | *euch* | poškozená litera u |
| 047v | *rch* | *ich* | poškozená litera |
| 049v | *1. gr. … 2. gr.* (OCR *g*, *९*) | *gr.* = groš | ověřeno výřezem |
| 054r | začátek strany v díře papíru | *toden Cörper … Schützen* | doplněno podle kustodu *toden* a zbytků písmen |
| 048r | *dein Stabe* | *dem Stabe* | poškozená litera |

Tiskové chyby jsou v `de` ponechané a vysvětlené v poznámce: *Lob* (za *Leib*, 045r), *zauerbannen*, *Tegzeit* (047v), *Reht* (050v), *Gefangtnen*, *Edel vnd vnd Vnedel* (052v), *Andwort* (kustod, vynechán).

## Sporná místa
1. **045r** „es sey vber Silber / Gold / Lob / Ehre / Gut / vnd Blut“ → „ať jde o stříbro, zlato, chválu, čest, statek a krev“. V ostatních odpovědích stojí *Leib*. Překládám podle tisku a uvádím poznámku.
2. **047v / 048r** „das Recht verbannen / vnd die Banck spannen“ → „zahájit soud a napnout lavici“. *Banck spannen* je dobová formule otevření soudu. Ponechal jsem doslovný obraz a připojil poznámku.
3. **049r** „so wil ich mir alles das jenige abgedinget haben … von dem ersten / zum andern … bis auff seinen selbst eigenen Mund vnd Jawort“ → „vyhrazuji si … od prvního k druhému, od druhého ke třetímu, až k jeho vlastním ústům a jeho ‚ano‘“. Jde o výhradu opravy řečníka, vysvětleno v poznámce. Sporné je i „Raht vnd Sprache“ → „porada a slovo“.
4. **050r** „vnd von dem Obersten vbergeben ist worden“ → „který byl předložen plukovníkovi“. Lze číst i „plukovníkem předán“.
5. **050v** „darauff sol gemacht werden / solches Recht zu stercken vnd hand zuhaben“ → „potom se má učinit [slib], že se toto právo bude …“. Věta je eliptická.
6. **051v** „begeret des Profosen Vorsprecher / vnd seine beyde Rehte“ → „[profous] žádá o svého řečníka a o své dva rádce“. Věta nemá podmět, a lze ji tedy číst i tak, že žádá řečník.
7. **053r** „wenn man den Raht gemehret / das vnter 2. oder 3. mahl auffhiebe“ → „aby [každý], až se bude o radě hlasovat, zvedl [ruku] pro jednu ze 2 nebo 3 [rad]“. Doplňky jsou výkladové.
8. **054r** „einer den andern nicht liederlich vbergeben“ → „aby jeden druhého lehkomyslně nevydával [soudu]“. Možné je i „neopouštěl“.
9. **056r** „Drumb denck / verwig dichs denn fortan“ → „Proto pomni a smiř se s tím napříště“ (*sich verwegen* = vzdát se naděje).

## Ustálené překlady v dávce (bez hesla v glosáři)
Richter = přísedící, Rechtsprecher = nálezce práva, ausweisung = nález, Stab = soudní hůl / hůl, Vorsprecher, Redener = řečník, guter Gesell = dobrý druh, Rehte/Rähte = rádci, gemeiner Man = obecný lid, Gasse = ulička, Mishändler = provinilec, arme Sünder = ubohý hříšník, Keyserlich Recht = císařské právo, Banck spannen = napnout lavici, Eysen = okovy.

## Návrhy do glosáře
| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| nalez | nález | ausweisung, ausweisunge | pravo | výrok přísedícího, co je právem (odpověď na rychtářovu otázku) |
| soudni-lavice | napnout lavici | die Banck spannen, spanne die Banck | pravo | formule slavnostního otevření soudu souběžná s „verbannen“ |
| obecny-lid | obecný lid | gemeiner Man, gemeinen Man, gemeinen Manne | pravo | celá obec lancknechtů jako soud při právu dlouhých pík |
| ulicka | ulička | Gasse, Gassen | pravo | ulička z pikenýrů, kterou probíhá odsouzený |
| radce | rádce (strany) | Rehte, Rähte, Rethe | pravo | dva rádci strany při poradách mimo kruh |
| dobry-druh | dobrý druh | guter Gesell, guten Gesellen, gut Gesell | pravo | obvyklé oslovení lancknechta; zde řečník i obžalovaný |
| recnik (doplnit de) | řečník | Vorsprecher, Redener | pravo | doplnit tvary do stávajícího hesla |
| soudni-sikovatel (doplnit de) | soudní šikovatel | Gerichtswebel | pravo | tvar tisku |
| sikovatel (doplnit de) | šikovatel | Feldwebel, Feltwebel | velitele | tvary tisku |
| velitele (doplnit de) | velitelé | Befehlichshaber | velitele | tvar tisku |
| ortsgulden | čtvrt zlatého | Ortsgülden | miry | Ort = ¼ zlatého |
| gros | groš | gr. | miry | zkratka v poplatcích soudu |

## Osoby a místa pro rejstřík
- Karel V. – jen nepřímo („Röm: Key: May:“, 048r).
- Kristus, „12 pokolení Izraele“ (050v).
- Gimel Bergen (Gimel Berg), tiskař v Drážďanech (055v).
- Drážďany (Dreßden), Moritzstraße (055v).
