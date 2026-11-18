# 2. revize – Třetí kniha, dávka D (3-037v … 3-052v)

Rozsah: 31 stran (skeny 326–356): závěr ohňostrojů ke zteči (klády, dýmavý oheň, hliněné granáty, smolné věnce, zkušební
trubice), „lékárenské ohně“ podle Marka Řeka, zápalné šípy, nabíjení a střelba z děl, kartáč, ježek, „silná voda“,
noční střelba a ztužený prach. Sousedé `3-037r` a `3-053r` jen čteny (návaznost sedí: 3-037r končí uzavřenou větou,
3-053r začíná novým odstavcem). Plynulost „středně“ podle `ZADANI_REVIZE2.md`; struktura bloků, `sken`, `id`,
`overeno_clovekem: false` a všechny přechody `pokracovani: true` (3-038r, 3-039r, 3-042r, 3-042v verse, 3-043r,
3-046r, 3-048v, 3-049r, 3-050r) beze změny. Veršované poučky (3-042r, 3-042v, 3-051r, 3-052r) zůstaly jako `verse`
se stejným počtem řádků.

Kontrola: `python -I nastroje/over_strany.py knihy/solms-1559 3-037v … 3-052v --prisne` → **0 chyb, 2 varování**
(3-038v, 3-042v: autentické *fein* „pěkně, jemně“, falešně pozitivní – ověřeno už v 1. kontrole).

## Plošné změny v celé dávce
- **Feurpfeil / Feurpfeiln / haußpfeil → „zápalný šíp“** podle glosáře (`zapalny-sip`); dosud „ohnivý šíp“ (cca 30 výskytů).
  Pozor: navazující strany od 3-053r (mimo dávku) mají dál „ohnivé šípy“ – sjednotit v další dávce.
- **Büchsen Puluer / Büchsenpuluer → „střelný prach“** (glosář `prach`), dosud „puškový/dělový prach“ (3-042r, 3-045r,
  3-047v, 3-048r, 3-050v, 3-052v). Totéž platí pro 3-053r–3-054v mimo dávku.
- **Steinbüchsen → „kamenná děla“** (glosář `kamenne-delo`), ne „kamenometná“ (3-048r); *stein* u děla při prvním výskytu
  „dělový kámen {stein}“ (3-046v, 3-047r, 3-049r, 3-051v).
- Nadpisy 3-044r … 3-052v sjednoceny tečkou na konci (dosud bez ní, na ostatních stranách s ní).
- Doplněny `{Termín}`: {Bechring} 3-038r, {schrit} 3-047r a 3-050r, {Quadraten} 3-047r, {schifferling} 3-048v,
  {Richtscheidt} a {Zirckel} 3-049r.

## Hlavní změny po stranách (výběr, před → po)
- **3-037v**: dělení řetězených souvětí; „něco dokázat“ → „něco svést“ (*etwas aufrichten*); „třásně … až na ten prach“ →
  „třásně … nad prachem“ (*auff das Puluer*); „nadělá to takový prach a dým spolu s rozletem“ → „kromě rozletu a třesku
  nadělá mnoho prachu a dýmu“.
- **3-038r**: „dokud není hrdlo zcela plné“ → „dokud není trubička zcela plná“ (*biß die Rörn gar vol*); „do lázně {gedäfft}“ →
  „do zápalné lázně {gedäfft}“ (glosář `smoleni`).
- **3-038v**: dlouhé souvětí rozděleno (… pracích. Utlučená směs … totiž nemusí …).
- **3-039r**: „mají být … sepsány podle Marka Řeka, jejichž moc … shledal“ → „následují ohňostroje, které prý sepsal Marek
  Řek; jejich síla a účinek … byly, jak píše, shledány“ (*sollen … von Marco Greco geschriben sein*); „vše, co lze spálit“ →
  „vše, co lze zpustošit“ (*was da zuuerheern ist*).
- **3-039v**: „čím častěji se potře“ → „pokropí“ (*besprengt*).
- **3-040r**: vypuštěno přidané „prý“ (*Also hat Alexander … verbrennt*); „podle mínění Alexandrových spisů“ → „podle
  Alexandrova mínění“ (*nach meinung Alexandri*).
- **3-040v**: „Leží-li někdo před tebou“ → „Leží-li [vojsko] před tebou“; „vrhej z dobrého krytu“ → „vrhej obezřetně“
  (*wol verwart*).
