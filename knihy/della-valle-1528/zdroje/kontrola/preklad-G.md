# Dávka G – překlad, skeny 141–163 (061r … 072r)

Kniha IV, kapitoly XVI–XXXVI (konec kodexu cti a soubojů), závěrečné slovo autora, tiráž, registr archů a tiskařský znak.
Přepis celý ze skenu (IIIF archive.org, 1600 px + výřezy), OCR archivu jen k orientaci. `over_strany.py --prisne`: 23 stran, 0 chyb, 0 varování.

## DŮLEŽITÉ – nesoulad struktury konce knihy se zadáním a s kniha.yaml
- **Tiráž a registr archů jsou na 071r (sken 161)**, ne na 071v. Líc listu 71 nese konec kap. XXXVI, závěrečné oslovení
  „Excellentissimo S. mio“, tiráž (Benátky, Piero de Ravani, 9. 12. 1528) a REGISTRO.
- **Tiskařský znak (siréna) je na 071v (sken 162)** – rub listu 71, prosvítá na něm zrcadlově text líce.
- **Sken 163 (strana 072r) je prázdný** – patrně prázdný list I8 [72] r nebo předsádka. Stranu `072r` jsem **nechal beze
  změny** (`stav: chybi_original`, `bloky: []`); podle PRAVIDEL § 1 se prázdné strany nezakládají – navrhuji ji správcem
  smazat (nebo jinak označit) a opravit `kniha.yaml` (`strany_poznamka`, `poznamky_k_prekladu`: „tiráž a registr 71 r
  (sken 161), tiskařský znak 71 v (sken 162), sken 163 prázdný“).
- Registr „1 A B C D E F G H I / 4 4 …“ = úvodní arch + archy A–I, vesměs kvaterniony (8 listů) → 80 listů, tj. [8] + 72;
  list [72] tedy v tisku existoval (prázdný).

## Přehled stran
| Strana | Sken | Obsah |
|---|---|---|
| 061r | 141 | konec kap. XV; kap. XVI (souboj do tří ran – kdo je poražený; příklad míčové hry a šermířských mistrů); začátek nadpisu XVII |
| 061v | 142 | kap. XVII (jeden chce bojovat na koni, druhý pěšky; smí sesednout a zabít svého koně) |
| 062r | 143 | konec XVII; kap. XVIII (zajatec přemožený dvakrát – komu patří) |
| 062v | 144 | konec XVIII (patří druhému vítězi); kap. XIX (urážka v nepřítomnosti) – začátek |
| 063r | 145 | XIX – urážku donesenou třetí osobou je nutno řešit, jinak mlčení = bázeň |
| 063v | 146 | konec XIX; kap. XX (co je horší: „paroháč“, nebo „zrádce“) |
| 064r | 147 | konec XX (zrada je nejhorší); kap. XXI (smí se odmítnout ten, kdo už jednou prohrál?) |
| 064v | 148 | konec XXI; kap. XXII (kapitán vyzvaný prostým vojákem) |
| 065r | 149 | konec XXII; kap. XXIII (šlechtic „de quattro quarti“ proti prostému muži; příklad Gaia Maria) |
| 065v | 150 | konec XXIII; kap. XXIIII (kdy lze namalovat na hanbu toho, kdo neodpoví – tři listy, šest měsíců); nadpis XXV |
| 066r | 151 | kap. XXV (malování zrádce); kap. XXVI (nedostavení k boji, objetí kolbiště za zvuku trub, omluvy) |
| 066v | 152 | konec XXVI (průkaz omluvy, lékařské osvědčení); kap. XXVII (smí se odmítnout ten, kdo byl už namalován) |
| 067r | 153 | konec XXVII; kap. XXVIII (dědí prvorozený syn vítěze zajatce?) |
| 067v | 154 | kap. XXIX (vyrovná políček slovní urážku?); kap. XXX (lze vyrovnat „zrádce/zbabělce“ slovy – omluvou) |
| 068r | 155 | konec XXX; kap. XXXI (nepřítel se z oprávněné příčiny nedostavil) |
| 068v | 156 | konec XXXI (náhrada výloh); kap. XXXII (urážka, kterou ze slušnosti nelze objasnit – čest žen) |
| 069r | 157 | konec XXXII; kap. XXXIII (donašeč a popření výroku) |
| 069v | 158 | konec XXXIII; kap. XXXIIII (kdo je urážen, když je donašeč odbyt jako lhář); začátek nadpisu XXXV |
| 070r | 159 | kap. XXXV (výzva s podmínkou zbraní – zbraně volí vyzvaný); nadpis XXXVI |
| 070v | 160 | kap. XXXVI (kdo namaluje jiného neprávem – bičování a cejch na každém místě) |
| 071r | 161 | konec XXXVI; závěrečné slovo autora hraběti; tiráž; registr archů (tabulka) |
| 071v | 162 | tiskařský znak Piera de Ravani (obrázek) |
| 072r | 163 | prázdný sken – neupraveno (viz výše) |

