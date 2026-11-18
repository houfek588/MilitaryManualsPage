# 2. revize – Druhá kniha, dávka A (erb-solms … 012v)

Rozsah: 26 stran (skeny 90–116): frontispis `erb-solms`, `titul`, `titul-v`, tabule `tab-01`, listy `001r`–`012v`
(úvod o povinnostech válečného pána, *Anbringen vnnd begern* a *Rathschlag* válečných radů k šesti článkům).
Sousedé jen čteni: `1-039v` (konec První knihy, bez návaznosti) a `013r` (pokračuje *Rathschlag*, šestý článek –
navazuje na konec 012v „…a ne o zlou lehkovážnost.“ / „Proto nechť Vaše římské císařské Veličenstvo…“).

Plynulost „středně“ podle `ZADANI_REVIZE2.md`: řetězená souvětí dělena na věty uvnitř bloků, struktura bloků,
`sken`, `id`, `stav: zkontrolovano` a `overeno_clovekem: false` beze změny; přechody `pokracovani: true`
(001v, 002r, 002v, 003r, 003v, 004r, 004v, 006v, 007r, 008v, 009r, 009v, 010r, 010v, 011r, 012r, 012v) dál sedí.

Kontrola: `python -I nastroje/over_strany.py knihy/solms-1559 erb-solms titul titul-v tab-01 001r … 012v --prisne`
→ **26 stran, 0 chyb, 0 varování**.

## Celoplošná sjednocení v dávce

- ***Maiestat*** (*E. Röm. Key. May.*, *jre Maiestat*) – v 006v–009r překládáno „Vaše římská císařská **Milost**“,
  ve zbytku knihy (25× i v 013r) „Vaše římské císařské **Veličenstvo**“. Sjednoceno na *Veličenstvo* včetně shody
  (vydalo, trvalo, ví…); v nepřímé řeči *jre Maiestat* = „Jeho Veličenstvo“.
- ***Kriegsuerstendigen / Kriegs verstendigen*** → „znalci válečnictví“ (heslo `znalec-valecnictvi`), dříve
  „váleční znalci“, „znalci války“ (titul, 002r, 004v).
- ***Policei*** → „veřejný pořádek {Policei}“ (002r, 011r; dříve „dobrá kázeň“, „pořádek“); ***Justicien*** →
  „spravedlnost {Justicien}“ (011r, heslo `justice`).
- ***Oberst / Obersten*** všude „plukovník“ (vč. 002r „pravým plukovníkem nade vším“, 010v „na rozkaz plukovníků“
  místo „velitelů“).
- Odstraněny zavádějící `{…}`: `{Regiment}` ve významu kázeň/správa (001v, 003v, 004r, 006v, 010r), `{hauffen}`
  ve významu dav/vojsko (001v, 002r, 007r), `{Artickel}` ve významu „článek, bod“ (006r, 006v, 008r, 009v, 010r,
  011v – heslo vede na *artikulní list*), `{gesellen}` = „dobrý druh“ (003r), duplicitní `{sold}`, `{massen}`,
  `{Kriegsuolck}`.
- Doplněny `{…}`: `{Kriegsordnung}` (004r), `{Kriegsordenung}` (006r), `{ämpter des Kriegs}` (004r),
  `{oberster Feldherr}` (002v), `{Schatzung}` (007r), `{Landtuolck}` = „zemský lid“ (007v), `{Passen}` (009r),
  `{Garköch}` (012r), `{Policei}`, `{Justicien}`, `{Kriegsuerstendigen}`.

## Opravy `de` podle skenů

