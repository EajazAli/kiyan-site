# Kiyan website

Static site for **kiyan.sa**. No framework, no build tools beyond Python 3.12+.
Open `index.html` through any web server, or upload the whole folder to a static host
(GitHub Pages, Netlify, Cloudflare Pages, or any shared hosting).

    python3 -m http.server 8000     # then open http://localhost:8000

## Editing

| To change…                   | Edit…                    | Then run            |
|------------------------------|--------------------------|---------------------|
| Team members, bios, photos (both languages) | `data/team.json` | `python3 build.py`  |
| English copy, pillars, FAQ   | `content.py`             | `python3 build.py`  |
| Arabic copy                  | `content_ar.py`          | `python3 build.py`  |
| Page layout / new sections   | `build.py`               | `python3 build.py`  |
| Colours, type, spacing       | `assets/css/main.css`    | nothing             |
| Behaviour (search, tabs…)    | `assets/js/main.js`      | nothing             |

`build.py` rewrites every `.html` file, `sitemap.xml`, `robots.txt`, `llms.txt` and the
search index. Do not edit the `.html` files by hand; the next build overwrites them.

### Adding a team member
1. Put a square photo (480px or larger) in `assets/img/team/`. Colour is fine; the site renders it monochrome.
2. Copy a block in `data/team.json`, change the values, set `"photo"` to the file name (leave it empty to show initials).
3. To start a new section such as "Consultants", add the name to `"groups"` and use it as the person's `"group"`.
4. Run `python3 build.py`. The card, bio, filter, search entry and structured data are all generated.

## What is in the box
- English at `/`, Arabic (right-to-left) at `/ar/`, linked by a language switch and `hreflang` tags
- 7 pages per language + 404: Home, Pillars, How we work, Team, FAQ, Contact, Legal
- First-visit loader and page-to-page sheet transitions (skipped for visitors who prefer reduced motion)
- Dark theme by default (visitors can switch to light; the choice is remembered)
- Team shown as a carousel on the home page and as full profile cards on the Team page, credentials always visible
- The six pillars: Right Reach, Right Category, Right Range, Right Store, Right Space, Right Execution
- SEO: unique titles and descriptions, canonical URLs, Open Graph image, bilingual `sitemap.xml`, `robots.txt`
- AEO / GEO: JSON-LD (Organization, ProfessionalService, Service, FAQPage, BreadcrumbList, Person),
  answer-first FAQ, `llms.txt` in both languages, AI crawlers explicitly allowed
- Light and dark themes, site search (Ctrl/⌘ K), keyboard-accessible tabs and dialogs, reduced-motion support
- Self-hosted fonts (Poppins, Noto Kufi Arabic; SIL Open Font License). No third-party requests unless Tag Manager or the form service is switched on.

## Before launch
- Have counsel review the Terms, Privacy, Security and Cookie text (`LEGAL` in `content.py` / `content_ar.py`).
- Confirm usage rights for the three photographs in `assets/img/photo/` (taken from the brand guide and the deck).
- Have a native Arabic speaker at Kiyan review `content_ar.py` and the Arabic names in `data/team.json`.
- Contact form opens the visitor's email or WhatsApp. Connect a form backend (e.g. Zoho Forms) to capture leads in a CRM.
- Add Google Analytics / Search Console tags, a Google Business Profile, and a street address for the map.
- Replace low-resolution portraits with a consistent photo shoot; add LinkedIn URLs in `data/team.json`.

## Added in the November 2026 client review

### Intelligence (articles, English and Arabic)
- Each article is one file in `content/intelligence/`. The file name becomes the address: `my-article.json` is published as `intelligence-my-article.html` (and `ar/intelligence-my-article.html`).
- An article appears in a language when it has a title and a body in that language. `"draft": true` keeps it off the site.
- Editor: open `/admin/` on the site. It saves straight to the GitHub repository, and the deploy workflow rebuilds the site (about a minute).
  Signing in needs a GitHub account with write access to the repository. "Sign In Using Access Token" works as is; for a "Sign In with GitHub" button, set `base_url` in `admin/config.yml` to a sign-in helper (see the comment there).
- `feed.xml` and `ar/feed.xml` are RSS feeds of the articles, for other sites and readers.

### Switches in `content.py` (SITE)
| Setting | What it turns on |
|---|---|
| `gtm_id` | Google Tag Manager (e.g. `GTM-ABC1234`). A consent notice appears and nothing loads until the visitor accepts; the legal text updates itself. Add Google Analytics inside Tag Manager. |
| `form_key` | A Web3Forms access key. The contact form then submits inside the page and emails the address registered with that key; without it the form opens the visitor's own email. |

### Other changes
- Poppins is the only Latin typeface (400, 500, 600, 700), with the type scale from the Lovable build of kiyan.sa.
- No page-to-page transition; the first-visit loader shows the mark and the tagline only.
- Switching language keeps the page, the section on screen and anything typed into the contact form.
- Headline claims and audit figures are removed; partner titles are not shown (they remain in `data/team.json` if needed later).