- **3-041r**: oprava `de` *vorn* → **voln** (ověřeno ve skenu, = *völlig*), pozn. 2 přepsána.
- **3-041v**: „Vezmi dehet (*Albitram*), to jest benátský terpentýn“ → „Vezmi *Albitram*, to jest benátský terpentýn“
  (tisk sám ztotožňuje s *gloriat*); „co kolem ní jest“ → „co kolem ní je nebo může být“.
- **3-042r**: nadpis „oheň na osmý den“ → „oheň, jenž vzplane za osm dní“ (*vber acht tag*); verš „Vyčkej, co udeřila
  hodina“ → „Dej pozor, kolik hodina odbila“; „jak se dělá kartáči“ → „jako se nabíjí kartáč“.
- **3-042v**: „Jak položit oheň“ → „Jak založit oheň“ (*Feur zulegen*, 2×); „2 díly směsi (*Ircomedis*)“ → „2 díly
  *Ircomedis*“ (přidané slovo); nová pozn. 3 k *pleiß* (olovo?, ověřeno ve skenu).
- **3-043r**: „nese člověk v délce jedné pídi oheň“ → „lze v píď dlouhé sítině nosit oheň“.
- **3-043v**: „terpentýn {Gloriet} či pryskyřici {Glaret}“ → „terpentýn {Gloriet} neboli *Glaret*“ (pravopisné varianty
  téhož); doplněno „[rozpustit]“; „když se to chce navlhčit“ → „když ji chceš použít“ + nová pozn. 2 (*netzen* za *nützen*,
  ověřeno ve skenu); poznámky přečíslovány 2→3 … 5→6.
- **3-044r**: vypuštěny poznámky opakující glosář (*Quintat* = kvintlík, *wildes feur* = divoký oheň), zbylé přečíslovány;
  „jest to“ → „je to“ (i 3-044v).
- **3-044v, 3-051v**: překlep v poznámce „ohněstrůjných“ → „ohňostrojných“.
- **3-045r**: „sírový drát“ → „sirný drát“ (jednotně s 3-041v); „šípový svorník“ → „dřík šípu“ (*boltz*).
- **3-046r**: „naplň dlouze pytlíčky, nalož s tímto vlhkým prachem“ → „dlouhé pytlíčky naplň tímto vlhkým prachem“.
- **3-047r**: „odstřelit/rozstřílet věž“ → „sestřelit věž“; „věž se otřese a zřítí spíše, než kdyby se … různě po ní“ →
  „věž se rozštěpí a zřítí rychleji, než kdyby se do ní jinak pálilo prudce a mnoho“; pozn. 2 zkrácena (neopakuje
  glosář `stopina`).
- **3-047v**: překlep „ledkiem“ → „ledkem“; „cvilichovým“ → „cvilinkovým“ (i 3-050v); „vyrovnej dělo do rovnováhy“ →
  „nastav dělo vodorovně“ (*inn gleichs gewicht*, i 3-051v); „zátka má být dobře zaražena“ → „[ucpávka] dobře zaražena“
  (podmět v tisku chybí, papírová zátka se naopak zarážet nemá) + přepsaná pozn. 3.
- **3-048r**: **„Naplň ji tedy ledem“ → „ledkem“**; „Má-li dělo komoru“ → „Má-li zbraň komoru“ (jde o ručnice a
  tarasnice); přepsány spekulativní pozn. 1 (tvrdý prach – postup je níže na téže straně), 2 (*Salpeter* ověřen ve
  skenu) a 5.
- **3-048v**: „nerozutíkalo od sebe“ → „nerozpadlo“; pozn. 2 k *haußpfeil* upravena (viz sporná místa).
- **3-049r**: „vadnou mušku“ → „nesprávné mířidlo“ (*falsch zilmaß*); „pravítko nebo měřidlo“ → „pravítko či rovnací
  pravítko {Richtscheidt}“.
- **3-049v**: „ze tří dílů prachem“ → „prachem do tří dílů“; „o polovinu kratší než širší“ → „kratší, než je široká“;
  „přibij hlínu“ → „natluč“; „nech ji letět“ → „nech tyč letět“.
- **3-050v**: „zastřílené nebo ne“ → „vyzkoušené střelbou, nebo ne“ (*beschossen*).
- **3-051r**: oprava `de` OCR **geschoffen → geschossen**; přeložen znovu odstavec *Von schiessen auff dem Felde* a přepsána
  pozn. 4 (viz sporná místa).
- **3-051v**: opravy `de` podle skenu **klotz Büchsen → klötz Büchsen**, **Burias → Burras** (ꝛ, shodně s 3-052r),
  **ronde → rondt**; „zátková děla“ → „děla se zátkami“.
