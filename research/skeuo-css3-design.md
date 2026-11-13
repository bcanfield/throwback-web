# Late skeuomorphic / early CSS3 design: characteristics

The phase after [web2-design.md](web2-design.md): roughly 2010–2013. Use this doc to build a page that passes as one from about 2011–2012. For the earliest phase see [old-web-design.md](old-web-design.md).

- **Part 1:** shared rules.
- **Part 2:** rules for each genre: (a) an iOS/Mac app page, (b) a Bootstrap 2 startup page, (c) a textured blog or portfolio.
- **Part 3:** each trait against the phase before ("was" = Web 2.0) and the modern AI default ("vs.").

Marks: **(V)** verified in a real capture or source file; **(V-map)** verified by another agent in `web-phases-2009-2022.md` and not re-checked here; **(U)** unverified.

### Two failure modes, both seen in test builds

1. **Building the cartoon.** Three test builds (an indie iOS page, a Bootstrap 2 startup, a textured blog) each leaned on the brief's skeuomorphic vocabulary and overdid it:
   - a rendered iPhone with bezel and glare, where real pages used a flat screenshot with a drop shadow (Day One, Fantastical, Reeder, Clear);
   - gradient chrome on nav, buttons and inputs of a shadowed sheet, where Elliot Jay Stocks put the texture behind the page and kept the content flat, and Marco is flat;
   - the full `-moz-`/`-webkit-`/`-o-`/`filter` ladder on every button, where real 2011 CSS is patchy;
   - Lobster headings, and a Like and a Tweet button on every post.

   Linen, stitching and ribbons are still unseen in 11 real pages. Only Instagram (paper clips) and Gowalla (leather, V-map) used a literal motif, one each.
2. **Building it too tidy and too stock.** The builds had one clean stack: Bootstrap 2.3.2 with `.hero-unit`, 3-up, quotes, pricing and CTA; generic `#wrapper`/`#sidebar` markup; a clean head; hand-tidy CSS. Real pages were:
   - minified or inline CSS with a `*{margin:0;border:0;background:0}` reset, typos (`antialising`) and commented-out rules;
   - re-skinned Bootstrap (Mailgun's airmail stripes and `stamp.png`; Balanced's 42 `@font-face` rules);
   - CMS class names (`.odd_posts`, `.hentry`) and heads with leftover metas and scripts.

   Real nav, buttons and cards on app pages were also bitmap sprites, which the builds replaced with CSS.

---

## Part 1: Shared rules

### Head and document

- **The doctype splits by genre, not by year.** Read in a real browser unless marked:
  - **App pages:** HTML5 for Sparrow (Apr 2012), Reeder (13 Nov 2011), Fantastical (1 Dec 2011) and Clear (14 Mar 2012). XHTML 1.0 Strict for Things (Mar 2012) and Tapbots (Jul 2011). HTML 4.01 Transitional for Day One (29 Feb 2012, `loose.dtd`) and Instagram (Feb 2012, with `http-equiv` Content-Type and the title `instagr.am`). No doctype (quirks, `BackCompat`) for Path (Feb 2012), despite `<meta charset>`, a viewport and Mixpanel. Lean HTML5; let one in three be older.
  - **Startups:** HTML5 on 4 of 4 real pages: Mailgun (6 Dec 2012, lowercase `<!doctype html>`), Sentry (25 Dec 2012), DrinkableTap (2 Jan 2013), and Balanced (13 Jan 2013, `<!DOCTYPE HTML>`, source only, not browser-read). Bootstrap's own examples are HTML5 too. No quirks, no XHTML here.
  - **Blogs and personal sites:** split. HTML5 for Elliot Jay Stocks (10 Aug 2011), Marco.org (14 Oct 2011) and the Twenty Eleven theme (`header.php:11`, tag 3.2.1, source only). XHTML 1.0 Transitional for Shawn Blanc (Oct 2011, WordPress 3.0.4) and Tumblr (Nov 2011). Rule: self-built or WordPress 3.2+ gets HTML5; a WordPress 3.0-era theme or Tumblr's own page keeps XHTML Transitional.

  An XHTML doctype alone is not "too old" here. Every XHTML page above is from 2011 or earlier.
