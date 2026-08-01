# AI Search (AEO/GEO) + Technical SEO Research — djorestis.com

Research date: **1 August 2026**
Scope: how to appear when a person asks an AI ("Who's a good Greek DJ in Brussels?") + current technical SEO requirements for a static, 4-language site on GitHub Pages.

**Evidence labelling used throughout:**
- **[CONFIRMED]** — stated in official Google/OpenAI/Anthropic/Microsoft documentation or an on-record statement by an employee of those companies.
- **[MEASURED]** — a published study with disclosed sample size and methodology (peer-reviewed or large-scale industry dataset). Correlation ≠ causation is flagged where relevant.
- **[CONSENSUS]** — widely repeated in the SEO/AEO practitioner community, plausible, but without a controlled study behind it.
- **[SPECULATIVE]** — asserted by vendors/agencies with no verifiable data. Treat as marketing.

---

## 0. Executive summary (read this first)

1. **The single biggest lever for "AI recommends a DJ in Brussels" is not on djorestis.com at all.** For local/service queries, AI assistants lean on Google Business Profile (Gemini/AI Mode is grounded in Google Maps), reviews, and third-party directories. **[MEASURED]** SOCi's 2026 Local Visibility Index found AI recommends only **1.2% of locations on ChatGPT and 7.4% on Perplexity**, vs **35.9%** visibility in Google's local 3-pack — AI local search is ~30× more selective than classic local search.
2. **Off-site brand signals correlate with AI citation far more strongly than anything on the page.** **[MEASURED]** Ahrefs (75,000 brands): YouTube mentions r=0.737, branded web mentions r=0.664, branded anchor text r=0.527, brand search volume r=0.392 — vs backlinks r=0.218.
3. **Schema markup is NOT a proven AI-citation lever.** **[MEASURED]** Ahrefs tracked 1,885 pages that added JSON-LD (Aug 2025–Mar 2026) against ~4,000 control pages and found **no major citation uplift** on AI Overviews, AI Mode or ChatGPT. Keep schema for Google rich results and machine comprehension — do not expect it to buy AI citations.
4. **FAQPage rich results are dead as of 7 May 2026.** The site has **28 FAQPage blocks**. Not risky, but no longer earns anything in Google.
5. **llms.txt is currently cargo cult for Google.** **[CONFIRMED]** Google explicitly says it is not required. **[MEASURED]** 97% of published llms.txt files receive zero AI-crawler requests.
6. **Bing indexing is the cheapest real win for ChatGPT visibility.** ChatGPT Search still retrieves via Bing's index. If Bing hasn't indexed a page, ChatGPT can't cite it.
7. **The site has effectively zero images (3 `<img>` tags, all favicon demos).** For a DJ — a visual, social-proof-driven business — this is the largest content gap for both humans and AI.

---

## 1. AEO / GEO — what is actually substantiated

### 1.1 What Google officially says

**[CONFIRMED]** Google Search Central, *AI features and your website*
https://developers.google.com/search/docs/appearance/ai-features
and *Google's guide to optimizing for generative AI features on Google Search* (published/updated June 2026)
https://developers.google.com/search/docs/fundamentals/ai-optimization-guide

Google's position, verbatim in substance:
- There are **no additional requirements** to appear in AI Overviews or AI Mode, and **no special optimizations** necessary.
- To be eligible as a supporting link in AI Overviews / AI Mode, a page must be **indexed, eligible to appear in Google Search, and eligible to be shown with a snippet**.
- **There is no special schema.org structured data needed** to appear in AI features. Google still recommends structured data as part of general SEO because it aids machine understanding and rich-result eligibility.
- Standard SEO fundamentals apply: crawlable, internally linked, helpful people-first content, meets technical requirements, complies with spam policies.
- **Snippet controls apply to AI features.** `nosnippet`, `max-snippet`, and `data-nosnippet` suppress a page's content from AI Overviews/AI Mode as well. This matters: *do not* add `nosnippet` anywhere.
- **[CONFIRMED]** Google added a note (15 June 2026) to the AI optimization guide stating **llms.txt files are not required for Google Search**.

> **Practical read:** Google's official answer to "how do I rank in AI Overviews" is "do normal SEO." Anything an agency sells beyond that is not Google-endorsed. That does not make it useless — it makes it unconfirmed.

### 1.2 The academic evidence

**[MEASURED]** *GEO: Generative Engine Optimization* — Aggarwal, Murahari, Rajpurohit, Kalyan, Narasimhan, Deshpande. KDD '24. https://arxiv.org/abs/2311.09735

Tested 9 content-level optimizations across a 10k-query benchmark. Findings:
- Best methods improved visibility **+41% (Position-Adjusted Word Count)** and **+28% (Subjective Impression)** vs baseline.
- The methods that worked: **adding quotations from credible sources, adding statistics, adding citations to authoritative sources, and using authoritative/fluent language**.
- Keyword stuffing — the classic SEO reflex — **did not help and sometimes hurt**.
- Effects are **domain-dependent**: quotations helped most in "People & Society / Explanation / History"; statistics helped most in "Law & Government".

> **Caveat for this site:** the study was run on informational queries against 2023–24 generative engines. A "recommend me a DJ" query is a *commercial local recommendation*, not an informational question. The quotation/statistic finding transfers well to the **blog**, poorly to service pages.

**[MEASURED]** Follow-up measurement work exists (e.g. arXiv 2604.25707, *From Citation Selection to Citation Absorption*) confirming that citation share is **highly volatile** — models re-generate answers from scratch each time and rebalance toward diversity and freshness, so a source visible on Monday can be absent Tuesday. Do not treat any single AI-visibility check as a stable measurement.

### 1.3 What predicts AI citation — industry data

**[MEASURED]** Ahrefs, study of 75,000 brands (2026). Correlation with AI Overview visibility:

