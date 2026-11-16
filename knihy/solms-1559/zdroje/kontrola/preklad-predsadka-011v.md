# Zpráva o překladu a revizi – Dávka 1 (`titul-svazek` až `011v`)

Kniha: `knihy/solms-1559` (Reinhard ze Solmsu, *Válečný popis a řád válečné správy*, 1559)
Zpracované strany (25): `titul-svazek`, `erb-solms`, `titul`, `titul-v`, `001r`, `001v`, `002r`, `002v`, `003r`, `003v`, `004r`, `004v`, `tab-01`, `006r`, `006v`, `007r`, `007v`, `008r`, `008v`, `009r`, `009v`, `010r`, `010v`, `011r`, `011v`.
Ověření `python -I nastroje/over_strany.py knihy/solms-1559 … --prisne`: **25 stran, 0 chyb, 0 varování**.

---

## 1. Přehled změn po stranách

- **`titul-svazek`** (sken 9): Ponechán hlavní nadpis `uroven: 1` (*Das erst Buch…*), opravena sazba nadpisu a doplněn odborný popis dřevořezu `drevorez-1.jpg` (císařský znak Karla V. s Herkulovými sloupy a devízou *PLVS. VLTRE*). Přidána poznámka `[^1]` k vymezení svazku.
- **`erb-solms`** (sken 90): Opravena zkomolenina OCR v záhlaví erbu (*Reinhart der Elter/ Graue zu Solms vnd Herr zu Müntzenburg/ etc.*), odstraněn chybně přepsaný text ze stuhy dřevořezu (*T.GRAFF… BORGY*), doplněn popis celostránkového dřevořezu `drevorez-090.jpg` se solmsko-münzenberským erbem na stromě a poznámka `[^1]` o autorovi.
- **`titul`** (sken 91): Doplněn vynechaný horní řádek `Das ander Buch.`, blok převeden na `nadpis` (`uroven: 1`), odstraněn falešný textový blok `PLVS VLTRE` vytažený z obrázku a doplněn chybějící blok `obrazek` (`soubor: drevorez-091.jpg`) podle `s091.jpg` s popisem. Doplněny poznámky k řadové číslovce *viervndzwentzigsten* (`[^1]`) a pěti jmenovaným císařským vojevůdcům (`[^2]`).
- **`titul-v`** (sken 92): Doplněn popis celostránkového dřevořezu `drevorez-092.jpg` (rytířský portrét velitele na zbrojním koni pod klenbou větví).
- **`001r`** (sken 93): Nadpis `Oberster Kriegsherr.` označen jako `uroven: 2`; doplněna ozdobná iniciála `EIn`; odstraněno záhlaví, číslo listu a signatura `a ij`; rozdělené slovo `bekenn-` na konci strany přesunuto celé (`bekennte`) na `001v`; přidána poznámka `[^1]` k tiskové podobě *notröstung*.
- **`001v`** (sken 94): První blok označen `pokracovani: true` se slovem `bekennte`; odstraněno záhlaví a kustod `chen` (`derglei-` z konce strany přesunuto celé jako `dergleichen` na `002r`).
- **`002r`** (sken 95): První blok `pokracovani: true` se slovem `dergleichen`; odstraněno chybně přepsané číslo `44` na konci bloku 3; přidána poznámka `[^1]` k tvaru *mosterung*.
- **`002v`** (sken 96): Slitý text rozdělen přesně dle tisku na **3 bloky** (1. `pokracovani: true`, 2. `Darumb soll der Kriegsherr…`, 3. `Wo aber ein Herr…`); odstraněno chybně připojené slovo z kustodu `Rath` na konci strany; přidána poznámka `[^1]` ke jménům Frundsberga a Marxe Sitticha z Emsu.
- **`003r`** (sken 97): Rozděleno dle tisku na **2 bloky** (1. `pokracovani: true`, 2. `Dann es ist wol zudencken…`); odstraněno zbloudilé číslo `3` na konci strany.
- **`003v`** (sken 98): Odstraněno přimíchané záhlaví `Dasander Buch` ze začátku prvního bloku; 1. blok `pokracovani: true`.
- **`004r`** (sken 99): Sloučený prostřední blok rozdělen přesně dle sazby tisku na **7 samostatných odstavců** (1. `pokracovani: true`, dále 5 samostatných pravidel o válečné kořisti a povinnostech pána, 7. nedokončený odstavec končící `oberste` bez kustodu `Feld-`). Přidány poznámky `[^1]` a `[^2]` k tiskařským odchylkám.
- **`004v`** (sken 100): Jediný slitý blok rozdělen přesně dle tisku na **5 odstavců** (1. `pokracovani: true`); odstraněn kustod `Anbrin-` na konci; přidána poznámka `[^1]` k obratu *mit nicht leidlich*.
- **`tab-01`** (sken 102): Prohlédnuta rozkládací tabule `tab-01.jpg` (Hans Döring, 1546) a doplněn podrobný popis porady pod stromem.
- **`006r`** (sken 103): Nadpis `Anbringen vnnd begern…` označen jako `uroven: 3`; doplněna ozdobná iniciála `IR` (*IR meine Kriegsräth…*); poslední dva články odděleny podle tisku (celkem 5 bloků); odstraněno číslo listu `6` na konci.
- **`006v`** (sken 104): První blok `pokracovani: true`; rozděleny úvodní odstavce článků 3–6 přesně podle tisku (celkem 7 bloků včetně `nadpis` `uroven: 3` *Rathschlag auff des Kriegsherrn…*); doplněna ozdobná iniciála `AV` (*AVff die vbergebene Artickel…*); odstraněno záhlaví a kustod `daß` (a vykřičník z OCR na konci).
- **`007r`** (sken 105): Rozděleno podle tisku na **4 odstavce** (1. `pokracovani: true`).
- **`007v`** (sken 106): Odstraněno přimíchané záhlaví `Dasander Buchy` z 1. bloku a samostatný blok kustodu `Auff` z konce strany; zachovány 2 odstavce.
- **`008r`** (sken 107): Ověřeny všechny 3 odstavce proti skenu `s107.jpg`.
- **`008v`** (sken 108): Dva slité bloky rozděleny podle sazby tisku na **5 odstavců** (1. `pokracovani: true`); rozdělené slovo `hauf-` na konci přesunuto celé (`hauffen`) na `009r`; přidány poznámky `[^1]` a `[^2]`.
- **`009r`** (sken 109): První blok `pokracovani: true` se slovem `hauffen`; odstraněna signatura archu (`b nij` → správně `b iiij`) z konce 4. bloku; přidána poznámka `[^1]` k výrazu *preyß sein*.
- **`009v`** (sken 110): První blok označen `pokracovani: true` (věta plynule navazuje bez tečky z `009r`: *…gůten bericht / annemen*).
- **`010r`** (sken 111): Odstavce rozděleny dle tisku na **6 bloků** (1. `pokracovani: true`); sjednoceno *Doppelsoldner* podle dlouhého `ſ` ve skenu; přidána poznámka `[^1]` k duplicitě *vnd vnd*.
- **`010v`** (sken 112): Odstavce rozděleny dle tisku na **5 bloků** (1. `pokracovani: true`); odstraněn chybně připsaný kustod `tag/` z konce posledního bloku.
- **`011r`** (sken 113): Odstraněn první blok tvořený záhlavím `Donbeschreibung der 24. Kriegsampter .`; 1. textový blok označen `pokracovani: true`; odstraněn kustod `Zum` z konce 5. bloku.
- **`011v`** (sken 114): Jediný slitý blok rozdělen dle sazby tisku na **7 samostatných odstavců**; ověřen přechod na `012r` (`…die allein auff sein` | `leib warten soll`, kustod `leib` vynechán); přidána poznámka `[^1]` k *buben* v trénu.

