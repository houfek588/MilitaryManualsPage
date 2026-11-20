# 2. revize – Šestá kniha, dávka C (6-018v … 6-027r, skeny 528–545)

Podklad: `zdroje/ZADANI_REVIZE2.md` (včetně rozhodnutí pro knihy 6–9) a zpráva překladatele `preklad-6-C.md`.
Všech 18 stran má nyní `stav: zkontrolovano`, `overeno_clovekem: false`. Sousední strany 6-018r a 7-erb-solms jsem jen četl.
Přechody mezi stranami sedí: 6-018r končí celou větou (čl. 25), takže 6-018v nemá `pokracovani`. Tabulky přecházející přes hranici stran (6-024r→6-024v, 6-024v→6-025r, 6-026v→6-027r) mají `pokracovani: true`.
Kontrola: `python -I nastroje/over_strany.py knihy/solms-1559 6-018v … 6-027r --prisne` skončila výsledkem **0 chyb, 0 varování**.

## Postup
- Všech 18 skenů (BSB IIIF, šířka 1400 px) jsem prošel řádek po řádku proti `de`. Sporné zlomky jsem kontroloval na výřezech v plném rozlišení.
- **Všechny součty v obou rejstřících jsem přepočítal**: koně, kyrysníky, trénní koně, vozy a přespočetné koně po skupinách i za oddíly. U příjezdného jsem přepočítal každou položku (koně × dny × 6 bac., vozy × noci × 12 bac.), úhrny skupin a stran i celkový součet.
- Přepis `de` odpovídá tisku. Žádnou chybu OCR v textu jsem nenašel, opravoval jsem jen formát (viz níže).

## Hlavní změny po stranách
**Ve všech 18 stranách**: virgule v `de` sjednocena na konvenci edice `slovo/ další` (překladatel psal `slovo / další`, předchozí dávky 6-A, 6-B a celá kniha 7 mají `/ `).

- **6-018v** (čl. 26–30)
  - čl. 28: „zatížit výkupným {schetzen}“ → „uložit jim výkupné {schetzen}“.
  - čl. 29: druhá věta přestavěna. Před: „Tato dobytá a k holdu přivedená místa i města … přijatí na milost, kolik jich dobyli, nemají být…“ → po: „Dobytá místa, která složila hold, ani města, zámky, městečka, vesnice a lidé přijatí na milost, kolik jich dobudou, nemají být po přijetí na milost dále poškozováni…“.
  - čl. 30: *zu vnd von den feinden* = „při tažení proti nepříteli i při ústupu od něj“ (dříve „proti nepříteli i při odchodu od něj“).
- **6-019r**
  - čl. 31: slovosled. Původně vložená vedlejší věta „aby se tomu předešlo“ uprostřed souvětí → „nemá – aby se tomu předešlo – žádný národ…“.
  - čl. 31: tautologie „odcizit jeho ukořistěnou kořist {beut}“ → „odcizit kořist {beut}, kterou získal, nebo jeho zajatce“.
  - čl. 33: „chceme tomu předejít, dbát na to a nařídit“ → „chceme tomu předejít, a proto se o to přičiníme a nařídíme“.
  - čl. 35: „nejpozději nejbližšího příštího dvacátého pátého května“.
  - čl. 37: „Císařské Veličenstvo {Kei. Mat.}“ → „Jeho císařské Veličenstvo“.
- **6-019v**
  - Nadpis přehlídkového rejstříku *Muster Register … Albrecht* změněn z `uroven: 2` na `uroven: 3`. Odpovídá to saskému rejstříku na 6-007r (úroveň 3 pod 6-003v, úroveň 2) a toto oddělení je pod nadpisem *Brandenburg. Wir Karl* na 6-017r (úroveň 2).
  - Z pozn. 2 jsem vypustil výklad *Drosser*: opakoval glosář (`trenni-kun`). Zůstal jen odkaz na žold na 6-022r.
