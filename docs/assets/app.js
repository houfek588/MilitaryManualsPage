/* Edice vojenských manuálů – čtečka (statická, bez backendu; data v window.EDICE) */
(() => {
'use strict';
const E = window.EDICE, M = E.meta;
const $ = s => document.querySelector(s);
const OBSAH = $('#obsah');
const STAVY = {zkontrolovano:'zkontrolováno strojově', prelozeno:'přeloženo (čeká na kontrolu)', castecne:'částečně přeloženo', chybi_preklad:'bez překladu', chybi_original:'bez textu'};
const STAV_PORADI = ['zkontrolovano','prelozeno','castecne','chybi_preklad','chybi_original'];

// ---------- úložiště (nemusí být k dispozici)
const uloz = (k, v) => { try { localStorage.setItem('edice.' + k, JSON.stringify(v)); } catch (e) {} };
const nacti = (k, d) => { try { const v = localStorage.getItem('edice.' + k); return v === null ? d : JSON.parse(v); } catch (e) { return d; } };

// ---------- indexy
const ODD = E.oddily, STR = E.stranky, BL = E.bloky;
const oddil = {}; ODD.forEach((s, i) => { s.i = i; oddil[s.id] = s; s.deti = []; });
ODD.forEach(s => { if (s.rodic) oddil[s.rodic].deti.push(s); });
const strana = {}; STR.forEach((p, i) => { p.i = i; strana[p.id] = p; });
const heslo = {}; E.hesla.forEach(h => heslo[h.id] = h);
const normDe = s => s.toLowerCase().replace(/ſ/g,'s').replace(/[åä]/g,'a').replace(/ö/g,'o').replace(/[üů]/g,'u').replace(/ß/g,'ss').replace(/th/g,'t').replace(/ey/g,'ei').replace(/ff/g,'f').replace(/dt/g,'t').replace(/[^a-z]/g,'');
const bezDiakritiky = s => s.normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/ſ/g,'s').toLowerCase();

// ---------- pomocné
const esc = s => String(s ?? '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
const plain = v => v == null ? '' : Array.isArray(v) ? v.map(plain).join(' ') : String(v).replace(/\[\^\d+\]/g,'').replace(/\{([^}]*)\}\*?/g,'[$1]').replace(/[*_]/g,'');
const strop = (s, n) => s.length > n ? s.slice(0, n - 1) + '…' : s;
const folio = p => p.list && /^[IVXLC]+$/.test(p.list) ? `fol. ${p.list} ${p.strana === 'verso' ? 'v' : 'r'}` : (p.list || p.id);
const folioDlouze = p => p.list && /^[IVXLC]+$/.test(p.list) ? `list ${p.list}, ${p.strana === 'verso' ? 'rub (verso)' : 'líc (recto)'}` : (p.list || p.id);
const skenUrl = p => M.sken.url_strana.replace('{sken}', p.sken);
const skenObr = (p, w) => M.sken.url_obrazek.replace('{sken5}', String(p.sken).padStart(5, '0')).replace('{sirka}', w);
const hlavniOddil = s => { while (s && s.rodic) s = oddil[s.rodic]; return s; };
const cestaOddilu = s => { const c = []; while (s) { c.unshift(s); s = s.rodic ? oddil[s.rodic] : null; } return c; };

// inline formátování: **tučně**, *kurzíva*, [^n] poznámka, {Termín} odkaz do glosáře
function inline(s, ctx) {
  let h = esc(s);
  h = h.replace(/\*\*(.+?)\*\*/g, '<b>$1</b>').replace(/(^|[^*])\*([^*\s][^*]*?)\*(?!\*)/g, '$1<i>$2</i>');
  h = h.replace(/\[\^(\d+)\]/g, (m, n) => ctx && ctx.p ? `<sup class="fn"><a href="#" data-fn="${ctx.p.id}:${n}">${n}</a></sup>` : '');
  h = h.replace(/\{([^}]*)\}\*?/g, (m, t) => {
    const id = E.demap[normDe(t.split('/')[0])] || E.demap[normDe(t)];
    return id ? `<a class="term" href="#/heslo/${id}" data-h="${id}">[${t}]</a>` : `<span class="term">[${t}]</span>`;
  });
  return h;
}
function hodnota(v, typ, ctx) {
  if (v == null || v === '') return '';
  if (typ === 'seznam' && Array.isArray(v)) return '<ul>' + v.map(x => `<li>${inline(x, ctx)}</li>`).join('') + '</ul>';
  if (typ === 'verse' && Array.isArray(v)) return '<p class="verse">' + v.map(x => inline(x, ctx)).join('<br>') + '</p>';
  if (typ === 'tabulka' && Array.isArray(v)) return '<table>' + v.map(r => '<tr>' + (Array.isArray(r) ? r : [r]).map(c => `<td>${inline(c, ctx)}</td>`).join('') + '</tr>').join('') + '</table>';
  if (Array.isArray(v)) return '<ul>' + v.map(x => `<li>${inline(x, ctx)}</li>`).join('') + '</ul>';
  return String(v).split(/\n\s*\n/).map(x => `<p>${inline(x, ctx).replace(/\n/g, '<br>')}</p>`).join('');
}

