# Zadání korektury – Niccolò Tartaglia, Quesiti et inventioni diverse (Benátky 1554)

Platí `PRAVIDLA_PREKLADU.md`, `zdroje/ZADANI_AGENTUM.md` (hlavně oddíl **ORIGINÁL JE ITALSKY**) a `kniha.yaml` →
`poznamky_k_prekladu`. Strany 1–154 jsou ve stavu `prelozeno` (přepis + překlad od sedmi překladatelů, zprávy
`zdroje/kontrola/preklad-A…G.md`). Cílem je **korektura překladu jako celku**: věrnost italskému originálu,
plynulost („středně“ – přirozený dialog, dobová zdvořilost) a jednotnost napříč knihou.

## Sjednocení napříč knihou (závazné)
- *Quesito* = **dotaz**; nadpis „Devátý dotaz, který položil …“ (úroveň 3, už sjednoceno). V textu „v sedmém dotazu“
  (ne „otázce“); název díla „Rozličné otázky a vynálezy“ zůstává. *Gionta* = Dodatek.
- Mluvčí tučně na začátku repliky: **Nicolò.**, **Převor.** (Gabriele Tadino, převor z Barletty), **Pan vévoda.**
  (Francesco Maria della Rovere), **Richard.** (Wentworth), **Pan Marcantonio.** (Morosini), **Hrabě Hieronimo.**,
  **Dělostřelec.**, **Ručničář.**, **Slévač.**, **Šikovatel.**; jinak „Pan + křestní jméno“ podle tisku.
- Oslovení: *Signor* = pan, *Vostra Signoria* = Vaše Milost, *Vostra Eccellenza* = Vaše Excelence, *Illustrissimo /
  Eccellentissimo* = nejosvícenější / nejvznešenější, *Magnifico* = urozený, *Clarissimo* = slovutný, *Maestà* = Veličenstvo.
- Dělostřelectvo: *bombardiero* = dělostřelec, *pezzo* = dělo, *mira (dauanti / de drio)* = (přední / zadní) mířidlo,
  *segno* = cíl, *linea visuale* = zorná čára, *transito / viaggio* = dráha, *brocca* = střed (cíle), *botta* = rána,
  *tiro* = výstřel / dostřel, *passata* = průraz, *bocca* = ústí, *foro / uacuo* = vývrt, *culatta* = závěr,
  *a livello* = vodorovně, *elevatione* = elevace, *ponto* (kvadrantu) = bod, *squadra* = kvadrant, *quadrante* = čtvrtkruh,
  *moto violente / naturale* = násilný / přirozený pohyb, *stroppaioni* = ucpávky, *inchiodare* = zatlouct.
- Šiky: *battaglia / squadrone / ordinanza* = šik, *quadra di gente / di terreno* = čtvercový co do mužstva / co do plochy,
  *fronte* = čelo, *cuneo* = klín, *forfice* = nůžky, *serra* = pila, *battaglia cornuta* = rohatý šik, *Sargente* = šikovatel.
- Měření: *bossolo* = buzola, *dioptra / trasguardo* = dioptra / průzor, *lancetta* = střelka, *calamita* = magnetovec,
  *policetta* = lístek, *scala* = měřítko, *uento* = vítr (směr; Tramontana – sever atd. ponech v závorce), *bacchetta* = tyčka.
- Opevnění: *baluardo / bastione* = bašta, *cortina* = kurtina, *caualliero* = kavalír, *forma piatta* = plochá bašta,
  *argine* = násep, *terrapieno* = val, *fossa* = příkop, *scarpa* = svah, *canonera* = střílna, *contraforte* = opěrný pilíř,
  *campagna* = předpolí.
- Geometrie (Eukleidés): *diffinitione* = definice, *suppositione* = předpoklad, *petitione* = postulát,
  *propositione* = věta, *radice quadrata* = druhá odmocnina.
- Míry: *passo* = krok, *piede* = stopa, *braccio* = loket, *dito* = prst, *libra* = libra, *oncia* = unce, *rotulo* = rotul.

## Na co se zaměřit
- Porovnej každý blok `cs` s italským `de` (posuny významu, zápory, kdo co říká, čísla, písmena bodů). Sporná čtení
  ověř ve skenu (návod v `ZADANI_AGENTUM.md`). Hranice stran: slovo rozdělené přes stranu patří na stranu, kde končí.
- Plynulost: rozhovor má znít přirozeně; rozděl přetížená souvětí, ale zachovej logiku důkazů a výpočtů.
- Termíny `{…}` v italské podobě z tisku jen při prvním výskytu na stránce; glosář `glosar.yaml` je závazný.
- Obrázky: soubory `obrazky/drevorez-*.jpg` už existují – otevři je a ověř, že `popis` odpovídá výřezu.
- Poznámky: zpřesnit, zbytečné vypustit, neopakovat glosář. Sporná místa ze zpráv překladatelů rozhodni, kde to jde.
- Neměň `overeno_clovekem` (zůstává `false`). Po kontrole `stav: zkontrolovano`. Ukládej stranu po straně.
- Na konci `python -I nastroje/over_strany.py knihy/tartaglia-1554 <tvoje strany> --prisne` (0 chyb) a zpráva
  `zdroje/kontrola/revize-<dávka>.md` (co jsi změnil, rozhodnutá a dál sporná místa, návrhy do glosáře).