| Signal | Correlation |
|---|---|
| YouTube mentions (titles, descriptions, transcripts) | 0.737 |
| Branded web mentions (unlinked included) | 0.664 |
| Branded anchor text | 0.527 |
| Brand search volume | 0.392 |
| Backlinks | 0.218 |

These are **correlations, not proven causation** — big brands have both more YouTube mentions and more AI citations. But the direction is consistent across vendors: **off-site brand presence beats on-page technical work** for AI visibility.

**[MEASURED]** Ahrefs, March 2026 (863,000 keywords, ~4M AI Overview URLs): only **38%** of AI Overview citations came from pages ranking in the organic top 10 — down from **76%** in July 2025. BrightEdge (12 Feb 2026) measured the same overlap at **~17%**. Semrush has reported figures as high as 84% using different methodology.
https://ahrefs.com/blog/ai-overview-citations-top-10/

> **Read:** methodologies disagree wildly, but every vendor agrees the overlap is **falling**. Ranking #1 in Google is no longer sufficient for AI citation, and conversely a page outside the top 10 can be cited.

### 1.4 What the practitioner consensus says (unconfirmed but low-cost)

**[CONSENSUS]** These are repeated by essentially every credible AEO source and are cheap/harmless to implement:
- **Answer-first structure.** Lead each section with a direct, self-contained answer, then support it. AI retrieval is *passage-level* — a passage is lifted out of context, so it must stand alone.
- **Descriptive H2/H3 phrased as the question a person would ask** ("How much does a wedding DJ cost in Belgium?" not "Pricing").
- **Self-contained passages of roughly 40–120 words** under each heading. (The frequently quoted "optimal passage length is 134–167 words" figure is **[SPECULATIVE]** — no primary source publishes this.)
- **Explicit entity naming.** Write "DJ Orestis, a Greek DJ based in Brussels, Belgium" rather than "we" / "I". Models resolve entities from text; pronouns don't resolve.
- **Concrete, extractable facts**: prices, durations, equipment lists, travel radius in km, languages spoken, number of events played. AI answers prefer specifics.
- **Featured-snippet capture.** Pages that previously won a featured snippet are cited in AI Overviews at roughly 2× the rate of non-snippet pages — widely reported, methodology not published, so **[CONSENSUS]** rather than [MEASURED].
- **Freshness.** Perplexity in particular weights recency heavily; content begins losing citation share after a couple of months.

**[SPECULATIVE]** — treat these as vendor marketing, no verifiable evidence:
- "Triple-schema stacking produces 1.8× more AI citations"
- "Sites with structured data are cited 3.2× more often"
- "61.7% citation rate for attribute-rich schema vs 41.6% for generic schema"
- Any claim that a specific word count, sentence length, or "semantic triple density" drives citations.
- "AI-specific content rewrites" and "micro-chunking" — Google's own guidance explicitly says these are not ranking factors for its generative features.

### 1.5 How each engine actually retrieves (relevant to strategy)

| Engine | Retrieval basis | Practical implication for djorestis.com |
|---|---|---|
| **Google AI Overviews / AI Mode** | Google's own index + query fan-out (one query decomposed into multiple sub-queries, passage-level retrieval via Gemini) | Normal Google indexing is the entry ticket. Cover sub-questions explicitly (price, languages, travel, equipment, genres) so fan-out sub-queries hit your pages. **[CONFIRMED]** query fan-out is Google's own described mechanism. |
| **Gemini / Ask Maps (local queries)** | Grounded directly in Google Maps / Google Business Profile | **The website is close to irrelevant here.** GBP completeness (services, description, photos, Q&A, posts, reviews) is what decides it. **[MEASURED]** SOCi found Gemini profile accuracy 100% vs 68% for ChatGPT/Perplexity, precisely because it is Maps-grounded. |
| **ChatGPT Search** | Bing index + OpenAI reranking; crawled by OAI-SearchBot / ChatGPT-User | **Bing indexing is the gate.** Get into Bing Webmaster Tools + IndexNow. |
| **Perplexity** | Own index (PerplexityBot) + partner search APIs; ~10–30 candidate pages reranked on relevance, authority, freshness | Allow PerplexityBot; publish/refresh dated content regularly. |
| **Claude** | Web search via Brave/partner APIs + Claude-SearchBot/ClaudeBot | Allow ClaudeBot and Claude-SearchBot; no other lever available. |

---

## 2. llms.txt — honest status as of August 2026

**Verdict: do not bother, or add it as a 10-minute no-cost experiment with zero expectations.**

- **[CONFIRMED]** Google: Gary Illyes stated (July 2025) that Google does not support llms.txt and has no plans to. John Mueller compared it to the discredited `keywords` meta tag. Google added a note to its AI optimization guide on **15 June 2026** stating llms.txt is **not required** for Google Search.
- **[CONFIRMED]** OpenAI's crawler documentation does not mention llms.txt; OpenAI directs site owners to **robots.txt**.
- **[CONFIRMED]** Anthropic's crawling guidance likewise points to robots.txt. (Anthropic publishes an llms.txt for its own developer docs — that is a *docs convenience for developers pasting context into an LLM*, not a crawler protocol Anthropic honours on third-party sites. This distinction is routinely misreported.)
- **[CONSENSUS]** Perplexity has indicated it may retrieve llms.txt to help prioritise page selection. This is the only meaningful adoption signal, and it is not documented as a guaranteed behaviour.
- **[MEASURED]** Server-log analysis reported by PPC Land: llms.txt adoption rose 8.8× year-on-year, but **97% of published llms.txt files receive zero AI-crawler requests**. GPTBot fetches them occasionally and rarely.
  https://ppc.land/llms-txt-adoption-rises-8-8x-but-97-of-files-get-zero-ai-requests/

**Recommendation for djorestis.com:** skip it. If added anyway, keep it to a genuine link index (it costs nothing and is not harmful), and never let it substitute for real page content. **robots.txt is the only file with broad, deliberate support from every major AI crawler operator.**