// ---------- vykreslení rozsahu bloků se značkami stran a poznámkami
const ovZnacka = p => p.ov
  ? ` · <span class="ov" title="Stranu prošel a schválil člověk${p.ov.datum ? ' ' + esc(p.ov.datum) : ''}${p.ov.kdo ? ' (' + esc(p.ov.kdo) + ')' : ''}">✓ ověřeno člověkem</span>`
  : ' · <span class="neov" title="Stranu zatím neověřil člověk">neověřeno člověkem</span>';
function predel(p, prvni) {
  const strn = p.strana === 'verso' ? 'levá strana' : 'pravá strana';
  return `<div class="predel" id="p-${p.id}"><span class="ik">📄</span><span>${prvni ? 'Strana' : 'Začátek strany'} <b>${folio(p)}</b> (sken č. ${p.sken}, ${strn})</span>
    <a href="#/strana/${p.id}">samostatná strana</a><a href="${skenUrl(p)}" target="_blank" rel="noopener">sken ↗</a>
    <span class="stav"><span class="tecka" style="background:var(--st-${p.stav})"></span>${STAVY[p.stav] || p.stav}${ovZnacka(p)}</span></div>`;
}
function poznamkyStrany(p, pouzite) {
  const ns = Object.keys(p.pozn || {}).filter(n => pouzite.has(n)).sort((a, b) => a - b);
  if (!ns.length) return '';
  return `<div class="poznamky"><span class="nadp">Poznámky překladatele · ${folio(p)}</span><ol>` +
    ns.map(n => `<li value="${n}" id="fn-${p.id}-${n}">${inline(p.pozn[n], null)}</li>`).join('') + '</ol></div>';
}
function vykresli(od, doo, moznosti = {}) {
  const sOrig = moznosti.orig !== false;
  let h = '', akt = null, pouzite = new Set();
  const zavri = () => { if (akt) h += poznamkyStrany(akt, pouzite); };
  for (let i = od; i < doo; i++) {
    const b = BL[i], p = STR[b.p];
    if (p !== akt) { zavri(); akt = p; pouzite = new Set(); h += predel(p, i === od && p.od === i); }
    const ctx = {p};
    const cs = b.cs == null ? '' : JSON.stringify(b.cs);
    (cs.match(/\[\^(\d+)\]/g) || []).forEach(m => pouzite.add(m.slice(2, -1)));
    const tridy = ['radek', b.t, b.c ? 'c' : '', b.z ? 'z' : ''].join(' ');
    if (b.t === 'obrazek') {
      h += `<div class="${tridy}" id="b${i}"><figure><img loading="lazy" src="obrazky/${esc(b.img)}" alt="${esc(b.popis || 'vyobrazení')}">${b.popis ? `<figcaption>${inline(b.popis, ctx)}</figcaption>` : ''}</figure></div>`;
      continue;
    }
    let de, cz;
    if (b.t === 'nadpis') {
      const tag = 'h' + Math.min(4, (b.u || 2) + 1);
      const s = ODD.find(x => x.od === i);
      de = b.de ? `<${tag}>${inline(b.de, ctx)}</${tag}>` : '';
      cz = b.cs ? `<${tag}>${s ? `<a href="#/kap/${s.id}" style="color:inherit;text-decoration:none">` : ''}${inline(b.cs, ctx)}${s ? '</a>' : ''}</${tag}>` : '<span class="chybi">[překlad chybí]</span>';
    } else {
      de = hodnota(b.de, b.t, ctx);
      cz = b.cs == null ? '<span class="chybi">[překlad zatím chybí]</span>' : hodnota(b.cs, b.t, ctx);
    }
    h += `<div class="${tridy}" id="b${i}">` + (sOrig ? `<div class="de" lang="de">${de}</div>` : '') + `<div class="cs">${cz}</div></div>`;
  }
  zavri();
  return h;
}
const zahlaviSloupcu = '<div class="zahlavi-sloupcu"><span class="de">Originál (1564)</span><span>Český překlad</span></div>';