| strana | bylo | tisk (sken) | pozn. |
|---|---|---|---|
| titul | Das ander Buch. | **Das ander Bůch.** | sken 91 |
| titul | Kriegsämpter noch nicht | **nach nicht** | nářeční *nach* = *noch* |
| 008v | ein einen hauffen | **einen einen hauffen** (*eiñ einen*) | pozn. 1 přepsána |
| 008v | geuierdte Ordnung | **Ordenung** | sken 108 |
| 012r | thun (3×), verhütet | **thůn, verhůtet** | sken 115 |
| 012r | bedunckt, Garkoch | **bedůnckt, Garköch** | |
| 012r | laß mann es dabei | **darbei** | |
| 012r | furten sich ab | **fürten** | |

Ověřeno beze změny: *Beimwelburg*, *Castel Alter*, *Kriegsuerstendigen* (sken 91); *Musterherr*, *Landsknecht*,
*Fendlin*, *Rotgesellen* (sken 108); *Barschen*, *Gestrengen vnd Ehrnuesten*, *Junckfrawen* (sken 115).
V OCR potvrzeny tiskové odchylky *notröstung* (001r), *verwaltnug*, *Kriegsorgnung*, *Poruiant* (004r),
*wers geübt* (001v). Mezery kolem virgul (` / `) na 012r–012v ponechány – stejně jsou psány i navazující
strany (013r ad.).

## Hlavní změny překladu po stranách

- **erb-solms** – pozn. 1 „polní maršál“ → „polní maršálek“.
- **titul** – „jinými válečnými znalci“ → „jinými znalci válečnictví {Kriegsuerstendigen}“.
- **titul-v** – popis dřevořezu zpřesněn podle obrázku: jezdec drží velitelskou hůl, kůň má plátový chránič hlavy
  s mřížkami na očích, šupinový nákrčník a kropír s rozetou (dřív „vrchní velitel“, bez hole).
- **tab-01** – popis přepsán: dříve „šest mužů“ a „úhelník“; na rytině je osm mužů (válečný pán ve vysokém
  klobouku s řetězem, šest radů, písař u šikmého pultu na okované truhle), dvě města za řekou.
- **001r** – dlouhý odstavec rozdělen na věty; *vnd besehe daß er des gewiß sei* „hledí si být jist, že ji má“ →
  „postará se, aby ji měl jistou“; *auß viller erfaren vrsachen* „zakoušených příčin“ → „příčin poznaných
  zkušeností“; *wieuil einer jeden rüstung* → „kolik z ní v jaké zbroji“.
- **001v** – *wers geübt vnd erfarn, hielt sich dann auch desto baß* chybně „kdo je vycvičený…“ → podmínka
  „kdyby to měl vycvičené a zakusil to, držel by se o to lépe“; *vnd eine schlechte besoldung hat* → „za nízký
  žold“; námitka v přímé řeči.
- **002r** – *dem ist wol zuthůn* → „dá se tomu snadno odpomoci“; *tragent einem Herrn vil auff* → „pána stojí mnoho
  peněz“; *ordenung machen zu ziehen* → „uspořádat pochodový šik“.
- **002v** – „páni Jörg z Frundsbergu, pan Marx“ → „pan Jörg…, pan Marx“; *hohen hauptern die gefangen werden*
  „zajatých vysokých velitelů“ → „zajatých vznešených osob“; *verringerung* → „snižovalo by to pánovu vážnost“;
  *Es were dann sach* → „Leda by snad…“.
- **003r** – rozdělen celý odstavec (13 vět); *kan nit felhen auß gůtem gemůt můß er sich entsetzen* „ztratí rozvahu“
  → „i při vší dobré vůli se musí zděsit“.
- **003v** – *souil Schlachten durch vortheil… gewunnen* „obratností“ → „s výhodou“; *freudigkeit* → „přílišná
  smělost“; *frei tröstlich* → „směle by povzbuzoval“; anakolutická perioda *Dieweil dann alles…* přeložena
  srozumitelně; *Regiment(en)* = „řízení / velitelství“.
- **004r** – *sie seien des widertheils Kriegsherrn oder seiner verwendten* chybně „protivníkovi, válečnému pánovi
  nebo spojencům“ → „nepřátelskému válečnému pánovi, nebo jeho spojencům“; *vmb volck oder gelt* „lid a peníze“ →
  „lid nebo peníze“; *Memorial* – věta o pamětní knize přeložena jasně.
