# Sporná místa a ediční poznámky – Solms (1559)

Přehled edičních rozhodnutí, foliace, terminologického sjednocení, revizí pracovního překladu i BSB OCR a zachovaných tiskových odchylek v Druhé knize Reinharda hraběte ze Solmsu (*Das ander Buch: Beschreibung der viervndzwentzigsten Kriegßämpter*, Lich 1559, sken BSB `bsb00085168`, sign. `Rar. 986`, `VD16 R 938`).

## 1. Rozsah a foliace

- **Rozsah edice**: celkem **158 stran** v `knihy/solms-1559/strany/` (všechny ve stavu `zkontrolovano`, `overeno_clovekem: false`), zahrnujících hlavní titulní list celého svazku (`titul-svazek`, sken `9`) a kompletní Druhou knihu (skeny `90`–`248`, tj. předsádka `erb-solms`, `titul`, `titul-v`, rozkládací tabule `tab-01` a listy `001r`–`087v`).
- **Vynechané nepotištěné stránky**: sken `101` (prázdný líc před rozkládací tabulí `tab-01` na skenu `102`) a sken `215` (prázdný líc před celostránkovým dřevořezem rubu `070v` na skenu `216`).
- **Přeskočená čísla listů v řadě edice a v tisku**:
  - `5` – místo listu 5 je vložena rozkládací tabule (`tab-01`, sken `102`).
  - `30` / `31` – v řadě ID souborů chybí `030r`/`030v`; na skenu `151` (ID `031r`, `list: '31'`) tisk uvádí číslo listu `30` a následující list `032r` (sken `153`) má číslo `32`, takže v samotném tisku je přeskočeno číslo `31`, zatímco edice zachovává identifikátory `031r`/`031v` pro plynulou posloupnost mezi `29` a `32`.
  - `33`, `47`, `51`, `56`, `58`, `63`, `68`, `70r` (dochován jen rub `070v`), `77` – čísla vynechaná v tisku (často na rozhraní složek či oddílů); text i kustody plynule navazují (např. nedokončená věta na konci `067v` přechází k novému oddílu na `069r`).
- **Chybně tištěná čísla listů v originále**: `29` tištěno jako `27`, `31` (sken `151`) tištěno jako `30`, `41` tištěno jako `42`, `81` tištěno jako `82`.

## 2. Sjednocená terminologie s Fronspergerem (1564) a nová hesla

Terminologie byla sjednocena s `knihy/fronsberger-1564/glosar.yaml` a doplněna v `knihy/solms-1559/glosar.yaml` na celkem **373 hesel** (všech 100 % `{Termín}` odkazů v českém textu je napojeno bez kolizí):

- **Páteřní vojenské úřady a pojmy (podle Fronspergera a glosáře projektu)**:
  - *Prouoß / Profoß* → `profous` (místo dřívějšího „probošt“ v pracovním `.md`), *Steckenknecht* → `profousův pacholek`, *Wachtmeister* → `vachmistr` (nikoli „strážmistr“), *Quartiermeister* → `kvartýrmistr` (nikoli „kvartýrmajstr“), *Hurnweibel* → `šikovatel trénu`, *Fendlin* → `praporec` (u pěchoty; *Fahne* → `korouhev`), *Spieß* → `píka`, *Schlange / Notschlange / halbe Schlange* → `kulverina` / `těžká kulverina` / `poloviční kulverina`, *Polwerck / Bollwerck* → `bolverk` (oproti *Bastey / Paßtheien* → `bašta`).
  - V hesle `pechota` byly odstraněny obecné tvary `Knecht` a `Knechten`, aby se tagy `{Knecht}` / `{Knechten}` správně napojovaly na heslo `knecht`.
- **Nová a Solmsova specifická hesla doplněná do `glosar.yaml`**:
  - Úřady a složky: `kapitan-justice` (*Capitan der Justitien*), `verejny-rad` (*Gemein Regiment*, *Pollicei*), `brantmeister` (*Brantmeister* – výpalný mistr), `brenfanen` (*Brenfanen* – paličský praporec), `beutmeister` (*Beutmeister* – mistr kořisti), `futerhauptman` (*Futerhauptman* – pícovací hejtman), `rumormistr` (*Rhumormeister*), `nejvyssi-velitel-jizdy` (*Oberster vber die Reutter*), `nejvyssi-vachmistr` (*Oberster Wachtmeister*), `nejvyssi-porucik` (*Oberster Leutenant*), `podmarsalek` (*Vntermarschalck*), `podzbrojmistr` (*Vnterzeugmeister*), `prehlidkovy-mistr` (*Mustermeister*), `polni-lekar` (*Feldartzet*), `osobni-lekar` (*Leibartzet*), `nizsi-sikovatele` (*Vnter Befelchsleut* a *Weibels Weibeln* na `074r`), `dozorce` (*Regierer*).
  - Ostatní pojmy a míry: `markytan` (*Marckenter* / *Marcatanten*), `glejt` (*Geleidt*, *Compaßbriff*; *Paßport* ponechán v `pruvodni-list`), `bezpecny-pruvod` (*Sicherung*, *Tröstung*), `vysunuty-zlom` (*Schnepfen*, *kropffung*), `spice-siku` (*Spitzen*), `jizdni-pacholek` (*Reisiger Knecht*), `zakopnik` (*Schantzgraber*; latinizující *Quastitor* připojen k `sancir`), `nevestky-a-chlapci` (*Huren vnd Buben*), `traskavy-ohen` (*Schlagfewr*), `achtel` (*Achtel*), `merice` (*Metzen*), `sah` (*Klafftern*), `ctvrt` (*viertel*), `pice` (*Füterung*), `reznik` (*Metzler*), `pobuda` (*Meutzkopff*).

