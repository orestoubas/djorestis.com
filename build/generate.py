#!/usr/bin/env python3
"""Static site generator for DJORESTIS.com.

Usage:  python3 build/generate.py
Reads   build/content_<lang>.py  (en required; fr/nl/el optional)
        build/blog_events.py, build/blog_guides.py  (optional, POSTS lists, EN only)
Writes  finished HTML into the repository root (en at /, others at /<lang>/),
        plus sitemap.xml. Everything emitted is plain static HTML/CSS/JS.
"""
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE_URL = "https://djorestis.com"
LANGS = ["en", "fr", "nl", "el"]

# ------------------------------------------------------------------ site config
EMAIL = "info@djorestis.com"

# WhatsApp number in international format, digits only (e.g. "32470123456").
# Leave empty to hide the WhatsApp button until the number is decided.
WHATSAPP_NUMBER = ""

# Google Analytics 4 Measurement ID (e.g. "G-XXXXXXXXXX").
# Leave empty to disable analytics AND the cookie-consent banner entirely.
GA4_ID = ""

# Company legal line for the footer + privacy page, e.g.
# "Company Name BV — BTW BE 0123.456.789". Empty = not shown.
COMPANY_LEGAL = ""

# ------------------------------------------------------------------ pages
# Page keys in order. Slug "" means the language home page.
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
    "restaurant":  {"en": "restaurant-dj-brussels", "fr": "dj-restaurant-bruxelles",
                    "nl": "restaurant-dj-brussel", "el": "dj-estiatorio"},
    "mykonos":     {"en": "greek-dj-europe", "fr": "dj-grec-europe",
                    "nl": "griekse-dj-europa", "el": "dj-mykonos-evropi"},
    "music":       {"en": "music", "fr": "musique", "nl": "muziek", "el": "mousiki"},
    "events":      {"en": "events", "fr": "evenements", "nl": "evenementen", "el": "ekdiloseis"},
    "contact":     {"en": "contact", "fr": "contact", "nl": "contact", "el": "epikoinonia"},
    "privacy":     {"en": "privacy", "fr": "confidentialite", "nl": "privacy", "el": "aporrito"},
}
NAV_KEYS = ["about", "services", "music", "events", "blog", "contact"]
SERVICE_KEYS = ["corporate", "wedding", "greek", "party", "fullpackage", "restaurant", "mykonos"]

BLOG_PATH = "/blog/"  # English only


def url_path(key, lang):
    if key == "blog":
        return BLOG_PATH
    slug = SLUGS[key][lang]
    prefix = "/" if lang == "en" else f"/{lang}/"
    return prefix if slug == "" else f"{prefix}{slug}/"


def out_file(path):
    p = path.strip("/")
    return ROOT / p / "index.html" if p else ROOT / "index.html"


def load_module(name):
    f = ROOT / "build" / f"{name}.py"
    if not f.exists():
        return None
    spec = importlib.util.spec_from_file_location(name, f)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def localize_links(html, lang):
    for key in SLUGS:
        html = html.replace("{link:%s}" % key, url_path(key, lang))
    html = html.replace("{link:blog}", BLOG_PATH)
    return html


LOGO_SVG = """<svg class="logo-svg" viewBox="0 0 500 68" role="img" aria-label="DJ Orestis" focusable="false">
  <text x="163" y="52" text-anchor="end" class="lg-word lg-gold">DJ</text>
  <g><circle cx="190" cy="38" r="19" fill="none" stroke="#C6A15B" stroke-width="2"/>
     <circle cx="190" cy="38" r="12" fill="none" stroke="#F4F1E8" stroke-width="0.8" opacity="0.45"/>
     <circle cx="190" cy="38" r="3.1" fill="#C6A15B"/></g>
  <text x="218" y="52" text-anchor="start" class="lg-word lg-ivory">RESTIS</text>
</svg>"""

