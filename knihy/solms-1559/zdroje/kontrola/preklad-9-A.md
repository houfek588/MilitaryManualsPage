# Překlad 9-A – Burgundský válečný řád: erb, titul, předmluva a začátek řádu (skeny 617–637)

Dávka: `9-erb-solms`, `9-titul`, `9-001r` … `9-009r` (19 stran). Soused před dávkou `8-014v` (dosud kostra), za dávkou `9-009v` (hotová, návaznost ověřena).
Postup: OCR `zdroje/ocr_bsb/0617–0637.txt` porovnáno se skeny BSB (1600 px, sporná místa výřezem), přepis `de` opraven, přeloženo, `stav: prelozeno`, `overeno_clovekem: false`.
Kontrola: `python -I nastroje/over_strany.py knihy/solms-1559 <19 id> --prisne` → **0 chyb, 1 varování** (falešně pozitivní, viz níže).

## Přehled stran
| id | sken | obsah |
|---|---|---|
| 9-erb-solms | 617 | nápis *Reinhart der Elter…* + erbovní dřevořez (popis) |
| 9-titul | 619 | titul *Borgundische Kriegßordnung…* (uroven 1), autor Filip Klévský, císařský znak (popis), *Anno Domini M. D. Lix.* |
| 9-001r | 621 | nadpis *Vorrede diser Borgundischen Kriegsordnung* (uroven 2), Solmsova předmluva |
| 9-001v | 622 | předmluva – pět povinností rytíře (*Zum andern … Zum fünfften*) |
| 9-002r | 623 | věnovací list Filipa Klévského Karlovi (iniciála *ALler*), genealogie |
| 9-002v | 624 | konec listu; nadpis *Hie facht an ein Historien…* (uroven 3); o spravedlivé příčině války (iniciála *VNd*) |
| 9-003r–9-004r | 625–627 | rada, rentmistr, duchovní mimo radu, válka proti nevěřícím, pomoc přátelům, milosrdenství vítěze |
| 9-004v | 628 | artikulní listy, přísaha hejtmanů, moc nejvyššího polního hejtmana |
| 9-005r–9-005v | 629–630 | úřad polního maršálka, kvartýrmistra a profousa (soudnictví, zajatci, proviant) |
| 9-006r | 631 | profousova práva (jazyk, máz vína, oceňování); nadpis *Alhie facht sich an ein Historie…* (uroven 3); první ležení (iniciála *HErr*) |
| 9-006v | 632 | uspořádání ležení, trh a šibenice; Karel Smělý „nadmíru pracovitý“ |
| 9-007r–9-009r | 633–637 | pochodový řád: rejstřík služeb, předvoj/hlavní šik/zadní voj, přechod řek po mostech, hlídkové roty |

