# DJORESTIS — Typography

Goal: corporate-elegant with a quiet classical (Greek) undertone. Nothing "club flyer".

## Pairing (Google Fonts)

### Display / logo / headings — **Marcellus** (400 only)
A lapidary Roman-inscription serif: flared, upright, engraved-feeling capitals. It carries the
Greco-Roman heritage without resorting to "Greek letter" gimmick fonts, and in all-caps with wide
letter-spacing it reads like a law-firm foil stamp — exactly the register for corporate events and
weddings. Marcellus ships in a single weight (400), which conveniently enforces restraint.

Usage: the wordmark, H1/H2, section titles. Always generous letter-spacing in all-caps
(`letter-spacing: 0.12–0.18em`), moderate spacing in mixed case (`0.01em`).

### Body / UI / tagline — **Jost** (300, 400, 500)
A geometric sans in the Futura tradition: clean, international, slightly warm. It handles body copy,
navigation, buttons and the letterspaced all-caps tagline ("YOUR EVENT AS YOU DREAM IT") with a
modern, businesslike voice that contrasts nicely with Marcellus without competing.

Usage: body 400 at 16–18px, line-height 1.6–1.7; nav/buttons 500, all-caps, `letter-spacing: 0.08em`;
tagline/captions 300, all-caps, `letter-spacing: 0.25–0.35em`.

## Weights to load

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Marcellus&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
```

Total: 4 font files — light payload, fast static site.

## Fallback stacks

```css
--font-display: 'Marcellus', 'Palatino Linotype', 'Book Antiqua', Palatino, Georgia, serif;
--font-body:    'Jost', 'Century Gothic', 'Avenir Next', 'Segoe UI', Helvetica, Arial, sans-serif;
```

The fallbacks are chosen to degrade gracefully: Palatino/Georgia keep the classical serif feel;
Century Gothic/Avenir keep the geometric sans feel.

## Rules of thumb

- Headings: Ivory `#F4F1E8`; allow one gold word or a thin gold rule, never a fully gold heading block.
- Never use Marcellus below ~18px — at small sizes switch to Jost.
- Never bold-fake Marcellus (it has no bold); scale up or add letter-spacing instead.
- Avoid italics throughout — the brand voice is upright and composed.
- Alternate considered and rejected: Cinzel (too "movie poster"), Playfair Display (too editorial/fashion), Montserrat (fine but generic — Jost has more character at the same safety level).
