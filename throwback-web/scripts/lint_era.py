#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Anachronism linter for throwback pages.

  uv run lint_era.py --era 1|2|3 [--mode costume|artifact] FILE...
  uv run lint_era.py --selftest

Flags features too new or too old for the era, cartoon and too-tidy signals,
and (costume mode) period fingerprints that harm real users plus missing basics.
Regex heuristics: a finding is a prompt to look, not proof. Exit 1 on any error.
"""
import argparse
import datetime
import re
import sys
from pathlib import Path

I = re.I
ALL = {1, 2, 3}
BOTH = {"costume", "artifact"}
HTML_EXT = {".html", ".htm", ".php", ".xhtml", ".shtml"}

# (id, eras, kind, level, scope, modes, pattern, reason)
# kind: too-new | too-old | cartoon | tidy | forgery | basics ; scope: any | html | js (<script>, on*= handlers, .js files)
R = [
    # ---- too new ----
    ("doctype-any", {1}, "too-new", "error", "html", {"artifact"}, r"<!doctype", "era-1 commercial pages had no doctype (quirks mode)"),
    ("doctype-note", {1}, "too-new", "note", "html", {"costume"}, r"<!doctype", "optional in costume; none is period, and a doctype changes how table/image gaps render: check the screenshot"),
    ("doctype-html5", {2}, "too-new", "error", "html", BOTH, r"<!doctype\s+html\s*>", "HTML5 doctype; use XHTML 1.0 Transitional"),
    ("meta-charset", {1, 2}, "too-new", "error", "html", BOTH, r"<meta\s+charset", "<meta charset> is HTML5; use http-equiv Content-Type utf-8"),
    ("viewport-device", {1, 2}, "too-new", "error", "html", BOTH, r"<meta[^>]+viewport[^>]+device-width", "device-width viewport is mobile-first; costume may use a fixed width=N viewport"),
    ("viewport-any", {1, 2}, "too-new", "error", "html", {"artifact"}, r"<meta[^>]+name=[\"']?viewport", "no viewport meta existed yet"),
    ("meta-description", {1}, "too-new", "error", "html", {"artifact"}, r"<meta[^>]+name=[\"']?description", "era-1 heads had no meta description"),
    ("meta-description-note", {1}, "too-new", "note", "html", {"costume"}, r"<meta[^>]+name=[\"']?description", "not period, but invisible; keep only if search snippets matter"),
    ("html5-elements", {1, 2}, "too-new", "error", "html", BOTH, r"<(header|nav|section|article|aside|footer|main|figure|figcaption|video|audio|canvas|picture|template|dialog|details|summary)\b", "HTML5 element"),
    ("html5-media", {3}, "too-new", "error", "html", BOTH, r"<(picture|dialog|template)\b|\bloading=[\"']?lazy|\ssrcset=", "post-2013 HTML feature"),
    ("data-attr", {1, 2}, "too-new", "error", "html", BOTH, r"\sdata-[\w-]+\s*=", "data- attributes are HTML5"),
    ("placeholder-attr", {1, 2}, "too-new", "error", "html", BOTH, r"\splaceholder\s*=", "placeholder attribute; set the hint text by script or use a label"),
    ("svg", {1, 2}, "too-new", "error", "any", BOTH, r"<svg\b|\.svg\b", "SVG; use GIF/PNG"),
    ("svg-icon-system", {3}, "too-new", "error", "any", BOTH, r"<symbol\b|<use\b[^>]*href=[\"']#|lucide|heroicons", "inline-SVG icon system is 2016+; use PNG sprites"),
    ("icon-font", ALL, "too-new", "error", "any", BOTH, r"font-?awesome|class=[\"'][^\"']*\bfa\s+fa-|material-icons|glyphicon\s+glyphicon-", "icon font of a later phase (era 3 exception: a Pictos-style font on one startup)"),
    ("border-radius", {1}, "too-new", "error", "any", BOTH, r"border-radius", "CSS rounded corners; use corner GIFs or square boxes"),
    ("border-radius-bare", {2}, "too-new", "error", "any", BOTH, r"(?<![-\w])border-radius\s*:", "unprefixed border-radius; corners are images (-moz- only as a Firefox extra)"),
    ("box-shadow", {1, 2}, "too-new", "error", "any", BOTH, r"box-shadow", "CSS box-shadow"),
    ("text-shadow", {1}, "too-new", "error", "any", BOTH, r"text-shadow", "CSS text-shadow"),
    ("text-shadow-2", {2}, "too-new", "warn", "any", BOTH, r"text-shadow", "only as a Safari-only extra, if at all"),
    ("css-gradient", {1, 2}, "too-new", "error", "any", BOTH, r"(linear|radial)-gradient|-webkit-gradient", "CSS gradient; use a tall repeat-x image"),
    ("rgba", {1}, "too-new", "error", "any", BOTH, r"rgba\(|hsla?\(", "alpha colour"),
    ("rgba-2", {2}, "too-new", "warn", "any", BOTH, r"rgba\(|hsla?\(", "rgba only inside a Safari-only text-shadow"),
    ("font-face", {1, 2}, "too-new", "error", "any", BOTH, r"@font-face", "web fonts; use the system stack"),
    ("google-fonts", {1, 2}, "too-new", "error", "any", BOTH, r"fonts\.(googleapis|gstatic)\.com", "Google Fonts (2010+)"),
    ("media-width", {1, 2}, "too-new", "error", "any", BOTH, r"@media[^{]*(min|max)-(device-)?width", "responsive media query"),
    ("transition", {1, 2}, "too-new", "error", "any", BOTH, r"(?<![-\w])(transition|animation|transform)\s*:|@keyframes", "CSS motion"),
    ("float-layout", {1}, "too-new", "warn", "any", BOTH, r"float\s*:\s*(left|right)", "CSS float layout is era 2; era 1 lays out with tables"),
    ("flex", ALL, "too-new", "error", "any", BOTH, r"display\s*:\s*(inline-)?flex|flex-(direction|wrap|grow|shrink|basis|flow)\s*:|(?<![-\w])flex\s*:", "flexbox"),
    ("grid", ALL, "too-new", "error", "any", BOTH, r"display\s*:\s*(inline-)?grid|grid-template", "CSS grid"),
    ("css-vars", ALL, "too-new", "error", "any", BOTH, r"var\(--|(?<![\w-])--[\w-]+\s*:", "CSS custom properties"),
    ("color-scheme", ALL, "too-new", "error", "any", BOTH, r"prefers-color-scheme|prefers-reduced-motion|color-scheme\s*:", "2019+ media feature"),
    ("modern-css", ALL, "too-new", "error", "any", BOTH, r"position\s*:\s*sticky|backdrop-filter|object-fit|aspect-ratio|clamp\(|(?<![-\w])gap\s*:|:is\(|:where\(|:has\(", "post-2013 CSS"),
    ("rem", ALL, "too-new", "error", "any", BOTH, r"\d(\.\d+)?rem\b", "rem units; use px, em or %"),
    ("modern-faces", ALL, "too-new", "error", "any", BOTH, r"font-family[^;}]*\b(Inter|Montserrat|Geist|Poppins|DM Sans|Space Grotesk|Plus Jakarta|Manrope)\b", "a later phase's face"),
    ("roboto", {1, 2}, "too-new", "error", "any", BOTH, r"font-family[^;}]*\bRoboto\b", "Roboto is 2012+"),
    ("tailwind", ALL, "too-new", "error", "html", BOTH, r"class=[\"'][^\"']*\b(rounded-(md|lg|xl|2xl|full)|px-\d|py-\d|text-(xs|sm|lg|\dxl)|bg-\w+-\d00|shadow-(md|lg|xl))\b", "utility-framework classes"),
    ("bootstrap3", ALL, "too-new", "error", "html", BOTH, r"\bcol-(xs|sm|md|lg|xl)-\d|navbar-default|navbar-toggle|\bbtn-default\b", "Bootstrap 3+ (Aug 2013, the flat phase)"),
    ("bootstrap232", {3}, "too-new", "warn", "any", BOTH, r"bootstrap[@/-]?v?2\.3", "Bootstrap 2.3 is a 2013 look; use 2.0-2.2 for a 2012 page"),
    ("js-es6", ALL, "too-new", "error", "js", BOTH, r"=>|\b(const|let)\s+[\w$]|\bfetch\(|\basync\s+function|\bawait\s|`[^`]*\$\{|\bclass\s+\w+\s*(extends|\{)", "ES2015+ JavaScript; write ES3/ES5"),
    ("js-listener", {1, 2}, "too-new", "error", "js", BOTH, r"addEventListener|querySelector", "modern DOM API; use inline handlers and getElementById"),
    ("gtag", ALL, "too-new", "error", "any", BOTH, r"gtag\(|googletagmanager", "gtag/GTM analytics"),
    ("urchin-early", {1}, "too-new", "error", "any", BOTH, r"urchin\.js|_gaq", "Google Analytics arrived in 2005"),
    # ---- too old ----
    ("font-tag", {2, 3}, "too-old", "error", "html", BOTH, r"<font\b", "<font> is era 1"),
    ("bgcolor", {2}, "too-old", "warn", "html", BOTH, r"\sbgcolor\s*=", "bgcolor beyond one leftover table is era 1"),
    ("bgcolor-3", {3}, "too-old", "error", "html", BOTH, r"\sbgcolor\s*=", "bgcolor is era 1"),
    ("image-map", {2, 3}, "too-old", "error", "html", BOTH, r"\susemap\s*=|<map\b", "image-map nav is era 1"),
    ("spacer-gif", {2}, "too-old", "warn", "any", BOTH, r"\b(spacer|blank(_1x1)?|pixel|s|trans(parent)?|clear)\.gif\b", "spacer-GIF layout is era 1"),
    ("spacer-gif-3", {3}, "too-old", "error", "any", BOTH, r"\b(spacer|blank(_1x1)?|pixel|trans(parent)?)\.gif\b", "spacer GIFs are era 1"),
    ("marquee", {2, 3}, "too-old", "error", "html", BOTH, r"<(marquee|blink)\b", "<marquee>/<blink>"),
    ("table-layout", {3}, "too-old", "error", "html", BOTH, r"<table[^>]*\b(cellpadding|cellspacing|width\s*=)", "table layout is eras 1-2"),
    ("corner-images", {3}, "too-old", "error", "any", BOTH, r"[\w-]*(corner|[-_](tl|tr|bl|br)|box-h[lr])\.(gif|png)\b|class=[\"']?xb\d", "image/markup corners are era 2; use border-radius"),
    ("width-750", {3}, "too-old", "warn", "any", BOTH, r"(?<![-\w])width\s*:\s*7[56]\dpx", "a 750-760px column is era 2; era 3 is 630-960"),
    ("urchin-late", {3}, "too-old", "error", "any", {"artifact"}, r"urchin\.js", "urchin.js is era 2; era 3 used async _gaq"),
    # ---- forgery fingerprints: harmful in costume ----
    ("dead-analytics", ALL, "forgery", "error", "any", {"costume"}, r"urchin\.js|urchinTracker|_uacct|_gaq|google-analytics\.com/ga\.js|mixpanel|optimizely|chartbeat", "dead tracking script; drop it in costume"),
    ("http-asset", ALL, "forgery", "error", "any", {"costume"}, r"\b(src|href|action)\s*=\s*[\"']?http://|url\(\s*[\"']?http://", "http:// asset or link; use https or relative"),
    ("session-id", ALL, "forgery", "error", "any", {"costume"}, r"[?&;](sid|uid|sessionid|jsessionid|phpsessid)=|/exec/obidos/|/ref=\w+_\w+", "fake session/tracking ID in a URL"),
    ("doc-write", ALL, "forgery", "error", "any", {"costume"}, r"document\.write|\bd\.write\(", "document.write (ad/analytics loader)"),
    ("flash", ALL, "forgery", "error", "any", {"costume"}, r"\.swf\b|swfobject|<embed\b|x-shockwave-flash", "Flash is dead; use a poster image or a link"),
    ("broken-markup", {1}, "forgery", "warn", "html", {"costume"}, r"face=\"[^\"]*,\"\s*\w|helvectica|<met\s", "deliberately broken markup; artifact mode only"),
    ("dead-widgets", ALL, "forgery", "error", "any", {"costume"}, r"plusone\.js|platform\.twitter\.com/widgets|connect\.facebook\.net|facebook\.com/plugins/like|addthis|instapaper\.com/[^\"']*iframe", "dead or changed social widget"),
    ("feed-scheme", ALL, "forgery", "error", "html", {"costume"}, r"href=[\"']feed:", "feed: scheme links no longer open"),
    ("generator-old", ALL, "forgery", "error", "html", {"costume"}, r"<meta[^>]+generator[^>]+(WordPress\s+[0-3]\.|Joomla|Movable)", "advertises an old, vulnerable CMS version"),
    ("old-libs", ALL, "forgery", "warn", "any", {"costume"}, r"jquery[-.]1\.\d[\w.]*\.js|jquery/1\.\d|prototype(\.min)?\.js|scriptaculous|mootools[\w.-]*\.js|bootstrap[\w.-]*2\.\d[\w./-]*\.js|bootstrap-(collapse|dropdown|tooltip|modal)\.js", "unmaintained library with known issues; write vanilla JS"),
    ("no-zoom", ALL, "basics", "error", "html", BOTH, r"user-scalable\s*=\s*(no|0)|maximum-scale\s*=\s*1(\.0)?\b", "zoom disabled; fixed layouts depend on pinch-zoom"),
    ("text-size-adjust", ALL, "basics", "warn", "any", {"costume"}, r"text-size-adjust\s*:\s*none", "blocks phone text inflation on a zoomed-out page"),
    # ---- the cartoon ----
    ("lobster", ALL, "cartoon", "warn", "any", BOTH, r"\blobster\b", "Lobster is the pastiche tell"),
    ("geocities-kit", {1, 2}, "cartoon", "warn", "any", BOTH, r"under[-_ ]?construction|hit[-_ ]?counter|counter\.gif|webring|best viewed (in|with)", "absent from commercial captures; personal pages only (unverified)"),
    ("marquee-1", {1}, "cartoon", "warn", "html", BOTH, r"<(marquee|blink)\b", "not on commercial captures"),
    ("starburst", {2, 3}, "cartoon", "warn", "any", BOTH, r"starburst|[-_]burst\b|beta[-_]?badge|badge[-_]?beta|reflection|box-reflect", "starbursts/reflections/beta badges were absent from real 2006-08 pages"),
    ("gel", {2}, "cartoon", "warn", "any", BOTH, r"\b(gel|glossy|web20|web2\.0)\b", "at most one glossy element (the sign-up pill)"),
    ("bezel", ALL, "cartoon", "warn", "any", BOTH, r"bezel|(iphone|device|phone)[-_]?frame|marvel-device|glare", "real pages showed a flat screenshot with a drop shadow"),
    ("stitching", {3}, "cartoon", "warn", "any", BOTH, r"stitch", "stitching unseen on 11 real pages"),
    # ---- too tidy / generic ----
    ("ai-copy", ALL, "tidy", "warn", "html", BOTH, r"\b(get started( free| today)?|build faster|ship (faster|smarter)|seamless(ly)?|supercharge|unlock (your|the)|all-in-one|trusted by (thousands|teams|leading)|empower|effortless(ly)?|next[- ]generation|game[- ]changer|elevate your)\b", "modern AI-default copy; write literal, specific copy"),
]
COMPILED = [(i, e, k, lv, sc, m, re.compile(p, I), why) for (i, e, k, lv, sc, m, p, why) in R]


def strip_comments(text):
    """Blank out CSS/HTML comments (keeping newlines) so commented-out rules don't fire."""
    blank = lambda m: re.sub(r"[^\n]", " ", m.group(0))
    text = re.sub(r"/\*.*?\*/", blank, text, flags=re.S)
    return re.sub(r"<!--(?!\[if).*?-->", blank, text, flags=re.S)