---

## 3. robots.txt and AI crawlers

### 3.1 Current site state

```
User-agent: *
Allow: /
Disallow: /build/

Sitemap: https://djorestis.com/sitemap.xml
```

**This is already correct for a business that wants to be recommended by AI.** The wildcard group permits every compliant AI crawler. Nothing needs to change functionally. An explicit allow-list is optional and mostly cosmetic/documentary.

### 3.2 The crawler landscape (2026)

**Training crawlers** — collect content to train/fine-tune models. Blocking these does *not* remove you from today's AI answers, but removes you from future model weights (i.e. from "what the model knows without searching").

| Bot | Operator |
|---|---|
| `GPTBot` | OpenAI |
| `ClaudeBot`, `anthropic-ai`, `Claude-Web` | Anthropic |
| `Google-Extended` | Google (Gemini training / grounding) |
| `CCBot` | Common Crawl (feeds many models) |
| `Applebot-Extended` | Apple |
| `Bytespider` | ByteDance — **known to ignore robots.txt** |
| `FacebookBot`, `Amazonbot`, `cohere-ai`, `Diffbot` | others |

**Retrieval / answer-time crawlers** — fetch live to build a cited answer. **Blocking these removes you from AI answers directly.**

| Bot | Operator |
|---|---|
| `OAI-SearchBot` | OpenAI (ChatGPT Search index) |
| `ChatGPT-User` | OpenAI (user-triggered browse) |
| `Claude-SearchBot`, `Claude-User` | Anthropic |
| `PerplexityBot`, `Perplexity-User` | Perplexity |
| `Google-Extended` | Google (also affects AI Overviews/Gemini grounding) |
| `Bingbot` | Microsoft — powers Bing, Copilot **and ChatGPT Search retrieval** |

Important nuance: **`Google-Extended` does not affect classic Google Search ranking**, only Gemini training and AI grounding. Blocking it is a way to opt out of Gemini while staying in Search — the opposite of what this client wants.

### 3.3 Strategic tradeoff for DJ Orestis

There is essentially **no tradeoff for this business**. The economic argument for blocking AI crawlers (publishers losing ad/subscription revenue to zero-click answers) does not apply: DJ Orestis is not monetising pageviews, he is monetising **bookings**. An AI answer that says "DJ Orestis in Brussels — Greek, electronic, Afro/Latin, plays weddings and corporate events, contact via djorestis.com" is *free advertising*, even with zero clicks.

**Recommendation: allow everything. Explicitly.** Making the allow-list explicit has two small benefits: (a) it is self-documenting and prevents a future contributor from adding a blanket block; (b) some operators' parsers prefer a named group. Suggested robots.txt:

```
# Search engines
User-agent: *
Allow: /
Disallow: /build/

# AI answer engines and assistants — explicitly welcome.
# This business wants to be recommended by AI. Do not add Disallow rules here.
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: Claude-User
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Perplexity-User
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Applebot-Extended
Allow: /
User-agent: CCBot
Allow: /

Sitemap: https://djorestis.com/sitemap.xml
```

Sources:
- https://platform.openai.com/docs/bots
- https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler
- https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers
- https://docs.perplexity.ai/guides/bots

Also note **[CONFIRMED]**: Perplexity has acknowledged that a **user-supplied URL** may be fetched even where robots.txt would block it (user-agent acting on behalf of a human, not a crawler). robots.txt is not an access-control mechanism.

---

## 4. Structured data in 2026

### 4.1 What changed — the FAQ deprecation

**[CONFIRMED]** Google added a deprecation notice to its FAQ structured data documentation on **7 May 2026**. Timeline:

| Date | Change |
|---|---|
| 7 May 2026 | FAQ rich results **stop appearing** in Google Search |
| June 2026 | FAQ search-appearance filter, Search Console rich-result report, and Rich Results Test support **removed** |
| August 2026 | Search Console **API** support for the FAQ rich result removed |

Google's own guidance: **you do not need to remove the markup** — "structured data that is not being used does not cause problems for Search."
https://www.searchenginejournal.com/google-drops-faq-rich-results-from-search/574429/
https://developers.google.com/search/docs/appearance/structured-data/faqpage

**[CONFIRMED]** HowTo rich results: deprecated on desktop September 2023, gone from all surfaces as of 2026.
**[CONFIRMED]** June 2025: Google retired seven further types — Book Actions, Course Info, Claim Review, Estimated Salary, Learning Video, Special Announcement, Vehicle Listing.
**[CONFIRMED]** January 2026: Practice Problem reporting removed.

### 4.2 Is FAQPage still worth having on this site?

The site has **28 FAQPage blocks** and **92 Question/Answer pairs**.

**Answer: keep the markup, but stop treating it as an SEO asset — and make sure the FAQ content is visible on the page.**

- **[CONFIRMED]** Zero Google rich-result value as of May 2026. No ranking penalty either.
- **[CONFIRMED]** Bing still supports FAQ rich results and continues to parse FAQPage.
- **[CONSENSUS]** AI crawlers parse JSON-LD, and Q&A-shaped content maps naturally onto how answer engines retrieve. This is plausible and free, but see §4.4 — it is **not** proven to lift AI citations.
- **Risk to check:** Google's structured data policy requires marked-up content to be **visible to users on the page**. If any FAQPage block on this site describes Q&As that are not rendered in the HTML body, that is a spam-policy violation. This should be verified page by page.

**Real value of the FAQ content is now in the visible copy, not the markup** — a well-written on-page Q&A block is exactly the answer-first, self-contained passage structure AI retrieval favours.

### 4.3 What still produces rich results in Google (2026)

Relevant to a service business:

