# 2. revize – Třetí kniha, dávka E (3-053r … 3-067r)

Rozsah: 29 stran (skeny 357–385), konec Třetí knihy: recepty na střelný prach (silný, daleko nesoucí, zápalný,
trhací, barevný), napravování zkaženého prachu, dobývání, čištění, zkoušení a nákup ledku, příprava síry
a sirného oleje, pálení dřevěného uhlí a milíře. Sousedé `3-052v` a `4-erb-solms` jen čteny; návaznost
`3-052v` (nadpis „Jak se má dělat velmi dobrý … prach“) → `3-053r` (recept bez nadpisu) sedí.
Přechody `pokracovani: true` (055r, 056v, 057r, 062v, 065v, 066r, 067r) beze změny a sedí s originálem.
Struktura bloků, `sken`, `id`, `stav: zkontrolovano`, `overeno_clovekem: false` beze změny; žádné `zarovnat`.

Kontrola: `python -I nastroje/over_strany.py knihy/solms-1559 3-053r … 3-067r --prisne` → **0 chyb, 1 varování**
(3-059v blok 2: *so wirt er fein vnd gůt* – skutečné *fein* „jemný“, není chyba OCR; neopravitelné).
Pořadí poznámek `[^n]` na všech stranách ověřeno skriptem (vzestupně od 1).

## Opravy `de` podle skenů

| strana | bylo | tisk (sken) | pozn. |
|---|---|---|---|
| 3-054v | laß es dann stehn | **laß es deñ (denn) stehn** | sken 360 |
| 3-062r | Camil / Alumen / Isponicum | **Alunien** | sken 375; srov. *salunien* na 062v |
| 3-062r | das fast nutzt | **nützt** | sken 375 |
| 3-062v | gleich als salumen | **salunien** | sken 376 (OCR četlo *salumen*) |
| 3-062v | ein jegliche Species | **jetzliche** | sken 376 |

Ověřeno ve skenech beze změny: *damit gereit der stück eines*, *Salarmoniac Litargis*, *verfeuchtlich* (357);
*heiß sieden / dann du möchst den wein verschüten*, *Salpartica* (358); *gar böß salpeter*, *garbs schwefel*,
*stettit*, *Camforis*, *bricht* (360); *Widertat*, *Capillum verium*, *1. vntz weiß / Albram holtz*, *bast* (363);
*Salpratica*, *den 12. ij. theil Kols*, *grabes schwefels*, *grimentlich*, značky unce (365 – sazba tiskne znak
podobný drachmě ʒ; že jde o unci, potvrzuje paralelní recept na 055v *1. vntz Kalchs*, ponecháno `℥`);
*werden dan die tropffen heiß* (372); *gůt schwartz* (375); *er treugt* (376); *wesch den Hafen | sen* (378);
*das vor al|lein gewesen ist*, *gulden werdt* (382).

## Jednotná terminologie v dávce

- *Büchsen Puluer / Büchsenpuluer* → vždy **„střelný prach“** a *Feurpfeil* → **„zápalný šíp“** podle glosáře
  a sjednocení v dávce 3-D (dosud střídáno „puškový prach“ / „ohnivý šíp“; 17 výskytů na 12 stranách).
- *Vierling / Quertlin* → **„čtvrtka“** podle glosáře (místo „čtvrtlibří“, „čtvrť mázu“); poznámka o vierlingu
  na 053r vypuštěna (vysvětluje glosář).
- *Centner / Zentner* → **„cent“** (065r „centnýř“ opraveno); *drithalb Centner* → „dva a půl centu“ (056v, 058v).
- *Litargis / silberschaum* → „olověný klejt“ (dříve „olovnatý glejt“ / „stříbrný klejt“).
- *Isponicum / Ispontcum* → všude „měděnka“ (054r mělo „španělská sůl“) – opora: 061v *Grünspan* na témže místě.
- *Salpartica / Salpratica / salpentica* (053v, 057r, 058v) – dříve „skalní sůl“ / „tavený ledek“; nejasná přísada
  nyní ponechána nepřeložená v kurzivě se shodnou poznámkou.
- *Alber- / Albram / Albran* → „topol“ (066v dříve „střemchové“, pozn. „krušina… topol bílý (linda)“).
- *grabes / graben / garbs schwefel* → „surová síra“ (054v dříve „čistá“).
- *Widertat* → „ploník“ (056r mělo „netík“ dvakrát, v rozporu s vlastní poznámkou).
- `{Mörser}` u kuchyňského hmoždíře (066r) odstraněn – vedl na heslo *moždíř* (dělo); `{zündtloch}` u milíře
  (067r) odstraněn – vedl na *zátravku*.
- „jest“ → „je“ v celé dávce (46 řádků; „to jest“ ve významu „tj.“ ponecháno), méně archaismů.

## Hlavní změny po stranách

- **3-053r** – „prosij“ → „prosej“; dlouhé souvětí receptu rozděleno na věty; „promění se v sobě“ → „navzájem se
  promísí“; *damit gereit der stück eines* nově „aby se přísady spojily v jedno“ (pozn. 2, dříve „čímž se každá
  přísada připraví“); pozn. 3 (*zustossen*) zneutralizována.