---

## 2. Významná ověřená OCR místa ze skenů

| Strana | Chyba OCR / starého přepisu | Skutečné znění ze skenu |
|---|---|---|
| `erb-solms` (`s090`) | `Mingenburg / x .` + text z dřevořezu | `Müntzenburg/ etc.` |
| `titul` (`s091`) | chybí `Das ander Bůch.`, `vierondzwengigsten`, `mig`, `Bet ... <`, `scliger gedecktnuß`, `Kriegsampter nach`, `PLVS VLTRE` | `Das ander Buch.`, `viervndzwentzigsten`, `mög`, `Bei ... (`, `seliger gedechtnuß)`, `Kriegsämpter noch`, dřevořez `drevorez-091.jpg` |
| `001r` (`s093`) | `In Oberster Kriegsher ?`, `Keysigen`, `gattnng`, `wreuil`, `Schiffsbrucken`, `fuff`, `aller` | `EIn Oberster Kriegsherr`, `Reysigen`, `gattung`, `wieuil`, `Schiffbrucken`, `fuß`, `alles` |
| `001v` (`s094`) | `drer`, `zwe`, `geschen`, `it weyß`, `on onordnung`, `einfach`, `oil`, `gont ... ch :`, `nut` | `drei`, `zwen`, `gesehen`, `nit weyß`, `vnd vnordnung`, `ein sach`, `vil`, `gönt ... ehr/`, `nit` |
| `002r` (`s095`) | `besexet`, `daber`, `mit bericht ist`, `ber sich`, `Policer`, `finant`, `Herasie` | `besetzt`, `dabei`, `nit bericht ist`, `bei sich`, `Policei`, `finantz`, `Herr sie` |
| `002v` (`s096`) | `Xitmeister`, `voil`, `willen`, `verzingerung`, `bese Hen`, `Rath` (kustod) | `Ritmeister`, `vil`, `wöllen`, `verringerung`, `besetzen`, (kustod vynechán) |
| `003r` (`s097`) | `jim fein amptzuuersehn ?`, `mit`, `eitt`, `geschicklichent`, `Herk` | `jm (sein ampt zuuersehn)`, `nit`, `ein`, `geschicklicheit`, `Hertz` |
| `003v` (`s098`) | `Dasander Buch`, `iwißt`, `owenlicher`, `focht`, `geho fam` | (záhlaví vynecháno), `wißt`, `ordenlicher`, `forcht`, `gehorsam` |
| `004r` (`s099`) | `Memonal`, `dzsich`, `crinnert`, `wut`, `memand`, `dret`, `nottürff iger` | `Memorial`, `daß sich`, `ein erinnert`, `wirt`, `niemand`, `drei`, `nottürfftiger` |
| `004v` (`s100`) | `ab zichen`, `vngand`, `geschukter`, `gehot`, `stårmen`, `vnodenlich` | `abziehen`, `vngnad`, `geschickter`, `gehört`, `stürmen`, `vnordenlich` |
| `006r` (`s103`) | `X meine Kriegsrath`, `fier`, `regtern`, `Kriegso : denung`, `zubungen`, `bertrawen`, `musierung` | `IR meine Kriegsräth`, `für`, `regiern`, `Kriegsordenung`, `zubringen`, `vertrawen`, `musterung` |
| `006v` (`s104`) | `Off die`, `Xom !`, `Prouiane herm`, `zu je`, `beuelhe !` | `AVff die`, `Röm.`, `Prouiant herrn`, `zu jm`, `beuelhe/` |
| `007r` (`s105`) | `Römus .`, `gangen`, `E.Xô`, `cum`, `onderncht`, `Echakung`, `darber` | `Römis.`, `gantzen`, `E. Rö.`, `eim`, `vnderricht`, `Schatzung`, `darbei` |
| `007v` (`s106`) | `Dasander Buchy`, `plak`, `mcht`, `were erivol`, `Commifz`/`Commift` | (záhlaví vynecháno), `platz`, `nicht`, `wer er wöl`, `Commiß` |
| `008r` (`s107`) | `nameledig`, `stick` | `name ledig`, `stück` |
| `008v` (`s108`) | `leilb`, `s fterherz`, `Odenung`, `int`, `wreuil`, `einader` | `leib`, `Musterherr`, `Ordnung`, `inn`, `wieuil`, `einander` |
| `009r` (`s109`) | `Keyssigen`, `weiger`, `Naicstat`, `eh ?`, `zusicht`, `Not , meister`, `haumpeman`, `b nij` | `Reyssigen`, `weniger`, `Maiestat`, `ehr`, `zusteht`, `Rotmeister`, `hauptman`, (signatura vynechána) |
| `009v` (`s110`) | `gebea`, `zuuo : kom , men`, `sete`, `emtpfahen` | `gebe.`, `zuuorkommen`, `seie`, `empfahen` |
| `010r` (`s111`) | `ſhren`, `misten`, `Doppelfoldner`, `wdlten`, `frgent`, `fer`, `Wache` | `jhren`, `müsten`, `Doppelsoldner`, `wölten`, `jrgent`, `sei`, `Wacht` |
| `010v` (`s112`) | `pm`, `mch2`, `Koffen`, `Artholeret`, `Xoß`, `tag/` (kustod) | `jm`, `mehr`, `Rossen`, `Artholerei`, `Roß`, (kustod vynechán) |
| `011r` (`s113`) | `Donbeschreibung...`, `täg`, `zuberatchschlagen`, `geheint`, `burch`, `mich` | (záhlaví vynecháno), `tag/`, `zuberathschlagen`, `geheim`, `durch`, `auch` |
| `011v` (`s114`) | `gansen`, `or fachen`, `prung`, `Hüren`, `einglichen`, `gluck` | `gantzen`, `vrsachen`, `jrrung`, `Hůren`, `eintzlichen`, `gluck` |