- **6-020r, 6-020v**: beze změn textu, všechny součty sedí.
- **6-021r**
  - **Dva nepřeložené řádky** v `cs`: „wagen / a 10 vberleng“ → „vozy a 10 přespočetných koní“, „wagen a 6 vberleng“ → „vozy a 6 přespočetných koní“.
  - Mluvnice: „vozy a 4 přespočetných koní“ → „vozy a 4 přespočetní koně“ (2×) a „2 přespočetných koní“ → „2 přespočetní koně“.
  - V pozn. 1 „trénového koně“ → „trénního koně“ (glosář).
- **6-021v**
  - Opravena mluvnice („2 přespočetní koně“, 2×).
  - **Nová pozn. 2**: skupina Bruch, Gaburt a Stackel má v úhrnu 8 přespočetných koní, položky na 6-021r dávají jen 6. Úhrn oddílu (68) s osmi počítá.
  - Další poznámky jsou přečíslované.
- **6-022r**
  - *Huffschmit* „kovář“ → „**podkovář**“ (glosář `podkovar`).
  - *Fendrichen* „praporečníci“ → „**korouhevníci**“ (rozhodnutí pro knihy 6–9: *Fendrich* u jízdy = korouhevník).
  - Úvodní odstavec vyúčtování přestavěn. Před: „Takto vychází vyúčtování příjezdného a přehlídky i toho, co … obdržel …, jak ukazují úhrny rejstříků i [záznam] přijatých peněz:“ → po: „Po porovnání příjezdného {anrit gelts} a přehlídky {Musterung} i toho, co … obdržel na příjezd {anzug} svůj a svých jezdců, vychází podle úhrnů rejstříků i [záznamu] přijatých peněz toto:“.
  - „Příjezdné pak dělá“ → „činí“.
  - „srazil, a … zůstává nad [příjezdné] ještě přeplaceno“ → „odečetl; nad [příjezdné] tak Jeho knížecí Milosti ještě zůstává přeplatek“.
  - Pozn. 1 zkrácena o výklad *Summa lateris* (je v glosáři `soucet-strany`).
- **6-022v**: beze změn textu (sken, iniciála **ERstlich** a *Sall* ověřeny).
- **6-023r, 6-023v**
  - „a koně na den po 6 bacenech“ → „a za koně na den po 6 bacenech“.
  - 6-023v: nová pozn. 1 *gudlen* (tisková chyba, stejně jako na 6-023r).
  - Do poznámek o chybných úhrnech stran doplněno, že celkový součet počítá se správnou částkou.
- **6-024r**: pozn. 1 „počítá s 12 bacenech“ → „počítá s 6 zl. 12 bac.“.
- **6-024v**: beze změn textu.
- **6-025r**: do pozn. 1 doplněno, že i sama položka za vůz Bernigßhausena (17 zl.) je vyšší než 17 nocí × 12 bac. (13 zl. 9 bac.).
- **6-025v**
  - **Oprava struktury tabulky**: řádek „Lorentz Schungel.“ měl ve druhém sloupci `de` i `cs` duplicitní text „Lorentz Schungel[^1]“, v `de` dokonce se značkou poznámky. Druhý sloupec je teď prázdný a značka je v `cs` u jména.
  - Pozn. 3 doplněna o úhrn strany (viz ověřená místa).
- **6-026r**: pozn. 2 přepsána podle přepočtu (viz níže). Chyba není jen v úhrnu skupiny, ale už v podílu na voze.
- **6-026v**: beze změn textu.
- **6-027r**
  - „Trénoví koně {Drosser}“ → „Trénní koně“.
  - „Celkový úhrn“ → „Celkový součet {Summa summarum}“ (glosář `summa-summarum`).
  - Pozn. 2 doplněna o zjištění ke kontrole celkového součtu.

