# Competitive SEO Analysis — DJ / Event Entertainment, Brussels (Belgium)

**Client:** DJ Orestis — djorestis.com
**Profile:** Brussels-based Greek DJ. Corporate events, weddings/baptisms, Greek community parties.
**Domain status:** Brand new (launched 2026-08-01). Zero authority, zero backlinks, zero indexation.
**Site:** Static, 4 languages (EN/FR/NL/EL), 7 SEO landing pages + 19-post blog.
**Research date:** 2026-08-01

---

## 0. Methodology & data-quality caveat — READ THIS FIRST

This matters for how much weight you put on each section below.

- **All SERP data here comes from the `WebSearch` tool, which is US-geolocated.** It is *not* a literal `google.be` scrape from a Brussels IP. Results are directionally accurate for who competes in this niche, but **actual Google.be rankings, and especially the local map pack, will differ** — local packs are the single biggest divergence, and they are invisible to this tool.
- **Confirmed artifact of US geo-targeting:** the query `corporate event dj brussels` returned `thebash.com/search/dj-brussels-il` — that is **Brussels, Illinois**, not Belgium. The Bash is a US marketplace and is almost certainly *not* a real competitor on google.be. Discount it.
- **`WebFetch` was blocked environment-wide.** Every fetch returned HTTP 403, including neutral high-traffic targets (`cueup.io`, `houseofweddings.com`), not just bot-protected competitor sites. Bash-based proxy diagnostics were also blocked by the permission classifier, so I could not confirm the root cause or work around it.
- **Consequence:** the competitor teardown in §2 is built from **SERP titles, meta descriptions, indexed URL paths, and search-snippet content — not from reading page source.** This means URL architecture, pricing, languages, and review counts are well-evidenced. **Schema markup, exact page counts, internal linking, and Core Web Vitals could NOT be verified** and are flagged as UNVERIFIED throughout. Do not present the schema claims to the client as fact.

**To close these gaps you need:** a VPN/Belgian-IP manual SERP check, plus a crawler (Screaming Frog) or simple `view-source:` on the 4 competitor domains. That is roughly 2 hours of manual work and it is the single highest-value next step.

---

## 1. SERP composition per target keyword

### 1.1 `wedding dj brussels` (EN)

| # | URL | Type |
|---|---|---|
| 1 | https://www.houseofweddings.com/en/dj/dj-s-in-brussels | Directory (BE wedding portal) |
| 2 | https://djprestigesound.be/en/dj-brussels | **Individual DJ/agency** |
| 3 | https://cueup.io/brussels/book-dj | Marketplace |
| 4 | https://www.houseofweddings.com/en/dj/dj-wedding-party/dj-wedding-in-brussels | Directory |
| 5 | https://djprestigesound.be/en | **Individual DJ/agency** |
| 6 | https://djprestigesound.be/en/catalog-2025.php | **Individual DJ/agency** |
| 7 | https://www.gigheaven.com/search/wedding-djs/belgium/brussels.html | Marketplace |
| 8 | https://djprestigesound.com/en/index.php | **Same operator, second domain** |

**Read:** Directories + marketplaces hold ~50% of the page. Prestige Sound occupies **4 of 8 slots across two domains** — near-total dominance of the only non-directory real estate.

### 1.2 `dj mariage bruxelles` (FR) — highest commercial intent

| # | URL | Type |
|---|---|---|
| 1 | https://www.houseofweddings.com/fr/dj/mariage/bruxelles | Directory |
| 2 | https://www.mariages.net/musique-mariage/dj-mariage/bruxelles-capitale | Marketplace (The Knot Worldwide) |
| 3 | https://www.mariages.net/musique-mariage/dj-mariage/belgique | Marketplace |
| 4 | https://ringtwice.be/fr/dj-mariage/bruxelles | Marketplace (BE services) |
| 5 | https://sonocadillac.be/index.php/dj-mariage/ | **Individual DJ** |
| 6 | https://www.mariage.be/ambiance-mariage/sonorisation-mariage-et-disc-jockey-belgique-bruxelles.asp | Directory |
| 7 | https://www.eventigo.eu/artists/musique/dj/mariage/bruxelles | Marketplace |
| 8 | https://www.eventigo.eu/artists-in/musique/dj/bruxelles | Marketplace |

