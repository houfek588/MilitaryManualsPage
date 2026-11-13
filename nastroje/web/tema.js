/* Světlý / tmavý motiv – společný pro všechny stránky webu (rozcestník, O projektu, čtečky knih).
   Načítá se v <head>, aby se motiv nastavil dřív, než se stránka vykreslí (bez probliknutí).

   Volba se pamatuje dvojím způsobem:
   1) localStorage („edice.tema“) – stačí na webu (GitHub Pages, lokální server);
   2) parametr v adrese ?tema=dark|light – přidává se k odkazům mezi stránkami webu. Je nutný při otevření
      ze souboru (file:///…), kde prohlížeče (např. Firefox) považují každý soubor za samostatný web
      a localStorage mezi nimi nesdílejí. */
(function () {
  'use strict';
  var R = document.documentElement, KLIC = 'edice.tema';
  function cti() { try { var v = JSON.parse(localStorage.getItem(KLIC)); return v === 'dark' || v === 'light' ? v : null; } catch (e) { return null; } }
  function uloz(t) { try { localStorage.setItem(KLIC, JSON.stringify(t)); } catch (e) {} }

  var z_adresy = /[?&]tema=(dark|light)\b/.exec(location.search);
  var t = z_adresy ? z_adresy[1] : cti();
  if (t) { R.dataset.theme = t; uloz(t); }

  // Přidá ?tema=… k odkazu na jinou stránku tohoto webu (relativní odkaz na .html).
  function upravOdkaz(a) {
    var t = R.dataset.theme, h = a.getAttribute('href');
    if (!t || !h || /^[a-z]+:|^\/\/|^#/i.test(h)) return;
    var m = /^([^?#]*\.html)(\?[^#]*)?(#.*)?$/.exec(h);
    if (!m) return;
    var q = (m[2] || '').replace(/^\?/, '').split('&').filter(function (x) { return x && !/^tema=/.test(x); });
    q.push('tema=' + t);
    a.setAttribute('href', m[1] + '?' + q.join('&') + (m[3] || ''));
  }
  function upravVse() { var a = document.querySelectorAll('a[href]'); for (var i = 0; i < a.length; i++) upravOdkaz(a[i]); }

  // Odkazy vzniklé až za běhu (čtečka knihy) se upraví při kliknutí.
  ['click', 'auxclick', 'contextmenu'].forEach(function (ev) {
    document.addEventListener(ev, function (e) { var a = e.target.closest && e.target.closest('a[href]'); if (a) upravOdkaz(a); }, true);
  });

  function prepni() {
    var dark = R.dataset.theme ? R.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
    R.dataset.theme = dark ? 'light' : 'dark';
    uloz(R.dataset.theme);
    upravVse();
    // aktuální adresu taky, aby obnovení stránky (F5) motiv zachovalo
    if (/[?&]tema=/.test(location.search) || location.protocol === 'file:') {
      try {
        var s = location.search.replace(/^\?/, '').split('&').filter(function (x) { return x && !/^tema=/.test(x); });
        s.push('tema=' + R.dataset.theme);
        history.replaceState(history.state, '', location.pathname + '?' + s.join('&') + location.hash);
      } catch (e) {}
    }
  }

  function navaz() {
    upravVse();
    var b = document.getElementById('prepinac-tema');
    if (b) b.addEventListener('click', prepni);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', navaz); else navaz();
})();
