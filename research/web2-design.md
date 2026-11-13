# Web 2.0 design: characteristics

The phase after [old-web-design.md](old-web-design.md): roughly 2004–2009. Use this doc to build a page that passes as one from about 2006–2008.

- **Part 1:** shared rules.
- **Part 2:** rules for each genre, because each has its own fingerprint.
- **Part 3:** each trait against the phase before ("was") and the modern AI default after ("vs.").

### Two failure modes, both seen in test builds

1. **Building the cartoon:** glossy gel buttons, mirror reflections, "beta" starbursts, pastel everything. Six real 2006–2008 sites, including three 2008 startup landing pages, showed **no** reflections, starbursts or "beta" badges. The design guide of the time already called them overused in 2008.
2. **Building it too tidy and too generic.** Real pages were:
   - template output (WordPress);
   - raw user text with typos (Digg);
   - mixes of new CSS and leftover tables (Flickr, Dropbox).

   An agent writing "clean Web 2.0" from scratch produces none of those.

---

## Part 1: Shared rules

### Head and document

- **Doctype: XHTML 1.0 Transitional, in standards mode.** It is verified in a real browser on Digg 2006, a 2006 WordPress blog, Remember The Milk 2008, Mint 2008 and Dropbox 2008. del.icio.us 2006 used XHTML 1.0 **Strict**, and its `<html id="delicious">` had no xmlns. Never `<!DOCTYPE html>`.
- **`<html xmlns="http://www.w3.org/1999/xhtml">`,** usually without `xml:lang`.
- **Encoding: `<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />`.** 37signals uses iso-8859-1. No `<meta charset>`, no viewport meta. From 2008, `<meta http-equiv="X-UA-Compatible" ...>` is plausible (Dropbox).
- **A description or keywords meta is optional:** Flickr and 37signals have one, Digg has neither.
- **Title is a lowercase brand or a slogan:** "digg / News", "del.icio.us", "Twitter: What are you doing?", "WordPress › Blog".
- **Favicon:** `<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />`.
- **Feed autodiscovery:** `<link rel="alternate" type="application/rss+xml" title="..." href="..." />`.
- **CSS:** `<link rel="stylesheet" type="text/css" media="screen" href="..." />`, or `@import` in `<style type="text/css" media="all">`. An extra inline `<style>` block in the page is normal (Dropbox, Kubrick). Rails adds `?1167433714` cache-busters.
- **Scripts:** a pile of `<script type="text/javascript" src="...">` in `<head>` (Digg has ~10). Inline code sits in `//<![CDATA[ ... //]]>`. No `async`, `defer` or modules.
- **Analytics:** `urchin.js`, then `_uacct = "UA-xxxxx-x"; urchinTracker();`, over `http://`. Optional: a default WordPress install has none.

### Markup

- **Structure:** `<div id="container|page|wrapper|header|content|sidebar|footer">`, and nav as a `<ul><li><a>` list.
- **Tables and old attributes survive:** Flickr 2007 has nested layout tables, and Dropbox 2008 is an 800px table with `<center>`, `border="0"` and `valign`. A page with zero leftovers is too pure. The amount varies by genre (Part 2).
- **XHTML-style empties:** `<br />` and `<img ... alt="" />`. Validity was not required; Dropbox's markup doesn't validate.
- **Inline styles and handlers on individual elements are normal:** Digg puts `style="z-index:1000"` on each story, and `onclick="return(...)"` handlers are everywhere.
- **Skip links,** `accesskey`, microformats (`hentry`, `rel="bookmark"`, `rel="nofollow"`) and real entities (`…`, `—`, `&amp;`).

### CSS

- **Width.** Most sites are a centred fixed column: Flickr 750px, Twitter 755, Kubrick 760, RTM 765, MySpace and Dropbox 800, 37signals 840, Apple 980. Digg is fluid (Part 2). Centre with `margin:0 auto`, plus `body{text-align:center}` and `#container{text-align:left}`.
- **Columns:** two at most three, floated, with a clearfix. Either `.clearfix:after{...}` with `* html .clearfix{height:1%}`, or `<br class="clear" />`.
- **IE6 hacks are visible:** `* html`, `/*IE6*/` comments, `!important /*imp for ie6*/`.
- **Gradients are background images.** A tall image with `repeat-x`, never a short strip tiled so the bands repeat (a tell in one test build).
- **Rounded corners are made from images or markup:**
  - stacked 1px `<b>` or `<div>` rows (RTM, Mint, Twitter `.xb1`–`.xb7`);
  - corner GIFs (Dropbox `box-hl/hr/bl/br`);
  - background images on nested divs (Digg).

  Four absolutely positioned corner divs on a flat box is a tell. `-moz-border-radius` is at most a Firefox-only extra. Never `border-radius`.