| Type | Status | Applicable here? |
|---|---|---|
| `LocalBusiness` / `Organization` | **Active** — feeds knowledge panel, entity understanding. Highest-leverage type in 2026. | Yes — already present, needs enrichment |
| `BreadcrumbList` | **Active** — breadcrumb trail in results | **Yes — currently missing entirely** |
| `Article` / `BlogPosting` | **Active** — Top Stories, article appearance, date display | Yes — present, missing `dateModified` |
| `Event` | **Active** — event rich results | Yes — for the Past events / upcoming gigs page |
| `VideoObject` | **Active** — video rich results, key moments | Yes, if video is added |
| `Review` / `AggregateRating` | **Active but heavily restricted** — see §4.5 | **Careful — see below** |
| `Service` | Not a rich-result type; useful for machine comprehension only | Present (28×), harmless, keep |
| `Person` | Not a rich-result type; strong entity/E-E-A-T signal | Present (19×), keep and enrich |
| `FAQPage` | **Deprecated for rich results** (May 2026) | Present (28×), keep but devalue |
| `HowTo` | **Deprecated** | Not present — do not add |

**Currently missing and worth adding: `BreadcrumbList`, `WebSite` (with `inLanguage`), `Organization` alongside `LocalBusiness`, `Event`, `ImageObject`, `Offer`/price range on services.**

### 4.4 Does schema help AI citations? The honest answer

**[MEASURED]** Ahrefs, *"We Tracked 1,885 Pages Adding Schema. AI Citations Barely Moved."* — 1,885 pages that added JSON-LD between August 2025 and March 2026, matched against ~4,000 control pages, measured across Google AI Overviews, AI Mode and ChatGPT. Result: **no major citation uplift on any platform.**
https://ahrefs.com/blog/schema-ai-citations/

**[CONFIRMED]** Google: "There's no special structured data you need to add to appear in AI features."

Counter-claims of 1.8×/3.2×/61.7% uplift are **[SPECULATIVE]** — they come from vendors selling schema tooling, with no disclosed methodology or control group.

> **Bottom line: implement schema for Google rich results, entity disambiguation and Bing — all real, documented benefits. Do not budget it as an AI-visibility tactic.**

### 4.5 Review / AggregateRating — rules and penalty triggers

This is the **highest-risk area** for a service business, and DJ Orestis has a strong temptation to add star ratings.

**[CONFIRMED]** Google's review snippet documentation (https://developers.google.com/search/docs/appearance/structured-data/review-snippet):

1. **Self-serving reviews are ineligible.** Since Google's September 2019 policy change, if the entity being reviewed **controls the reviews about itself**, pages using `LocalBusiness` or `Organization` structured data are **not eligible** for the review star feature. Marking up testimonials you collected and published yourself, on your own site, under your own `LocalBusiness` schema, is exactly the disallowed case.
   https://developers.google.com/search/blog/2019/09/making-review-rich-results-more-helpful
2. **Visibility requirement.** If a page uses `AggregateRating`, users must be able to **see that aggregate rating** on the page. If individual reviews are marked up, the review text and rating must be visible.
3. **[CONFIRMED — new, 24 July 2026]** Google added a guideline banning **undisclosed incentivized reviews**. Reviews written in exchange for money, discounts, vouchers or free products, without clear and prominent disclosure of the incentive, violate the guidelines.
   https://ppc.land/google-bans-undisclosed-incentivized-reviews-sites-face-manual-action/
4. **Penalty mechanism:** a **manual action** that causes structured data on the affected page to be **ignored**, while the page itself remains in search results. It is a feature-level, not site-level, punishment — but it can be extended.

**Recommendation for djorestis.com:**
- **Do NOT add `AggregateRating` to the `LocalBusiness` schema based on self-collected testimonials.** This is the single most likely way to earn a manual action here.
- **Do** display real testimonials as visible on-page content (great for humans, great for AI extraction, zero risk) — just without `Review`/`AggregateRating` markup on the business entity.
- **Do** drive reviews to **Google Business Profile**, where they carry actual weight for local ranking *and* for AI local recommendation. **[MEASURED]** SOCi: AI platforms use reviews as a **confidence threshold, not a ranking gradient** — ChatGPT-recommended locations average **4.3 stars**; locations near 3.4 stars with review-response rates under 5% are effectively invisible in AI local recommendations.
- Third-party review platforms (Google, Facebook, wedding directories) are where review schema legitimately lives — on their domain, not yours.

---

## 5. Core Web Vitals 2026

### 5.1 Current metrics and thresholds — [CONFIRMED]

https://web.dev/articles/vitals · https://developers.google.com/search/docs/appearance/core-web-vitals

| Metric | Measures | Good | Needs improvement | Poor |
|---|---|---|---|---|
| **LCP** (Largest Contentful Paint) | Loading | ≤ 2.5 s | 2.5–4.0 s | > 4.0 s |
| **INP** (Interaction to Next Paint) | Responsiveness | ≤ 200 ms | 200–500 ms | > 500 ms |
| **CLS** (Cumulative Layout Shift) | Visual stability | ≤ 0.1 | 0.1–0.25 | > 0.25 |

- **[CONFIRMED] INP replaced FID as a Core Web Vital on 12 March 2024.** FID was fully retired from Google tooling in September 2024. (Note: several 2026 blog posts state "INP replaced FID in March 2026" — this is **wrong**; it was 2024.)
- **[CONFIRMED]** Scoring is at the **75th percentile of real-user (CrUX) data over a rolling 28-day window**, per URL, split desktop/mobile. Lab scores (Lighthouse) do not determine the assessment.
- Supporting non-Core metrics worth watching: TTFB, FCP, and (for LCP debugging) the LCP sub-part breakdown — TTFB / resource load delay / resource load duration / element render delay.

### 5.2 How much it actually matters — [CONFIRMED, with nuance]

