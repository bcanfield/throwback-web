---
name: throwback-web
description: Design and build a website from scratch in a deliberately dated style (1996–2003 table web, 2004–2009 Web 2.0, or 2010–2013 skeuomorphic/early CSS3) that passes as real, not as a parody. Use whenever the user wants a retro, old-school, 90s, Y2K, early-2000s, Web 2.0 or skeuomorphic website, says "make it look old" or "like the old internet", wants a site that is "not like every AI site" or "stands out from AI slop", or asks to throw back, period-style or recreate an old-web look, even if they never name an era.
---

# Throwback web

Thesis: the best way to stand out in a pool of AI slop is to throw back dramatically. The target is a page a person from that year would take for a real site: never a parody of it, and never a modern page wearing a filter.

## Modes

Pick the mode before building and say which one you're using.

- **Costume (default):** a real site someone will ship today. The visible design and the period idioms in the markup are faithful. Drop the period fingerprints that only matter for forgery and harm real users: fake session/tracking IDs, dead third-party scripts (`urchin.js`, `_gaq`, `plusone.js`, Flash), `http://` assets, deliberately broken markup, stale © years, ad `document.write`, old-version generator metas, unmaintained JS libraries.
  - **Basics stay** wherever they don't change the look: `alt` text, form labels, keyboard use, readable contrast, HTTPS, UTF-8 (declared the era's way).
  - **Copyright:** the © line ends at the current year ("© 1999–2026", or just "© 2026"). Dated content (changelog entries, post dates, "Updated October 13, 1999") is content, not a fingerprint: keep it.
  - **Fonts:** name every substitution in the report. Stacks carry the period's own fallbacks, then an open one for systems without the face: `verdana, geneva, "DejaVu Sans", sans-serif`; `georgia, "DejaVu Serif", serif`; `"Lucida Grande", "Lucida Sans Unicode", tahoma, sans-serif`. Typekit faces: era file §4.
  - **Phones:** each era file has a "Costume mode" section with its policy. In short: eras 1–2 keep the fixed layout and zoom out on a phone, as they did then, with a fixed `width=N` viewport so it opens fitted, zoom never disabled, body text big enough to survive. Era 3 picks either Dribbble-style `width=1000` or Bootstrap 2's period responsive add-on. State the choice.
- **Artifact:** keeps every fingerprint, for art pieces, demos and museum-style recreations. Items marked **[artifact]** in the era files apply only here.
- **Always:** references are for technique. Never copy a real brand, logo, name, image, copy or site; invent the site's own.

## Process

Paths to `references/` and `scripts/` are relative to this skill's directory; run the scripts by their full path.

### 1. Read the brief

Note what the site *does* (tool, store, community, blog, product page), who uses it, and whether it ships (costume) or is a piece (artifact). If the user names an era or decade, honour it.

### 2. Pick the era and the genre

Pick by what the site does, not its subject. State the pick in one line with the reason; ask only if the brief is empty.

| Kind of site | Era | Genre in the era file |
|---|---|---|
| Local business, shop with a catalogue, directory, listings | 1 | store, or portal/directory |
| A tool: calculator, lookup, booking, tracker, sign-in | 1 | utility (the homepage *is* the tool) |
| Headlines, link list, investor/plain corporate, documentation | 1 | plain survivor, or reference |
| Event, fan, novelty, movie | 1 | novelty |
| Personal homepage, hobby page | 1 | personal (unverified, say so) |
| Community, forum-ish, link sharing, voting, bookmarking | 2 | social news / bookmarking |
| Blog, newsletter archive, small company blog | 2 | Kubrick blog |
| Photo or media sharing | 2 | photo/community (Flickr) |
| Web app launching or in beta, sign-up page | 2 | startup landing (2008) |
| Indie app, Mac/iOS app, product page | 3 | iOS/Mac app page |
| SaaS, API, developer tool | 3 | Bootstrap 2 startup |
| Designer portfolio, writer's journal | 3 | textured blog |

User words map too: "90s", "Y2K", "early 2000s" → 1; "Web 2.0", "mid/late 2000s", "MySpace era" → 2; "skeuomorphic", "iOS 6", "2011", "early Bootstrap" → 3.

Then read **only** that era's file:

- Era 1, 1996–2003: [references/era-1996-2003.md](references/era-1996-2003.md)
- Era 2, 2004–2009: [references/era-2004-2009.md](references/era-2004-2009.md)
- Era 3, 2010–2013: [references/era-2010-2013.md](references/era-2010-2013.md)

Nothing from 2013 on goes in: no responsive-flat Bootstrap 3 look, no Material, no dark/Inter/glass. Those are on each era file's "too new" list.

Done when: one era, one genre, one mode, stated.

### 3. Pick 2–3 reference sites

Choose 2–3 exemplars of that genre from the era file's Exemplars table. Write down, per reference, the concrete values you will use: column width, palette hexes, font stack and size, nav pattern, footer pattern. Optionally fetch the real captures with [references/research-method.md](references/research-method.md); skip it when offline: the era file is enough.

Done when: every value you need for the build has a source (the era file or a fetched capture), not a guess.

### 4. Build with the era's rules