## Ověřená místa ze skenů a přepočtů
- **528–529**
  - Čtení *Verung*, *Ritmei-|sterl* i *neuntzig* (tisk; správně 96) potvrzuji.
  - Tužkový přípisek „(Sechs)“ a signaturu *D ij* překladatel správně vynechal.
- **530**
  - Vůz Leuchtenberga je na výřezu v plném rozlišení ½ (rozmazaný zlomek, ne 1½). Úhrn skupiny je v tisku zřetelně 3½, takže součet 2½ ≠ 3½ je chyba tisku, jak uvádí pozn. 3.
  - Ostatní úhrny na 530–534 sedí (116/10/10/11, 24/1/½/2, 37/0/3/4½, 34/0/2/2½, 27/0/2/2, 21/0/1/1½). Úhrny 305/15/22½/27, 88/6/5/7½, 108/0/6½/9/14 a 147/0/11½/9½/68 sedí s tištěnými dílčími úhrny.
- **533**
  - U Wentzela von Grun a Reinharta Gaburta tisk počet vozů opravdu neuvádí (prázdné místo).
  - Ověřeny drosser ½ ve skupině Meiburg (správně 1½) a vozy 1 ve skupině Heinricha Meiburga (správně 1½). Úhrn oddílu 108 počítá u vozů s tištěnou 1.
- **534**: *Jobst Scha?t* je opravdu poškozené. Výpočet stavu sedí (648 zl., 6½ × 8 = 52 zl., 13 × 25 = 325 zl.).
- **535**
  - Stav: 2063 zl. ✓.
  - Měsíční žold: 7776 + 252 + 273 + 1272 + 72 + 82 = 9727 ✓.
  - Úhrny 21 kyrysníků, 45½ trénních koní a 53 vozů souhlasí se součtem čtyř oddílů.
- **536–545 (příjezdné)**: všechny položky jsem přepočítal.
  - Potvrzuji tiskové chyby, které uvedl překladatel.
  - Nově zjištěno na **6-026r**: podíl Ruckßlebena na voze má být 14 × 8 = 112 bac. = **7 zl. 7 bac.** (tisk 7 zl. 12 bac.) a úhrn skupiny tedy 52 zl. 4 bac. S tím **přesně** souhlasí tištěný úhrn strany 389 zl. 7 bac. Dříve poznámka uváděla jen „zhruba“.
  - Nově zjištěno na **6-027r**: u Meischnerova podílu na voze vychází 11 × 20 = 220 bac. = 14 zl. 10 bac., tisk má 15 zl. 6 bac. (= 21 nocí). Úhrn skupiny s tištěnou částkou počítá. Do poznámek jsem to nedával, je to drobnost.
  - **Celkový součet 5166 zl. 11 bac.**: součet osmnácti tištěných úhrnů stran dává 5186 zl. 1 bac. Částka 5166 zl. 11 bac. vyjde přesně, jen když se použijí opravené úhrny 319 zl. 3 bac. (6-023r), 217 zl. 9 bac. (6-023v) a **166 zl. 9 bac. (6-025v)** místo tištěného 165 zl. 14 bac. Chyby tedy vznikly až při sazbě, původní účet byl správný. Na 6-025v proto platí opravený úhrn Gotharta Pfeiffa 55 zl. 8 bac. Doplněno do poznámek 6-023r, 6-023v, 6-025v a 6-027r.
  - Koně: součet úhrnů stran dává 652 (jak uvádí tisk) s opraveným počtem 37 na 6-025r a s tištěnými 39 (6-026v) a 20 (6-025v).

## Sporná místa k rozhodnutí
1. **vberleng** – DE *wagen vnd 6 vberleng*, *57 wagenpferd vberleng*; CS „přespočetní koně“ (pracovní překlad ponechán).
   - Z 6-027r plyne, že jde o tažné koně k vozům: *57 wagenpferd vberleng*, 46 z nich „činí 2 vozy“.
   - Zvážit, zda by nebylo výstižnější „přespřežní koně“ nebo „vozní koně navíc“. Do rozhodnutí ponechávám „přespočetní“.