---

## 3. Sporná místa (DE + CS) k posouzení

1. **`titul`** (*viervndzwentzigsten Kriegßämpter*): Originál klade řadovou číslovku („čtyřiadvacátých“) namísto základní („dvaceti čtyř“). Ponecháno v `de`, v `cs` přeloženo srozumitelně „dvaceti čtyř“ s poznámkou `[^1]`.
2. **`001r`** (*notröstung*): Zjevný sazečský překlep za *Notrüstung* (potřebné vybavení a nářadí k dělostřelectvu). Ponecháno v `de`, přeloženo „potřebného vybavení[^1]“.
3. **`001v`** (*mit jhn reit werden*): Starý obrat (srov. *bereit / zu Rande werden*, vypořádat se s někým). Přeloženo „nikdo si s nimi neví rady“.
4. **`004r`** (*verwaltnug*, *Kriegsorgnung*, *ein erinnert*, *Poruiant*): Drobné sazečské přesmyčky ponechány v `de` a vysvětleny v poznámkách `[^1]` a `[^2]`.
5. **`004v`** (*vnd mit nicht leidlich … inn gefehrlicheit setzen*): Poněkud zkrácená či sazečsky porušená konstrukce ve smyslu *nicht leichtlich* / *nicht leidlich* („nikterak lehce“ / „nesluší se snadno“). Přeloženo „nikterak lehce[^1]“.
6. **`008v`** (*ein einen hauffen* a *beschehen*): Zřejmě sazečská kontaminace *in einen hauffen* („do jednoho houfu“ / „jeden houf za druhým“) a tvar *beschehen* za *besehen* („prohlédnout“). Ponecháno v `de` s poznámkami `[^1]` a `[^2]`.
7. **`010r`** (*jrer erfarung vnd vnd erbarkeit halben*): Zdvojené *vnd* přes přelom řádku; ponecháno v `de`, vysvětleno v poznámce `[^1]`.

