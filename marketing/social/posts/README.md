# Ready-to-post images

Ten of the twelve weeks from `../../INSTAGRAM-PLAN.md` are rendered and ready to upload.
Captions for each week are in that plan.

| File | Week | Format |
|---|---|---|
| `01-launch.png` | 1 | Announcement |
| `02-weddings.png` | 2 | Service |
| `03-corporate.png` | 3 | Service |
| `04-greek.png` | 4 | Service (Greek) |
| `06-apartment.png` | 6 | Tip |
| `07-zeibekiko.png` | 7 | Music moment |
| `08-season.png` | 8 | Booking prompt |
| `10-briefing.png` | 10 | Tip (corporate) |
| `11-mykonos.png` | 11 | Music moment |
| `12-package.png` | 12 | Booking prompt |

**Weeks 5 and 9 are deliberately missing.** Both are event recaps, and a recap made from a
text card defeats the purpose — those need real photos or video from a night. Shoot them at
the next Papillon Schuman event and they become the two strongest posts in the set.

## Making more

Edit `../post-template.html` — the kicker, headline, and two meta slots are marked with
`<!-- SLOT: -->` comments. Then render:

```
chromium --headless --window-size=1240,1280 --screenshot=out.png post-template.html
```

and crop to 1080×1080. Or rebuild it in Canva using the brand colours
(`#0E0E10` background, `#C6A15B` gold, `#F4F1E8` ivory) and fonts Marcellus + Jost.