## 3. Hlavní opravy pracovního překladu (`064r`–`087v`) a BSB OCR

- **Doplnění výpadků BSB OCR podle stažených skenů**:
  - `038r` (sken `163`), `039r` (sken `165`): doplněny zlomky `½` vypadlé v OCR (`132½.` achtelu, `1½ Centner` u krávy).
  - `039v` (sken `166`): doplněn celý řádek tabulky `Neun Schaaff.` vynechaný v OCR (obě strany tabulky pak součtem dávají přesně 3000 liber = 30 centů).
  - `040r` (sken `167`): doplněna položka `35 Ochsen` vynechaná v OCR.
- **Revize předpřipraveného překladu ze souboru `Solms/...md` (`064r`–`087v`)**:
  - Terminologická a věcná revize: např. „probošt“ → `profous`, „dráb“ → `profousův pacholek`, „strážmistr“ → `vachmistr`, „kvartýrmajstr“ → `kvartýrmistr`, „korouhev“ (u pěších *Fendlin*) → `praporec`, oddíl `074r` *Von Weibels Weibeln* (v pracovním `.md` mylně nadepsán „O rotmistrech“) opraven na `O nižších šikovatelích {Weibels Weibeln}`.
  - Struktura tisku: dvousloupcový rozpis žoldů plukovního štábu na `064r` byl srovnán podle skenu `205` po sloupcích za sebou.
  - Švy dávek a syntax tagů: vyhlazen přechod věty přes hranici dávek `035v → 036r` (`pokracovani: true`), na `028v` upraven složený tag `{doppel / einfach / halb hacken}` → `{doppel hacken}` a na `046v` odstraněna tečka z `{Meiln.}` → `{Meiln}`.

## 4. Zachované tiskové a početní chyby originálu (1559)

Německý text `de` ponechává dobové chyby tisku věrně podle skenů BSB a upozorňuje na ně v poznámkách překladatele:

- **Tiskařské přesmyčky a překlepy v textu**:
  - `001r`: *notröstung* za *Notrüstung*; `004r`: *verwaltnug*, *Kriegsorgnung*, *Poruiant*; `008v`: zdvojené *ein einen hauffen* a *beschehen* za *besehen*; `010r`: zdvojené *vnd vnd*; `016r`: zkrácené *der Ober* za *der Oberst*; `021v`: *Feldhaupt* za *Feldhauptman*.
  - `026r`: *Wahtmeister*; `028r`: věcný omyl tisku *des Schantzmeisters* místo *des Zeugmeisters* a spojení *von jnen lassen* místo *von jnen lösen*; `035v`: *Kregsherr*; `036v`, `038v`: *gerodnet* za *geordnet*; `044r`: *Prouinatherr*; `043r`: zdvojené *die die* a problematické *nicht gerechnet* (za *mit gerechnet*?); `045v`: vypadlé slovo za *an der [Lände?] vnd desselben Fleckens*; `046r`: *greydt*, *gewich* a chybný zápor *kein durchaus abwechselung*.
  - `050v`: *gegen dem fein* za *Feind* (hlášeno též jako jediné varování kontrolního skriptu `over_strany.py --prisne`) a dvakrát *gegen den Freünden*; `052r`: *Büchen* za *Büchsen*, *Wabenburg* za *Wagenburg*; `057r`, `059r`, `059v`, `060v`: *Feldmarschack*, *vrsch*, *Feldhaumans*, *Hautptman*.
  - `065r`, `066r`, `086v`: *Obest*, *Obester*, *Obensten* za *Oberst(er/en)*; `072r`: *Kencht* za *Knecht*; `078r`: *Scharpffrichrer*, *weinger* za *weniger*; `078v`, `079v`: *ambs*, *Schimdt*, *Fecken*, *Manot*; `082v`: zdvojené *die die*; `083r`, `084v`: *nottufft warden*, *gründtlch*; `087r`: osamocené záhlaví *Hauptleut.* pod nadpisem a dřevořezová iniciála *W* vsazená místo *E* před *S sollen* (*ES sollen*); `087v`: *am Gerich* bez koncového *t*.
- **Početní chyby v tabulkách komisu (`037r`–`041v`, `046v`)**:
  - `037r`: vytištěno `2500` chlebů místo `3500` (dobový čtenář na okraj rukou připsal `35` a `dreißig`) a `1066` achtelů místo `1666`; `037v`: `drei Metzen` místo `sechs Metzen`.
  - `040r`–`040v`: tiskové omyly v počtech zvířat a centů (`40` ovcí místo `14`, `370` centů místo `350`, `130` skopců místo `35`, `130 Shaaff` místo `140`, v měsíční tabulce `1315` telat místo `1350`, `280` skopců a `413` ovcí přeneseno z týdenní tabulky, `Fünff Schaaff` místo `Fünfftzehen Schaaff`).
  - `041v`: `dreissig drei` (33) korců místo `83` a `1 500 000` měřic místo `150 000`; `046v`: údaj `ein pfundt` chleba u počtu `28 000` osob, jenž odpovídá dvouliberovým bochníkům.
