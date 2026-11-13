# Old-web design: characteristics

What a site from roughly 1996–2003 looks like, and what survivors like Berkshire Hathaway, Hacker News and Drudge still look like. Use it to build a page that passes as one from that era.

Part 1 gives the rules a builder needs. Part 2 lists the traits, each set against the habit of today's default AI-generated page that it is the counterpart to ("vs."), and names where it was seen.

---

## Part 1: Building one

**The commonest failure is a page that is too clean, too complete and too designed.** Real pages were minimal and hand-made, or else machine-generated and sloppy. They were never tidy and thorough at the same time.

### Head and document

- **No doctype.** Yahoo 1998, Amazon 1999, MapQuest 2000, Hotmail 2001 and CDnow 1999 have none, so they render in quirks mode.
- **Minimal `<head>`.** Yahoo has only `<title>` and `<base>`. There is no meta description and no viewport meta. If a meta tag appears at all, it is a stuffed keywords list (~600–700 characters on Amazon and MapQuest) or a PICS-Label (MapQuest).
- **The title is the brand plus a slogan, with odd punctuation.** For example "Amazon.com--Earth's Biggest Selection" or "Yahoo!".
- **`<body>` is bare or carries only `bgcolor`, `text`, `link`, `vlink` and `alink`.** Colours often lack the `#`, as in Excite's `bgcolor="FFFFFF" link="000066"`. There are no margin attributes, so the browser's default 8px margin shows.

### Markup

- **Imperfect markup is authentic.** The real pages have broken quoting (`face="verdana," arial`), typos (`helvectica`, `<met ...>`), empty `<tr></tr>` and `<td> </td>`, a missing `</tr>`, `<form>` directly inside `<table>`, and `<a name="#top">`. Leave in a few of these, but not so many that they look deliberate.
- **Wrap nearly every run of text in its own `<font face=... size=...>`.** The face is usually `verdana,arial,helvetica` and occasionally `geneva,arial`. Sizes are `-1`, `-2`, `1` or `2`. Tags are repeated cell by cell; nobody sets a font once at the top.
- **Lay out with `<table>`: nested tables, `cellpadding`/`cellspacing`, `width=` in pixels or `100%`.** Spacer GIFs (`blank_1x1.gif`, `s.gif`) set the gaps.
- **Hand-written pages use upper- or mixed-case tags with unquoted attributes.** (Unverified: our fetch tool normalised case and quoting.)

### Links, URLs and images

- **Session and tracking IDs appear in URLs and hidden inputs.** Examples: MapQuest `uid=u55a02t7b4uclbxe:...`, Amazon `/exec/obidos/.../ref=gw_m_r_bo_1/`, CDnow `SID=...`, `/cgi-bin/...?link=...`.
- **Images are loaded by absolute URL from a separate image host.** Examples: `us.yimg.com`, `mqgraphics.mapquest.com/gif/`, `gs.cdnow.com`, or a bare IP. Some have no `alt`.
- **Navigation is ONE wide GIF with `usemap` (often also `ismap`), and its `<map>`/`<area>` block sits at the end of the file.** It is not one button image per item. This holds for Yahoo (460×59), Amazon (590×59) and MapQuest (polygon areas).
- **Text is set in GIFs:** logos, tab labels and even Hotmail's language picker (312×65 with a map).

### Content

- **Keep it plain and specific, and do not invent extras.** Real copy is short editorial blurbs, cross-promo one-liners ("Yahoo! Mail - free email account") and lists of names, titles and dates. Invented flourishes are the giveaway: "NEW!" badges, countdowns, feature grids and FAQs.
- **A utility homepage is the tool itself.** MapQuest shows the directions form. Hotmail shows a sign-in box with "New user? Sign up now!". Neither is a signup funnel with a feature list.
- **A store homepage is editorial.** Amazon 1999 shows no prices on the home page: just three titles and authors per box, and covers inside blurbs. CDnow does show "List Price $17.97" and a red "Add to Cart $12.58" link, and promos read "Always 30% Off".
- **Put the date top-right in small type** ("Wednesday, October 13, 1999"), with labels like "Updated Hourly".
- **Footer**
  - A row of `Text | Text | Text` links, then a single line in the smallest size, such as "© 1996-1999, Amazon.com, Inc.", "Legal Notices" or "TERMS OF USE / Privacy Statement".
  - Yahoo's footer has no copyright line at all; it holds region lists ("World Yahoos", "Metros") in a table.

