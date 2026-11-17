# Společné zadání pro agenty – Bernská výcviková příručka (1615)

Projekt: `C:\Projects\RT\MilitaryManuals` (Windows; Python spouštěj `python -I`; soubory s diakritikou zapisuj nástrojem Write/Edit).
Kniha: `knihy/bern-1615`. Přečti: `PRAVIDLA_PREKLADU.md`, `knihy/bern-1615/kniha.yaml` (hlavně `poznamky_k_prekladu`) a `knihy/bern-1615/glosar.yaml`.

## Čím se tato kniha liší od Fronspergera a Lavatera
- **Zdroj originálu**: Německý text v YAML vychází z OCR digitalizace Universitätsbibliothek Bern (e-rara.ch, ID `2050509`), které obsahuje chyby.
  - Opravuj chyby OCR podle smyslu, dobového pravopisu i vizuálních skenů (stažené náhledy problémových stran z předsádky a zlomů jsou v `C:\Users\houfe\.gemini\antigravity\brain\f42cdff0-0a05-49ca-9b6f-c93bb2ae806c\scratch\erara_check\c<sken>.jpg`, kde `<sken>` = pole `sken` v YAML souboru).
  - Typické opravy: zdvojený kustod na přelomu stran smaž (`Vnder-` na `[8]`/`[9]`, `Hand/` na `029`/`030`), slovo rozdělené přes hranici stran přesuň **celé na stranu, kde končí** (`PRAVIDLA_PREKLADU.md` § 1), rozepiš tiskařské zkratky s makronem (`haltē` → `halten`, `Regiméts` → `Regiments`, `Vögtē` → `Vögten`, `Herꝛen` → `Herren`, `ꝛc.` → `etc.`, `vz`/`dz` → `daß`), oprav zkomoleniny (`fehztigen` → `fertigen`, `Aßlegung` → `Außlegung`, `mert` → `wert`, `Heyten` → `Heyden`, `lesen Kriegen` → `lehren Kriegen`, `funft` → `Gunst`, `Noht manglen` → `Noht manglen`, `Zugenden` → `Tugenden`, `Ensen` → `Eysen`, `rechts vnd` → `rechts vmb`, `Herstele euch` jen pokud je i v tisku, jinak ověř ve skenu).
- **Stránkování**: `id` stran předsádky: `titul` (sken 3), `citaty` (sken 4), `predmluva-01`..`predmluva-14` (skeny 5–18); číslované strany `001`–`052` (skeny 19–70).
- **Úrovně nadpisů**:
  - `uroven: 1` = hlavní části (`titul`, `Vorred.`/`Předmluva` na `predmluva-01`, `Cvičení s mušketou` na `001`, `Cvičení s píkou` na `025`, `Následují obraty bitevního šiku` na `041`).
  - `uroven: 2` = pododdíly („Povelová slova a rozkazy…“, „Následuje stráž“, „Výklad těchto vojenských termínů“).
  - `uroven: 3` = nadpisy jednotlivých povelů nad výkladovými odstavci (mušketa 1–40, píka 1–19, obraty 1–33).
- **Povely (závazné sjednocení)**:
  - Všechny povely (v seznamech i v nadpisech výkladů u muškety, píky i obratů) sjednoť na **2. osobu množného čísla rozkazovacího způsobu** (*Skloňte mušketu a sejměte ji z ramene.*, *Sejměte doutnák.*, *Otevřete odměrku nálože (nebo nálož).*, *Nabijte mušketu.*, *Vytáhněte nabiják.*, *Zasuňte nabiják zpět.*, *Vpravo zatočte (nebo vpravo zatočte).*).
  - Odstraň přebytečná lomítka `/` z českých povelů i vět (např. na str. 26), nahraď je přirozenou češtinou (čárkou, spojkou).
- **Terminologie**:
  - *Ladmaß (oder Ladung)* překládej věrně jako **odměrka nálože (nebo nálož)**; význam „apoštol“ uveď v poznámce nebo nech odkaz na glosář (`odmerka-naloze`).
  - *Fourcket* překládej důsledně jako **furketa** (`{Fourcket}`), *Gabel* jako **vidlice** (`{Gabel}`).
  - Vždy piš **mušketa** (oprav všechny tvary *musketa*, *muskety*).
  - Vždy **píka** pro *Spieß* (už většinou je, zkontroluj shodu).
  - *Ladstecken* = **nabiják**; *Laden / Schafft* = **pažba**; *Pfanne* = **pánvička**; *Hahn / Hanen* = **kohout**; *Trucker* = **spoušť**; *Schwanschrauben* = **dnový šroub**; *Zündfläschlein* = **prachovnička**.
  - Bernské úřady na `predmluva-01` (sken 5): `rychtář {Schuldtheiß}` (s poznámkou, že v čele republiky Bern stál *Schultheiß*, česky též šultys či starosta), `zemským fojtům {Landtvögten}`, `guvernérům {Gubernatorn}`, `kastelánům {Tschachtlanen}`, `fojtům {Vögten}`, `místodržícím {Statthalteren}`, `podfojtům {Vndervögten}`, `zemským biřicům {Freyweiblen}`, `ammanům {Ammanen}`, `biřicům {Weiblen}` (civilní zřízenci, ne vojenské hodnosti) (+ vysvětlující poznámka k bernské zemské správě).
  - Doplň `{Termín}` v podobě z tisku při **prvním výskytu na každé stránce** (`PRAVIDLA_PREKLADU.md` § 3).
- **Zvláštní strany**:
  - `citaty` (sken 4): oprav latinský text podle skenu (`c4.jpg`) a doplň přesný český překlad všech tří citátů (Polybios 6, Cicero *Pro Murena*, Cicero *De officiis* 1) + stručnou poznámku o autorech.
  - `043`–`051`: vyřeš všechna `zarovnat: true` tak, že český překlad rozdělíš přesně na hranici strany podle německého originálu (`pokracovani: true` na začátku následující strany) a příznak `zarovnat` smažeš.
  - `052`: doplň výstižný `popis` pro erbovní dřevořez `erb-bern.png` (dřevořez znaku města a republiky Bern – kráčející medvěd na šikmém pruhu v kartuši pod nápisem *ENDE.*).
- **Ověření**:
  - Nastav `stav: zkontrolovano` a ponech `overeno_clovekem: false`.
  - Spusť `python -I nastroje/over_strany.py knihy/bern-1615 <id ...> --prisne` a oprav všechny chyby a varování.

## Zpráva
Ulož do `knihy/bern-1615/zdroje/kontrola/<davka>.md`: přehled změn po stranách, ověřená OCR místa ze skenů, sporná místa k rozhodnutí (s citací DE a CS) a návrhy nových hesel do glosáře. Do odpovědi vrať jen stručné shrnutí.