2. **Einrosser** (6-019v, 6-022v) – CS „jezdci o jednom koni“ vedle *Einspennigen* „jednokoní jezdci“. Glosář řadí *Einrosser* pod `jednokony-jezdec`, tisk však obě skupiny uvádí vedle sebe, proto rozlišení ponechávám. Doporučuji samostatné heslo.
3. **Úroveň nadpisu 6-019v** (změněna na 3) a **6-022v** (ponechána 3) – saský díl má *Register des Anreitens* na 6-010v na úrovni 2. Pro jednotnost knihy 6 by bylo dobré sjednotit oba díly (saský i braniborský): rejstříky na úroveň 3 pod nadpisem knížete (úroveň 2).
4. **6-022r** *bleiben jren f. g. noch hierüber außstehen 1333 zl. 4 bac.* – CS „nad [příjezdné] tak Jeho knížecí Milosti ještě zůstává přeplatek“. Výklad překladatele (přeplatek zálohy, který se odečítá od 11790 zl.) potvrzuje aritmetika: 11790 − 1333 zl. 4 bac. = 10456 zl. 11 bac.
5. **Summa per se** (6-023v) – CS „úhrn: tatáž částka“. Je to srozumitelné, ponecháno.
6. **6-019r čl. 37** *zu allen gemelten* (neúplná věta tisku) – CS „nad všechny uvedené [částky]“. Ponecháno s poznámkou.

## Návrhy do glosáře
Návrhy překladatele (`preklad-6-C.md`) podporuji s těmito úpravami:

| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| prespocetny-kun | přespočetný kůň | vberleng, Überläng | zold | Tažný (vozní) kůň nad stanovený počet; v braniborském rejstříku 1544 se 46 takových koní přepočítává na 2 vozy (*57 wagenpferd vberleng*). |
| jezdec-o-jednom-koni | jezdec o jednom koni | Einrosser | jednotky | Jezdec sloužící s jediným koněm, v rejstříku uváděný vedle *Einspennige*. Z hesla `jednokony-jezdec` by se pak *Einrosser* vyřadil. |
| odjezdne | odjezdné | abrit gelt, abrit | zold | Peníze na cestu jezdců z místa propuštění domů; protějšek příjezdného. |
| podil-na-voze | podíl na voze | anzal des wagens, anzall des wagens | zold | Podíl jezdce na nákladech společného vozu (bacenů na noc). |
| kara | kára | Karn | zold | Lehký vůz (kára), v rejstříku příjezdného místo vozu. |
| hejtman-strelcu | hejtman střelců | Schützen Hauptman | velitele | Velitel jízdních střelců v oddíle markraběte (50 zl. za úřad). |
| tabule | tabule | Taffel, Tafel | zold | Peníze na stůl (vydržování dvora) velitele, zde 300 zl. měsíčně. |
| prijezd | příjezd | anzug, anzog | sluzba | Příjezd oddílu na přehlídkové místo (vyúčtování příjezdného). |

- **Do stávajících hesel doplnit tvary `de`**:
  - `prijezdne`: *Anritgelt*, *anrit gelts*, *Anrit gelt* (část už je v glosáři).
  - `podkovar`: *Huffschmidten*.
  - `soucet-strany`: *Summa latris*.
  - `summa-summarum`: *Summa summarum des gelts*, *Summarum*.
- Heslo `trenni-kun` (*Drosser*) v glosáři už je a překlad ho používá. Návrh překladatele `trenovy-kun` je tím vyřízen.
- *Fendrich* u jízdy = „korouhevník“ podle rozhodnutí 2026-11-17. Glosář `prapornik` zatím uvádí jen „praporečník“, doporučuji doplnit do `pozn` výjimku pro jízdu nebo zřídit heslo `korouhevnik`.