### JavaScript

- **Present but peripheral:** `window.open(...)` help pop-ups, `form.login.focus()`, an `onchange` that swaps the form action. The page still works without it.

### Avoid

- A doctype, a meta description, a viewport meta, `alt` on every image, relative tidy URLs and consistent indentation.
- **"Best viewed in…" badges, hit counters, under-construction GIFs and webrings.** None appeared on the 10+ commercial captures checked. Those belong to personal pages (GeoCities and the like), which were not checked.
- **Boxes on a page that had none.** Yahoo's homepage has no boxed panels; Amazon's does.

---

## Part 2: Traits vs. the modern default

### Layout

- **The page is a table: either fixed pixel width, or `width=100%` with fixed-width (~590px) banners inside.** vs. full-bleed responsive hero. Space Jam 1996 (500px), MapQuest 2000 (739px), CDnow (590–600px), Amazon 1999 (100%), HN (min-width 796px).
- **A "box" is a table wrapped in a 1px coloured table** (outer `cellpadding=1 bgcolor=#cccc99` or `#708090`, inner `cellpadding=4` on white). vs. `rounded-2xl` cards with soft shadows. Amazon 1999.
- **Three columns: left nav rail, content, right rail.** vs. one centred column of stacked sections. Amazon 1999 (171px + content + 200px), MapQuest 2000 (grey form column), Wikipedia MonoBook.
- **The homepage *is* the content: an index of links or the tool itself.** vs. hero → 3 feature cards → social proof → pricing → FAQ → footer. Yahoo 1998, Drudge, HN, Hotmail.
- **Content starts top-left with only the browser's default margin.** vs. generous, uniform whitespace. Drudge, HN.
- **`<hr>` is used sparingly, mostly before the footer** (Yahoo 2, Excite 1 as `<hr noshade size=1 width=98%>`, Amazon 1 in the footer). Drudge is the exception, with ~40. vs. spacing and alternating background bands.

### Typography

- **Small Verdana/Arial via repeated `<font size=-1>`; ~10pt body, ~7pt metadata.** vs. large Inter/Geist and an oversized hero headline. HN, Amazon 1999, MapQuest 2000, CDnow.
- **No type scale; emphasis by bold or `size=+N`.** MapQuest uses bold size=4 links, Drudge a `size=+7` red headline. vs. a designed scale with all-caps eyebrow labels. Berkshire, Drudge, MapQuest.
- **Plain headings with a 1px rule beneath.** vs. gradient-filled headline text. Wikipedia MonoBook H1.
- **Literal, specific copy: titles, authors, dates, counts, prices.** vs. "Build faster. Ship smarter." Amazon's "100 Hot Books", Berkshire's "Updated <date>" under each link.

### Colour

- **Each site sets its own link colours.** Wikipedia uses #002bb8 with visited #5a3696, Berkshire purple with visited red, Amazon #003399 with visited #996633 and alink #FF9933, Excite 000066 with visited 990000. Hotmail makes visited the same as unvisited (#0033cc). MapQuest sets none and removes underlines (`a{text-decoration:none}`), as HN does. vs. buttons as the main affordance.
- **Flat `bgcolor` blocks in odd, house-specific palettes.** vs. indigo-500 → violet gradients.
  - Amazon: tan #cccc99, #eeeecc headers, #CC6600 orange text, #FFCC66 search box, #006699 subnav.
  - MapQuest: yellow #ffdd00 and maroon #990000.
  - Hotmail: a tiled background GIF, with white and yellow text on blue.
  - HN: beige #f6f6ef.
- **One loud accent, or a strong brand panel.** vs. gradient glows and coloured shadows. HN orange bar, Drudge red headline, Hotmail blue panel.
- **Novelty sites commit fully: black page, tiled star GIF, red text.** vs. tasteful dark mode. Space Jam 1996.

### Navigation

- **Text links separated by `|` or `-`, top and footer; "more..." in bold.** vs. sticky blurred navbar with a gradient "Get Started" button. Yahoo, Amazon, MapQuest, Berkshire.
- **The directory nav is a `<ul><li>` list in two table columns.** Each item is `<a><b>Category</b></a><font size=-1><br>sub, sub, sub...</font><br><br>`. vs. a mega-menu. Yahoo 1998; Amazon 1999 does the same in its left rail, without `<ul>`.
- **Image-map nav GIF** (see Part 1). vs. Lucide icon + label.
- **Boxed tabs with 1px borders, the selected one tinted.** vs. segmented pills. Wikipedia MonoBook.
- **A "Text Only" version link.** vs. one JS-dependent version. Amazon 1999.