**Read:** This is the **most directory-saturated SERP of all** — 7 of 8 results are portals. Only one independent DJ (Sono Cadillac) breaks through, and it targets Brabant Wallon rather than Brussels proper. Brutal for a new domain.

### 1.3 `bruiloft dj brussel` (NL) — the weak spot

| # | URL | Type |
|---|---|---|
| 1 | https://dj-bruiloft-brussel.djsteven.be/ | **Individual DJ — exact-match subdomain** |
| 2 | https://dj-bruiloft-brussel.hifferman-events.be/ | **Individual DJ — exact-match subdomain** |
| 3 | https://www.houseofweddings.com/nl/dj/trouwfeest/brussel | Directory |
| 4 | https://www.houseofweddings.com/nl/dj/brussel | Directory |
| 5 | https://www.evenses.com/brussel | Agency/booking platform (multi-country) |

**Read — this is the most important finding in the whole document.** Only ~5 results returned, versus 8 for FR/EN. The top two are **exact-match-domain subdomains** (`dj-bruiloft-brussel.djsteven.be`) — a crude, dated SEO tactic that only works when competition is thin. Nobody has built a genuinely good Dutch page for Brussels. **This SERP is soft.**

### 1.4 `corporate event dj brussels` (EN)

| # | URL | Type |
|---|---|---|
| 1 | https://djprestigesound.be/en/dj-brussels | **Individual DJ/agency** |
| 2 | ~~https://www.thebash.com/search/dj-brussels-il~~ | **US geo artifact — Brussels, ILLINOIS. Ignore.** |
| 3 | https://cueup.io/brussels/book-dj | Marketplace |
| 4 | https://djprestigesound.be/en | **Individual DJ/agency** |
| 5 | https://djbruxelles.com/ | **Agency** |
| 6 | https://djprestigesound.be/en/dj-belgique | **Individual DJ/agency** |
| 7 | https://www.gigheaven.com/search/event-djs/belgium/brussels.html | Marketplace |
| 8 | https://www.gigheaven.com/search/event-djs/belgium.html | Marketplace |

**Read:** Note what is *missing* — **not one result is a dedicated corporate-DJ landing page.** Prestige Sound ranks with general "DJ Brussels" pages, not corporate-specific ones. The corporate intent is being served by pages that don't actually target it. That is a content gap.

### 1.5 `dj entreprise bruxelles` (FR)

| # | URL | Type |
|---|---|---|
| 1 | https://www.dj-events.be/prestations/professionnels/animation-dj-entreprise | **Individual DJ — dedicated corporate page** |
| 2 | https://refevent.be/prestataires/dj/bruxelles | Directory |
| 3 | https://www.starnight.be/dj-soiree/soiree-dentreprise/chouette-soiree-dentreprise-au-centre-de-bruxelles/ | **DJ/AV company — blog-style post** |
| 4 | https://linkaband.com/animation-entreprise/dj | Marketplace (FR) |
| 5 | https://www.eventigo.eu/artists-in/musique/dj/bruxelles | Marketplace |
| 6 | https://www.vnh-events.com/dj-entreprise | **Agency** |
| 7 | https://www.blindtestlive.com/dj-entreprise | Agency (adjacent niche) |
| 8 | https://www.dj-dee-l.com/ | **Individual DJ** |

**Read:** Far more fragmented and **far more individual-DJ-friendly** than `dj mariage bruxelles`. Five independents rank. Directory grip is weak. Notably, Starnight ranks with what is effectively a *blog post* about a corporate party in central Brussels — proof that content, not just service pages, wins here. **This is the best FR opportunity.**

