# Search engine setup — what to click, in order

Three short jobs. The Bing one matters more than most people realise, because
**ChatGPT Search retrieves through Bing's index** — a page Bing hasn't indexed
cannot be cited when someone asks an AI to recommend a DJ in Brussels.

---

## 1. Bing Webmaster Tools (10 minutes)

1. Go to **https://www.bing.com/webmasters** and sign in (a Microsoft account,
   or sign in with Google — that's the fast path).
2. Choose **Import from Google Search Console**. Since Search Console is already
   verified for djorestis.com, this imports the site and its verification in one
   step — no DNS record needed.
   *If the import fails*, add the site manually as `https://djorestis.com` and
   verify with the **CNAME** option, adding the record at Papaki exactly the way
   you added the Google verification record.
3. Once verified, open **Sitemaps** and submit:
   `https://djorestis.com/sitemap.xml`
4. Open **Settings → Crawl control** and leave it on the default (let Bing decide).
5. Optional but useful: **URL Inspection → Request indexing** on your three
   priority pages — the Greek page, the wedding page and the homepage.

**Why it's worth the ten minutes:** Bing crawls small new sites slowly on its own.
Submitting directly is the difference between being indexed in days versus months,
and Bing's index feeds ChatGPT and Copilot.

## 2. IndexNow (2 minutes, inside Bing Webmaster Tools)

IndexNow pings search engines the moment a page changes instead of waiting for a
crawl. Bing, Yandex, Seznam and Naver support it.

1. In Bing Webmaster Tools, open **IndexNow**.
2. Click **Generate API key**. Bing gives you a key and a file to host.
3. Send me the key — I'll add the key file to the site and wire the ping into the
   build, so every future change notifies Bing automatically.

Google does not use IndexNow. For Google, the sitemap plus normal crawling is the
supported route.

## 3. Apple Business Connect (10 minutes)

Apple unified its business listings into one platform in April 2026, covering
Apple Maps, Siri and Spotlight across 200+ countries. Free, and almost no
competitor in Brussels will have claimed theirs.

1. Go to **https://businessconnect.apple.com** and sign in with an Apple ID.
2. Register as a service-area business — same posture as Google: **no storefront**,
   address entered for verification and kept private, service areas set to Brussels
   and the Belgian cities you actually work in.
3. Add the logo (`marketing/social/avatar-1024.png`) and cover
   (`marketing/social/gbp-cover-1200x675.png`).

---

## Already done — no action needed

- **Google Search Console** verified, sitemap submitted, linked to Analytics.
- **Google Analytics 4** live behind a consent banner.
- **robots.txt** explicitly welcomes GPTBot, ClaudeBot, PerplexityBot,
  OAI-SearchBot, Google-Extended and Applebot-Extended. This business earns from
  bookings, not pageviews, so an AI recommending you is free advertising — there
  is no reason to block them.
- **sitemap.xml** carries accurate `lastmod` dates for blog posts.

## What to check monthly

In Search Console, the only two reports worth your time:

- **Performance → Queries** — what people actually typed to find you. This is real
  data, unlike keyword guesses, and should steer future content.
- **Pages → Not indexed** — anything unexpectedly excluded.

Ignore impressions as a success measure. The number that matters is enquiries.
