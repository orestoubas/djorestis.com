# Getting great photos & videos for DJORESTIS.com

The site currently shows elegant "coming soon" placeholders. Here's the fastest route to
replacing them with material that sells you.

## 1. The honest advice first

For a business site targeting corporate clients, **real photos of you performing beat
anything AI-generated**. Clients will meet you in person; the photos must be you.
AI is excellent for *improving* real photos — not for inventing them.

## 2. Fastest wins (this month)

- **Papillon Schuman residency** — ask a photographer friend (or hire a student
  photographer, ±€100–150 for an hour) to shoot one of your regular nights. One good
  session covers the whole site: booth close-ups, crowd shots, wide room shots.
- **Your next wedding/corporate gig** — ask the event's photographer for 5–10 frames of
  you at work. Most happily share in exchange for a credit; couples almost always say yes.
- **Phone footage you already have** — old stories/reels often contain usable frames
  (see enhancement tools below).

What to capture: (a) you at the decks, engaged, good light; (b) the crowd from behind
the booth; (c) detail shots — hands on the mixer, lighting rig; (d) one clean
half-portrait for the About page.

## 3. AI tools that actually help

| Task | Tool |
|---|---|
| Sharpen/denoise phone photos from dark venues | **Topaz Photo AI** (paid, best in class) or **Lightroom** "Enhance / Denoise" |
| Upscale low-resolution frames from video | Topaz Photo AI / **Magnific** / Lightroom Super Resolution |
| Remove distracting objects or people from a shot | **Photoshop Generative Fill** or **Cleanup.pictures** (free, browser) |
| Cut yourself out for posters/socials | **remove.bg** or Canva background remover |
| Quick edits, socials, consistency | **Canva Pro** (also applies your gold/dark brand colors) |
| Color-grade video clips into aftermovie snippets | **CapCut** (free) or DaVinci Resolve (free) |

Recommended flow for existing dark venue shots: Lightroom Denoise → crop → slight warm
grade toward the site's gold/dark palette → export at 1600px wide, JPEG quality 80.

## 4. Video placeholders

The Music page has two 16:9 slots. Best fillers, in order of impact:
1. A 60–90s **aftermovie** cut from phone clips of your best nights (CapCut can do this in an evening).
2. A simple **one-take set recording** at Papillon Schuman (static tripod + your mixer's recording = plenty).
3. Embeds: once on YouTube, replace the placeholder `<div>`s in `build/content_en.py`
   (Music page) with the YouTube `<iframe>` embed code and regenerate.

## 5. Image specs for the site

- Split-section photos (home/about/service pages): portrait 4:5, ≥1200×1500px.
- Music-page media: 16:9.
- Format: JPEG (photos) — put files in `assets/img/`, then replace the
  `{PLACEHOLDER_PHOTO}` markers in `build/content_*.py` with
  `<img src="/assets/img/yourfile.jpg" alt="DJ Orestis performing at …">` and regenerate.
  Descriptive alt text (venue + city) also helps SEO.