- **3-053v** – *dann du möchst den wein verschüten*: „neboť bys jinak mohl víno rozlít“ (+ pozn. o porušeném textu)
  → „potom můžeš víno slít“ (*verschütten* = vylít; souhlasí s paralelou na 057r).
- **3-054r** – *so du am aller besten erwelest*: „jakou si jen můžeš přát“ (čteno jako *erwählen*) → „v octě, který
  co nejlépe provaříš“ (*erwelen* = uvést do varu, jak o řádek výše); věty rozděleny; pozn. 1 bez OCR údajů.
- **3-054v** – *stettit* „malý dílek“ → „štetit“ s odkazem `[[3-058r|l. 58r]]` na vysvětlivku tisku (Nota: čtvrtina
  lotu = kvintlík); „nabij jím třetinu děla“ → „nabij jím dělo do třetiny“; „mistrný“ → „mistrovský“ (jako 055v).
- **3-055r** – *thů der zweier species von Mercurio sublimato darzů* „přidej dvě přísady ze sublimované rtuti“
  → „přidej k těm dvěma přísadám sublimovanou rtuť“ + nová pozn. 3 (nejisté); pozn. 2 *Puluerstein* propojena
  s *braunstein* na 058v.
- **3-055v** – „do velké koule“ → „do velkých koulí“ (*vnder die grossen Kugel*, dále *die dritten*); pozn. 1 a 2
  zkráceny o výklad, který dává glosář (hlavní dělo, unce).
- **3-056r** – „mocně žene“ → „lépe žene“ (*baß*); věty zpřirozeny.
- **3-056v** – vypuštěna pozn. 1 (jen historie chyb OCR), přečíslováno; zkouška prachu na kameni přestavěna.
- **3-057r** – pozn. 2 bez OCR, doplněno ověření značky unce; *das weit schiessende Puluer, das jemant gehaben mag*
  → „ten nejdále střílející prach, jaký kdo může mít“.
- **3-057v** – *fül die auff das drittheil* „naplň je do jedné třetiny“ → „nabij jím dělo do třetiny“ (*die* = Büchse
  z nadpisu na 057r); *zum dritten jar* „každého třetího roku“ → „ve třetím roce“; „od železa může chytit oheň“
  → „od železné [paličky] by mohl chytit oheň“; pozn. 4 (OCR) vypuštěna.
- **3-058r** – zdvojené „surové síry (*graben Schwefels*) {Schwefels}“ sjednoceno; pozn. 5 (OCR) vypuštěna.
- **3-058v** – úvod odstavce *EIn alt vergangen Puluer…* jako věcný nadpis („Jak napravit starý zvětralý prach…:
  Dále vezmi…“); „nech zvolna vyschnout“ → „nech tak trochu proschnout“ (*also wenig*); *je 30. züge* → „na každých
  30 [liber] hmoty“; nová pozn. 6 k porušenému závěru receptu (srov. 055r).
- **3-059r, 059v, 060r, 060v, 061r, 061v, 062r, 062v, 063r, 063v** – vypuštěny poznámky, které jen popisovaly
  chyby BSB OCR (celkem 11), zbylé přečíslovány. 059v *seud die zwei theil ein* „odvař dva díly“ → „vyvař dvě
  třetiny“; 060r *Brünnwasser* „čirou pramenitou vodu (*Brünnwasser*)“ + OCR pozn. → „čistou studniční vodu“;
  060v „ledek… velmi bují“ → „hojně roste“, „avšak ty se máš vždy vystříhat“ → „Ty se však vždy vyvaruj bílého
  ledku“; 061r „1 libra vykoná více“ zpřehledněno; 061v „vodu slij, aby ledek zkrystalizoval“ → „vodu slij a nech
  ledek zkrystalizovat“ (*geuß… ab / laß… gestehn*); 062r „urovnaj“ → „urovnej“, *Camil* ponecháno nepřeložené
  (dříve „heřmánek“ jako jistota), „obrať jej dnem vzhůru“ → „obracej jej“; 062v *er treugt* „je způsobilý“ →
  „je dobrý“ (s pozn.); 063r úvaha o kupcích rozdělena na 3 věty, *wirt gůt Essig darauß* → „bude z něj dobrá
  hmota“ (pozn. o *Essig* ponechána); 063v *Hafen sen* – pozn. přepsána: *sen* je zbytek *aussen* (srov. 064r
  *außwendig*), proto „smeť… [výkvět z] hrnce [zvenčí]“.
- **3-064r** – „ledek prorazí hrncem ven“ → „vykvete skrz stěnu hrnce ven“; poučení o polévání zdi rozděleno.
- **3-064v** – „latinsky se nazývá kamenná sůl (*sal petrae*)“ → „(*steinsaltz*)“ – tisk má *steinsaltz*, ne *sal
  petrae*; *röß* „prudký“ → „ostrý“.
