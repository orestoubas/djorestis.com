# DJORESTIS — Branding Proposals: Summary

All files live in `assets/branding/`. Open **`preview.html`** in a browser (with internet access,
so Google Fonts load) to compare everything side by side.

## The concepts

**Concept 1 — Lapidary Wordmark** (`concept-1.svg`)
The most conservative direction: "DJORESTIS" set in Marcellus, an engraved Roman-inscription serif,
with the "DJ" in champagne gold and "ORESTIS" in ivory, wide letter-spacing, a small rotated-square
ornament above and the tagline between hairline rules below. It reads like a law-firm or five-star
hotel foil stamp — maximum trust for the Freshfields/BCG audience — and the classical letterforms
quietly nod to the Greek heritage without any literal motif.

**Concept 2 — The Vinyl O** (`concept-2.svg`) — *recommended*
The same elegant Marcellus wordmark, but the "O" of ORESTIS is drawn as a vinyl record: a gold outer
ring, a faint ivory groove, and a gold label dot. One idea, executed once, at the exact centre of the
name — it makes the brand unmistakably a music brand while staying completely free of clip-art. The
record doubles as a standalone monogram, which is exactly what the favicon uses.

**Concept 3 — Column & Waveform** (`concept-3.svg`)
A modern alternative: "DJ ORESTIS" in Jost SemiBold caps with a compact mark of five symmetric gold
bars that reads simultaneously as an audio waveform/equalizer and as a Greek column silhouette. The
most contemporary and "agency" of the four — a good fit if the client wants to skew toward the
corporate-tech end of the event market.

**Concept 4 — Crest Monogram** (`concept-4.svg`)
A stacked, ceremonial lockup: the vinyl-record mark large at top, a discreet three-unit Greek meander
(spiral-key) accent beneath it, then the wordmark and tagline. This is the "wedding invitation /
poster / centre-of-page" arrangement — best used as the secondary vertical lockup of Concept 2 rather
than as a competing brand.

## Recommendation

**Concept 2 (The Vinyl O) as the primary logo**, with Concept 4 as its official stacked/vertical
variant (same mark, same type) for square formats, posters and invitations, and `favicon.svg` — the
vinyl O alone on an Onyx rounded tile — for browser tabs and social avatars. Rationale: Concept 1 is
trustworthy but forgettable and says nothing about music; Concept 3 is handsome but the most generic;
Concept 2 keeps all of Concept 1's corporate elegance while embedding the DJ story into the name
itself, and it yields a mark that scales from a 16 px favicon to a stage backdrop.

## Identity at a glance

- **Palette** (full rules and WCAG notes in `palette.md`): Onyx `#0E0E10` and Charcoal `#16161A`
  backgrounds; **Champagne Gold `#C6A15B`** as the single accent (hover `#D9BC7F`, pressed
  `#8F7439`); Ivory `#F4F1E8` and Warm Grey `#A8A49A` text; optional Aegean `#35606A` supporting
  tint. Muted gold was chosen over bright `#FFD700`, which reads casino/party-flyer; champagne gold
  reads brushed-metal/ballroom and also passes WCAG AAA as text on the near-black background.
- **Typography** (details in `typography.md`): **Marcellus 400** for the wordmark and headings +
  **Jost 300/400/500** for body, navigation, buttons and the letterspaced tagline. Load via one
  Google Fonts request; fallbacks: Palatino/Georgia (serif), Century Gothic/Segoe (sans).

## Usage guidance

- The logos are hand-written SVG using Google Fonts font-family names. On the website, either inline
  the SVG in the HTML (recommended for the header) or embed via `<object>`; each file also carries
  its own `@import` so it renders correctly opened standalone. Note that `<img>` embedding will NOT
  load the fonts — inline or `<object>` only. The favicon is pure shapes and safe everywhere,
  including `<img>` and `<link rel="icon">`.
- Minimum sizes: horizontal wordmark >= 200 px wide (drop the tagline below ~320 px); crest >= 120 px
  tall; below that, use the favicon mark alone.
- Keep clear space of at least the height of the "O" ring around every lockup; never place the logo
  on photography without a dark scrim; never recolor beyond the approved gold/ivory pair.
- Gold discipline: one gold element per zone (the "DJ", a rule, or a button — not all three).
