# Postup přidání nové knihy

Návod shrnuje, jak se do edice dostaly knihy s pracovním překladem (Fronsperger `fronsberger-1564`, Lavater
`lavater-1651`, Bern, Solms) i knihy přeložené jen z odkazu na digitalizaci (Ott `ott-1530`,
Wintzenberger `wintzenberger-1588` – pro ně viz [rychlý postup](#0-kniha-jen-z-odkazu-na-digitalizaci)).
Pravidla překladu a formát dat popisuje [PRAVIDLA_PREKLADU.md](PRAVIDLA_PREKLADU.md), obecnou strukturu a nástroje
[README.md](README.md). Tady je pořadí kroků a na co si dát pozor.

Na konci je [kontrolní seznam](#kontrolní-seznam).

---

## 0. Kniha jen z odkazu na digitalizaci

Stačí zadání typu „Přidej knihu, odkaz: https://www.digitale-sammlungen.de/de/view/bsb…“. Pracovní překlad
není potřeba – originál se přepíše z OCR a skenu, přeloží a zreviduje agenty. Postup (podrobnosti v dalších oddílech):

1. **Metadata a úplnost skenu** (§ 1, § 3): z titulního listu, katalogu (VD16/VD17, OPAC knihovny) a IIIF manifestu.
   Projdi skeny (zmenšený náhled všech snímků), najdi desky, prázdné strany, předsádku, tabule, zdvojené nebo
   chybějící listy a převod **snímek → list/strana** (ověř na signaturách archů a kustodách na několika místech).
2. **Složka a `kniha.yaml`** zkopírované z podobné knihy (Ott = nefoliovaný tisk, Solms = foliace, Bern = stránkování).
   Do `poznamky_k_prekladu` struktura knihy (úrovně nadpisů) a terminologická rozhodnutí specifická pro knihu.
3. **OCR**: `python -I nastroje/stahni_ocr_bsb.py knihy/<kniha> <bsb-id>` (+ manifest do `zdroje/`).
4. **Prázdné strany**: `python -I nastroje/zaloz_strany.py knihy/<kniha> --od <sken> --do <sken> --prvni <sken listu 1> --titul <sken> --vynech <prázdné> --zkouska`,
   ověř výpis podle skenu a spusť bez `--zkouska`. Předsádku před listem 1 (věnování, předmluva) založ ručně.
5. **Glosář** zkopírovaný z knihy stejného období (§ 6).
6. **Zadání agentům** `zdroje/ZADANI_AGENTUM.md` (vzor `knihy/wintzenberger-1588/zdroje/`): zdroj originálu, převod
   snímků, zvláštnosti skenu, struktura, terminologie, kam ukládat zprávy a dočasné soubory.
7. **Překlad**: agenti `prekladatel` v dávkách po 20–25 stranách souběžně (§ 8), každý se svým podadresářem
   scratchpadu. Pak hranice dávek, glosář z návrhů ve zprávách, dřevořezy (§ 7).
8. **Revize**: `zdroje/ZADANI_REVIZE.md` (vzor `knihy/wintzenberger-1588/zdroje/`) se závazným sjednocením termínů
   napříč dávkami a agenti `kontrola-prekladu` nad celou knihou → `stav: zkontrolovano`.
9. **Dokončení** (§ 9–10): nepropojené termíny do glosáře, `SPORNA_MISTA.md`, `over_strany.py`, build, kontrola
   v prohlížeči, README, paměť projektu.

**Výchozí volby, na které se není třeba ptát:** překlad + revize celé knihy; plynulost „středně“ (PRAVIDLA § 3);
dřevořezy jako výřezy s popisem a přepisem nápisů; výchozí terminologie podle PRAVIDLA § 3; prázdné strany
vynechat; tiskové chyby ponechat s poznámkou.

**Rozhoduje autor projektu** – práce se kvůli tomu nezastavuje: agent zvolí výchozí řešení, pokračuje a na konci
ho vyjmenuje v závěrečné zprávě nebo v `SPORNA_MISTA.md`: český název knihy (`nazev` – agent navrhne věcný překlad
titulu), odchylky od výchozí terminologie, nejasná místa textu, vady exempláře (chybějící listy – hledat jinou
digitalizaci?), zvýšení verze webu (dělá autor). Zeptat se předem je namístě jen tehdy, když by špatná volba
znamenala předělat velkou část práce (např. dvě různá vydání téhož díla).

**Limity použití:** agenti ukládají stranu po straně a zprávu píší na konci. Když dávka spadne na limit, pokračuje
se zprávou téže dávce (ne novým agentem) – strany se stavem `prelozeno` / `zkontrolovano` jsou hotové.

---

## 1. Podklady

| Co | Kde vzít | Poznámka |
|---|---|---|
| **Sken originálu** | BSB/MDZ (digitale-sammlungen.de) – IIIF obrázky i OCR přes API; Deutsches Textarchiv; HAB, ÖNB… | Google Books automatický přístup blokuje – nepoužitelné pro skripty. |
| **Text originálu** | OCR skenu (BSB hOCR) nebo hotový přepis (DTA TEI) | Ruční přepis (DTA) je přesnější než OCR – pak se v něm nic „neopravuje“. |
| **Pracovní překlad** | Export z Google Docs do `.md` (uložit do složky `<Autor>/` v kořeni) | Archiv, po importu se už needituje. |
| **Licence** | Stránka skenu / přepisu | Uvádí se v `kniha.yaml` (`sken.licence`, `sken.paticka`). |

**Ověř úplnost skenu dřív, než mu uvěříš.** U Fronspergera starší digitalizace (= Google Books) tiše
vynechala tři dvojstrany a vypadalo to jako chyba foliace. Kontroluj návaznost textu, kustody (první slovo další
strany pod sazbou) a signatury archů. Když existuje víc digitalizací, vyber tu úplnou.

---

## 2. Složka knihy

```
knihy/<autor>-<rok>/          id knihy: malá písmena bez diakritiky, autor-rok (je i v adrese webu)
  kniha.yaml                  metadata, zdroj skenů, pokyny k překladu
  glosar.yaml                 terminologie = věcný rejstřík
  strany/<id>.yaml            jedna strana tisku = jeden soubor (zdroj pravdy)
  obrazky/                    vyobrazení (dřevořezy, mědirytiny, obrázky z pracovního překladu)
  zdroje/                     OCR / přepis po stranách, manifest, zprávy z kontrol, zadání pro agenty
  SPORNA_MISTA.md             souhrn sporných míst k rozhodnutí (vzniká při kontrole)
```

Build zařadí do rozcestníku každou složku v `knihy/`, která má `kniha.yaml` – nic dalšího se registrovat nemusí.

---

## 3. `kniha.yaml`

Nejjednodušší je zkopírovat `kniha.yaml` z knihy s podobným číslováním a přepsat ho.

| Pole | Význam |
|---|---|
| `id` | stejné jako název složky |
| `nazev`, `nazev_orig`, `podtitul` | český název (vybírá autor projektu), původní název, podtitul z titulního listu |
| `autor`, `autor_zivot`, `vydani`, `rok`, `katalog`, `rozsah`, `jazyk_orig` | bibliografické údaje (VD16/VD17, počet listů/stran) |
| `jazyk` | jazyk originálu: `de` (výchozí) nebo `it`; řídí normalizaci tvarů v glosáři (`build.py` → `NORM`, `app.js` → `normDe`), popisky webu a kontrolu OCR. Nový jazyk = doplnit normalizaci v obou souborech a `KONCOVKY_JAZYK` |
| `popis` | 2–3 věty o obsahu – zobrazí se v rozcestníku |
| `prekladatel` | kdo/jak překládal |
| `strankovani` | `folio` (tisk číslovaný po listech → „fol. XII r“, id stran `012r`) nebo `strany` (→ „str. 12“, id `012`) |
| `strany_poznamka`, `zdroj_textu` | vysvětlení číslování a původu německého textu (stránka „O edici“) |
| `sken.*` | instituce, signatura, `url_dilo`, `url_strana` a `url_obrazek` se zástupnými znaky `{sken}`, `{sken4}`, `{sken5}` (číslo snímku doplněné nulami na 4/5 číslic), `{sirka}`; `licence`, `paticka` |
| `poznamky_k_prekladu` | pokyny pro překladatele a kontrolory: zdroj originálu, úrovně nadpisů (co je díl/kniha = 1, kapitola = 2, podnadpis = 3), zvláštnosti knihy |

Pořadí stran na webu určuje **pole `sken`** (číslo snímku) v každé straně – předsádka, tabule i errata se tak
zařadí samy tam, kde jsou ve skenu.

---

## 4. Text originálu po stranách

Do `zdroje/` připrav text originálu rozdělený podle snímků (`NNNN.txt`, NNNN = `sken`). Podle toho čerpají import,
překladatel i kontrola úplnosti.

- **OCR z BSB:** `python -I nastroje/stahni_ocr_bsb.py knihy/<kniha> <bsb-id>` → `zdroje/ocr_bsb/NNNN.txt`.
  Uložit si i IIIF manifest (`zdroje/manifest_<bsb-id>.json`) – je potřeba pro výřezy obrázků.
- **OCR z Internet Archive:** `python -I nastroje/stahni_ocr_ia.py knihy/<kniha> <ia-id>` → `zdroje/ocr_ia/NNNN.txt`
  (NNNN = číslo listu skenu = číslo souboru `_NNNN.jp2`). Obrázky přes IIIF
  `https://iiif.archive.org/iiif/<ia-id>%24<sken>/…` (server přesměrovává – `curl -L`), stránka v prohlížeči
  archive.org má číslo n = sken − 1 (`sken.zaklad_id: -1` a `{erara_id}` v `url_strana`; vzor `knihy/della-valle-1528`).
  OCR archivu bývá u starých tisků špatné – agenti pak přepisují ze skenu. Nástroj `vyrez_drevorezy.py` umí jen BSB;
  u jiných zdrojů vyříznou obrázky přímo překladatelé (zadání v `ZADANI_AGENTUM.md` Della Valla).
- **Přepis DTA:** stáhnout TEI XML ručně v prohlížeči (web DTA má ochranu proti robotům – neobcházet ji),
  uložit do `zdroje/` a `python -I nastroje/dta_strany.py knihy/<kniha> zdroje/<soubor>.xml` → `zdroje/dta/NNNN.txt`
  (typografické znaky se rovnou převedou: ſ→s, uͤ→ü, ꝛ→r).
- Najdi převod **číslo strany/listu → číslo snímku** (u Fronspergera list N r = snímek 7 + 2N) a zapiš ho do
  `sken.poznamka`. Ověř ho na několika místech napříč knihou.

---

## 5. Strany (`strany/*.yaml`)

**Id stran:**
- foliace: `001r`, `001v` …; stránkování: `001` … (tři číslice, odpovídá číslu v tisku),
- nečíslované části slovně: `titul`, `venovani-1`, `predmluva-1`, `vyklad-1`, `errata` …,
- samostatné tabule s rytinami: `tab-01` …, `frontispis`.

**Import pracovního překladu.** Importy jsou jednorázové a psané pro konkrétní dokument – pro novou knihu
zkopíruj `nastroje/import_lavater.py` (přepis DTA) nebo `nastroje/import_md.py` (OCR) a uprav:
- rozpoznání značek stran v `.md` (každý dokument je značí jinak),
- seznam předsádky a tabulí (u Lavatera `PREDSADKA`, `TABULE`, `ZAVER`),
- párování odstavců DE ↔ CS (zrcadlové párování je nejdůležitější pravidlo – PRAVIDLA § 1).

Import zapíše `zdroje/import_report.txt` – projdi ho: chybějící strany, nespárované bloky (`zarovnat: true`),
hvězdičkové termíny `[X]*` (= podle autora překladu sem patří poznámka).

Strany, které v pracovním překladu chybí, se založí prázdné (`stav: chybi_original`) a doplní je agent.
**Bez pracovního překladu** založ všechny strany nástrojem `nastroje/zaloz_strany.py` (viz § 0, bod 4).
Každá strana začíná s `overeno_clovekem: false`.

Pozor na **slova rozdělená přes hranici stran**: celé slovo patří na stranu, kde končí (PRAVIDLA § 1).

---

## 6. Glosář (`glosar.yaml`)

- Začni kopií glosáře existující knihy: velká část vojenské terminologie je společná a hesla, která se v knize
  nevyskytují, build na web nedá.
- Doplň termíny typické pro novou knihu a období (u Lavatera opevnění 17. stol.: bašta, kurtina, ravelin…).
  Rozhodnutí o sporné terminologii zapiš do `pozn` nebo `nepouzivat` (zakázané překlady hlídá `over_strany.py`).
- `de` = tvary z tisku. Běžné pádové koncovky (‑n, ‑en, ‑e, ‑s, ‑es, ‑er, ‑ern, ‑em) build doplní sám,
  ostatní varianty pravopisu (Ygel/Igel, Lärmen/Lermen) je třeba vypsat.
- Tvar, který se odvodí koncovkou chybně (Massen ≠ Maß), dej do seznamu `bez_odkazu` na začátku souboru.
- `hledat` = regulární výrazy českých tvarů pro rejstřík. U obecných slov (velitel, stráž) nech `[]` – rejstřík
  pak ukáže jen místa označená německým termínem.

Glosář upravuje jen hlavní relace (ne agenti v dávkách) – agenti návrhy hesel píšou do svých zpráv.

---

## 7. Obrázky

- **Dřevořezy v sazbě** (BSB): blok `typ: obrazek, soubor: drevorez-<sken>.jpg` a `python -I nastroje/vyrez_drevorezy.py knihy/<kniha>`
  (výřez přes IIIF podle mezer v OCR). Výsledek vždy zkontroluj okem; ruční výřez `--region sken:x,y,w,h`.
- **Tabule s rytinami**: každá jako samostatná strana (`tab-NN`) s blokem `obrazek` a podrobným `popis`
  (co zobrazuje, popisky a písmena, ke kterým stranám patří). Obrázky stáhnout ze skenu do `obrazky/`.
- Každý obrázek potřebuje `popis` – je to text pro čtečky i pro PDF.

---

## 8. Překlad a kontrola (agenti)

1. Napiš **`zdroje/ZADANI_AGENTUM.md`** – čím se kniha liší od ostatních: zdroj originálu, číslování a id stran,
   adresa skenu, vady skenu, terminologické zvláštnosti, kam ukládat zprávy. (Vzor s pracovním překladem:
   `knihy/lavater-1651/zdroje/ZADANI_AGENTUM.md`, bez něj: `knihy/wintzenberger-1588/zdroje/ZADANI_AGENTUM.md`.)
   Pro korekturu celé knihy napiš **`zdroje/ZADANI_REVIZE.md`** se sjednocením termínů napříč dávkami.
2. Rozděl strany do **dávek po 15–25 stranách** podle kapitol.
3. Nepřeložené strany: agent **`prekladatel`**. Přeložené: agent **`kontrola-prekladu`** (věrnost, plynulost,
   terminologie podle glosáře, párování, úplnost originálu). Dávky mohou běžet souběžně, každá jen nad svými stranami.
4. Zprávy z dávek jsou v `zdroje/kontrola/<dávka>.md`. Z nich:
   - zapracuj návrhy do glosáře a sjednoť terminologii napříč knihou (hromadné záměny skriptem, jen kde to originál potvrzuje),
   - vyřeš **hranice dávek** – sousední agenti se občas neshodnou, na které straně končí odstavec nebo rozdělené slovo,
   - sepiš otevřené otázky do `SPORNA_MISTA.md` (rozhoduje autor projektu).
5. Hotové strany mají `stav: zkontrolovano` (= strojová kontrola). `overeno_clovekem` agenti nikdy nenastavují.

---

## 9. Odkazy v textu

- **Termíny do rejstříku** `{Termín}` – po buildu změř, kolik termínů zůstalo bez hesla, a nejčastější doplň do glosáře.
- **Odkazy na strany** `[[id|text]]` (PRAVIDLA § 4):
  - knihy se stránkováním: `python -I nastroje/odkazy_strany.py knihy/<kniha>` označí „Čti s. 5“, „str. 58–59“,
    „3. strany“ (nejdřív `--zkouska`). Ověř, že čísla v textu odpovídají stránkování **tohoto** vydání – části
    převzaté ze starších vydání (u Lavatera starší pokyn knihaři) mohou počítat jinak; takové strany dej do `VYNECHAT`.
  - odkazy na tabule s rytinami podle vlastního číslování knihy – vzor `nastroje/odkazy_rytiny.py`.

---

## 10. Kontrola, build, vydání

```bash
python -I nastroje/over_strany.py knihy/<kniha>
```

```bash
python -I nastroje/build.py
```

- `over_strany.py` musí skončit s 0 chybami; varování projdi (nepoměr délek DE/CS, nespárované bloky, zakázané termíny).
- Náhled: `docs/index.html` dvojklikem, nebo server `python -m http.server 8766 --directory docs`.
  Projdi rozcestník, obsah (úrovně nadpisů), několik stran v zrcadlovém zobrazení, rejstřík, hledání, PDF a odkazy na sken.
- **Verzi webu** v `projekt.yaml` zvyšuje autor projektu – nová kniha = první číslo (MAJOR), viz README › Verzování.
- Do README (sekce Knihy / Zdroje) doplň knihu a zdroj originálu, do paměti projektu rozhodnutí o terminologii.
- `docs/` je generovaný – needitovat ručně (případné ruční úpravy přenést do šablon v `nastroje/web/`).

**Ruční ověření** probíhá průběžně po vydání: kdo stranu přečte a schválí, spustí
`python -I nastroje/overeno_clovekem.py knihy/<kniha> 001-010 --kdo "jméno"`.

---

## Kontrolní seznam

- [ ] sken je úplný (návaznost textu, kustody, signatury), vady skenu (chybějící / zdvojené listy) popsané
      v `strany_poznamka`, licence zapsaná
- [ ] český název knihy navržený a uvedený v závěrečné zprávě (autor projektu ho může změnit v `kniha.yaml`)
- [ ] `knihy/<id>/kniha.yaml` – metadata, `strankovani`, adresy skenu, `poznamky_k_prekladu`
- [ ] text originálu po snímcích v `zdroje/` (OCR nebo DTA) a převod strana → snímek ověřený na několika místech
- [ ] import pracovního překladu, `import_report.txt` prošlý, chybějící strany založené – nebo bez pracovního
      překladu všechny strany založené `zaloz_strany.py` (převod ověřený `--zkouska`)
- [ ] glosář (kopie + specifické termíny, `nepouzivat`, `bez_odkazu`)
- [ ] obrázky: dřevořezy vyříznuté a zkontrolované, tabule jako `tab-NN` s popisem
- [ ] `zdroje/ZADANI_AGENTUM.md` a `ZADANI_REVIZE.md`, dávky přeloženy a zkontrolovány, zprávy v `zdroje/kontrola/`
- [ ] terminologie sjednocená, hranice dávek vyřešené, `SPORNA_MISTA.md` sepsané
- [ ] nepropojené termíny doplněné do glosáře, odkazy na strany a tabule označené
- [ ] `over_strany.py` bez chyb, `build.py` proběhl, web prošlý v prohlížeči
- [ ] README doplněné; verzi v `projekt.yaml` (MAJOR) zvýší autor projektu
