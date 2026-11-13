# Responsive flat design: characteristics

The phase after [skeuo-css3-design.md](skeuo-css3-design.md): roughly 2013–2016 (the phase map, `web-phases-2009-2022.md`, gives the same dates). Use this doc to build a page that passes as one from about 2014–2015.

- **Part 1:** shared rules.
- **Part 2:** rules for each genre: (a) a full-bleed-hero startup or agency one-pager, (b) a small-business theme site (Avada, ThemeForest), (c) a Medium-style editorial or blog post.
- **Part 3:** each trait against the phase before ("was" = 2010–2013 skeuomorphic/CSS3) and the modern AI default ("vs.").

Marks: **(V)** verified in a real capture or source file, named; **(U)** unverified. Three test builds (13 Nov 2026) were compared with real captures; their findings are folded in and each keeps its source.

### Two failure modes, both seen in test builds

1. **Cloning the template, or the cartoon.** The first brief gave exact Start Bootstrap values, and the one-pager build came out as a recolour of the "Agency" template (flat-1). The templates are a demo, not the web. Real one-pagers were product-led: a laptop mockup (Squarespace), a video thumbnail with a signup form (Slack), a customer-story caption. They also lacked the cartoon: no dark overlay, no parallax on any hero (V, below). Template values are in a "what the templates did" note, not a default.
2. **Building it too clean, too light and fully responsive.** The model's default is mobile-first, one tidy grid, 5 scripts and a fresh footer. Real pages were:
   - **Heavy and noisy.** An Avada small-business site had 43 scripts, 20 stylesheets and 82 inline `style=` attributes; the build had 5 and 6 (V, charterbayhomes, 29 Apr 2015). Slack, Squarespace and InVision carried analytics, Optimizely, Olark and popup banners (V).
   - **Desktop-first or not responsive.** InVision, Jan 2015: `<meta name="viewport" content="width=1024" />` (V). Airbnb, Oct 2014: `width=1045`; Apple iOS 7, Oct 2013: `width=1024` (V).
   - **Stale and untidy.** A "© 2009-2014" footer on an Apr 2015 page, `xmlns` leftovers on `<html>`, theme widgets nobody removed (V, charterbayhomes).

---

## Part 1: Shared rules

### Head and document

- **Doctype `<!DOCTYPE html>`, standards mode.** Checked in a real browser (`document.URL` matched the capture; `compatMode` CSS1Compat) on Slack 17 Nov 2014, Squarespace 15 Nov 2014, InVision 15 Jan 2015, charterbayhomes 29 Apr 2015, littlebigbikes 10 Mar 2015, restaurant-lastsupper.de 27 Jun 2015 and Medium Sep 2015 (V, flat-1, -2, -3). The case varies (Squarespace is lowercase `<!doctype html>`; InVision has two blank CRLF lines before it).
- **The `<html>` tag may still be XHTML-era.** All three Avada sites: `<html xmlns="http://www.w3.org/1999/xhtml" lang=".." xmlns:og=".." xmlns:fb=".." prefix="og: ..">` (V). A clean `lang="en"` is the template's form. Slack, InVision and Squarespace carried conditional-comment classes on `<html>` (V).
- **Head order in the templates (V, Agency):** `<meta charset="utf-8">`; `X-UA-Compatible`; viewport; empty `description` and `author`; a title like "Agency - Start Bootstrap Theme". Real themes often lead with `<meta http-equiv="Content-Type" ...>` (Avada sites, Medium; V).
- **Viewport on real sites:**
  - Slack Mar 2015: `width=device-width, initial-scale=1.0, maximum-scale=1.0` (V).
  - Medium 2014–15: `width=device-width, initial-scale=1, maximum-scale=1` plus `user-scalable="no"` (V).
  - Squarespace Nov 2014: the same plus `minimal-ui` (V).
  - Google Design Jan 2015: `initial-scale=1, minimum-scale=1, width=device-width, height=device-height` (V).
  - InVision Jan 2015: `width=1024` (V).