### Imagery

- **Small, functional images: product covers inside blurbs (`align=left`, `hspace=7 vspace=3`), logos, bullets.** vs. 3D blobs, AI illustrations, stock team photos. Amazon 78×107 covers, MapQuest compass GIFs.
- **Bullets are `<li>`, a literal `•`, or a tiny GIF; it depends on the site.** vs. emoji- or icon-led feature bullets. Yahoo `<li>`, Amazon and Excite `•`, MapQuest yellow-triangle GIF.
- **Invisible spacer GIFs hold the layout.** vs. flex/grid gap utilities. MapQuest, HN.

### Interaction

- **Native form controls, sized in characters.** vs. custom shadcn inputs and pill buttons. Yahoo `size=30` + "Search", MapQuest `size=15` and a 2-character state box.
  - Occasionally a tiny inline `<style>` tints the submit button: MapQuest `.button` is maroon/yellow.
- **Buttons named for what they do.** vs. a primary + ghost CTA pair. MapQuest "Get Directions" / "Clear".
- **Every action is a full page load; state lives in the URL and hidden inputs.** vs. client-side SPA.
- **Pop-up windows for help.** vs. modals and drawers. MapQuest `window.open(...515×600)`.
- **No motion; hover barely styled.** vs. fade-in-on-scroll everywhere. Every site checked.

### Density and content

- **Dozens of links per screen (~90 on Amazon's home, hundreds on Drudge); the reader scans.** vs. three cards and one CTA per viewport.
- **Small grey metadata under each item: date, author, points.** vs. no timestamps or provenance. HN, Berkshire.
- **The proof is the content, specific and checkable.** vs. logo strips and anonymous testimonials. Berkshire shareholder letters, Amazon bestseller lists.

### CSS and code

- **Styling mostly in HTML attributes (`bgcolor`, `<font>`, `<center>`, `align`).** vs. dozens of Tailwind utilities per element. Berkshire, Space Jam, Amazon 1999, Drudge.
- **CSS, where present, is thin and layered on top of the font tags.** Hotmail uses `<font class="f">`, MapQuest a tiny inline `<style>`, MonoBook one stylesheet with `* html` IE hacks. vs. a utility framework and component library.
- **Light pages.** vs. heavy client JS. Berkshire, HN.
- **Not responsive: built for 800×600; on a phone you zoom and scroll sideways.** vs. mobile-first.

---

## Limits of this doc

- **Some details are unverified.** Tag case, attribute quoting and whitespace in the captures could not be checked, because the fetch tool normalised them. A raw-bytes fetch is needed; the Wayback Machine blocks plain `curl`.
- **Personal and hobby pages were not checked.** That covers GeoCities, Angelfire and fan sites; Slashdot, eBay and early Google were not checked either. Everything here describes commercial sites and a few survivors.
- **The built pages were compared by source only.** Each agent's page was checked against real captures, but nobody rendered either side for screenshots.

## Sources

- **Fetched 13 Nov 2026 (raw `id_` Wayback captures where dated).**
  - 1990s: Yahoo (12 Dec 1998), Excite (16 Jan 1999), CDnow (27 Apr 1999), Amazon (13 Oct 1999).
  - 2000s: MapQuest (20 May 2000), Hotmail (1 Jun 2001), Wikipedia MonoBook `main.css` (28 Feb 2005).
  - Live sites: Hacker News, berkshirehathaway.com, drudgereport.com, spacejam.com/1996.
- **Modern / AI-generated look.** These are practitioner write-ups, with no measurement behind them:
  - [925studios](https://www.925studios.co/blog/ai-slop-design-tells)
  - [Utsubo](https://www.utsubo.com/blog/built-with-ai-trust-signals-2026)
  - [codemyspec](https://codemyspec.com/blog/vibe-coded-websites-look-the-same)
  - [DEV / alanwest](https://dev.to/alanwest/why-every-ai-built-website-looks-the-same-blame-tailwinds-indigo-500-3h2p)
  - [devtake](https://devtake.pages.dev/article/ai-generated-frontend-slop)
