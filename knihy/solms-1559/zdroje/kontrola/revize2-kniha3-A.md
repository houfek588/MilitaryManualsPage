# 2. revize – Solms 1559, dávka „kniha3-A“ (`3-erb-solms`, `3-titul`, `3-titul-v`, `3-001r`–`3-013r`, skeny 250–277)

Revize podle `zdroje/ZADANI_REVIZE2.md` (plynulost „středně“, Oberst = plukovník, Kriegßleut = válečníci, Justitien = spravedlnost).
Struktura bloků, `sken`, `id`, `stav: zkontrolovano` a `overeno_clovekem: false` jsou beze změny. Sousedy `087v` a `3-013v` jsem jen četl;
`3-013v` mezitím upravila jiná dávka, návaznost `3-013r` → `3-013v` („nechají | vozy jet vedle šiku“) sedí.

Ověření: `python -I nastroje/over_strany.py knihy/solms-1559 3-erb-solms 3-titul 3-titul-v 3-001r … 3-013r --prisne`
→ **28 stran, 0 chyb, 0 varování**.

Postup: všechny bloky `cs` jsem porovnal s `de`. `de` jsem strojově porovnal s OCR (`zdroje/ocr_bsb/0253–0277.txt`).
Sporná místa jsem ověřil ve skenech BSB IIIF (`bsb00085168_00255`, `_00260`, `_00262`, `_00263`, `_00264`, `_00275`;
u s. 255 i výřezy z verze o šířce 2800 px).

## 1. Opravy originálu (`de`) podle skenu

Předchozí kontrola na několika místech „opravila“ tisk:

| Strana | Bylo | Nyní (podle skenu) | Pozn. |
|---|---|---|---|
| `3-002r` | `verordneter stundt` | `verordneter stůndt` | tisk má *ů* |
| `3-002r` | `zu lernen` | `zu lermen` | tisková chyba za *lernen*; vysvětleno ve sloučené pozn. 1 |
| `3-005v` | `beschrieben` (3×) | `beschriben` | tisk všude *beschriben* |
| `3-006r` | `sol ein Zeugmeister sehn` | `sol ein Zeugmeisten[^4] sehn` | tisková chyba, nová pozn. 4 |
| `3-006v` | `er wöl aber in dem vngefahrt sein` | `er wol aber …` | tisk *wol* (stejně jako o řádek výš *wol er das*) |

Ve skenu potvrzeno a ponecháno: `in 5. theil … das wern 20. person einen Rotmeister` (`3-006r`, s. 263), `quastitores vber schantzer`,
`des Feurwerck` v 9. bodě (`3-004v`, s. 260), `glaubhafftig` 2× v bodech 2 a 3, `Oberkeit` 2× (`3-006v`, s. 264), `außgerich`,
`vngesichlichkeit`, `Rahthschlag`, `nicht bekeñt` (`3-002r`), `es kompt anders das geschütz … gegen den freunden zu streichen`,
`halb Falconetlin`, `dücken` (`3-012r`, s. 275).

Formální nejednotnost: od `3-010r` do `3-031v` mají strany Třetí knihy virgule se mezerou (`wirt / er`), dříve bez mezery (`wirt/ er`).
Neměnil jsem to, protože by úprava jen v této dávce byla nejednotná se sousedními stranami. Navrhuji to sjednotit skriptem v celé knize.

## 2. Hlavní změny překladu po stranách

