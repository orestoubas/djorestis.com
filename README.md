# DJORESTIS.com

Static website for **DJ Orestis** — Brussels-based DJ for corporate events, weddings and
Greek parties across Belgium, the Netherlands, France, Germany, the UK and Greece.

Dark, business-elegant design · 4 languages (EN at `/`, FR/NL/EL at `/fr/`, `/nl/`, `/el/`) ·
full on-page SEO (per-page titles & descriptions, canonical + hreflang, schema.org
LocalBusiness / Service / FAQ markup, sitemap.xml, robots.txt) · no frameworks, no build
dependencies, no cookies.

## Repository layout

| Path | What it is |
|---|---|
| `index.html`, `about/`, `contact/`, … | The finished website (generated — don't edit by hand) |
| `fr/`, `nl/`, `el/` | French, Dutch, Greek versions |
| `assets/css`, `assets/js`, `assets/fonts` | Styles, one small script, self-hosted fonts (incl. Greek subsets) |
| `assets/branding/` | Logo concepts, favicon, palette & typography guides, `preview.html` |
| `build/generate.py` | Site generator — plain Python 3, no packages needed |
| `build/content_en.py` (+ `_fr` `_nl` `_el`) | **All text lives here.** Edit these, then regenerate. |
| `.htaccess`, `robots.txt`, `sitemap.xml`, `404.html` | Server config & SEO plumbing |

## Editing content

1. Edit the text in `build/content_<lang>.py` (every visible string of every page).
2. Run `python3 build/generate.py` — it rewrites all HTML pages and `sitemap.xml`.
3. Upload / commit the result.

Never edit the generated `index.html` files directly: the next regeneration would overwrite
your change.

## Deploying to Papaki shared hosting

1. Buy any Linux hosting package at papaki.gr and attach the domain `djorestis.com`.
2. In the Papaki/Plesk control panel, find **FTP access** (or File Manager).
3. Upload **everything except the `build/` folder and `.git`** into the web root
   (usually `httpdocs/` or `public_html/`), keeping the folder structure.
   Include the hidden `.htaccess` file — it sets up the 404 page, https/non-www
   redirects and caching.
4. Enable the free Let's Encrypt SSL certificate in the panel (one click in Plesk).
5. Done — the site is fully static, so there's nothing else to configure.

### Alternative: free hosting via GitHub Pages / Cloudflare Pages

The same files work as-is. Point the domain's DNS at the host, set the custom domain,
and deploys happen automatically on every push (`.htaccess` is ignored there; Pages
handles 404.html and https itself).

## Contact form

The quote form works out of the box by opening the visitor's email client, pre-filled
(mailto fallback). For proper in-page submission:

1. Create a free account at [formspree.io](https://formspree.io) (50 submissions/month free)
   with the address that should receive requests.
2. Copy the form endpoint URL (looks like `https://formspree.io/f/abcdwxyz`).
3. In `build/generate.py`, put that URL in the form's `data-endpoint=""` attribute,
   regenerate, upload.

## Go-live checklist (SEO)

- [ ] Verify the domain in [Google Search Console](https://search.google.com/search-console)
      and submit `https://djorestis.com/sitemap.xml`.
- [ ] Create a [Google Business Profile](https://business.google.com) ("DJ Orestis",
      category *DJ service*, area served Brussels/Belgium) — this is the single biggest
      lever for "wedding DJ Brussels"-type local searches, and enables Google reviews.
- [ ] After every event, send happy clients the Business-Profile review link.
- [ ] Replace the photo/video placeholders with real material (see `PHOTOS.md`).
- [ ] Fill in the real social media URLs in `build/generate.py` (footer `data-social` links).
- [ ] Optional: add analytics. A privacy-friendly option (Plausible, Simple Analytics)
      needs no cookie banner; Google Analytics 4 requires a consent banner in the EU.
- [ ] Ask soundsgreekevents.be to link to djorestis.com (a relevant backlink helps ranking).