### 1.6 `greek dj brussels` / `dj grec bruxelles` — the open goal

Searched `"greek dj" brussels hire baptism wedding`, `greek dj brussels Greek music party Belgium`, and `"dj grec" bruxelles mariage grec Belgique`.

| Result | Type |
|---|---|
| https://www.soundsgreekevents.be/ | **The only genuine Greek-DJ competitor in Belgium** |
| https://www.soundsgreekevents.be/events | Same operator |
| https://allevents.in/brussels/greek | Events aggregator |
| https://www.eventbrite.com/d/belgium--brussel--10471/music--events/dj/ | Events aggregator |
| https://scarlettentertainment.com/us/acts/traditional-greek-dj | Intl. booking agency (not BE-specific) |
| https://www.tripadvisor.com/...Kafenio-Brussels.html | Restaurant review (irrelevant) |
| https://www.gigheaven.com/search/event-djs/belgium/brussels.html | Generic marketplace fallback |

**Critical findings:**

1. **`dj grec bruxelles` (FR) has effectively NO dedicated competitor.** The search returned only generic wedding-DJ directories — Google had nothing Greek-specific to serve and fell back to generic results. **This is an unclaimed SERP.**
2. **`soundsgreekevents.be` already features DJ Orestis by name**, alongside DJ Giannis Vagenas, described as performing back-to-back Greek sets, based in Woluwe-Saint-Lambert. Positioning: "100% Greek music, plate smashing, flower throwing."

**⚠️ This requires a direct conversation with the client before any strategy is built on it.** Sounds Greek Events is either (a) the client's own existing brand/collective, (b) a former partner, or (c) an active competitor. The SEO implications are opposite in each case:
- If **own/affiliated** → it is an authority asset. Interlink it, and it becomes the fastest backlink + entity-consolidation win available.
- If **competitor** → the client is trying to outrank a site that already ranks for his own personal name, which is a brand-confusion problem before it is an SEO problem.

Do not proceed on the Greek pages until this is resolved. It changes everything about that cluster.

### 1.7 Supporting SERPs

**`party dj brussels`** — dominated by marketplaces (`cueup.io`, `gigheaven.com` ×2, `twine.net`), plus `djbruxelles.com`, `scarlettentertainment.com`. Generic, low-intent, heavily aggregated.

**`restaurant dj brussels`** — genuinely different SERP: no DJ-service pages rank. Results are **venues** (`mix.brussels/romeo`, `thehoxton.com/brussels/tope-restaurant`, `akaibrussels.com`, `roostersbrussels`), one B2B agency (`driiing.be/en/dj-in-store-event/`), and an editorial piece (`mixmag.net`). **Searcher intent is "where can I go hear a DJ," not "hire a DJ."** The client's `/restaurant-dj-brussels/` page is targeting a query whose intent it does not match — see §5.

---

## 2. Competitor teardown

> **UNVERIFIED where marked** — see §0. Architecture/pricing/language claims are evidence-backed from indexed URLs and snippets; schema and page counts are inference.

### 2.1 djprestigesound.be — the market leader, by a distance

The one competitor that matters most.

**Confirmed URL architecture** (every URL below appeared in live search results):

*City pages, FR:* `/fr/dj-liege`, `/fr/dj-bruges`, `/fr/dj-mariage-liege`, `/fr/dj-mariage-bruges`
*City pages, NL:* `/nl/dj-hasselt`
*City pages, EN:* `/en/dj-louvain`, `/en/dj-brussels`, `/en/dj-belgique`
*Service pages:* `/en/services/mariage`, `/fr/ceremonie`
*Pricing:* `/fr/tarifs`, `/nl/tarifs`
*Content:* `/fr/tarifs-dj-belgique-2026`
*Campaign:* `/en/catalog-2025.php`
*Second domain:* `djprestigesound.com/en/index.php`