## Návaznost
- 060v (sken 140) je zatím prázdná (jiný agent). Její italský text končí „gran priuilegio, & diuina gratia hara lhuomo che
  cia-“; slovo „ciascuna“ jsem dal celé na 061r. Český začátek 061r: „každou špatně vykonanou věc [učinit], jako by se
  nebyla stala …“ – překladatel 060v by měl skončit např. „Velikou výsadu a Boží milost by měl člověk, kdyby mohl“.
- **064v/065r**: konec archu H má kustodu „re commune“ (konec 064v) – vynechána; slovo „hono-|re“ je celé na 065r.
- Nadpisy rozdělené přes stranu (061r/061v kap. XVII, 069v/070r kap. XXXV) jsou dva bloky `nadpis`, druhý s `pokracovani: true`.

## Nejistá čtení ze skenu (ověřeno výřezy)
- 064v nadpis „DESFIDA“ + dělicí znaménko + „da uno milite“ – patrně za „desfidato“ (poznámka).
- 065r „piu daniente“ – čtení jisté, smysl ne (tisková chyba? snad „conueniente“); „Capitato“ = tisková chyba za Capitano.
- 066r „eq̃parare“ = equiparare (q s přeškrtnutou dříkem = qui).
- 066v/067r „legitima ma-|tre sia poncella“.
- 064v „buone op̄e“ = opere.
- 070v „iustitia/tristitia“ – ligatura ti vypadá jako „n“ (iustina, tristina); přepsáno iustitia, tristitia. „in-|sano“.
- 071r „libret[to] bre[ue]mente“ – papír poškozen, doplněno v hranatých závorkách.
- 071r registr: první znak je stará číslice „1“ (úvodní arch).

## Sporná místa (IT – CS – proč)
- 061r „quello che harra donato doi ferite sia el perditore“ – „ten, kdo udělil dvě rány, je poražený“: nadpis mluví o
  tom, kdo dvě rány utržil (leuato); ponecháno podle tisku s poznámkou.
- 061v „& li dice par fare troppo che lentra … uenendo spontando“ – „dokonce mu říká – byť se to zdá přespříliš – …
  proti tomu, kdo přijíždí s napřaženým hrotem“: smysl odvozen.
- 062v „ha menato de alcuno atto chel fosse mancato per prima“ a „molte uendite ce la uenditione“ – nejasné, přeloženo
  podle smyslu (poznámky).
- 063v souvětí o „cornuto“ („una cosa che senne fa tanta stima piu che thesoro, e uita perche nol stima …“) – překlad
  podle patrného smyslu.
- 066r nadpis XXVI „un che si retrouera el di deputato“ – podle textu jde o toho, kdo se NEdostaví; přeloženo „[ne]dostaví“.
- 067r „& de doi primi sarebbe uenuto a morte che obligarse ad doi“ – „raději by hned napoprvé zemřel, než by se zavázal
  dvěma“: nejisté.
- 067r/068r „el bon triumpho … gente di ferro, & de ualore armata“, „come el buon poeta dice“ – vykládáno jako citát
  z Petrarkových Triumfů; přesné místo jsem neověřil.
