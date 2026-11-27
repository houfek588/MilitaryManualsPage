# Společné zadání pro agenty – Battista della Valle, Vallo (Benátky 1528)

Projekt: `C:\Projects\RT\MilitaryManuals` (Windows; Python spouštěj `python -I`, v Pythonu nastav
`sys.stdout.reconfigure(encoding='utf-8')`; soubory zapisuj v UTF-8). Kniha: `knihy/della-valle-1528`.
Nejdřív přečti: `PRAVIDLA_PREKLADU.md`, `knihy/della-valle-1528/kniha.yaml` (hlavně `poznamky_k_prekladu`) a
`knihy/della-valle-1528/glosar.yaml`. Vzorem italské knihy je hotový Tartaglia (`knihy/tartaglia-1554`) – smíš se
podívat, jak tam vypadají strany, ale překládej tento text.

## ORIGINÁL JE ITALSKY
Pole **`de` obsahuje italský text** (název pole je historický, znamená „originál“), `{Termín}` je italský tvar z tisku.
Německá pravidla OCR (§ 2) neplatí; dlouhé **ſ** převeď na s, ligaturu ß (ſs) na „ss“, zkratky s vlnovkou rozepiš
(cõ → con, ẽ → en, q̃ → que, ꝑ → per), u/v a i/j ponech podle tisku (uarie, hauere), akcenty podle tisku.
Výchozí německá terminologie z PRAVIDLA § 3 neplatí; platí glosář knihy a `poznamky_k_prekladu`.

## Strany
- Strany jsou kostry (`stav: chybi_original`, `bloky: []`) založené `nastroje/zaloz_strany.py`. Pole `id`, `list`,
  `strana`, `sken` neměň. Úvod: `titul` (sken 5), `u001v` … `u008v` (nečíslované listy [1] v – [8] v, skeny 6–20);
  text: `001r` … `071v` (list N r = sken 2N + 19) a `072r` (tiskařský znak, sken 163).
- **Originál PŘEPISUJ ZE SKENU.** OCR archivu (`zdroje/ocr_ia/NNNN.txt`, NNNN = sken na 4 číslice) je velmi špatné,
  slouží jen k orientaci. Sken (jedno číslo = `sken`, BEZ doplňování nulami):
  `curl -sL -o <tvoje-podsložka-scratchpadu>/sNNN.jpg "https://iiif.archive.org/iiif/vallolibrocotine00dell%24<sken>/full/1600,/0/default.jpg"`
  (plný sken má asi 2436 × 3745 px), drobné písmo zvětši výřezem
  `…/vallolibrocotine00dell%24<sken>/<x>,<y>,<w>,<h>/1400,/0/default.jpg` (souřadnice v pixelech plného skenu;
  `-L` je nutné, server přesměrovává). Vynech živé záhlaví (LIBRO / PRIMO), číslo listu, signatury (A ij) a kustody;
  slovo rozdělené přes hranici stran patří celé na stranu, kde končí. Ozdobné iniciály doplň do slova.
- **Bloky**: nadpisy podle `poznamky_k_prekladu` (kniha = 1, kapitola „Capitolo …“ = 2), odstavce 1 : 1 podle tisku,
  `pokracovani: true` u odstavce z předchozí strany. Obsah (Tabola) jako `seznam` s čísly listů podle tisku.
  Verše jako `verse`. Výpočty bataillonů (počty mužů, řad, odmocniny) přelož přesně, čísla neměň.
- **Obrázky – vyřízni je sám.** Každé vyobrazení (dřevořez, stroj, šik sázený z písmen a teček, nákres bašty) =
  blok `obrazek` se souborem `drevorez-<sken>.jpg` (druhý na téže straně `drevorez-<sken>b.jpg`) a českým `popis`
  (co ukazuje, počty řad a mužů u šiků, přepis a překlad nápisů a písmen: FRONTE – čelo, SCHINO – týl, Fianco – bok).
  Soubor vytvoř: zjisti obdélník obrazce v plném skenu (podle náhledu, případně pomocí PIL na zmenšeném obrázku) a
  stáhni `…/vallolibrocotine00dell%24<sken>/<x>,<y>,<w>,<h>/<min(w,1000)>,/0/default.jpg` do
  `knihy/della-valle-1528/obrazky/drevorez-<sken>.jpg`; výsledek **otevři a zkontroluj** (nic useknutého, co nejméně
  okolního textu). Je-li celá strana jen obrazec, vyřízni celou sazbu bez okrajů.
- **Překlad (`cs`)**: věrně a čtivě (plynulost „středně“), tón vojenské příručky a v knize IV kodexu cti. `{Termín
  z tisku}` při prvním výskytu na stránce. Kde glosář chybí, zvol překlad, drž ho v celé dávce a navrhni heslo do
  zprávy (glosář needituj).
- **Poznámky**: osoby, místa, bitvy a obléhání (Della Valle sloužil v italských válkách 1500–1527), dobové reálie,
  nejasná místa; tiskové chyby v `de` ponech a vysvětli. Neopakuj výklad glosáře.
- Překladatel nastaví `stav: prelozeno`, kontrolor `stav: zkontrolovano`; `overeno_clovekem` zůstává `false`.

## Výstup
- Edituj jen strany své dávky; stranu před a za dávkou jen čti (návaznost vět).
- Pomocné soubory a skeny jen ve **vlastní podsložce scratchpadu**. Ukládej stranu po straně (při přerušení limitem
  se pokračuje od první strany, která ještě nemá stav `prelozeno`).
- Po dokončení: `python -I nastroje/over_strany.py knihy/della-valle-1528 <id …> --prisne` – 0 chyb.
- Zprávu ulož do `knihy/della-valle-1528/zdroje/kontrola/<preklad|revize>-<dávka>.md`: přehled stran, nejistá čtení ze
  skenu, sporná místa (IT + CS + důvod), seznam vyříznutých obrázků, návrhy hesel (id, cs, italské tvary, kategorie,
  pozn), osoby a místa. Do odpovědi vrať shrnutí do 10 řádků.
