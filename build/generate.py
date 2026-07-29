#!/usr/bin/env python3
"""Static site generator for DJORESTIS.com.

Usage:  python3 build/generate.py
Reads   build/content_<lang>.py  (en is required, fr/nl/el optional)
Writes  finished HTML into the repository root (en at /, others at /<lang>/),
        plus sitemap.xml. Everything emitted is plain static HTML/CSS/JS —
        upload the repo root to any web host.
"""
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE_URL = "https://djorestis.com"
LANGS = ["en", "fr", "nl", "el"]
EMAIL = "vasileiadis.orestis@gmail.com"

# Page keys in nav order. Slug "" means the language home page.
SLUGS = {
    "home":        {"en": "", "fr": "", "nl": "", "el": ""},
    "about":       {"en": "about", "fr": "a-propos", "nl": "over-mij", "el": "sxetika"},
    "services":    {"en": "services", "fr": "services", "nl": "diensten", "el": "ypiresies"},
    "corporate":   {"en": "corporate-event-dj-brussels", "fr": "dj-entreprise-bruxelles",
                    "nl": "bedrijfsfeest-dj-brussel", "el": "etairika-events"},
    "wedding":     {"en": "wedding-dj-brussels", "fr": "dj-mariage-bruxelles",
                    "nl": "bruiloft-dj-brussel", "el": "dj-gamou-vaptisis"},
    "greek":       {"en": "greek-dj-brussels", "fr": "dj-grec-bruxelles",
                    "nl": "griekse-dj-brussel", "el": "ellinas-dj-vryxelles"},
    "party":       {"en": "party-dj-brussels", "fr": "dj-soiree-privee-bruxelles",
                    "nl": "feest-dj-brussel", "el": "idiotika-parti"},
    "fullpackage": {"en": "full-package", "fr": "formule-complete",
                    "nl": "totaalpakket", "el": "plires-paketo"},
    "music":       {"en": "music", "fr": "musique", "nl": "muziek", "el": "mousiki"},
    "events":      {"en": "events", "fr": "evenements", "nl": "evenementen", "el": "ekdiloseis"},
    "contact":     {"en": "contact", "fr": "contact", "nl": "contact", "el": "epikoinonia"},
    "privacy":     {"en": "privacy", "fr": "confidentialite", "nl": "privacy", "el": "aporrito"},
}
NAV_KEYS = ["about", "services", "music", "events", "contact"]
SERVICE_KEYS = ["corporate", "wedding", "greek", "party", "fullpackage"]


def url_path(key, lang):
    slug = SLUGS[key][lang]
    prefix = "/" if lang == "en" else f"/{lang}/"
    return prefix if slug == "" else f"{prefix}{slug}/"


def out_file(key, lang):
    p = url_path(key, lang).strip("/")
    return ROOT / p / "index.html" if p else ROOT / "index.html"


def load_content(lang):
    f = ROOT / "build" / f"content_{lang}.py"
    if not f.exists():
        return None
    spec = importlib.util.spec_from_file_location(f"content_{lang}", f)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def localize_links(html, lang):
    for key in SLUGS:
        html = html.replace("{link:%s}" % key, url_path(key, lang))
    return html


LOGO_SVG = """<svg class="logo-svg" viewBox="0 0 500 68" role="img" aria-label="DJ Orestis" focusable="false">
  <text x="163" y="52" text-anchor="end" class="lg-word lg-gold">DJ</text>
  <g><circle cx="190" cy="38" r="19" fill="none" stroke="#C6A15B" stroke-width="2"/>
     <circle cx="190" cy="38" r="12" fill="none" stroke="#F4F1E8" stroke-width="0.8" opacity="0.45"/>
     <circle cx="190" cy="38" r="3.1" fill="#C6A15B"/></g>
  <text x="218" y="52" text-anchor="start" class="lg-word lg-ivory">RESTIS</text>
</svg>"""


def hreflang_tags(key, langs_present):
    tags = []
    for lg in LANGS:
        if lg in langs_present:
            tags.append(f'<link rel="alternate" hreflang="{lg}" href="{BASE_URL}{url_path(key, lg)}">')
    tags.append(f'<link rel="alternate" hreflang="x-default" href="{BASE_URL}{url_path(key, "en")}">')
    return "\n  ".join(tags)


def lang_switcher(key, lang, langs_present):
    items = []
    for lg in LANGS:
        if lg not in langs_present:
            continue
        cls = ' class="active"' if lg == lang else ""
        items.append(f'<li{cls}><a href="{url_path(key, lg)}" hreflang="{lg}" lang="{lg}">{lg.upper()}</a></li>')
    return '<ul class="lang-switch" aria-label="Language">' + "".join(items) + "</ul>"


