# Web design phases, 2009–2022

Follows [web2-design.md](web2-design.md). Stops before AI-generated sites. **V** = verified in a raw Wayback `id_` capture (site, date, file); **U** = unverified (period knowledge only).

| Phase | Years | Triggers | Ended by |
|---|---|---|---|
| 1. Late skeuomorphic + CSS3 | 2010–2013 | iPhone 4 Retina + iPad (2010), CSS3 in Safari/Firefox/Chrome, Google Web Fonts (May 2010), IE9 (2011), Bootstrap 2.0 (Jan 2012) | Windows 8 (Oct 2012), iOS 7 (Jun/Sep 2013), Bootstrap 3 (Aug 2013) |
| 2. Responsive flat template | 2013–2016 | Bootstrap 3 "mobile first", iOS 7, Font Awesome 3/4, theme marketplaces, Google's mobile-friendly ranking (Apr 2015) | Material Design spreading to the web, flexbox, React marketing sites, template fatigue |
| 3. Product + illustration (Material era) | 2016–2019 | Material Design (Jun 2014), React/SPA stacks, flexbox, inline SVG, Facebook's "Alegria" illustration style (2017) | macOS dark mode (2018) and `prefers-color-scheme` (2019), Tailwind 1.0 (May 2019), Big Sur (Nov 2020) |
| 4. Dark, system-font, component | 2019–2022 | Dark mode in OSes, Next.js + CSS-in-JS, Inter, Figma, Webflow; neumorphism (Dec 2019) and glassmorphism (2020) blips | Out of scope (the AI-generated phase) |

I split the third candidate in two. Stripe 2017 and Linear 2021 differ on almost every trait: light vs dark canvas, brand font vs Inter/system stack, BEM classes vs styled-components hashes.

---

## 1. Late skeuomorphic + CSS3 (2010–2013)

**Fingerprint**
- **Layout:** centred fixed column, 940–990px: Gowalla 960 (V, Dec 2010, `main.css`), MailChimp 960/990 (V, Mar 2011, `site.css`), Bootstrap 2 `.container` 940 (V, May 2012, `bootstrap.css` v2.0.3).
- **Viewport:** none, or fixed. Dribbble has `<meta name="viewport" content="width=1000">` (V, Jun 2011, head). Bootstrap 2 already has `width=device-width` plus a separate `bootstrap-responsive.css` (V), so responsive is an add-on here, not the base.
- **CSS3 everywhere, vendor-prefixed:** Gowalla has 502 `border-radius` (160 `-moz-`, 96 `-webkit-`), 223 `box-shadow`, `-webkit-gradient(linear, 0% 0%, 0% 100%, color-stop(...))` beside `linear-gradient`, and IE `filter: progid` (V). Radius is small: MailChimp has a 5px `-webkit-`/`-moz-`/plain triple (V).
- **Textures as bitmaps:** Gowalla `leather.jpg` and MailChimp `noise.png` (V). Linen, stitching and paper are U as a web-wide norm.
- **Letterpress shadows:** 1px highlight/dark pairs. MailChimp has `box-shadow: 0px 1px 0 #373731, 0px -1px 0 #0e0d0b` and `0px 1px 1px #fff` (V).
- **Buttons:** gradient pills. Bootstrap 2 `.btn-primary` is `#0088cc→#0055cc` in five prefixed syntaxes plus `filter` and `*background-color` (IE7) (V).
- **Type:** "Helvetica Neue", Helvetica, Arial at 13px/18px (Bootstrap 2, V); Dribbble has 20 Helvetica Neue stacks (V). Georgia and novelty faces for headings: Gowalla uses Chalkduster (V). Google Fonts are U for this period's mainstream.
- **Head:** `<meta charset="utf-8">`, Open Graph tags, `apple-touch-icon-precomposed` (57/72/114/144), and the async `_gaq` snippet (V, MailChimp 2011; Bootstrap 2012).
- **Icons:** sprites; Glyphicons PNG in Bootstrap 2 (V).
- **Sections:** illustrated mascot or character (Freddie on MailChimp, `og:image` V), ribbons and badges (U).

**Too old:** an XHTML doctype, `urchin.js`, rounded corners from GIFs, no CSS3. **Too new:** unprefixed-only CSS3, flat fills, icon fonts, a hamburger, full-bleed photo heroes, Montserrat.

