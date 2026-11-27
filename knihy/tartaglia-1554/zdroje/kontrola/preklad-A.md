# Překlad – dávka A (skeny 1–22: titul … 011v)

Všech 22 stran má `stav: prelozeno` a `overeno_clovekem: false`. `over_strany.py --prisne`: 0 chyb, 0 varování.
Každá strana byla porovnána se skenem (BSB, 1600 px, sporná místa ve výřezech).

## Obsah stran
- **titul** – titulní list: název, dodatek o nedobytném městě, „Con privilegio“, dřevořezový portrét autora (drevorez-1),
  „Appresso de l'auttore MDLIIII“.
- **001v** – souhrn obsahu devíti knih (každá kniha = jeden odstavec, odkaz na list).
- **002r–003v** – „Tavola“: podrobný obsah knih I–V jako `seznam` (položky jsou tak, jak jsou v tisku, čísla listů
  a dotazů ponechána; v `cs` je odkaz [[NNNr|listu N]] na líc uvedeného listu). Podnadpisy „El soggetto delli
  Quesiti del … libro“ jsou nadpisy úrovně 3. Kniha VI v tabulce chybí (i v tisku). Na 003v báseň „Alli lettori“
  (sonetto caudato, `verse`, 17 veršů).
- **004r–004v** – věnování Jindřichu VIII.: dotaz veronského dělostřelce (1531), Nova scientia (1537) kvůli
  Sulejmanově hrozbě, sbírka dotazů z autorova zápisníku, Richard Wentworth jako prostředník.
- **005r–007r** – kniha I, 1. dotaz (vévoda z Urbina, Benátky 1538): popis kvadrantu (12 bodů × 12 minut),
  elevace 0–6 bodů u děl, 7–12 u moždířů; dostřel roste do 6. bodu (45°); tabulka dostřelů z jediného výstřelu;
  vévoda chce zkoušku vidět po návratu z Pesara. Tři dřevořezy děl s kvadrantem (drevorez-11, 11b, 12).
- **007v–010v** – 2. dotaz: dělo na vrcholu kopce (vodorovně) × dělo na úpatí (zdvižené) proti pevnosti; důkaz
  z nauky o vahách (Jordanus, Archimédés): těleso vychýlené z „polohy rovnosti“ je „lehčí“, proto koule zdviženého
  děla letí déle „po přímce“; číselné příklady (200 × 800 kroků, 760/130, 600/150, 116 kroků podle Eukl. I.47).
  Obrázky drevorez-14, 16, 16b, 18.
- **010v–011v** – 3. dotaz: koule nikdy neletí dokonale po přímce (kromě svislice); důkaz půlením úseku a b
  do nekonečna. Obrázek drevorez-22 (dráha A–F–E–B–C–D). Konec 011v navazuje na 012r („tím činí“ | „svůj pohyb
  méně zakřiveným.“).

## Strukturní rozhodnutí
- Repliky jsou v tisku sázeny v jednom odstavci za sebou (DVCA. … NICOLO. … S. D. …); podle zadání je každá replika
  samostatný blok. Mluvčí: DVCA = **Vévoda.**, S. D. / S. DVCA = **Pan vévoda.**, N. / NICOLO = **Nicolò.**
- Mezititulky uvnitř dotazu („Diffinitione Prima“, „Suppositione Seconda“, 008v) jsou bloky `odstavec` s tučným
  `cs`, ne nadpisy (aby nezahlcovaly obsah; nadpis úrovně 2 by porušil hierarchii pod úrovní 3).
- Popisky pod dřevořezy (006r, 006v: „Pezzo aliuellato.“ …) jsou samostatné bloky `odstavec` před obrázkem.
- Označení bodů v tisku „.b.a.c.“ přepisuji v `de` jako „.b.a.c.“ (s tečkami), v `cs` „b a c“.
- Quesito = **dotaz** (sjednoceno s dávkami B–F; nadpisy „První dotaz {Quesito}, který položil …“). V názvu díla
  zůstává „Rozličné otázky a vynálezy“ podle kniha.yaml.

## Vady tisku a sporná místa
- **001v**: „Nel tertio … a car. 73“ – má být 37 (přehozené číslice), poznámka s odkazem na 037r.
- **002v**: „al Quesito. 29.“ – má být 19. **003v**: „a carte. 79. & 60.“ – má být 59 (třetí dotaz V. knihy je na 58v).
- **002r**: dvě sousední položky mají „al Quesito 11“ – tabulka délek děl je opravdu součástí 11. dotazu (17v–19r).
- **008r (sken 15)**: v záhlaví vytištěno číslo listu **7** místo 8 (list 7 číslován dvakrát); `list: '8'` ponecháno.
- **004r**: „Ma anchora sopra di nouo me hanno fatto …“ – věta je neúplná (vypadl předmět po „sopra“); v cs doplněno
  „o [jiných věcech]“ a vysvětleno poznámkou. Tamtéž nepárová závorka „… alto ingegno)“.
- **007r**: „accidtiē“ (rozepsáno „accidentie“) a „discaugarsi“ (patrně chyba za „discargarsi“ = vystřelit).
- **009r–009v**: body na svislici jsou v tisku označeny znaky **&, ꝯ, ꝝ** (došla písmena); ponechány v de i cs.
  Třetí znak čtu jako ꝝ (zkratka -rum) – ve skenu nejasný (může jít o jiný zkratkový znak); ověřit.