- **Stylesheets and fonts:** a theme file, then fonts by `<link>`, not `@import`.
  - Agency: `http://fonts.googleapis.com/css?family=Montserrat:400,700`, plus Kaushan Script, Droid Serif and Roboto Slab (V). Plain `http://`.
  - Slack: `https://fonts.googleapis.com/css?family=Lato:300,400,700,900` (V).
  - Paid fonts: `//cloud.typography.com/...` (Gotham and Chronicle on Squarespace; Hoefler on Stripe; V). InVision used brandon-grotesque, Charter Bay Typekit (V).
  - Avada loaded its own `@font-face`, e.g. `'PTSansRegular'` (V).
- **IE shims:** `<!--[if lt IE 9]>` with html5shiv 3.7.0 and respond.min.js 1.4.2 from `oss.maxcdn.com` in the templates (V, Agency, Creative). Avada shipped `html5shiv.js`, `respond.js` and `excanvas.js` from its theme folder, plus `jquery-migrate` (V).

### Markup

- **HTML5 elements** in the templates: `<nav>`, `<header>`, `<section id="services">`, `<footer>`. Real pages mix them with div soup: Squarespace used full-screen `section.scene` blocks with no container (V).
- **What the templates did (V, Agency, Font Awesome 4.1.0):** Bootstrap 3 grid `.container > .row > .col-md-4`, and the icon badge `<span class="fa-stack fa-4x"><i class="fa fa-circle fa-stack-2x text-primary"></i><i class="fa fa-laptop fa-stack-1x fa-inverse"></i></span>`. This is the template's habit. Avada, Slack and Squarespace did not use it.

### CSS

- **Bootstrap 3.3.0 defaults (V, `bootstrap.css`, Agency tag v1.0.0):** `.container` 750/970/1170px with 15px padding; body Helvetica Neue 14px/1.42857143, #333; links #428bca; `.btn` 6px 12px; `.navbar-default` #f8f8f8 on #e7e7e7. No gradients or letterpress shadows; Bootstrap 3.0.0 (19 Aug 2013, V) already dropped them. This applies only to sites that load Bootstrap. **Avada 3.7 does not**: its `style.css` has a "Needed Styles From Bootstrap" subset plus its own `fusion-column` grid, and no `.container` (V, charterbayhomes `style.css`, 15 Mar 2015).
- **Breakpoints are mostly desktop-first `max-width`:**
  - Slack 1680 / 1024 / 767 / 640 / 479 (V, 17 Nov 2014).
  - Squarespace 1200 / 1024 / 768 / 480 (V, 15 Nov 2014).
  - Avada `media.css` 800 / 767 / 710 / 782 (V, charterbayhomes, 15 Mar 2015).
  - Medium 1000 / 800 / 680 / 500 (V, Aug 2014); Stripe 1012 / 479 (V, Jun 2015); MDL 1.0 850 / 760 / 840 / 1024 (V, Jul 2015).
  - Only the Bootstrap templates are mobile-first `min-width` 768 / 992 / 1200 (V).
- **Flat fills, one loud accent** (template values, V): Agency #fed136 on #222 and #f7f7f7; Creative #f05f40; Flat UI 2.0.0 (May 2013) #1abc9c, #3498db, #34495e, #e74c3c. Real palettes were less loud: Charter Bay beige #f7f5f0 with tan #cdc2af borders, navy and gold; littlebigbikes one green; InVision #ff3366 (V).
- **Hero images:** `background-size: cover` with `-webkit-`, `-moz-` and `-o-` kept beside it, `background-position:center` (V). A photo may be pre-darkened or blurred in the file instead of by CSS (Slack; V).
- **Shadows and gradients: not absent.**
  - Avada's `.fusion-button` has `box-shadow:0 1px 1px`, `text-shadow:0 1px 0 #fff` and a 1px border; `style.css` has 354 `box-shadow` and 92 gradient declarations (V, charterbayhomes).
  - Slack's button: `border-bottom:2px solid #194ba3` and a text-shadow, a raised "flat" button (V). Slack hero text: `text-shadow:0 1px 10px rgba(0,0,0,.5)` (V).
  - Material: MDL 1.0 `box-shadow: 0 2px 2px 0 rgba(0,0,0,.14), 0 3px 1px -2px rgba(0,0,0,.2), 0 1px 5px 0 rgba(0,0,0,.12)` (V, `material.css`).
  - Only the Bootstrap 3 and Start Bootstrap defaults are shadow-free. Long shadows (2013) were not found (U).