---

## 4. Návrhy na doplnění `glosar.yaml`

### A) Nová hesla navrhovaná do glosáře
```yaml
- id: markytan
  cs: markytán
  de:
  - Marcatant
  - Marcatanten
  - Marcketenter
  kategorie: zold
  hledat:
  - markytán
  pozn: Táborový obchodník prodávající vojákům potraviny, nápoje a drobné zboží; podléhal dohledu a cenové kontrole profouse.

- id: bezpecny-pruvod
  cs: bezpečný průvod
  de:
  - Geleyt
  - geleit
  kategorie: sluzba
  hledat:
  - bezpečn\w* průvod
  pozn: Ochranný doprovod (eskorta) a záruka bezpečné cesty pro zásobovače a obchodníky přivážející proviant do ležení.
```

### B) Pravopisné a pádové varianty do stávajících hesel (výběr tvarů z 1. dávky)
- **`valecny-pan`**: přidat `Oberster Kriegsherr`
- **`plukovnik`**: přidat `Obersten`
- **`hejtman`**: přidat `Hauptleuten`
- **`valecny-rada`**: přidat `Kriegsräth`, `Kriegs Räth`, `Kriegsräthen`
- **`porucik`**: přidat `obersten Leutenant`
- **`rytmistr`**: přidat `Ritmeister`
- **`polni-marsalek`**: přidat `Feldmargschalck`
- **`dvojzoldner`**: přidat `Doppelsoldner`, `Doppelsoldnern`
- **`dvojity-zold`**: přidat `doppelnsold`, `Doppelsolds`
- **`trubac`**: přidat `Trummeter`, `Trummetter`
- **`hudba`**: přidat `Trummenschlager`, `Trummenschläger`
- **`puskar`**: přidat `Büchsenmeistern`
- **`delostrelectvo`**: přidat `Artholerei`
- **`munice`**: přidat `Municion`
- **`zold`**: přidat `Söld`, `besoldung`
- **`prijezdne`**: přidat `reitgelt`
- **`prehlidka`**: přidat `mosterung`, `muster Register`
- **`sluzebni-list`**: přidat `bestellbrieff`
- **`artikulni-list`**: přidat `Artickels Brieffen`
- **`proviant`**: přidat `Poruiant`
- **`proviantni-pan`**: přidat `Prouiant herrn`
- **`losament`**: přidat `Losamentern`
- **`maz`**: přidat `massen`
- **`prisaha`**: přidat `eydt`, `eyds`
- **`valecny-lid`**: přidat `Krigsuolck`, `Kriegsuolcks`, `Kriegsleuten`
- **`velitele`**: přidat `Beuelchßleuten`, `Befelhabern`, `beuelchs leut`
- **`sik`**: přidat `Ordenung`, `ordenung`, `geuierdte Ordnung`, `Schlachtordenung`, `hauffen`, `hauff`
- **`predvoj`**: přidat `fürzug`
- **`zadni-voj`**: přidat `nachzug`
- **`jizda`**: přidat `Reyssigen`, `Reisigen`
- **`rotni-druh`**: přidat `Rotgesellen`
- **`rota`**: přidat `Rot`
- **`poplach`**: přidat `lermen platz`
- **`vzpoura`**: přidat `meutereien`, `meuterei`
- **`utok`**: přidat `stürmen`
- **`pacholek`**: přidat `buben`
- **`vlasi`**: přidat `Welschs`
- **`rada`**: přidat `glieder`, `gliedsweiß`