- **`3-erb-solms`**: pozn. 1 „polní maršál“ → „polní maršálek“ (podle glosáře).
- **`3-titul`**: „ke střelnému prachu pro děla i ručnice“ → „ke střelnému prachu“ (*Büchsen Puluer* = střelný prach, „pro děla i ručnice“ bylo přidáno); „mocná“ → „účinná“.
- **`3-001r`**: úvodní anakolut *DIeweil …* jsem převedl na oznamovací větu a rozdělil ho na 3 věty. „přistoupit k činu“ → „věc skutkem provést“. Odstavec *Zum andern* rozdělen; „velkých děl“ → „velké dělostřelectvo“ (*ein groß Geschütz*); „velení“ → „povinnosti“ (*Beuelch*). *darzů im Zeughauß* jsem přeložil jako „která k nim patří, ve zbrojnici“ místo „[co náleží] do zbrojnice“. *gerißnen Figurn*: „vyrytými obrazy“ → „nakreslenými obrazy“ (*reißen* = kreslit, rýsovat; shoda se `3-011r`).
- **`3-001v`**: dlouhé souvětí o „polovině houfu“ rozděleno: „ke které straně se přiklonit“ → „ke které straně by bylo lépe se přidat“, „tamti“ → „protivníci“; *nit vil gepraucht* „vycvičení“ → „zkušení“. Konec strany přepsán na „ať každý den koná radu a všechny své“; návaznost na `3-002r` upravena.
- **`3-002r`**: navazující věta „velitele povolává do rady … pak jim má předložit k poradě nějaký případ, ať je jakýkoli“. *sie sehen das villerlei leut nicht bekent*: „rozliční lidé nejsou spolehliví“ → „všelijaké lidi nelze dobře znát“. *vngesichlichkeit*: „nešikovnosti“ → „nepřístojnostem“. *ist es aber an jm nit angenem*: „není-li to při něm vítáno“ → „Nemá-li v tom však zalíbení“. Pasáž o dobré povaze jsem rozdělil do vět. Poznámka 1 sjednocuje tři tiskové chyby odstavce.
- **`3-002v`**: „nenechat je z toho vyjít, pokud to pro jiné záležitosti může být“ → „nepouštět je z toho, pokud to jiné záležitosti dovolí“; „jak má jednoho před druhým ctít nebo mu velet“ → „koho má ctít víc než druhého a komu co svěřit“. Opravena časová souslednost („pozná … učiní dobře“). Novotvar „spoluporadívá“ jsem nahradil. „A nemůže minout, že …“ → „A nemůže to být jinak, než že …“.
- **`3-003r`**: „vedl podnik stran proviantu“ → „podnikl něco s proviantem“; „od správců“ → „od svých představených“ (*Regenten*). „v návyku [válečné] školy – tak je to chvalitebné a čestné o tom vyprávět“ → „držet ve [válečné] škole. To se o něm pak vypráví ke chvále a cti“. „drží dobrou spravedlnost“ → „dbají dobré spravedlnosti {Justitien}“.
- **`3-003v`**: „veliké knížata“ → „veliká knížata“ (shoda rodu). „jeho nejvyšší potřeba“ → „jeho naléhavá potřeba“ (vztaženo k dělostřelectvu). Zmatená věta o lidech a dělech je přepsána („nemohou ta děla vytvořit ani vycvičit lidi tak, jako lidé dovedou děla zhotovit a užívat“).
- **`3-004r`**: „má být prostřednictvím zmíněné osoby spoluporaděno“ → „se má radit i se zmíněnou osobou“; „dokud to nemá být zjevné a není třeba udeřit“ → „dokud věc nemusí vyjít najevo a není třeba přikročit k činu“; „co stojí“ → „kolik stojí“. V podnadpisu je „velení“ nahrazeno slovem „povinnosti“.
- **`3-004v`**: bod 4 jsem opravil podle smyslu: „leč by nutnost vyžadovala, aby byl přísný“ → „vyžaduje-li to však nutnost, má být přísný“; „učí tam, kde vidí, že je to dobře uloženo“ → „učit ty, u nichž vidí, že je to dobře vynaloženo a že si to zapamatují“. U bodu 5 „válečný zvyk“ → „válečné obyčeje“. **Věcná oprava** bodu 13: „aby nemířila do stráže ani přes poplachové místo do ležení“ → „aby ze stráže ani z poplachového místa nemířila do ležení“.
- **`3-005r`**: **věcná oprava** bodu 17. *der also zu seinen pferden vnd seiner gesellen ein nimpt*: „jenž se takto přibírá ke svým koním“ → „který tak zabere [kvartýr] pro své koně i pro koně svých druhů“. Sloveso *einnemen* je užito jako v bodě 16; pozn. 1 je přepsána. „vozkovského pacholka“ → „vozového pacholka {wagen Knecht}“.
- **`3-005v`**: dlouhé souvětí rozděleno („Mají se to totiž od něho naučit…“). *auff allen Amptern*: „na všech úřadech“ → „ve všech úřadech[^3]“, nová pozn. 3 (*Ampt* = správní okrsek, ne funkce). „z tohoto opatství“ → „z toho a toho opatství“.
- **`3-006r`**: *zubesolden vnd jm zu befelhen*: „má se mu svěřit velení“ → „mají se mu svěřovat úkoly“. Pozn. 2 (*in 5. theil*) je zpřesněna: obě možná čtení a ověření ve skenu. Nová pozn. 4 (*Zeugmeisten*).
- **`3-006v`**: nelogické „nemá sobě malou čest či zisk natolik oblíbit, aby skrze to neupadla v posměch“ → „nemá mu na malé cti či zisku příliš záležet, aby tím neupadl v posměch a hanbu“. *vngefahrt*: „zůstat bez úhony [nikoho neklamat]“ → „za to však ručit nemůže[^1]“, nová pozn. 1. Poznámky jsou přečíslovány (1 *vngefahrt*, 2 *Oberkeit*, 3 *außgerich*).
- **`3-007r`**: „kluci“ → „chlapci“ (*buben*). *in zügen verlegen*: „umisťovat na taženích“ → „vydržovat na taženích“ (*verlegen* = financovat). *beschreiben bei die Zeugmeister*: „přidělovat ke zbrojmistrům“ → „dávat je zapsat u zbrojmistrů“. *Ämptern vnd Pflegen*: „úřadech a panstvích“ → „úřadech a správách {Pflegen}“.
- **`3-007v`**: nadpis „Velení a správa poručíka.“ → „Povinnosti a správa poručíka“ (bez tečky jako v tisku).
- **`3-008r`**: nadpisy „Velení a úkoly šlechticů“ / „Velení puškařů“ → „Povinnosti …“ (*beuelch* u nevelících osob). *im landt die Ämpter befelhen zuuersehen mit dem geschütz*: „svěřit správu úřadů s děly“ → „svěřit, aby v zemi zaopatřovali úřady děly a zásobami“. *verschreiben*: „povolat“ → „písemně doporučit“.
- **`3-008v`**: „se dostatečně vyslechli velitelé“ → „bylo dostatečně pojednáno o velitelích“; souvětí rozděleno a doplněno „[děla]“.
- **`3-009r`**: „na něhož by ostatní hleděli a měli bázeň“ → „… a dbali ho“ (*sorg* ≠ bázeň). *demselbigen ists zu beuelhen*: „jemu se má velet“ → „tomu je třeba [děla] svěřit“ (byl obrácený význam).
- **`3-009v`**: zmatená věta o rozdělení děl v bitvě a o několika šancích je rozdělena; „jakémužto nebezpečí musí dostatečně čelit“ → „neboť je takovému nebezpečí vystaven víc než dost“.
- **`3-010r`**: navazující věta upravena („dal jim příklad pečlivosti, aby byli stejně svědomití, až se sami později dostanou k takové správě“). *in disem spil*: „v tomto válečném díle“ → „v této [válečné] hře“ (shoda s metaforou „hry“ na `3-001v`).
- **`3-010v`**: sjednoceno „žoky“ (dříve střídavě „žoky / pytle“ pro *Wolsecken / seck*).
- **`3-011r`**: **věcná oprava** *biß einn gůten Schůch an die Büchsen, daß die mit den Rorn darüber gehn*. Původně „až na dobrou stopu k dělům, aby nad nimi vyčnívala hlavněmi“, nyní „až asi na dobrou stopu pod děla, aby děla mířila hlavněmi přes násep“. *Quastitores*: „zákopníky“ → „kvastitory“ (shoda se `3-006r`).
- **`3-011v`**: „nechat jeho vůz dovézt“ → „nechat dovézt jeho vozy“; „mužů znalých války“ → „znalců válečnictví {Kriegsuerstendigen}“ (glosář).
- **`3-012r`**: **věcná oprava** *es kompt anders das geschütz in wendig der Wagenburgk gegen den freunden zu streichen*. Původně „ledaže by dělo stálo uvnitř vozové hradby“, nyní „jinak by dělo uvnitř vozové hradby střílelo směrem k vlastním lidem“. U „s ručnicemi“ jsem odstranil `{rorn}`, protože glosář vede *rorn* na „hlaveň“.
- **`3-012v`**: *in der ordnung des Wagenburgkmeisters*: „v šiku {ordnung}“ → „v sestavě určené mistrem vozové hradby“ (nejde o bitevní šik).
- **`3-013r`**: *in der Ordnung vnnd versehung*: „v šiku {Ordnung} a pod ochranou“ → „zařazené v pořadí a pod dohledem“. „aby zůstaly v šiku“ → „v pořádku“. `{ordnung}` jsem přesunul k prvnímu skutečnému „šiku“ („vedle šiku {ordnung}, či za šikem“).