- **Buttons (V):**
  - Agency 3px radius, solid #fed136; Bootstrap 4px; Flat UI 6px.
  - Squarespace: a pill, `border-radius:50px; letter-spacing:1px`.
  - InVision: 5px radius, #ff3366. littlebigbikes: round outlined pills.
  - **Ghost buttons are common:** Slack `#landing #signin_link` is transparent with `border:1px solid white`, .25rem radius, alone top right (17 Nov 2014); Squarespace `.getstarted` is `border:2px solid #666; background:transparent; border-radius:0` inside the menu panel (15 Nov 2014); InVision has `.button.outline`; Stripe's `.button.secondary` is `rgba(255,255,255,.5)` beside a filled button (Jun 2015). Not every hero has one.
- **Type:**
  - Templates: uppercase Montserrat 700 headings with a Droid Serif or Merriweather italic lead-in; Open Sans (V, Agency, Creative).
  - Real: Lato (Slack); Gotham with Chronicle (Squarespace); brandon-grotesque (InVision); Roboto (MDL, Google Design); Avada body `13px/20px 'PTSansRegular'` (V, charterbayhomes `style.css`), with an Italianno script H1, Lato and uppercase serif nav on Charter Bay.
  - **Real type is often in rem:** Slack `.section.splash h1{font-size:7rem}` (V). Templates use px (body 14px, `p` 16px, hero h1 50px rising to 75px at ≥768; Creative `fitText` 35–65px; V).

### JavaScript

- **Template stack (V, Agency, Creative):** jQuery, `bootstrap.min.js`, `jquery.easing 1.3`, `classie.js`, `cbpAnimatedHeader.js`, `jqBootstrapValidation.js`; Creative adds `jquery.fittext.js`, `wow.min.js` with `animate.css`, `scrollspy` and `affix`. Smooth scroll is `$('a.page-scroll').bind('click', ...)` with `.animate({scrollTop: ...}, 1250, 'easeInOutExpo')`. `bind`, not `on`.
- **Real pages carried far more:** analytics, Optimizely, Olark, popup banners (Slack, Squarespace, InVision; V); on Avada, Slider Revolution, LayerSlider, UberMenu, Jetpack, contact-form-7, Typekit and `retina.js` (V). Fade-in on scroll was not found in CSS or markup on the three one-pagers; their JS was not read (U).

### Avoid

- **Too old:**
  - XHTML doctypes, `<center>`, table layout.
  - Prefixed gradient buttons, letterpress shadows, leather and noise textures, Glyphicon PNGs, sprite icons.