// ---------- navigace mezi oddíly
function dalsiOddil(s) {
  return ODD.find(k => k.od >= s.do && k.u === s.u) || ODD.find(k => k.od >= s.do) || null;
}
function predchoziOddil(s) {
  let r = null;
  for (const k of ODD) { if (k.do <= s.od && k.u <= s.u) r = k; }
  if (!r) for (const k of ODD) { if (k.do <= s.od) r = k; }
  return r;
}
const navOdkaz = (s, smer) => s ? `<a class="${smer}" href="#/kap/${s.id}" data-klav="${smer}"><small>${smer === 'dalsi' ? 'Další →' : '← Předchozí'}</small>${esc(strop(plain(s.cs || s.de), 70))}</a>` : '<span></span>';

// ---------- pohledy
const V = {};
V.obsah = () => {
  const celk = STR.length;
  const postup = STAV_PORADI.filter(s => E.stav[s]).map(s => `<span style="width:${100 * E.stav[s] / celk}%;background:var(--st-${s})" title="${STAVY[s]}: ${E.stav[s]}"></span>`).join('');
  const leg = STAV_PORADI.filter(s => E.stav[s]).map(s => `<span><span class="tecka" style="background:var(--st-${s})"></span>${STAVY[s]} ${E.stav[s]}</span>`).join('');
  const strom = s => {
    const p = STR[s.p];
    const pol = `<a class="pol" href="#/kap/${s.id}"><span class="fol">${folio(p)}</span>${inline(s.cs || s.de, null)}</a>`;
    if (!s.deti.length) return `<li class="u${s.u}">${pol}</li>`;
    return `<li class="u${s.u}"><details><summary>${pol}</summary><ul>${s.deti.map(strom).join('')}</ul></details></li>`;
  };
  const tit = STR[0];
  return `<div class="titul"><div>
    <h1>${esc(M.nazev)}<span class="de">${esc(M.nazev_orig)} – ${esc(M.podtitul || '')}</span></h1>
    <p class="uvod">${esc(M.autor)} (${esc(M.autor_zivot || '')}). ${esc(M.vydani)}. ${esc(M.rozsah || '')}. ${esc(M.vd16 || '')}.</p>
    <p>${esc(M.popis || '')}</p>
    <p class="m">Překlad: ${esc(M.prekladatel || '')}. Sken: ${esc(M.sken.instituce)}, ${esc(M.sken.signatura)} (<a href="${M.sken.url_dilo}" target="_blank" rel="noopener">digitale-sammlungen.de ↗</a>).</p>
    <div class="postup">${postup}</div><div class="legenda">${leg}</div>
    <p class="m"><span class="ov">✓</span> Ověřeno člověkem: <b>${E.overeno || 0}</b> z ${celk} stran (ostatní prošly jen strojovou kontrolou).</p>
    <p><a class="chip" href="#/kap/${ODD[0].id}">Začít číst</a><a class="chip" href="#/strany">Listovat po stranách</a><a class="chip" href="#/rejstrik">Věcný rejstřík</a><a class="chip" href="#/tisk">Stáhnout PDF</a></p>
  </div><figure><a href="${skenUrl(tit)}" target="_blank" rel="noopener"><img src="${skenObr(tit, 520)}" alt="Titulní list tisku z roku ${M.rok}" loading="lazy" onerror="if(!this.dataset.z){this.dataset.z=1;this.src='obrazky/drevorez-1.jpg'}else{this.closest('figure').hidden=true}"></a><figcaption>Titulní list (BSB München; offline titulní dřevořez)</figcaption></figure></div>
  <h2 class="sekce">Obsah</h2>
  <ul class="toc">${ODD.filter(s => !s.rodic).map(strom).join('')}</ul>`;
};