- **Viewport:** mostly absent. Sentry (25 Dec 2012), Mailgun (6 Dec 2012) and Balanced (13 Jan 2013) had no viewport meta; Sentry had one `@media` rule and Mailgun none, so Sentry is 940px wide and scrolls at 375px. Bootstrap-template pages (DrinkableTap), Path and Bootstrap 2.3.2 have `width=device-width, initial-scale=1.0`. Bootstrap 2.0.0's example had none, Dribbble had `width=1000` (V-map), and Sparrow only `@media (max-device-width: 768px){ body{zoom:90%} }`.
- **Head clutter is the norm.** Clear (Mar 2012): `class="no-js"`, `X-UA-Compatible`, `dns-prefetch`, schema.org `itemscope`, Modernizr, Typekit. Day One: `author` and `copyright` metas. Old WordPress-era sites: `imagetoolbar`, `revisit-after`, `distribution`, `robots` and keywords metas, plus Mint and ad scripts.

### Markup

- **HTML5 sectioning appears in 2012 pages** (`<header>`, `<nav role="navigation">`, `<article>`, `<footer role="contentinfo">` in Sparrow) but divs stay common: `#wrapper`, `#page`, `#shadow`, `#navi`, `#sidebar` (Things). Use the CMS's own class names where there is a CMS: Elliot Jay Stocks `.odd_posts` and `.archive_listing` (10 Aug 2011), WordPress `.hentry` and `.entry-content` (Twenty Eleven).
- **Image replacement is everywhere:** `.replace{display:block;overflow:hidden;text-indent:-999em;background:url(sprite.png) no-repeat}` (Sparrow). Logos, App Store buttons and nav are text-indented sprites.
- **Buttons and chrome are bitmaps on app pages** in 2011–12: Coda `<img src="img/nav-download.png" onmouseover="fadeOut(this)">`; Fantastical nav slices 91/92px and `container-top-sides.png`; Clear `app-store-button.png` 206×73. CSS3 buttons are for forms and secondary actions.

### CSS

- **Real CSS is minified or inline, and untidy.** Fantastical `master.css` (7 Oct 2011) is minified. Reeder and Day One are inline in the page. Expect a `*{margin:0;border:0;background:0}` reset, a typo like `antialising`, commented-out blocks, `/* DEFINITIONS */` headers with VERSION dates (Elliot Jay Stocks) and `!important`.
- **Width:** a centred fixed column. Sparrow 954px, Bootstrap 2 `.container` 940px, Clear 940px, Fantastical 804px, Instagram 810px, Day One 630px, Marco 620px, Gowalla 960 (V-map). Twenty Eleven is the exception: `#page` max 1000px, fluid. Fluid on news-style sites (Globe, breakpoints at 480, 620, 810 and 1400px).
- **CSS3 is prefixed, and unevenly.** The Sparrow `screen.css` (Apr 2012) ladder:

  ```css
  -moz-border-radius:3px; -webkit-border-radius:3px; border-radius:3px;
  -webkit-box-shadow:0 1px 1px #fff; box-shadow:0 1px 1px #fff;
  background:-webkit-linear-gradient(top,#fff,#e0e0e0);
  background:-moz-linear-gradient(top,#fff,#e0e0e0);
  background:-o-linear-gradient(top,#fff,#e0e0e0);
  ```

  Bootstrap 2.3.2 `.btn` is the long form (down to `filter: progid:DXImageTransform` and `*background-color`). But most real sheets were patchy:
  - Clear (`clear.005.css`, 23 Feb 2012): bare `border-radius`, `-moz-`/`-webkit-` shadows, and a `90deg` `-moz` gradient.
  - Fantastical: no `-o-` gradients.
  - Reeder (13 Nov 2011): `-o-` prefixes.
  - Elliot Jay Stocks `enrichment.css` (19 May 2011): radius with `-webkit-` and `-moz-` only.
  - Marco `main2.css` (15 Oct 2011): no CSS3 at all.

  Vary the prefix set per rule, and never write the full ladder on every element.
