# Společné zadání pro agenty – Reinhard ze Solmsu, Válečný popis (1559)

Projekt: `C:\Projects\RT\MilitaryManuals` (Windows; Python spouštěj `python -I`; soubory v UTF-8 zapisuj nástrojem Write/Edit).
Kniha: `knihy/solms-1559`. Nejprve přečti: `PRAVIDLA_PREKLADU.md`, `knihy/solms-1559/kniha.yaml` a `knihy/solms-1559/glosar.yaml`.

## Zdroje a vizuální kontrola skenů
- **OCR přepis**: `knihy/solms-1559/zdroje/ocr_bsb/NNNN.txt` (`NNNN` = čtyřmístné pole `sken`, např. `0093.txt`).
- **Náhledy skenů (BSB München, `bsb00085168`)**: `C:\Users\houfe\.gemini\antigravity\brain\f42cdff0-0a05-49ca-9b6f-c93bb2ae806c\scratch\solms_img\sNNN.jpg` (`NNN` = třímístné pole `sken`, např. `s009.jpg`, `s093.jpg`–`s248.jpg`). Prohlížej je nástrojem `read_file` u **každé** strany, kterou přepisuješ z OCR, a u všech podezřelých či nejasných míst při revizi `de`.
- **Dřevořezy a tabule**: `knihy/solms-1559/obrazky/` (`drevorez-1.jpg`, `drevorez-090.jpg`, `drevorez-092.jpg`, `tab-01.jpg`, `drevorez-120.jpg` až `drevorez-228.jpg`). U každého obrázku si snímek prohlédni a doplň výstižný, odborný `popis`.

