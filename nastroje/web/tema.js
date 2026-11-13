/* Přepínač světlého/tmavého motivu pro statické stránky (rozcestník, O projektu). */
(function () {
  var r = document.documentElement, t = null;
  try { t = JSON.parse(localStorage.getItem('edice.tema')); } catch (e) {}
  if (t) r.dataset.theme = t;
  var b = document.getElementById('prepinac-tema');
  if (b) b.onclick = function () {
    var dark = r.dataset.theme ? r.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
    r.dataset.theme = dark ? 'light' : 'dark';
    try { localStorage.setItem('edice.tema', JSON.stringify(r.dataset.theme)); } catch (e) {}
  };
})();
