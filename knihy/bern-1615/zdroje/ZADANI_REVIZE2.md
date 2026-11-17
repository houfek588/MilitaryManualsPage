# Zadání 2. revize – Bern 1615 (korektura překladu a plynulost)

Kniha už jednou prošla kontrolou (zprávy `zdroje/kontrola/*.md`, souhrn `SPORNA_MISTA.md`). Tato revize se soustředí na
**kvalitu češtiny a přesnost překladu**, ne na formát. Platí `PRAVIDLA_PREKLADU.md`, `zdroje/ZADANI_AGENTUM.md`
a `kniha.yaml` → `poznamky_k_prekladu`; níže uvedená rozhodnutí autora projektu (2026-11-17) mají přednost.

## Rozhodnutí autora projektu
1. **Povely bez přivlastňovacích zájmen.** Německé „Ewer / euwre“ se v povelech nepřekládá:
   „Skloňte mušketu a sejměte ji z ramene.“, „Vezměte doutnák do pravé ruky.“, „Vyrovnejte zástupy.“
   Zájmeno ponech jen tam, kde nese význam (např. rozlišení vlastní × cizí). Stejně uprav nadpisy povelů nad výkladem –
   **znění povelu v seznamu a v nadpisu výkladu musí být totožné**.
2. **Obraty šiku (str. 41–52) v českém pořadovém stylu** – stručně, blízko originálu i výkladu v knize:

   | Originál | Česky |
   |---|---|
   | Reyen / Glider | Zástupy. / Řady. |
   | Rechtsvmb / Lincksvmb | Vpravo vbok. / Vlevo vbok. |
   | Richtet euwere Reyen / Glider | Vyrovnejte zástupy. / Vyrovnejte řady. |
   | Rechtsvmb kehrt euch / Lincksvmb kehrt euch | Vpravo čelem vzad. / Vlevo čelem vzad. |
   | Herstelt euch / Rechts herstelt euch | Do původního postavení. / Vpravo do původního postavení. |
   | Rechts schliesset euwre Reyen / Schliesset euwre Glider | Vpravo semkněte zástupy. / Semkněte řady. |
   | Rechts offnet euwre Reyen / Vorwerts offnet euwre Glider | Vpravo rozestupte zástupy. / Vpřed rozestupte řady. |
   | Rechts schwingt/ oder schwenckt euch | Vpravo zakružte neboli zatočte. |
   | Euwer Reyen rechts vmb kehrt | Zástupy vpravo čelem vzad. (protipochod/kontramarš vysvětli v poznámce podle výkladu) |
   | Rechts doppliert euwre Reyen / Glider | Vpravo zdvojte zástupy. / Vpravo zdvojte řady. |

   „Herstelt euch“ = návrat do postavení před předchozím obratem či zdvojením – ověř podle výkladu na str. 44–52 a sjednoť
   i v textu výkladu. Pokud výklad vyžaduje jiné znění, napiš to do zprávy (nevymýšlej vlastní systém).

## Na co se zaměřit
- **Věrnost**: porovnej každý blok `cs` s `de`. Hledej vynechaný či přidaný text, posunutý význam, špatně pochopená slovesa
  a předložky raně novohorní němčiny (obsich = vzhůru, nidsich = dolů, hindersich = dozadu, nebends = vedle, zuvor = předtím…).
  Technický smysl úkonů (nabíjení, držení muškety a píky, obraty) musí být srozumitelný a správný.
- **Plynulost**: přirozený český slovosled, žádné německé konstrukce („má být pilně dbáno, aby…“ jen kde to sedí), méně
  opakování „opět / zase / tak / nato“, rozdělení přetížených souvětí, kde to párování dovolí. Výklad je psán ve 3. osobě
  („voják má…“) – ponech, ale ať zní česky. Archaismy střídmě; text má být čtivý pro dnešního reenactora.
- **Terminologie**: podle `glosar.yaml` a tabulky v `ZADANI_AGENTUM.md` (mušketa, píka, furketa × vidlice, odměrka nálože,
  nabiják, pažba, pánvička, kohout, spoušť, doutnák, prachovnička, zástup = Reyen, řada = Glid). Stejný úkon = stejné sloveso
  v celé dávce (např. „přiložte“ pro anlegen, „ofoukněte“ pro abblasen).
- **Sporná místa ověř ve skenu**: `curl -s -L -o <scratchpad>/s<sken>.jpg "https://www.e-rara.ch/i3f/v20/<2050511+sken>/full/1200,/0/default.jpg"`
  a otevři nástrojem Read (sken je pole `sken` ve stránce; např. str. 41 = sken 59 = 2050570). Chyby OCR v `de` oprav
  (dobový pravopis zachovej), tiskové chyby tisku nech a vysvětli poznámkou.
- **Poznámky**: oprav nepřesné, zbytečné vynech; nové jen tam, kde čtenář bez nich nepochopí úkon nebo termín.
- Neměň strukturu bloků, `sken`, `id`, `overeno_clovekem` (zůstává `false`); odkazy `[[id|text]]` zachovej.

## Hranice dávek a výstup
- Edituj jen strany své dávky; první stranu před a za dávkou si jen přečti (návaznost vět přes hranici stran).
- Po úpravách: `python -I nastroje/over_strany.py knihy/bern-1615 <id …> --prisne` – 0 chyb.
- Zprávu ulož do `knihy/bern-1615/zdroje/kontrola/revize2-<dávka>.md`: hlavní změny po stranách (stručně, ukázky před → po),
  sporná místa k rozhodnutí (DE + CS + důvod), návrhy do glosáře. Glosář ani `SPORNA_MISTA.md` needituj.
- Do odpovědi vrať shrnutí do 15 řádků.