- **Buttons and tabs use sliding doors and sprites.** Hover by `background-position`. A pill button is three PNG slices with a `repeat-x` middle (RTM "Signup Now!").
- **Shadows:** `text-shadow` only as a Safari-only extra, as in Dropbox's rgba. No `box-shadow`.
- **Type base on `body`** in percent or em. Families are Arial, Verdana, Lucida Grande, Tahoma or Trebuchet at 11–12px or 10pt. Notes go down to 8pt. Big headings get `letter-spacing:-1px`.
- **Links are mostly still underlined,** with a brand blue and a lighter visited colour. The reversed-colour hover block is Flickr's alone; don't make it a default.

### JavaScript

- **Libraries date the page.** In 2006 they are Prototype + script.aculo.us (Digg, Twitter, WordPress K2), Lightbox, swfobject and moo.fx. By 2008 MooTools is also common (Mint: `window.addEvent('load', ...)`). jQuery 1.x is plausible toward 2008–09 but was not seen.
- **Handlers are inline:** `href="javascript://" onclick="return(fn())"`, `window.open('...','TOC','width=600,height=480')`.
- **Ads:** `document.write('<' + "script ...")` phpAds zones.
- **Loaders:** `d.write` for analytics, and placeholder text set by a script (Facebook, Dropbox).
- **Flash** for video and demos, via swfobject (Dropbox).

### Avoid

- **Too old:**
  - `<font>`, `bgcolor` on everything, spacer-GIF layouts and image-map nav.
  - No doctype.
  - A link-wall homepage.
- **Too new:**
  - Flexbox, grid and media queries.
  - `border-radius`, `box-shadow`, CSS gradients, `rgba` outside Safari-only `text-shadow`, and `@font-face`.
  - Google Fonts, icon fonts and SVG.
  - HTML5 elements, `data-` attributes and the `placeholder` attribute.
  - `addEventListener` idioms, ES6, `fetch`, jQuery 2+, `https://` assets and `gtag`.
- **The cartoon:** reflections, starbursts and "beta" badges as graphics. "Beta" is plain text or in the title (Dropbox), or a small text label. At most one glossy element, typically a three-slice pill sign-up button. Its gloss is unverified.
- **Edited, uniform copy where real sites had user text or template strings.**

---

## Part 2: By genre

### Social news / bookmarking (Digg, del.icio.us, 2006)

- **Digg is fluid**
  - `html{min-width:902px}`, `#container{max-width:1200px}`, body padding `0 20px`.
  - A rounded white content panel (`main-back.gif`) sits on a pale body gradient.
