# Společné zadání pro agenty – Michael Ott von Echterdingen, Kriegsordnung (kolem 1530)

Projekt: `C:\Projects\RT\MilitaryManuals` (Windows; Python spouštěj `python -I`, v Pythonu nastav
`sys.stdout.reconfigure(encoding='utf-8')`; soubory zapisuj v UTF-8). Kniha: `knihy/ott-1530`.
Nejdřív přečti: `PRAVIDLA_PREKLADU.md`, `knihy/ott-1530/kniha.yaml` (hlavně `poznamky_k_prekladu`) a
`knihy/ott-1530/glosar.yaml`.

## Strany
- Strany jsou kostry (`stav: chybi_original`, `bloky: []`), založené nástrojem `nastroje/zaloz_strany.py` (`--od 1 --do 84 --prvni 1 --titul 1 --vynech 2,84`).
  Pole `id`, `list`, `strana`, `sken` neměň. Id: `titul` (sken 1) a listy `002r` … `042r` (list [N] r = sken 2N−1).
- **Originál (`de`)**: výchozí je OCR `knihy/ott-1530/zdroje/ocr_bsb/NNNN.txt` (NNNN = sken, 4 číslice), u tohoto tisku
  hodně chybné. **Každou stranu porovnej se skenem**:
  `curl -s -o <tvoje-podsložka-scratchpadu>/sNNN.jpg "https://api.digitale-sammlungen.de/iiif/image/v2/bsb00089558_<NNNNN>/full/1600,/0/default.jpg"`
  (NNNNN = sken na 5 číslic) a otevři nástrojem Read; drobné písmo zvětši výřezem
  (`…/bsb00089558_<NNNNN>/<x>,<y>,<w>,<h>/1200,/0/default.jpg`). Pravopis tisku zachovej (švábské *ai/ay*, *ů*, *Zeügmaister*),
  zkratky rozepiš (vñ → vnd, ē → en, ꝛc. → etc.), vynech signatury archů (a ij …) a kustody; slovo rozdělené přes hranici
  stran patří celé na stranu, kde končí. Ozdobné iniciály doplň do slova.
- **Bloky**: nadpisy (`uroven` podle `kniha.yaml`), odstavce 1 : 1 podle sazby, `pokracovani: true` u odstavce, který
  přechází z předchozí strany. Výčty (zásoby, děla, koně, vozy, munice, žold) jako `seznam` nebo `tabulka` se stejným
  počtem položek v `de` i `cs`; čísla a míry přesně (centner = cent, fl. = zlatý, kr. = krejcar).
- **Překlad (`cs`)**: věrně a čtivě – plynulost „středně“: dlouhá souvětí dělit na věty, kde to smysl dovolí, přirozený
  český slovosled, dobový tón řádů a přísah zachovat. Terminologie podle glosáře a `poznamky_k_prekladu`
  (Oberst = plukovník, u vrchního velitele celého vojska „vrchní velitel“; Fendlin = praporec, u jízdy korouhev;
  Kriegßleut = válečníci). `{Termín z tisku}` při prvním výskytu na stránce. Kde glosář chybí, zvol překlad, drž ho
  v celé dávce a navrhni heslo do zprávy (glosář needituj).
- **Poznámky**: reálie, nejasná místa, tiskové chyby (v `de` je ponech, vysvětli). Neopakuj výklad glosáře.
  Ott byl předlohou Fronspergera (`knihy/fronsberger-1564`) – shodné pasáže smíš porovnat s tamním překladem
  kvůli terminologii, ale překládej Ottův text, ne Fronspergerův.
- Překladatel nastaví `stav: prelozeno`, kontrolor `stav: zkontrolovano`; `overeno_clovekem` zůstává `false`.

## Výstup
- Edituj jen strany své dávky; stranu před a za dávkou jen čti (návaznost vět).
- Pomocné soubory a skeny jen ve **vlastní podsložce scratchpadu** – sdílené soubory přepisují jiní agenti.
  Ukládej stranu po straně (při přerušení limitem se tak nic neztratí).
- Po dokončení: `python -I nastroje/over_strany.py knihy/ott-1530 <id …> --prisne` – 0 chyb.
- Zprávu ulož do `knihy/ott-1530/zdroje/kontrola/<preklad|revize>-<dávka>.md`: přehled stran, nejistá čtení ze skenu,
  sporná místa (DE + CS + důvod), návrhy hesel (id, cs, de, kategorie, pozn). Do odpovědi vrať shrnutí do 10 řádků.