V.kap = (id, blok) => {
  const s = oddil[id];
  if (!s) return V.nenalezeno();
  const cesta = cestaOddilu(s).slice(0, -1).map(x => `<a href="#/kap/${x.id}">${esc(strop(plain(x.cs || x.de), 50))}</a>`).join(' › ');
  const p1 = STR[BL[s.od] ? BL[s.od].p : s.p], p2 = STR[BL[Math.max(s.od, s.do - 1)] ? BL[Math.max(s.od, s.do - 1)].p : s.p];
  const rozsah = p1 === p2 ? folio(p1) : `${folio(p1)} – ${folio(p2)}`;
  const nav = `<div class="nav-ctecka">${navOdkaz(predchoziOddil(s), 'predchozi')}${navOdkaz(dalsiOddil(s), 'dalsi')}</div>`;
  const pod = s.deti.length ? `<p class="m">Obsahuje: ${s.deti.map(d => `<a href="#/kap/${d.id}">${esc(strop(plain(d.cs || d.de), 60))}</a>`).join(' · ')}</p>` : '';
  setTimeout(() => blok != null && cil('b' + blok), 0);
  return `<p class="drobky"><a href="#/">Obsah</a>${cesta ? ' › ' + cesta : ''}</p>
    <h1>${inline(s.cs || s.de, null)}<span class="de">${inline(s.de, null)}</span></h1>
    <p class="m">${rozsah} · <a href="#/tisk/${s.id}">PDF této části</a></p>${pod}${nav}
    <div class="ctecka">${zahlaviSloupcu}${vykresli(s.od, s.do)}</div>${nav}`;
};

V.vse = () => `<h1>${esc(M.nazev)} – celá kniha</h1>${zahlaviSloupcu}<div class="ctecka">${vykresli(0, BL.length)}</div>`;

V.strana = id => {
  const p = strana[id];
  if (!p) return V.nenalezeno();
  const pred = STR[p.i - 1], dal = STR[p.i + 1];
  const s = ODD.filter(x => x.od <= Math.max(p.od, 0) && x.do > p.od).pop() || ODD.filter(x => x.od <= p.od).pop();
  const nav = `<div class="nav-ctecka">${pred ? `<a class="predchozi" href="#/strana/${pred.id}" data-klav="predchozi"><small>← Předchozí strana</small>${folio(pred)}</a>` : '<span></span>'}${dal ? `<a class="dalsi" href="#/strana/${dal.id}" data-klav="dalsi"><small>Další strana →</small>${folio(dal)}</a>` : ''}</div>`;
  const obsah = p.do > p.od ? vykresli(p.od, p.do) : `${predel(p, true)}<p class="prazdne">Tato strana zatím nemá přepsaný text. Podívejte se na sken.</p>`;
  const sekce = s ? `<p class="m">Kapitola: ${cestaOddilu(s).map(x => `<a href="#/kap/${x.id}">${esc(strop(plain(x.cs || x.de), 60))}</a>`).join(' › ')}</p>` : '';
  return `<p class="drobky"><a href="#/">Obsah</a> › <a href="#/strany">Strany</a></p>
    <h1>${folio(p)}<span class="de">${folioDlouze(p)} · sken č. ${p.sken}</span></h1>${sekce}${nav}
    <div class="strana-layout"><div class="ctecka">${zahlaviSloupcu}${obsah}</div>
    <aside class="sken-panel"><a href="${skenUrl(p)}" target="_blank" rel="noopener"><img src="${skenObr(p, 700)}" alt="Sken ${folio(p)}" loading="lazy" onerror="this.alt='Náhled skenu není dostupný (offline?)'"></a>
    <p class="m">Náhled skenu (BSB, ${esc(M.sken.id)}, sken ${p.sken}). <a href="${skenUrl(p)}" target="_blank" rel="noopener">Otevřít v prohlížeči MDZ ↗</a></p></aside></div>${nav}`;
};

