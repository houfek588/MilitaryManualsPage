# Překlad – dávka 6-C (Solms 1559, Šestá kniha, skeny 528–545)

Strany: 6-018v … 6-027r (18 stran). Všechny `stav: prelozeno`, `overeno_clovekem: false`.
Kontrola: `python -I nastroje/over_strany.py knihy/solms-1559 6-018v … 6-027r --prisne` → 0 chyb, 0 varování.
Sousední strany 6-018r (končí článkem 25, celou větou) a 7-erb-solms (frontispis) jsem jen přečetl. Na 6-018v proto není `pokracovani`.

## Přehled stran
| Strana | Sken | Obsah | Bloky |
|---|---|---|---|
| 6-018v | 528 | Služební list Karla V. pro markraběte Albrechta, čl. 26–30 (odjezdné, škody na poddaných, zajatci, kořist, poslušnost) | 5× odstavec |
| 6-019r | 529 | čl. 31–37 (národy a víra, mince, přehlídkové místo u Špýru, datace 5. 4. 1544, tabule, drabanti) | 8× odstavec |
| 6-019v | 530 | Nadpis přehlídkového rejstříku (Landau, 5. 6. 1544, komisař Christoph von Schaumburg) a jezdci ze stáje markraběte | nadpis 2, odstavec, tabulka |
| 6-020r | 531 | pokračování rejstříku (Götz von Berlichingen aj.) a záhlaví celkového úhrnu | tabulka, odstavec |
| 6-020v–6-021v | 532–534 | úhrn 305 koní; oddíly Ph. von Cronberg (88), H. von Bernigßhausen (108), J. von Dalwig (147); nadpis 3 *Marggraff Albrechts Stat* | tabulky, nadpis 3 |
| 6-022r | 535 | stav (2063 zl.), měsíční žold (9727 zl.), vyúčtování příjezdného a záloh (zbývá 997 zl. 11 bac.) | tabulka, odstavec, tabulka |
| 6-022v–6-027r | 536–545 | druhý rejstřík: příjezdné (*Anrittgeld*) po osobách (6 bac. na koně a den, 12 bac. na vůz a noc); celkový úhrn 5166 zl. 11 bac.; *Ende der Register* | nadpis 3, tabulky, 2× odstavec |

Forma: rejstříky jsou tabulky. U prvního rejstříku mají dva sloupce (položka | počet). Dvousloupcová sazba tisku je přepsána souvisle: nejdřív levý, pak pravý sloupec. Úhrny označené v tisku svorkou jsou rozepsány do řádků „Summa …“ / „úhrnem …“. Druhý rejstřík má sloupce text | částka. V `cs` jsou částky zkrácené (zl., bac.) a jména osob zůstávají v podobě tisku, tituly jsou přeložené (hrabě, lankrabě, rýnský hrabě). Položky přecházející přes hranici stran (6-024r→6-024v, 6-024v→6-025r, 6-026v→6-027r) mají u tabulky `pokracovani: true`. Kustody, záhlaví, čísla listů, signatury (D ij, D iij, D iiij, E, E ij) a tužkový přípisek „(Sechs)“ na skenu 529 jsem vynechal.

## Ověřená čtení ze skenů (OCR → sken)
- 529: `Verung mundlicher abred` (tisk opravdu *Verung*, zřejmě za *Vermög*); `Ritmei-|sterl` → *Ritmeistern* (poškozené n); `neuntzig gulden` (tisk; správně 96).
- 530: `mit 91 pferden` (OCR 21); zlomky ½ u vozů ověřené zvětšením; u Leuchtenbergu vůz ½ (poškozená 1), úhrn skupiny 3½.
- 531: `vnd 4 vberleng`; 533: úhrn trénových koní skupiny Meiburg je v tisku ½; 534: `Jobst Scha?t` (poškozené písmeno; na 544 *Jobst Schat*), `Bernhart von Viermast`.
- 536: iniciála **ERstlich**; *Sall* (tisk, za *Stall*); 539: zlomek vozu u Haberkorna čten jako ⅔ (špatně čitelný).
- 540: `Laie von Brendel`, `den 2 Maij` (tisk); 541: `zu Reuern`, `12 flo 7 batz.`; 545: `macht zusamen 4 wagen 10 vberleng`.