- **[CONFIRMED]** Core Web Vitals are a real ranking signal, folded into Google's core ranking systems as part of page experience.
- **[CONFIRMED]** John Mueller, on record: Core Web Vitals are "**not giant factors in ranking**"; "It is a ranking factor, and it's more than a tie-breaker, but it also doesn't replace relevance." He has said you are unlikely to see a big ranking drop from CWV issues alone.
  https://www.searchenginejournal.com/googles-mueller-dismisses-core-web-vitals-impact-on-rankings/530715/
- **[CONSENSUS]** CWV behaves as a *limiting* factor: it rarely lifts a page on its own, but poor CWV compounds other weaknesses.
- **[MEASURED]** ~43% of sites still fail the 200 ms INP threshold in 2026 — INP is the most commonly failed vital.

### 5.3 What this static site should check

A static, JS-free, self-hosted-fonts site on a CDN should pass all three trivially. Specific checks:

- **CrUX data may not exist** for a low-traffic site. If Search Console's Core Web Vitals report says "not enough data," that is normal and **not a problem** — Google falls back to origin-level or no signal.
- **LCP**: fonts are preloaded (good). Confirm `font-display: swap` in `/assets/css/fonts.css`. The current LCP element is likely the H1 text — fine. **This changes the moment real photos are added**: the hero image will become LCP.
- **CLS**: every future `<img>` **must** have explicit `width` and `height` attributes (or `aspect-ratio` in CSS). Currently only 3 img tags exist and they do have dimensions — but the pattern must be enforced when photos land.
- **INP**: near-zero risk. Only JS on the site is the nav toggle and consent-gated GA4. Keep GA4 loading `async`/deferred and behind consent (already the case).
- Measure with PageSpeed Insights (field + lab) and the `web-vitals` JS library if field data is ever needed.

---

## 6. Technical checklist — static site on GitHub Pages

### 6.1 Findings on the current site

| Item | State | Verdict |
|---|---|---|
| `robots.txt` | Allow all, disallow `/build/`, sitemap declared | **Good** |
| `sitemap.xml` | 76 URLs, no `lastmod`, no hreflang, no images | **Improve** — see 6.3 |
| `404.html` | Exists, `noindex`, styled | **Good.** GitHub Pages serves it with a true HTTP 404 |
| Canonicals | Absolute, HTTPS, trailing slash, self-referencing | **Good** |
| hreflang | 5 links (en/fr/nl/el/x-default) on every page | **Good** — see §7 |
| `.nojekyll` | Present | **Good** — required so `/assets/`-style paths and any underscore dirs aren't mangled |
| `CNAME` | Present | Good |
| **`.htaccess`** | Present, Apache-only, references "Papaki shared hosting" | **OBSOLETE — dead file on GitHub Pages.** Does nothing. See §8 |
| `/build/` directory | Deployed to the live site, blocked only by robots.txt | **Risky** — see §8 |
| Images | **3 `<img>` tags total, all favicon demos.** No WebP/AVIF. No `loading`, no `fetchpriority` | **Largest content gap** |
| `dateModified` on Articles | **0 of 19** | **Missing** — freshness signal |
| `mainEntityOfPage` on Articles | 0 of 19 | Minor gap |
| `BreadcrumbList` | **Absent site-wide** | **Missing** — active rich result |
| `Organization` / `WebSite` schema | Absent (only `LocalBusiness`) | Gap for entity resolution |
| `Review` / `AggregateRating` | **Absent** | **Good — keep it that way** (§4.5) |
| Bing Webmaster Tools / IndexNow | Not set up (no key file present) | **Missing — highest-ROI quick win** |

### 6.2 GitHub Pages specifics commonly missed

