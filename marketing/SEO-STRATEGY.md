# SEO strategy for djorestis.com — Belgian market

Based on five parallel research streams (competitor SERP analysis, Belgian directory
landscape, local-SEO controlled tests, AI-search/technical, multilingual & content
strategy). ~140 web searches total.

**Method caveat, stated up front:** direct page-fetching was blocked environment-wide during
this research, so findings come from search-result extraction rather than reading pages end
to end, and the search tool is US-geolocated (it approximates google.be rather than
replicating it). Architecture, pricing and difficulty observations are well-evidenced;
competitor schema details are inferred. Every load-bearing figure below is cited in
`research/` so it can be spot-checked.

---

## The strategic picture in one paragraph

You cannot win "wedding DJ Brussels" this year. `djprestigesound.be` has ~15 years of domain
age, a second domain for double SERP occupancy, 150+ reviews at 4.9, and a programmatic
city×service×language page matrix — they hold 4 of 8 slots on that query. What you *can* win,
quickly, is **Greek**: `dj grec bruxelles` / `griekse dj brussel` / `greek dj brussels` have
effectively no competition, and Google currently serves generic fallbacks because nothing
Greek-specific exists in Brussels. That is a defensible moat no competitor can copy. The
second opening is **Dutch** (`bruiloft dj brussel`), where the field is thin. The third is
**corporate**, where no competitor has a dedicated landing page — and you already do.

Two things outrank every item on this list: **a verified Google Business Profile** (~32% of
local signal; the map pack takes 44–58% of clicks) and **reviews**. For Q1, those will
out-earn the entire website.

## Realistic ranking difficulty

| Target | Verdict |
|---|---|
| Greek queries (all languages) | **1–6 months** — no real competition. Priority one |
| `bruiloft dj brussel` (NL) | **6–9 months** — thin field, crude competitors |
| Corporate queries | **6–12 months** — fragmented, no competitor landing page |
| `wedding dj brussels` | **12+ months** — Prestige Sound + directories own it |
| `dj mariage bruxelles` | **12–18 months**, top 3 may be unrealistic — 7 of 8 results are directories. **Get listed *in* them instead of fighting them** |
| `party dj brussels` | **12+ months**, weak intent. Deprioritise |

---

# The 10 changes

### 1. Publish pricing — "from €X" on every service page
**Highest-confidence recommendation in this document.** Survey data: 78% of couples say
pricing is the #1 factor in deciding who to contact; 80% look for it first; **30% will not
enquire at all without it**. Roughly 67% of vendors who hide pricing give exactly your stated
reason ("I'd rather explain on a call") — meaning transparency is a differentiator, not a
risk. You already publish market ranges in `/blog/dj-cost-belgium-price-guide/`, but your
service pages show nothing, so a visitor comparing three DJs has no reason to pick you.
Add a "from €X" line to each service page in all four languages. I searched deliberately for
counter-evidence and found none published.
*Needs from you: your actual starting prices.*

### 2. Fix the restaurant page — it targets the wrong intent
`restaurant dj brussels` returns *venues* (people looking for a restaurant with music), not
restaurateurs hiring a resident DJ. As written, the page will attract traffic that never
converts. Reposition it explicitly B2B: target "resident DJ for restaurants", "Greek night
for your venue", and speak to owners about covers and bar revenue rather than to guests.

### 3. Add real photographs — still the biggest single gap
The site has **zero content images**. No image search presence, no visual trust, nothing for
a corporate planner to judge you by. This blocks conversion on every page and every paid
click. When you have them: WebP, explicit width/height, `fetchpriority="high"` on the hero,
and never lazy-load the largest image. See `PHOTOS.md`.
*Needs from you: the photos.*

### 4. Turn the event recaps into venue pages
The strongest idea in the research. Couples search **"[vendor] at [venue name]"** *with the
date already booked* — the most qualified leads that exist online. Venue names are also
language-neutral across FR/NL/EN, so one page serves all three markets. Your nine event
recaps are venue pages in embryo: retitle them to lead with the venue, and add room,
acoustics and load-in detail.

### 5. Do **not** build per-city pages
Explicitly flagged as a live risk. Google's spam policy names this pattern, and the March
2026 core update hit local service businesses hardest — *"especially sites built on templated
location pages"* — with **domain-level** damage, meaning thin city pages drag down pages that
were fine. You cannot pass the uniqueness test for Antwerp or Ghent today: no venues played,
no testimonials. Earn each city page the week after your second real booking there.
Your existing 4-language structure is legitimate and is *not* this pattern.