- **Two nav bands.** The blue brand band (#1B5790) carries a sprite logo with a hover state and section buttons (News / Videos / Podcasts, with a text "beta"). Below it is a green sub-nav (#CCDEAF): "All Topics / Technology / …", with a "Submit a New Story" pill on the right. A login drawer drops down from the header. Popular and Upcoming are tabs with counts ("Upcoming (3,455)").
- **Each story**
  - **Count:** a yellow shaded count box ("30 diggs", text #736926) beside a separate "digg it" box. Each is its own sprite (`digg-box-2.gif`, hover at `-300px`).
  - **Headline:** an h3 at 130% bold, `letter-spacing:-0.02em`, underlined, with a dotted `link-line.gif`. Visited is a pale #86b0e1 and hover is #003.
  - **Timestamp:** a red bold timestamp (`.d`, #a12a2a): "made popular 4 minutes ago".
  - **Toolbar:** "N comments | Blog It | Email It | Topic: x", plus a Bury dropdown.
- **Palette** is earthy rather than pure blue: text #393733, green h2 #8DAB3B, orange #E45B00, olive #93883F.
- **Body type:** `83%/1.4 arial`. The h2 is 185% at -1px.
- **Copy is raw user submissions,** with typos, ALL-CAPS words and odd casing.
- **Footer:** a grey #eee strip of six `<dl>` columns with uppercase Tahoma links, a t-shirt promo image, then a trademark and Creative Commons paragraph.
- **del.icio.us differs**
  - XHTML Strict; `#ffffd0` notices.
  - Per-item "people 130", "first posted by …" and five tags.
  - A tag list on a `#eee` strip with size classes.
  - Tags per item and tag clouds belong to bookmarking, not to Digg.

### WordPress blog with the Kubrick default theme (2006)

**WordPress output is a fingerprint, so copy the template strings exactly.** The theme's source is on GitHub at `raw.githubusercontent.com`, under the WordPress tag `2.0.5`.

- **Head:**
  - `<head profile="http://gmpg.org/xfn/11">` and `<meta name="generator" content="WordPress 2.0.5" />`.
  - Then the stylesheet, the RSS alternate and pingback links, in that order.
  - Then an inline `<style media="screen">` that sets the `#page` background image.
- **Post:**

  ```html
  <div class="post" id="post-N">
    <h2><a href="..." rel="bookmark" title="Permanent Link to TITLE">TITLE</a></h2>
    <small>November 9th, 2006 <!-- by author --></small>
    <div class="entry">...</div>
    <p class="postmetadata">Posted in <a>Cat</a> | <a>Edit</a> | <a>N Comments »</a></p>
  </div>
  ```

  - The author name appears only as an HTML comment.
  - Dates are always "Month Dayth, Year".
- **Sidebar order:**
  1. Search.
  2. A "You are currently browsing…" paragraph.
  3. Pages.
  4. Archives.
  5. Categories.
  6. The blogroll, with each link category under its own `<h2>`.
  7. Meta: Register or Site Admin, and Log in.

  There is no calendar, and the author blurb is commented out.
- **Look:**
  - Body #d5d6d7 with a 1px-wide JPG background (`kubrickbgcolor.jpg`).
  - `#page` is 760px, with a 1px #959596 border and a 20px margin.
  - `kubrickbg.jpg` draws the sidebar divider. The header is one 200px image, with no `<img>`. The footer uses `kubrickfooter.jpg`.
  - Content 450px, sidebar 190px, 45px left padding. `hr{display:none}`.
  - Links #06c, hover #147, visited `.entry p a` #b85b5a.
- **Details:**
  - `.alt` comment striping (#f8f8f8, 1px #ddd borders).
  - `abbr` with a dashed underline, and `<span class="caps">` around acronyms.
  - `» ` bullets on sidebar lists via `:before`.
- **Footer:**
  - "Entries (RSS) and Comments (RSS)", with `feed:` scheme links.
  - A query-count comment.
  - Credits that include Michael Heilemann's tagline.
- **The K2 theme differs:** `hentry`, `entry-title`, `entry-meta`, and `abbr.published` with an ISO title.

### Startup landing page, ~2008 (Remember The Milk, Mint, Dropbox)

- **No sidebar.** Pitch, sign-up and proof all sit in the centre column.
- **Remember The Milk** (RTM, March 2008):
  - A full-width blue feature band (#005CB8 with `hp_bg.png`) around a 765px inner column.
  - A tilted product graphic overlaps the band by 12px. It is a stylised checklist, not a screenshot.
  - A three-slice "Signup Now!" pill, then "for a free account" and "take a tour".
  - A 3×2 `<table>` of captioned feature images.
  - A press quote with the publication's logo.
  - A six-column footer link list plus a legal line.
- **Mint 2008:**
  - Plain-text headings ("Free Personal Finance Software").
  - "Learn More" and "Sign Up Now" buttons.
  - A tabbed tour.
  - Rotating testimonials with full name and city.
  - Trust seals in the footer.
  - MooTools.
- **Dropbox, June 2008, in beta:**
  - An 800px table layout with `<center>`.
  - A Flash demo video.
  - A beta email sign-up form with script-set placeholder text.
  - "beta" in the title and copy.
  - A right-aligned 8pt footer row.
  - Tahoma/Trebuchet at 10pt.
- **Labels:** "NEW" at 0.75em on #FFCC66, or an orange "New!" (#EA5200).

### Others, from the first research pass only (no test build)

- **Flickr 2006–07:**
  - 750px with nested tables.
  - A 424×283 hero photo with a "Sign Up Now!" button.
  - Links #0063DC, with a reversed hover.
  - A NEW label in 8px Verdana on #FFE28A.
- **37signals:** 840px, Verdana 12px with Georgia intros, a cream band #fff9d8, a black footer with 10px text.
- **Twitter 2007–08:** 755px, Lucida Grande .75em, a 555+166 split, a #DDFFCC sidebar, a "beta" label, and Snazzy corners.
- **MySpace 2006:** 800px, Verdana 11px, a #039 header, and a `Home | Browse | Search | …` pipe nav.

---

## Part 3: Traits, before and after

| Trait (2004–2009) | Was (1996–2003) | vs. modern AI default |
|---|---|---|
| Centred fixed column 750–840px (or Digg-style fluid with min/max) on a pale grey or gradient canvas | Left-flush table or `width=100%` on white | Full-bleed responsive sections |
| 2 columns, max 3, made with floats + clearfix; tables linger | 3 table columns | One centred column of stacked sections |
| Solid header band in the brand colour, often a second sub-nav band | Logo GIF, image-map nav | Sticky blurred navbar |
| Gradient and rounded corners as images, sprites, sliding doors | Flat `bgcolor`, square table boxes | CSS gradients, `rounded-2xl`, soft shadows |
| Arial / Verdana / Lucida Grande / Tahoma at 11–12px; big headings at -1px tracking | `<font>` Verdana at -1/-2 | Inter / Geist, a giant hero |
| Links still underlined, brand blue, lighter visited | Per-site link and visited colours | Links styled away; buttons instead |
| Landing page: centred pitch, three-slice pill button, feature table, testimonials with names, trust seals | Homepage is the content or the tool | Hero → 3 cards → logo strip → pricing → FAQ |
| Inside pages: raw user content with counts, timestamps, "submitted by", tags | Editorial lists | Generic claims, no data |
| "NEW" labels, text "beta", orange RSS button, yellow notice box | Text bullets, "Updated hourly" | Pill badges, emoji bullets |
| Inline AJAX (vote, save), Lightbox, Flash demo video | Full reload for everything | SPA, fade-in-on-scroll |
| Footer: `<dl>` link columns or a short pipe row; © line; blog "powered by" credits | `Text \| Text` + one © line | Four-column mega footer |

## How it was checked

- **Research:** raw Wayback `id_` captures and their CSS for Digg, del.icio.us, Flickr, 37signals, MySpace, Twitter, Facebook, Apple, YouTube (head only), wordpress.org, and binarybonsai.com (K2). All are Dec 2006 – Jan 2008.
- **Test round (13 Nov 2026):** three agents built fictional pages from an earlier version of this doc, then compared them against real captures.
  - A Digg/del.icio.us-style site, against Digg 30 Dec 2006 and del.icio.us 26 Dec 2006.
  - A Kubrick blog, against binarybonsai 16 Nov 2006 and the Kubrick 2.0.5 source.
  - A beta startup page, against RTM Mar 2008, Mint Apr 2008 and Dropbox Jun 2008.

  Their findings are folded in above.
- **Method notes:**
  - The fetch tool re-serialises HTML: it drops the doctype and normalises case. Check the doctype in a real browser with `document.doctype`.
  - `id_` captures render without CSS or images, so screenshot the normal (non-`id_`) Wayback URL.
  - Wayback blocks plain curl. GitHub raw works.

## Limits

- **No real capture was seen rendered;** only the test builds were screenshotted.
- **Some sources are missing:** Mint's CSS (404), Facebook, Apple and YouTube CSS, and whether RTM's pill button was glossy.
- **The blog genre rests on one real capture** plus the theme's source.
- **Not checked:** Backpack, Highrise, Wufoo, Last.fm, Netvibes, Vimeo.
- **Tag case and attribute quoting are unverified.**
- **The revised doc has not had a second round of builds.**

## Sources

- **Wayback captures:**
  - Digg (30 Dec 2006, + `global.css`).
  - del.icio.us (26 Dec 2006).
  - Flickr (Dec 2006 / Jan 2007).
  - 37signals (Dec 2006 / Jan 2007, + `basic.css`).
  - MySpace (Dec 2006).
  - Twitter (Dec 2006, Jan 2008).
  - Facebook (Jan 2008).
  - Apple (Dec 2007).
  - YouTube (Dec 2006).
  - wordpress.org (Dec 2006).
  - binarybonsai.com (Nov 2006, Jan 2007).
  - Remember The Milk (Mar 2008).
  - Mint (Apr 2008).
  - Dropbox (Jun 2008).
- **WordPress 2.0.5 Kubrick theme source** (GitHub).
- **Ben Hunt, "Web 2.0 how-to design guide"**, webdesignfromscratch.com (2008 capture).
