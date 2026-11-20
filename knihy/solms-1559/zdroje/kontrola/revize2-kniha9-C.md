# 2. revize – dávka 9-C (Solms 1559, Devátá kniha, skeny 660–681)

Strany: 9-020v … 9-030v a 9-erb-konec (22 stran). Soused 9-020r jen čten (návaznost: 9-020r končí větou, 9-020v začíná novým odstavcem).
Všechny strany porovnány se skeny BSB (bsb00085168, 1400 px, místo 668 navíc výřez) a se zprávou překladatele `preklad-9-C.md`.
Stav všech 22 stran: `zkontrolovano`, `overeno_clovekem: false`. `over_strany.py --prisne`: 22 stran, 0 chyb, 0 varování.

## Ověření `de` proti skenům
- Přepis `de` je u všech stran věrný; zkratky rozepsány správně, záhlaví, signatury (D iiij, E, E ij, E iij, E iiij) a kustody vynechány.
- Hranice stran a kustody sedí: 020v/021r (*seind*), 021r/021v (*reden*), 021v/022r (*ziehen*), 022r/022v (*Wann* – nový odstavec), 022v/023r (*wacht*),
  023r/023v (*vnd*), 023v/024r (*Wann* – nový odstavec), 024r/024v, 025r/025v, 025v/026r (*Geschütz*), 026r/026v, 026v/027r (*Feind*),
  027r/027v (*wenig-|sten* – slovo správně celé na 9-027v), 027v/028r (*sei-|nem* – celé na 9-028r), 028r/028v (*Aber* – nový odstavec),
  028v/029r (*möchten*), 029r/029v (*Item* – nový odstavec), 029v/030r (*das*), 030r/030v (*Weitter* – nový odstavec). `pokracovani` všude správně.
- 024v/025r: kustos tisku *spüren*, ale 9-025r začíná *einen weiten weg* – chyba tisku (snad vypadlý řádek), ověřeno ve skenu; překlad přes hranici čte souvisle.
- **Oprava `de`** 9-024v: *mit einem Kenchtzehen* → *mit einem Kencht zehen* (ve skenu dvě slova; přesmyčka *Kencht* = *Knecht*); poznámka 3 upravena.
- Potvrzena tisková čtení (ponechána s poznámkou): *volbnbringen*, *belergert* (021r), *Fleiß*, *reden welt* (021v), *tag vnd anch*, *verretei*, *las-|lasen* (022v),
  *weitzeichen*, *ferrer* (023r), *bei manchen*, *garben*, *scheim* (024r), *nachulogents*, *solllen*, *einigßweiß* (024v), *gering hortig* (025v), *vnud* (026v),
  *reicher*, *jelicher*, *wie derhalben* (029r), *hindersehen* / *hindersen* (030r), *Kriegßornung*, *Priuilega*, *vneingkeiten* (030v), *Mintzenberg* (erb).
- **Foliace tisku** (doplněk ke zprávě překladatele): listy 22–30 nesou čísla 22, **24** (list 23), 24, 25, 26, 27, 28, 29, **25** (list 30). Chybně tedy i list 23
  (9-023r má v tisku číslo 24), nejen list 30. Pole `list` ponecháno podle skutečného pořadí.

## Hlavní změny po stranách (před → po)
- **9-020v**: „pokládali za výhodu, když nepřítel, stojící směrem k údolí – byť jen nepatrně … –, musel útočit“ → „… když nepřítel musel útočit zdola, i kdyby stál jen nepatrně, třeba jen o stopu níže“;
  „Nechci se přít, že můj názor je nejlepší, jen vám ukazuji své dobré zdání“ → „Nechci tvrdit … jen vám sděluji, co sám pokládám za dobré“; „Víc vám nemohu říci o tom, co se týká bitevního šiku“ → „O bitevním šiku … vám víc říci nemohu“.
- **9-021r**: „Za prvé bude jeho největší starostí“ → „Na prvním místě …“ (kolize s následujícím „Za prvé:“); věta *als wenig jhr ehrlich leut habt* přestavěna („poctivé muže … rozdělte mezi svůj lid, ať jich máte sebeméně“);
  „zjevně truchlit“ → „okázale truchlit“ (*euch vbel vmb sie gehaben*); *auffhalten* „mařit“ → „zdržovat“.
- **9-021v**: „Dále je mé dobré zdání“ → „Dále mám za dobré“; slovosled věty o ženách a dětech.
- **9-022r**: „po začátku obléhání“ → „až bude město obleženo“; závěrečná věta o znalcích opevnění učesána.
- **9-022v**: *fünff oder sechs tag gnůg vnd mehr zu schaffen … mit dem Geschirr dann mit den Feinden* – „pět nebo šest dní i déle víc práce“ → „pět nebo šest dní víc než dost práce, a to spíš s náčiním než s nepřítelem“;
  *ye weniger yr herauß fallet im anzug der Feind* → „Čím méně budete vyrážet ven, když nepřítel přitahuje“.