- **3-052r**: „kosou ránu“ → „plochou ránu po zemi“ (*streiffenden schus*); „dělo úmyslně roztrhnout“ → „snadno roztrhnout“
  (*gern zuschiessen*).

## Ověřeno ve skenech (BSB IIIF bsb00085168, skeny 333, 336, 338, 346, 347, 354)
- 333 (3-041r): *voln vnd gentzlich* (ne *vorn*) – opraveno; *Eyer 15. Calcis viue ij.* a *ij. Salpeter* souhlasí.
- 336 (3-042v): *pleiß* skutečně v tisku; dole kustod *ter* za *Salpe-* – slovo *Salpeter* je správně celé na 3-043r.
- 338 (3-043v): *wann mann es netzen wil*, *1. Centener zulöschen wachs*, *ein ölein Calonefemia*, *eichen feur* – vše
  v tisku (tiskové chyby, ponechány s poznámkami).
- 347 (3-048r): *fül sie mit Salpeter*, *vmb geuß die Form mit*, *je nimder sich der schafft zu schlecht* – v tisku.
- 354 (3-051v): *klötz Büchsen*, *Burras*, *rondt Puluers*, *bewarnet biß mit vier Büchsen* – opraveny první tři, čtvrté
  je v tisku (pozn. 6 ponechána).

## Sporná místa k rozhodnutí
1. **3-051r** – *so hab acht so auß der geschossen wirdt / so mach mann zuuor an ein rauch mit Puluer / ehe er scheusset /
   vnd so auff jn geschossen ist / so schieß mann darnach auch auff jn.* CS nyní: „… dávej pozor, odkud se z něho střílí.
   Než [nepřítel] vystřelí, udělej nejprve prachem kouř, a jakmile se na něj vystřelí, střílej potom také ty na
   nepřítele.“ Výklad jako lest (kouř předstírá výstřel, nepřítel prozradí dělo); dřívější verze četla jako sledování
   kouře nepřátelského děla. *auff jn* může znamenat kouř i nepřítele.
2. **3-048v / 3-049r** – *haußpfeil* přeloženo podle glosáře „zápalné šípy“, ale předpis o zápalné náplni nemluví (šípy
   nabité do děla za desku). Navrhuji rozhodnout, zda *haußpfeil* nemá v glosáři samostatné heslo.
3. **3-041r** – *Tuch* v *auß der Materien mach ein Tuch* (ve skenu *Tuch*), přeloženo „sukno“; smyslem spíš „koláč“ (*Kuchen*)?
   Ponecháno doslovně.
4. **3-041r** – *öle vnd Eyer 15.* přeloženo „olej a 15 vajec“; může jít i o 15 dílů oleje a vajec. Ponecháno.
5. **3-043v** – *netzen* chápáno jako *nützen* („použít“), nová poznámka; doslovné „navlhčit“ v kontextu nedává smysl
   (hmota se vznítí od větru/slunce).
6. **3-046v** – dělení vývrtu na 5 dílů (1 zátka, 1 „nechat stát“, 3 prach) ponecháno doslovně; dosavadní pozn. 2 je
   spekulativní (*Flugraum*), doporučuji ji zkrátit na „patrně volný prostor pro kámen před zátkou“.

## Návrhy do glosáře
- `zapalny-sip` – sjednotit napříč 3. knihou (od 3-053r dál „ohnivé šípy“); případně vyjmout *haußpfeil* do hesla
  `domovni-sip` | cs „domovní šíp“ | de *haußpfeil* | delostrelectvo | „Šíp vystřelovaný (i z děla) proti stavením“.
- `sekane-zelezo` | cs „sekané železo“ | de *schifferling, Schifferling, schirfferling* | delostrelectvo | „Kostky
  nasekané z čtyřhranného tyčového železa, nabíjené do děla jako kartáč (3-048v–3-049r).“
- `jezek` | cs „ježek“ | de *Igel* | delostrelectvo | „Náboj ze stovek nasekaných železných kousků před železnou miskou
  (3-050r).“
- `tvrdy-prach` | cs „tvrdý prach“ | de *hertes Puluer, herten Puluers* | delostrelectvo | „Prach uhnětený s pálenkou
  (a rtutí) a vysušený do tvrdé hmoty (3-048r).“
- `hrudkovity-prach` | cs „hrudkovitý prach“ | de *Knöllig Puluer, knölligem Puluer* | delostrelectvo | „Prach ztužený
  octem do bochánků/hrudek, odolnější proti zkáze (3-052v–3-053r).“
- `kamenna-koule` – pozn. mluví o „kamenometných dělech“, glosář má heslo „kamenné dělo“; sjednotit formulaci.