def business_jsonld(mod):
    return {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "@id": BASE_URL + "/#business",
        "name": "DJ Orestis (DJORESTIS)",
        "description": mod.PAGES["home"]["desc"],
        "url": BASE_URL + "/",
        "logo": BASE_URL + "/assets/branding/favicon.svg",
        "image": BASE_URL + "/assets/branding/concept-2.svg",
        "email": EMAIL,
        "slogan": mod.STRINGS["tagline"],
        "address": {"@type": "PostalAddress", "addressLocality": "Brussels", "addressCountry": "BE"},
        "areaServed": ["Belgium", "Netherlands", "France", "Germany", "United Kingdom", "Greece"],
        "knowsLanguage": ["el", "en", "fr", "nl"],
        "priceRange": "$$",
        "sameAs": ["https://soundsgreekevents.be"],
    }


def service_jsonld(mod, key):
    page = mod.PAGES[key]
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": page["h1"],
        "description": page["desc"],
        "url": BASE_URL + url_path(key, mod.LANG),
        "serviceType": page.get("service_type", page["h1"]),
        "provider": {"@id": BASE_URL + "/#business"},
        "areaServed": ["Belgium", "Netherlands", "France", "Germany", "United Kingdom", "Greece"],
    }


def faq_jsonld(faq):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq
        ],
    }


def faq_html(faq, heading):
    items = "".join(
        f"<details class='faq-item'><summary>{q}</summary><div class='faq-body'><p>{a}</p></div></details>"
        for q, a in faq
    )
    return f"<section class='section faq'><div class='wrap narrow'><h2>{heading}</h2>{items}</div></section>"


def contact_form(s):
    f = s["form"]
    opts = "".join(f"<option>{o}</option>" for o in f["event_types"])
    return f"""
<form id="quote-form" class="quote-form" method="POST" action="" data-endpoint="" data-email="{EMAIL}"
      data-sent-msg="{f['sent']}" data-error-msg="{f['error']}" data-mailto-subject="{f['mailto_subject']}" novalidate>
  <div class="form-grid">
    <label>{f['name']}<input type="text" name="name" required autocomplete="name"></label>
    <label>{f['email']}<input type="email" name="email" required autocomplete="email"></label>
    <label>{f['phone']}<input type="tel" name="phone" autocomplete="tel"></label>
    <label>{f['event_type']}<select name="event_type">{opts}</select></label>
    <label>{f['date']}<input type="date" name="event_date"></label>
    <label>{f['location']}<input type="text" name="location" placeholder="{f['location_ph']}"></label>
    <label>{f['guests']}<input type="number" name="guests" min="1" max="5000"></label>
    <label>{f['budget']}<input type="text" name="budget" placeholder="{f['budget_ph']}"></label>
  </div>
  <label class="full">{f['extras']}
    <span class="checks">
      <label class="check"><input type="checkbox" name="extras" value="Sound &amp; light"> {f['x_sound']}</label>
      <label class="check"><input type="checkbox" name="extras" value="Photography"> {f['x_photo']}</label>
      <label class="check"><input type="checkbox" name="extras" value="Video"> {f['x_video']}</label>
    </span>
  </label>
  <label class="full">{f['message']}<textarea name="message" rows="5" placeholder="{f['message_ph']}"></textarea></label>
  <button type="submit" class="btn btn-gold">{f['submit']}</button>
  <p class="form-note">{f['note']}</p>
  <p class="form-status" role="status" aria-live="polite"></p>
</form>"""