| Attribute | Finding |
|---|---|
| Structure | **Programmatic city × service × language matrix.** Pattern: `/{lang}/dj-{city}` and `/{lang}/dj-mariage-{city}`. Confirmed cities: Brussels, Liège, Bruges, Leuven, Hasselt + Belgium-wide. Likely 60–100+ indexed pages (UNVERIFIED count). |
| Languages | **Trilingual FR/NL/EN**, true directory-per-language (`/fr/`, `/nl/`, `/en/`). Explicitly markets "trilingue" as a selling point. |
| Pricing | **Fully transparent, in title tags.** €800 HTVA evening (5h); €1300 HTVA full day; €1500 DJ+sax duo; sound/light add-on from €250. Terms published: 30% deposit, balance 7 days prior. |
| Reviews | **150+ Google reviews, 4.9/5.** Rating injected into title tags ("4.9★", "5★"). |
| Blog | Weak/none as a true blog — but ranks a **dated money-page** (`/fr/tarifs-dj-belgique-2026`) that functions as content. |
| Schema | **UNVERIFIED.** Rich-result-style titles strongly suggest LocalBusiness + AggregateRating + Offer, but not confirmed. |
| Differentiators | 15 yrs, 500+ events, 200+ weddings/yr, 4K drone upsell, live musicians (sax/violin/piano), venue-specific knowledge (castles, estates, hotels). |
| Second domain | `djprestigesound.com` runs in parallel — double SERP occupancy. |

**Why it ranks:** the trifecta — scaled programmatic geo/service coverage, genuine review authority, and 15 years of domain age/links. Title tags are aggressively CTR-optimised (price + rating + benefit).

### 2.2 djbruxelles.com

| Attribute | Finding |
|---|---|
| Positioning | "Best Agency for Private Parties & Events in Brussels" — agency with roster, not solo DJ |
| Segments | Corporate, weddings, **christenings/baptisms**, club parties |
| Ranks for | `corporate event dj brussels`, `party dj brussels` |
| Structure | UNVERIFIED (403). Homepage-led; appears shallow — homepage does the ranking, not deep pages |
| Domain | **Exact-match domain for "dj bruxelles"** — significant standing advantage on the FR head term |
| Note | Also targets baptisms — **direct overlap with the client's baptism angle** |

### 2.3 sonocadillac.be