V.strany = () => {
  const skup = {};
  STR.forEach(p => { const s = hlavniOddil(ODD.filter(x => x.od <= p.od).pop() || ODD[0]); (skup[s.id] = skup[s.id] || {s, p: []}).p.push(p); });
  const leg = STAV_PORADI.filter(s => E.stav[s]).map(s => `<span><span class="tecka" style="background:var(--st-${s})"></span>${STAVY[s]} ${E.stav[s]}</span>`).join('');
  return `<h1>Strany tisku<span class="de">Listování podle původní foliace (líc r / rub v)</span></h1>
    <p class="uvod">Tisk je číslován po listech (foliace): r = líc, v = rub. List XVI má v tisku chybně číslo XVII.</p><div class="legenda">${leg}</div>` +
    Object.values(skup).map(g => `<h2 class="sekce">${inline(g.s.cs || g.s.de, null)}</h2><div class="mrizka">` +
      g.p.map(p => `<a href="#/strana/${p.id}" style="--c:var(--st-${p.stav})" title="${STAVY[p.stav]}${p.ov ? ' · ověřeno člověkem' : ''}">${folio(p)}${p.ov ? ' <span class="ov">✓</span>' : ''}<small>sken ${p.sken}</small></a>`).join('') + '</div>').join('');
};

V.rejstrik = () => {
  const kat = Object.entries(E.kategorie);
  return `<h1>Věcný rejstřík<span class="de">Termíny, úřady, zbraně, osoby a místa s odkazy do textu</span></h1>
    <input class="filtr" id="filtr" type="search" placeholder="Filtrovat hesla (česky i německy)…" aria-label="Filtrovat hesla">
    ${kat.map(([k, nazev]) => {
      const hs = E.hesla.filter(h => h.kat === k).sort((a, b) => a.cs.localeCompare(b.cs, 'cs'));
      if (!hs.length) return '';
      return `<div class="kat"><h2 class="sekce">${esc(nazev)}</h2><div class="hesla">${hs.map(h =>
        `<a href="#/heslo/${h.id}" data-f="${esc(bezDiakritiky(h.cs + ' ' + h.de.join(' ')))}">${esc(h.cs)} <span class="de">${esc(h.de[0] || '')}</span> <span class="n">${h.v.length}</span></a>`).join('')}</div></div>`;
    }).join('')}`;
};

V.heslo = id => {
  const h = heslo[id];
  if (!h) return V.nenalezeno();
  const vys = h.v.map(v => {
    const b = BL[v.b], p = STR[b.p], s = oddil[b.s];
    return `<div class="vyskyt"><div class="kontext">${esc(v.k)}<mark>${esc(v.h)}</mark>${esc(v.z)}</div>
      <div class="m"><a href="#/kap/${s.id}/${v.b}">${esc(strop(plain(s.cs || s.de), 70))}</a> · <a href="#/strana/${p.id}">${folio(p)}</a></div></div>`;
  }).join('');
  return `<p class="drobky"><a href="#/rejstrik">Rejstřík</a> › ${esc(E.kategorie[h.kat] || '')}</p>
    <h1>${esc(h.cs)}<span class="de">${esc(h.de.join(', '))}</span></h1>
    ${h.pozn ? `<p>${esc(h.pozn)}</p>` : ''}
    <h2 class="sekce">Výskyty v překladu (${h.v.length})</h2>${vys || '<p class="prazdne">V přeloženém textu zatím bez výskytu.</p>'}`;
};

V.hledat = q => {
  q = (q || '').trim();
  const box = $('#q'); if (box && box.value !== q) box.value = q;
  if (q.length < 2) return '<h1>Hledání</h1><p class="prazdne">Zadejte alespoň dva znaky.</p>';
  const nq = bezDiakritiky(q);
  const hesla = E.hesla.filter(h => bezDiakritiky(h.cs + ' ' + h.de.join(' ')).includes(nq));
  const vys = [];
  for (let i = 0; i < BL.length && vys.length < 300; i++) {
    const b = BL[i];
    for (const jaz of ['cs', 'de']) {
      const t = plain(b[jaz]); if (!t) continue;
      const k = bezDiakritiky(t).indexOf(nq);
      if (k >= 0) { vys.push({i, jaz, t, k}); break; }
    }
  }
  const radky = vys.map(v => {
    const b = BL[v.i], p = STR[b.p], s = oddil[b.s];
    const a = Math.max(0, v.k - 80), z = Math.min(v.t.length, v.k + q.length + 80);
    return `<a class="vysledek" href="#/kap/${s.id}/${v.i}"><div${v.jaz === 'de' ? ' class="de"' : ''}>${a ? '…' : ''}${esc(v.t.slice(a, v.k))}<mark>${esc(v.t.slice(v.k, v.k + q.length))}</mark>${esc(v.t.slice(v.k + q.length, z))}${z < v.t.length ? '…' : ''}</div>
      <div class="m">${esc(strop(plain(s.cs || s.de), 70))} · ${folio(p)}${v.jaz === 'de' ? ' · v originálu' : ''}</div></a>`;
  }).join('');
  return `<h1>Hledání: „${esc(q)}“</h1>
    ${hesla.length ? `<p>Hesla rejstříku: ${hesla.map(h => `<a class="chip" href="#/heslo/${h.id}">${esc(h.cs)}</a>`).join('')}</p>` : ''}
    <p class="m">${vys.length >= 300 ? 'Prvních 300' : vys.length} výsledků (bez ohledu na diakritiku; hledá v překladu i originálu).</p>${radky}`;
};