- **010v**: „circa à passa .140. auanti al termine“ – výpočtem má být asi 100 (200 − 100); ponecháno, poznámka.
- **005r**: „similiudine“ (tisková chyba), neuzavřená závorka; **010r** neuzavřená závorka „(come fu detto …“.
- **titul**: nápis na podstavci portrétu je ve skenu jen zčásti čitelný („… INVENTIONI SONO DIFFICILE MA … AGION…“);
  plné znění „LE INVENTIONI SONO DIFFICILE MA EL AGIONGERE È FACILE“ doplněno podle známé podoby portrétu – ověřit.
- **003v**: „quasi di che fattion, ouer autorita si uoglia“ – přeloženo „téměř jakékoli podoby či významu“; nejisté.
- **007r**: „ogni grosso bombardero“ – „grosso“ chápu jako neobratný, hrubý (ne „velký“).
- **008r**: „brazzi“ = ramena vah (ne loket) – záměrně bez {…}, aby se neodkazovalo na heslo loket.
- Pojem „tirar per linea retta“ překládám „střílet/letět po přímce“ (Tartagliova přímá část dráhy), vysvětleno v pozn.

## Ověřeno ve skenu (výřezy)
Čísla listů v souhrnu (001v) a v tabulce (002r–003v), iniciála „L“ věnování (LE Dimande), nápis portrétu,
„accidtiē … discaugarsi“ (007r), zkratkové znaky &, ꝯ, ꝝ a popisky obrazce (009r–009v), slovo „se-|condo“
přes hranici 009v/010r (celé na 010r), „que-|sta“ přes 011r/011v (celé na 011v).

## Návrhy do glosáře
| id | cs | de (it) | kategorie | pozn |
|---|---|---|---|---|
| dotaz | dotaz | quesito, quesiti | mereni (nebo nová „dilo“) | Quesito – otázka tazatele, jíž je uvozena každá kapitola; nadpisy „První dotaz, který položil …“. |
| ctvrtkruh | čtvrtkruh (stupnice kvadrantu) | quadrante | mereni | Vepsaný čtvrtkruh se stupnicí uvnitř kvadrantu (squadra); odlišit od celého přístroje. |
| minuta | minuta (kvadrantu) | minuto, minuti | mereni | 1/12 bodu; kvadrant má 144 minut, 72 minut = 45°. |
| olovnice | olovnice | perpendicolo, piombino | mereni | Nit se závažím zavěšená ve středu kvadrantu. |
| vodorovne | vodorovná poloha (děla) | aliuello, aliuellato, aliuellata, a liuello | delostrelectvo | Hlaveň vodorovně = nulová elevace, „poloha rovnosti“. |
| po-primce | (střelba) po přímce | linea retta, per linea retta, de mira | delostrelectvo | Přímý úsek dráhy střely; „tirar de mira“ = střelba po mířidlech. |
| prurazy | průraz | passata | delostrelectvo | (shodně s dávkou B) průbojnost střely v cíli. |
| poloha-rovnosti | poloha rovnosti | sito della equalita | mereni | Vodorovná poloha vahadla (Jordanus „situs aequalitatis“). |
| cara-smeru | čára směru | linea della direttione | mereni | Svislice, po níž těleso volně padá. |
| nasilny-pohyb | násilný pohyb | moto uiolente | delostrelectvo | Aristotelský pojem: pohyb vnucený vnější silou. |
| zatlouct | zatlouct / odzátkovat (dělo) | inchiodare / dischiodare | delostrelectvo | Vyřazení děla hřebem v zápalu a jeho zprovoznění. |
| klin, nuzky, pila | klín, nůžky, pila (šik) | cuneo, forfice, serra / segha | jednotky | Vegetiovské útvary (kniha IV). |
| zakopnik | zákopník | guastadori | jednotky | Pomocníci k zemním pracím. |
| tabulka-dostrelu | tabulka (dostřelů) | tauola | delostrelectvo | Tartagliova tabulka dostřelů pro všechny elevace. |
| nova-scientia | Nová věda | nuoua scientia, noua scientia | osoby (dílo) | Tartagliova Nova scientia (Benátky 1537). |

## Osoby a místa pro rejstřík
- Jindřich VIII., anglický král (věnování, 004r) – glosář `jindrich-viii`.
- Francesco Maria I. della Rovere, vévoda z Urbina (1. až 3. dotaz) – `vevoda-urbinsky`.
- Richard Wentworth („Ricardo Ventuorth“), anglický šlechtic, Tartagliův žák a kmotr; tazatel knihy V (004v).
- Sulejman I., turecký sultán („Soliman Imperator de Turchi“, 004r).
- Archimédés (O rovnováze rovin, 008r), Eukleidés (Základy I.47, 010v), Aristotelés (Mechanika, 001v),
  Platón, Plótínos (báseň 003v).
- Místa: Benátky (1538, 005r), Verona (1531, 004r; zkouška kolubriny 009v, 011r), Pesaro (007r), Rhodos (002v),
  Lido/„Lio“ (002v); Anglie, Francie, Irsko (titul věnování).