- Start from the era file's §8 Skeleton (head + layout scaffold), then follow its shared rules and genre section. Copy concrete values; don't round them toward modern defaults.
- Write the copy the era wrote: literal, specific, a bit plain (names, dates, counts, prices). Era-2 community pages need raw user text; blogs need the template strings.
- Images: make bitmaps, not CSS stand-ins, when the era used bitmaps. `scripts/make_assets.py` (`--help` lists them) builds:
  - era 1: spacer GIF, aliased logo/heading GIF (`logo`), one wide image-map nav GIF that prints its `<map>` (`navmap`);
  - era 2: tall gradient strips, corner GIFs, 88×31 buttons (costume: only for real links, never joke buttons);
  - era 3: noise/paper tiles, a two-state download button sprite (`appbutton`), icon sprites (`sprite`), a flat app-window frame with drop shadow for screenshots (`window`).
  Paste the CSS/HTML the script prints: offsets and `<area>` coords come from the image, so nothing is mis-cropped. Where each asset goes: the genre section in the era file.
- Keep the leftovers the genre had (a table in era 2, an IE hack, a CMS class name, patchy prefixes in era 3). A page with none reads as a rebuild.

### 5. Imperfection pass (costume)

Real pages were made by hand, under deadline. A finished build is always too even; roughen it without breaking it (nothing overlaps, every link works, contrast holds). Do three of the general items and two of your era's:

- [ ] Cut one section the brief can live without.
- [ ] Unequal columns: one runs longer than the other; nothing is mirrored left/right.
- [ ] Spacing varies: one box has different padding, one gap is odd (7px, 13px), not every block on the same rhythm.
- [ ] Copy plainer and shorter: fragments, numbers, names; one unglamorous fact (hours, a phone number, "Last updated …").
- [ ] Lists have 2, 4 or 5 items, not 3; not every item gets an icon or image.
- Era 1: a stray empty `<td>&nbsp;</td>`; form labels not lined up (inputs with different `size=`); a sibling box in a different `<font size>`; a bold "more..." link.
- Era 2: one leftover table or inline `style=`; headings that differ between sidebar boxes; one box square where the rest are rounded; user text with a typo or ALL-CAPS.
- Era 3: prefixes vary per rule; letterpress on some text, not all; a caption that is one plain fragment; the price beside the button, not in a 3-tier table.

### 6. Self-check

Check against both failure modes, in this order:

1. **The cartoon:** did you build the era's clichés instead of its pages? (Era 1: hit counters and "best viewed in" on a commercial site. Era 2: gloss, reflections, beta starbursts. Era 3: bezel phones, linen + leather, Lobster, the full prefix ladder, ribbons.) Keep at most one signature flourish.
2. **Too tidy / too generic:** is it cleaner, more complete and more evenly spaced than any real page was? Does it still have the modern skeleton (hero → feature cards → testimonials → pricing → FAQ) or AI copy ("Get started", "seamless")? Cut sections; roughen what the era file says was rough. When the brief needs all of those, compress, don't stack bands: price goes beside the download/sign-up button; quotes go in a sidebar or one line under the hero; features become a list; FAQ becomes one "Questions? write to …" line. At most three full-width bands.
3. **Tells:** walk the era file's Tells list; most should be present.
4. **Lint:** run the linter on every HTML and CSS file and fix each error (or justify it in one line):

   ```
   uv run scripts/lint_era.py --era 1|2|3 --mode costume|artifact site/*.html site/*.css
   ```
   It flags too-new and too-old features, cartoon and too-tidy signals, and in costume mode the harmful fingerprints and missing basics. It ends by listing every rule it checked and the error/warning/note counts. Regex heuristics: a warning is a prompt to look.

Done when: the lint has no errors you haven't justified, and you can name which reference each major element came from.

### 7. Render and look

Serve the folder over HTTP (`file://` hides viewport behaviour): `python3 -m http.server 8000 --bind 127.0.0.1` in the site folder, run in the background; stop it when done. Then screenshot at the era's screen, 800×600 (era 1) or 1024×768 (eras 2–3), **and at phone width**. With scrapling (load the tools via ToolSearch; the viewport is set when the session opens, not per screenshot):

```
browser_open       session_id="phone" additional_args={"viewport":{"width":375,"height":667},"device_scale_factor":2,"is_mobile":true,"has_touch":true}
browser_fetch      session_id="phone" url="http://127.0.0.1:8000/index.html" google_search=false
browser_evaluate   session_id="phone" expression="() => [innerWidth, document.documentElement.scrollWidth]"
browser_screenshot session_id="phone"
close_session      session_id="phone"
```

`is_mobile` makes the page's viewport meta apply, as on a phone: `innerWidth` is then your `width=N` (fixed policy) or 375 (`device-width`); `scrollWidth` above `innerWidth` means something overflows. For the desktop shot open a second session with only `{"viewport":{"width":800,"height":600}}` (or 1024×768). Close every session you open. Without scrapling: agent-browser or headless Chrome (`--window-size=800,600 --screenshot`) for desktop; for the phone under a fixed `width=N` policy, render at N wide and judge the text at 375/N of its size, which is what the phone shows.

Compare side by side with a reference screenshot if you fetched one. Look for: anything that reads as 2020s at thumbnail size; text unreadable on the phone after zoom-out; content overflowing its column; images missing.

Done when: you have looked at both screenshots, they look like the references at a glance, and the phone view works under the stated policy.

## Reporting back

Tell the user: era, genre, mode and why; the 2–3 references; what was dropped for costume mode (and the phone policy); any font substitutions; anything you took from an item the era file marks unverified.