V.tisk = vybrany => {
  const strom = ODD.map(s => `<label class="u${s.u}"><input type="checkbox" value="${s.id}"${s.id === vybrany ? ' checked' : ''}> ${esc(strop(plain(s.cs || s.de), 90))} <span class="m">${folio(STR[s.p])}</span></label>`).join('');
  setTimeout(() => {
    const strom = $('#tisk-strom');
    strom.addEventListener('change', e => {
      const s = oddil[e.target.value]; if (!s) return;
      ODD.filter(k => k.od >= s.od && k.do <= s.do && k !== s).forEach(k => { strom.querySelector(`input[value="${k.id}"]`).checked = e.target.checked; });
    });
    $('#tisk-cela').onclick = () => strom.querySelectorAll('input').forEach(x => x.checked = true);
    $('#tisk-nic').onclick = () => strom.querySelectorAll('input').forEach(x => x.checked = false);
    $('#tisk-go').onclick = () => tiskni();
  }, 0);
  return `<h1>Stáhnout PDF<span class="de">Výběr se vytiskne přes dialog prohlížeče – zvolte „Uložit jako PDF“.</span></h1>
  <div class="tisk-volby">
    <fieldset><legend>Co vytisknout</legend>
      <p><label><input type="radio" name="rozsah" value="kap" checked> vybrané kapitoly</label><br>
      <label><input type="radio" name="rozsah" value="str"> rozsah stran od <select id="tisk-od">${STR.map(p => `<option value="${p.i}">${folio(p)}</option>`).join('')}</select>
       do <select id="tisk-do">${STR.map((p, i) => `<option value="${p.i}"${i === STR.length - 1 ? ' selected' : ''}>${folio(p)}</option>`).join('')}</select></label></p>
      <p><button class="tl" id="tisk-cela" type="button">Vybrat vše</button> <button class="tl" id="tisk-nic" type="button">Zrušit výběr</button></p>
      <div class="tisk-strom" id="tisk-strom">${strom}</div>
    </fieldset>
    <fieldset><legend>Podoba</legend>
      <p><label><input type="radio" name="jazyk" value="cs" checked> jen český překlad</label><br>
      <label><input type="radio" name="jazyk" value="oba"> originál + překlad (dva sloupce)</label></p>
      <p><label><input type="checkbox" id="tisk-poz" checked> poznámky překladatele</label><br>
      <label><input type="checkbox" id="tisk-pre" checked> předěly stran tisku</label></p>
      <button class="tl velke" id="tisk-go" type="button" aria-pressed="true">Vytvořit PDF</button>
      <p class="m">Tip: v dialogu tisku vypněte „Záhlaví a zápatí“ a zapněte „Grafika na pozadí“.</p>
    </fieldset>
  </div>`;
};
function tiskni() {
  const oba = document.querySelector('input[name="jazyk"]:checked').value === 'oba';
  const rozsahy = [];
  if (document.querySelector('input[name="rozsah"]:checked').value === 'str') {
    const a = +$('#tisk-od').value, b = +$('#tisk-do').value;
    rozsahy.push([STR[Math.min(a, b)].od, STR[Math.max(a, b)].do]);
  } else {
    const vyb = [...document.querySelectorAll('#tisk-strom input:checked')].map(x => oddil[x.value]);
    // sloučit do souvislých rozsahů (oddíl bez pododdílů nebo jen jeho vlastní text)
    const pokryto = new Uint8Array(BL.length);
    vyb.forEach(s => { const konec = s.deti.length ? s.deti[0].od : s.do; for (let i = s.od; i < konec; i++) pokryto[i] = 1; });
    let z = -1;
    for (let i = 0; i <= BL.length; i++) {
      if (i < BL.length && pokryto[i]) { if (z < 0) z = i; } else if (z >= 0) { rozsahy.push([z, i]); z = -1; }
    }
  }
  if (!rozsahy.length) { alert('Vyberte alespoň jednu kapitolu nebo rozsah stran.'); return; }
  const out = $('#tisk-vystup');
  out.innerHTML = `<div class="tisk-titul"><h1>${esc(M.nazev)}</h1><p class="de">${esc(M.nazev_orig)}</p><p>${esc(M.autor)}, ${esc(M.vydani)}</p><p class="m">Český překlad · ${new Date().toLocaleDateString('cs-CZ')}</p></div>` +
    rozsahy.map(([a, b]) => `<div class="ctecka">${oba ? zahlaviSloupcu : ''}${vykresli(a, b, {orig: oba})}</div>`).join('');
  if (!$('#tisk-poz').checked) out.querySelectorAll('.poznamky,sup.fn').forEach(x => x.remove());
  if (!$('#tisk-pre').checked) out.querySelectorAll('.predel').forEach(x => x.remove());
  out.classList.toggle('bez-orig-tisk', !oba);
  document.body.classList.add('tiskne');
  const bylo = document.body.classList.contains('bez-orig');
  document.body.classList.toggle('bez-orig', !oba);
  const konec = () => { document.body.classList.remove('tiskne'); document.body.classList.toggle('bez-orig', bylo); out.innerHTML = ''; window.removeEventListener('afterprint', konec); };
  window.addEventListener('afterprint', konec);
  setTimeout(() => window.print(), 50);
}