Beze změny (prošlo kontrolou): `3-titul-v`, `3-007r` odst. 2–4, terminologie děl (falkonet, kulverina, kartouna se v této
dávce, kromě *halb Falconetlin*, nevyskytují).

## 3. Sporná místa k rozhodnutí

1. **`3-009r`** – *Wo aber ein Oberster/ als einer vom Adel vber jn ist/ den müssen sie dann achten* → „Kde však nad nimi stojí nějaký plukovník {Oberster} jakožto někdo ze šlechty“.
   Podle rozhodnutí z 2026-11-17 je ponecháno „plukovník“. Jde však o obecné „představený, nadřízený“ u jednoho oddílu děl, ne o hodnost; zvážit výjimku.
2. **`3-006v`** – *er wol aber in dem vngefahrt sein* → „za to však ručit nemůže[^1]“. Čtení podle právní formule *on gefärde* (bez ručení) je pravděpodobné, ne jisté.
3. **`3-006r` / `3-011r`** – *500 … in 5. theil / das wern 20. person einen Rotmeister*: tisk ověřen, nesrovnalost zůstává (25 rot po 20, nebo 5 oddílů po 100).
4. **`3-004v`** – 9. bod *des Feurwerck* (tisk ověřen): pravděpodobně omylem místo *Fuhrwerck*. Překlad zůstal věrný („ohňostroji[^2]“) s poznámkou; zvážit, zda nepřekládat podle smyslu.
5. **`3-003r`** – *muß das volck mit gelt vberhalten vnnd zalen* → „musí lid držet jen penězi a platit mu“; *vberhalten* může znamenat i „přeplácet“.
6. **`3-011v`**, pozn. 1 (rozpor s Druhou knihou `050r`, komu se svěřuje dělová vozba) – ponecháno, k ověření.