## Ověřená místa ze skenu (OCR → tisk)
- Iniciály doplněny: *DIeweil* (621), *ALler* (623), *VNd* (624), *HErr* (631).
- Hranice stran: kustos *bracht/* (624) – slovo *voln-|bracht* přesunuto celé na 9-003r; *son-|der* (635/636) → *sonder* na 9-008v; *zie-|hen* (636/637) → *ziehen* na 9-009r. Kustody *sich, Nach-, gewalt, Alle, Item/, die, nach* vynechány.
- 622 *an bet den zunul* → *an beiden zuuil*; *geli* → *gelt*; 623 *Xauenstein* → *Rauenstein*, *Marcle* ponecháno (tisková chyba); 624 *fein ordenlich* ověřeno výřezem – skutečně *fein* (varování over_strany je falešné).
- 629 *Lo-|sierung*, *Prouosen*; 630 *jm der x. pfenning* (OCR *jmder ra*); *vnd er die drit* (OCR *vnder die drit*); 632 *Hetschier vnd gewarde*, *der Cliuier von der Marck* (tisková chyba za *Oliuier*); 633 *glufen*, *Arm-|brost schůß*; 636 *(von den fünffhundert Knechten)* v závorce v tisku.
- Zkratky rozepsány: *eiñ/keiñ* → *einen/keinen*, *vñ* → *vnd*, *darīn* → *darinn*, *dē* → *dem*, *ꝛc.* → *etc.*
- Ponechané tiskové chyby (poznámka nebo zpráva): *Marcle* (623), *möche ym* (625), *Feldauptman* (628), *Tresonier* (624), *Cliuier* (632), *Schlachtordmung*, *Vnb* (634), *ein pferdt oder sechßzehen* (635), *darpffer* (637).
- 629: odstavec *Es ist auch von nöten daß jr einen Marschalck…* začíná na novém řádku bez odsazení (předchozí řádek plný, končí tečkou); kvůli změně tématu veden jako samostatný blok.

## Sporná místa (DE – CS – důvod)
1. 9-001v *wie er desselbigen gnůgsam außfürung zum ersten thůt* – „dokud ji nejprve dostatečně nezdůvodní“ – výklad podle kontextu (spravedlivá válka), poznámka.
2. 9-003r *wirdt on zweifel auch nicht vbel darzů rathen* – „bezpochyby také neporadí špatně“ – logika věty nejasná, poznámka.
3. 9-004v *weder gab noch zeit ansehen* – „nehledět ani na dary, ani na čas“ – *zeit* snad tisková chyba.
4. 9-005r *Veldmarschalck der Losierung den man auch ein quartirmeister heist* – rozloženo na tři úřady (maršálek vojska / maršálek ubytování = kvartýrmistr / maršálkův profous) podle francouzské předlohy; *das drit theil des Hauptmans des hauffens sol auff jn warten* – „třetina houfu vrchního hejtmana má být k jeho službám“ (nejspíš předvoj); *vber alle zalung … vff des Fürsten vnd seiner Trabenten noch ein Sold* – smysl nejistý.
5. 9-006r nadpis *ein beschlossens Landt* – „ohrazená země“, snad místo *Leger*.
6. 9-007r *auff die beut geschickt* – „vysláni napřed za kořistí“ (jízdní předvoj na výzvědy/výpad), poznámka.
7. 9-007v *zum meisten … zum letsten*, *die Ordnung wissen zu enden* (= *ändern*) – výklad v poznámce.
8. 9-008r *etliche auff Wasser* – snad *auff Fässer* (mosty na sudech).
9. *Oberst* (9-004v, 9-005v, 9-007v) přeloženo podle závazného pravidla „plukovník“, i když u Filipa jde zjevně o vrchního velitele (nejvyšší polní hejtman) – k rozhodnutí, zda zde neudělat výjimku.
10. *Historie / Historien* v nadpisech = „výjev“ (popisek miniatury rukopisné předlohy), uroven 3 – shodně s dávkou 9-B (*Alhie soll ein Statt … gemalt werden*).

## Terminologie (zvolená v dávce)
- *Marschalck* → „polní maršálek“ (první výskyt na stránce s `{Marschalck}`, dále „maršálek“); *Veldmarschalck* → polní maršálek.
- *Leutenant* → „poručík“ s poznámkou (zástupce panovníka, franc. *lieutenant général*); *Prouos/Prouoß* → profous; *Quartirmeister* → kvartýrmistr; *Furirer* → furýr; *Trabenten* → drabanti; *Büchsenmeister* → puškař.
- *Fendlin* (pěchota i jízda) → „korouhev či praporec“; *vorzug/nachzug* → předvoj/zadní voj; *Schlachtordnung* (střední voj) → hlavní šik; *streiffende Rot* → hlídková rota (shodně s 9-009v).
- *Falckenetlin/Falckenetlein* → falkonet; *Hacken* → hákovnice; *Spieß* → píka; *Artickelßbriff* → artikulní list; *Justitiam* → spravedlnost; *penlich/peinlich* → hrdelní / útrpně.
- *Rentmeister* → rentmistr; *Tresonier* → pokladník; *Hetschier* → hartšíř; *Landtschafft* (stavy) → zemské stavy, ale *Landtschafft* = krajina (9-008v) bez `{}`.

## Návrhy hesel do glosáře
| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| polni-marsalek (doplnit de) | polní maršálek | Marschalck, Marschalcks, marschalck des Velds | velitele | U Filipa Klévského *maréchal de l'ost* – vrchní soudce a velitel předvoje. |
| marsalek-ubytovani | maršálek ubytování | Veldmarschalck der Losierung, Losierung | velitele | Franc. *maréchal des logis*; v německém textu ztotožněn s kvartýrmistrem. |
| rentmistr | rentmistr | Rentmeister, Xentmeister | zold | Správce panovníkových důchodů, počítá náklady války. |
| hartsir | hartšíř | Hetschier, Hartschier | velitele | Jízdní tělesná stráž knížete (ital. *arciere*, franc. *archer*). |
| hlidkova-rota | hlídková rota | streiffende Rot, streiffende Pferdt | sluzba | Jízdní hlídka za zadním vojem / před předvojem. |
| hlavni-sik | hlavní šik | Schlachtordnung (mezi Vorzug a Nachzug), gewaltiger hauff | jednotky | Střední voj (franc. *bataille*). |
| esplanada | esplanáda | Osplanade | opevneni | Ital. *spianata* – zarovnaný volný prostor. |
| nabijeci-vuz | vůz s nabíjecím náčiním | Ladwagen | delostrelectvo | Vůz s nabíjecím nářadím u polních děl. |
| vyjev | výjev (obraz) | Historie, Historien | – | Popisek miniatury v rukopisné předloze Burgundského řádu. |
