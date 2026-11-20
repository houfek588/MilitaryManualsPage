# 2. revize – Devátá kniha, dávka A (skeny 617–637)

Dávka: `9-erb-solms`, `9-titul`, `9-001r` … `9-009r` (19 stran; Burgundský válečný řád – erb, titul, předmluva, list Filipa Klévského, úřady, ležení, pochodový řád). Sousedé `8-014v` a `9-009v` jen čteny, návaznost vět sedí (9-009r „…že nepřátelé jsou tak“ → 9-009v „silní…“).
Postup: všech 19 skenů staženo z BSB IIIF (1400 px, výřez titulního dřevořezu), `de` porovnáno se skenem řádek po řádku, `cs` blok po bloku s `de`. Všechny strany `stav: zkontrolovano`, `overeno_clovekem: false`.
Kontrola: `python -I nastroje/over_strany.py knihy/solms-1559 <19 id> --prisne` → **0 chyb, 1 varování** (9-002v *fein ordenlich* – ve skenu 624 skutečně *fein*, falešně pozitivní).

## Ověřeno ve skenech
- **617 (9-erb-solms)**: nápis nad dřevořezem zní *Reinhart der Elter Graue zu Solms/ vnd Herꝛ zu Müntzenberg/ꝛc.* – tvar **Müntzenberg** (s *ü* a *tz*) odpovídá tisku na této straně, přepis `de` je správný. Podoba *MINCZE[N]BORGK* je jen na nápisové stuze dřevořezu (správně uvedena v `popis`). Popis erbu (lvi v 1. a 4. poli, dělené münzenberské pole ve 2. a 3.) odpovídá skenu.
- **619 (9-titul)**: text titulu i rozdělení červeného/černého tisku ověřeno; ve výřezu dřevořezu dva putti u sloupů, nápisy *PLVS. – VLTRE*, orel s nimby a srdečním štítem – popis sedí.
- Iniciály *DIeweil* (621), *ALler* (623), *VNd* (624), *HErr* (631) potvrzeny.
- Hranice stran a kustody: *voln-|bracht* (624/625), *son-|der* (635/636), *zie-|hen* (636/637), kustody *sich, Nach-, gewalt, Alle, Item/, die, nach* – vše správně.
- Opravy překladatele (*an beiden zuuil*, *Rauenstein*, *jm der x. pfenning*, *vnd er die drit*, *Hetschier vnd gewarde*, *Arm-|brost schůß*, *(von den fünffhundert Knechten)*) ve skenu potvrzeny.
- **626**: *Blůtsuerwanden* → **Blůtßuerwanden** (tisk má *ß*).
- Tiskové chyby potvrzeny: *Marcle* (623), *möche ym* (625), *Feldauptman* (628), *Tresonier* (624), *Cliuier* (632), *Schlachtordmung*, *Vnb* (634), *darpffer* (637).
- 629: blok *Es ist auch von nöten daß jr einen Marschalck…* začíná na novém řádku bez odsazení; samostatný blok ponechán (změna tématu, předchozí řádek končí tečkou).

## Hlavní změny po stranách
- **9-erb-solms, 9-titul**: beze změn textu (jen stav).
- **9-001r**: úvodní souvětí – „dostal jsem také již před dlouhou dobou jeden válečný popis“ → „získal jsem už před dlouhou dobou i válečný popis“; *wann sie darbei odder mit im Feld sein werden* – „s nimi v poli“ (posunutý význam) → „s vojskem v poli“.
- **9-001v**: zdvojené „totiž“ – „nemá být nic tak milé – totiž peníze –“ → „si totiž nemá ničeho – zejména peněz – cenit natolik, aby…“.
- **9-002r**: odstraněno `{Marcle}` (vlastní jméno do `{}` nepatří, výklad je v poznámce); *vorab in allem* „a to zvláště ve všem“ → „natož ve všech“.
- **9-002v**: nadpis – vypuštěno přidané „na trůnu“ (*in seiner Maiestat sitzet* = „sedí ve svém majestátu“), doplněna tečka; rozkazovací „Předložte… sdělte…“ → „Máte jim předložit… sdělit…“ (shoda s *solt jhr*); „Mínili-li by však…“ → „Kdyby však váš rentmistr… mínili“.
- **9-003r**: *wann das Haupt jhnen nicht benant* → „Nebude-li jim hlava [vojska] předem jmenována“; „nedávejte jim o té věci nic slyšet“ → „nenechte je o té věci nic slyšet“.
- **9-003v**: *auch dieselbigen widerumb zu dem Christlichen glauben bringen* – „je opět přivedl“ (mylně vztaženo k dobyvatelům) → „ty [země a lidi] opět přivedl ke křesťanské víře“; `de` *Blůtßuerwanden*.
- **9-004r**: *wollust/ blůtuergiessung … anfechtungen* „rozkoše, krvežíznivosti … pokušení“ → „z rozmaru, pro krveprolití … pohnutek“.
- **9-004v**: „Jeho rozkazům se má pilně vyhovět jako vaší vlastní osobě“ → „…, jako by šlo o vás samého“.
- **9-005r**: „Týž maršálek má mít doktory práv“ → „Maršálek má mít při sobě doktory práv“; `{Veldhauptman}` → `{obersten Veldhauptman}` (shoda s glosářem).
- **9-005v**: *mit sampt den kundtschafften besichtige, damit er … dieselbigen außtheilen künde* – „vyslechl zprávy zvědů, aby je mohl rozdělit“ (*dieselbigen* = kvartýry) → „spolu se zvědy prohlédl celé položení terénu, aby mohl kvartýry rozdělit“; „aby to ten…“ → „aby to maršálek…“; *selbst hand anlegen … was anderst zun gerichts hendeln gehört* → „má sám zakročit, kde bude třeba, ve všem, co patří k soudním věcem“; `{Veldhauptmans}` → `{Obersten Veldhauptmans}`.
- **9-006r**: „smí jistě pokračovat“ → „smí ovšem pokračovat“; tečka v nadpisu.
- **9-006v**: „zdá se mi dobré, že čím dříve…“ → „mám za to, že čím dříve…“; `{Hetschier vnd gewarde}` rozděleno na „hartšíři {Hetschier} a garda {gewarde}“ (odkaz na heslo `hartsir`), poznámka zkrácena jen na *gewarde* (výklad hartšíře je v glosáři).
- **9-007r**: dvojí zápor „zabránit, aby se nikdo nevrhl… nevyplenil… nekradl“ → „zabránit, aby někdo vpadl…, vyplenil ji a kradl“; *wann mann leut also liederlich verleurt* „když se lidé lehkomyslně ztrácejí“ → „když se takto lehkomyslně přichází o lidi“.
- **9-007v**: zdvojené „podle toho … podle toho“ přestavěno: „a podle toho, zda je země otevřená, či úzká, má člověk umět pořádek změnit.[^1]“
- **9-008r**: *ein pferdt oder sechßzehen* – nejde o tiskovou chybu, ale o dobovou vazbu přibližného počtu („nějakých šestnáct“); „[deset] či šestnáct koní“ → „asi šestnáct koní“, poznámka 1 přepsána.
- **9-008v**: „o poslední stejně jako o první“ → „o poslední [oddíly]…“; „Když už tam stáli“ → „Když tam již odstáli“; *inn einer Ordnung ziehen, wie obstehet* „v jednom šiku“ → „v takovém pořádku, jak stojí výše“; `{vor}` → „v předvoji či zadním voji {vor odder nachzug}“.
- **9-009r**: nová poznámka k tiskové chybě *darpffer* (= *dapffer*).