## 4. Návrhy do glosáře

| id | cs | de | kategorie | pozn |
|---|---|---|---|---|
| `sancir` (doplnění) | šancíř | + Quastitores, quastitores | osoby | Solms píše *Quastitores / Quastitorn / Quastores* (z it. *guastatori*); tvar *Quastitores* (`3-006r`, `3-011r`) chybí. |
| `velitele` (doplnění) | velitelé | + Befelchsleut | velitele | tvar ze `3-008v` |
| `mozdir` (doplnění) | moždíř | + Mörsern | delostrelectvo | tvar ze `3-001r` |
| `hlaven` (pozn.) | hlaveň | Rorn, rorn | delostrelectvo | Rozlišit: u děl *Rorn* = hlavně (`3-011r`), u střelců *Schützen mit rorn* = ručnice (`3-012r`). Navrhuji přidat *rorn* (u střelců) do hesla `rucnice`, nebo tvar vyřadit z `hlaven`. |
| `pflege` (nové) | správa (pflega) | Pflegen, Pflege | mista | Územní správní okrsek pod pflegerem, souběžně s *Ampt* (`3-007r`). |
| `urad-vojensky` (pozn.) | úřad | Ampt, Ampter | – | Doplnit význam „územní správní okrsek“ (`3-005v`, `3-007r`, `3-008r`), aby nebylo nutné psát poznámky na stranách. |
| `vozovy-pacholek` (nové) | vozový pacholek | wagen Knecht | osoby | Pacholek u vozu a koní šlechtice při dělostřelectvu (`3-005r`). |
| `ordnung` (pozn. k `sik`) | šik / pořadí | Ordnung | jednotky | U vozů (*in der Ordnung des Wagenburgmeisters*, `3-012v`, `3-013r`) znamená „pořadí, sestava vozů“, ne bitevní šik; poznámka v hesle by pomohla. |