def js_only(text, suffix):
    """Keep script bodies and on*= handler values, blank the rest (newlines kept): prose like 'let it set' never fires."""
    if suffix.lower() == ".js":
        return text
    if suffix.lower() not in HTML_EXT:
        return ""
    keep = [m.span(1) for m in re.finditer(r"<script\b[^>]*>(.*?)</script>", text, I | re.S)]
    keep += [m.span(2) for m in re.finditer(r"\son\w+\s*=\s*([\"'])(.*?)\1", text, I | re.S)]
    out = re.sub(r"[^\n]", " ", text)
    for a, b in keep:
        out = out[:a] + text[a:b] + out[b:]
    return out


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def file_checks(text, is_html, era, mode):
    """Whole-file heuristics. Yields (id, kind, level, line, reason)."""
    low = text.lower()
    n = lambda pat: len(re.findall(pat, text, I))
    if is_html:
        if era == 1:
            runs = len(re.findall(r">[^<]*[A-Za-z0-9][^<]*<", re.sub(r"(?is)<(script|style|title|option|textarea)\b.*?</\1>", "", text)))
            fonts = n(r"<font\b")
            if runs >= 4 and fonts < 0.25 * runs:
                yield ("font-density", "tidy", "warn", 1, f"{fonts} <font> for {runs} text runs: real pages wrapped nearly every run (repeat it per cell)")
            if "<table" not in low:
                yield ("no-tables", "too-new", "error", 1, "no <table>: the era-1 page IS a table")
            if n(r"\sclass\s*=") > 25:
                yield ("class-styled", "tidy", "warn", 1, "styling should live in attributes (bgcolor, <font>, align), not classes")
        if era in (2, 3) and not re.search(r"<!doctype", text, I):
            yield ("no-doctype", "too-old", "error" if era == 2 else "warn", 1, "no doctype is era 1")
        if era == 2 and not re.search(r"\*\s*html|<!--\[if|_height|/\*\s*ie", text, I) and "<table" not in low and "clear" not in low:
            yield ("too-pure-2", "tidy", "warn", 1, "no IE6 hack, clearfix or table leftover: too pure for 2006-08 (check the CSS file too)")
        if era == 3 and "hero-unit" in low and n(r"class=[\"'][^\"']*\bspan4\b") >= 3:
            yield ("stock-bootstrap", "tidy", "warn", 1, "stock Bootstrap hero + 3 x span4: real startups wrote their own header and skinned it")
        if n(r"(id|class)=[\"'][^\"']*\b(hero|features|testimonials|pricing|faq|cta|social-proof|logo-?cloud)\b") >= 4:
            yield ("landing-skeleton", "tidy", "warn", 1, "hero -> features -> testimonials -> pricing -> FAQ is the modern AI skeleton")
        if n(r"twitter-share-button|fb-like|share on twitter|tweet this|plugins/like") >= 3:
            yield ("share-everywhere", "cartoon", "warn", 1, "Like/Tweet on every post; real social was sparse")
        if mode == "costume":
            for m in re.finditer(r"<(img|area)\b[^>]*>", text, I):
                if not re.search(r"\salt\s*=", m.group(0), I):
                    yield ("missing-alt", "basics", "error", line_of(text, m.start()), f"<{m.group(1).lower()}> without alt")
            fields = n(r"<(input(?![^>]*type=[\"']?(hidden|submit|image|button|reset))|select|textarea)\b")
            labels = n(r"<label\b|aria-label|\stitle=")
            if fields > labels:
                yield ("unlabelled", "basics", "error", 1, f"{fields} form fields, {labels} labels")
            if not re.search(r"charset\s*=\s*[\"']?utf-8", text, I):
                yield ("no-utf8", "basics", "error", 1, "declare UTF-8 (http-equiv Content-Type in eras 1-2)")
            year = datetime.date.today().year
            for m in re.finditer(r"(?:©|&copy;|\(c\)|copyright)\s*(?:\d{4}\s*(?:-|–|&ndash;)\s*)?(\d{4})", text, I):
                if int(m.group(1)) < year - 1:
                    yield ("stale-copyright", "forgery", "warn", line_of(text, m.start()), f"© ends {m.group(1)}; in costume end it at the current year")
    if era == 3:
        if re.search(r"-moz-border-radius", text, I) and not re.search(r"(?<![-\w])border-radius", text, I):
            yield ("moz-radius-only", "too-old", "error", 1, "-moz-border-radius alone is era 2; add the bare property")
        if re.search(r"(?<![-\w])(linear-gradient|border-radius)", text, I) and not re.search(r"-(webkit|moz)-", text, I):
            yield ("unprefixed-only", "too-new", "error", 1, "unprefixed-only CSS3; 2011-12 CSS carried -webkit-/-moz- prefixes")
        o, w = n(r"-o-"), n(r"-webkit-")
        if o >= 3 and o >= 0.8 * w or n(r"progid:DXImageTransform") > 4:
            yield ("full-ladder", "cartoon", "warn", 1, "the full prefix ladder on everything; real sheets were patchy")
        textures = {t for t in ("linen", "leather", "paper", "wood", "denim", "felt", "canvas") if re.search(rf"\b{t}", text, I)}
        if len(textures) >= 2:
            yield ("texture-pileup", "cartoon", "warn", 1, f"textures {sorted(textures)}: pick one, at the page edge")
        if n(r"ribbon") >= 2:
            yield ("ribbons", "cartoon", "warn", 1, "ribbons repeated; unseen on real pages")
        if re.search(r"fonts\.googleapis", text, I) and not re.search(r"typekit|@font-face", text, I):
            yield ("google-fonts-only", "too-new", "warn", 1, "Google-Fonts-only stack; period sites used Typekit (or self-host via @font-face)")


