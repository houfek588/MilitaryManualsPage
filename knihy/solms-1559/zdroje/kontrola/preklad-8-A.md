# Překlad – dávka 8-A (Osmá kniha, skeny 585–599)

Strany: `8-erb-solms`, `8-titul`, `8-001r` – `8-006r` (13 stran; skeny 586 a 588 jsou prázdné rubové strany a v edici nejsou).
Soused před dávkou `7-018r` (sken 583) ani za dávkou `8-006v` (sken 600) zatím nemá text, takže jsem jen ověřil, že
dávka na obou koncích začíná a končí celým odstavcem. Výjimkou je přelom 8-006r → 8-006v, kde podle skenu 600
začíná nový odstavec *Item auff 500 personen … ein woch*.
Všechny strany mají `stav: prelozeno` a `overeno_clovekem: false`. `over_strany.py --prisne` hlásí 0 chyb a 1 varování (planý poplach, viz níže).

## Přehled stran
| Strana | Sken | Obsah | Bloky |
|---|---|---|---|
| 8-erb-solms | 585 | erbovní frontispis, nápis *Reinhart der Elter…* | odstavec + obrázek (popis) |
| 8-titul | 587 | titulní list *Das acht Bůch. Ein kurtzer Bericht…*, znak Karla V., tiráž *Getruckt im Jar M. D. LX.* | nadpis 1 + odstavec + obrázek + tiráž |
| 8-001r | 589 | nadpis knihy (úr. 2), úvod s iniciálou **W**, tři hlavní body (posádka, proviant, děla) | 7 bloků, poslední přechází (*ge-/macht*) |
| 8-001v | 590 | rozpis obranných míst a zdvojení posádky; stráže; malé pevnosti, zátarasy a průsmyky | 5 bloků, `pokracovani` |
| 8-002r | 591 | velké pevnosti a výpady; posádka ze dvou a více národů | 4 bloky, poslední přechází (*vr-/sachen*) |
| 8-002v | 592 | proč ne zemský lid; plukovník a rovný řád mezi národy; stráže; úvod k proviantu | 4 bloky, `pokracovani` |
| 8-003r | 593 | mouka, slanina, nakládání a uchování solného masa (lák) | 3 bloky |
| 8-003v | 594 | nadpis (úr. 3) *Volgen die Stück so zur Prouiant gehören*; soupis zásob jako `seznam` (28 položek); trvanlivost potravin | 8 bloků |
| 8-004r | 595 | nadpis (úr. 3) *Commis Ordnung*; proviantní pán; achtel a chléb; **tabulka chleba a obilí** (11 řádků, 4 sloupce) | 5 bloků |
| 8-004v | 596 | konec tabulky (`pokracovani`); zkrácení chleba trojčlenkou (58 : 77 achtelům); rozdílné míry | 7 bloků |
| 8-005r | 597 | přepočet místních měr (16 × 15 = 240 liber → 132½ chleba); prostranství pro výdej chleba | 4 bloky, `pokracovani` |
| 8-005v | 598 | proviantmistr na 500 mužů, výdej po kvartýrech, potvrzenky, služebníci proviantního pána | 6 bloků |
| 8-006r | 599 | maso: odhadní váhy dobytka a rozpisy na 100/500 osob – **3 tabulky** | 8 bloků |