def render_page(mod, key, langs_present):
    lang = mod.LANG
    s = mod.STRINGS
    page = mod.PAGES[key]
    path = url_path(key, lang)
    canonical = BASE_URL + path

    active_attr = ' class="active"'
    nav_links = "".join(
        f'<li><a href="{url_path(k, lang)}"{active_attr if k == key else ""}>{s["nav"][k]}</a></li>'
        for k in NAV_KEYS
    )
    svc_links = "".join(f'<li><a href="{url_path(k, lang)}">{s["nav"][k]}</a></li>' for k in SERVICE_KEYS)
    explore_links = "".join(f'<li><a href="{url_path(k, lang)}">{s["nav"][k]}</a></li>'
                            for k in ["about", "music", "events", "privacy"])

    schemas = []
    if key == "home":
        schemas.append(business_jsonld(mod))
    if key in SERVICE_KEYS:
        schemas.append(service_jsonld(mod, key))
    if page.get("faq"):
        schemas.append(faq_jsonld(page["faq"]))
    jsonld = "\n  ".join(
        f'<script type="application/ld+json">{json.dumps(sc, ensure_ascii=False)}</script>' for sc in schemas
    )

    body = localize_links(page["body"], lang)
    body = body.replace("{FORM}", contact_form(s))
    body = body.replace("{PLACEHOLDER_PHOTO}",
                        f"<div class='media-ph' role='img' aria-label='{s['photo_ph']}'>"
                        f"<span class='ph-ring'></span><span>{s['photo_ph']}</span></div>")
    body = body.replace("{PLACEHOLDER_VIDEO}",
                        f"<div class='media-ph wide' role='img' aria-label='{s['video_ph']}'>"
                        f"<span class='ph-ring'></span><span>{s['video_ph']}</span></div>")
    if page.get("faq"):
        body += faq_html(page["faq"], s["faq_heading"])

    hero_cls = "hero hero-home" if key == "home" else "hero"
    hero_kicker = f"<p class='kicker'>{page['kicker']}</p>" if page.get("kicker") else ""
    hero_sub = f"<p class='hero-sub'>{page['sub']}</p>" if page.get("sub") else ""
    hero_ctas = ""
    if key not in ("privacy", "contact"):
        hero_ctas = (f"<div class='hero-ctas'><a class='btn btn-gold' href='{url_path('contact', lang)}'>{s['cta_quote']}</a>"
                     f"<a class='btn btn-ghost' href='{url_path('services', lang)}'>{s['cta_services']}</a></div>")

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{page['title']}</title>
  <meta name="description" content="{page['desc']}">
  <link rel="canonical" href="{canonical}">
  {hreflang_tags(key, langs_present)}
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="DJORESTIS">
  <meta property="og:title" content="{page['title']}">
  <meta property="og:description" content="{page['desc']}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{BASE_URL}/assets/og-image.png">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" type="image/svg+xml" href="/assets/branding/favicon.svg">
  <link rel="apple-touch-icon" href="/assets/branding/favicon.svg">
  <link rel="preload" href="/assets/fonts/marcellus-400-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/assets/fonts/jost-400-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/assets/css/fonts.css">
  <link rel="stylesheet" href="/assets/css/style.css">
  {jsonld}
</head>
<body>
<a class="skip-link" href="#main">{s['skip']}</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="logo" href="{url_path('home', lang)}" aria-label="DJ Orestis — {s['nav']['home']}">{LOGO_SVG}</a>
    <nav class="site-nav" id="site-nav" aria-label="Main">
      <ul>{nav_links}</ul>
      {lang_switcher(key, lang, langs_present)}
      <a class="btn btn-gold nav-cta" href="{url_path('contact', lang)}">{s['cta_quote']}</a>
    </nav>
    <button class="nav-toggle" aria-controls="site-nav" aria-expanded="false"><span></span><span></span><span></span><span class="sr-only">Menu</span></button>
  </div>
</header>
<main id="main">
<section class="{hero_cls}">
  <div class="wrap">
    {hero_kicker}
    <h1>{page['h1']}</h1>
    {hero_sub}
    {hero_ctas}
  </div>
</section>
{body}
</main>
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div class="f-brand">
      {LOGO_SVG}
      <p class="f-tagline">{s['tagline']}</p>
      <p class="f-sge">{s['footer_sge']} <a href="https://soundsgreekevents.be" rel="noopener">Sounds Greek Events</a></p>
    </div>
    <nav aria-label="{s['footer_services']}"><h3>{s['footer_services']}</h3><ul>{svc_links}</ul></nav>
    <nav aria-label="{s['footer_explore']}"><h3>{s['footer_explore']}</h3><ul>{explore_links}</ul></nav>
    <div><h3>{s['footer_contact']}</h3>
      <ul>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>{s['footer_based']}</li>
        <li>{s['footer_areas']}</li>
      </ul>
      <ul class="socials" aria-label="Social media">
        <li><a href="#" aria-label="Instagram" data-social="instagram">Instagram</a></li>
        <li><a href="#" aria-label="Facebook" data-social="facebook">Facebook</a></li>
        <li><a href="#" aria-label="LinkedIn" data-social="linkedin">LinkedIn</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <p>© <span id="year">2026</span> DJORESTIS — DJ Orestis, Brussels. {s['footer_rights']}</p>
    <p><a href="{url_path('privacy', lang)}">{s['nav']['privacy']}</a></p>
  </div>
</footer>
<script src="/assets/js/main.js" defer></script>
</body>
</html>
"""


def main():
    mods = {}
    for lg in LANGS:
        mod = load_content(lg)
        if mod:
            mods[lg] = mod
    if "en" not in mods:
        sys.exit("content_en.py is required")
    langs_present = list(mods.keys())

    urls = []
    for lg, mod in mods.items():
        for key in SLUGS:
            if key not in mod.PAGES:
                continue
            html = render_page(mod, key, langs_present)
            dest = out_file(key, lg)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(html, encoding="utf-8")
            urls.append(BASE_URL + url_path(key, lg))
            print(f"  wrote {dest.relative_to(ROOT)}")

    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sitemap.append(f"  <url><loc>{u}</loc></url>")
    sitemap.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8")
    print(f"  wrote sitemap.xml ({len(urls)} URLs, languages: {', '.join(langs_present)})")


if __name__ == "__main__":
    main()