## Sporná místa k rozhodnutí
1. **Oberst u Filipa Klévského** (9-004v *hat ein Oberster desto besser fug*, 9-005v *so der Oberst nit vorhanden*, 9-007v *wann der Oberst oder der Marschalck nicht vorhanden*) – podle závazného rozhodnutí „plukovník“; věcně jde o vrchního velitele (= *oberster Feldhauptman*). Na 9-005v to vede k nelogické větě („Není-li přítomen plukovník…, první je kníže“). Navrhuji zvážit výjimku pro 9. knihu („nejvyšší velitel“) nebo poznámku.
2. 9-004v *weder gab noch zeit ansehen* – „nehledět ani na dary, ani na čas“; *zeit* možná ve smyslu „neodkládat“; ponechána poznámka překladatele.
3. 9-005r *das drit theil des Hauptmans des hauffens sol auff jn warten* a *vber alle zalung … vff des Fürsten vnd seiner Trabenten noch ein Sold* – smysl nejistý, poznámky ponechány.
4. 9-008v *nemet drei odder vier dapfferer Mäner, die euch ein Wagenburg (von den fünffhundert Knechten) machen* – „tři nebo čtyři statečné muže“ je doslovné; možná vypadlo *hundert* (tři či čtyři sta z oněch pěti set). Ponecháno doslova.
5. 9-001r/9-001v nejasná místa (*wie er desselbigen gnůgsam außfürung zum ersten thůt*) a 9-003r (*wirdt on zweifel auch nicht vbel darzů rathen*) – výklad v poznámkách překladatele přijat.

## Návrhy do glosáře (glosář needitován)
| id | cs | de (doplnit) | kategorie | pozn |
|---|---|---|---|---|
| nejvyssi-polni-hejtman | nejvyšší polní hejtman | Obersten Veldhauptmans, Oberster Feldauptman | velitele | varianty z 9-004v, 9-005v |
| drabant | drabant | Trabenten | velitele | 9-005r |
| prusmyk | průsmyk / zemský průchod | päß, paß | sluzba | 9-005v, 9-008v (u řeky = přechod) |
| artikulni-list | artikulní list | Artickelßbriff, Artickeln | pravo | 9-004v |
| justice | justice (spravedlnost) | Justitiam | pravo | 9-004v, 9-005r |
| jizda | jízda | Reisigen zeug, reisigen Zeug | jednotky | 9-007v, 9-008v |
| rentmistr | rentmistr | Rentmeister | zold | správce panovníkových důchodů (návrh překladatele) |
| marsalek-ubytovani | maršálek ubytování | Veldmarschalck der Losierung, Losierung | velitele | franc. *maréchal des logis* (návrh překladatele) |
| hlavni-sik | hlavní šik / hlavní houf | Schlachtordnung (střední voj), gewaltiger hauff | jednotky | franc. *bataille* (návrh překladatele) |
| esplanada | esplanáda | Osplanade | opevneni | ital. *spianata* |
| vyjev | výjev | Historie, Historien | – | popisek miniatury rukopisné předlohy |

Heslo `hartsir` (Hetschier) již v glosáři existuje – návrh překladatele odpadá.