V.oEdici = () => `<h1>O edici</h1>
  <p>${esc(M.autor)}: <i>${esc(M.nazev_orig)}</i>, ${esc(M.vydani)} (${esc(M.vd16 || '')}).</p>
  <p>Německý text je přepsán podle digitalizace ${esc(M.sken.instituce)} (${esc(M.sken.signatura)}, ${esc(M.sken.id)}) z OCR s ručně/strojově opravenými chybami; zachovává dobový pravopis včetně lomítek (virgulí).
  Český překlad se drží odstavců tisku, aby bylo možné oba texty číst vedle sebe. Odborné termíny se při prvním výskytu na stránce uvádějí v závorce v podobě z tisku <span class="term">[takto]</span> a vedou do věcného rejstříku;
  doplňky překladatele jsou v [hranatých závorkách].</p>
  <p>Strany jsou označeny podle foliace tisku: <b>r</b> (recto) = líc listu, pravá strana dvojstrany; <b>v</b> (verso) = rub, levá strana. „Sken č.“ odkazuje na pořadí snímku v digitalizaci BSB.</p>
  <p class="m">Licence skenů: ${esc(M.sken.licence || '')}.</p>
  <p class="m">Ovládání: ← → předchozí/další kapitola nebo strana · O skrýt/zobrazit originál · / hledat.</p>`;
V.nenalezeno = () => '<h1>Nenalezeno</h1><p><a href="#/">Zpět na obsah</a></p>';

