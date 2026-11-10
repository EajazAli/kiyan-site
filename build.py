#!/usr/bin/env python3
"""Kiyan website generator (English + Arabic). No dependencies, Python 3.12+.
`python3 build.py` rewrites every page in / (English) and /ar/ (Arabic), the
sitemap, robots.txt, llms.txt and the search data from content.py,
content_ar.py and data/team.json."""
import json, math, html, datetime, pathlib
import content as EN
import content_ar as AR

ROOT = pathlib.Path(__file__).parent
TEAM = json.loads((ROOT / "data/team.json").read_text(encoding="utf-8"))
TODAY = datetime.date.today().isoformat()
e = html.escape
BASE = EN.SITE["url"]

# Set per language by build_language()
C = EN          # content module
A = ""          # asset prefix ("" for English at the root, "../" for /ar/)
OUT = ROOT      # output directory
SITEMAP = []

def t(k): return C.UI[k]
def is_ar(): return C.LANG == "ar"
def url_for(lang, fname):
    return BASE + "/" + ("ar/" if lang == "ar" else "") + ("" if fname == "index.html" else fname)

def people():
    out = []
    for p in TEAM["people"]:
        q = dict(p)
        if is_ar() and p.get("ar"):
            q.update({k: v for k, v in p["ar"].items() if v or k == "career"})
        q["focus_labels"] = [C.FOCUS_LABELS.get(f, f) for f in p["focus"]]
        q["latin_name"] = p["name"]
        out.append(q)
    return out

# ----------------------------------------------------------------- icons
I = {
 "arrow": '<svg class="arr" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M2 8h11M9 3.5 13.5 8 9 12.5"/></svg>',
 "chev": '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="m2.5 4.5 3.5 3.5 3.5-3.5"/></svg>',
 "search": '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="9" cy="9" r="5.5"/><path d="m13.5 13.5 4 4"/></svg>',
 "sun": '<svg class="sun" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="10" cy="10" r="3.6"/><path d="M10 1.8v2M10 16.2v2M1.8 10h2M16.2 10h2M4.2 4.2l1.4 1.4M14.4 14.4l1.4 1.4M4.2 15.8l1.4-1.4M14.4 5.6l1.4-1.4"/></svg>',
 "moon": '<svg class="moon" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M16.5 12.2A7 7 0 0 1 7.8 3.5a7 7 0 1 0 8.7 8.7Z"/></svg>',
 "menu": '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M3 6.5h14M3 13.5h14"/></svg>',
 "close": '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="m5 5 10 10M15 5 5 15"/></svg>',
 "mail": '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="2.5" y="4.5" width="15" height="11" rx="2"/><path d="m3 6 7 5 7-5"/></svg>',
 "in": '<svg viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path d="M4.5 7.5h2.6V16H4.5zM5.8 3.6a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM8.8 7.5h2.5v1.2c.4-.8 1.4-1.4 2.7-1.4 2.4 0 3 1.5 3 3.8V16h-2.6v-4.3c0-1.1-.3-1.9-1.3-1.9-1.2 0-1.7.8-1.7 2V16H8.8z"/></svg>',
 "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2.2a9.7 9.7 0 0 0-8.3 14.8L2.3 21.8l4.9-1.3A9.7 9.7 0 1 0 12 2.2Zm0 1.8a7.9 7.9 0 1 1-4 14.7l-.3-.2-2.8.7.8-2.7-.2-.3A7.9 7.9 0 0 1 12 4Zm-3.3 3.9c-.2 0-.5.1-.7.4-.3.3-1 1-1 2.3 0 1.4 1 2.7 1.2 2.9.1.2 2 3.1 4.9 4.3 2.4 1 2.9.8 3.4.7.5 0 1.7-.7 1.9-1.3.2-.7.2-1.2.2-1.3-.1-.1-.3-.2-.6-.4l-1.9-.9c-.3-.1-.5-.1-.7.2l-.9 1.1c-.2.2-.3.2-.6.1-.3-.2-1.2-.5-2.3-1.4-.8-.8-1.4-1.7-1.6-2-.2-.3 0-.5.1-.6l.4-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.1c-.2-.5-.4-.5-.6-.5h-.6Z"/></svg>',
 "globe": '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="10" cy="10" r="7.2"/><path d="M2.8 10h14.4M10 2.8c2.4 2.2 2.4 12.2 0 14.4M10 2.8c-2.4 2.2-2.4 12.2 0 14.4"/></svg>',
}


def _ic(d): return f'<svg class="mi" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'
MI = {
 "reach": _ic('<path d="M12 21s-6.5-5.6-6.5-10.5a6.5 6.5 0 0 1 13 0C18.500 15.400 12 21 12 21Z"/><circle cx="12" cy="10.5" r="2.3"/>'),
 "category": _ic('<rect x="3.5" y="3.5" width="7" height="7" rx="1.2"/><rect x="13.5" y="3.5" width="7" height="7" rx="1.2"/><rect x="3.5" y="13.5" width="7" height="7" rx="1.2"/><rect x="13.5" y="13.5" width="7" height="7" rx="1.2"/>'),
 "range": _ic('<path d="M4 20V5M9.300 20v-9M14.700 20v-5M20 20v-2.5"/>'),
 "store": _ic('<path d="M4 10v10h16V10M3 10l1.500-5.500h15L21 10a3 3 0 0 1-6 0 3 3 0 0 1-6 0 3 3 0 0 1-6 0ZM10 20v-5h4v5"/>'),
 "space": _ic('<rect x="3.5" y="3.5" width="17" height="17" rx="1.5"/><path d="M3.500 9.200h17M3.500 14.800h17M8 6v3.200M12 6v3.200M15 11.600v3.200M8 17.400v3.1"/>'),
 "execution": _ic('<circle cx="12" cy="12" r="8.5"/><path d="m8.200 12.300 2.600 2.600 5-5.4"/>'),
 "table": _ic('<circle cx="12" cy="12" r="3.2"/><circle cx="12" cy="4.5" r="1.8"/><circle cx="5.5" cy="16" r="1.8"/><circle cx="18.5" cy="16" r="1.8"/>'),
 "gap": _ic('<path d="M4 5h16M6.500 10h11M9 15h6M11 20h2"/>'),
 "people": _ic('<circle cx="9" cy="8.5" r="3.2"/><path d="M3 19.500c.500-3.300 3-5 6-5s5.500 1.700 6 5M16 5.600a3.200 3.200 0 0 1 0 5.800M17.500 14.800c1.900.600 3.100 2.200 3.500 4.7"/>'),
 "flask": _ic('<path d="M9.500 3.500h5M10.500 3.500v5.700L5 18.500a1.400 1.400 0 0 0 1.200 2h11.600a1.400 1.400 0 0 0 1.200-2l-5.500-9.300V3.500M7.800 14.500h8.4"/>'),
 "help": _ic('<circle cx="12" cy="12" r="8.5"/><path d="M9.700 9.600a2.400 2.400 0 1 1 3.500 2.100c-.800.500-1.200 1-1.200 2M12 16.700v.100"/>'),
 "case": _ic('<rect x="3.5" y="7.5" width="17" height="12" rx="1.8"/><path d="M9 7.500V5.300h6v2.200M3.500 12.500h17"/>'),
 "mail": _ic('<rect x="3.5" y="5.5" width="17" height="13" rx="1.8"/><path d="m4 7 8 6 8-6"/>'),
}