WHATSAPP_SVG = """<svg viewBox="0 0 32 32" aria-hidden="true" focusable="false"><path fill="currentColor" d="M16 3C9.4 3 4 8.3 4 14.9c0 2.1.6 4.1 1.6 5.9L4 29l8.4-1.6c1.7.9 3.6 1.4 5.6 1.4 6.6 0 12-5.3 12-11.9S22.6 3 16 3zm0 21.8c-1.8 0-3.5-.5-5-1.3l-.4-.2-5 1 1-4.8-.3-.4c-1-1.6-1.5-3.4-1.5-5.2 0-5.5 4.6-10 10.2-10s10.2 4.5 10.2 10-4.6 9.9-10.2 9.9zm5.6-7.4c-.3-.2-1.8-.9-2.1-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.2-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.5-.6c.2-.2.2-.3.3-.6.1-.2 0-.4 0-.6-.1-.2-.7-1.7-1-2.3-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.1 1.1-1.1 2.7s1.2 3.1 1.3 3.3c.2.2 2.3 3.6 5.7 5 .8.3 1.4.5 1.9.7.8.2 1.5.2 2.1.1.6-.1 1.8-.8 2.1-1.5.3-.7.3-1.3.2-1.5-.1-.1-.3-.2-.6-.4z"/></svg>"""