## Ověřená čtení ze skenu (BSB IIIF, výřezy v plném rozlišení)
- 8-001r: ozdobná iniciála je fraktura **W** → *WEil ich eine Kriegßordnung…* (OCR: *Eil ich*).
- 8-001r: čtu *gnůgsam, gůtem, stůck, seien, wirt*. OCR má *gnügsam, seten, wirk*.
- 8-004r: čísla jsem kontroloval na zvětšeném výřezu. Čtu *20½. lib.* (OCR *201.lib*) a sloupce *2500 Brot*, *1066 achtel* přesně podle tisku (viz tiskové chyby).
- 8-004v/8-005r: slovo *dassel-|big* je rozdělené přes stránku (pod sazbou 596 stojí jen kustoda *big*), proto je celé *dasselbig* na 8-005r.
- 8-005r: čtu *15. pfundt* (OCR *5.pfundt*) a *132½. Brot* (OCR *132.*). V tisku je zřetelně *in. 84.*
- 8-006r: odhadní váhy jsou *3. Centner / 1½. Centner / 36 / 30 / 20 Pfundt*. Všechny rozpisy dobytka jsem přepočítal a souhlasí.
- Signatury (*A ij*, *A iij*, *A iiij*, *B*), čísla listů (i–vi), záhlaví *Das acht Buch/* a *Von Besatzung einer Stat.* a kustody jsem vynechal.

## Tiskové chyby (v `de` ponechané, vysvětlené poznámkou)
- 8-004r: *Ein woche … 500 personen 2500 Brot*. Správně má být 3500, jak odpovídá 70 centům i 38 achtelům a 7 měřicím.
- 8-004r: *150000 Brot … 1066 achtel vnd 5 metzen*. Správně má být 1666 achtelů a 5 měřic.
- 8-004v: *77 achtel vnd drei metzen*. V tabulce na předchozí straně stojí 6 měřic, a to je výpočtem správně.
- 8-003r: *Feysch* (2×) místo *Fleysch*. *witter* je patrně *wider*.
- 8-005r: *vberschlagdn*, *angrzeigt*. 8-005v: *bekmopt* (= *bekompt*).

## Sporná místa k rozhodnutí
1. **8-001v** *so soll mann dasselbig dupliern auff 2000. oder noch mehr oder auff 100. gerechnet* → „…zdvojnásobit na 2000 nebo ještě víc, anebo počítat [dalších] 100 na [každou] stovku“. Smysl dovětku je nejistý, vysvětluje ho poznámka.
2. **8-005r** *auch in 24. oder 36. vnd in. 84.* Podle řady by se čekalo 48. Ponechal jsem 84 a doplnil poznámku.
3. **8-005v** *dem obersten Prouiantherrn leichtlicher mit zwei hunderten vmbzugehn* → „snazší jednat s dvěma sty“. Může jít o chybu za *fünff hunderten*, viz poznámka.
4. **8-003v** *Holtz zum bawen vnnd Darressen* → „dříví na stavby a na sušárny“. *Darressen* čtu jako *Darr-Esse* (sušárna), poznámka.
5. **8-005v** *Quartier* zde znamená část posádky přidělenou kvartýrmistrovi. Přeložil jsem „kvartýr {Quartier}“ podle glosáře a smysl vysvětlil poznámkou.
6. **8-001v / 8-002r** *Wehr(en)* = „obranné místo / obranná místa“. *Ständt / stende* = „postavení“: slovo „stanoviště“ jsem nepoužil, protože glosář ho vyhrazuje pro *Letze*.
7. **8-005v** *gantzen hauffen* = „celé houfy“, nikoli „šik“ podle hesla `sik`. Jde o neuspořádanou masu lidí, ne o bitevní šik.
8. **8-001v** *Rüstung* = „výzbroj“ (zbrojní a obranné vybavení obranného místa), nikoli „zbroj“ podle hesla `zbroj`.

## Varování validátoru
- `8-003r blok 2: v de možná chyba OCR (foll/ift/fein)`: planý poplach. Jde o *fein reyn in daß Saltz legen* („pěkně čisté“) a sken *fein* potvrzuje.

## Návrhy hesel do glosáře
| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| obranne-misto | obranné místo | Wehr, Wehren, wehrn | opevneni | obsazované obranné místo či úsek pevnosti (věž, bašta, úsek hradby), na které se rozpisuje posádka a děla |
| komisni-rad | komisní řád | Commis Ordnung | zold | lze přidat k heslu `komis` (de už obsahuje *Commis Ordnung*); v 8. knize jde o řád vydávání chleba a masa posádce |
| zataras | zátaras (klauza) | Klausen, Klause | opevneni | malá pevnůstka uzavírající horské údolí či cestu |
| vypad | výpad | außfal, außfelle | opevneni | výpad obležené posádky |
| lak | lák | Lack, Soltz | zold | solný nálev na nakládané maso |
| skopec | skopec | Hamel, Hämel | miry | vykastrovaný beran; v rozpisech masa 30 liber |
| handschrifft | vlastnoruční potvrzení | Handschrifft | zold | stvrzenka proviantmistra o převzetí chleba |
| ochrana | ostraha | hůt | sluzba | bdělá ostraha (vedle *Wacht*, stráže) |
