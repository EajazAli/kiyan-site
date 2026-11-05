/* Kiyan hero: a green particle wave in three.js (r128, loaded from cdnjs). Falls back to the still image
   when WebGL or the library is unavailable, and holds still under reduced motion. */
(function () {
  var canvas = document.getElementById('wave');
  if (!canvas || typeof THREE === 'undefined') return;
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var renderer;
  try { renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true, powerPreference: 'low-power' }); }
  catch (e) { return; }
  renderer.setPixelRatio(Math.min(devicePixelRatio || 1, 2));
  renderer.setClearColor(0x000000, 0);
  canvas.parentElement.classList.add('has-gl');

  var scene = new THREE.Scene();
  scene.fog = new THREE.Fog(0x0d0f10, 70, 190);
  var camera = new THREE.PerspectiveCamera(50, 2, 1, 400);
  camera.position.set(0, 30, 96);
  camera.lookAt(0, -10, 0);

  var COLS = 170, ROWS = 70, SX = 1.4, SZ = 1.5;
  var count = COLS * ROWS;
  var pos = new Float32Array(count * 3), col = new Float32Array(count * 3), base = new Float32Array(count * 2);
  var g = new THREE.Color(0x86bc25), dim = new THREE.Color(0x2a4a0c), blue = new THREE.Color(0x2d6df6);
  var i = 0;
  for (var r = 0; r < ROWS; r++) for (var c = 0; c < COLS; c++) {
    var x = (c - COLS / 2) * SX, z = (r - ROWS / 2) * SZ;
    pos[i * 3] = x; pos[i * 3 + 1] = 0; pos[i * 3 + 2] = z;
    base[i * 2] = x; base[i * 2 + 1] = z;
    i++;
  }
  var geo = new THREE.BufferGeometry();
  geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  geo.setAttribute('color', new THREE.BufferAttribute(col, 3));
  // a round, soft sprite so the points read as light, not squares
  var sc = document.createElement('canvas'); sc.width = sc.height = 64;
  var g2 = sc.getContext('2d'), grd = g2.createRadialGradient(32, 32, 0, 32, 32, 32);
  grd.addColorStop(0, 'rgba(255,255,255,1)'); grd.addColorStop(0.35, 'rgba(255,255,255,.85)'); grd.addColorStop(1, 'rgba(255,255,255,0)');
  g2.fillStyle = grd; g2.fillRect(0, 0, 64, 64);
  var sprite = new THREE.CanvasTexture(sc);
  var mat = new THREE.PointsMaterial({ size: 1.6, map: sprite, vertexColors: true, transparent: true, opacity: 0.9, sizeAttenuation: true, depthWrite: false, blending: THREE.AdditiveBlending });
  var points = new THREE.Points(geo, mat);
  scene.add(points);

  var mx = 0, my = 0, tx = 0, ty = 0;
  var hero = canvas.closest('.hero');
  if (hero && matchMedia('(hover: hover) and (pointer: fine)').matches) {
    hero.addEventListener('pointermove', function (e) { var r = hero.getBoundingClientRect(); tx = ((e.clientX - r.left) / r.width - 0.5) * 2; ty = ((e.clientY - r.top) / r.height - 0.5) * 2; });
    hero.addEventListener('pointerleave', function () { tx = 0; ty = 0; });
  }

  function resize() {
    var w = canvas.clientWidth, h = canvas.clientHeight;
    if (!w || !h) return;
    renderer.setSize(w, h, false);
    camera.aspect = w / h; camera.updateProjectionMatrix();
  }
  window.addEventListener('resize', resize); resize();

  var t = 0, visible = true, tmp = new THREE.Color();
  var io = new IntersectionObserver(function (es) { visible = es[0].isIntersecting; }, { threshold: 0 });
  io.observe(canvas);

  function frame(ts) {
    if (!reduce) t = ts * 0.00045;
    mx += (tx - mx) * 0.05; my += (ty - my) * 0.05;
    var p = geo.attributes.position.array, cl = geo.attributes.color.array;
    for (var k = 0; k < count; k++) {
      var x = base[k * 2], z = base[k * 2 + 1];
      var y = Math.sin(x * 0.085 + t * 1.6) * 2.4
            + Math.sin(z * 0.14 - t * 1.1) * 1.8
            + Math.sin((x + z) * 0.05 + t * 0.7) * 2.8
            + Math.cos(x * 0.03 - z * 0.07 + t) * 1.2 - 6;
      p[k * 3 + 1] = y;
      var h = (y + 14) / 16; // 0 low .. 1 high
      tmp.copy(dim).lerp(g, Math.min(1, Math.max(0, h * 1.25)));
      if (h > 0.82) tmp.lerp(blue, (h - 0.82) * 0.9);
      cl[k * 3] = tmp.r; cl[k * 3 + 1] = tmp.g; cl[k * 3 + 2] = tmp.b;
    }
    geo.attributes.position.needsUpdate = true;
    geo.attributes.color.needsUpdate = true;
    camera.position.x = mx * 10; camera.position.y = 30 - my * 5;
    camera.lookAt(0, -10, 0);
    renderer.render(scene, camera);
    if (!reduce && visible) requestAnimationFrame(frame); else if (!reduce) setTimeout(function () { requestAnimationFrame(frame); }, 400);
  }
  requestAnimationFrame(frame);
})();
