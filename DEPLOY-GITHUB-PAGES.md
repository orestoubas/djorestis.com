# Going live: GitHub Pages + djorestis.com

The repo already contains everything Pages needs (`CNAME` with `djorestis.com`,
`.nojekyll`, and the finished site at the repo root). Two short steps remain,
both one-time.

## Step 1 — Enable GitHub Pages (2 minutes, in the browser)

1. Open the repository on GitHub → **Settings → Pages**.
2. Under **Build and deployment / Source**, choose **Deploy from a branch**.
3. Branch: select the branch that carries the site
   (currently `claude/djorestis-portfolio-discovery-ahqbkc`; after merging, switch this to `main`),
   folder **/ (root)** → **Save**.
4. Wait ~1 minute. Pages reads the `CNAME` file and configures the custom
   domain `djorestis.com` automatically. It will show "DNS check" warnings
   until Step 2 is done — that's expected.
5. Once DNS is set (Step 2), return here and tick **Enforce HTTPS**
   (GitHub issues a free certificate automatically).

From then on, **every push to the selected branch redeploys the site
automatically** within a minute or two — that's the "work on the website at
any moment" workflow you wanted.

## Step 2 — Point the domain at GitHub (5 minutes, at Papaki)

In the Papaki control panel for djorestis.com, open **DNS management
(Διαχείριση DNS)** and set these records:

| Type | Name/Host | Value |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | `<your-github-username>.github.io.` |

- Delete any existing A/AAAA records on `@` that point elsewhere (e.g. a
  Papaki parking page).
- Keep the MX records if/when you set up the info@djorestis.com mailbox at
  Papaki — mail and website are independent; only A/CNAME records move the site.
- Propagation typically takes minutes, occasionally a few hours.

## Checks after go-live

- https://djorestis.com loads with a padlock (after "Enforce HTTPS").
- https://www.djorestis.com redirects to the apex domain.
- Then do the SEO go-live list in `README.md` (Search Console + sitemap,
  Google Business Profile).

## The email address

`info@djorestis.com` needs the Papaki mailbox that comes with the domain/
hosting package: Papaki panel → Email → create `info@djorestis.com`, then
add the MX records they show you to the same DNS zone (they coexist with
the GitHub A records). Until that mailbox exists, mail to info@ bounces —
if you want, forward it to your Gmail from the Papaki panel.
