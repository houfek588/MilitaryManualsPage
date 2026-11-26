# Společné zadání pro agenty – Daniel Wintzenberger, Beschreibung einer Kriegs-Ordnung (Drážďany 1588)

Projekt: `C:\Projects\RT\MilitaryManuals` (Windows; Python spouštěj `python -I`, v Pythonu nastav
`sys.stdout.reconfigure(encoding='utf-8')`; soubory zapisuj v UTF-8). Kniha: `knihy/wintzenberger-1588`.
Nejdřív přečti: `PRAVIDLA_PREKLADU.md`, `knihy/wintzenberger-1588/kniha.yaml` (hlavně `poznamky_k_prekladu`) a
`knihy/wintzenberger-1588/glosar.yaml`.

## Strany
- Strany jsou kostry (`stav: chybi_original`, `bloky: []`), založené nástrojem `nastroje/zaloz_strany.py` (`--od 5 --do 115 --prvni 5 --titul 5`).
  Pole `id`, `list`, `strana`, `sken` neměň. Id: `titul` (sken 5) a listy `001v` … `056r` (list [N] r = sken 2N + 3, [N] v = sken 2N + 4).
- **Originál (`de`)**: výchozí je OCR `knihy/wintzenberger-1588/zdroje/ocr_bsb/NNNN.txt` (NNNN = sken, 4 číslice), u fraktury
  místy chybné. **Každou stranu porovnej se skenem**:
  `curl -s -o <tvoje-podsložka-scratchpadu>/sNNN.jpg "https://api.digitale-sammlungen.de/iiif/image/v2/bsb00032546_<NNNNN>/full/1600,/0/default.jpg"`
  (NNNNN = sken na 5 číslic) a otevři nástrojem Read; drobné písmo zvětši výřezem
  (`…/bsb00032546_<NNNNN>/<x>,<y>,<w>,<h>/1200,/0/default.jpg`). Pravopis tisku zachovej (*vnd*, *Obrister*, *Artalerey*, *Fenlein*),
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
  Druhý díl obsahuje služební a artikulní list Karla V. a hrdelní právo – podobné texty jsou přeložené ve Fronspergerovi
  a Solmsovi (`knihy/fronsberger-1564`, `knihy/solms-1559`); smíš je porovnat kvůli terminologii, ale překládej tento text.
  Zvláštnost digitalizace: strany `014v` a `015r` (skeny 32–33) jsou omylem znovu nasnímané strany `030v` a `031r`
  (skeny 64–65; tatáž fyzická dvojstrana) – přepis i překlad musí být totožné, poznámka upozorní, že pokračování první
  části v digitalizaci chybí.
- Překladatel nastaví `stav: prelozeno`, kontrolor `stav: zkontrolovano`; `overeno_clovekem` zůstává `false`.

## Výstup
- Edituj jen strany své dávky; stranu před a za dávkou jen čti (návaznost vět).
- Pomocné soubory a skeny jen ve **vlastní podsložce scratchpadu** – sdílené soubory přepisují jiní agenti.
  Ukládej stranu po straně (při přerušení limitem se tak nic neztratí).
- Po dokončení: `python -I nastroje/over_strany.py knihy/wintzenberger-1588 <id …> --prisne` – 0 chyb.
- Zprávu ulož do `knihy/wintzenberger-1588/zdroje/kontrola/<preklad|revize>-<dávka>.md`: přehled stran, nejistá čtení ze skenu,
  sporná místa (DE + CS + důvod), návrhy hesel (id, cs, de, kategorie, pozn). Do odpovědi vrať shrnutí do 10 řádků.