- **[CONFIRMED]** GitHub Pages **cannot do server-side redirects.** No `.htaccess`, no 301s. The `.htaccess` in this repo is inert. www→apex and HTTP→HTTPS are handled by GitHub Pages itself **provided DNS is configured correctly** (apex A/AAAA records to GitHub's IPs **and** a `www` CNAME to `<user>.github.io`) and **"Enforce HTTPS" is enabled** in repository settings. Verify both.
- **Trailing slashes:** GitHub Pages redirects `/path` → `/path/`. All internal links and canonicals on this site already use trailing slashes — **keep that invariant absolutely consistent**, because a `/path` link costs an extra redirect hop and, historically, a documented GitHub Pages bug has downgraded no-trailing-slash HTTPS links to HTTP.
  https://github.com/slorber/trailing-slash-guide
- **404 status code:** GitHub Pages serves the root `404.html` with a genuine HTTP 404 for a custom domain. Correct as-is. **Do not** convert it to a JS redirect-to-index (the SPA workaround) — that turns every 404 into a soft-404.
- **Caching headers cannot be controlled** on GitHub Pages. Not fixable; not a real problem for a small site. If it ever matters, put Cloudflare in front.
- **The `/build/` directory is publicly served.** `Disallow: /build/` in robots.txt stops compliant crawlers but **does not stop non-compliant AI crawlers, nor humans**. Robots.txt disallow also does not prevent indexing of URLs discovered elsewhere. Better: don't deploy `/build/` at all (build in CI, publish only the output), or at minimum ensure nothing sensitive is in it.

### 6.3 Sitemap best practice

**[CONFIRMED]** Google:
- `<priority>` and `<changefreq>` are **ignored**. Do not add them.
- `<lastmod>` **is used** by Google (Mueller and Illyes both on record) — **but only if it is accurate**. If every URL shows today's date, Google ignores `lastmod` for the whole site. **Add real `lastmod` values or none at all.**
- Limits: 50,000 URLs / 50 MB per file. This site (76 URLs) is nowhere near.
- Never include noindex pages, redirects, 4xx URLs, or non-canonical variants.

**hreflang in the sitemap vs `<link>` tags:** **[CONFIRMED]** Google accepts hreflang via HTML `<link>` tags, HTTP headers, **or** sitemap `xhtml:link` entries — all three are equally valid, and **you should use only one method**. This site already uses `<link>` tags correctly on all four language versions. **Do not duplicate hreflang into the sitemap** — that's the classic way to introduce a conflict. Sitemap hreflang is only worth it at scale (thousands of URLs) where editing head tags is expensive.

**Image sitemaps:** **[CONFIRMED]** still supported and useful for discovering images that regular crawling might miss (CSS backgrounds, lazy-loaded, JS-injected). Currently pointless — the site has no images. **Worth adding once real photography is published**, especially for a DJ where image search is a genuine discovery channel.

**Recommended sitemap change:** add accurate `<lastmod>` per URL, generated from the source file's real modification date by the build script.

### 6.4 IndexNow + Bing Webmaster Tools — the highest-ROI quick win

**Why it matters:** **[CONFIRMED]** ChatGPT Search retrieves web results via **Bing's index**. A page Bing has not indexed cannot appear in a ChatGPT answer, regardless of how good it is. Bing crawls small sites far less aggressively than Google, so new blog posts can wait weeks. IndexNow pushes URLs to Bing (and Yandex, Seznam, Naver) within seconds.
https://www.indexnow.org/ · https://www.bing.com/webmasters

**[MEASURED]** IndexNow processes >5 billion URL submissions/day across 80M+ sites (indexnow.org, early 2026).

**Implementation on GitHub Pages — note the security wrinkle:**
- The default authentication is a key file at `https://djorestis.com/<key>.txt` containing the key.
- If the repo is **public**, committing the key file exposes the key. This is a low-severity issue (worst case someone else submits your URLs), but the clean pattern is to store the key in **GitHub Secrets** and write the key file during the deploy workflow, then POST the URL list to the IndexNow API from the same workflow.
- Ready-made action: https://github.com/bojieyang/indexnow-action
- Also do the manual, zero-effort version first: **verify the site in Bing Webmaster Tools and submit sitemap.xml.** Bing WMT can import verification and sitemaps directly from Google Search Console.

### 6.5 Images (when they get added)

**[CONFIRMED / well-documented]**
- **WebP is the safe default** in 2026: ~97% browser support, 25–34% smaller than JPEG, fast decode (~14 ms for 1200×800).
- **AVIF** is ~50% smaller than JPEG and 20–30% smaller than WebP, but ~93% support and slower decode (~35 ms). Use via `<picture>` with WebP/JPEG fallback for hero images only.
- **Never lazy-load the LCP image.** Measured impact: lazy-loading the LCP image moved the 75th-percentile LCP from 364 ms to 720 ms and dropped "good" pages from 79% to 52%.
- Use **`fetchpriority="high"` on exactly one image per page** (the hero/LCP image). Google's own tests cut LCP 2.6 s → 1.9 s from that single attribute.
- Eager-load the first 2–3 above-the-fold images; `loading="lazy"` for everything below the fold.
- **Always set explicit `width` and `height`** on every `<img>` to prevent CLS.
- Descriptive `alt` text — matters for accessibility, image search, and is one of the few image signals text-based AI crawlers can read.

Recommended pattern:
```html
<picture>
  <source srcset="/assets/img/hero.avif" type="image/avif">
  <source srcset="/assets/img/hero.webp" type="image/webp">
  <img src="/assets/img/hero.jpg" width="1600" height="900"
       fetchpriority="high" decoding="async"
       alt="DJ Orestis mixing at a Greek wedding reception in Brussels">
</picture>
```

---

## 7. hreflang for a Belgium-targeted multilingual site

### 7.1 The evidence-based answer

**The current implementation is correct. Do not change it to `fr-BE` / `nl-BE`.**

Reasoning, grounded in Google's documentation (https://developers.google.com/search/docs/specialty/international/localized-versions):

1. **`hreflang` values are ISO 639-1 language, optionally plus ISO 3166-1 Alpha-2 region.** The **language is mandatory; the region is optional and purely additive**. `hreflang="fr"` means "French speakers anywhere." `hreflang="fr-BE"` means "French speakers **in Belgium only**."
2. **Country codes narrow, they never widen.** Using `fr-BE` would mean this site's French page is **not** offered to a French speaker searching from France, Luxembourg, Switzerland, or a French-speaking expat's browser set to France. Given DJ Orestis explicitly serves **Belgium, Netherlands, France, Germany, UK and Greece** (per his own `areaServed`), region-locking to BE is actively counterproductive.
3. **Region codes are only justified when you have genuinely different content per region** — different prices, different currency, different legal terms, different phone numbers. This site serves the *same* French content to everyone. **[CONFIRMED]** Google's guidance is that if you have one standardized French version serving multiple regions, designate `hreflang="fr"` without a country.
4. **The multi-language-one-country case (Belgium) is handled by language codes, not region codes.** Belgium has three official languages; a Belgian user's browser/Google locale already signals whether they want FR or NL. `fr` and `nl` resolve that correctly. `fr-BE`/`nl-BE` adds nothing and subtracts reach.
5. **Do not use a country code by itself.** `hreflang="BE"` is invalid — **[CONFIRMED]** Google does not derive language from country.

### 7.2 x-default — yes, keep it

**[CONFIRMED]** `x-default` specifies the fallback for users whose language matches none of your versions. The site points `x-default` at the English root (`https://djorestis.com/`). This is the correct choice: English is the widest-reach fallback and is already the root URL.

A common alternative is pointing `x-default` at a language-selector page. **Do not do that here** — a redirect/selector page is worse UX and wastes the strongest URL on the domain.

### 7.3 Return-tag correctness — the thing that actually breaks

**[CONFIRMED]** hreflang is **bidirectional**: if page A declares B as an alternate, B must declare A. Every page must also declare **itself** (self-referencing hreflang). **A single broken link in a cluster causes Google to ignore the entire cluster.**

**[CONSENSUS]** ~75% of hreflang implementations in the wild contain errors — missing return tags, broken URLs, wrong ISO codes.

**Verified on this site:** all four homepage variants (`/`, `/fr/`, `/nl/`, `/el/`) emit the identical 5-link block including self-reference and `x-default`. This is correct.

**The thing to actually verify: the deeper pages.** Every service page must point at its own translated counterparts, not at the homepages. E.g. `/wedding-dj-brussels/` must declare:
```html
<link rel="alternate" hreflang="en" href="https://djorestis.com/wedding-dj-brussels/">
<link rel="alternate" hreflang="fr" href="https://djorestis.com/fr/dj-mariage-bruxelles/">
<link rel="alternate" hreflang="nl" href="https://djorestis.com/nl/bruiloft-dj-brussel/">
<link rel="alternate" hreflang="el" href="https://djorestis.com/el/[greek-slug]/">
<link rel="alternate" hreflang="x-default" href="https://djorestis.com/wedding-dj-brussels/">
```
**Audit this per-page.** Localised slugs (which this site correctly uses) are exactly where hreflang clusters break.

Second thing to verify: **do all 19 blog posts exist in all 4 languages?** If not, they must either have **no hreflang at all** or hreflang pointing only to the versions that genuinely exist. Pointing a Greek blog hreflang at a non-existent URL breaks the cluster. (The sitemap shows the blog URLs at the English root only — check whether `/fr/blog/` etc. exist.)

### 7.4 Other hreflang rules that apply

- **`hreflang` and `canonical` must agree.** Each language version must be its own canonical. **Verified correct** — `/el/` canonicals to `/el/`. A frequent fatal error is canonicalising all language versions to the English one, which nullifies hreflang entirely.
- **Use absolute URLs including protocol.** Correct on this site.
- **`hreflang` is a signal, not a directive** — Google may still choose differently.
- **`hreflang` does not help ranking**; it only ensures the *right version* is served to the right user. It solves duplicate-content ambiguity between languages.
- **`<html lang>` attribute** must match. `/el/` should be `<html lang="el">` — **verify**, since the English template uses `lang="en"`.

---

## 8. Currently on the site: obsolete or risky

| Item | Issue | Severity | Action |
|---|---|---|---|
| **`.htaccess`** | Apache config for "Papaki shared hosting". GitHub Pages ignores it entirely. It creates the false impression that www→non-www redirects, HTTPS forcing, `/build/` blocking, and cache headers are handled. **None of them are.** | **Medium** — dangerous because it hides a gap | Delete it, or keep with a header comment `# INERT on GitHub Pages — kept for reference only`. Then verify DNS (apex A/AAAA + www CNAME) and "Enforce HTTPS" in repo settings actually cover the redirects. |
| **28× `FAQPage` markup** | Rich results deprecated 7 May 2026. Zero Google value. | **Low** — no penalty | Keep (Bing + machine comprehension), but stop counting it as an SEO asset. **Verify every marked-up Q&A is visibly rendered** — invisible marked-up content is a spam-policy violation. |
| **`/build/` deployed live** | Generator sources are publicly reachable. Robots.txt disallow doesn't bind non-compliant crawlers or prevent indexing of externally-discovered URLs. | **Low–Medium** | Exclude from deploy (build in CI, publish output only). |
| **No `dateModified` on any of 19 Articles** | Freshness is the strongest distinctive citation factor on Perplexity, and Google uses it for article appearance. All 19 posts carry only 2024 `datePublished`, so they read as 1–2 years stale. | **Medium** | Add `dateModified`; genuinely refresh the highest-value posts and update the date honestly. Never fake it. |
| **No `lastmod` in sitemap** | Google uses `lastmod` when accurate. 76 URLs with none. | **Low–Medium** | Generate from real file mtimes in the build. Don't stamp everything with today's date. |
| **No `BreadcrumbList` anywhere** | Active, supported rich result. Free. | **Low–Medium** | Add to all service/blog pages. |
| **`LocalBusiness` lacks `telephone`, `geo`, `openingHours`, `areaServed` as structured objects, `founder`, `knowsAbout`, real `sameAs`** | `sameAs` currently lists only one URL (`soundsgreekevents.be`). Entity resolution — the thing that actually determines whether an AI knows "DJ Orestis" is a real, identifiable entity — depends on `sameAs` pointing at verifiable external profiles. | **Medium–High** for AI | Expand `sameAs` to Instagram, Facebook, YouTube, SoundCloud/Mixcloud, LinkedIn, Google Business Profile, Wikidata (if created). Add `Organization` and `WebSite` schema. |
| **Effectively zero images (3 favicon demos)** | For a DJ, this is a severe credibility and engagement gap; also removes an entire discovery channel (image search, social preview quality) and gives AI nothing visual to reference. | **High** | Add real event photography with descriptive alt text, WebP + AVIF, explicit dimensions, `fetchpriority="high"` on hero only. |
| **`priceRange: "$$"`** | Uses US dollar convention on a Belgian site. Harmless but sloppy; Google accepts it. | **Very Low** | Consider `"€€"` or an explicit range. |
| **No Bing Webmaster Tools / IndexNow** | Directly blocks ChatGPT visibility. | **High** | Set up. |
| **`x-default` → English root** | Correct. | — | No change |
| **`fr` / `nl` / `el` language-only hreflang** | Correct. Do **not** "improve" to `fr-BE`/`nl-BE`. | — | No change |
| **No `Review`/`AggregateRating`** | Correct and safe. | — | **Keep it that way.** Adding self-collected star ratings under `LocalBusiness` is the fastest route to a manual action. |

---

## 9. The uncomfortable strategic conclusion

For the query this project actually cares about — *"who's a good Greek DJ for a wedding in Brussels?"* asked to ChatGPT/Gemini/Perplexity — the website is **necessary but not sufficient**, and the technical work above is table stakes, not the differentiator.

**[MEASURED]** The evidence says the ranking of levers is:

1. **Google Business Profile** — completeness, categories, service list, photos, Q&A, posts, and above all **review volume + rating + response rate**. Gemini/Ask Maps is grounded directly in Maps; **[MEASURED]** profile accuracy on Gemini is 100% vs 68% on ChatGPT/Perplexity for exactly that reason. **[CONFIRMED]** a DJ qualifies as a *service-area business*: leave the address field blank, define service areas, expect video verification.
2. **Third-party presence** — Belgian/EU wedding and event directories, venue partner pages, Greek-community organisation pages. These are what AI cites when it doesn't cite the brand site, and **[MEASURED]** AI local answers route heavily to directories and publishers rather than independent business sites.
3. **Off-site brand mentions** — **[MEASURED]** YouTube mentions correlate 0.737 with AI Overview visibility, branded web mentions 0.664, vs backlinks 0.218. For a DJ, **YouTube is a structurally under-exploited channel**: set videos, event recaps, venue name-drops in titles/descriptions/transcripts. This is the single highest-correlation signal in the Ahrefs dataset and it costs nothing but time.
4. **Being in Bing's index** — the gate for ChatGPT.
5. **On-page AEO structure** — answer-first passages, question-shaped headings, concrete extractable facts (prices in €, travel radius in km, languages, genres, setup specs).
6. **Schema** — real value for Google rich results and entity resolution; **[MEASURED]** no proven AI-citation uplift.
7. **Core Web Vitals** — **[CONFIRMED]** real but small; already effectively solved by being a static site.

---

## 10. Sources

**Official documentation (Google / OpenAI / Anthropic / Microsoft)**
- Google, AI features and your website — https://developers.google.com/search/docs/appearance/ai-features
- Google, Guide to optimizing for generative AI features (June 2026, incl. llms.txt note added 15 June 2026) — https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Google, FAQPage structured data (deprecation notice added 7 May 2026) — https://developers.google.com/search/docs/appearance/structured-data/faqpage
- Google, Review snippet structured data — https://developers.google.com/search/docs/appearance/structured-data/review-snippet
- Google, Making Review Rich Results more helpful (Sept 2019, self-serving reviews rule) — https://developers.google.com/search/blog/2019/09/making-review-rich-results-more-helpful
- Google, Localized versions / hreflang — https://developers.google.com/search/docs/specialty/international/localized-versions
- Google, Core Web Vitals — https://developers.google.com/search/docs/appearance/core-web-vitals · https://web.dev/articles/vitals
- Google, Overview of Google crawlers (Google-Extended) — https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers
- OpenAI, Bots — https://platform.openai.com/docs/bots
- Anthropic, crawler & site-owner guidance — https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler
- Perplexity, bots — https://docs.perplexity.ai/guides/bots
- IndexNow — https://www.indexnow.org/ · https://www.indexnow.org/faq
- Bing Webmaster Tools — https://www.bing.com/webmasters
- Google Business Profile, service-area businesses — https://support.google.com/business/answer/9157481
- Google Business Profile, eligibility — https://support.google.com/business/answer/13763036

**Academic**
- Aggarwal et al., *GEO: Generative Engine Optimization*, KDD '24 — https://arxiv.org/abs/2311.09735
- *From Citation Selection to Citation Absorption: A Measurement Framework for GEO Across AI Search Platforms* — https://arxiv.org/pdf/2604.25707

**Industry studies with disclosed methodology**
- Ahrefs, *We Tracked 1,885 Pages Adding Schema. AI Citations Barely Moved.* (Aug 2025–Mar 2026) — https://ahrefs.com/blog/schema-ai-citations/
- Ahrefs, *38% of AI Overview Citations Pull From The Top 10* (Mar 2026; 863k keywords, 4M URLs) — https://ahrefs.com/blog/ai-overview-citations-top-10/
- Ahrefs, brand signals vs AI Overview visibility (75,000 brands) — https://ahrefs.com/blog/search-rankings-ai-citations
- SOCi 2026 Local Visibility Index — https://soci.ai/insights/lvi/ · https://www.soci.ai/blog/how-to-rank-in-chatgpt-perplexity-and-google-ai-overview/ · https://www.prnewswire.com/news-releases/in-ai-driven-discovery-few-brands-are-chosen-most-disappear-302672281.html
- PPC Land, llms.txt adoption 8.8× / 97% zero requests — https://ppc.land/llms-txt-adoption-rises-8-8x-but-97-of-files-get-zero-ai-requests/
- PPC Land, Google bans undisclosed incentivized reviews (guideline added 24 July 2026) — https://ppc.land/google-bans-undisclosed-incentivized-reviews-sites-face-manual-action/

**Trade press / practitioner reporting**
- Search Engine Journal, Google Drops FAQ Rich Results From Search — https://www.searchenginejournal.com/google-drops-faq-rich-results-from-search/574429/
- Search Engine Journal, Google AI Overview Citations From Top-Ranking Pages Drop Sharply — https://www.searchenginejournal.com/google-ai-overview-citations-from-top-ranking-pages-drop-sharply/568637/
- Search Engine Journal, Mueller on Core Web Vitals impact — https://www.searchenginejournal.com/googles-mueller-dismisses-core-web-vitals-impact-on-rankings/530715/
- Search Engine Roundtable, Google unlikely to cause big ranking drop over CWV — https://www.seroundtable.com/google-ranking-drop-core-web-vitals-38297.html
- BrightLocal, Can local businesses use review schema? — https://www.brightlocal.com/learn/review-schema/
- Trailing slash guide (static hosting) — https://github.com/slorber/trailing-slash-guide
- IndexNow GitHub Action — https://github.com/bojieyang/indexnow-action
- John Mueller, automating IndexNow on static sites with GitHub Actions — https://johnmu.com/2025-used-to/
- CLICKTRUST, international SEO in bilingual countries (Belgium) — https://clicktrust.be/blog/seo/how-to-get-international-seo-right-in-bilingual-countries/
