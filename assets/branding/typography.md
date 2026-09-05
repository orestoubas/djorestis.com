# DJORESTIS — Typography

Goal: corporate-elegant with a quiet classical (Greek) undertone. Nothing "club flyer".

## Pairing (Google Fonts)

### Wordmark — **Cinzel** (400 only)
The logo alone. Trajan-column Roman capitals: the J is short and barely descends, so the vinyl O
gets clean air on both sides — the reason we moved off Marcellus for the wordmark. Cinzel has no
true lowercase (its lowercase codepoints render as small capitals), so it must never be used for
headings or body copy. Wordmark only, always all-caps.

Usage: `--font-wordmark` in `style.css`, and the `.lg` / `.wordmark` classes in the social,
press-kit and branding lockups. Nowhere else.


### Display / headings — **EB Garamond** (400, 500)
An old-style serif with real Greek. That is why it is here: the site ships in
four languages and the Greek pages are full of Latin words — "DJ Orestis",
"electronic, Afro, Latin, RnB" — so a Latin-only display face breaks every mixed
sentence into a second typeface mid-line. EB Garamond's Greek is drawn from
historical Garamond Greek types rather than added later, and it sits naturally
beside the Latin.

Its x-height is 0.406 em against Marcellus's 0.500, so the type scale is set
about 15% larger than it was to hold the same optical weight. Do not "fix" those
sizes back down.

Usage: H1/H2/H3, section titles, pull quotes, stat figures, price figures.

### Previously — Marcellus (retired from the site, kept for print assets)
A lapidary Roman-inscription serif: flared, upright, engraved-feeling capitals. It carries the
Greco-Roman heritage without resorting to "Greek letter" gimmick fonts, and in all-caps with wide
letter-spacing it reads like a law-firm foil stamp — exactly the register for corporate events and
weddings. Marcellus ships in a single weight (400), which conveniently enforces restraint.

Usage: H1/H2, section titles, pull quotes, stat figures. Always generous letter-spacing in all-caps
(`letter-spacing: 0.12–0.18em`), moderate spacing in mixed case (`0.01em`).

### Body / UI / tagline — **Manrope** (300, 400, 500)
A geometric sans covering Latin and Greek, holding the line Jost held. Its
x-height is 0.547 em against Jost's 0.469, so body copy is set at 16px where it
used to be 17px.

### Previously — Jost (retired from the site, kept for print assets)
A geometric sans in the Futura tradition: clean, international, slightly warm. It handles body copy,
navigation, buttons and the letterspaced all-caps tagline ("YOUR EVENT AS YOU DREAM IT") with a
modern, businesslike voice that contrasts nicely with Marcellus without competing.

Usage: body 400 at 16–18px, line-height 1.6–1.7; nav/buttons 500, all-caps, `letter-spacing: 0.08em`;
tagline/captions 300, all-caps, `letter-spacing: 0.25–0.35em`.

## Weights to load

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel&family=Marcellus&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
```

Total: 19 font files, but a browser fetches only the subsets a page uses —
an English reader never downloads the Greek. Was 6 files — light payload, fast static site. All self-hosted as woff2 under
`/assets/fonts/`; the Google Fonts link above is for reference and mockups only.

## Fallback stacks

```css
--font-wordmark: 'Cinzel', 'EB Garamond', 'Palatino Linotype', Palatino, Georgia, serif;
--font-display:  'EB Garamond', 'Palatino Linotype', 'Book Antiqua', Palatino, Georgia, serif;
--font-body:     'Manrope', 'Avenir Next', 'Segoe UI', Helvetica, Arial, sans-serif;
```

## The rule that matters

**Every text face on this site must cover Latin and Greek.** Marcellus and Jost
did not, and for months the Greek pages set "DJ Orestis" in one typeface and the
words around it in another, inside the same sentence. Before adopting any new
face, check it: request
`https://fonts.googleapis.com/css2?family=NAME` and confirm a `U+0370-0377`
block comes back. Cinzel is the single exception — it sets the wordmark, which
is Latin by definition.

The fallbacks are chosen to degrade gracefully: Palatino/Georgia keep the classical serif feel;
Century Gothic/Avenir keep the geometric sans feel.

## Rules of thumb

- Headings: Ivory `#F4F1E8`; allow one gold word or a thin gold rule, never a fully gold heading block.
- Never use Marcellus below ~18px — at small sizes switch to Jost.
- Never set Cinzel in mixed case: the lowercase are small capitals and the result reads as a mistake.
- Never bold-fake Marcellus (it has no bold); scale up or add letter-spacing instead.
- Avoid italics throughout — the brand voice is upright and composed.
- Alternates considered and rejected for the wordmark: Gilda Display (warmer, heavier in the header), Forum (narrower, J still hooks), Cormorant Garamond / Prata / Spectral (all share Marcellus's deep descending J, which was the problem).
- Alternate considered and rejected for headings: Playfair Display (too editorial/fashion), Montserrat (fine but generic — Jost has more character at the same safety level).