- 070r „desfida esser alemane con chi ne sera forse innocente“ – „esser a le mane“ = pustit se do křížku; přeloženo tak.

## Vyříznuté obrázky
- `knihy/della-valle-1528/obrazky/drevorez-162.jpg` – tiskařský znak (korunovaná siréna se dvěma ocasy), výřez
  1040,1035,1250,1520 ze skenu 162, zkontrolován (celý rám, bez textu).

## Návrhy do glosáře
| id | cs | italské tvary | kategorie | pozn |
|---|---|---|---|---|
| oltranza | na život a na smrt | ad tutta oltranza, a tutta oltranza, oltranza | pravo | Souboj „do krajnosti“, dokud se jeden nevzdá, nepadne nebo není vyhnán z kolbiště; opak souboje „per accordo“ (do smluveného počtu ran). |
| zajatec | zajatec | presone, prigione | pravo | Poražený, který se vzdal, se stává zajatcem vítěze (závazek listinou – instrumento). |
| listina | listina (závazek) | instrumento | pravo | Notářská listina, jíž se zajatec zavazuje vítězi; i jiné úřední listiny. |
| malovat-na-hanbu | namalovat na hanbu | depingere, pingere, depinto, depento, depingesse | pravo | Pittura infamante – veřejné hanlivé vyobrazení toho, kdo se nedostavil k souboji nebo zradil (titul knihy: „con lo pingere“). |
| urazka | urážka | iniuria, ingiuria, carrico, caricho, incarico, offesa, offensione | pravo | Urážka cti slovem nebo činem. |
| narceni | nařčení, pohana | taccia, pecco | pravo | |
| zbabelec | zbabělec | poltrone, codardo | pravo | |
| zradce | zrádce | traditore, tradimento | pravo | Podle kap. XX nejtěžší nařčení. |
| lhar | lhář | busardo, bosardo, busadro, mentitore | pravo | Doplnit k „mentita“; formule „mentire per la gola“ = lhát hrdlem. |
| donasec | donašeč | reportatore | pravo | Třetí osoba, která donese urážku (kap. XXXIII–XXXIIII). |
| spor | spor | querela, querella, querele, lite | pravo | |
| zadostiucineni | zadostiučinění | satisfactione, satisfattione | pravo | |
| valecnik | válečník | milite, militi, milite priuato | jednotky | Voják obecně; milite priuato = prostý válečník bez velitelské hodnosti. |
| valecne-remeslo | válečné řemeslo | militia | pravo | Vojenská služba a rytířský stav jako „řemeslo“. |
| bezpecny-pruvod | bezpečný průvod (glejt) | saluo condutto | pravo | |
| zastupce | zástupce v souboji | campione | pravo | Bojuje místo jiného (pán, žena, nemocný). |
| zavora | závora (kolbiště) | barra | pravo | Bariéra, za kterou se vjíždí do kolbiště. |
| sermirsky-mistr | šermířský mistr | maestro de scrimire | zbrane | |
| kolbiste (doplnit) | kolbiště | + campo, Campo | pravo | „Dare el campo“ = poskytnout kolbiště; „correre el campo a suon de trombe“ = objet kolbiště s trubači a vyhlásit nedostavení soka. |
| vyzyvatel/vyzvany (doplnit) | | + actore, desfidatore, recercatore / desfidato, recercato | pravo | Tisk střídá attore/actore. |
| gentilhomo-4-quarti | šlechtic o čtyřech předcích | gentilhomo de quattro quarti | pravo | Všichni čtyři prarodiče urození. |

## Osoby a místa pro rejstřík
- Gaius Marius z Arpina (Caio Mario Arpinate) – 065r.
- Francesco Petrarca („el buon poeta“, „el bon triumpho“) – 067r, 068r (nepřímo).
- Římští vojevůdci (Capitani Romani) obecně – 064r/064v.
- Enrico Pandone, hrabě z Venafra – oslovení „Excellentissimo S. mio“ – 071r.
- Piero de Ravani, tiskař – 071r, 071v; Benátky (Venetia) – 071r.