- **9-023r**: věta o polním znamení zbavena hranaté vsuvky („ale ti před městem znamení města znát nemají“).
- **9-023v**: „bez obsáhlých nebo dobrých zpráv“ → „bez obsáhlých či spolehlivých zpráv“.
- **9-024r**: věta o zajatcích na glejt přestavěna („jsou-li někteří z vašich lidí v zajetí a chodí na glejt a na slib návratu ven a dovnitř, ať přicházejí k branám…“); podmět „na něj“ → „na nepřítele“.
- **9-024v**: *solt jr leut haben … denselbigen anzeigen wo sie hin wöllen* – „ukázat jim“ → „těm mají říci, kam chtějí jít“ (jde o průvodce); oprava `de` viz výše.
- **9-025r**: gramatická chyba „jemu by mohl hlídka na stromě oznámit“ → „aby mu hlídka na stromě mohla oznámit“; „nemají vyrazit příliš brzy, dokud…“ → „předčasně, nýbrž až nepřítel přejde kolem nich“.
- **9-025v**: „už se položil k obléhání“ → „rozložil se k obléhání“.
- **9-026r**: *als bald die Feinde jr leger geschlagen* – „rozbije ležení“ (dvojznačné) → „postaví své ležení“.
- **9-026v**: *daß yr daselbst hin ein Blochhauß machet* – „za ním“ → „na tom místě“ (tisk místo neurčuje); *dasselbig stürmen* – „bolverk dobýt útokem“ → „na srub zaútočit“; doplněno „ohňů {Fewer}“.
- **9-027r**: beze změny textu (ověřeno).
- **9-027v**: porušená závorka tisku (*… daselbst (ich wolt auch ein grössere Kammer … verhören) auff das köstlichest zurichten lassen*) – „skvostně vyzdobit“ se vztahuje k větší komoře, ne ke komoře na spaní: věta přeložena podle toho; „komorník {Kämmerling}“ → „{Oberster Kämmerling}“.
- **9-028r**: *alle ewer hilff* „posily“ → „síly“ (nejde o posily, ale o všechny vlastní lodě); drobná stylistika.
- **9-028v**: *vnd jr also groß Nachen hett* „máte jen velké lodě“ → „vy máte takové velké lodě“ („jen“ v tisku není); věta o lodích, které by najely na břeh, zpřesněna.
- **9-029r**: slovosled věty o dvou loďkách vzadu.
- **9-029v**: *keins bei grosser straff hinder euch faren lassen* – „a to žádnou jinak, pod velkým trestem“ → „pod velkým trestem nesmí žádná z nich plout jinak“; doplněn podmět „a vy dejte troubit“.
- **9-030r**: beze změny textu (ověřeno; poznámka o foliaci platí).
- **9-030v**: *soll ers wider geben* → „má to dát vrátit“.
- **9-erb-konec**: v popisu dřevořezu opraveno čtení nápisové pásky (tři úseky po dvou řádcích): „REINHA|RT. GRAFF. ZV|SOLMS – VND HER[R]|ZV MINCZEN|BORGK“, tj. *Reinhart Graff zu Solms und Herr zu Minczenborgk*. Heraldika (lev v 1. a 4. poli, dělený štít Münzenberg ve 2. a 3.) ve skenu potvrzena.

## Sporná místa k rozhodnutí
1. **9-021v** *anzeigen er hett die wort geredt* – CS „vypovídat o tom, jak ta slova pronesl“ + pozn. 2. Smysl nejistý (spíš „tvrdit, že ta slova [jen] řekl“ = zlehčovat); ponecháno.
2. **9-030v** *ewer Leuttenant soll auch … das Fewer … füren* – CS „jako váš poručík“. *Leuttenant* zde znamená „zástupce panovníka“; glosář `porucik` ponechán kvůli jednotnosti, zvážit poznámku.
3. **9-026v** *Blochhauß … daselbst hin* – srub „na tom místě“ (u rozstříleného bolverku). Věcně jde o vnitřní retranšement za bolverkem; překladatelův výklad „za ním“ je možný, ale v textu není.
4. **9-029r** *reicher* – poznámka navrhuje *rauher*; nelze vyloučit ani doslovné „bohatší“ (nepravděpodobné). Ponecháno.
5. **9-erb-konec / 9-erb-solms** – tisk na skenu 681 má *Mintzenberg*; sjednocení s 9-erb-solms (*Müntzenberg*) nechť ověří správce podle skenu 617 (strana mimo dávku).
6. **9-024v/9-025r** – nesoulad kustodu *spüren* s počátkem další strany: případně doplnit poznámku na 9-025r (nyní jen ve zprávách).

## Návrhy do glosáře
Hesla `admiral` a `galera` už v glosáři jsou; z návrhů překladatele (`preklad-9-C.md`) doporučuji přijmout:

| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| kapitan-lodi | kapitán | Patron, patron | velitele | Velitel a lodivod jednotlivé lodi (franc. *patron*). |
| velka-lod | velká loď | Nachen, groß Nachen | zbrane | Vysoká plachetní loď (franc. *nef*), ne člun. |
| lodstvo | loďstvo | Armada | jednotky | Celé válečné loďstvo, dělené na čtyři části pod plukovníky. |
| lodni-mistr | lodní mistr | Schiffmeister | velitele | Zkušený lodník přizývaný k válečné radě na moři. |
| prachar | prachař | Puluermacher | delostrelectvo | Výrobce střelného prachu a zápalných směsí. |
| pocta | pocta | Reuerentz | sluzba | Pozdrav lodí admirálovi večer a ráno (provolání, hudba). |
| komornik | nejvyšší komorník | Oberster Kämmerling | velitele | Dvorský úředník starající se o panovníkovy komory na lodi. |
| kotlar (rozšíření) / valecny-buben | válečný buben | Heerbaucke, Heer baucken, Heerbaucken | sluzba | Kotlový buben k signálům; nyní glosář zná jen *Heerbaucker* (kotlář). |
| srub (rozšíření) | srub | Plocheuser | opevneni | Tvar z 9-022r. |
| padaci-mriz (rozšíření) | padací mříž | schützgeter | opevneni | Tvar z 9-022v. |
| velitele (rozšíření) | velitelé | beuelchs leut, Beuelchs leut | velitele | Tvary z 9-029r. |
| zapalny-sip (rozšíření) | zápalný šíp | Fewerpfeiln | zbrane | Tvar z 9-027r. |