def lint_text(text, path_suffix, era, mode):
    is_html = path_suffix.lower() in HTML_EXT
    text = strip_comments(text)
    js = js_only(text, path_suffix)
    out = []
    for rid, eras, kind, level, scope, modes, rx, why in COMPILED:
        if era not in eras or mode not in modes or (scope == "html" and not is_html):
            continue
        hits = list(rx.finditer(js if scope == "js" else text))
        if hits:
            lines = sorted({line_of(text, h.start()) for h in hits})
            out.append((rid, kind, level, lines, why))
    for rid, kind, level, line, why in file_checks(text, is_html, era, mode):
        out.append((rid, kind, level, [line], why))
    return out


def selftest():
    ids = lambda t, suf, era, mode="costume": {f[0] for f in lint_text(t, suf, era, mode)}
    e1_good = ('<html><head><title>Acme--Tools</title><meta http-equiv="Content-Type" content="text/html; charset=utf-8">'
               '</head><body bgcolor="FFFFFF"><table width=760><tr><td><font face="verdana,arial" size=-1>Hi</font>'
               '<img src="s.gif" alt="" width=1 height=1></td></tr></table>&copy; 1999-%d Acme</body></html>' % datetime.date.today().year)
    assert ids(e1_good, ".html", 1) == set(), ids(e1_good, ".html", 1)
    bad1 = '<!DOCTYPE html><meta charset="utf-8"><header style="display:flex;border-radius:8px">x</header>'
    assert {"doctype-note", "meta-charset", "html5-elements", "flex", "border-radius", "no-tables"} <= ids(bad1, ".html", 1)
    assert "meta-description" in ids('<meta name="description" content="x">', ".html", 1, "artifact")
    assert "meta-description" not in ids('<meta name="description" content="x">', ".html", 1, "costume")
    assert "viewport-any" not in ids('<meta name="viewport" content="width=776">', ".html", 1, "costume")
    assert "viewport-device" in ids('<meta name="viewport" content="width=device-width">', ".html", 1)
    css2 = ".box{-moz-border-radius:4px} .x{border-radius:4px;box-shadow:0 0 1px #000;background:linear-gradient(#fff,#000)}"
    assert {"border-radius-bare", "box-shadow", "css-gradient"} <= ids(css2, ".css", 2)
    assert "border-radius-bare" not in ids(".box{-moz-border-radius:4px}", ".css", 2)
    assert {"font-tag", "bgcolor", "meta-charset", "html5-elements"} <= ids('<meta charset="utf-8"><font size=2><td bgcolor="#fff"><nav>', ".html", 2)
    css3 = ".a{display:grid;--c:#fff;color:var(--c)} @media (prefers-color-scheme:dark){} .b{border-radius:4px}"
    assert {"grid", "css-vars", "color-scheme", "unprefixed-only"} <= ids(css3, ".css", 3)
    assert "google-fonts-only" in ids('<link href="https://fonts.googleapis.com/css?family=Lobster">', ".html", 3)
    assert "lobster" in ids("h1{font-family:Lobster,Georgia}", ".css", 3)
    ladder = ".b{" + "-webkit-x:1;-moz-x:1;-o-x:1;" * 4 + "}"
    assert "full-ladder" in ids(ladder, ".css", 3)
    assert "texture-pileup" in ids("body{background:url(linen.png)} .c{background:url(leather.jpg)}", ".css", 3)
    assert "bezel" in ids('<div class="iphone-frame">', ".html", 3)
    assert {"dead-analytics", "http-asset", "flash", "missing-alt"} <= ids('<script src="http://x/urchin.js"></script><embed src="a.swf"><img src="a.gif">', ".html", 2)
    assert "dead-analytics" not in ids('<script src="urchin.js"></script>', ".html", 2, "artifact")
    assert "stale-copyright" in ids("&copy; 1999 Acme", ".html", 1)
    assert "ai-copy" in ids("<p>Get started today and build faster.</p>", ".html", 3)
    assert "flex" not in ids("/* .x{display:flex} */ .y{color:red}", ".css", 3)
    assert "no-zoom" in ids('<meta name="viewport" content="width=800, user-scalable=no">', ".html", 1)
    # regressions from test round 1
    assert "js-es6" not in ids("<p>Paint needs a day; let it set before the second coat.</p>", ".html", 1)
    assert "js-es6" in ids("<script>let n = 1;</script>", ".html", 3)
    assert "js-es6" in ids('<a href="#" onclick="const x=1">x</a>', ".html", 3)
    assert "js-es6" in ids("var f = (a) => a;", ".js", 3) and "js-es6" not in ids("a{content:'=>'}", ".css", 3)
    assert "width-750" not in ids("@media (max-width:767px){.a{width:100%}} @media (min-width: 768px){}", ".css", 3)
    assert "width-750" in ids("#page{width:760px}", ".css", 3)
    assert "doctype-any" not in ids("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\">" + e1_good, ".html", 1)
    assert "doctype-any" in ids("<!DOCTYPE html>" + e1_good, ".html", 1, "artifact")
    sparse = "<table>" + "<tr><td>Hammers and saws</td></tr>" * 8 + "</table><font size=-1>x</font>"
    assert "font-density" in ids(sparse, ".html", 1) and "font-density" not in ids(e1_good, ".html", 1)
    print("selftest ok")