def business_jsonld(mod):
    data = {
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
    if COMPANY_LEGAL:
        data["legalName"] = COMPANY_LEGAL
    return data


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


def article_jsonld(post):
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": post["title"],
        "description": post["desc"],
        "datePublished": post["date"],
        "url": BASE_URL + BLOG_PATH + post["slug"] + "/",
        "inLanguage": "en",
        "author": {"@type": "Person", "name": "DJ Orestis", "url": BASE_URL + "/about/"},
        "publisher": {"@id": BASE_URL + "/#business"},
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


def nav_label(mod, en_mod, key):
    if key == "blog":
        return mod.STRINGS["nav"].get("blog", "Blog")
    return mod.STRINGS["nav"].get(key) or en_mod.STRINGS["nav"].get(key, key)


def hreflang_tags(key, mods):
    tags = []
    for lg in LANGS:
        if lg in mods and key in mods[lg].PAGES:
            tags.append(f'<link rel="alternate" hreflang="{lg}" href="{BASE_URL}{url_path(key, lg)}">')
    if len(tags) <= 1:
        return ""
    tags.append(f'<link rel="alternate" hreflang="x-default" href="{BASE_URL}{url_path(key, "en")}">')
    return "\n  ".join(tags)


def lang_switcher(key, lang, mods):
    items = []
    for lg in LANGS:
        if lg not in mods:
            continue
        # Blog is EN-only: other languages link to their home page.
        if key == "blog" or key not in mods[lg].PAGES:
            href = url_path("home", lg) if lg != "en" else url_path(key, "en")
        else:
            href = url_path(key, lg)
        cls = ' class="active"' if lg == lang else ""
        items.append(f'<li{cls}><a href="{href}" hreflang="{lg}" lang="{lg}">{lg.upper()}</a></li>')
    return '<ul class="lang-switch" aria-label="Language">' + "".join(items) + "</ul>"


def cookie_banner(s):
    if not GA4_ID:
        return ""
    c = s.get("cookie") or {
        "text": "This site uses cookies for anonymous visitor statistics.",
        "accept": "Accept", "decline": "Decline",
    }
    return f"""
<div id="cookie-banner" hidden data-ga="{GA4_ID}">
  <p>{c['text']}</p>
  <div class="cookie-actions">
    <button class="btn btn-gold" data-consent="yes">{c['accept']}</button>
    <button class="btn btn-ghost" data-consent="no">{c['decline']}</button>
  </div>
</div>"""


def whatsapp_button(s):
    if not WHATSAPP_NUMBER:
        return ""
    label = s.get("whatsapp_label", "Chat on WhatsApp")
    return (f'<a class="wa-btn" href="https://wa.me/{WHATSAPP_NUMBER}" target="_blank" rel="noopener" '
            f'aria-label="{label}" title="{label}">{WHATSAPP_SVG}</a>')


def page_shell(mod, en_mod, mods, *, key, title, desc, canonical, hreflang, robots,
               hero_html, body, schemas, lang):
    s = mod.STRINGS
    active_attr = ' class="active"'
    nav_items = []
    for k in NAV_KEYS:
        href = BLOG_PATH if k == "blog" else url_path(k, lang)
        active = active_attr if k == key else ""
        nav_items.append(f'<li><a href="{href}"{active}>{nav_label(mod, en_mod, k)}</a></li>')
    nav_links = "".join(nav_items)
    svc_links = "".join(
        f'<li><a href="{url_path(k, lang) if k in mod.PAGES else url_path(k, "en")}">{nav_label(mod, en_mod, k)}</a></li>'
        for k in SERVICE_KEYS
    )
    explore_links = "".join(
        f'<li><a href="{url_path(k, lang)}">{nav_label(mod, en_mod, k)}</a></li>'
        for k in ["about", "music", "events", "privacy"]
    )

    jsonld = "\n  ".join(
        f'<script type="application/ld+json">{json.dumps(sc, ensure_ascii=False)}</script>' for sc in schemas
    )
    hreflang_block = (hreflang + "\n  ") if hreflang else ""
    robots_block = f'<meta name="robots" content="{robots}">\n  ' if robots else ""
    legal_line = f"<p class='f-legal'>{COMPANY_LEGAL}</p>" if COMPANY_LEGAL else ""

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  {robots_block}<link rel="canonical" href="{canonical}">
  {hreflang_block}<meta property="og:type" content="website">
  <meta property="og:site_name" content="DJORESTIS">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
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
      {lang_switcher(key, lang, mods)}
      <a class="btn btn-gold nav-cta" href="{url_path('contact', lang)}">{s['cta_quote']}</a>
    </nav>
    <button class="nav-toggle" aria-controls="site-nav" aria-expanded="false"><span></span><span></span><span></span><span class="sr-only">Menu</span></button>
  </div>
</header>
<main id="main">
{hero_html}
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
        <li><a href="https://instagram.com/djorestis" rel="noopener" aria-label="Instagram" data-social="instagram">Instagram</a></li>
        <li><a href="https://tiktok.com/@djorestis" rel="noopener" aria-label="TikTok" data-social="tiktok">TikTok</a></li>
        <li><a href="https://facebook.com/djorestis" rel="noopener" aria-label="Facebook" data-social="facebook">Facebook</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <div><p>© <span id="year">2026</span> DJORESTIS — DJ Orestis, Brussels. {s['footer_rights']}</p>{legal_line}</div>
    <p><a href="{url_path('privacy', lang)}">{s['nav']['privacy']}</a></p>
  </div>
</footer>
{whatsapp_button(s)}{cookie_banner(s)}
<script src="/assets/js/main.js" defer></script>
</body>
</html>
"""


def render_page(mods, en_mod, lang, key):
    mod = mods[lang]
    s = mod.STRINGS
    page = mod.PAGES[key]
    path = url_path(key, lang)
    canonical = BASE_URL + path

    schemas = []
    if key == "home":
        schemas.append(business_jsonld(mod))
    if key in SERVICE_KEYS:
        schemas.append(service_jsonld(mod, key))
    if page.get("faq"):
        schemas.append(faq_jsonld(page["faq"]))

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
    hero_html = f"""<section class="{hero_cls}">
  <div class="wrap">
    {hero_kicker}
    <h1>{page['h1']}</h1>
    {hero_sub}
    {hero_ctas}
  </div>
</section>"""

    return page_shell(mod, en_mod, mods, key=key, title=page["title"], desc=page["desc"],
                      canonical=canonical, hreflang=hreflang_tags(key, mods), robots=None,
                      hero_html=hero_html, body=body, schemas=schemas, lang=lang)


def render_blog_index(mods, en_mod, posts):
    s = en_mod.STRINGS
    b = s.get("blog", {})
    title = b.get("index_title", "Blog — Stories & Guides from the Booth | DJ Orestis")
    desc = b.get("index_desc", "Event stories and practical guides from DJ Orestis: corporate parties, weddings and Greek nights in Brussels and across Europe.")
    h1 = b.get("h1", "From the <span class='gold'>booth</span>")
    sub = b.get("sub", "Event stories, lessons learned and practical guides — weddings, corporate nights and Greek parties across Europe.")

    cards = []
    for p in posts:
        date_h = f"<time datetime='{p['date']}'>{p['date']}</time>"
        cards.append(
            f"<a class='card post-card' href='{BLOG_PATH}{p['slug']}/'>"
            f"<p class='post-meta'>{date_h} · {p['category']}</p>"
            f"<h3>{p['title']}</h3><p>{p['desc']}</p>"
            f"<span class='card-more'>{b.get('read_more', 'Read the story')} →</span></a>"
        )
    body = f"""<section class="section"><div class="wrap"><div class="card-grid posts">{''.join(cards)}</div></div></section>
<section class="section cta-band"><div class="wrap center"><h2>{b.get('cta', 'Planning something similar?')}</h2>
<a class="btn btn-gold" href="{url_path('contact', 'en')}">{s['cta_quote']}</a></div></section>"""

    hero = f"""<section class="hero"><div class="wrap">
    <p class='kicker'>Blog</p><h1>{h1}</h1><p class='hero-sub'>{sub}</p></div></section>"""

    return page_shell(mods["en"], en_mod, mods, key="blog", title=title, desc=desc,
                      canonical=BASE_URL + BLOG_PATH, hreflang="", robots=None,
                      hero_html=hero, body=body, schemas=[], lang="en")


def render_blog_post(mods, en_mod, post):
    s = en_mod.STRINGS
    b = s.get("blog", {})
    path = BLOG_PATH + post["slug"] + "/"
    body_html = localize_links(post["body"], "en")
    body_html = body_html.replace("{PLACEHOLDER_PHOTO}",
                                  f"<div class='media-ph' role='img' aria-label='{s['photo_ph']}'>"
                                  f"<span class='ph-ring'></span><span>{s['photo_ph']}</span></div>")
    body = f"""<article class="section blog-post"><div class="wrap narrow">
{body_html}
<p class="post-back"><a href="{BLOG_PATH}">← {b.get('back', 'All articles')}</a></p>
</div></article>
<section class="section cta-band"><div class="wrap center"><h2>{b.get('cta', 'Planning something similar?')}</h2>
<a class="btn btn-gold" href="{url_path('contact', 'en')}">{s['cta_quote']}</a></div></section>"""

    hero = f"""<section class="hero"><div class="wrap">
    <p class='kicker'><time datetime="{post['date']}">{post['date']}</time> · {post['category']}</p>
    <h1>{post['h1'] if post.get('h1') else post['title']}</h1>
    {f"<p class='hero-sub'>{post['sub']}</p>" if post.get('sub') else ''}</div></section>"""

    return page_shell(mods["en"], en_mod, mods, key="blog", title=post["title"] + " | DJ Orestis",
                      desc=post["desc"], canonical=BASE_URL + path, hreflang="", robots=None,
                      hero_html=hero, body=body, schemas=[article_jsonld(post)], lang="en")


def main():
    mods = {}
    for lg in LANGS:
        mod = load_module(f"content_{lg}")
        if mod:
            mods[lg] = mod
    if "en" not in mods:
        sys.exit("content_en.py is required")
    en_mod = mods["en"]

    urls = []
    for lg, mod in mods.items():
        for key in SLUGS:
            if key not in mod.PAGES:
                continue
            html = render_page(mods, en_mod, lg, key)
            dest = out_file(url_path(key, lg))
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(html, encoding="utf-8")
            urls.append(BASE_URL + url_path(key, lg))
    print(f"  wrote {len(urls)} pages ({', '.join(mods.keys())})")

    # ------------------------------------------------------------------ blog
    posts = []
    for name in ("blog_events", "blog_guides"):
        mod = load_module(name)
        if mod and hasattr(mod, "POSTS"):
            posts.extend(mod.POSTS)
    if posts:
        posts.sort(key=lambda p: p["date"], reverse=True)
        slugs_seen = set()
        for p in posts:
            if p["slug"] in slugs_seen:
                sys.exit(f"duplicate blog slug: {p['slug']}")
            slugs_seen.add(p["slug"])
            dest = out_file(BLOG_PATH + p["slug"] + "/")
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(render_blog_post(mods, en_mod, p), encoding="utf-8")
            urls.append(BASE_URL + BLOG_PATH + p["slug"] + "/")
        dest = out_file(BLOG_PATH)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render_blog_index(mods, en_mod, posts), encoding="utf-8")
        urls.append(BASE_URL + BLOG_PATH)
        print(f"  wrote blog: index + {len(posts)} posts")

    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sitemap.append(f"  <url><loc>{u}</loc></url>")
    sitemap.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8")
    print(f"  wrote sitemap.xml ({len(urls)} URLs)")


if __name__ == "__main__":
    main()