- **Radius is small:** 3px (Sparrow), 4px (Bootstrap navbar, Elliot Jay Stocks images), 6px (hero unit, Tumblr button). No pill-everything.
- **Letterpress is real but not universal.** A 1px white shadow under dark text on grey (Sparrow `0 1px 1px white`). Elliot Jay Stocks sets `text-shadow:1px -1px 1px rgba(255,255,255,.6)` on all of `body`. Marco has none; Twenty Eleven has one `text-shadow` in 2,670 lines. On dark fills the shadow goes up: `0 -1px 0 rgba(0,0,0,.25)` (Bootstrap `.btn-primary`). Hero text on a photo: `0 2px 1px rgba(0,0,0,.6)` (Sparrow).
- **Textures are bitmaps, at the page edge:** Sparrow body `#e6e6e6 url(bg-noise.gif)` and a `#main` paper sheet with `box-shadow:0 0 2px #666`; Fantastical and Reeder faint grey noise PNGs; Day One blue noise; Clear a blurred cafe photo; Shawn Blanc a repeating `background.jpg` on header, nav and footer; Elliot Jay Stocks a fixed paper `body.jpg` over a `repeat-x` `html.gif` and a `footer.jpg` tile, with the content on the open page. Gowalla `leather.jpg` and MailChimp `noise.png` (V-map). Marco and Twenty Eleven have none.
- **Type:** Helvetica Neue at 13px/18px (Path, Bootstrap 2.0–2.2), 15px weight 300 (Twenty Eleven). Lucida Grande, Verdana (Things, Tapbots 12px), Day One 11px `"arial"`. Georgia on blogs and news (Marco 16px, Globe). **Web fonts are Typekit, not Google Fonts or Cufón** (none seen on the three blogs): Sparrow `proxima-nova-1, proxima-nova-2`, Fantastical and Clear `ff-dax-web-pro`, Elliot Jay Stocks `ff-tisa-web-pro-1, ff-tisa-web-pro-2, Georgia, Times` (`typography.css`, 19 May 2011), Shawn Blanc `gesta`, `proxima-nova`, `warnock-pro`. Sparrow adds a `.wf-active` rule bumping weights to 600.
- **Responsive is an add-on or absent.** Bootstrap 2 ships `bootstrap-responsive.css`. The Globe (Oct 2011) uses `respond.min.js` and `@media screen and (min-width: 480px)`. Marco has breakpoints at 680px and 520px. Many startups have none (see Viewport).

### JavaScript

- **jQuery 1.x:** Sparrow 1.7.1, Day One 1.4 with **Fancybox 1.3.4** (V, now seen). Other small plugins: `jquery.easing.1.3`, `jquery.tweet`, `jquery.transit`, a Globe carousel. Nivo Slider and `Cufón` remain (U).
- **Social is sparse.** Sparrow: `addthis` CSS and a Facebook Like iframe `width:120px; height:20px` in the footer. Globe: `plusone.js`. Marco: an Instapaper "Read Later" iframe. Elliot Jay Stocks: `plusone.js` only. Twenty Eleven: none. Do not put Like and Tweet on every post. A Tweet button is (U), and today's Twitter `widgets.js` renders "X Post", so don't use it.

### Avoid

- **Too old:**
  - Tables for layout and `<font>`.
  - Corner GIFs, and 1px-row rounded corners.
  - `-moz-border-radius` alone.
  - A fixed 750px column.
  - Image-only gradient chrome on blogs and startups (app pages do use sprites).
- **Too new:**
  - Unprefixed-only `border-radius` or `linear-gradient`.
  - Flat fills with no shadows on app and startup pages.
  - Font Awesome, Montserrat, Inter, `rem`, flexbox, grid, and a hamburger outside Bootstrap's own `btn-navbar`.
  - Bootstrap 2.3.2 (14px/20px, released Mar 2013) on a page dated 2012. Use 2.0–2.2 (see 2b).
- **Moved out of "too new", because real pages had them:**
  - **Icon fonts:** Sentry used Pictos (`get.pictos.cc`) on `getsentry.com/welcome`, 25 Dec 2012.
  - **A photo hero:** Clear's full-width blurred photo (14 Mar 2012) with a 940px column; DrinkableTap's container-width photo hero (2 Jan 2013) with a 200-weight 30px headline; Path's video background (Feb 2012). Sentry's own hero was a flat `#f04618` with a real dashboard shot.
