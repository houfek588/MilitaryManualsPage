# 2. revize – Solms 1559, dávka „kniha2-E“ (`054r`–`073r`, skeny 191–221)

Revize podle `zdroje/ZADANI_REVIZE2.md` (plynulost „středně“, Oberst = plukovník, Fendlin u jízdy = korouhev,
Kriegßleut = válečníci). Struktura bloků, `sken`, `id`, `stav: zkontrolovano` a `overeno_clovekem: false` beze změny.
Sousedé `053v` a `073v` jen čteny; návaznost `053v → 054r` („před nejvyšším | polním hejtmanem“) a `073r → 073v` sedí.

Strany dávky (30): `054r 054v 055r 055v 057r 057v 059r 059v 060r 060v 061r 061v 062r 062v 064r 064v 065r 065v 066r 066v
067r 067v 069r 069v 070v 071r 071v 072r 072v 073r`.

Ověření: `python -I nastroje/over_strany.py knihy/solms-1559 <30 stran> --prisne` → **30 stran, 0 chyb, 0 varování**.

Postup: strojové porovnání `de` s OCR (`zdroje/ocr_bsb/0191–0221.txt`) po slovech; odchylky a sporná místa ověřena
ve skenech BSB IIIF (`bsb00085168_00195`, `_00198`–`_00203`, `_00205`–`_00209`, výřezy). Dřevořezy `drevorez-216.jpg`
a `drevorez-220.jpg` prohlédnuty.

## 1. Opravy originálu (`de`) podle skenu

| Strana | Bylo | Nyní (podle tisku) | Pozn. |
|---|---|---|---|
| `055v` | `Kriegßherrn` | `Kriegsherrn` | tisk má *Kriegs-* (OCR *Kriegsherm* = *Kriegsherꝛn*) |
| `059r` | `Grauen oder Herrn`, `die Herrn sollen jnen` | `Herren` (2×) | tisk *Herꝛen* (OCR *Herzen*) |
| `059v` | `Kriegßherrn` / `Kriegßherr` (6×) | `Kriegsherren` / `Kriegsherr` | sken 198: *Kriegsherꝛen*, *Kriegsherꝛ* |
| `059v` | `in jrem bestelbrieff erhalten` | `bestelbreiff` | tiskový tvar |
| `059v` | `so von seinem volck nider ligen lösen` | `… nider ligen lassen` | **tisk má *lassen*** (předchozí kontrola emendovala); ponecháno, nová pozn. 2 (smysl *lösen*) |
| `059v` | `dem Herrn besser` | `dem Herren besser` | |
| `060r` | `mit seinen Reuttern will machen` | `Reutern` | |
| `060r` | `grundtlich` | `gründtlich` | |
| `060r` | `lenger werde dann sie breidt ist` | `… bereidt ist` | tisk poprvé *bereidt*, dále *breidt*; pozn. 1 |
| `060r` | `beritten seie / nemen / denselben` | `beritten seie / neben denselben` | **tisk má *neben***, emendace *nemen* byla jen v `de`; tisková chyba vysvětlena v pozn. 2 |
| `060v` | `Kriegßherrn` | `Kriegsherrn` | |
| `061r` | `wann er Reutter im Leger hett` | `… helt` | tisk *helt* (= hält), ne *hett* |
| `061r` | `jren Herrn`, `jenen Herrn` | `Herren` | |
| `061v` | `vortheil ersicht` | `vortheil erste` | tisk *erste* (tisková chyba za *ersicht*), nová pozn. 1 |
| `061v` | `Lieben Herrn` | `Lieben Herren` | |
| `062r` | `mit seinem hauffen` | `mit seinen hauffen` | tisk |
| `062r` | `Feldmarschalck erkündigen` | `Feldmarschelck erkündigen` | tisk; nová pozn. 1, `{Feldmarschelck}` |
| `064v` | `Ampter besetzt hat` | `besatzt` | tisk |
| `065v` | `vnd dannoch vngeschafft müß abziehen` | **`vngestrafft`** | chyba přepisu (OCR i tisk *vngestrafft*); změněn i překlad |

Ověřeno a ponecháno: iniciály `EIn` (055r), `WAnn` (057r), `VOn` (059r), `WJewol` (064r), `DEr` (067r, 072r), `DIe` (069r, 071r),
`WAs` (062v), `WAchtmeister` (073r); tiskové tvary `Rart` (065v), `Obester` (066r), `Obest` (065r), `Feldhaumans` (059v),
`Feldmarschack` (057r), `zimbliche` (062r), `beseitz` (061v), kustody `stand` (057r) a `sonst` (060v). Rozpis žoldů
na `064r` souhlasí se skenem 205 (sloupce za sebou, 46 řádků; tabulka beze změny).
Nejisté (neměněno): `061v` *Hauptman sollichen* – tisk snad *Hauptteman/Haupteman* (OCR *Haupteman*), nečitelné.

## 2. Hlavní změny překladu po stranách

