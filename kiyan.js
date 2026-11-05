/* Kiyan landing: micro-interactions. Everything here is additive; the page reads fully without it. */
(function () {
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = matchMedia('(hover: hover) and (pointer: fine)').matches;
  var clamp = function (v, a, b) { return Math.max(a, Math.min(b, v)); };
  var lerp = function (a, b, t) { return a + (b - a) * t; };

  /* nav: open/close, scrolled state */
  var nav = document.getElementById('nav'), toggle = nav.querySelector('.nav__toggle');
  toggle.addEventListener('click', function () { var o = nav.classList.toggle('is-open'); toggle.setAttribute('aria-expanded', o); });
  nav.querySelectorAll('.nav__menu a').forEach(function (a) { a.addEventListener('click', function () { nav.classList.remove('is-open'); toggle.setAttribute('aria-expanded', 'false'); }); });

  /* nav scrollspy: a pill slides under the link of the section in view */
  var links = Array.prototype.slice.call(nav.querySelectorAll('.nav__links a'));
  var ind = nav.querySelector('.nav__ind');
  var targets = links.map(function (a) { return document.querySelector(a.getAttribute('href')); });
  function moveInd(a) {
    if (!ind || !a) { if (ind) ind.style.opacity = 0; return; }
    var r = a.getBoundingClientRect(), p = a.parentElement.getBoundingClientRect();
    ind.style.transform = 'translateX(' + (r.left - p.left) + 'px)';
    ind.style.width = r.width + 'px';
    ind.style.opacity = 1;
  }
  links.forEach(function (a) {
    a.addEventListener('mouseenter', function () { moveInd(a); });
    a.addEventListener('mouseleave', function () { moveInd(current); });
  });
  var current = null;
  function spy() {
    var y = window.innerHeight * 0.4, best = null;
    targets.forEach(function (t, i) { if (t) { var r = t.getBoundingClientRect(); if (r.top <= y && r.bottom > y) best = links[i]; } });
    if (best !== current) { current = best; links.forEach(function (a) { a.classList.toggle('is-active', a === best); }); moveInd(best); }
  }

  /* progress bar */
  var bar = document.getElementById('progress');
  function progress() {
    var h = document.documentElement.scrollHeight - innerHeight;
    if (bar) bar.style.transform = 'scaleX(' + (h > 0 ? scrollY / h : 0) + ')';
  }

  /* reveals (once) and counters */
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (!e.isIntersecting) return;
      e.target.classList.add('in');
      io.unobserve(e.target);
    });
  }, { rootMargin: '0px 0px -10% 0px' });
  document.querySelectorAll('.q, .person, .section-head, .split__copy, .pillar__head, .pillar__body, .pillar__aside, .tcol, .form, .cta__copy, .poc__copy, .poc__photo, .pareto, .storemap, .objective, .model, .step').forEach(function (el) { el.classList.add('reveal'); io.observe(el); });

  document.querySelectorAll('[data-count]').forEach(function (el) {
    var to = parseInt(el.getAttribute('data-count'), 10);
    if (reduce) { el.textContent = to; return; }
    var t0 = null, dur = 1100;
    function tick(ts) {
      if (!t0) t0 = ts;
      var k = clamp((ts - t0) / dur, 0, 1); k = 1 - Math.pow(1 - k, 3);
      el.textContent = Math.round(to * k);
      if (k < 1) requestAnimationFrame(tick);
    }
    setTimeout(function () { requestAnimationFrame(tick); }, 350);
  });

  /* hero: pointer parallax on the scene, planes and floats at different depths */
  var scene = document.querySelector('[data-tilt]');
  var mx = 0, my = 0, tx = 0, ty = 0;
  if (scene && fine && !reduce) {
    var layers = [
      { el: scene.querySelector('.scene__plane--green'), d: 10 },
      { el: scene.querySelector('.scene__plane--centre'), d: 16 },
      { el: scene.querySelector('.scene__plane--blue'), d: 24 },
      { el: scene.querySelector('.float--ladder'), d: 30 },
      { el: scene.querySelector('.float--space'), d: 26 },
      { el: scene.querySelector('.float--academy'), d: 34 }
    ];
    var hero = document.querySelector('.hero');
    hero.addEventListener('pointermove', function (e) {
      var r = hero.getBoundingClientRect();
      tx = ((e.clientX - r.left) / r.width - 0.5) * 2;
      ty = ((e.clientY - r.top) / r.height - 0.5) * 2;
    });
    hero.addEventListener('pointerleave', function () { tx = 0; ty = 0; });
    (function loop() {
      mx = lerp(mx, tx, 0.08); my = lerp(my, ty, 0.08);
      layers.forEach(function (l) { if (l.el) l.el.style.setProperty('--px', (mx * l.d).toFixed(2) + 'px'); if (l.el) l.el.style.setProperty('--py', (my * l.d).toFixed(2) + 'px'); });
      scene.style.setProperty('--rx', (-my * 3).toFixed(2) + 'deg');
      scene.style.setProperty('--ry', (mx * 4).toFixed(2) + 'deg');
      requestAnimationFrame(loop);
    })();
  }

  /* magnetic primary buttons (hero and form) */
  if (fine && !reduce) {
    document.querySelectorAll('.btn--primary.btn--lg').forEach(function (b) {
      var bx = 0, by = 0, gx = 0, gy = 0, raf;
      function run() { bx = lerp(bx, gx, 0.18); by = lerp(by, gy, 0.18); b.style.setProperty('--mx', bx.toFixed(2) + 'px'); b.style.setProperty('--my', by.toFixed(2) + 'px'); if (Math.abs(bx - gx) > 0.1 || Math.abs(by - gy) > 0.1) raf = requestAnimationFrame(run); }
      b.addEventListener('pointermove', function (e) { var r = b.getBoundingClientRect(); gx = (e.clientX - r.left - r.width / 2) * 0.22; gy = (e.clientY - r.top - r.height / 2) * 0.32; cancelAnimationFrame(raf); run(); });
      b.addEventListener('pointerleave', function () { gx = 0; gy = 0; cancelAnimationFrame(raf); run(); });
    });
  }

  /* spotlight: a soft light follows the pointer across the space cards */
  if (fine) {
    document.querySelectorAll('[data-spot]').forEach(function (c) {
      c.addEventListener('pointermove', function (e) { var r = c.getBoundingClientRect(); c.style.setProperty('--sx', ((e.clientX - r.left) / r.width * 100).toFixed(1) + '%'); c.style.setProperty('--sy', ((e.clientY - r.top) / r.height * 100).toFixed(1) + '%'); });
    });
  }

  /* the ladder: built by scroll. p runs 0 to 1 while the panel travels from the lower
     viewport edge to its centre; each rung lands in turn, the line draws, Impact fills last. */
  var ladder = document.querySelector('[data-ladder]');
  var stepEl = document.querySelector('[data-ladder-step]'), labelEl = document.querySelector('[data-ladder-label]');
  var ladderList = ladder ? ladder.querySelector('.ladder') : null;
  var names = ladderList && ladderList.getAttribute('data-labels') ? ladderList.getAttribute('data-labels').split('|') : ['Data', 'Information', 'Knowledge', 'Wisdom', 'Impact'];
  var N = names.length;
  var lp = reduce ? 1 : 0, lastStep = -1;
  function ladderFrame() {
    if (!ladder) return;
    var r = ladder.getBoundingClientRect(), vh = innerHeight;
    var target = reduce ? 1 : clamp((vh * 0.92 - r.top) / (vh * 0.55 + r.height * 0.25), 0, 1);
    lp = lerp(lp, target, reduce ? 1 : 0.14);
    if (Math.abs(lp - target) < 0.002) lp = target;
    ladder.style.setProperty('--p', lp.toFixed(4));
    var step = clamp(Math.floor(lp * (N + 0.4)), 0, N - 1);
    if (step !== lastStep) {
      lastStep = step;
      if (stepEl) stepEl.textContent = 'Stage ' + (step + 1) + ' of ' + N;
      if (labelEl) { labelEl.textContent = names[step]; labelEl.classList.remove('swap'); void labelEl.offsetWidth; labelEl.classList.add('swap'); }
      ladder.classList.toggle('is-built', step === N - 1 && lp > 0.96);
    }
    if (lp === 1 && !ladder.classList.contains('is-built')) ladder.classList.add('is-built');
  }

  /* one scroll loop */
  var ticking = false;
  function onScroll() {
    if (ticking) return; ticking = true;
    requestAnimationFrame(function () {
      nav.classList.toggle('is-scrolled', scrollY > 8);
      spy(); progress(); ladderFrame();
      ticking = false;
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', function () { moveInd(current); onScroll(); });
  // the ladder settles with a lerp, so keep drawing while it moves
  (function settle() { ladderFrame(); requestAnimationFrame(settle); })();
  onScroll(); spy(); progress();
})();
