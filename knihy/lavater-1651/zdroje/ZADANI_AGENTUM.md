# Společné zadání pro agenty – Lavater, Kriegs-Büchlein (1651)

Projekt: C:\Projects\RT\MilitaryManuals (Windows, Git Bash; Python spouštěj `python -I`; soubory s diakritikou
zapisuj nástrojem Write/Edit, ne přes heredoc v Bash).
Kniha: `knihy/lavater-1651`. Přečti: `PRAVIDLA_PREKLADU.md`, `knihy/lavater-1651/kniha.yaml` (hlavně
`poznamky_k_prekladu`!) a `knihy/lavater-1651/glosar.yaml`.

## Čím se tato kniha liší od Fronspergera
- **Originál = přepis Deutsches Textarchiv**, ne OCR: `knihy/lavater-1651/zdroje/dta/NNNN.txt` (NNNN = pole `sken`,
  4 číslice). Pole `de` musí obsahově přesně odpovídat tomuto souboru (text celé strany, nic navíc, nic chybějícího).
  V přepisu DTA nic „neopravuj“ – je ruční a přesný. Jedinou povolenou odchylkou jsou slova rozdělená přes hranici
  stran: podle PRAVIDLA § 1 patří celá na stranu, kde končí (to má přednost před doslovnou shodou s DTA). „## “ v souboru = nadpis, „- “ = položka seznamu,
  „[Marg.: …]“ = marginálie (připoj ji do odstavce, ke kterému patří, v podobě „[Marg.: …]“ i v cs), „[obrázek]“ = vyobrazení.
- Stránkování: id stran `001`–`134` = strana tisku; předsádka (frontispis, titul, vazba, venovani, predmluva-1…3,
  vyklad-1…4, slovnicek-1…2, basne-1…4), tabule s mědirytinami `tab-01`…`tab-12` a `errata`.
- Sken strany: `https://www.deutschestextarchiv.de/media/images/lavater_kriegsbuechlein_1659/lavater_kriegsbuechlein_1659_NNNN_800px.jpg`
  (NNNN = sken, 4 číslice; ve vyšším rozlišení `_1600px.jpg`). Stáhni jen obrázky, a to obyčejným `curl -s -L -o <scratchpad>/x.jpg <url>`
  (žádné cookies ani obcházení ochran webu). Text stránek DTA přes web nestahuj – máš ho v zdroje/dta.
- Pracovní překlad měl německé termíny v kulatých závorkách „(Brustwehr)“ – import je většinou převedl na `{Brustwehr}`.
  Zbylé kulaté závorky s německým termínem převeď na `{…}` podle pravidel (jen první výskyt na stránce).
  Opisy typu „{Streychwehr nebo Flancke}“ oprav na `{Streychwehr}` / `{Flancke}` podle tisku.
- Terminologie opevnění: viz glosář (předprseň – ne „hrudí“, bašta, kurtina, flanka, čelo bašty, hrdlo, berma, dolní val,
  krytá cesta, kontreskarpa, ravelin, hornwerk…). Název knihy: „Válečná knížka“; díly: „První/Druhý/Třetí/Čtvrtý díl Válečné knížky“.
- Nové strany zakládej a hotové ukládej s `overeno_clovekem: false` (pole nikdy neměň na true).

## Zpráva
Ulož do `knihy/lavater-1651/zdroje/kontrola/<dávka>.md`: přehled stran (zásadní změny), sporná místa (DE citace + CS + proč),
návrhy do glosáře (id, cs, de, kategorie, pozn – zvlášť opevňovací a vojenské termíny 17. století), osoby a místa.
Glosář ani strany mimo svou dávku needituj. Do odpovědi vrať krátké shrnutí (max. 15 řádků).