- **`054r`**: „takového pohnání … nikdo nevyčkává rád“ → „nikdo nedočká rád“; „svého pacholka {Bůben}“ → „své pachole“ (glosář);
  dva dlouhé odstavce o vozové hradbě rozděleny; „před těžkou jízdou“ sjednoceno „těžkooděncům“ (*schwer Rüstung*);
  zrušena zbytečná pozn. „V tisku Norweden“ (glosář `norove`), doplněno `{Muscabiter}`.
- **`055r`**: velký odstavec o vozmistrovi rozdělen do ~15 vět; *in der ordnung vnd versehung* „v šiku a pod ochranou“
  → „v pořadí a pod dohledem“ (jde o pořadí vozů, ne o šik); „tak mají i vozy táhnout za nimi a před nimi a střídat se“
  → „tak se mají vpředu a vzadu střídat i jejich vozy“; *langsam auff sein* „vstávat pozdě“ → „otálet“; shoda „ostatní, které“.
- **`055v`**: *darnach darauff ein zeucht* nově „když pak za ním vjede na cestu“; „úřad a pravomoc“ → „úřad a povinnost“ (*beuelch*);
  pasáž o oslech rozdělena, „samotní v jednom houfu“ → „zvlášť v jednom houfu“.
- **`057r`**: „není zapotřebí žádného kvartýrmistra, neboť kde stojí řada vozové hradby každého [oddílu]“ → „kde má kdo v řadě
  vozové hradby své vozy“; „jež jsou pro stručnost pominuty“ → „které pro stručnost pomíjím“ (1. os.); visící podmět
  v odst. 2 opraven („mají kvartýrmistři … začít“); **gramatická chyba** „ubytuje se vždy kurfiřty“ → „ubytovávají se vždy kurfiřti“.
- **`057v`**: „nepravosti“ → „podvody“ (*gefehrlicheit*), věty rozděleny; „kdy … vyjet, jelikož znají kvartýr“ → „neboť vědí, kde má který hejtman kvartýr“.
- **`059r`**: „Stejně tak i [žold] měsíčně na jednoho koně“ → „Totéž platí o měsíčním žoldu na jednoho koně“; **věcná oprava**
  „jak se pak ostatním jezdcům … vydržují vozy, tak se vydržují i hejtmanovi“ → „Jako jsou ostatní jezdci placeni podle svých
  koní i s vozy, tak je placen i hejtman za své koně“; *trosser* sjednoceno „trénní sluha“; drabanti „pod některým hejtmanem pěchoty“
  → „u hejtmana se přehlížejí a platí jako pěší“ + pozn. 2 (viz sporná místa); odstraněno zdvojené „chodit“ na přelomu 059r/059v.
- **`059v`**: „lze radit“ → „lze doporučit“; podmět „je bez jejich škody“ → „každého z nich … bez jeho škody“; **věcná oprava**
  *es ist sonst aller schade … von feinden geschehen* „jinak by všechny škody pocházely od nepřátel“ → „jinak by se každá škoda
  na koních vydávala za škodu způsobenou nepřítelem“; **věcná oprava** *diß ist auch nit lang gewesen* „ani tento zvyk netrvá dlouho“
  → „i tento článek se objevil teprve nedávno“; konec věty přes hranici 059v/060r („podle toho, co stojí u nejvyššího polního hejtmana |
  v posledním článku“).
- **`060r`**: „aby vyjel stranou“ (*auff ein ort rücken*) → „vyjel na určité místo“; **neúplná věta** „Za druhé, kdyby hejtman … nerozuměl,
  aby špice věděla…“ přestavěna („Za druhé proto, aby špice věděla …, kdyby hejtman …“); „dobře vsedlí … jízdní čeledíni“ → „vyzbrojení čeledíni na dobrých koních“.
- **`060v`**: „k obklopení korouhve“ → „k obsazení korouhve“ (*zubesetzung*, 2×); *daß er sein stat wider zu finden wisse* přeformulováno.
- **`061r`**: „a neležet … a nečekat na troubení“ → „a ne se válet … a čekat, až se zatroubí“; dlouhé souvětí o tajném vzdalování ze šiku
  rozděleno, nedořešené „aby … nevypadaly“ převedeno na oznamovací důsledek; `{Fůterung}` = píce.
- **`061v`**: „společně táboří“ → „hospodaří společně“ (*purschen*); **věcná oprava** „nevpadli mezi předvoj či zadní voj do vojska přes děla“
  → „nevpadli mezi předvojem a zadním vojem do vojska a nenapadli děla, vozy nebo trén“ (*vbers*); „zemani“ → „junkři {Junckern}“ (glosář).
- **`062r`**: „To by se mohlo dít i dosud“ → „To by se mohlo dělat i dnes“; „hledět na něho“ → „řídit se jím“; *zeichen* jednotně „znamení“
  (dříve „prapor“); „ledaže ví, co se praporečníkovi sluší“ → „který neví, co praporečníkovi přísluší“.
- **`062v`**: odstavec o rumormistrovi rozdělen; nejasné „má proti nim vždy nasadit jezdce, kteří leží pod některým [z jejich] hejtmanů“
  → „má na ně vždy posílat jezdce od téhož hejtmana, pod nímž provinilci leží“; zrušena pozn. o *Rhumormeister* (opakovala glosář).
