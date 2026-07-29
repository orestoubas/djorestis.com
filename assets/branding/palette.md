# DJORESTIS — Color System

A dark, business-elegant palette: near-black surfaces, one refined gold, warm neutrals.
Gold is the *accent*, never the wallpaper — restraint is what makes it read as premium.

## Core palette

| Role | Name | Hex | Usage |
|---|---|---|---|
| Background (primary) | Onyx | `#0E0E10` | Page background, hero sections, favicon tile |
| Background (elevated) | Charcoal | `#16161A` | Cards, panels, footer, alternating sections |
| Hairline / border | Graphite | `#2A2A30` | Dividers, card borders, input outlines |
| Accent (primary) | Champagne Gold | `#C6A15B` | "DJ" in the wordmark, icons, links, primary buttons, active states |
| Accent (hover/bright) | Pale Gold | `#D9BC7F` | Hover/focus state of gold elements |
| Accent (deep) | Antique Gold | `#8F7439` | Pressed states, decorative rules, large gold surfaces at low intensity |
| Text (primary) | Ivory | `#F4F1E8` | Headings, "ORESTIS" in the wordmark, body copy on dark |
| Text (secondary) | Warm Grey | `#A8A49A` | Taglines, captions, secondary copy |
| Text (muted) | Stone | `#6E6A61` | Disabled states, footnotes, decorative hairlines only |
| Supporting accent (optional) | Aegean | `#35606A` | Sparingly: section tints, photo duotones, chart/secondary highlights. Never for text on dark. |

## Why muted gold (`#C6A15B`) and not bright gold (`#FFD700`)

- `#FFD700` reads as casino/party-flyer on screens — exactly the "nightclub-cheesy" register to avoid for Freshfields/BCG-type clients.
- `#C6A15B` is a desaturated champagne/brass tone: it evokes brushed metal, hotel ballrooms and letterpress foil — corporate-event language — while still being unmistakably "gold with dark".
- It also behaves better: it passes WCAG contrast as *text* on the near-black background (see below), so the gold "DJ" and gold links are genuinely readable, not just decorative.

## Usage rules

- **Backgrounds:** Onyx `#0E0E10` everywhere by default; Charcoal `#16161A` for cards/raised blocks; separate them with Graphite `#2A2A30` 1px hairlines, never with shadows.
- **Headings:** Ivory `#F4F1E8`. A single gold word or thin gold rule per section is the maximum gold density for headings.
- **Body text:** Ivory for primary, Warm Grey `#A8A49A` for supporting text. Never set body paragraphs in gold.
- **Primary button:** Champagne Gold background + Onyx `#0E0E10` text. Hover: Pale Gold `#D9BC7F` background. Pressed: Antique Gold `#8F7439`.
- **Secondary button:** transparent, 1px Champagne Gold border, gold text. Hover: border and text switch to Pale Gold, optional 6–8% gold background tint.
- **Links:** Champagne Gold, hover Pale Gold, underline on hover only.
- **Gold budget:** at most ~10% of any viewport should be gold. If a section already has a gold heading accent and a gold button, everything else in it stays neutral.
- **Aegean** `#35606A` is optional seasoning (e.g. a subtle tint behind the weddings section). If in doubt, leave it out — the brand works as a strict three-tone system (black / gold / ivory).

## WCAG contrast (against Onyx `#0E0E10`)

| Foreground | Ratio (approx.) | Verdict |
|---|---|---|
| Ivory `#F4F1E8` | ~17.4 : 1 | AAA — any size |
| Warm Grey `#A8A49A` | ~7.8 : 1 | AAA normal text |
| Champagne Gold `#C6A15B` | ~8.0 : 1 | AAA normal text — safe for links, buttons, the gold "DJ" |
| Pale Gold `#D9BC7F` | ~10.6 : 1 | AAA |
| Stone `#6E6A61` | ~3.6 : 1 | Large text / decorative only — not for body copy |
| Onyx text on Champagne Gold button | ~8.0 : 1 | AAA — button labels are fine |

(Ratios vs. Charcoal `#16161A` drop slightly; Ivory, Warm Grey and both golds still pass AA/AAA for normal text.)
