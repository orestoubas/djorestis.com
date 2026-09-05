# Venue logos

Drop a file here and it replaces that venue's name in the "Where I play" section
on the homepage. Nothing else to change — the generator checks for the file on
every build and falls back to the text name when it is missing.

## Filenames

The stem must match the `logo` field in `build/venues.py`:

| File stem     | Venue            |
|---------------|------------------|
| `machina`     | Machina          |
| `arion`       | Arion            |
| `greekit`     | Greekit          |
| `greekyaya`   | Greek Yaya       |
| `meatropolis` | Meatropolis Grill|
| `kosmos`      | Kosmos Place     |
| `papillon`    | Papillon         |
| `akt`         | AKT              |
| `capital`     | Capital          |
| `tomeli`      | To Meli          |
| `chevalmarin` | Le Cheval Marin  |
| `hivernage`   | Hivernage        |
| `melusina`    | Melusina         |
| `veilingzaal` | De Veilingzaal   |
| `cameraclub`  | Camera Club      |

Extensions are tried in this order: `.svg`, `.png`, `.webp`, `.jpg`.

Nine of these ship with the site already, built by `tools/build-venue-logos.py`
from sources in `build/venue-logo-src/`. Prefer that script over dropping a file
here by hand: it flattens the mark to the site's ivory tint and normalises its
size against the rest of the wall. A raw file dropped here still works, but it
will sit at whatever colour and weight it arrived in.

## What to ask each venue for

`.svg` if they have it — it stays sharp at any size and weighs almost nothing.
Otherwise a transparent `.png` at least 300px wide. A logo on a white rectangle
will show as a white rectangle on the dark background, so it has to be
transparent or the mark has to be cut out first.

The site desaturates every logo so the row reads as one strip rather than a
ransom note of brand colours; the real colours come back on hover.

## Permission

A venue's logo is its trademark, and putting it on your site implies they
endorse you. Get it in writing before adding a file — an email reply saying
"yes, you can use our logo on your website" is enough. The supplier-list request
in `marketing/VENUE-OUTREACH-KIT.md` is the natural place to ask; the same
message can request both.

Until a logo arrives, the venue still appears — as its name, linked to its own
site or Instagram. That is a perfectly good state to ship in, and it is what is
live today.