- **The cartoon:**
  - A ribbon on every card.
  - A rendered phone with bezel and glare.
  - A gel app icon on a wooden desk. (Fantastical's realistic icon in the header is the one glossy item seen.)
  - Linen plus leather plus paper together.
  - Lobster or a stamp-logo header on a Georgia body.
  - Gradient chrome on every element.

  Pick one texture and put it at the page edge.

---

## Part 2: By genre

### (a) iOS/Mac app marketing page (Sparrow, Things, Instagram, Tapbots, Coda, Reeder, Day One, Fantastical, Clear)

- **Layout:** a centred sheet 630–954px wide on a textured body. Reeder (13 Nov 2011) is a 40/60 split on noise PNGs with CSS in the page. Fantastical (1 Dec 2011) is an 804px column with a sprite nav and `container-top-sides.png`. Day One (29 Feb 2012) is a 630px sheet on blue noise. Clear (14 Mar 2012) is a 940px column over a full-width blurred photo.
  - Sparrow Apr 2012: a 954px header with a logo sprite and right-floated nav, then a 345px `#featured` band (`#16356C`, tiled image, white 28px h1 with `0 2px 1px rgba(0,0,0,.6)`, screenshot at `bottom:0; right:69px`). Keep the screenshot inside the band; the build's phone overflowed onto the nav.
- **Hero and CTA:** one product shot, one sentence. Sparrow "Get mail done"; Things "Task management has never been this easy."; Fantastical "Meet your new assistant."
- **Download buttons are bitmaps.** Sparrow's are 196×56 sprites with a hover at `-170px`. Things stacks three tall buttons ("Download Things 1.5.4 / Mac OS X 10.6 or later", "Purchase … $49.95", "Now available on the Mac App Store"). Clear uses `app-store-button.png` at 206×73.
- **Mockups: a flat screenshot with a drop shadow, no bezel,** on all four of Day One (`dayone-devices.jpg`), Fantastical (`fantastical-screenshot.png`), Reeder and Clear. Instagram (Feb 2012) used an iPhone image (281px) left, a free badge at `top:20px; left:-35px`, and a 509px right column with `tabBackground.png` and `paper-clips.png` over brown `#563c13` text. Day One's images are missing from Wayback, so only its CSS was read.
- **Features:** three 48px sprite icons with a 17px h2 and 14px grey text (Sparrow). Things: a two-column list of 16 small PNG icons. Fantastical: a feature list with "Coming Soon" items, a press-kit link, a newsletter box.
- **Proof:** press quotes as logo sprites that swap the quote text (Sparrow: Ars, Cult of Mac, DF, TechCrunch). Things: Macworld awards in a sidebar. Coda: an Apple Design Awards badge.
- **Footer is short:** Day One a 10px `<small>` "© 2011 Bloom Built"; Fantastical a logo and ©; Things `Contact | Impressum`.

### (b) Bootstrap-2-era web startup or SaaS page

- **Pin the version to the date.** All four real 2012 pages had 13px/18px body, so Bootstrap 2.0–2.2: Mailgun `site.css` (14 Nov 2012), Sentry `global.min.css` (22 Jan 2013), DrinkableTap `bootstrap.min.css`, Balanced `bootstrap-2.0.*.css` (13 Jan 2013). Bootstrap 2.3.2 (14px/20px) is a 2013 look. Bootstrap was often folded into a site sheet (`ba-bs.css`, `dt-bs.css`, `mg.css`).
- **Real startups rarely used `.hero-unit`.** Sentry and Mailgun wrote their own `header` / `#header` and used only grid classes (`span4 feature`, `span5 offset1`, `span9`, `span10`). Use the stock template below only for a Bootstrap-showcase page; no real startup page seen used it unchanged.
- **Stock hero template** (v2.0.0 and v2.3.2 `docs/examples/hero.html`, V). `<!DOCTYPE html>`, `<meta charset="utf-8">`, "Le styles" comments, the html5shim conditional, apple-touch icons, `body{padding-top:60px}`:

  ```html
  <div class="navbar navbar-fixed-top"><div class="navbar-inner"><div class="container">
    <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse"> ...3 x <span class="i-bar"> (2.0) ...
    <a class="brand" href="#">Project name</a>
    <div class="nav-collapse"><ul class="nav"><li class="active"><a href="#">Home</a></li>...
  <div class="hero-unit"><h1>Hello, world!</h1><p>...</p>
    <p><a class="btn btn-primary btn-large">Learn more &raquo;</a></p></div>
  <div class="row"><div class="span4"><h2>Heading</h2><p>...</p><p><a class="btn" href="#">View details &raquo;</a></p></div> x3
  <hr><footer><p>&copy; Company 2012</p></footer>
  ```

  2.3.2 CSS: hero unit `padding:60px; background:#eee; border-radius:6px; font-weight:200`; `.btn-primary` `#0088cc→#0044cc` (2.0: `#0088cc→#0055cc`, V-map); `.span4` is 300px in the 940px grid.
- **Skin it heavily, as real pages did.**
  - Mailgun (YC S10, 6 Dec 2012): airmail-stripe borders, `paper.png`, `stamp.png`, `barcode.png`, a 16-column grid, rendered devices.
  - Balanced: 42 `@font-face` rules and `background_website3.png`.
  - Sentry (25 Dec 2012): a real dashboard screenshot on a flat `#f04618` hero.
  - DrinkableTap (2 Oct 2012): photo hero. Its CSS capture is Aug 2013, a weak date.
  - Path (Feb 2012): 43 `border-radius`, 12 gradients, 46 `@media` rules, Mixpanel, Optimizely, Chartbeat, a "Get the app" CTA over a video. Use a still for 2011.
- **Content:** a 3-up feature row, "Sign up" and "Learn more" buttons, a short pricing table. **Logo strips and "Customers" bands are period:** Mailgun (6 Dec 2012) and YC, UserVoice and 37signals logos. Custom art beats a generated screenshot and flat icons.
- **Mobile:** viewport and responsive CSS are optional on a 2012 page (Part 1). If added, test at 375px: the build's fixed-width hero overflowed.

### (c) Textured personal blog or portfolio

- **Texture belongs behind the page; the reading area is flat.** Elliot Jay Stocks (Harmony CMS, not WordPress, 10 Aug 2011): `layout.css` puts one fixed background image on `html`/`body`, with content on the open page; `enrichment.css` has `-webkit-`/`-moz-` only, a 4px radius and `rgba` backgrounds on `img`; the letterpress shadow sits on all of `body`. Shawn Blanc (Oct 2011) is the dark variant: body `#393831`, text `#a0a08b`, 13px, headings `#bebea6` in `warnock-pro, Georgia, serif` at 22.75px, a repeating `background.jpg` over `#242320` on `#header`, `#navigation` and `.ancillary` only, no radius, no shadow.
- **Some blogs are plain.** Marco.org (custom, not Tumblr, 14 Oct 2011, `main2.css`): a flat `#372312` band, Georgia 16px, a 620px column, breakpoints at 680px and 520px, no images, no CSS3, an Instapaper iframe. Twenty Eleven 1.2 (tag 3.2.1, `style.css`): `body` `#e2e2e2`, 15px Helvetica Neue weight 300, `#page` max 1000px, paired `-moz-`/`-webkit-box-shadow`, one `text-shadow`.
- **Fingerprints are the CMS's.** Shawn Blanc: `<meta name="generator" content="WordPress 3.0.4">`, theme `/wp-content/themes/threefifty/`, FancyZoom, Typekit, Mint, a fusionads pull, `urchin.js`. Twenty Eleven uses `.hentry`, `.entry-content`. Elliot Jay Stocks uses `.odd_posts`, `.archive_listing`.
- **Type:** serif throughout (Elliot Jay Stocks Tisa, Marco Georgia). **Lobster over a Georgia body is the pastiche tell.** Body 13–16px.
- **Tumblr (Nov 2011):** the sign-up page is XHTML Transitional with Prototype, a `#3c5a76` body with `status_bg.png` and a 6px-radius image-backed "Start posting!" button. A Tumblr blog theme is (U): no source was read.
- **Sharing:** none, `plusone.js`, or an Instapaper link. Not a Like and a Tweet on every post.

---

## Part 3: Traits, before and after

| Trait (2010–2013) | Was (Web 2.0, 2004–2009) | vs. modern AI default |
|---|---|---|
| Fixed 630–960px column on a textured body (noise, leather, a blurred photo); texture at the page edge, flat reading area | Fixed 750–840px on a pale grey or gradient canvas | Full-bleed responsive sections on flat white or dark |
| `border-radius` 3–6px, `box-shadow`, patchy prefixes (not the full ladder), sometimes none at all | Corners and gradients from images; no `box-shadow` | `rounded-2xl`, soft large shadows, one unprefixed gradient |
| Flat screenshot with a drop shadow; Typekit; paper clips on one page | Tilted product graphic | A CSS phone frame, a logo strip |

## How it was checked

- **Research (13 Nov 2026):** Wayback captures, doctype and `compatMode` read in a real browser with `document.doctype`, stylesheet rules read from the loaded sheet. Sparrow, Things, Instagram, Boston Globe, Tapbots, Tumblr, Shawn Blanc, Path, Panic Coda (Jun 2011 to Apr 2012), and Bootstrap v2.0.0 and v2.3.2 from raw GitHub.
- **Test round (13 Nov 2026):** three agents built pages from the earlier version of this doc, then compared them against real captures. Their findings are folded in above.
  - An indie iOS page ("Foxglove"), against Reeder (13 Nov 2011), Day One (29 Feb 2012), Fantastical (1 Dec 2011, `master.css` 7 Oct 2011) and Clear (14 Mar 2012, `clear.005.css` 23 Feb 2012).
  - A Bootstrap 2.3.2 startup ("Quillfold"), against Mailgun (6 Dec 2012, `site.css` 14 Nov 2012), Sentry (25 Dec 2012, `global.min.css` 22 Jan 2013), DrinkableTap (HTML 2 Jan 2013) and Balanced (13 Jan 2013).
  - A WordPress 3.2.1 designer journal ("Wren & Ink"), against Elliot Jay Stocks (10 Aug 2011), Marco.org (14 Oct 2011, `main2.css` 15 Oct 2011) and Twenty Eleven 1.2 (GitHub raw, tag 3.2.1).
- **Method notes:**
  - Wayback ignores query strings and mixes dates on subresources. Tumblr's capture loaded 2013-era CSS and JS beside 2011 files. Sentry's CSS was four weeks after its HTML, and DrinkableTap's was eight months after. Check each asset's timestamp.
  - The fetch tool drops the doctype (it hid Elliot Jay Stocks' HTML5). Read it in a browser.
  - Plain `id_` captures show no CSS. Wayback blocks plain curl; GitHub raw works.
  - Wayback loses image hosts and JS-built bodies (Day One's S3 images, Clear's `#main`, both 2012), so visual checks need another capture. Its screenshots were of capture pages, not full pages.
  - Test builds screenshotted from `file://` miss viewport behaviour, and a live Twitter `widgets.js` shows today's "X Post".
- **The revised doc has not had a second round of builds.**

## Limits

- **Not checked on a real page:** Cufón and sIFR fading out, Nivo, linen or stitched UI, ribbon banners, the Google Fonts API in 2011–12, the black App Store badge itself.
- **Not fetched:** Gowalla, MailChimp and Dribbble (V-map only), Forrst, Things', Coda's and Tapbots' CSS, the Globe's full CSS.
- **No ThemeForest template, no Tumblr blog theme source.** No Bootstrap-2 startup was checked in a real mobile browser beyond Sentry's 375px width; behaviour of the rest on phones is unverified.
- **Balanced's doctype** is from source, not a browser. IE conditional comments and self-hosted `@font-face` were not checked on the blogs.

## Sources

- **Wayback captures:** every site and date named above.
- **GitHub raw:** `twbs/bootstrap` tags `v2.0.0` and `v2.3.2`; `wordpress-develop` tag 3.2.1 (Twenty Eleven).
- **Another agent's notes:** `web-phases-2009-2022.md`, section 1 (Gowalla, MailChimp, Dribbble, Bootstrap 2.0.3).