### 6. Restructure service pages answer-first
The one AEO tactic with published experimental backing (KDD'24): quotations, statistics,
citations and authoritative language lifted AI citation rates 28–41%, while keyword stuffing
did nothing. Practically: question-shaped headings, self-contained passages that answer
without surrounding context, and concrete extractable facts — euro prices, travel radius in
km, guest capacity, languages, setup time. Name the entity ("DJ Orestis") rather than "I"
where it reads naturally, so an AI can attribute the fact.

### 7. Set up Bing Webmaster Tools + IndexNow
Best effort-to-return item on the technical list. **ChatGPT Search retrieves through Bing's
index** — a page Bing hasn't indexed cannot be cited by it — and Bing crawls small new sites
slowly. Free, one-time.
*Needs from you: 10 minutes at bing.com/webmasters.*

### 8. Move the site into `/docs` so internal files stop being published
Your `marketing/` and `build/` folders are served publicly — including the Google Ads
strategy and the blog fact-check notes. I've blocked both in robots.txt, but that only stops
crawlers, not direct access. The clean fix: move the site into a `/docs` folder and switch
the Pages source to it, after which nothing outside `/docs` is published.
*Needs from you: one settings change, coordinated with me so the site doesn't blink.*

### 9. Translate three blog posts to French — not the whole blog
French is the commercial priority in Brussels (81% speak it), but translating 19 posts is
wasted effort: all the pro-translation ROI evidence is e-commerce, not local services.
Translate the three highest-intent guides first — the pricing guide, how to choose a wedding
DJ, and when to book — measure in Search Console for 8–12 weeks, and extend to Dutch only if
it moves. Leave the event recaps untranslated; they are proof assets, not traffic assets.

### 10. Build the Greek institutional cluster
Your moat, and nobody else can claim it. The Greek Community of Brussels (ekbru.be), the
Orthodox Metropolis of Belgium and the Schaerbeek Greek parish are where **baptisms and
weddings actually originate** — that is lead generation, not just link building. Add the
Belgo-Hellenic Chamber of Commerce, which combines your two highest-margin segments (Greek
niche + corporate). Also get the contextual link from soundsgreekevents.be — keep it
editorial and in-content, never a sitewide footer link between two properties you own.

---

## Already implemented (no action needed from you)

- **Person + WebSite + BreadcrumbList schema** added; `LocalBusiness` gained `knowsAbout`
  and `founder`. Breadcrumbs are still an actively supported rich result.
- **Entity `sameAs` chain** now config-driven — it expands automatically as you register
  profiles. This is the cheapest E-E-A-T signal available to a solo provider.
- **Dead social links removed.** The footer linked to Instagram/TikTok/Facebook accounts that
  don't exist yet — broken links and a weak entity signal. They now appear only once real.
- **`dateModified` on all articles + accurate `lastmod` in the sitemap** (blog posts only —
  never invented for static pages, since Google only honours `lastmod` when it's truthful).
- **robots.txt now explicitly welcomes AI crawlers** and blocks `/build/` and `/marketing/`.
- **hreflang audited across all 76 pages**: zero broken alternates, zero missing return tags,
  zero canonical mismatches, blog correctly carries none. ~75% of implementations have errors;
  yours doesn't.
- **11 over-length page titles shortened** so Google stops truncating them mid-phrase.

## Deliberately NOT done, and why

- **No `AggregateRating` / `Review` schema.** Self-controlled review markup makes the page
  ineligible for star features and risks a manual action that nullifies all its structured
  data. Show testimonials as visible copy; drive real reviews to Google Business Profile.
- **hreflang stays language-only** (`fr`, `nl`) rather than `fr-BE` / `nl-BE`. Region codes
  would *narrow* reach — `fr-BE` stops serving your French pages to searchers in France,
  Luxembourg and Switzerland, contradicting your own European positioning.
- **No `llms.txt`.** Google states it isn't required; Google's Illyes confirmed no support and
  no plans; ~97% of published `llms.txt` files receive zero AI-crawler requests. Cargo cult.
- **`FAQPage` markup kept but downgraded in expectations.** FAQ rich results were deprecated
  in May 2026. No penalty, Google says don't remove it, and Bing still uses it — but it is no
  longer an SEO asset. It does feed Gemini-powered "Ask Maps", which sources from your site,
  your GBP and your reviews.
- **`.htaccess` left in place but understand it does nothing.** It's Apache config for the
  original Papaki plan; GitHub Pages ignores it entirely. It only *looks* like it handles
  www→apex redirects, HTTPS and folder blocking. DNS and Pages settings do that now.

## Claims worth distrusting

The 2025–26 local-SEO blogosphere is heavily AI-generated and invents plausible statistics.
Four widely-repeated figures traced to no primary source and should never be quoted:
"top-3 businesses average 47 reviews", "responding to reviews gains 2.3 positions", "74% of
consumers want reviews from the last 3 months" (BrightLocal 2025 actually measured recency
sensitivity *falling* to 20%), and "blogging produces 55% more traffic / 67% more leads"
(recycled ~2010 HubSpot marketing copy).

Similarly, schema markup is worth doing for rich results and entity resolution — but not as
an AI-visibility purchase. Ahrefs tracked 1,885 pages that added JSON-LD against ~4,000
controls and found **no major AI-citation uplift**. Vendor claims of "3.2× more citations"
have no disclosed methodology.

## Sequence

**Weeks 1–4 (highest return, mostly off-site):** verify the Google Business Profile, fill
Services exhaustively with detailed descriptions, start a slow review drip (~5/month toward
10+), list on eventplanner.be, WEWED.be, Infobel, Goudengids, Cueup, and the Greek
institutions. Set up Bing Webmaster Tools.

**Weeks 4–8 (on-site):** add pricing, fix the restaurant page's intent, add photos as they
arrive, restructure service pages answer-first.

**Months 2–4:** convert event recaps into venue pages, translate three guides to French,
pursue House of Weddings, apply for wedding-fair exhibitor listings.

**Months 4–9:** first meaningful organic rankings land. Earn city pages only where you have
booked real work. Reassess against Search Console data rather than assumption.