| Attribute | Finding |
|---|---|
| URL | `sonocadillac.be/` , `/index.php/dj-mariage/` |
| Positioning | Wedding entertainment, Brussels + **Brabant Wallon** (15+ yrs) |
| Offer | Tiered packages: sound/light/video, **unlimited hours**, spark jets, heavy fog, custom playlists |
| Ranks for | `dj mariage bruxelles` (#5) — the only independent on that SERP |
| Weakness | **Mono-lingual FR, `/index.php/` CMS paths, Brabant-Wallon-first positioning.** Beatable on Brussels-specific and multilingual intent |
| Citations | Listed on `ideesmariage.be/ab-sono-cadillac/profil/dj-sonorisation/1480/tubize` |

### 2.4 dj-events.be

| Attribute | Finding |
|---|---|
| URL | `/prestations/professionnels/animation-dj-entreprise`, `/prestations/prives/animation-dj-mariage` |
| Structure | **Clean segment split: `/prestations/professionnels/` vs `/prestations/prives/`** — a genuinely good IA the client should copy |
| Ranks for | **#1 `dj entreprise bruxelles`** |
| Coverage | Brussels, Brabant Wallon, Brabant Flamand |
| Why it ranks | Dedicated corporate page with clean topical URL — beats bigger sites that lack one |

### 2.5 starnight.be

| Attribute | Finding |
|---|---|
| Structure | Deep, well-organised, **bilingual FR + `/en/`**: `/en/our-services/`, `/en/our-equipment/`, `/en/prices/`, `/en/contact/`, `/en/links/`, `/en/our-equipment/equipment-delirium-pack/`, `/dj-soiree/` |
| Pricing | **Dedicated `/en/prices/` page** |
| Content play | Ranks for `dj entreprise bruxelles` via a **narrative event write-up**: `/dj-soiree/soiree-dentreprise/chouette-soiree-dentreprise-au-centre-de-bruxelles/` |
| Lesson | **Event recap posts with venue + district names rank for commercial corporate queries.** Directly replicable by the client. |

### 2.6 soundsgreekevents.be

| Attribute | Finding |
|---|---|
| Positioning | Greek DJ + private parties, weddings, **baptism days**, equipment lease |
| Location | Woluwe-Saint-Lambert, Brussels |
| Talent | **DJ Orestis** + DJ Giannis Vagenas |
| Pages | `/` , `/events` — appears very shallow |
| Status | **Only real Greek-DJ competitor in BE — and relationship to client is UNRESOLVED (see §1.6)** |

### 2.7 Others noted

`evenses.com` / `evenses.be` (multi-country platform: `/brussel`, `/dj`, `/double-dj`, `/nederlandse-DJ`) · `vnh-events.com/dj-entreprise` · `dj-dee-l.com` (350+ events) · `driiing.be` (B2B in-store) · `hifferman-events.be` & `djsteven.be` (EMD subdomains) · `scarlettentertainment.com` (intl., name-drops Ferrero/Belfius/AG Insurance as corporate clients).

---

## 3. Directories & marketplaces — competitors AND listing opportunities

Ranked by observed SERP frequency. **Every one of these is a listing the client should claim.**

| Platform | URLs seen | Notes / priority |
|---|---|---|
| **House of Weddings** | `/en/dj/dj-s-in-brussels`, `/fr/dj/mariage/bruxelles`, `/nl/dj/trouwfeest/brussel`, `/nl/dj/brussel`, `/en/dj/dj-wedding-party/dj-wedding-in-brussels` | **Highest priority.** Ranks top-3 in ALL of EN/FR/NL. Belgian-native, "Quality Label" program. Multilingual = matches client exactly. |
| **Mariages.net** | `/musique-mariage/dj-mariage/bruxelles-capitale`, `/musique-mariage/dj-mariage/belgique` | The Knot Worldwide. Owns FR wedding intent. Massive authority. |
| **Cueup** | `cueup.io/brussels/book-dj` (171 DJs), `/belgium/book-dj` (169), `/wedding/belgium/book-dj` (175) | Free artist profiles w/ mixes, images, testimonials. Ranks EN + corporate + party. Fast win. |
| **GigHeaven** | `/search/wedding-djs/belgium/brussels.html`, `/search/event-djs/belgium/brussels.html`, `/search/event-djs/belgium.html` | 831 event DJs Brussels; avg €600. Ranks on nearly every EN SERP. |
| **Eventigo** | `/artists/musique/dj/mariage/bruxelles`, `/artists-in/musique/dj/bruxelles` | Strong FR. |
| **Ring Twice** | `ringtwice.be/fr/dj-mariage/bruxelles`, `/fr/dj-mariage` | Belgian services marketplace. |
| **WEWED** | `wewed.be/prestataires/dj`, `wewed.be/prestataires` | Belgian, **"premium visibility, no commission"** — explicit vendor signup. |
| **Refevent** | `refevent.be/prestataires/dj/bruxelles` | BE event directory; ranks FR corporate. |
| **Mariage.be** | `/ambiance-mariage/sonorisation-mariage-et-disc-jockey-belgique-bruxelles.asp` | Old but ranking. |
| **Idées Mariage** | `ideesmariage.be` | Where Sono Cadillac is cited — mirror competitor citations. |
| **Linkaband** | `linkaband.com/animation-entreprise/dj` | FR corporate. |
| **Twine** | `twine.net/find/djs/be/brussels` | Freelance marketplace. |
| **allevents.in / Eventbrite** | `allevents.in/brussels/greek`, `eventbrite.com/d/belgium--brussel--10471/music--events/dj/` | **Greek-event listings — cheap wins for the Greek cluster.** |
| The Bash | `thebash.com/search/dj-brussels-il` | **US geo artifact. Not a real BE competitor.** |

**Strategic point:** the client cannot outrank House of Weddings or Mariages.net. He can **be the top-listed DJ inside them**. On the most directory-saturated SERPs (`dj mariage bruxelles`), directory listings are a faster route to the same customer than organic ranking — and they carry referral traffic and citation value in parallel.

---

## 4. SERP features & People Also Ask

**Caveat:** the search tool does not expose SERP feature blocks directly. The following is inferred from result composition and returned snippet content — **verify manually from a Belgian IP.**

**Local map pack** — near-certain on `dj mariage bruxelles`, `wedding dj brussels`, `dj entreprise bruxelles`. "DJ near me"-type intent triggers it reliably, and Prestige Sound's heavy promotion of its 150-review 4.9 Google rating implies it is competing in the pack. **This is likely the single most valuable SERP feature in this niche and it is invisible in the data above.**

**Featured snippets** — strongly implied on pricing queries. `combien coûte un DJ mariage Belgique` returned direct price extractions (€800–€1500; €500–€2000 range; €400 amateur vs €1800+ premium). Prestige Sound's `/fr/tarifs-dj-belgique-2026` is built to capture exactly this.

**Reviews/ratings** — visible in competitor title tags across the board (4.9★, 5★, "1677 reviews", "avg 5 out of 5").

**Video** — YouTube/Instagram presence is standard (Prestige Sound: YouTube + @djprestigesound). Not confirmed as blended video results.

**Questions surfacing in search data (probable PAA):**
- Combien coûte un DJ pour un mariage en Belgique ? / Quel est le prix moyen d'un DJ mariage ?
- Quelle est la différence entre un DJ amateur et un DJ professionnel ?
- Qu'est-ce qui est inclus dans le tarif d'un DJ ? (sono, éclairage, micro discours)
- Combien de temps à l'avance faut-il réserver un DJ ? (answer surfaced: ~1 year)
- Quel acompte faut-il verser ? (surfaced: 30% deposit, balance 7 days prior)
- Hoeveel kost een DJ voor een bruiloft?
- How much does a wedding DJ cost in Brussels? (surfaced: avg €629; range €41–€12,735)
- Does the DJ act as MC / handle speeches and first dance?
- How many songs should I put on my must-play list? (surfaced: 20–30 + a blacklist)

**Content implication:** pricing and logistics questions dominate. The client's blog should answer these **explicitly, with real numbers, in FR and NL first.** Vague "contact us for a quote" content will not compete against a competitor publishing €800/€1300 openly.

---

## 5. Realistic difficulty assessment

Assumes: brand-new domain, zero links, static site, competent execution, no paid links.

**Non-negotiable prerequisite:** a **Google Business Profile** for Brussels, verified, categorised "DJ" / "Disc-jockey", with steady review velocity. GBP is ~32% of local ranking signal and the map pack takes 44–58% of clicks. **Without GBP, none of the 3–6 month forecasts below hold.** This outranks every on-page task in priority.

| Keyword | Difficulty | Verdict |
|---|---|---|
| `dj grec bruxelles` (FR) | **Very low** | **3–6 mo, realistically 1–3.** No dedicated competitor exists; Google serves generic fallbacks. Should be #1. ⚠️ Resolve Sounds Greek Events first. |
| `greek dj brussels` (EN) | **Low** | **3–6 mo.** Only soundsgreekevents.be + weak intl. agencies. |
| Greek long-tail (`greek wedding dj belgium`, `dj βάπτισης Βρυξέλλες`, `ελληνικό γλέντι Βρυξέλλες`, `greek baptism dj brussels`) | **Very low** | **3–6 mo.** Near-zero competition. The EL pages have almost no rivals. **Highest ROI on the site.** |
| `bruiloft dj brussel` (NL) | **Low–medium** | **6–9 mo.** Genuinely soft — top 2 are EMD subdomains, thin SERP. A real multilingual NL page should beat them. **Best value/effort ratio of the mainstream terms.** |
| `dj entreprise bruxelles` (FR) | **Medium** | **6–12 mo** for top 5. Fragmented, 5 independents rank, weak directory grip. Starnight proves content wins here. Corporate buyers also convert on brand/referral, not rank alone. |
| `corporate event dj brussels` (EN) | **Medium** | **6–12 mo.** Lower FR volume but **no competitor has a dedicated corporate page** — pure gap. English favours the EU-institution/expat corporate audience, which is the client's best-margin segment. |
| `party dj brussels` (EN) | **Medium–high** | **12+ mo.** Marketplace-saturated (Cueup, GigHeaven, Twine), vague intent, poor conversion. **Deprioritise.** |
| `wedding dj brussels` (EN) | **High** | **12+ mo.** Prestige Sound holds 4/8 slots across two domains + directories take the rest. |
| `dj mariage bruxelles` (FR) | **Very high** | **12–18 mo+, and top 3 may be unrealistic.** 7 of 8 results are high-authority directories. **Highest volume, highest intent, hardest SERP.** Get listed in the directories instead of fighting them. |
| `restaurant dj brussels` (EN) | **Mismatched** | **Rankable but low-value — intent mismatch.** SERP returns *venues* (Romeo, Tope, Akai) for people seeking a night out, not restaurateurs hiring a DJ. **Recommend repositioning this page** toward B2B intent (`dj for restaurants/bars Brussels`, `resident dj hire horeca Brussels`) — cf. `driiing.be`, the only B2B result. Otherwise it will attract traffic that never converts. |

### Structural disadvantages to be honest with the client about

1. **Domain age & links.** Prestige Sound has ~15 yrs and two domains. Zero backlinks is the binding constraint — no amount of on-page work substitutes.
2. **Review moat.** 150+ Google reviews at 4.9 is a years-long asset feeding both organic CTR and the map pack. Reviews are ~16% of local signal. **Start collecting from day one.**
3. **Scale.** A 7-page site cannot out-cover a 60–100-page programmatic city×service×language matrix on head terms.

### Recommended sequencing

- **Now (weeks 1–4):** GBP verification + review engine. Claim Cueup, GigHeaven, House of Weddings, WEWED, Eventigo, Ring Twice, Refevent. Resolve the Sounds Greek Events relationship.
- **Months 1–3:** Own the Greek cluster (EL + FR + EN). Publish pricing-transparency content with real numbers in FR/NL — target the featured snippets competitors are winning.
- **Months 3–9:** Push NL `bruiloft dj brussel`, build the dedicated corporate pages (copy `dj-events.be`'s `/professionnels/` vs `/prives/` split), publish Starnight-style event recaps naming real Brussels venues and districts.
- **Months 9–18:** Only then contest `wedding dj brussels`. Treat `dj mariage bruxelles` as a directory-placement and paid channel, not an organic target.

**Strategic bottom line:** the client's defensible advantage is **Greek specialism + genuine 4-language capability**, not competing head-on with Prestige Sound. The Greek cluster and the Dutch-language gap are where a new domain can actually win this year.

---

## 6. Verification backlog

1. Manual google.be SERP check from a Belgian IP for all 7 keywords — capture map pack, PAA, featured snippets.
2. `view-source:` / crawl djprestigesound.be, djbruxelles.com, sonocadillac.be, dj-events.be — confirm schema, true page count, hreflang.
3. Backlink profile check (Ahrefs/Semrush) on djprestigesound.be.
4. **Clarify the DJ Orestis ↔ soundsgreekevents.be relationship — blocks the Greek strategy.**
5. Confirm djorestis.com indexation status in Search Console.
