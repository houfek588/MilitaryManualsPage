# Zadání 2. revize – Solms 1559 (korektura překladu a plynulost)

Kniha už prošla překladem a kontrolou (zprávy `zdroje/kontrola/*.md`, souhrn `SPORNA_MISTA.md`). Tato revize se soustředí
na **kvalitu češtiny a přesnost překladu**, ne na formát. Platí `PRAVIDLA_PREKLADU.md`, `zdroje/ZADANI_AGENTUM.md`
a `kniha.yaml` → `poznamky_k_prekladu`; níže uvedená rozhodnutí autora projektu (2026-11-17) mají přednost.
Revize probíhá **postupně po knihách** (nejdřív První kniha).

## Rozhodnutí autora projektu: plynulost „středně“
- Dlouhá řetězená souvětí (… / so / vnd / dann …) **děl na samostatné věty tam, kde to smysl dovolí** – v rámci bloku,
  párování blok ↔ odstavec tisku se nemění. Přechod přes hranici strany (`pokracovani: true`) musí dál sedět s originálem.
- **Přirozený český slovosled**, sloveso ne automaticky na konec; méně opakování „a“, „také“, „tak“, „jakož i“, „týž“;
  odkazovací zájmena („tentýž“, „tyto“) nahraď jasným podmětem, kde by čtenář tápal, kdo co dělá.
- **Zachovej dobový tón** (úřední řeč 16. století, listiny, přísahy) a **autorovu 1. osobu** („mám za to“, „chci“, „pojednám“).
  Formule listin a přísah („budete přísahat…“, „Jeho Římské císařské Veličenstvo“) ponech v ustálené podobě.
- Archaismy střídmě; text má být čtivý pro dnešního reenactora a historika.

## Rozhodnutí autora projektu: terminologie (2026-11-17)
- **Oberst / Oberster / Obersten** (samostatně, bez dalšího titulu) = vždy **„plukovník“** – i tam, kde jde o vrchního
  velitele celého vojska. Ne „nejvyšší velitel“, „nejvyšší polní hejtman“ ani „představený“. Složeniny (*Oberster
  Feldhauptman* = nejvyšší polní hejtman, *Oberster Zeugmeister* = nejvyšší zbrojmistr…) podle glosáře.
  **Výjimka (2026-11-19):** v Deváté knize (Burgundský řád) Oberst ve smyslu vrchního velitele celého vojska
  = „vrchní velitel“ (9-004v, 9-005v, 9-007v, 9-011r, 9-018v); velitelé ležení, posádky města či loďstva zůstávají „plukovník“.
- **Fendlin / Fendlein u jízdy = „korouhev“**, u pěchoty „praporec“; u smíšených míst („zu roß oder zu fůß“) obojí.
- *Kriegßleut* = „válečníci“; *Justitien* = „justice / spravedlnost“ (heslo `justice`, ne `soud`).
- Knihy 6–9: *Fendrich / Fenderich* u jízdy = „korouhevník“; *Durchleuchtig* (knížata) = „osvícený“;
  *Drosser / Droß* = „trénní kůň“; *Summa lat.* = „součet strany“; *Veldoberster* = „polní plukovník“;
  *Gerüster pferd* = „zbrojný kůň“; *Feurpfeil* = „zápalný šíp“; *Büchsenpulver* = „střelný prach“.
- **Revize knih 6–9** (strany ve stavu `prelozeno`, přeložené od nuly z OCR): ověř přepis `de` proti skenu u všech
  nejistých míst a tabulek (čísla, jména, součty), věrnost a plynulost překladu; po kontrole nastav `stav: zkontrolovano`.

## Na co se zaměřit
- **Věrnost**: porovnej každý blok `cs` s `de`. Hledej vynechaný či přidaný text, posunutý význam, chybně pochopené zápory
  (*nit* = ne), předložky a příslovce raně novohorní němčiny (*vorhin* = předtím, *ob* = nad, *gůt zu achten* = snadno
  usoudit, *erleiden* = snést, *verwahren* = zajistit…), slovesné vazby a podměty. Čísla, míry a mince přesně.
- **Terminologie**: podle `glosar.yaml` a tabulky v `ZADANI_AGENTUM.md`. Stejný pojem = stejné slovo v celé dávce;
  `{Termín z tisku}` při prvním výskytu na stránce. Kde glosář chybí nebo nesedí, napiš návrh do zprávy (glosář needituj).
- **Sporná místa ověř ve skenu**: `curl -s -o <scratchpad>/s<NNNNN>.jpg "https://api.digitale-sammlungen.de/iiif/image/v2/bsb00085168_<NNNNN>/full/1400,/0/default.jpg"`
  (`NNNNN` = pole `sken` doplněné nulami na 5 číslic) a otevři nástrojem Read; OCR text je v `zdroje/ocr_bsb/NNNN.txt`.
  Chyby OCR v `de` oprav (dobový pravopis zachovej), tiskové chyby tisku nech a vysvětli poznámkou.
- **Poznámky**: oprav nepřesné, zbytečné vynech; nové jen tam, kde čtenář bez nich nepochopí reálii nebo termín.
  Poznámky nemají opakovat výklad z glosáře.
- Neměň strukturu bloků, `sken`, `id`, `overeno_clovekem` (zůstává `false`); odkazy `[[id|text]]` zachovej.

## Hranice dávek a výstup
- Edituj jen strany své dávky; poslední stranu před dávkou a první za ní si jen přečti (návaznost vět přes hranici stran).
- Po úpravách: `python -I nastroje/over_strany.py knihy/solms-1559 <id …> --prisne` – 0 chyb.
- Zprávu ulož do `knihy/solms-1559/zdroje/kontrola/revize2-<dávka>.md`: hlavní změny po stranách (stručně, ukázky před → po),
  ověřená místa ze skenů, sporná místa k rozhodnutí (DE + CS + důvod), návrhy do glosáře (id, cs, de, kategorie, pozn).
  Glosář ani `SPORNA_MISTA.md` needituj.
- Do odpovědi vrať shrnutí do 15 řádků.