## Tiskové a početní chyby originálu (ponechány v `de`, vysvětleny poznámkou)
6-019r 12 × 8 = 96 (tisk 90). 6-019v úhrn vozů 3½ (položky 2½). 6-021r drosser ½ (má být 1½), vozy 1 (1½). 6-022v vozy 12 (11), 66 zl. 5 bac., Albert Berlin 24 zl. (19 zl. 3 bac.). 6-023r 329 zl. 3 bac. (319). 6-023v 227 zl. 9 bac. (217). 6-024r 6 zl. 13 bac. (12). 6-024v „12 tag … 17 tag“, „2 Maij“. 6-025r 129 (119), koní 73 (37), 82 zl. 6 bac. (92). 6-025v 60 zl. 8 bac. (55 zl. 8 bac.). 6-026r 250 zl. 4 bac. (52 zl. 9 bac.). 6-026v 714 zl. (147), koní 39 (40). Celkové součty (305 / 648 koní, 9727 / 11790 / 5166 zl. 11 bac.) však sedí.

## Sporná místa k rozhodnutí
1. **vberleng** (6-020r až 6-027r) – DE *wagen vnd 6 vberleng*, *57 wagenpferd vberleng*; CS „přespočetní koně“. Význam není jistý: jde o koně nad stanovený počet, nejspíš tažné koně k vozům. Překlad je pracovní.
2. **Drosser** – CS „trénoví koně“. Glosář `trén` má *Trosser* = „trén“, což v počtech („trén 7“) nedává smysl. Navrhuji samostatné heslo.
3. **Fendrich** u jízdy (6-022r, *3 Fendrichen*) – podle glosáře „praporečník“. Vzhledem k rozhodnutí „Fendlin u jízdy = korouhev“ zvážit „korouhevník“.
4. **Summa per se** – CS „úhrn: tatáž částka“ (jediná položka skupiny je zároveň úhrnem).
5. 6-022r *bleiben jren f. g. noch hierüber außstehen 1333 zl. 4 bac.* – vykládám jako přeplatek zálohy na příjezdné (6500 − 5166 zl. 11 bac.), který komisař odečetl. CS „zůstává nad [příjezdné] ještě přeplaceno“.
6. 6-019r čl. 37 končí neúplně (*zu allen gemelten*) – CS „nad všechny uvedené [částky]“.

## Návrhy hesel do glosáře
| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| trenovy-kun | trénový kůň | Drosser, Trosser | jednotky | Kůň trénu s pacholkem v přehlídkovém rejstříku jízdy; žold 6 zl. měsíčně, do příjezdného se nepočítá. |
| prespocetny-kun | přespočetný kůň | vberleng, Überläng | zold | Koně nad stanovený počet, zřejmě tažní koně k vozům; 46 takových koní se přepočítává na 2 vozy. |
| jezdec-o-jednom-koni | jezdec o jednom koni | Einrosser | jednotky | Jezdec sloužící s jediným koněm (vedle *Einspennige*). |
| odjezdne | odjezdné | abrit gelt, abrit | zold | Peníze na cestu jezdců z místa propuštění domů; protějšek příjezdného. |
| uhrn-strany | úhrn strany | Summa lateris, Summa latris, Summa lat. | zold | Účetní mezisoučet stránky rejstříku. |
| podil-na-voze | podíl na voze | anzal des wagens | zold | Podíl jezdce na nákladech společného vozu (bacenů na noc). |
| kovar | kovář | Huffschmit, Huffschmidten | velitele | Podkovář jízdy, jeden na sto koní, s přeplatkem 12 zl. |
| hejtman-strelcu | hejtman střelců | Schützen Hauptman | velitele | Velitel jízdních střelců v oddíle markraběte (50 zl. za úřad). |
| tabule | tabule | Taffel, Tafel | zold | Peníze na stůl (vydržování dvora) velitele, zde 300 zl. měsíčně. |
| prijezd | příjezd | anzug, anzog | sluzba | Příjezd oddílu na přehlídkové místo (vyúčtování příjezdného). |

Do `de` existujícího hesla `prijezdne` doplnit tvary *Anritgelt, anrit gelts*.