- **Too new:**
  - CSS grid, `gap`, `clamp()`, `system-ui` stacks, custom properties.
  - Mobile-first flexbox as the main layout.
  - Skewed section edges, diagonal gradients, illustration-heavy sections (2016–2019; Stripe's `108deg` hero gradient in Jun 2015 is a niche early sign, V).
  - Inline SVG icons, dark mode, `backdrop-filter`, `loading="lazy"`.
- **The template clone:** an Agency-style hero (uppercase Montserrat, 3px-radius solid button, `.container` sections, Font Awesome badge circles) as the default for every one-pager.
- **Too clean:**
  - 5 scripts and 6 stylesheets, a pristine `lang="en"`, a fresh copyright and chirpy copy.
  - Fully responsive Bootstrap on every page.
  - A fake generated skyline or stock-looking hero where real ones used product mockups or darkened photos.
- **Too cartoonish:** a dark overlay and parallax on every hero (none found), neon flat-UI palettes.

---

## Part 2: By genre

### (a) Full-bleed-hero startup or agency one-pager (Slack, Squarespace, InVision; templates Agency, Creative)

Real pages first. Do not start from the template.

- **Slack, 17 Nov 2014** (V, `rollup-homepage_1416017571.css`):
  - A video splash: an `h1` with a quote, a thumbnail with `srcset`, an email + company form, "Sign up for Free".
  - A pre-darkened, blurred photo, with the `text-shadow` above. No CSS overlay.
  - Phone: the form moves behind a button into a full-screen overlay (`form_overlay`).
  - Lato; heading in rem; a ghost "Sign in" top right.
- **Squarespace, 15 Nov 2014** (V, `site.css`):
  - Full-screen `section.scene` blocks, no container, a laptop mockup.
  - `.scrim{background-color:rgba(0,0,0,0)}` and `data-scrim-value="0"` on 18 of 18 scenes: the overlay exists in markup and is off.
  - **A desktop hamburger:** `.navigation-trigger` ("Menu" plus an icon) is `inline-block`, 91×71, at 1280px wide. It opens a panel holding a ghost `.getstarted`.
  - The only `background-attachment:fixed` is on an iPad icon. Pill buttons.
- **InVision, 15 Jan 2015** (V, HTML only): `width=1024`, so not responsive; brandon-grotesque; `.button.outline`; #ff3366 buttons. Its `screen.css` capture is 21 Mar 2014, so its overlay and hero CSS were not readable.
- **Parallax:** none on any of the three heroes. Parallax belongs to the Avada bands (genre b), not to these.
- **What the templates did** (V, source, Agency Oct 2014, Creative Apr 2015):
  - Skeleton: fixed navbar, `<header>` hero, `#services`, `#portfolio` (light grey), `#about` timeline, `#team`, a client-logo row, `#contact`, footer.
  - Nav transparent over the hero at ≥768, shrinking to `padding:10px 0` on `#222` after a scroll offset.
  - Agency hero: `cover`, no overlay, Droid Serif italic lead-in 22px (40px at ≥768), Montserrat 700 uppercase heading 50px (75px), one `.btn-xl` (20px 40px, 3px, #fed136), padding 100/50px on phone and 300/200px at ≥768.
  - Phone: navbar collapses to three bars; `.col-md-4` stacks below 992px.

### (b) Small-business theme site (Avada 3.7, 2014–2015)

- **Where it was found:** the Avada showcase page (Wayback, 12 Aug 2015) lists real sites. Charter Bay Home Builders (Tampa, 29 Apr 2015, Avada 3.7.1), littlebigbikes.com (10 Mar 2015, Avada 3.7.3, WooCommerce 2.3.5, WP 4.1.1) and restaurant-lastsupper.de (27 Jun 2015, theme folder renamed `/template/`) were read (V). The Avada demo (theme-fusion.com/avada, 1 Jul 2014 and 2 Jun 2015) shows WordPress 3.9.1, WooCommerce 2.1.11, Slider Revolution 4.5.4 and `data-spy="scroll"` on `<body>` (V).
- **Layout:** Charter Bay is about 950px wide at 1920 (screenshot only; U for CSS). No Bootstrap `.container`.
- **Markup fingerprint** (V): `fusion-megamenu-holder`, `avada-row`, `fusion-button button-default button-medium`, `fusion-animated`. Body classes like `no-tablet-sticky-header no-mobile-totop layout-wide-mode`.
- **Bands carry inline style** (V, Avada demo): `class="fusion-fullwidth fullwidth-box hentry" style="background-attachment:fixed; background-color:#f8f8f8; background-image:url(...); background-size:cover; ..."`. That fixed attachment is the parallax.
- **Real heroes and palettes:**
  - Charter Bay: one full-width photo with a translucent caption bar, no button.
  - littlebigbikes: green accent, outlined pill buttons; its slider area was blank in the capture (probably a Wayback artefact).
- **Footer:** Charter Bay still showed "© 2009-2014 | All Rights Reserved" in Apr 2015, with Recent Posts and Recent Tweets widgets. littlebigbikes: "Copyright 2015", a share sidebar, a "Connect With Us" band (V).
- **At phone width** (V, Charter Bay): a "Go to..." select plus a "MENU" bar, a hero scaled down uncropped (~90px tall), and icon-box headings wrapping to four lines beside a small image. Not a clean hamburger.

### (c) Medium-style editorial / blog post (Medium, Signal v. Noise, Ghost, 2014–2015)

- **Medium: no hero, no nav, no site logo** on a post. The byline (avatar, green name, "Jan 5 · 8 min read") sits **above** the title, which is a plain 36px `h3`. No tag chips; a sticky recommend/count rail and Follow markup instead (V, Medium post of 5 Jan 2015, capture 6 Sep 2015, `20150906061327`, computed and screenshot).
- **Medium computed type (same capture):**
  - `p`: Georgia stack, **22px/33px**, `rgba(0,0,0,.8)`, letter-spacing .16px, margin-bottom 30px. The Aug 2014 CSS had `letter-spacing:-0.02em` and `text-rendering:optimizeLegibility`; the sans stack was `"jaf-bernino-sans","Lucida Grande",...`.
  - Column: 700px. At 375px: `p` **20px/28px**, h3 26px, column 330px (20px margins). The pull quote loses its `-160px` margin.
  - Headings (Aug 2014 CSS): `h3` 36px/1.2 bold; `h2` 60px/1 at -0.04em.
  - Serif accents `"freight-text-pro",Georgia,...`: blockquote italic, `border-left:3px solid rgba(0,0,0,.8)`, `padding-left:20px`, `margin-left:-23px`, hanging flush at the viewport edge on a phone. Pull quote 32px italic centred, `margin:48px -160px`. **Figure captions are italic serif in the left margin** (screenshot).
- **Markup** (V): `article.postArticle > section.postWrapper > .postField--body > section.section--first > .section-inner.layoutSingleColumn > h3.graf--h3`, 4-hex `name` on every block, `figure.graf--figure` with `aspectRatioPlaceholder`.
- **Signal v. Noise, 3 Feb 2015** (V, `20150203054927`, CSS `application-21141054…css` same timestamp, computed): kepler-std (Typekit) **21.6px/34.56px** (1.6), #333, paragraph margin 0 with `text-indent`, column 660px, centred acta-display 45px h1, and a script-like italic "Jamis wrote this on…" line.
- **Ghost blog, 1 Jun 2015** (V, `20150601043403`, a heavily customised theme): Open Sans **16px/26.4px**, #3c4043, column 619px.
- **Ghost Casper 0.9.0** (V, `assets/css/screen.css`): Droid Serif 20px/1.6em, #3A4145, 700px, blockquote `.4em` left border. A drop cap was also seen (details not recorded; U).
- **Do not invent a hybrid** header (title, subtitle, byline) that matches no real site.

---

## Part 3: Traits, before and after

| Trait (2013–2016) | Was (2010–2013) | vs. modern AI default |
|---|---|---|
| Viewport `width=device-width, initial-scale=1`, but many sites desktop-first `max-width` or fixed (`1024`, `1045`) | None, or a fixed width | Mobile-first, `clamp()`, fluid type |
| Product-led hero: mockup, video thumbnail, or a customer-story photo; text-shadow, no overlay | Fixed 940–960px column on a textured body | A gradient-mesh hero with a pill button |
| Solid fills, one accent, plus real shadows and 1px borders on theme buttons | Gradient buttons, letterpress shadows, leather and noise | `slate` neutrals, soft shadows, one tinted accent |
| Ghost, pill or raised buttons; 3–6px radius (Material: layered shadow, FAB) | 3–6px radius plus gradients, all prefixed | `rounded-2xl` plus soft large shadows |
| Lato, Gotham, brandon, Open Sans, PT Sans at 13–16px; rem on some | Helvetica Neue 13px, Georgia headings | Inter or Geist, a giant `text-6xl` hero |
| Font Awesome 4 `<i class="fa ...">` | Sprites, Glyphicon PNGs | Inline SVG (Lucide, Heroicons) |
| Hamburger below 768px; a "Menu" trigger even on desktop (Squarespace); a "Go to..." select on Avada phones | Horizontal nav, image-replaced links | Sticky blurred navbar |
| Long-scroll one-pager with `#anchors`, or full-screen scenes | Multi-page site, tabs | Stacked sections, scroll-snap, fade-in |
| 40+ scripts, 20 stylesheets, widgets, analytics, popups, stale footer years | jQuery 1.4–1.9, small plugins | A framework, `IntersectionObserver` fades |
| Medium: 700px column, 22px/33px Georgia, byline above title, no hero | Textured blog, WordPress theme | `max-w-prose`, a sticky table of contents, tag chips |

## How it was checked

- **Research (13 Nov 2026):** raw Wayback `id_` captures (head, key CSS) of the exemplars in Sources, plus GitHub source for the templates and frameworks.
- **Test round (13 Nov 2026):** three agents built fictional pages from the first version of this doc, then compared them with real archived pages. Their findings are folded in above.
  - A one-pager (Bootstrap 3.3.1, jQuery 1.11.1, Font Awesome 4.2.0) vs Slack, Squarespace and InVision. It came out a recolour of Agency.
  - A dentist site ("Brightwater Family Dental"; Bootstrap 3.3.5, Owl 2, WOW) vs Charter Bay, littlebigbikes and restaurant-lastsupper.
  - A Medium-style post vs Medium 2015, Signal v. Noise and Ghost.
- **Method notes:**
  - **Browser method:** open a session, `browser_fetch` the `id_` URL, then `browser_evaluate` (`document.doctype`, `compatMode`, computed styles). Confirm `document.URL` equals the capture. For the Medium check, the non-`id_` URL was opened. This replaces the old "fails" note.
  - **Wayback rate limit:** a 15–20s gap between requests worked.
  - **CSS can predate the HTML:** InVision `screen.css` was 21 Mar 2014 vs HTML 15 Jan 2015, and was not used. Check every `?ver=` and CSS capture timestamp against the page's date. Charter Bay's CSS was 15 Mar 2015 at the same `ver=3.7.1`.
  - **Finding real sites:** the Avada showcase page and the Wayback availability API.
  - The fetch tool re-serialises HTML and drops the doctype; use the browser for that. `id_` captures render without CSS or images, so screenshot the normal URL. Large CSS was saved to a file and searched. Scrapling cannot resize the viewport, so 375px views were iframe wrappers.

## Limits

- **375px views:** only Squarespace and the builds were screenshotted. Avada's phone behaviour comes from one site's screenshot.
- **Unread CSS or JS:** littlebigbikes and restaurant-lastsupper CSS, InVision's overlay and hero CSS, and the fade-in JS on all three one-pagers.
- **Squarespace's hamburger** is confirmed by computed style, not traced through its media queries. Charter Bay's ~950px width is from a screenshot, not CSS.
- **Not found or not checked:** Windows 8 Metro tiles, iOS 7 CSS, long shadows, Raleway, Waypoints, Angular, React, Mailchimp, Spotify, Dropbox 2014 CSS, Enfold, BeTheme, The7, Medium's Ghost-style drop cap, Intercom (bot-blocked) and Buffer (a sign-in splash, dropped).
- **Material is an early sign only:** MDL 1.0 is Jul 2015, and no 2014 Material page's CSS was read.
- **The revised doc has not had a second round of builds.**

## Sources

- **Wayback:** Slack (17 Nov 2014 + CSS; Feb and Mar 2015), Squarespace (15 Nov 2014), InVision (15 Jan 2015), Charter Bay (29 Apr 2015, CSS 15 Mar 2015), littlebigbikes (10 Mar 2015), restaurant-lastsupper.de (27 Jun 2015), Avada showcase (12 Aug 2015) and demo (1 Jul 2014, 2 Jun 2015), Medium (Aug 2014 CSS; 5 Jan 2015 post, captured 6 Sep 2015), Signal v. Noise (3 Feb 2015), Ghost blog (1 Jun 2015), Airbnb (Oct 2014), Stripe (Jun 2015 + CSS), Apple iOS 7 (Oct 2013), Google Design (Jan 2015), Dropbox (Jun 2014).
- **GitHub:** Start Bootstrap Agency (31 Oct 2014) and Creative (8 Apr 2015), Bootstrap 3.0.0 (19 Aug 2013), Flat UI 2.0.0, Material Design Lite v1.0.0, Ghost Casper 0.9.0.
- **Phase map:** `web-phases-2009-2022.md`, section 2.