- **`064r`**: „plukovník u knechtů“ → „nad knechty“; souvětí rozděleno, „namísto pána“ → „v zastoupení pána“.
- **`064v`**: „prostý lid {gemein Man}“ → „obec“ (glosář); věta o propadnutí majetku přestavěna; **věcná oprava** *darzu wist der Oberst
  Veldhauptman nit* „neboť jinak by … nevěděl“ → „nejvyšší polní hejtman by navíc nevěděl“; *hauffen* „šiky“ → „houfy“.
- **`065r`**: dlouhá věta o cizích kontingentech rozdělena a zpřehledněna (kdo komu dává pravomoc); „poplachové shromaždiště“ → „poplachové místo“ (jednotně v dávce).
- **`065v`**: *vngestrafft* (viz výše): „s nepořízenou“ → „aniž by byl nepřítel potrestán“; *sprengen* „podkopat [hradby]“ → „odstřelovat“ (glosář);
  „poctivě knechty napomínat“ → „počestně povzbuzovat“ (*ehrlich ermanen*); „sesednout a jít pěšky“ → „sesednout a postavit se pěšky“.
- **`066r`**: zrušen přídavek „[a rvačku]“; *verehrung* „poctou“ → „čestným darem“ (glosář); „takové správy“ → „takového velení“;
  *mit Recht* „po právu“ → „soudně“.
- **`067r`**: přísaha profouse rozdělena do 3 vět; *schätzt die Prouiant* „oceňuje proviant“ → „stanovuje ceny proviantu“.
- **`067v`**: *mit recht* → „na základě rozsudku“; *Gerichtsman* „soudní muž“ → „přísedící“ (glosář), pozn. 2 zkrácena na tiskové *sei*;
  „týž nestranně vykonat“ → „ten pak“; poslední odstavec převeden z plurálu do jednotného čísla (*Welcher oder welche*).
- **`069r`**, **`069v`**: drobné úpravy slovosledu; „vzešly by velké zbytečné výdaje“ → „pán by tím jen zbytečně vydal mnoho peněz“.
- **`071r`**: `{paß}` (glosář `prusmyk`), „poplachové shromaždiště“ → „poplachové místo“.
- **`072v`**: popis dřevořezu zpřesněn – za vachmistrem jede jezdec se vztyčeným **obouručním mečem** (dříve „dlouhá rovná zbraň či píka“), plátová ochrana paží, klobouk s peřím.
- **`073r`**: „před obléhanou posádkou“ → „před obléhaným místem“; „žertovat“ → „zahrávat si“; souvětí o kontrole stráží rozděleno.
- Beze změny: `054v`, `066v`, `070v`, `071v` (popisy dřevořezů odpovídají), `072r`.

## 3. Sporná místa k rozhodnutí

1. **`059r`** – *die Trabanten werden vnder einem Hauptman zu fůß gemustert vnd bezalt.* Dříve „pod některým hejtmanem pěchoty“, nyní
   „u hejtmana se přehlížejí a platí jako pěší“. *zu fůß* chápu adverbiálně (drabanti hejtmana jízdy jsou pěší). Obě čtení v pozn. 2.
2. **`059v`** – tisk *nider ligen lassen* místo očekávaného *lösen*; v `de` ponechán tisk, překlad podle smyslu („vykoupit“), pozn. 2.
3. **`060r`** – tisk *neben denselben* místo *nemen*; lze číst i „vedle téhož [praporečníka]“, ale pak chybí sloveso k *Er soll einn … Kriegsman*. Překlad „vezme“.
4. **`061v`** – tisk *erste* (= *ersicht*?); případně *Haupteman* v tisku na téže řádce – ověřit při vyšším rozlišení.
5. **`071r`** – *daß sie daran riet haben* (pozn. 1 „váhá“) – smysl nejistý (snad *irr/Rat*?), ponecháno.
6. **Knecht ve významu sluhy** (`054r`, `055v`, `059r`, `060r`, `060v`, `061v`): ponecháno „čeledín {Knecht}“ místo glosářového „knecht“, protože jde o služebníky jezdců/úředníků, ne o pěší žoldnéře.

## 4. Návrhy do glosáře

| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| `knecht` (doplnit pozn.) | čeledín (ve významu sluhy) | Knecht | jednotky | U jezdců a úředníků (*Knecht vnd Pferde*, *kein knecht*) znamená sluhu/čeledína; překládat „čeledín“, ne „knecht“. |
| `tren-sluha` | trénní sluha | Trosser, Trossern | jednotky | Sluha u vozů a koní v trénu jezdce; dnes v hesle `trén`, ale jde o osobu. |
| `polni-marsalek` (doplnit de) | polní maršálek | Feldmarschelck | velitele | Tiskový tvar na `062r`. |
| `poplach` (cs pro *Lermenplatz*) | poplachové místo | Lermenplatz, Lermen platz, lermenplatz | sluzba | Sjednotit (v dávce dříve i „poplachové shromaždiště“). |
