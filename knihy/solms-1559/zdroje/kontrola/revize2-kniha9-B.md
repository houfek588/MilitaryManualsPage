# 2. revize – Solms 1559, dávka „kniha9-B“ (`9-009v` – `9-020r`, skeny 638–659, Burgundský válečný řád)

Revize podle `zdroje/ZADANI_REVIZE2.md` (plynulost „středně“, terminologie 2026-11-17, oddíl o knihách 6–9) a zprávy
překladatele `preklad-9-B.md`. Sousedé `9-009r` a `9-020v` jen čteni; návaznost přes hranice stran (`… der | massen`,
`… nach dem | essen`, `… drei oder vier tag | daruor`, `… nemlich | sechßzig`) sedí. Struktura bloků, `sken`, `id`
a `overeno_clovekem: false` beze změny; všech 22 stran má nyní `stav: zkontrolovano`.

Ověření: `python -I nastroje/over_strany.py knihy/solms-1559 9-009v … 9-020r --prisne` → **22 stran, 0 chyb, 0 varování**.

Skeny staženy z BSB IIIF (1400 px, u 650 i 2800 px s výřezy). Celé prohlédnuty skeny 638, 639, 640, 641, 647, 650, 652,
655, 657, 658, výřezy 650 a 659; u ostatních stran ponechány přepisy, které překladatel ověřil (bez podezřelých míst).

## 1. Opravy originálu (`de`) podle skenu

| Strana | Bylo | Nyní | Pozn. |
|---|---|---|---|
| `9-015v` | `zu zweien dingen` | `zu zweigen dingen` | tisk skutečně *zweigen* (výřez 2800 px) |
| `9-015v` | `lieber ober dann vnder der Statt` | `lieber vber dann vnder der Statt` | tisk *vber* |
| `9-015v` | `welches nicht sein mag weil sie ob der statt ist` | `… mag wenn sie ob der statt ist` | tisk *weñ* (= wenn); *weil* je správně jen dále u *alle zeit / weil vnd arbeit* (= Weile) |
| `9-020r` | `sechtzig oder sibentzig par` | `sechßzig oder sibentzig par` | tisk *sechßzig*, shodně s kustodou na 658 |

Ověřeno a ponecháno (tisk): `massen starck` bez spojovníku (638), `Herr dē artickel` (639), `sochs alles` (640),
`Scharwach`, `abtrettren` (641), `in der Satt weichen` (647), `redung` (650), `beschlossen`, `Culffer vnd Naplos`,
`jemmerlich` (652), `verbotten`, `Dopffelsolner`, `Hauptgůt` (655), `jrh dann sehet`, `sein jr kommen`, `bergig oder oben` (657),
`yr` v celé druhé polovině 658, `verziehe`, `ordnuug`→ponecháno `ordnung` (658: obrácené *n*, nejde o slovo), iniciála *AVch* (650).
Nadpis na 650 („Alhie soll ein Statt … gemalt werden“) je skutečně bez obrazu – blok `obrazek` se nedoplňuje.

## 2. Terminologie a věrnost (hlavní změny)

- `9-009v`: *Bůben* „pacholek/pacholky“ → **pachole / pacholata** (glosář `pacholek` = „pachole“); *Fendlin* velitele
  „korouhvička“ → **korouhev** (rozhodnutí: *Fendlin* u jízdy = korouhev); poznámka o *Hetschier* vypuštěna (opakovala
  glosář `hartsir`), poznámka k *laß fliehen* zkrácena (vypuštěn nesmyslný alternativní výklad), přečíslováno.
- `9-010r`: „Je také nutné, abych vám ukázal toto: když prohlížíte pole“ → „Musím vám také připomenout: zatímco prohlížíte pole“;
  *vom hauffen tringen* „zatlačit k vojsku“ → „zatlačit **od** vojska“ (význam).
- `9-010v`: *hübschlich abziehen* „pěkně v pořádku stáhnout“ → „opatrně stáhnout“.
- `9-011v`: *liederlich ein lermen* „z lehkomyslnosti poplach“ → „poplach pro nic za nic“; *durch verachtung versaumpt*
  „propást [nebezpečí] z lehkomyslnosti“ → „být z podcenění [nepřítele] zaskočen“; ohně „přímo naproti místu“ → „přímo před místem“.
- `9-012r`: *die leut zuuerhören* „lidi vyslýchat“ → „lidem dávat slyšení“; „ze stájí a vrat“ → „ze stájí a dveří“ (*Thürn*).
- `9-012v`: vazba „dává zrádci, zlými pacholky … házet“ → „nechává zrádce, zlé pacholky nebo malomocné ženy házet“;
  *gesind* „čeládka“ → **družina {gesind}** (jednotně s `9-020r`).
- `9-013r`: *durch die verechtlicheit des Herren … böß worden* „zlenivěli, protože jimi pán pohrdal“ → „pro pánovu lhostejnost
  zpustli“ (+ doplněna poznámka); *wann jhr es veracht hett* „zanedbali“ → „podcenili“; *daß sie es jhnen noch einmal anzeigen*
  chybně „nebo ať…“ → „a ať jim to oni sami ještě jednou zopakují“.