## Čím se Solmsův tisk liší (pravidla pro `de`)
- **Ozdobné iniciály na začátku kapitol**: OCR počáteční iniciálu často vynechává nebo zkomolí (`In Oberster Kriegsher?` místo `EIn Oberster Kriegsherr`, `Er Feldmarschalck` místo `DEr Feldmarschalck`, `Achtmeister` místo `WAchtmeister`, `Je` místo `DIe`, `Nfenglich` místo `ANfenglich`). Vždy ověř iniciálu ve skenu `sNNN.jpg` a doplň ji!
- **Opravy OCR při zachování dobového pravopisu**:
  - Oprav záměny typické pro frakturu v BSB OCR: `f`/`ſ`/`s`, `u`/`n`/`v`, `o`/`a`, `z`/`r`, `k`/`tz`, `rr`/`z`, `?` v slovech (`Kriegsher?` → `Kriegsherr`), `\!`, knihovní razítka/signatury v OCR (`00085168`, `Finis cod.`, `gem 3663`).
  - Dlouhé `ſ` vždy přepiš jako `s`; zkrácené nosovky rozepiš (`vñ` → `vnd`, `mā` → `man`, `rechtē` → `rechten`, `Kriegßmāner` → `Kriegßmanner`) a `ꝛc.` → `etc.`.
  - Vynech běžící záhlaví (`Das ander Buch.`, `Von beschreibung der 24. Kriegsämpter.`), čísla listů (`1`–`87`), tiskařské signatury archů (`a ij`, `b iij`, `c`, `m ij`…) a **kustody** pod sazbou.
  - Slova rozdělená na konci řádku spoj; slovo rozdělené přes **hranici stran** přesuň **celé na stranu, kde končí** (`PRAVIDLA_PREKLADU.md` § 1).
  - Dobový pravopis tisku zachovej (`vnd`, `auff`, `Lantsknecht`, `Prouoß`, `Reutter`, `Keyser`). Skutečné tiskařské chyby předlohy (jako *Nutz*/*Rechs*, či chybné číslování v nadpisech tisku) zachovej v `de` a vysvětli v `poznamky`.
- **Stránkování**: arabská foliace `001r`–`087v` + předsádka `titul-svazek` (9), `erb-solms` (90), `titul` (91), `titul-v` (92) + tabule `tab-01` (102). Skeny `101` a `215` jsou prázdné nepotištěné líce (nejsou v edici).

## Struktura bloků a nadpisů
- **`uroven: 1`**: hlavní titulní listy (`titul-svazek` – *Das erst Buch.*, `titul` – *Das ander Buch.*).
- **`uroven: 2`**: hlavní kapitoly jednotlivých válečných úřadů a velkých řádů (např. *Oberster Kriegsherr*, *Oberster Feldhauptman*, *Von des Feldmarschalcks ampt*, *Von dem obersten Zeugmeister Ampt*, *Von des obersten Leutenants oder Feldhauptmans ampt*, *Oberst Prouiantherr*, *Oberster vber alle Reutter*, *Von des Wagenburgmeisters Ampt*, *Der Reuter Wachtmeister*, *Der Wagenmeister*, *Von der Reutter quartiermeister*, *Von der Reutter Hauptleuten oder Rittmeistern*, *Vondes Oberster ampt vber das Fußuolck*, *Artickelsbriff der Lantsknecht*, *Ordnung einer Besatzung*, *Gerichtsordnung der Lantsknecht*).
- **`uroven: 3`**: podkapitoly, jednotlivé nižší úřady a vložené listiny (*Anbringen vnnd begern…*, *Commis Ordnung*, *Vom Obersten Prouofen ampt*, *Von der Lantskneckt Hauptleut*, *Von den gemeinen Fendrichen*, *Der Scharpffrichter*, *Der Reutter Bestallung*, *Bestelbrieff der Lantskneckt Obersten* atd.).
- **Tabulky (`typ: tabulka`)**: Dvousloupcové výpisy žoldu (např. `064r`) nebo strukturované přehledy zásob (pokud tvoří zřetelnou tabulku ve skenu) zapiš jako `typ: tabulka`, kde `de` i `cs` jsou seznamy řádků (seznam buněk `[sloupec1, sloupec2, …]`) se shodným počtem řádků a buněk; jednoduché výčty jako `typ: seznam`.
- **Párování 1 : 1**: bloky musí přesně odpovídat odstavcům tisku. Přecházející odstavec má `pokracovani: true` bez „…“. Všechna `zarovnat: true` vyřeš a příznak smaž.

## Závazná terminologie (dle `knihy/solms-1559/glosar.yaml`)
Celá kniha musí důsledně dodržovat jednotnou terminologii edice (stejně jako `fronsberger-1564`), zejména:
- *Feldmarschalck* → **`polní maršálek`** (nikoli *polní maršál*)
- *Prouoß / Profoß* → **`profous`** (nikoli *probošt*)
- *Wachtmeister* → **`vachmistr`** (nikoli *strážmistr*, *vachtmistr*)
- *Quartiermeister* → **`kvartýrmistr`** (nikoli *kvartýrmajstr*)
- *Forirer / Forierer / Fourier* → **`furýr`** (nikoli *furiér*)
- *Fürer* → **`vůdce`** (nikoli *fýrer*)
- *Hurnweibel* → **`šikovatel trénu`** (nikoli *pobočný sluha*, *hurnvejbl*)
- *Trabant* → **`drabant`** (nikoli *trabant*)
- *Steckenknecht* → **`profousův pacholek`** (nikoli *dráb*)
- *Stockmeister* → **`žalářník`**
- *Nachrichter / Scharpffrichter* → **`kat`**
- *Feldscherer* → **`ranhojič`** (nikoli *polní felčar*)
- *Prouiantmeister* → **`proviantmistr`** (nikoli *provizorní/proviantní mistr*)
- *Prouiantherr* → **`proviantní pán`**
- *Wagenburgmeister* → **`mistr vozové hradby`**
- *Lantsknecht* → **`lancknecht`** (nikoli *landsknecht*)
- *Doppelfoldner / Toppelfoldner* → **`dvojžoldnéř`** (nikoli *dvojnásobný žoldnéř*)
- *Renfanen / Renfan* → **`předvojová korouhev`** (nikoli *úderný prapor*)
- *Bestallung / Bestelbrieff* → **`služební list`** (nikoli *jmenovací dekret*, *najímací list*)
- *Commis* → **`komis`**, *Harst* → **`harst`**, *Marzel* → **`marcel`**, *Gastrecht* → **`hostinské právo`**
- *Spieß* → **`píka`**; *Schlange / Notschlange / halbe Schlange* → **`kulverina`** / **`těžká kulverina`** / **`poloviční kulverina`**; *Polwerck / Bollwerck* → **`bolverk`**; *Paßtey* → **`bašta`**.
- Při prvním výskytu termínu na stránce doplň `{Termín z tisku}` podle pravopisu této stránky.

## Ověření a zpráva
- Nikdy neměň `overeno_clovekem` na `true`.
- Překladatelské dávky nastavují `stav: prelozeno`, kontrolní dávky `stav: zkontrolovano`.
- Po dokončení spusť `python -I nastroje/over_strany.py knihy/solms-1559 <strany> --prisne` — musí skončit s **0 chybami** a bez opravitelných varování.
- Zprávu ulož do `knihy/solms-1559/zdroje/kontrola/<soubor>.md` (přehled změn po stranách, ověřená OCR místa ze skenů, sporná místa DE+CS k rozhodnutí, návrhy do glosáře s `id/cs/de/kategorie/pozn`).