**Exemplars:** Gowalla (Dec 2010, V); MailChimp (Mar 2011, V); Dribbble (Jun 2011, head V); Bootstrap 2 docs (May 2012, V); Path, Forrst (2011, U).

## 2. Responsive flat template (2013–2016)

The Start Bootstrap "Agency" theme (V, Jan–Feb 2015, `index`, `agency.css`, `bootstrap.min.css` v3.3.1) is close to the phase's median page.

**Fingerprint**
- **Responsive base:** `width=device-width, initial-scale=1`, Bootstrap 3 containers 750/970/1170, and `@media(min-width:768px)` to step up (V).
- **Nav:** `navbar-fixed-top` that is transparent at the top and shrinks to `#222` on scroll (`.navbar-shrink`, `transition: padding .3s`). The hamburger is three `.icon-bar` spans, 22×2px (V).
- **Hero:** full-bleed photo with `background-size: cover` plus four prefixes, centred text, a giant uppercase heading (Montserrat 700 at 75px), an italic serif lead-in, and one big flat button (`padding: 20px 40px; border-radius: 3px`) (V).
- **Colour:** flat fills, one loud accent (`#fed136`) on `#222` and `#f7f7f7` bands. Bootstrap's `#337ab7` primary has no gradient (V).
- **Type:** Google Fonts by `<link>`: Montserrat, Droid Serif, Roboto Slab, Kaushan Script (V). Base 14px/1.428 Helvetica Neue (Bootstrap 3.3.1, V). Open Sans and Lato as defaults are U.
- **Icons:** Font Awesome `<i class="fa fa-twitter">` in round social buttons (V).
- **One-pager:** `#services`, `#portfolio`, `#about` (timeline), `#team`, `#contact` with `.page-scroll` anchor links; sections with `padding: 150px 0` (V).
- **Interaction:** portfolio tiles with an `rgba(...,.9)` hover overlay, `transition: all .3s`, modals (V). Parallax is U.
- **Footer:** three `col-md-4` blocks: ©, social circles, Privacy/Terms (V).
- **Copy:** lorem ipsum subheads left in production themes (V, in the theme demo).
- **Ghost buttons** (transparent, 1–2px white border): U.

**Too old:** gradients, textures, letterpress shadows, 940px fixed, Glyphicon PNGs. **Too new:** flexbox or grid layouts, inline SVG icons, skewed sections, flat illustrations of people, dark mode.

**Exemplars:** Start Bootstrap Agency (2014–15, V); Bootstrap 3 (Aug 2013, release U, CSS V); Medium (Dec 2013, head V only); Squarespace and Dropbox (2014, U; the Dropbox capture showed no viewport meta).

## 3. Product + illustration, Material era (2016–2019)

**Fingerprint**
- **Layout:** flexbox for components, still with `-ms-flexbox` prefixes (Stripe, V, Jun 2017, `home/index-*.css`). No grid and no custom properties seen.
- **Hero:** a diagonal colour field. Stripe's `#stripes` is `transform: skewY(-12deg)` with `linear-gradient(150deg,#53f 15%,#05d5ff 70%,#a6ffcb 94%)` and coloured bars (V). The product shown as tilted device mock-ups (`rotate(-12deg)`) built in CSS (V).
- **Depth:** soft layered shadows tinted with the brand colour: `0 4px 6px rgba(50,50,93,.11), 0 1px 3px rgba(0,0,0,.08)` (V).
- **Type:** a commissioned or licensed brand sans (Stripe Camphor, then the stack Open Sans, Segoe UI) (V). Text navy `#32325d`, tint `#f6f9fc` (V). Roboto/Material on Google properties is U.
- **Icons:** inline SVG with brand fills (V, Stripe). Font icons fade.
- **Sections:** "NEW" pill announcement above the H1, uppercase small section labels, a code sample, a customer logo strip with SVG logos (V, Stripe 2017). Slack 2019 has "You're in good company" plus a logo strip, customer-story cards, and product UI shots with `srcset` 1x/2x (V, Slack Jun 2019).
- **Markup:** hashed asset filenames, `<script defer>`, and utility or BEM classes: Slack `c-type-headline-jumbo`, `u-margin-bottom--x-large` (V).
- **Imagery:** flat people illustrations ("Corporate Memphis") (U). Slack's alt texts describe "stylized credit cards" (V, indirect).
- **Material:** cards, FAB and ripple; strongest in apps and admin templates (U).