# ------------------------------------------------- generative dot-matrix art
def art(kind, cols=48, rows=20):
    """Deterministic dot-matrix illustration, one per pillar. Each grid cell is a
    dot whose size and colour follow a rule that pictures what the pillar does."""
    cell = 20
    w, h = cols * cell, rows * cell
    def rnd(i, j, s=1):
        v = math.sin(i * 127.1 + j * 311.7 + s * 74.7) * 43758.5453
        return v - math.floor(v)
    def shelf(i, j, gaps=.93):
        s, k = j // 4, j % 4
        if k == 3: return 0, None
        block = int((i + s * 5) / (5 + s % 3)); r = rnd(block, s, 3)
        if rnd(i // 2, s, 9) > gaps: return .06, None
        return .35 + r * .55, ("b" if r > .62 else ("g" if r < .16 else None))
    dots = []
    for j in range(rows):
        for i in range(cols):
            x, y = i / (cols - 1), j / (rows - 1)
            v, c = 0.0, None
            if kind == "reach":          # every outlet mapped and graded around its cities
                dens = max(math.exp(-((x - cx) ** 2 * 5 + (y - cy) ** 2) * 9) for cx, cy in [(.2, .55), (.52, .3), (.8, .62)])
                if rnd(i, j, 2) < .12 + dens * .85:
                    g = rnd(i, j, 7)
                    v, c = (1, "g") if g > .9 else ((.7, "b") if g > .68 else (.4, None))
                else: v = .05
            elif kind == "category":     # four roles sized by their share of categories
                for k, (a, b, col) in enumerate([(0, 4, "g"), (6, 32, None), (34, 41, "b"), (43, 47, None)]):
                    if a <= i <= b:
                        v = .5 + .45 * rnd(i, j, k) if k != 3 else .25 + .6 * (0.5 + 0.5 * math.sin(j * 1.1))
                        c = col
            elif kind == "range":        # a few lines carry the category: the Pareto curve and its tail
                height = .1 + .86 * math.exp(-x * 4.2)
                if i % 2 == 1: v = 0
                elif y >= 1 - height:
                    c = "g" if x < .1 else ("b" if x < .22 else None); v = .75 if c else .35
                else: v = .05
            elif kind == "store":        # stores grouped into clusters that behave alike
                v = .08
                for k, (cx, cy, r) in enumerate([(.17, .6, .13), (.42, .32, .16), (.7, .6, .22), (.9, .25, .1)]):
                    d = math.hypot((x - cx) * 2.4, y - cy)
                    if d < r: v = max(v, 1 - d / r * .75); c = "g" if k == 2 else ("b" if k % 2 else None)
            elif kind == "space":        # a planogram: shelves, blocks and facings
                v, c = shelf(i, j)
            elif kind == "execution":    # the same shelf audited: gaps flagged, one capture sweeping across
                v, c = shelf(i, j, gaps=.8)
                if v > .1: v, c = .45, None
                if i in (30, 31) and j % 4 != 3: v, c = 1, "g"
                elif v <= .1 and j % 4 != 3 and i < 30: v, c = .5, "b"
            v = max(0, min(1, v))
            if v < .03: continue
            fill = {"g": "#86BC25", "b": "#2D6DF6", None: "#3A3B41"}[c]
            op = "" if c else f' opacity="{round(.45 + v * .55, 2)}"'
            dots.append(f'<circle cx="{i * cell + 10}" cy="{j * cell + 10}" r="{round(1.1 + v * 6.2, 2)}" fill="{fill}"{op}/>')
    return f'<svg viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">' + "".join(dots) + "</svg>"

def art_img(kind):
    f = ROOT / f"assets/img/art-{kind}.svg"
    if C is EN: f.write_text(art(kind), encoding="utf-8")
    return f'<img src="{A}assets/img/art-{kind}.svg" alt="" width="960" height="400" loading="lazy" style="inline-size:100%;block-size:100%;object-fit:cover">'

def universe_svg():
    fam = "Noto Kufi Arabic, sans-serif" if is_ar() else "IBM Plex Mono, monospace"
    ls = "0" if is_ar() else "1.2"; big, small = ("15", "11.5") if is_ar() else ("11", "8.5")
    return f'''<svg viewBox="0 0 520 440" role="img" aria-label="{e(t("svg_label"))}" xmlns="http://www.w3.org/2000/svg" font-family="{fam}" font-size="{big}" letter-spacing="{ls}" direction="{C.DIR}">
<circle cx="260" cy="220" r="208" fill="none" stroke="#86BC25" stroke-width="1.5" stroke-dasharray="2 7" stroke-linecap="round"/>
<circle cx="260" cy="220" r="146" fill="none" stroke="#F5F5F3" stroke-width="1.5"/>
<circle cx="260" cy="220" r="84" fill="#86BC25" fill-opacity=".14" stroke="#86BC25" stroke-width="1.5"/>
<circle cx="260" cy="12" r="5" fill="#86BC25"/><circle cx="406" cy="220" r="5" fill="#F5F5F3"/><circle cx="260" cy="136" r="5" fill="#2D6DF6"/>
<text x="260" y="216" text-anchor="middle" fill="#86BC25">{t("svg_inside")}</text>
<text x="260" y="236" text-anchor="middle" fill="#C6C9CF" font-size="{small}">{t("svg_inside_s")}</text>
<text x="260" y="328" text-anchor="middle" fill="#F5F5F3">{t("svg_store")}</text>
<text x="260" y="345" text-anchor="middle" fill="#A9ADB5" font-size="{small}">{t("svg_store_s")}</text>
<text x="260" y="390" text-anchor="middle" fill="#86BC25">{t("svg_outside")}</text>
<text x="260" y="407" text-anchor="middle" fill="#A9ADB5" font-size="{small}">{t("svg_outside_s")}</text>
</svg>'''

# ------------------------------------------------------------ structured data
def org_ld():
    S = C.SITE
    return {
        "@context": "https://schema.org", "@type": ["Organization", "ProfessionalService"], "@id": BASE + "/#organization",
        "name": "Kiyan", "alternateName": "كيان", "url": BASE + "/", "slogan": S["tagline"], "description": S["description"],
        "logo": BASE + "/assets/img/kiyan-logo.svg", "image": BASE + "/assets/img/og.png",
        "email": S["email"], "telephone": "+" + S["whatsapp"],
        "address": {"@type": "PostalAddress", "addressLocality": "Riyadh", "addressCountry": "SA"},
        "areaServed": [{"@type": "Country", "name": "Saudi Arabia"}],
        "sameAs": [S["linkedin"]],
        "knowsAbout": ["Category management", "Retail execution", "Retail census", "Store universe", "Planogram design", "Assortment optimisation",
                       "Store clustering", "Space planning", "On-shelf availability", "Shelf audit", "Route-to-market", "Joint business planning"],
        "contactPoint": {"@type": "ContactPoint", "contactType": "sales", "email": S["email"], "telephone": "+" + S["whatsapp"], "availableLanguage": ["English", "Arabic"]},
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": t("p_eyebrow"), "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": p["name"], "description": p["title"] + " " + p["lede"], "url": url_for(C.LANG, "pillars.html") + "#" + p["id"]}} for p in C.PILLARS]},
    }

def crumbs_ld(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": url_for(C.LANG, u)} for i, (u, n) in enumerate(trail)]}

def faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": C.LANG, "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False).replace("</", "<\\/") + "</script>"

THEME_JS = "(function(d,w){var r=d.documentElement;try{var t=localStorage.getItem('kiyan-theme');if(t==='light'||t==='dark')r.setAttribute('data-theme',t)}catch(e){}r.classList.remove('no-js');if(w.matchMedia&&w.matchMedia('(prefers-reduced-motion: reduce)').matches)return;var s=false;try{s=!!sessionStorage.getItem('kiyan-seen')}catch(e){}r.classList.add(s?'is-entering':'is-preloading');w.__kiyanBail=setTimeout(function(){r.classList.remove('is-entering','is-preloading')},7000)})(document,window)"

# ------------------------------------------------------------ page shell
def other_page(current):
    return ("../" + current if is_ar() else "ar/" + current), ("en" if is_ar() else "ar")

def header(current):
    other, ol = other_page(current)
    def item(href, icon, title, desc):
        return f'<a class="mega-item" href="{href}">{MI[icon]}<span><strong>{e(title)}</strong><span class="d">{e(desc)}</span></span></a>'
    pillars = "".join(item("pillars.html#" + p["id"], p["id"], p["name"], p["menu"]) for p in C.PILLARS)
    company = "".join(item(*x) for x in t("mg_items"))
    def panel(pid, head, desc, items, extra=""):
        return f'''<div class="mega" id="{pid}"><div class="wrap"><div class="mega-head"><strong>{head}</strong><span>{desc}</span></div>
          <div class="mega-body"><div class="mega-grid">{items}</div>{extra}</div></div></div>'''
    promo = f'''<a class="mega-promo" href="contact.html?topic=poc"><img src="{A}assets/img/photo/shelf-wide.webp" alt="" width="1200" height="800" loading="lazy"><strong>{t("mega_feat_h")}</strong><span>{t("mega_feat_p")}</span><span class="mega-promo-link">{t("mg_promo_link")} {I["arrow"]}</span></a>'''
    cur = ' aria-current="page"' if current == "team.html" else ""
    return f'''<a class="skip" href="#main">{t("skip")}</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="{e(C.SITE["name"])} — {t("home")}">
      <img class="logo-light" src="{A}assets/img/kiyan-logo.svg" alt="Kiyan" width="83" height="34">
      <img class="logo-dark" src="{A}assets/img/kiyan-logo-white.svg" alt="" width="83" height="34">
    </a>
    <nav class="nav" id="nav" aria-label="{t("menu")}">
      <button class="nav-link" aria-expanded="false" aria-controls="mega-pillars">{t("nav_pillars")} {I["chev"]}</button>
      {panel("mega-pillars", t("mg_p_h"), t("mg_p_d"), pillars, promo)}
      <button class="nav-link" aria-expanded="false" aria-controls="mega-company">{t("nav_company")} {I["chev"]}</button>
      {panel("mega-company", t("mg_c_h"), t("mg_c_d"), company)}
      <a href="team.html"{cur}>{t("nav_team")}</a>
      <a class="nav-mobile-only" href="{other}" lang="{ol}" hreflang="{ol}">{t("lang_switch")}</a>
      <a class="btn btn--primary nav-mobile-only" href="contact.html?topic=poc">{t("cta_poc")} {I["arrow"]}</a>
    </nav>
    <div class="header-tools">
      <button class="search-btn" id="search-open" aria-label="{t("search_label")}">{I["search"]}<span>{t("search")}</span><kbd>⌘K</kbd></button>
      <button class="icon-btn theme-toggle" id="theme-toggle" aria-label="{t("theme")}">{I["sun"]}{I["moon"]}</button>
      <a class="lang-btn" href="{other}" lang="{ol}" hreflang="{ol}" aria-label="{e(t("lang_switch_label"))}">{I["globe"]}<span>{t("lang_switch")}</span></a>
      <a class="btn btn--primary header-cta" href="contact.html?topic=poc">{t("cta_poc")}</a>
      <button class="icon-btn menu-btn" id="menu-btn" aria-label="{t("menu")}" aria-expanded="false" aria-controls="nav">{I["menu"]}</button>
    </div>
  </div>
</header>'''

def cta_band():
    return f'''<section class="cta on-ink" aria-labelledby="cta-h">
  <div class="wrap">
    <div><p class="eyebrow">{t("cta_eyebrow")}</p><h2 id="cta-h">{t("cta_h")}</h2></div>
    <div><p>{t("cta_p")}</p>
    <div class="btn-row"><a class="btn btn--light" href="contact.html?topic=poc">{t("cta_poc")} {I["arrow"]}</a><a class="btn btn--ghost" href="contact.html?type=call">{t("cta_call")}</a></div></div>
  </div>
</section>'''

def footer(current):
    S = C.SITE; other, ol = other_page(current)
    sp = "".join(f'<li><a href="pillars.html#{p["id"]}">{e(p["name"])}</a></li>' for p in C.PILLARS)
    offices = "".join(f'<span class="chip">{o}</span>' for o in S["offices"])
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <img class="logo-light" src="{A}assets/img/kiyan-logo-tagline.svg" alt="Kiyan — Where Intelligence meets Execution" width="136" height="64" loading="lazy">
        <img class="logo-dark" src="{A}assets/img/kiyan-logo-tagline-white.svg" alt="" width="136" height="64" loading="lazy">
        <p>{S["footer"]}</p>
        <div class="offices">{offices}</div>
      </div>
      <div><h4>{t("foot_pillars")}</h4><ul>{sp}</ul></div>
      <div><h4>{t("foot_kiyan")}</h4><ul><li><a href="index.html#execution-gap">{t("foot_gap")}</a></li><li><a href="how-we-work.html">{t("nav_how")}</a></li><li><a href="team.html">{t("nav_team")}</a></li><li><a href="how-we-work.html#poc">{t("foot_poc")}</a></li><li><a href="faq.html">{t("nav_faq")}</a></li><li><a href="how-we-work.html#careers">{t("careers_eyebrow")}</a></li></ul></div>
      <div><h4>{t("foot_contact")}</h4><ul><li><a href="mailto:{S["email"]}">{S["email"]}</a></li><li><a href="https://wa.me/{S["whatsapp"]}" rel="noopener">{t("whatsapp")} <bdi dir="ltr">{S["whatsapp_display"]}</bdi></a></li><li><a href="{S["linkedin"]}" rel="noopener">{t("linkedin")}</a></li><li><a href="contact.html">{t("nav_contact")}</a></li><li><a href="{other}" lang="{ol}" hreflang="{ol}">{t("lang_switch")}</a></li></ul></div>
    </div>
    <div class="foot-bottom"><span>© {datetime.date.today().year} Kiyan. {t("rights")} · {t("hq")}</span>
      <nav class="foot-legal" aria-label="{t("lg_crumb")}"><a class="foot-lang" href="{other}" lang="{ol}" hreflang="{ol}" aria-label="{e(t("lang_switch_label"))}">{I["globe"]}<span lang="{C.LANG}">{t("lang_current")}</span>{I["chev"]}</a><a href="legal.html#terms">{t("lg_terms")}</a><a href="legal.html#privacy">{t("lg_privacy")}</a><a href="legal.html#security">{t("lg_security")}</a><a href="legal.html#cookies">{t("lg_cookies")}</a><a href="{A}sitemap.xml">{t("sitemap")}</a></nav></div>
  </div>
</footer>
<a class="wa" href="https://wa.me/{S["whatsapp"]}" rel="noopener" aria-label="{t("wa_label")}">{I["wa"]}</a>
<dialog class="search" id="search" aria-label="{t("search")}">
  <div class="search-in">{I["search"]}<input id="search-input" type="search" placeholder="{e(t("search_ph"))}" autocomplete="off" aria-label="{t("search_label")}"><button class="icon-btn" id="search-close" aria-label="{t("close")}">{I["close"]}</button></div>
  <div class="search-results" id="search-results" role="listbox"></div>
</dialog>
<script src="{A}assets/js/data-{C.LANG}.js" defer></script>
<script src="{A}assets/js/main.js" defer></script>'''

def page(fname, title, desc, body, trail=None, extra_ld=(), cta=True, listed=True):
    url = url_for(C.LANG, fname)
    lds = [org_ld(), {"@context": "https://schema.org", "@type": "WebSite", "@id": BASE + "/#website", "url": BASE + "/", "name": "Kiyan", "inLanguage": ["en", "ar"], "publisher": {"@id": BASE + "/#organization"}}]
    if trail: lds.append(crumbs_ld([("index.html", t("home"))] + trail))
    lds += list(extra_ld)
    alt = ("".join(f'<link rel="alternate" hreflang="{l}" href="{url_for(l, fname)}">\n' for l in ("en", "ar")) + f'<link rel="alternate" hreflang="x-default" href="{url_for("en", fname)}">') if listed else ""
    if is_ar(): fonts = f'<link rel="preload" href="{A}assets/fonts/noto-kufi-arabic-arabic-600-normal.woff2" as="font" type="font/woff2" crossorigin>'
    else: fonts = '<link rel="preload" href="assets/fonts/poppins-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>\n<link rel="preload" href="assets/fonts/inter-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>'
    robots = "index, follow, max-snippet:-1, max-image-preview:large" if listed else "noindex"
    out = f'''<!doctype html>
<html lang="{C.LANG}" dir="{C.DIR}" class="no-js" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
{alt}
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#100F0F">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(C.SITE["name"])}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/img/og.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:locale" content="{C.OG_LOCALE}"><meta property="og:locale:alternate" content="{"en_GB" if is_ar() else "ar_SA"}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{A}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{A}assets/img/apple-touch-icon.png">
<link rel="manifest" href="{A}site.webmanifest">
{fonts}
<script>{THEME_JS}</script>
<link rel="stylesheet" href="{A}assets/css/main.css">
{"".join(ld(x) for x in lds)}
</head>
<body data-page="{e(t("pg_names").get(fname, ""))}">
<div class="preloader" aria-hidden="true">
  <div class="pl-sheet pl-sheet--b"></div><div class="pl-sheet pl-sheet--g"></div><div class="pl-sheet pl-sheet--w"></div>
  <div class="pl-inner">
    <div class="pl-top"><img src="{A}assets/img/kiyan-logo-white.svg" alt="" width="83" height="34"><span>{t("pl_top")}</span></div>
    <div class="pl-mid"><div class="pl-word">{"".join(f"<span><i>{w}</i></span>" for w in t("pl_words"))}</div></div>
    <div class="pl-bottom"><div><span class="pl-label">{t("pl_bars")}</span><div class="pl-bars"><span></span><span></span><span></span><span></span><span></span><span></span></div></div><div class="pl-count" dir="ltr">000</div></div>
  </div>
</div>
<div class="pt" aria-hidden="true"><div class="pt-sheet pt-sheet--b"></div><div class="pt-sheet pt-sheet--g"></div><div class="pt-sheet pt-sheet--w"></div><div class="pt-sheet pt-sheet--k"><div class="pt-label"><span></span></div></div></div>
{header(fname)}
<main id="main">
{body}
{cta_band() if cta else ""}
</main>
{footer(fname)}
</body>
</html>
'''
    (OUT / fname).write_text(out, encoding="utf-8")
    if listed: SITEMAP.append((C.LANG, fname, title, desc))

def crumbs(trail):
    items = f'<li><a href="index.html">{t("home")}</a></li>' + "".join(
        f'<li><a href="{u}">{n}</a></li>' if i < len(trail) - 1 else f'<li aria-current="page">{n}</li>' for i, (u, n) in enumerate(trail))
    return f'<nav aria-label="Breadcrumb"><ol class="crumbs">{items}</ol></nav>'

def page_hero(trail, eyebrow, h1, lede, extra=""):
    return f'<section class="page-hero"><div class="wrap">{crumbs(trail)}<p class="eyebrow">{eyebrow}</p><h1>{h1}</h1><p class="lede">{lede}</p>{extra}</div></section>'

def initials(name):
    p = name.split(); return (p[0][0] + p[-1][0]).upper()

def portrait(p):
    if p.get("photo"):
        alt = t("tm_portrait").format(name=p["name"], role=p["role"])
        return f'<div class="portrait"><img src="{A}assets/img/team/{p["photo"]}" alt="{e(alt)}" width="480" height="480" loading="lazy"></div>'
    return f'<div class="portrait portrait--mono" role="img" aria-label="{e(p["name"])}">{initials(p["latin_name"])}</div>'

def profile_card(p, focus=False):
    cred = ""
    if p["career"]:
        cred = f'<p class="mini-label">{t("prev_at")}</p><ul class="cred">' + "".join(f'<li><b dir="auto">{e(b)}</b><span>{e(a)}</span></li>' for a, b in p["career"]) + "</ul>"
    mail = f'<a class="profile-mail" href="mailto:{p["email"]}" dir="ltr">{I["mail"]}{p["email"]}</a>' if p.get("email") else ""
    chips = "".join(f'<span class="chip">{e(f)}</span>' for f in p["focus_labels"])
    attrs = f' id="{p["id"]}" data-focus="{e("|".join(p["focus"]))}"' if focus else ""
    return f'''<article class="profile"{attrs}>
    <div class="profile-photo">{portrait(p)}<div class="profile-chips">{chips}</div></div>
    <div class="profile-body"><h3>{e(p["name"])}</h3><p class="role">{e(p["role"])}</p><p class="summary">{e(p["summary"])}</p>{cred}{mail}</div></article>'''

def carousel(cards):
    return f'''<div class="carousel" data-carousel role="region" aria-roledescription="carousel" aria-label="{t("car_label")}">
    <div class="car-track" tabindex="0">{cards}</div>
    <div class="car-ui"><div class="car-progress"><i></i></div><span class="car-count" dir="ltr" aria-hidden="true"></span>
    <button class="icon-btn car-btn" data-dir="-1" aria-label="{t("car_prev")}">{I["arrow"]}</button><button class="icon-btn car-btn" data-dir="1" aria-label="{t("car_next")}">{I["arrow"]}</button></div></div>'''

def faq_block(items):
    return '<div class="faq">' + "".join(f'<details><summary>{e(q)}</summary><div class="a"><p>{e(a)}</p></div></details>' for q, a in items) + "</div>"

def ticks(items): return '<ul class="ticks">' + "".join(f"<li>{e(x)}</li>" for x in items) + "</ul>"
def sol_card(title, pts, impact): return f'<div class="card"><h4>{e(title)}</h4>{ticks(pts)}<div class="impact"><b>{t("impact")}</b>{e(impact)}</div></div>'
def num(a):
    """Figures stay left-to-right; Arabic words (e.g. دقيقتان) follow the page direction."""
    return f'<b dir="ltr">{a}</b>' if a[0] in "0123456789−" else f"<b>{a}</b>"
def kpis(items): return '<div class="kpis">' + "".join(f"<div>{num(a)}<span>{b}</span></div>" for a, b in items) + "</div>"
def poc_block(pid="poc"):
    return f'''<div class="poc reveal" id="{pid}">
    <div><h3>{t("poc_h")}</h3><p>{t("poc_p")}</p><div class="btn-row"><a class="btn btn--light" href="contact.html?topic=poc">{t("poc_btn")} {I["arrow"]}</a></div></div>
    <div class="poc-steps">{"".join(f"<div><b>1</b><span>{x}</span></div>" for x in t("poc_units"))}</div></div>'''
def three_roles():
    T = C.THREE
    def media(img):
        """A short silent loop when assets/video/<name>.mp4 exists; the still is its poster and the fallback."""
        still = f"{A}assets/img/photo/{img}.webp"
        if (ROOT / f"assets/video/{img}.mp4").exists():
            return f'<video class="hcard-media" muted loop playsinline preload="none" poster="{still}" width="960" height="720" aria-hidden="true" data-loop><source src="{A}assets/video/{img}.mp4" type="video/mp4"></video>'
        return f'<img class="hcard-media" src="{still}" alt="" width="1200" height="900" loading="lazy">'
    def card(key, img, mid=False):
        return f'''<article class="hcard{" hcard--mid" if mid else ""} reveal">
      {media(img)}
      <span class="hcard-tag">{t("role_tag_" + key)}</span>
      <div class="hcard-body"><h3>{t("role_h_" + key)}</h3>{ticks(T[key])}</div></article>'''
    return f'<div class="hcards">{card("m", "manufacturer")}{card("k", "partner", True)}{card("r", "retailer")}</div>'
def qmark(name): return name + ("؟" if is_ar() else "?")

# ================================================================= HOME
def build_home():
    G = C.GAP
    funnel = "".join(f'<div class="funnel-row"><div class="funnel-bar" style="--w:{w}%;--c:{c};--o:{o}"><b>{n}</b><span>{d}</span></div></div>' for n, d, w, c, o in G["stages"])
    points = "".join(f'<div class="reveal" style="--d:{i*90}ms"><span class="mono">{a}</span><h3>{b}</h3><p>{c}</p></div>' for i, (a, b, c) in enumerate(G["points"]))
    impacts = "".join(f"<div><b>{a}</b>{b}</div>" for a, b in G["impacts"])
    stats = "".join(f'<div class="stat"><b dir="ltr">{a}' + (f"<sup>{s}</sup>" if s else "") + f'</b><span>{d}</span></div>' for a, s, d in t("stats"))
    diag = "".join(f'<button class="diag-q" aria-pressed="false" data-right="{p["id"]}" data-name="{e(p["name"])}" data-sol="{e(p["start"])}"><span class="n">{p["n"]}</span><strong>{e(qmark(p["name"]))}</strong><span class="q">{e(p["q"])}</span><span class="state">{t("q_tap")}</span></button>' for p in C.PILLARS)
    tabs = "".join(f'<button class="space-tab" role="tab" id="st-{p["id"]}" aria-controls="sp-{p["id"]}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}"><span class="n">{p["n"]}</span><span class="t">{e(p["name"])}</span>{I["arrow"]}</button>' for i, p in enumerate(C.PILLARS))
    panels = "".join(f'''<article class="space-panel" role="tabpanel" id="sp-{p["id"]}" aria-labelledby="st-{p["id"]}"{"" if i == 0 else " hidden"}>
      <div class="space-art">{art_img(p["id"])}</div>
      <div class="space-body"><span class="mono" style="color:#86BC25">{p["n"]} / {e(p["name"])}</span><p class="promise">{e(p["title"])}</p><p>{e(p["lede"])}</p>
      <div class="chips">{"".join(f'<span class="chip">{e(c)}</span>' for c in p["chips"])}</div>
      <a class="arrow-link" href="pillars.html#{p["id"]}">{t("p_explore").format(x=e(p["name"]))} {I["arrow"]}</a></div></article>''' for i, p in enumerate(C.PILLARS))
    ppl = carousel("".join(profile_card(p) for p in people()))
    pstats = "".join(f"<div>{num(a)}<span>{b}</span></div>" for a, b in t("proof_stats"))
    body = f'''
<section class="hero on-ink" aria-labelledby="hero-h">
  <canvas class="hero-canvas" id="hero-canvas" aria-hidden="true"></canvas>
  <div class="wrap">
    <p class="eyebrow">{t("hero_eyebrow")}</p>
    <h1 id="hero-h">{t("hero_h")}</h1>
    <p class="lede">{t("hero_p")}</p>
    <div class="btn-row"><a class="btn btn--primary" href="contact.html?topic=poc">{t("cta_poc")} {I["arrow"]}</a><a class="btn btn--ghost" href="#pillars">{t("hero_secondary")}</a></div>
  </div>
  <div class="hero-state" aria-hidden="true"><span>{t("hero_signal")}</span><i id="hero-bar"></i><b id="hero-label">{t("hero_decision")}</b></div>
</section>

<section aria-label="{t("stats_label")}"><div class="wrap"><div class="stats">{stats}</div></div></section>

<section class="section" id="execution-gap" aria-labelledby="gap-h"><div class="wrap">
  <div class="gap-grid">
    <div class="reveal"><p class="eyebrow eyebrow--blue">{t("gap_eyebrow")}</p><h2 id="gap-h">{G["title"]}</h2><div class="rule"></div><p class="lede">{G["lede"]}</p></div>
    <div class="reveal" style="--d:120ms"><div class="funnel">{funnel}</div><div class="funnel-foot"><span>{t("gap_from")}</span><span>{t("gap_to")}</span></div></div>
  </div>
  <div class="gap-points">{points}</div>
  <p class="mini-label" style="margin-top:clamp(40px,5vw,64px)">{t("gap_impact")}</p>
  <div class="impact-row reveal">{impacts}</div>
</div></section>

<section class="section section--soft" id="questions" aria-labelledby="diag-h"><div class="wrap">
  <div class="section-head"><div><p class="eyebrow">{t("q_eyebrow")}</p><h2 id="diag-h">{t("q_h")}</h2></div><p class="muted">{t("q_p")}</p></div>
  <div class="diag" id="diag">{diag}</div>
  <div class="diag-result" id="diag-result" aria-live="polite"><div><h3 id="diag-title">{t("q_none_h")}</h3><p id="diag-text">{t("q_none_p")}</p></div><a class="btn btn--primary" id="diag-cta" href="contact.html">{t("q_cta")} {I["arrow"]}</a></div>
</div></section>

<section class="section" id="pillars" aria-labelledby="pillars-h"><div class="wrap">
  <div class="section-head"><div><p class="eyebrow eyebrow--blue">{t("p_eyebrow")}</p><h2 id="pillars-h">{t("p_h")}</h2></div><p class="muted">{t("p_p")}</p></div>
  <div class="spaces"><div class="space-tabs" role="tablist" aria-label="{t("p_tabs")}" data-tabs>{tabs}</div><div>{panels}</div></div>
</div></section>

<section class="section section--soft" id="how" aria-labelledby="how-h"><div class="wrap">
  <div class="section-head"><div><p class="eyebrow">{t("how_eyebrow")}</p><h2 id="how-h">{t("how_h")}</h2></div><p class="muted">{t("how_p")}</p></div>
  {three_roles()}
  <p class="pull" style="margin-top:clamp(32px,4vw,56px)">{t("hw_obj")}</p>
  <p style="margin-top:24px"><a class="arrow-link" href="how-we-work.html">{t("how_more")} {I["arrow"]}</a></p>
</div></section>

<section class="section on-ink" aria-labelledby="proof-h"><div class="wrap">
  <div class="proof">
    <div class="reveal"><p class="eyebrow">{t("proof_eyebrow")}</p><h2 id="proof-h">{t("proof_h")}</h2><div class="rule"></div><p class="lede">{t("proof_p")}</p><div class="btn-row"><a class="btn btn--light" href="pillars.html#execution">{t("proof_link")} {I["arrow"]}</a></div></div>
    <div class="reveal" style="--d:120ms"><figure class="proof-shot"><img src="{A}assets/img/photo/shelf-audit.webp" alt="{e(t("proof_alt"))}" width="1400" height="1050" loading="lazy"></figure><div class="proof-stats">{pstats}</div></div>
  </div>
  {poc_block("poc")}
</div></section>

<section class="section" id="people" aria-labelledby="people-h"><div class="wrap">
  <div class="section-head"><div><p class="eyebrow">{t("people_eyebrow")}</p><h2 id="people-h">{t("people_h")}</h2></div><p class="muted">{t("people_p")}</p></div>
  {ppl}
  <div class="pedigree reveal"><span class="mono">{t("pedigree")}</span>{"".join(f'<span dir="ltr">{f}</span>' for f in C.FIRMS)}</div>
  <p style="margin-top:32px"><a class="arrow-link" href="team.html">{t("people_link")} {I["arrow"]}</a></p>
</div></section>

<section class="section section--soft" aria-labelledby="faq-h"><div class="wrap"><div class="split">
  <div><p class="eyebrow">{t("faq_eyebrow")}</p><h2 id="faq-h">{t("faq_h")}</h2><p class="muted" style="margin-top:1.25rem">{t("faq_p")}</p><p style="margin-top:24px"><a class="arrow-link" href="faq.html">{t("faq_all")} {I["arrow"]}</a></p></div>
  {faq_block([C.FAQ[i] for i in C.HOME_FAQ])}
</div></div></section>'''
    page("index.html", t("t_home"), t("d_home"), body, extra_ld=[faq_ld([C.FAQ[i] for i in C.HOME_FAQ])])

# =============================================================== PILLARS
def pillar_extra(pid):
    if pid == "reach":
        layers = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in C.LAYERS)
        th = "".join(f"<th>{x}</th>" for x in t("layers_th"))
        leaks = "".join(f'<div class="card"><span class="n">{i+1:02d}</span><h4>{a}</h4><p>{b}</p></div>' for i, (a, b) in enumerate(C.LEAKS))
        return f'''<div class="pillar-extra pillar-extra--ink on-ink" id="store-universe"><div class="cols-2" style="align-items:center">
  <div><h3 class="h-sub">{t("layers_h")}</h3><p class="muted" style="margin-top:1rem">{t("layers_p")}</p>
    <div class="table-wrap" style="margin-top:28px"><table class="t"><thead><tr>{th}</tr></thead><tbody>{layers}</tbody></table></div>
    <p class="pull pull--sm" style="margin-top:28px">{t("layers_pull")}</p></div>
  <div>{universe_svg()}</div></div></div>
<div class="pillar-extra" id="route-to-market"><div class="cols-2"><h3 class="h-sub">{t("rtm_h")}</h3><p class="muted">{t("rtm_p")}</p></div>
  <div class="cols-3" style="margin-top:32px">{leaks}</div>
  <div class="cols-2" style="margin-top:clamp(40px,5vw,64px)"><div><h3 class="h-sub">{t("rtm2_h")}</h3><p class="muted" style="margin-top:1rem">{t("rtm2_p")}</p><div class="chips" style="margin-top:24px">{"".join(f'<span class="chip">{x}</span>' for x in t("rtm_rights"))}</div></div>
  <div class="card"><span class="n">{t("changes")}</span>{ticks(C.RTM_CHANGES)}</div></div>
  <div class="loop">{"".join(f"<div>{x}</div>" for x in t("loop"))}</div>
  <p class="pull pull--sm">{t("rtm_pull")}</p></div>'''
    if pid == "store":
        gets = "".join(f"<li><strong style='color:var(--text)'>{a}.</strong> {b}</li>" for a, b in C.SEGMENT_GETS)
        return f'''<div class="pillar-extra" id="segmentation"><div class="cols-2"><h3 class="h-sub">{t("seg_h")}</h3><p class="muted">{t("seg_p")}</p></div>
  <div class="cols-2" style="margin-top:32px"><div class="card"><span class="n">{t("receive")}</span><ul class="ticks">{gets}</ul></div>
  <div class="card"><span class="n">{t("changes")}</span>{ticks(C.SEGMENT_CHANGES)}</div></div></div>'''
    if pid == "space":
        rows = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in C.PLANO)
        th = "".join(f"<th>{x}</th>" for x in t("plano_th"))
        return f'''<div class="pillar-extra" id="planograms"><div class="cols-2"><div><h3 class="h-sub">{t("plano_h")}</h3><p class="muted" style="margin-top:1rem">{t("plano_p")}</p></div>
  <div class="table-wrap"><table class="t"><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table></div></div></div>'''
    return ""

def build_pillars():
    secs = ""
    for p in C.PILLARS:
        roles = ""
        if p.get("roles"):
            roles = f'<p class="mini-label" style="margin-top:28px">{t("roles_h")}</p><div class="impact-row impact-row--2">' + "".join(f'<div><b>{a}</b>{e(b)}<br><span class="mono" style="color:var(--accent-text)">{c}</span></div>' for a, b, c in p["roles"]) + "</div>"
        n = len(p["cards"])
        secs += f'''<section class="pillar" id="{p["id"]}" aria-labelledby="h-{p["id"]}"><div class="wrap">
  <div class="pillar-head">
    <div class="reveal"><span class="num">{p["n"]} / {t("nav_pillars")}</span><h2 id="h-{p["id"]}">{e(p["name"])}</h2>
      <p class="mini-label" style="margin-top:24px">{t("pp_question")}</p><p class="pillar-q">{e(p["q"])}</p>
      <div class="art">{art_img(p["id"])}</div></div>
    <div class="reveal" style="--d:100ms"><h3 class="h-sub">{e(p["title"])}</h3><p class="lede" style="margin-top:1rem">{e(p["lede"])}</p>
      <div class="chips" style="margin-top:24px">{"".join(f'<span class="chip">{e(c)}</span>' for c in p["chips"])}</div>
      {kpis(p["kpis"]) if p.get("kpis") else ""}{roles}</div>
  </div>
  <p class="mini-label" style="margin-top:clamp(32px,4vw,56px)">{t("pp_solutions")}</p>
  <div class="cols-{3 if n == 3 else 2}">{"".join(sol_card(*c) for c in p["cards"])}</div>
  {pillar_extra(p["id"])}
  <p style="margin-top:32px"><a class="arrow-link" href="contact.html?topic={p["id"]}">{t("pp_poc")} {I["arrow"]}</a></p>
</div></section>'''
    jump = "".join(f'<a class="chip" style="text-decoration:none" href="#{p["id"]}">{p["n"]} {e(p["name"])}</a>' for p in C.PILLARS)
    trail = [("pillars.html", t("pp_crumb"))]
    body = page_hero(trail, t("pp_eyebrow"), t("pp_h"), t("pp_p"), f'<div class="chips" style="margin-top:2rem">{jump}</div>') + secs + f'''
<section class="section section--soft" aria-labelledby="poc-h2"><div class="wrap"><h2 class="sr-only" id="poc-h2">{t("poc_eyebrow")}</h2>{poc_block("poc")}</div></section>'''
    svc = [{"@context": "https://schema.org", "@type": "Service", "name": p["name"], "serviceType": "Category management consulting", "provider": {"@id": BASE + "/#organization"},
            "areaServed": "Saudi Arabia", "url": url_for(C.LANG, "pillars.html") + "#" + p["id"], "description": p["title"] + " " + p["lede"]} for p in C.PILLARS]
    page("pillars.html", t("t_pillars"), t("d_pillars"), body, trail=trail, extra_ld=svc + [faq_ld([C.FAQ[i] for i in (2, 6, 7, 9)])])

# ============================================================ HOW WE WORK
def build_how():
    trail = [("how-we-work.html", t("hw_crumb"))]
    chain = "".join(f"<div><b style='color:var(--accent-text)'>{i+1:02d}</b><p style='color:var(--text);font-weight:600'>{x}</p></div>" for i, x in enumerate(t("hw_chain")))
    pr = "".join(f'<div class="card reveal" style="--d:{i*70}ms"><span class="n">{i+1:02d}</span><h3>{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate(C.PRINCIPLES))
    steps = "".join(f'<div class="card"><span class="n">{i+1:02d}</span><h3>{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate(C.POC_STEPS))
    subj = t("careers_subject").replace(" ", "%20")
    body = page_hero(trail, t("hw_eyebrow"), t("hw_h"), t("hw_p")) + f'''
<section class="section section--soft" aria-label="{t("how_h")}"><div class="wrap">
  {three_roles()}
  <p class="pull" style="margin-top:clamp(40px,5vw,72px)">{t("hw_obj")}</p>
  <div class="chain chain--5" style="margin-top:28px">{chain}</div>
</div></section>
<section class="section" id="poc" aria-labelledby="poc-h"><div class="wrap">
  <div class="section-head"><div><p class="eyebrow eyebrow--blue">{t("poc_eyebrow")}</p><h2 id="poc-h">{t("poc2_h")}</h2></div><p class="muted">{t("poc2_p")}</p></div>
  <div class="cols-3">{steps}</div>
  <div class="btn-row"><a class="btn btn--primary" href="contact.html?topic=poc">{t("poc_btn")} {I["arrow"]}</a></div>
</div></section>
<section class="section section--soft" aria-labelledby="pr-h"><div class="wrap">
  <div class="section-head"><div><p class="eyebrow">{t("pr_eyebrow")}</p><h2 id="pr-h">{t("pr_h")}</h2></div><p class="muted">{t("pr_p")}</p></div>
  <div class="cols-2">{pr}</div>
</div></section>
<section class="section on-ink" aria-labelledby="where-h"><div class="wrap"><div class="split">
  <div><p class="eyebrow">{t("where_eyebrow")}</p><h2 id="where-h">{t("where_h")}</h2></div>
  <div><p class="lede">{t("where_p")}</p><div class="chips" style="margin-top:28px">{"".join(f'<span class="chip">{o}</span>' for o in C.SITE["offices"])}</div></div>
</div></div></section>
<section class="section" id="careers" aria-labelledby="car-h"><div class="wrap"><div class="split">
  <div><p class="eyebrow eyebrow--blue">{t("careers_eyebrow")}</p><h2 id="car-h">{t("careers_h")}</h2></div>
  <div><p class="lede">{t("careers_p")}</p><div class="btn-row"><a class="btn btn--primary" href="mailto:{C.SITE["email"]}?subject={subj}">{t("careers_btn")} {I["arrow"]}</a><a class="btn btn--ghost" href="team.html">{t("people_link")}</a></div></div>
</div></div></section>'''
    page("how-we-work.html", t("t_how"), t("d_how"), body, trail=trail, extra_ld=[faq_ld([C.FAQ[5], C.FAQ[8]])])

# ================================================================ TEAM
def build_team():
    P = people(); trail = [("team.html", t("tm_crumb"))]
    focuses = []
    for p in P:
        for f in p["focus"]:
            if f not in focuses: focuses.append(f)
    filt = f'<button class="filter-btn" aria-pressed="true" data-filter="*">{t("tm_all")}</button>' + "".join(f'<button class="filter-btn" aria-pressed="false" data-filter="{e(f)}">{e(C.FOCUS_LABELS.get(f, f))}</button>' for f in focuses)
    groups = ""; multi = len(TEAM["groups"]) > 1
    for g in TEAM["groups"]:
        members = [p for p in P if p["group"] == g]
        if not members: continue
        gl = TEAM.get("groups_ar", {}).get(g, g) if is_ar() else g
        head = f'<h2 style="font-size:clamp(1.5rem,2.4vw,2rem);margin-block:clamp(40px,6vw,72px) 28px">{e(gl)}</h2>' if multi else f'<h2 class="sr-only">{e(gl)}</h2>'
        groups += head + f'<div class="profile-grid">{"".join(profile_card(p, focus=True) for p in members)}</div>'
    dialogs = ""
    persons = []
    for p in P:
        d = {"@type": "Person", "name": p["latin_name"], "jobTitle": p["role"], "description": p["summary"], "worksFor": {"@id": BASE + "/#organization"}, "url": url_for(C.LANG, "team.html") + "#" + p["id"]}
        if p["name"] != p["latin_name"]: d["alternateName"] = p["name"]
        if p.get("photo"): d["image"] = f'{BASE}/assets/img/team/{p["photo"]}'
        if p.get("email"): d["email"] = p["email"]
        persons.append(d)
    subj = t("careers_subject").replace(" ", "%20")
    body = page_hero(trail, t("tm_eyebrow"), t("tm_h"), t("tm_p")) + f'''
<section class="section section--tight" aria-label="{t("tm_crumb")}"><div class="wrap">
  <div class="team-filter" role="group" aria-label="{t("tm_filter")}">{filt}</div>
  {groups}
</div></section>
<section class="section section--soft" id="join" aria-labelledby="join-h"><div class="wrap"><div class="split">
  <div><p class="eyebrow">{t("careers_eyebrow")}</p><h2 id="join-h">{t("tm_join_h")}</h2></div>
  <div><p class="lede">{t("tm_join_p")}</p><div class="btn-row"><a class="btn btn--primary" href="mailto:{C.SITE["email"]}?subject={subj}">{t("tm_join_btn")} {I["arrow"]}</a></div></div>
</div></div></section>
{dialogs}'''
    page("team.html", t("t_team"), t("d_team"), body, trail=trail,
         extra_ld=[{"@context": "https://schema.org", "@type": "AboutPage", "name": t("t_team"), "mainEntity": {"@id": BASE + "/#organization"}, "mentions": persons}])

# ================================================================= FAQ
def build_faq():
    trail = [("faq.html", t("fq_crumb"))]
    body = page_hero(trail, t("faq_eyebrow"), t("fq_h"), t("fq_p")) + f'''
<section class="section section--tight"><div class="wrap"><div class="split"><div><p class="muted">{t("fq_cant")}</p><p style="margin-top:12px"><a class="arrow-link" href="contact.html">{t("fq_ask")} {I["arrow"]}</a></p></div>{faq_block(C.FAQ)}</div></div></section>'''
    page("faq.html", t("t_faq"), t("d_faq"), body, trail=trail, extra_ld=[faq_ld(C.FAQ)])

# ============================================================= CONTACT
def build_contact():
    S = C.SITE; trail = [("contact.html", t("ct_crumb"))]
    opts = "".join(f'<option value="{p["id"]}">{e(p["name"])}</option>' for p in C.PILLARS)
    ty = t("ct_types")
    plist = "".join(f'<p><a href="mailto:{p["email"]}">{e(p["name"])}</a><br>{e(p["role"])} · <bdi dir="ltr">{p["email"]}</bdi></p>' for p in people() if p.get("email"))
    body = page_hero(trail, t("ct_eyebrow"), t("ct_h"), t("ct_p")) + f'''
<section class="section section--tight"><div class="wrap"><div class="contact-grid">
  <form class="form" id="contact-form" action="mailto:{S["email"]}" method="post" enctype="text/plain">
    <div><span class="sr-only" id="type-l">{t("ct_type")}</span><div class="seg" role="radiogroup" aria-labelledby="type-l">
      <input type="radio" name="type" id="ty-poc" value="{ty[0]}" checked><label for="ty-poc">{ty[0]}</label>
      <input type="radio" name="type" id="ty-call" value="{ty[1]}"><label for="ty-call">{ty[1]}</label>
      <input type="radio" name="type" id="ty-rfp" value="{ty[2]}"><label for="ty-rfp">{ty[2]}</label></div></div>
    <div class="row"><div class="field"><label for="f-name">{t("ct_name")}</label><input id="f-name" name="name" autocomplete="name" required></div>
    <div class="field"><label for="f-role">{t("ct_role")}</label><input id="f-role" name="role" autocomplete="organization-title"></div></div>
    <div class="row"><div class="field"><label for="f-company">{t("ct_company")}</label><input id="f-company" name="company" autocomplete="organization" required></div>
    <div class="field"><label for="f-email">{t("ct_email")}</label><input id="f-email" name="email" type="email" dir="ltr" autocomplete="email" required></div></div>
    <div class="field"><label for="f-topic">{t("ct_topic")}</label><select id="f-topic" name="topic"><option value="">{t("ct_unsure")}</option>{opts}</select></div>
    <div class="field"><label for="f-msg">{t("ct_msg")}</label><textarea id="f-msg" name="message" placeholder="{e(t("ct_msg_ph"))}"></textarea></div>
    <div class="btn-row" style="margin-top:0"><button class="btn btn--primary" type="submit">{t("ct_send")} {I["arrow"]}</button><a class="btn btn--ghost" id="wa-send" href="https://wa.me/{S["whatsapp"]}" rel="noopener">{t("ct_wa")}</a></div>
    <p class="form-note">{t("ct_note")}</p>
  </form>
  <aside class="contact-list" aria-label="{t("ct_direct")}">
    <div><h3>{t("ct_email_h")}</h3><a href="mailto:{S["email"]}" dir="ltr">{S["email"]}</a></div>
    <div><h3>{t("whatsapp")}</h3><a href="https://wa.me/{S["whatsapp"]}" rel="noopener" dir="ltr">{S["whatsapp_display"]}</a></div>
    <div><h3>{t("linkedin")}</h3><a href="{S["linkedin"]}" rel="noopener" dir="ltr">linkedin.com/company/kiyansa</a></div>
    <div><h3>{t("ct_partners")}</h3>{plist}</div>
    <div><h3>{t("ct_offices")}</h3><p style="color:var(--text);font-weight:600">{" · ".join(S["offices"])}</p><p>{t("ct_offices_p")}</p></div>
  </aside>
</div></div></section>'''
    page("contact.html", t("t_contact"), t("d_contact"), body, trail=trail, cta=False,
         extra_ld=[{"@context": "https://schema.org", "@type": "ContactPage", "url": url_for(C.LANG, "contact.html"), "name": t("t_contact")}])

def build_legal():
    trail = [("legal.html", t("lg_crumb"))]
    nav = "".join(f'<li><a href="#{i}">{e(h)}</a></li>' for i, h, _ in C.LEGAL)
    secs = "".join(f'<section id="{i}" class="legal-sec"><h2>{e(h)}</h2>' + "".join(f"<p>{e(x)}</p>" for x in ps) + "</section>" for i, h, ps in C.LEGAL)
    body = page_hero(trail, t("lg_crumb"), t("lg_h"), t("lg_p")) + f'''
<section class="section section--tight"><div class="wrap"><div class="split"><ul class="legal-nav">{nav}</ul><div class="legal">{secs}</div></div></div></section>'''
    page("legal.html", t("t_legal"), t("d_legal"), body, trail=trail, cta=False)

def build_404():
    body = f'<section class="page-hero"><div class="wrap" style="min-height:50vh"><p class="eyebrow">404</p><h1>{t("nf_h")}</h1><p class="lede">{t("nf_p")}</p><div class="btn-row"><a class="btn btn--primary" href="index.html">{t("nf_btn")} {I["arrow"]}</a><a class="btn btn--ghost" href="pillars.html">{t("hero_secondary")}</a></div></div></section>'
    page("404.html", t("t_404"), t("nf_p"), body, cta=False, listed=False)

# ------------------------------------------------------- per-language data
def build_data():
    idx = [{"k": t("k_page"), "t": ti.split(" | ")[0], "d": d, "u": f} for l, f, ti, d in SITEMAP if l == C.LANG]
    idx += [{"k": t("k_pillar"), "t": p["name"], "d": p["q"] + " " + p["title"], "u": "pillars.html#" + p["id"], "x": " ".join(p["chips"])} for p in C.PILLARS]
    idx += [{"k": t("k_solution"), "t": c[0], "d": c[2], "u": "pillars.html#" + p["id"], "x": " ".join(c[1])} for p in C.PILLARS for c in p["cards"]]
    idx += [{"k": t("k_solution"), "t": a, "d": b, "u": "pillars.html#route-to-market"} for a, b in C.LEAKS]
    idx += [{"k": t("k_solution"), "t": t("seg_h"), "d": t("seg_p"), "u": "pillars.html#segmentation"},
            {"k": t("k_solution"), "t": t("poc_h"), "d": t("poc2_h") + " " + t("poc2_p"), "u": "how-we-work.html#poc"}]
    idx += [{"k": t("k_person"), "t": p["name"], "d": p["role"] + ". " + p["summary"], "u": "team.html#" + p["id"], "x": p["latin_name"]} for p in people()]
    idx += [{"k": t("k_question"), "t": q, "d": a[:150] + "…", "u": "faq.html"} for q, a in C.FAQ]
    keys = ["q_tap", "q_marked", "q_none_h", "q_none_p", "q_one", "q_many", "q_start", "q_poc", "q_prefill", "s_empty", "m_enquiry", "m_pillar", "m_new", "ct_name", "ct_role", "ct_company", "ct_email"]
    T = {k: t(k) for k in keys}; T["pages"] = t("pg_names"); T["sep"] = "، " if is_ar() else ", "; T["sep2"] = "؛ " if is_ar() else "; "
    (ROOT / f"assets/js/data-{C.LANG}.js").write_text("window.KIYAN_INDEX=" + json.dumps(idx, ensure_ascii=False) + ";window.KIYAN_T=" + json.dumps(T, ensure_ascii=False) + ";", encoding="utf-8")

def build_language(mod):
    global C, A, OUT
    C = mod; A = "../" if mod.LANG == "ar" else ""; OUT = ROOT / "ar" if mod.LANG == "ar" else ROOT
    OUT.mkdir(exist_ok=True)
    for b in (build_home, build_pillars, build_how, build_team, build_faq, build_contact, build_legal, build_404): b()
    build_data()

# ---------------------------------------------------------------- extras
def build_extras():
    tl = (ROOT / "assets/img/kiyan-logo-tagline.svg").read_text()
    (ROOT / "assets/img/kiyan-logo-tagline-white.svg").write_text(tl.replace("#100f0f", "#ffffff"))
    icon = (ROOT / "assets/img/kiyan-icon.svg").read_text()
    (ROOT / "favicon.svg").write_text(icon.replace('fill="#100f0f"', 'fill="#100f0f" class="c"').replace("</svg>", "<style>@media (prefers-color-scheme:dark){.c{fill:#fff}}</style></svg>"))
    (ROOT / "site.webmanifest").write_text(json.dumps({"name": "Kiyan", "short_name": "Kiyan", "description": EN.SITE["tagline"], "start_url": "./", "display": "browser", "background_color": "#100F0F", "theme_color": "#100F0F",
        "icons": [{"src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=1))
    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended", "Bingbot", "CCBot"]
    (ROOT / "robots.txt").write_text("User-agent: *\nAllow: /\n\n# AI search and answer engines are welcome to read and cite this site.\n" + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"Sitemap: {BASE}/sitemap.xml\n")
    prio = {"index.html": "1.0", "pillars.html": "0.9", "contact.html": "0.8"}
    rows = ""
    for l, f, _, _ in SITEMAP:
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{x}" href="{url_for(x, f)}"/>' for x in ("en", "ar"))
        rows += f'  <url><loc>{url_for(l, f)}</loc><lastmod>{TODAY}</lastmod><priority>{prio.get(f, "0.7")}</priority>{alts}</url>\n'
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + rows + "</urlset>\n")
    for mod in (EN, AR):
        S = mod.SITE; U = mod.UI
        L = [f"# {S['name']}", "", f"> {S['description']} \"{S['tagline']}\"", "", f"## {U['p_eyebrow']}", ""]
        L += [f"- **{p['name']}**: {p['q']} {p['title']} {p['lede']}" for p in mod.PILLARS]
        L += ["", f"## {U['how_h']}", "", U["hw_p"], "", f"## {U['poc_eyebrow']}", "", U["poc2_h"] + " " + U["poc2_p"], "", f"## {U['nav_team']}", ""]
        for p in TEAM["people"]:
            q = {**p, **(p.get("ar", {}) if mod.LANG == "ar" else {})}
            L.append(f"- {q['name']}, {q['role']}. {q['summary']}")
        L += ["", f"## {U['nav_faq']}", ""]
        for q, a in mod.FAQ: L += [f"### {q}", a, ""]
        L += [f"## {U['nav_contact']}", "", f"- {S['email']}", f"- WhatsApp: {S['whatsapp_display']}", f"- {S['linkedin']}", f"- {url_for(mod.LANG, 'index.html')}",
              f"- English: {BASE}/llms.txt", f"- العربية: {BASE}/ar/llms.txt", ""]
        (ROOT / ("ar/llms.txt" if mod.LANG == "ar" else "llms.txt")).write_text("\n".join(L), encoding="utf-8")

if __name__ == "__main__":
    for old in ["spaces.html", "demand-space.html", "academy.html", "who-we-serve.html", "about.html", "assets/js/search-index.js"] + [f"assets/img/art-{k}.svg" for k in ("intelligence", "innovation", "demand", "expansion", "value", "experience", "academy")]:
        (ROOT / old).unlink(missing_ok=True)
    build_language(EN); build_language(AR); build_extras()
    print("Built", len(SITEMAP), "pages across English and Arabic (+ two 404 pages)")