def applicable(era, mode):
    """Rule ids that run for this era and mode (whole-file checks included), for the clean-run summary."""
    ids_ = [rid for rid, eras, _k, _l, _s, modes, _p, _w in R if era in eras and mode in modes]
    extra = {1: ["font-density", "no-tables", "class-styled"], 2: ["no-doctype", "too-pure-2"],
             3: ["no-doctype", "stock-bootstrap", "moz-radius-only", "unprefixed-only", "full-ladder", "texture-pileup", "ribbons", "google-fonts-only"]}[era]
    extra += ["landing-skeleton", "share-everywhere"] + (["missing-alt", "unlabelled", "no-utf8", "stale-copyright"] if mode == "costume" else [])
    return ids_ + extra


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--era", type=int, choices=[1, 2, 3])
    ap.add_argument("--mode", choices=["costume", "artifact"], default="costume")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("paths", nargs="*")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.era or not a.paths:
        ap.error("--era and at least one path are required")
    errors = warns = notes = 0
    for p in a.paths:
        path = Path(p)
        findings = lint_text(path.read_text(errors="replace"), path.suffix, a.era, a.mode)
        for rid, kind, level, lines, why in sorted(findings, key=lambda f: (f[2] != "error", f[3][0])):
            more = f" (+{len(lines) - 3} more)" if len(lines) > 3 else ""
            print(f"{p}:{','.join(map(str, lines[:3]))}{more} [{level} {kind}] {rid}: {why}")
            errors += level == "error"; warns += level == "warn"; notes += level == "note"
    rules = applicable(a.era, a.mode)
    print(f"checked {len(rules)} rules: {' '.join(rules)}")
    print(f"{errors} error(s), {warns} warning(s), {notes} note(s) across {len(a.paths)} file(s), era {a.era}, {a.mode} mode")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