- `9-014r`: *was die grossen stück erschelt* „co velká děla rozbila“ → „co velká děla otřásla, to snadno povalí“.
- `9-014v`: odstraněn domyšlený doplněk „[nepřátelský] prach“ (smysl nejistý, vysvětluje poznámka).
- `9-015r`: *Wehrn* „náspy“ → „obranné stavby“ (jednotně s `9-014v`).
- `9-015v`: u *graben* (= podkop) odstraněna závorka `{graben}`, která odkazovala na heslo „příkop“.
- `9-016r`: *Ordnung* (střídání pracovních čet) „rozdělit do pořadí {Ordnung}“ → „rozdělit do směn“ (heslo šik nesedí).
- `9-016v`: vlastní jméno ze závorek ven („Neapole {Naplos}“ → „Neapole“, původní podoba v poznámce); „zapomněl ukázat“ → „zapomněl říci“;
  *vnder dem hauffen* „z houfu“ → „uprostřed houfu“; *im stürmen vnd anlauffen* „při útoku a výpadu na hradby“ → „při útoku a zteči“
  (výpad = akce obránců).
- `9-017r`: *zu rück schiessen oder schlagen* „zpětně střílet nebo bít do těch“ → „odrážet střelbou nebo zbraní ty, kdo slézají…“.
- `9-017v`: *gemeinen Knechten* „obecní knechti“ → „prostí knechti“ (obec = jiný pojem); *Kirch soll frei sein* „svobodný“ → „nedotknutelný“.
- `9-018r`: „Slíbil jsem vám také ukázat“ → „povědět“.
- `9-018v`: *Landen so der kelte vnderworffen* „zemích, které podléhají zimě“ → „které jsou vystaveny mrazu“.
- `9-019r`: „jak se s vámi výše uvedené okolnosti setkají“ → „které z výše uvedených okolností vás potkají“.
- `9-019v`: *so stelt euch vil manhaffter* „stavte se mužněji“ → „tvařte se mužněji“; *hawet mit den Feinden drein*
  „vražte s nepřítelem do sebe“ → „udeřte na nepřítele“.
- `9-020r`: *Spiesser* „kopiníci“ → **pikenýři** (jednotně s *Spieß* = píka).

Beze změny ponecháno (sedí s rozhodnutími): *Oberster* = plukovník (i `Obersten vber die scharwacht`, `derselbige Oberster`,
`der Oberst nit streittig`), *Marschalck / Veldmarschalck* = polní maršálek, *Kriegßleut* = válečníci, *Scharwacht* = obchůzka
s vysvětlující poznámkou na `9-010v`, *Polwerck/Bolwerck/Poluerck* = bolverk, *Pasteien* = bašty, *Fendlin* u pěchoty = praporec.

## 3. Sporná místa k rozhodnutí

1. **Scharwacht** (`9-010v`, `9-011r`, `9-012r`) – v burgundském řádu nehybná noční stráž po dvojicích kolem ležení,
   kterou obcházejí vachmistři; glosář „obchůzka“ (= pochůzková hlídka) sedí jen částečně. Ponecháno „obchůzka“ + poznámka;
   zvážit „noční stráž“ pro knihu 9.
2. `9-010v` *die redt* / `9-015v` *redung* – CS „pomoc“ (= *Rettung*); u 640 je možné i *Rede* (zpráva, rozkaz od velitele). Poznámky ponechány.
3. `9-014v` *damit das Puluer nit dareinn komme* – CS neutrálně „aby se tam nedostal prach“ + poznámka se dvěma výklady.
4. `9-018v` *wann der Oberst nit streittig ist / vnd die Leut in das Veld tringen will* – CS „není svéhlavý a nechce lidi nutit
   [zůstávat] v poli“; zápor u druhé části je domyšlen, smysl nejistý.
5. `9-009v` *laß fliehen* – CS „nechá ji vlát“ (*fliegen*), poznámka.
6. `9-012v` *Je-li [maršálek] na nebezpečném místě* – podmět *er* nejasný (maršálek / profous / vojsko); ponecháno.
7. `9-014r` pozn. 2 *es sei dann glück oder sonst ein gůter zufall* – výklad „leda by se cíle dosáhlo dříve“ ponechán.
8. `9-016v` *Culffer* – neurčeno.

## 4. Návrhy do glosáře (glosář needitován)

| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| dvojzoldner (doplnit tvar) | dvojžoldnéř | Dopffelsolner | jednotky | tvar z `9-018r` chybí v `de` hesla |
| srub (doplnit tvar) | srub | Polchhauß | opevneni | tvar z `9-014v` |
| druzina | družina | Gesind, gesind | jednotky | vlastní lidé velitele (šlechtici a jejich ozbrojenci), `9-012v`, `9-020r` |
| obranne-stavby | obranné stavby | Wehrn, Wehren | opevneni | obecně obranná zařízení hradby / ležení (`9-014r`, `9-015r`); odlišit od *Streichwehr* |
| zebrik | útočný žebřík | Leidern, Leiter | opevneni | `9-017r`, `9-017v` |
| mistr-strelby | mistr střelby | Schützmeister, schützenmeister | delostrelectvo | v burgundském řádu velitel baterie / puškař (`9-010r`, `9-014v`) |
| stredni-dela | střední děla | mittel stück, mitteln stücken | delostrelectvo | `9-014r` |
| hlavni-voj | hlavní voj | gewaltig hauff | jednotky | nyní tvar v hesle `sik`; v knize 9 jde o hlavní sílu vojska (`9-010r`) |
| ostep | oštěp | Scheffelein, Scheffeleinen | zbrane | krátké vrhací kopí, čtení nejisté (`9-020r`) |
| obchuzka (pozn.) | obchůzka | Scharwacht, Scharwach | sluzba | doplnit tvar *Scharwach* a poznámku o burgundské noční stráži po dvojicích |
| mimochodnik | mimochodník | Zelter, Zelterlin | sluzba | klidný kůň velitele (`9-009v`, `9-011r`) |