**Too old:** full-bleed stock photo plus ghost button, Font Awesome, Montserrat uppercase, `navbar-fixed-top`. **Too new:** dark canvas by default, Inter, `backdrop-filter`, thick black borders.

**Exemplars:** Stripe (Jun 2017, V); Slack (Jun 2019, HTML V); material.io (2014–), Dropbox rebrand (2017), Intercom (2018) (U).

## 4. Dark, system-font, component (2019–2022)

**Fingerprint**
- **Stack:** Next.js (`/_next/static/chunks/*`), styled-components (`/*!sc*/`, hashed `.gtDKGd` classes) and `gtag.js` (V, Linear Jun 2021, homepage). Webflow for marketing sites (V, Gumroad Jun 2022, `gumroad-v2.webflow.*.css`).
- **Dark by default:** `theme-color #1B1A16`, backgrounds `#1b1c1d`, `#0B0B0C`, muted text `#8a8f98` (V, Linear).
- **Type:** `"Inter UI","SF Pro Display",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,...` (V, Linear).
- **Glow and glass:** gradient CTA `linear-gradient(92.88deg,#455eb5,#5643cc,#673fd7)` with a hover glow `0 1px 40px rgba(80,63,205,.5)`, `backdrop-filter: blur(5px)`, 8px radius (V, Linear).
- **Neo-brutalist counter-trend:** `border: 2px solid #000`, hard shadows `6px 6px 0 0 #000`, flat pink `#ff90e8` and yellow `#ffc900`, licensed grotesk (Mabry Pro) (V, Gumroad 2022). Uses `display:grid` (29 uses, V).
- **Neumorphism:** a Dribbble blip, rare on live sites (U).
- **Dark mode via `prefers-color-scheme`:** not seen in the two captures (U).

**Too old:** light navy-on-white Stripe palette, `-ms-` prefixes, skewed stripes. **Too new:** out of scope.

**Exemplars:** Linear (Jun 2021, V); Gumroad (Jun 2022, V); Vercel, Raycast (2021, U); Apple Big Sur pages (2020, U).

---

## How to tell adjacent phases apart

- **1 vs 2:** a gradient or texture image and 940–990px fixed width means 1. A flat accent, `background-size: cover` photo hero, hamburger and Google Font means 2. Bootstrap 2 (2012) already responsive is the bridge.
- **2 vs 3:** Font Awesome, uppercase Montserrat and a stock photo means 2. Inline SVG, brand gradient or diagonal field, product mock-ups, a logo strip and flexbox mean 3.
- **3 vs 4:** light canvas, navy text, brand font and BEM classes means 3. Dark canvas, Inter/system stack, glow or blur, and CSS-in-JS or Webflow hashes mean 4. Hard black borders and offset shadows are 4's counter-trend.

## Sources and limits

- **Wayback `id_` captures (V):**
  - Gowalla 16 Dec 2010 (`/`, `main.css`).
  - MailChimp 15 Mar 2011 (`/`, `css/site.css`).
  - Dribbble 30 Jun 2011 (head).
  - Bootstrap 2.0.3 docs 26 May 2012 (`/`, `bootstrap.css`).
  - Medium 14 Dec 2013 (head).
  - Dropbox 15 Jun 2014 (head).
  - Start Bootstrap Agency 28 Feb 2015 (`/`, `agency.css` and `bootstrap.min.css` 3.3.1, CSS captured 4 Jan 2015).
  - Stripe 1 Jun 2017 (`/`, `home/index-*.css`).
  - Slack 14 Jun 2019 (`/`).
  - Linear 1 Jun 2021 (`/`, inline styles).
  - Gumroad 1 Jun 2022 (`/`, Webflow CSS).
- **Method trap:** Wayback ignores query strings when matching. A June 2011 request for Dribbble's `master.css?1309286388` returned the March 2013 file. Check the returned URL's timestamp.
- **Release dates are from memory (U):** Marcotte's "Responsive Web Design" (A List Apart, May 2010), Bootstrap releases, Material, iOS 7, Tailwind. No Smashing Magazine or A List Apart page or trend roundup was fetched.
- **Not seen rendered:** no screenshots were taken. Imagery claims (illustration style, parallax, ghost buttons, linen) are unverified.
- **Sample:** 11 sites, mostly US startups. Weak on news, e-commerce, government and WordPress themes after 2012.
