# Společné zadání pro agenty – Niccolò Tartaglia, Quesiti et inventioni diverse (Benátky 1554)

Projekt: `C:\Projects\RT\MilitaryManuals` (Windows; Python spouštěj `python -I`, v Pythonu nastav
`sys.stdout.reconfigure(encoding='utf-8')`; soubory zapisuj v UTF-8). Kniha: `knihy/tartaglia-1554`.
Nejdřív přečti: `PRAVIDLA_PREKLADU.md`, `knihy/tartaglia-1554/kniha.yaml` (hlavně `poznamky_k_prekladu`) a
`knihy/tartaglia-1554/glosar.yaml`.

## ORIGINÁL JE ITALSKY
Tato kniha je jako jediná v edici **italská** (benátská toskánština, 1554). Pravidla edice jsou psaná pro němčinu;
platí stejně, jen:
- pole **`de` obsahuje italský text** (název pole je historický, znamená „originál“), `{Termín}` je italský tvar z tisku,
- německá pravidla OCR (§ 2: *foll → soll*, *k → tz* …) neplatí; místo nich: dlouhé **ſ** čtené jako **f**
  (fi → si, fono → sono, fopra → sopra, fua → sua, cofa → cosa, ftare → stare), ſ převeď na s, ligaturu ß (ſs) na „ss“,
  zkratky s vlnovkou rozepiš (cõ → con, q̃ → que, ā → an/am), u/v a i/j ponech podle tisku (uarie, hauere, Iulio),
  akcenty podle tisku (città, à, perche),
- výchozí terminologie z PRAVIDLA § 3 (Oberst, Fähnlein…) se týká němčiny; pro italštinu platí glosář knihy a
  terminologie v `poznamky_k_prekladu`.

## Strany
- Strany jsou kostry (`stav: chybi_original`, `bloky: []`), založené `nastroje/zaloz_strany.py` (`--od 1 --do 256
  --prvni 1 --titul 1 --foliace-od 5`). Pole `id`, `list`, `strana`, `sken` neměň. List N r = sken 2N − 1, N v = sken 2N;
  listy 1–4 (titul, obsah, věnování) nejsou foliované. Překládají se jen skeny 1–154 (knihy I–VI a Gionta);
  skeny 155–256 (knihy VII–IX) zůstávají bez textu.
- **Originál**: výchozí je OCR `knihy/tartaglia-1554/zdroje/ocr_bsb/NNNN.txt` (NNNN = sken, 4 číslice). OCR antikvy je
  slušné, ale s typickými chybami ſ/f, rozdělenými slovy a zkomolenými čísly. **Každou stranu porovnej se skenem**:
  `curl -s -o <tvoje-podsložka-scratchpadu>/sNNN.jpg "https://api.digitale-sammlungen.de/iiif/image/v2/bsb11221340_<NNNNN>/full/1600,/0/default.jpg"`
  (NNNNN = sken na 5 číslic) a otevři nástrojem Read; drobné písmo a čísla v obrazcích zvětši výřezem
  (`…/bsb11221340_<NNNNN>/<x>,<y>,<w>,<h>/1200,/0/default.jpg`). Vynech živé záhlaví (PRIMO, LIBRO, SECONDO…), číslo
  listu, signatury (A ij) a kustody; slovo rozdělené přes hranici stran patří celé na stranu, kde končí.
  Ozdobné iniciály doplň do slova.
- **Bloky**: kniha je řada „quesiti“ (dotazů) v podobě rozhovoru. Nadpis knihy = úroveň 1, nadpis quesita („Quesito
  primo fatto dal Signor …“) = úroveň 3, případné mezinadpisy uvnitř knihy = 2. **Každá replika = jeden blok
  `odstavec`**; jméno mluvčího je v tisku na začátku repliky (BOMBARDIERO., N., S. DVCA., S. PRIOR) – v `de` ho ponech,
  v `cs` ho přelož a dej tučně: `**Dělostřelec.** …`, `**Nicolò.** …`, `**Pan vévoda.** …`. Tabulky (váhy koulí,
  složení prachu, počty mužů v šicích) jako `tabulka` se stejným počtem řádků a sloupců v `de` i `cs`.
- **Obrázky**: dřevořezy a geometrické figury jako blok `obrazek` se souborem `drevorez-<sken>.jpg` (druhý na téže
  straně `drevorez-<sken>b.jpg`) a českým `popis` – co obrazec ukazuje, včetně písmen a nápisů (a, b, c; „Ponente“).
  Soubor nevytvářej, výřez dodá správce. Šiky sázené z písmen/teček (kniha IV) popiš v `popis` (rozměry, počty).
- **Překlad (`cs`)**: věrně a čtivě (plynulost „středně“), rozhovor má znít jako přirozený dialog, ale s dobovou
  zdvořilostí (Vaše Excelence, Vaše Milost). Výpočty, proporce a geometrické důkazy překládej přesně – čísla, písmena
  bodů a pořadí kroků neměň. `{Termín z tisku}` při prvním výskytu na stránce. Kde glosář chybí, zvol překlad, drž ho
  v celé dávce a navrhni heslo do zprávy (glosář needituj).
- **Poznámky**: osoby (tazatelé, jejich funkce), místa a události (obléhání, bitvy), dobové reálie a nejasná místa;
  tiskové chyby v `de` ponech a vysvětli. Neopakuj výklad glosáře.
- Překladatel nastaví `stav: prelozeno`, kontrolor `stav: zkontrolovano`; `overeno_clovekem` zůstává `false`.

## Výstup
- Edituj jen strany své dávky; stranu před a za dávkou jen čti (návaznost vět).
- Pomocné soubory a skeny jen ve **vlastní podsložce scratchpadu** – sdílené soubory přepisují jiní agenti.
  Ukládej stranu po straně (při přerušení limitem se tak nic neztratí).
- Po dokončení: `python -I nastroje/over_strany.py knihy/tartaglia-1554 <id …> --prisne` – 0 chyb.
- Zprávu ulož do `knihy/tartaglia-1554/zdroje/kontrola/<preklad|revize>-<dávka>.md`: přehled stran, nejistá čtení ze
  skenu, sporná místa (IT + CS + důvod), návrhy hesel (id, cs, italské tvary, kategorie, pozn), osoby a místa.
  Do odpovědi vrať shrnutí do 10 řádků.