- **3-065r/065v** – „centnýř“ → „cent“; 065v „solanková voda s ledkem“ (chybně) → „ledková voda, předtím slitá zvlášť“.
- **3-066r** – `{Mörser}` a pozn. 1 vypuštěny; verše o sirných svících přebásněny (AABB zachováno: mít/rozpustit,
  k ní/skrze ni); *mach dann das Glaß naß* „navlhči skleněnou nádobu“ → „sklo [se rtutí] navlhči… rozmíchej v síře“
  (*Glaß* je přísada z téhož receptu); *brauchs nit zuuil* „nedávej jí však tolik“ → „není jí třeba tolik“.
- **3-066v** – *Albran* „střemchové“ → „topolové“, pozn. přepsána; „lněný ubrus“ → „ubrus“ (*lněný* v tisku není).
- **3-067r** – `{zündtloch}` u milíře → „zapalovací průduch“ bez odkazu.

## Sporná místa k rozhodnutí

1. **3-053r** *stoß das damit gereit der stück eines* – CS „Utluč to, aby se přísady spojily v jedno“; čtení
   *gereit* = *gerät* je hypotéza (pozn. 2).
2. **3-053r** *dann hebt sich der Zeug an zustossen* – CS „potom se hmota začne [znovu] tlouci“; smysl nejistý (pozn. 3).
3. **3-055r** *nime des ein achttheil / thů der zweier species von Mercurio sublimato darzů* – CS „vezmi toho jednu
   osminu, přidej k těm dvěma přísadám sublimovanou rtuť“; alternativa „přidej sublimátu tolik co obou přísad“.
4. **3-057r** znaky `℥. iiij.` atd. – v sazbě vypadají jako drachma (ʒ); ponecháno jako unce podle paralely 055v.
   Kdyby šlo o drachmy, byl by poměr 4 : 1 : kafr 1 kvintlík nepravděpodobný.
5. **3-053v / 057r / 058v** *Salpartica / Salpratica / salpentica* – nepřeloženo; dřívější „skalní sůl“ / „tavený
   ledek (*sal prunellae*)“ nemají oporu v textu.
6. **3-062r** *Camil* – nepřeloženo (heřmánek? vápno?).
7. **3-062r** *gibt es gůt schwartz / vnd in etlicher maß plawes Feur* – CS „sytě černý a zčásti modrý oheň“; možná
   tisková chyba (pozn. 2).
8. **3-062v** celý první odstavec (*als Sal siluestrum / salunien zeucht zu jm…*) je v tisku porušený; přeloženo
   doslovně s pozn. 1.
9. **3-063r** *wirt gůt Essig darauß* – CS „dobrá hmota“ (předpoklad *zeug*); doslova „dobrý ocet“.
10. **3-066v / 3-056r** *Albran / Albram / Alber* = topol – sjednoceno; *weiß Dennen* = „bílá jedle“.

## Návrhy do glosáře (needitováno)

| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| prach | střelný prach | + Büchen Puluer, Büchsen puluer | delostrelectvo | Doplnit tvary z 3-054r a 3-048r; *Büchsenpulver* = „střelný prach“ (sjednoceno s 3-D). |
| salmiak | salmiak | Salarmoniac, Salis Armoniac, salarmoniac | delostrelectvo | Chlorid amonný, přísada posilující prach a čisticí přísada při rafinaci ledku. |
| medenka | měděnka | Spangrün, Spangrön, Grünspan, Isponicum, Ispontcum | delostrelectvo | Octan měďnatý („španělská zeleň“, *viride hispanicum*), přísada při čištění ledku. |
| skalice | skalice | Galitzenstein, Glaritzenstein, Kupfer wasser, Vitriolum Romanum, Atrament, Atrimentum | delostrelectvo | Bílá (zinečnatá), zelená (železnatá) či modrá (měďnatá) skalice; *Atrament* konzervuje uhlí. |
| kamenec | kamenec | Alaun, Alaum, Alandt, Alumen, Alunien, salunien | delostrelectvo | Podvojný síran, nečistota i čisticí přísada ledku. |
| olovny-klejt | olověný klejt | Litargis, silberschaum | delostrelectvo | Oxid olovnatý z čištění stříbra. |
| sublimat | sublimát | sublimat, Mercurio Sublimato, Mercurius sublimatus | delostrelectvo | Chlorid rtuťnatý, přísada „posilující“ prach. |
| kafr | kafr | Kampffer, Kampfer, Campfer, Camforis, Camporia, Camper | delostrelectvo | Přísada urychlující hoření prachu. |
| sanytr | sanýtr | Saluiter, saluiter, Salutter preparatum | delostrelectvo | Podle tisku název ledku po přečištění varem. |
| stetit | štetit | stettit, Stettit | miry | Podle tisku (l. 58r) čtvrtina lotu = kvintlík. |
| ctvrtka | čtvrtka | + vierling, quertlin | miry | Doplnit malá písmena (v 3. knize výhradně *vierling*); *Quertlin* = čtvrtka mázu. |
| stopa | stopa | + schůhß | miry | Tvar z 3-067r. |
| milir | milíř | Koln hauffen | delostrelectvo | Hranice dřeva přikrytá hlínou k pálení uhlí (3-067r). |
