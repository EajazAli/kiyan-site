/* Kiyan — site behaviour. Vanilla JS, no dependencies. */
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var T = window.KIYAN_T || {}, RTL = document.documentElement.dir === 'rtl';
  var fmt = function (s, o) { return String(s || '').replace(/\{(\w+)\}/g, function (m, k) { return o[k]; }); };

  /* ---------- first-visit loader ----------
     First page of a session only: the two halves of the Kiyan mark come together, the dot
     forms between them and the tagline rises, then the brand-colour sheets peel away.
     Moving from page to page is an ordinary, immediate page load. */
  var root = document.documentElement, pre = $('.preloader');
  var clearBoot = function () { clearTimeout(window.__kiyanBail); root.classList.remove('is-preloading'); };
  if (reduce || !pre) clearBoot();
  else if (root.classList.contains('is-preloading')) {
    clearTimeout(window.__kiyanBail);
    var JOIN = 900, HOLD = 2300, OUT = HOLD + 450;
    window.scrollTo(0, 0);
    void pre.offsetWidth; setTimeout(function () { pre.classList.add('is-in'); }, 60);
    setTimeout(function () { pre.classList.add('is-joined'); }, JOIN);
    setTimeout(function () { pre.classList.add('is-words-out'); }, HOLD);
    setTimeout(function () { pre.classList.add('is-out'); }, OUT);
    setTimeout(function () { clearBoot(); pre.classList.remove('is-in', 'is-joined', 'is-words-out', 'is-out'); try { sessionStorage.setItem('kiyan-seen', '1'); } catch (e) {} }, OUT + 1500);
  }
  window.addEventListener('pageshow', function (e) { if (e.persisted) clearBoot(); });

  /* ---------- language switch keeps your place ----------
     The other language opens on the same page, at the same section, with the same
     enquiry details, instead of starting again from the top. */
  var LANG_KEY = 'kiyan-lang-pos';
  $$('a[hreflang]').forEach(function (a) {
    a.addEventListener('click', function () {
      var marks = $$('main [id]'), at = null;
      marks.forEach(function (el) { if (el.offsetParent !== null && el.getBoundingClientRect().top <= 140) at = el; });
      var max = document.documentElement.scrollHeight - window.innerHeight, pos = { r: max > 0 ? window.scrollY / max : 0 };
      if (at) { var rc = at.getBoundingClientRect(); pos.id = at.id; pos.f = rc.height > 0 ? Math.max(0, -rc.top) / rc.height : 0; }
      var f = $('#contact-form');
      if (f) { pos.form = {}; ['name', 'role', 'company', 'email', 'topic', 'message'].forEach(function (n) { pos.form[n] = f.elements[n].value; }); pos.type = (f.querySelector('input[name="type"]:checked') || {}).id; }
      try { sessionStorage.setItem(LANG_KEY, JSON.stringify(pos)); } catch (e) {}
      if (location.search && a.getAttribute('href').indexOf('?') < 0) a.setAttribute('href', a.getAttribute('href') + location.search);
    });
  });
  (function () {
    var pos = null;
    try { pos = JSON.parse(sessionStorage.getItem(LANG_KEY) || 'null'); sessionStorage.removeItem(LANG_KEY); } catch (e) {}
    if (!pos) return;
    var f = $('#contact-form');
    if (f && pos.form) {
      Object.keys(pos.form).forEach(function (n) { if (f.elements[n]) f.elements[n].value = pos.form[n]; });
      if (pos.type && document.getElementById(pos.type)) document.getElementById(pos.type).checked = true;
    }
    var go = function () {
      var el = pos.id && document.getElementById(pos.id), y;
      if (el && el.offsetParent !== null) { var rc = el.getBoundingClientRect(); y = rc.top + window.scrollY + (pos.f || 0) * rc.height - (pos.f ? 0 : 96); }
      else y = pos.r * (document.documentElement.scrollHeight - window.innerHeight);
      window.scrollTo({ top: Math.max(0, y), behavior: 'instant' });
    };
    go(); window.addEventListener('load', go);
  })();

  /* ---------- analytics, only after the visitor accepts ---------- */
  var gtmId = root.getAttribute('data-gtm'), consent = $('#consent');
  var gtmHosts = (root.getAttribute('data-gtm-hosts') || '').split(',').filter(Boolean);
  if (gtmHosts.length && gtmHosts.indexOf(location.hostname) < 0) gtmId = null;      // preview and local copies are never measured
  window.dataLayer = window.dataLayer || [];
  var loadGTM = function () {
    if (window.__kiyanGTM || !gtmId) return; window.__kiyanGTM = 1;
    window.dataLayer.push({ 'gtm.start': new Date().getTime(), event: 'gtm.js' });
    var sc = document.createElement('script'); sc.async = true;
    sc.src = 'https://www.googletagmanager.com/gtm.js?id=' + encodeURIComponent(gtmId);
    document.head.appendChild(sc);
  };
  if (gtmId) {
    var choice = null; try { choice = localStorage.getItem('kiyan-consent'); } catch (e) {}
    if (choice === 'yes') loadGTM();
    else if (choice !== 'no' && consent) consent.hidden = false;
    $$('[data-consent]').forEach(function (b) {
      b.addEventListener('click', function () {
        var v = b.getAttribute('data-consent');
        try { localStorage.setItem('kiyan-consent', v); } catch (e) {}
        consent.hidden = true; if (v === 'yes') loadGTM();
      });
    });
  }

  /* ---------- theme ---------- */
  var tt = $('#theme-toggle');
  if (tt) tt.addEventListener('click', function () {
    var next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    try { localStorage.setItem('kiyan-theme', next); } catch (e) {}
  });

  /* ---------- navigation ---------- */
  var nav = $('#nav'), menuBtn = $('#menu-btn'), megaBtns = $$('.nav-link[aria-controls]');
  var fine = matchMedia('(hover: hover) and (min-width: 961px)'), hoverT;
  function setMega(which) {            // which: a button, or false to close all
    megaBtns.forEach(function (b) {
      var on = b === which, panel = document.getElementById(b.getAttribute('aria-controls'));
      b.setAttribute('aria-expanded', on); panel.classList.toggle('open', on);
    });
  }
  megaBtns.forEach(function (b) {
    var panel = document.getElementById(b.getAttribute('aria-controls'));
    b.addEventListener('click', function (e) { e.stopPropagation(); setMega(b.getAttribute('aria-expanded') === 'true' ? false : b); });
    // desktop: open on hover, as on large corporate sites; click and keyboard still work everywhere
    [b, panel].forEach(function (el) {
      el.addEventListener('mouseenter', function () { if (fine.matches) { clearTimeout(hoverT); setMega(b); } });
      el.addEventListener('mouseleave', function () { if (fine.matches) hoverT = setTimeout(function () { setMega(false); }, 160); });
    });
  });
  document.addEventListener('click', function (e) { if (!e.target.closest('.mega')) setMega(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { setMega(false); setMenu(false); } });
  function setMenu(open) {
    if (!nav) return;
    nav.classList.toggle('open', open); menuBtn.setAttribute('aria-expanded', open);
    document.body.style.overflow = open ? 'hidden' : '';
  }
  if (menuBtn) menuBtn.addEventListener('click', function () { setMenu(!nav.classList.contains('open')); });
  $$('#nav a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); setMega(false); }); });

  /* ---------- short silent loops: play only while on screen, never for reduced motion ---------- */
  var loops = $$('video[data-loop]');
  if (loops.length && !reduce && 'IntersectionObserver' in window) {
    var vio = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        var v = en.target;
        if (en.isIntersecting) { var p = v.play(); if (p && p.catch) p.catch(function () {}); } else v.pause();
      });
    }, { rootMargin: '200px 0px', threshold: 0.15 });
    loops.forEach(function (v) { v.muted = true; vio.observe(v); });
  }

  /* ---------- reveal on scroll ---------- */
  var reveals = $$('.reveal');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    reveals.forEach(function (el) { io.observe(el); });
  } else reveals.forEach(function (el) { el.classList.add('in'); });

  /* ---------- accessible tabs (spaces, roles, solutions) ---------- */
  $$('[data-tabs]').forEach(function (list) {
    var tabs = $$('[role="tab"]', list);
    function panelOf(t) { return document.getElementById(t.getAttribute('aria-controls')); }
    // the artwork shares one dot lattice, so cross-fading old over new reads as the dots regrouping
    function animate(from, to) {
      if (reduce || !from || !to || from === to) return;
      var art = $('.space-art', to), old = $('.space-art img:not(.art-ghost)', from);
      $$('.art-ghost').forEach(function (g) { g.remove(); });
      if (art && old) {
        var ghost = old.cloneNode(true);
        ghost.classList.add('art-ghost'); ghost.removeAttribute('loading');
        art.appendChild(ghost);
        setTimeout(function () { ghost.remove(); }, 900);
      }
      to.classList.remove('is-entering'); void to.offsetWidth; to.classList.add('is-entering');
      clearTimeout(to._enter); to._enter = setTimeout(function () { to.classList.remove('is-entering'); }, 1100);
    }
    function select(tab, focus) {
      var prev = tabs.filter(function (t) { return t.getAttribute('aria-selected') === 'true'; })[0];
      if (prev && prev !== tab) animate(panelOf(prev), panelOf(tab));
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', on); t.tabIndex = on ? 0 : -1;
        var p = document.getElementById(t.getAttribute('aria-controls')); if (p) p.hidden = !on;
      });
      if (focus) tab.focus();
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { select(t); });
      t.addEventListener('keydown', function (e) {
        var d = { ArrowDown: 1, ArrowRight: 1, ArrowUp: -1, ArrowLeft: -1 }[e.key];
        if (d) { e.preventDefault(); select(tabs[(i + d + tabs.length) % tabs.length], true); }
      });
    });
    // deep link, e.g. demand-space.html#p-range
    var h = location.hash.slice(1), target = h && tabs.filter(function (t) { return t.getAttribute('aria-controls') === h; })[0];
    if (target) select(target);
  });

  /* ---------- team: filter + bios ---------- */
  var filters = $$('.filter-btn');
  filters.forEach(function (b) {
    b.addEventListener('click', function () {
      filters.forEach(function (x) { x.setAttribute('aria-pressed', x === b); });
      var f = b.dataset.filter;
      $$('.profile[data-focus]').forEach(function (p) { p.hidden = !(f === '*' || p.dataset.focus.split('|').indexOf(f) > -1); });
    });
  });
  function openBio(id, push) {
    var d = document.getElementById('bio-' + id);
    if (!d || !d.showModal) return;
    d.showModal();
    if (push) history.replaceState(null, '', '#' + id);
  }
  $$('[data-bio]').forEach(function (b) { b.addEventListener('click', function () { openBio(b.dataset.bio, true); }); });
  $$('dialog.bio').forEach(function (d) {
    d.addEventListener('click', function (e) { if (e.target === d || e.target.closest('[data-close]')) d.close(); });
    d.addEventListener('close', function () { history.replaceState(null, '', location.pathname + location.search); });
  });
  if ($('dialog.bio') && location.hash.length > 1) openBio(location.hash.slice(1));
  var tgt = location.hash.length > 1 && document.getElementById(location.hash.slice(1));
  if (tgt && tgt.classList.contains('profile')) tgt.classList.add('is-target');

  /* ---------- carousel ---------- */
  $$('[data-carousel]').forEach(function (car) {
    var track = $('.car-track', car), cards = $$('.profile', track), bar = $('.car-progress i', car), count = $('.car-count', car), btns = $$('.car-btn', car);
    var pad = function (n) { return (n < 10 ? '0' : '') + n; };
    var sync = function () {
      var max = track.scrollWidth - track.clientWidth, x = Math.abs(track.scrollLeft), p = max > 0 ? x / max : 1;
      var step = cards.length > 1 ? Math.abs(cards[1].offsetLeft - cards[0].offsetLeft) : 1;
      var vis = Math.max(1, Math.round(track.clientWidth / step)), last = Math.min(cards.length, Math.round(x / step) + vis);
      bar.style.inlineSize = Math.max(8, Math.min(100, (vis / cards.length + p * (1 - vis / cards.length)) * 100)) + '%';
      count.textContent = pad(last) + ' / ' + pad(cards.length);
      btns[0].disabled = x < 4; btns[1].disabled = x > max - 4;
    };
    btns.forEach(function (b) { b.addEventListener('click', function () {
      var step = cards.length > 1 ? Math.abs(cards[1].offsetLeft - cards[0].offsetLeft) : track.clientWidth;
      track.scrollBy({ left: step * (+b.dataset.dir) * (RTL ? -1 : 1), behavior: reduce ? 'auto' : 'smooth' });
    }); });
    track.addEventListener('scroll', function () { requestAnimationFrame(sync); }, { passive: true });
    window.addEventListener('resize', sync); sync();
  });

  /* ---------- demand diagnostic ---------- */
  var diag = $('#diag');
  if (diag) {
    var qs = $$('.diag-q', diag), res = $('#diag-result'), title = $('#diag-title'), text = $('#diag-text'), cta = $('#diag-cta');
    var update = function () {
      var on = qs.filter(function (q) { return q.getAttribute('aria-pressed') === 'true'; });
      qs.forEach(function (q) { $('.state', q).textContent = q.getAttribute('aria-pressed') === 'true' ? T.q_marked : T.q_tap; });
      res.classList.toggle('has', on.length > 0);
      if (!on.length) { title.textContent = T.q_none_h; text.textContent = T.q_none_p; cta.href = 'contact.html'; return; }
      var names = on.map(function (q) { return q.dataset.name; }).join(T.sep);
      title.textContent = on.length === 1 ? fmt(T.q_one, { x: names }) : fmt(T.q_many, { n: on.length, x: names });
      text.textContent = fmt(T.q_start, { x: on.map(function (q) { return q.dataset.sol; }).join(T.sep2) }) + (on.length > 2 ? T.q_poc : '');
      cta.href = 'contact.html?topic=' + (on.length === 1 ? on[0].dataset.right : 'poc') + '&gaps=' + encodeURIComponent(names);
    };
    qs.forEach(function (q) { q.addEventListener('click', function () { q.setAttribute('aria-pressed', q.getAttribute('aria-pressed') !== 'true'); update(); }); });
  }

  /* ---------- contact form ----------
     With a form key set in content.py the enquiry is sent from inside the page and the
     visitor sees a thank-you. Without one it opens the visitor's own email, as before. */
  var form = $('#contact-form');
  if (form) {
    var params = new URLSearchParams(location.search), topic = params.get('topic'), gaps = params.get('gaps');
    if (params.get('type') === 'rfp') $('#ty-rfp').checked = true;
    if (params.get('type') === 'call') $('#ty-call').checked = true;
    if (topic && topic !== 'poc' && $('#f-topic option[value="' + topic + '"]')) $('#f-topic').value = topic;
    if (gaps && !$('#f-msg').value) $('#f-msg').value = fmt(T.q_prefill, { x: gaps }) + '\n\n';
    var val = function (n) { return (form.elements[n].value || '').trim(); };
    var compose = function () {
      var sel = form.elements.topic;
      return {
        subject: val('type') + ' — ' + (val('company') || T.m_new),
        pillar: sel.options[sel.selectedIndex].text,
        body: [T.m_enquiry + ': ' + val('type'), T.ct_name + ': ' + val('name'), T.ct_role + ': ' + val('role'), T.ct_company + ': ' + val('company'), T.ct_email + ': ' + val('email'),
          T.m_pillar + ': ' + sel.options[sel.selectedIndex].text, '', val('message')].join('\n')
      };
    };
    var endpoint = form.getAttribute('data-endpoint'), key = form.getAttribute('data-key');
    var done = $('#form-done'), ferr = $('#form-error'), sendBtn = $('button[type="submit"]', form);
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var m = compose();
      if (!endpoint || !key || !window.fetch) {
        location.href = 'mailto:info@kiyan.sa?subject=' + encodeURIComponent(m.subject) + '&body=' + encodeURIComponent(m.body);
        return;
      }
      if (form.elements.botcheck.checked) return;          // a field people never see; only bots tick it
      var label = sendBtn.innerHTML, type = val('type');
      ferr.hidden = true; form.classList.add('is-sending'); sendBtn.textContent = sendBtn.getAttribute('data-sending');
      fetch(endpoint, {
        method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify({ access_key: key, subject: m.subject, from_name: 'Kiyan website', enquiry_type: type, name: val('name'), role: val('role'),
          company: val('company'), email: val('email'), pillar: m.pillar, message: val('message'), language: document.documentElement.lang, page: location.href })
      }).then(function (r) { return r.json().then(function (d) { if (!r.ok || d.success === false) throw new Error('send failed'); }); })
        .then(function () {
          form.reset(); form.hidden = true; done.hidden = false; done.focus();
          window.dataLayer.push({ event: 'contact_form_submit', enquiry_type: type });
        })
        .catch(function () { ferr.hidden = false; })
        .then(function () { form.classList.remove('is-sending'); sendBtn.innerHTML = label; });
    });
    var again = $('#form-again');
    if (again) again.addEventListener('click', function () { done.hidden = true; form.hidden = false; form.elements.name.focus(); });
    $('#wa-send').addEventListener('click', function (e) {
      var m = compose(); this.href = this.href.split('?')[0] + '?text=' + encodeURIComponent(m.subject + '\n\n' + m.body);
    });
  }

  /* ---------- pillars page: the navigator follows the section on screen ---------- */
  var pnav = $('#pnav');
  if (pnav) {
    var plinks = $$('a', pnav), psecs = plinks.map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); });
    var pwrap = $('.wrap', pnav), pcur = -1, pwait = 0;
    var spy = function () {
      var cur = -1;
      psecs.forEach(function (sec, i) { if (sec && sec.getBoundingClientRect().top <= 170) cur = i; });
      if (cur === pcur) return; pcur = cur;
      plinks.forEach(function (a, i) { a.classList.toggle('is-current', i === cur); if (i === cur) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current'); });
      if (cur >= 0) pwrap.scrollTo({ left: plinks[cur].offsetLeft - (pwrap.clientWidth - plinks[cur].offsetWidth) / 2, behavior: reduce ? 'auto' : 'smooth' });
    };
    window.addEventListener('scroll', function () { var n = Date.now(); if (n - pwait > 80) { pwait = n; spy(); } }, { passive: true });
    window.addEventListener('scrollend', spy); spy();
  }

  /* ---------- articles: copy link ---------- */
  $$('[data-copy]').forEach(function (b) {
    b.addEventListener('click', function () {
      var url = location.href.split('#')[0], label = b.textContent;
      var ok = function () { b.textContent = b.getAttribute('data-done'); setTimeout(function () { b.textContent = label; }, 1800); };
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(url).then(ok, function () { window.prompt('', url); });
      else window.prompt('', url);
    });
  });

  /* ---------- search palette ---------- */
  var sd = $('#search'), si = $('#search-input'), sr = $('#search-results'), active = 0, hits = [];
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function renderSearch() {
    var q = si.value.trim().toLowerCase(), idx = window.KIYAN_INDEX || [];
    if (!q) hits = idx.slice(0, 12);
    else {
      var terms = q.split(/\s+/);
      hits = idx.map(function (x) {
        var t = x.t.toLowerCase(), all = (x.t + ' ' + x.d + ' ' + (x.x || '') + ' ' + x.k).toLowerCase(), s = 0;
        for (var i = 0; i < terms.length; i++) { if (all.indexOf(terms[i]) < 0) return null; s += t.indexOf(terms[i]) > -1 ? (t.indexOf(terms[i]) === 0 ? 6 : 4) : 1; }
        return { x: x, s: s };
      }).filter(Boolean).sort(function (a, b) { return b.s - a.s; }).slice(0, 10).map(function (h) { return h.x; });
    }
    active = 0;
    sr.innerHTML = hits.length ? hits.map(function (x, i) {
      return '<a href="' + x.u + '" role="option" class="' + (i === 0 ? 'active' : '') + '"><span class="k">' + esc(x.k) + '</span><strong>' + esc(x.t) + '</strong><span>' + esc(x.d) + '</span></a>';
    }).join('') : '<div class="search-empty">' + esc(fmt(T.s_empty, { q: si.value })) + '</div>';
  }
  function openSearch() { if (!sd || !sd.showModal) return; setMenu(false); sd.showModal(); si.value = ''; renderSearch(); si.focus(); }
  if (sd) {
    $('#search-open').addEventListener('click', openSearch);
    $('#search-close').addEventListener('click', function () { sd.close(); });
    sd.addEventListener('click', function (e) { if (e.target === sd) sd.close(); });
    si.addEventListener('input', renderSearch);
    si.addEventListener('keydown', function (e) {
      var links = $$('a[role="option"]', sr);
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        e.preventDefault(); if (!links.length) return;
        active = (active + (e.key === 'ArrowDown' ? 1 : -1) + links.length) % links.length;
        links.forEach(function (l, i) { l.classList.toggle('active', i === active); });
        links[active].scrollIntoView({ block: 'nearest' });
      } else if (e.key === 'Enter' && links[active]) { e.preventDefault(); sd.close(); location.href = links[active].getAttribute('href'); }
    });
    sr.addEventListener('click', function (e) { if (e.target.closest('a')) sd.close(); });
    document.addEventListener('keydown', function (e) {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); sd.open ? sd.close() : openSearch(); }
      else if (e.key === '/' && !/input|textarea|select/i.test(document.activeElement.tagName) && !sd.open) { e.preventDefault(); openSearch(); }
    });
    if (!/Mac|iPhone|iPad/.test(navigator.platform)) { var k = $('#search-open kbd'); if (k) k.textContent = 'Ctrl K'; }
  }

  /* ---------- hero: signal resolving into a shelf ----------
     Scattered points (raw market signal) settle into an ordered planogram
     (a decision on the shelf), then drift apart again. */
  var cv = $('#hero-canvas');
  if (cv && cv.getContext) {
    var ctx = cv.getContext('2d'), W = 0, H = 0, dpr = 1, pts = [], t0 = performance.now(), raf = 0, visible = true;
    var bar = $('#hero-bar'), label = $('#hero-label');
    var COLORS = ['#F5F5F3', '#F5F5F3', '#F5F5F3', '#2D6DF6', '#2D6DF6', '#86BC25'];
    var rand = (function (s) { return function () { s = (s * 16807) % 2147483647; return (s - 1) / 2147483646; }; })(20261);
    var build = function () {
      var r = cv.getBoundingClientRect(); dpr = Math.min(window.devicePixelRatio || 1, 2);
      W = r.width; H = r.height; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      pts = [];
      var narrow = W < 820;
      var gx0 = narrow ? W * 0.08 : W * 0.61, gx1 = W * (narrow ? 0.92 : 0.95), gy0 = narrow ? H - 190 : H * 0.16, gy1 = narrow ? H - 56 : H * 0.84;
      var shelves = narrow ? 4 : 6, step = narrow ? 13 : 15, perShelf = 3;
      var shelfH = (gy1 - gy0) / shelves, cols = Math.floor((gx1 - gx0) / step);
      for (var s = 0; s < shelves; s++) {
        var c = 0;
        while (c < cols) {
          var width = 3 + Math.floor(rand() * 6), color = COLORS[Math.floor(rand() * COLORS.length)], gap = rand() > 0.9;
          for (var k = 0; k < width && c < cols; k++, c++) {
            for (var rr = 0; rr < perShelf; rr++) {
              if (gap && rr < 2) continue;
              pts.push({
                tx: RTL && !narrow ? W - (gx0 + c * step) : gx0 + c * step, ty: gy0 + s * shelfH + shelfH - 14 - rr * step,
                sx: narrow ? rand() * W : (RTL ? rand() * W * 0.6 - W * 0.02 : rand() * W * 0.6 + W * 0.42), sy: rand() * H,
                ph: rand() * 6.28, sp: 0.4 + rand() * 0.9, amp: 14 + rand() * 30, color: color, d: rand() * 0.35,
                r: color === '#F5F5F3' ? 1.6 : 2.1
              });
            }
          }
          c += 1;
        }
      }
      if (RTL && !narrow) { var a0 = W - gx1, a1 = W - gx0; gx0 = a0; gx1 = a1; }
      cv._shelf = { gx0: gx0, gx1: gx1, gy0: gy0, shelfH: shelfH, shelves: shelves };
    };
    var ease = function (x) { return x < 0 ? 0 : x > 1 ? 1 : x * x * (3 - 2 * x); };
    var frame = function (now) {
      var t = (now - t0) / 1000, cycle = 11, ph = (t % cycle) / cycle;
      // 0–.18 scattered · .18–.46 forming · .46–.82 ordered · .82–1 releasing
      var p = reduce ? 1 : ph < 0.18 ? 0 : ph < 0.46 ? (ph - 0.18) / 0.28 : ph < 0.82 ? 1 : 1 - (ph - 0.82) / 0.18;
      ctx.clearRect(0, 0, W, H);
      var sh = cv._shelf, eg = ease(p);
      ctx.strokeStyle = 'rgba(245,245,243,' + (0.16 * eg) + ')'; ctx.lineWidth = 1;
      for (var s = 0; s < sh.shelves; s++) {
        var y = sh.gy0 + (s + 1) * sh.shelfH - 5;
        ctx.beginPath(); if (RTL) { ctx.moveTo(sh.gx1 + 8, y); ctx.lineTo(sh.gx1 + 8 - (sh.gx1 - sh.gx0 + 16) * eg, y); } else { ctx.moveTo(sh.gx0 - 8, y); ctx.lineTo(sh.gx0 - 8 + (sh.gx1 - sh.gx0 + 16) * eg, y); } ctx.stroke();
      }
      for (var i = 0; i < pts.length; i++) {
        var q = pts[i], k = ease((p - q.d) / (1 - 0.35));
        var dx = Math.cos(t * q.sp + q.ph) * q.amp, dy = Math.sin(t * q.sp * 0.8 + q.ph * 1.7) * q.amp;
        var x = q.sx + dx + (q.tx - q.sx - dx) * k, yy = q.sy + dy + (q.ty - q.sy - dy) * k;
        ctx.globalAlpha = q.color === '#F5F5F3' ? 0.22 + 0.4 * k : 0.5 + 0.5 * k;
        ctx.fillStyle = q.color;
        ctx.beginPath(); ctx.arc(x, yy, q.r + k * 1.4, 0, 6.2832); ctx.fill();
      }
      ctx.globalAlpha = 1;
      if (bar) bar.style.setProperty('--p', eg.toFixed(3));
      if (label) label.style.opacity = 0.35 + 0.65 * eg;
      if (!reduce && visible) raf = requestAnimationFrame(frame);
    };
    build(); raf = requestAnimationFrame(frame);
    var rz; window.addEventListener('resize', function () { clearTimeout(rz); rz = setTimeout(function () { build(); if (reduce) frame(performance.now()); }, 150); });
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es) {
      visible = es[0].isIntersecting; cancelAnimationFrame(raf); if (visible) raf = requestAnimationFrame(frame);
    }).observe(cv);
  }
})();