- **004v** – rozdělení vět; *Kriegs verstendigen* → „znalci válečnictví“; *verächtlich* → „lehkovážně“.
- **006r** – nadpis „předává… k projednání obtížných článků“ → „předkládá… k poradě několik tíživých článků“;
  řeč válečného pána rozčleněna; *schatzung* „vydírání“ → „předražování“; „nevěře při přehlídce“ → „nepoctivosti“.
- **006v** – nadpis *Rathschlag…* → „Dobré zdání válečných radů k článkům předaným válečným pánem“; Veličenstvo.
- **007r** – *bei einem gantzen hauffen* → „u celého vojska“; *Schatzung der Prouiant* „odhad ceny“ → „ceny
  {Schatzung} proviantu“.
- **007v** – *sie haben jre maß auch im faß* → „mají i v sudu svou míru“; *das tregt inn an der maß* „což přibývá
  na míře“ → „což mu na mázu vynáší“; *Geleyt* „bezpečný průvod“ → „glejt {Geleyt}, tedy bezpečný průvod“ (heslo
  `glejt`); *Landtuolck* „venkovský lid“ → „zemský lid“ (heslo `zemsky-lid`).
- **008r** – výklad podvodu s „povolenými jmény“ zpřehledněn; *Ist aber der vor jhm durch vngerechtfertiget…*
  přeložen „Prošel-li však ten před ním bez prověření, jde i on za ním a [hejtman] opět mlčí“; *einem einen sold
  zwen… machen* → „jednomu knechtovi napsat dva, tři, čtyři nebo pět žoldů a dát mu z nich jeden“.
- **008v** – *ob der sold jm allein zustehe* → „zda mu žold náleží sama“; *eiñ einen hauffen mustern* → „aby jeden
  [muž] přehlížel celý houf“ (pozn. 1); konec odstavce *vnnd wann die Fendlin also alle geordenet seind…* navázán
  dvojtečkou na další blok („Tehdy má válečný pán…“), dřív byl přeložen jako výsledek.
- **009r** – zběh: *der ehrlichen mannlichen Knecht… müssig gehen* – podmět opraven (čestní knechti se mu mají
  vyhýbat); *preyß sein* „vydán na pospas“ → „vydán v plen“.
- **009v** – *so können sie ein ander handlung mit dem Kriegsherrn gehaben* „jednat jinak“ → „vést zvláštní
  jednání“; *der vnfletter vnd schreier auch der Hauptleut vrsach* → „za výtržníky a křiklouny mohou i hejtmani“.
- **010r** – *sie würden jn wider etwas sagen* → „knechti by zase něco řekli proti nim“; *nicht gůte anzeygung hat*
  → „nemá dobrý doklad, proč do ležení přichází“.
- **010v** – *keinen Schuß mit keiner Büchsen* – `{Büchsen}` (heslo *děla*) odstraněn, „z žádné palné zbraně“;
  *Rotterei* „spiklenectví“ → „srocování“; *Wir sehen auch inn vil weg für gůt an* → „Z mnoha důvodů…“.
- **011r** – *die ein Nation* upřesněno („ten národ, jehož řeči nerozumí“); *Policei vnnd Justicien*.
- **011v** – *nit bedacht werden möchten* „nepromyslely“ → „nepomyslely“; nová pozn. 1 k *durch dise vil personn*
  (stará pozn. 1 → 2); *vmbschlagen* → „verbování“; *dringt… von einander* → „rozdělí… daleko od sebe“.
- **012r** – „slečinky… jimž musí sloužit ostatní“ zpřehledněno; *Knecht… reytten* „jezdci“ → „knechti“;
  *Gestrengen vnd Ehrnuesten* „přísní a cti pevní“ → „stateční a slovutní“ (pozn. 2 přepsána podle české
  titulatury rytířů a vladyků); pozn. 1 (barda) zkrácena.