// ---------- směrování
function route() {
  const hash = decodeURIComponent(location.hash.replace(/^#\/?/, ''));
  const [cesta, dotaz] = hash.split('?');
  const c = cesta.split('/');
  let html, menu = '';
  switch (c[0]) {
    case '': html = V.obsah(); menu = 'obsah'; break;
    case 'kap': html = V.kap(c[1], c[2]); break;
    case 'vse': html = V.vse(); break;
    case 'strana': html = V.strana(c[1]); menu = 'strany'; break;
    case 'strany': html = V.strany(); menu = 'strany'; break;
    case 'rejstrik': html = V.rejstrik(); menu = 'rejstrik'; break;
    case 'heslo': html = V.heslo(c[1]); menu = 'rejstrik'; break;
    case 'hledat': html = V.hledat(new URLSearchParams(dotaz || '').get('q')); break;
    case 'tisk': html = V.tisk(c[1]); menu = 'tisk'; break;
    case 'o-edici': html = V.oEdici(); break;
    default: html = V.nenalezeno();
  }
  OBSAH.innerHTML = html;
  document.querySelectorAll('.menu a').forEach(a => a.classList.toggle('on', a.dataset.m === menu));
  const nadp = OBSAH.querySelector('h1');
  document.title = (nadp ? nadp.childNodes[0].textContent + ' – ' : '') + M.nazev;
  if (!(c[0] === 'kap' && c[2])) window.scrollTo(0, 0);
  const f = $('#filtr');
  if (f) f.addEventListener('input', () => {
    const q = bezDiakritiky(f.value);
    OBSAH.querySelectorAll('.hesla a').forEach(a => a.hidden = q && !a.dataset.f.includes(q));
  });
}
function cil(id) {
  const el = document.getElementById(id);
  if (!el) return;
  el.scrollIntoView({block: 'start'});
  el.classList.add('cil');
}

// ---------- bublina: poznámky a glosář
const BUB = $('#bublina');
function ukazBublinu(el, html) {
  BUB.innerHTML = html; BUB.hidden = false;
  const r = el.getBoundingClientRect();
  const w = Math.min(360, window.innerWidth - 24);
  BUB.style.maxWidth = w + 'px';
  let x = window.scrollX + r.left - 20;
  x = Math.max(window.scrollX + 8, Math.min(x, window.scrollX + window.innerWidth - w - 12));
  BUB.style.left = x + 'px';
  BUB.style.top = (window.scrollY + r.bottom + 6) + 'px';
}
document.addEventListener('mouseover', e => {
  const t = e.target.closest('a.term[data-h]');
  if (t) { const h = heslo[t.dataset.h]; ukazBublinu(t, `<b>${esc(h.cs)}</b>${esc(h.pozn || h.de.join(', '))}<div class="m">Klikněte pro výskyty v rejstříku</div>`); return; }
  const f = e.target.closest('a[data-fn]');
  if (f) { const [pid, n] = f.dataset.fn.split(':'); ukazBublinu(f, `<b>Poznámka ${n}</b>${inline(strana[pid].pozn[n] || '', null)}`); return; }
});
document.addEventListener('mouseout', e => { if (e.target.closest('a.term, a[data-fn]')) BUB.hidden = true; });
document.addEventListener('click', e => {
  const f = e.target.closest('a[data-fn]');
  if (f) { e.preventDefault(); const [pid, n] = f.dataset.fn.split(':'); cil(`fn-${pid}-${n}`); }
});

// ---------- přepínače a klávesy
const prepOrig = $('#prepinac-orig');
function nastavOrig(v) { document.body.classList.toggle('bez-orig', !v); prepOrig.setAttribute('aria-pressed', v); prepOrig.textContent = v ? 'Originál' : 'Jen překlad'; uloz('orig', v); }
prepOrig.onclick = () => nastavOrig(document.body.classList.contains('bez-orig'));
nastavOrig(nacti('orig', true));
const R = document.documentElement;
const tema = nacti('tema', null); if (tema) R.dataset.theme = tema;
$('#prepinac-tema').onclick = () => {
  const dark = R.dataset.theme ? R.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
  R.dataset.theme = dark ? 'light' : 'dark'; uloz('tema', R.dataset.theme);
};
document.addEventListener('keydown', e => {
  if (e.target.closest('input,select,textarea') || e.ctrlKey || e.metaKey || e.altKey) return;
  if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
    const a = OBSAH.querySelector(`.nav-ctecka a[data-klav="${e.key === 'ArrowRight' ? 'dalsi' : 'predchozi'}"]`);
    if (a) { e.preventDefault(); location.hash = a.getAttribute('href'); }
  } else if (e.key === 'o' || e.key === 'O') { prepOrig.click(); }
  else if (e.key === '/') { e.preventDefault(); $('#q').focus(); }
});
const q = $('#q');
let qt;
q.addEventListener('input', () => { clearTimeout(qt); qt = setTimeout(() => { if (q.value.trim().length >= 2) location.hash = '#/hledat?q=' + encodeURIComponent(q.value.trim()); }, 350); });
q.addEventListener('keydown', e => { if (e.key === 'Enter') location.hash = '#/hledat?q=' + encodeURIComponent(q.value.trim()); });
window.addEventListener('hashchange', route);
route();
})();