- **012v** – *ist nur des schuld* → „a je to jen naše vina“; rouhání „hrubé hříšné klení“ → „hrozné, zlé klení“,
  *verschweren* → „zaklínáme se“; poslední blok: rada „vyslechne-li… své rady“ → „ať v tom vyslechne i jejich
  rady“ (*jre Räth* = rady velitelů).

## Sporná místa k rozhodnutí

1. **008v, *mann soll nicht allzeit eiñ einen hauffen mustern lassen / es sei dann ein verwarte person*** – čteno
   „nemá se vždy dovolovat, aby jeden [muž] přehlížel celý houf, ledaže je to spolehlivá osoba“; alternativa
   (zdvojení sazečem) „nemá se vždy přehlížet hromadně v jednom houfu“. Pozn. 1 uvádí obě čtení.
2. **008r, *Ist aber der vor jhm durch vngerechtfertiget / sihet er auch hinnach / vnd schweiget auch still*** –
   podmět *er* nejasný (další podvodník × hejtman); přeloženo „jde i on za ním a [hejtman] opět mlčí“.
3. **011v, *so möcht durch dise vil personn… verhalten werden*** – doslova „skrze tyto mnohé osoby by mohly být
   zamlčeny“, což odporuje argumentaci; přeloženo „bez těchto mnoha osob by mohly být… zamlčeny“ s pozn. 1.
   Možná tisková chyba (*on* / *ohn dise vil personn*).
4. **012r, *die Gestrengen vnd Ehrnuesten*** – zvoleno „stateční a slovutní“ (česká dobová titulatura); možné
   i doslovnější „stateční a ctihodní“.
5. **007v, *Geleyt*** – podle glosáře „glejt“ s vysvětlivkou „bezpečný průvod“; v textu jde o ozbrojený doprovod
   dovozců proviantu, ne o listinu.
6. **003v / 004r, *Regiment, regierung*** – v obecných úvahách o vedení války přeloženo „řízení, správa,
   velitelství“ bez `{Regiment}`; v 002r–002v, 007v, 011r ponecháno „pluk {Regiment}“.

## Návrhy do glosáře

| id | cs | de | kategorie | pozn. |
|---|---|---|---|---|
| `majestat` (nové) | Veličenstvo (Vaše/Jeho římské císařské Veličenstvo) | Maiestat, Maiest., May., Mai., Mat. | osoby | sjednotit oslovení; v 2. knize se střídala „Milost“ a „Veličenstvo“. |
| `glejt` (pozn.) | – | Geleyt, Geleit | – | doplnit, že *Geleyt halten* = zajišťovat ozbrojený průvod (ne listinu). |
| `artikulni-list` (pozn./de) | – | Artickel | – | samostatné *Artickel* = „článek, bod“ (006r–011v), ne artikulní list; zvážit vyjmutí z `de`. |
| `dela` (pozn.) | – | Büchse, Büchsen | – | *Büchse* též obecně palná zbraň / puška (010v „keinen Schuß mit keiner Büchsen“). |
| `cena-proviantu` (nové) | stanovení ceny, cena | Schatzung (der Prouiant), schetzen | zold | *schetzen* = oceňovat zboží (profous, proviantní pán); *schatzung* též „předražování“. |
| `polni-kuchar` (de) | – | Garköch | – | doplnit tvar z 012r. |
| `znalec-valecnictvi` (de) | – | Kriegsuerstendigen (bez ß), Kriegs verstendigen | – | tvary z titulu a 004v. |
| `verejny-rad` (de) | – | Policei | – | tvar z 002r, 011r. |
| `stav-slechticky` (nové, volitelně) | stateční a slovutní | die Gestrengen vnd Ehrnuesten | osoby | titulatura nižší šlechty (012r). |
