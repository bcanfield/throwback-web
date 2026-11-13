#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["pillow"]
# ///
"""Period image assets, so builds stop hand-rolling them.

  uv run make_assets.py spacer   OUT.gif                                   # 1x1 transparent GIF (era 1)
  uv run make_assets.py logo     OUT.gif --text 'Kessler & Sons' [--font serif|sans|PATH] [--size 26] [--fg '#900'] [--bg '#fff'] [--pad 2]
                                                                           # aliased text GIF, cropped tight: logos, headings (era 1, 2)
  uv run make_assets.py navmap   OUT.gif --labels 'Home|Tools|Paint|Hours' [--href 'index.html|tools.html|...'] [--font sans] [--size 12]
                                 [--fg '#fff'] [--bg '#990000'] [--sep '#ffdd00'] [--padx 12] [--height 22]
                                                                           # ONE wide image-map nav GIF; prints <img usemap> + <map> (era 1)
  uv run make_assets.py gradient OUT.png --height 40 --top '#fff' --bottom '#e0e0e0' [--width 1]
                                                                           # tall repeat-x strip (era 2)
  uv run make_assets.py corners  PREFIX --radius 6 --fg '#fff' --bg '#d5d6d7'
                                                                           # PREFIX-tl/tr/bl/br.gif (era 2 only)
  uv run make_assets.py noise    OUT.png --base '#e6e6e6' [--amount 6] [--size 128] [--seed 1]
                                                                           # tileable noise; warm base + low amount = paper (era 3)
  uv run make_assets.py button   OUT.gif --text 'FOO NOW' [--bg '#336699'] [--fg '#fff'] [--font path.ttf]
                                                                           # 88x31 bevelled button; '\\n' in --text splits two lines
                                                                           # costume: real links only (a badge for your host, RSS), never joke buttons
  uv run make_assets.py appbutton OUT.png --text 'Download for Mac' [--sub 'v1.4 - Mac OS X 10.7+'] [--width 196] [--height 56]
                                 [--top '#6db33f'] [--bottom '#3f7f1f'] [--class btn]
                                                                           # era-3 bitmap button: normal over hover in one sprite; prints the CSS
  uv run make_assets.py sprite   OUT.png IN1 IN2 ... [--gap 10] [--prefix icon]
                                                                           # vertical sprite with transparent gaps; prints one CSS rule per frame
  uv run make_assets.py window   OUT.png --width 640 --height 400 [--title 'Preferences'] [--content IN.png] [--shadow 14]
                                                                           # flat Mac app window + baked drop shadow, no bezel (era 3)

Fonts: serif/sans pick a system face (Times New Roman/Georgia, Verdana/Arial; DejaVu on Linux).
Use the printed CSS/HTML as-is: offsets come from the image, so sprites can't be mis-cropped.
Colours accept #rgb or #rrggbb. Run with --selftest to build one of each into a temp dir.
"""
import argparse
import html
import random
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONTS = {
    "serif": ["/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf", "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
              "C:/Windows/Fonts/timesbd.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", "DejaVuSerif-Bold.ttf"],
    "sans": ["/System/Library/Fonts/Supplemental/Verdana Bold.ttf", "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
             "C:/Windows/Fonts/verdanab.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "DejaVuSans-Bold.ttf"],
}


def rgb(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def font(spec, size):
    for p in FONTS.get(spec, [spec] if spec else []):
        try:
            return ImageFont.truetype(p, size)
        except OSError:
            pass
    print(f"warning: no font for {spec!r}; using PIL's bitmap default", file=sys.stderr)
    return ImageFont.load_default()


def aliased(im):
    d = ImageDraw.Draw(im)
    d.fontmode = "1"  # no antialiasing: period GIF text was hard-edged
    return d


def spacer(out):
    im = Image.new("P", (1, 1), 0)
    im.putpalette([255, 255, 255] + [0, 0, 0] * 255)
    im.save(out, transparency=0)


def logo(out, text, face="serif", size=26, fg="#000", bg="#fff", pad=2):
    f = font(face, size)
    l, t, r, b = ImageDraw.Draw(Image.new("RGB", (1, 1))).textbbox((0, 0), text, font=f)
    im = Image.new("RGB", (r - l + 2 * pad, b - t + 2 * pad), rgb(bg))
    aliased(im).text((pad - l, pad - t), text, fill=rgb(fg), font=f)
    im.convert("P", palette=Image.ADAPTIVE, colors=2).save(out)
    print(f'<img src="{Path(out).name}" width={im.width} height={im.height} alt="{html.escape(text)}" border=0>')
    return im.size


def navmap(out, labels, hrefs=None, face="sans", size=12, fg="#fff", bg="#990000", sep="#ffdd00", padx=12, height=22):
    f = font(face, size)
    probe = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    boxes = [probe.textbbox((0, 0), s, font=f) for s in labels]
    widths = [b[2] - b[0] + 2 * padx for b in boxes]
    im = Image.new("RGB", (sum(widths) + len(labels) - 1, height), rgb(bg))
    d = aliased(im)
    x, areas = 0, []
    for i, (s, b, w) in enumerate(zip(labels, boxes, widths)):
        d.text((x + padx - b[0], (height - (b[3] - b[1])) // 2 - b[1]), s, fill=rgb(fg), font=f)
        areas.append((x, x + w - 1, s))
        x += w
        if i < len(labels) - 1:
            d.line((x, 3, x, height - 4), fill=rgb(sep))
            x += 1
    im.convert("P", palette=Image.ADAPTIVE, colors=8).save(out)
    hrefs = hrefs or [s.lower().replace(" ", "") + ".html" for s in labels]
    name = Path(out).stem
    print(f'<img src="{Path(out).name}" width={im.width} height={height} usemap="#{name}" border=0 alt="">')
    print(f'<map name="{name}">')
    for (x0, x1, s), h in zip(areas, hrefs):
        print(f'<area shape=rect coords="{x0},0,{x1},{height - 1}" href="{h}" alt="{s}">')
    print("</map>")
    return im.size, areas


def gradient(out, height, top, bottom, width=1):
    t, b = rgb(top), rgb(bottom)
    im = Image.new("RGB", (width, height))
    for y in range(height):
        f = y / max(height - 1, 1)
        im.paste(tuple(round(t[i] + (b[i] - t[i]) * f) for i in range(3)), (0, y, width, y + 1))
    im.save(out)
    return im


def corners(prefix, radius, fg, bg):
    s = 4  # draw at 4x and downsample for antialiasing against the page colour
    big = Image.new("RGB", (radius * 2 * s, radius * 2 * s), rgb(bg))
    ImageDraw.Draw(big).ellipse((0, 0, radius * 2 * s - 1, radius * 2 * s - 1), fill=rgb(fg))
    circle = big.resize((radius * 2, radius * 2), Image.LANCZOS)
    boxes = {"tl": (0, 0), "tr": (radius, 0), "bl": (0, radius), "br": (radius, radius)}
    paths = []
    for name, (x, y) in boxes.items():
        p = f"{prefix}-{name}.gif"
        circle.crop((x, y, x + radius, y + radius)).convert("P", palette=Image.ADAPTIVE).save(p)
        paths.append(p)
    return paths


def noise(out, base, amount=6, size=128, seed=1):
    rnd = random.Random(seed)
    r, g, b = rgb(base)
    im = Image.new("RGB", (size, size))
    px = im.load()
    for y in range(size):
        for x in range(size):
            d = rnd.randint(-amount, amount)
            px[x, y] = (max(0, min(255, r + d)), max(0, min(255, g + d)), max(0, min(255, b + d)))
    im.save(out)


def button(out, text, bg="#336699", fg="#ffffff", fontpath=None):
    w, h = 88, 31
    im = Image.new("RGB", (w, h), rgb(bg))
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, w - 1, h - 1), outline=(0, 0, 0))
    d.line((1, 1, w - 2, 1), fill=(255, 255, 255)); d.line((1, 1, 1, h - 2), fill=(255, 255, 255))
    d.line((1, h - 2, w - 2, h - 2), fill=(96, 96, 96)); d.line((w - 2, 1, w - 2, h - 2), fill=(96, 96, 96))
    f = ImageFont.truetype(fontpath, 10) if fontpath else ImageFont.load_default()
    lines = text.split("\\n")
    boxes = [d.textbbox((0, 0), ln, font=f) for ln in lines]
    lh = max(b[3] - b[1] for b in boxes) + 2
    y = (h - lh * len(lines)) // 2
    for ln, bx in zip(lines, boxes):
        d.text(((w - (bx[2] - bx[0])) // 2 - bx[0], y - bx[1]), ln, fill=rgb(fg), font=f)
        y += lh
    im.convert("P", palette=Image.ADAPTIVE).save(out)


def _shade(c, k):
    return tuple(max(0, min(255, round(v * k))) for v in c)


def appbutton(out, text, sub=None, width=196, height=56, top="#6db33f", bottom="#3f7f1f", cls="btn"):
    """Two states stacked: normal at 0, hover at -height. Gradient, 1px darker border, inner highlight, letterpress text."""
    sheet = Image.new("RGBA", (width, height * 2), (0, 0, 0, 0))
    big, small = font("sans", 17), font("sans", 10)
    for i, k in enumerate((1.0, 1.08)):
        t, b = _shade(rgb(top), k), _shade(rgb(bottom), k)
        face = Image.new("RGBA", (width, height))
        g = Image.new("RGB", (1, height))
        for y in range(height):
            f = y / max(height - 1, 1)
            g.putpixel((0, y), tuple(round(t[j] + (b[j] - t[j]) * f) for j in range(3)))
        face.paste(g.resize((width, height)), (0, 0))
        mask = Image.new("L", (width, height), 0)
        ImageDraw.Draw(mask).rounded_rectangle((0, 0, width - 1, height - 1), radius=5, fill=255)
        d = ImageDraw.Draw(face)
        d.rounded_rectangle((0, 0, width - 1, height - 1), radius=5, outline=_shade(rgb(bottom), 0.75))
        d.line((4, 1, width - 5, 1), fill=_shade(rgb(top), 1.25))
        lines = [(text, big)] + ([(sub, small)] if sub else [])
        bbs = [d.textbbox((0, 0), s, font=f) for s, f in lines]
        total = sum(bb[3] - bb[1] for bb in bbs) + 4 * (len(lines) - 1)
        y = (height - total) // 2
        for (s, f), bb in zip(lines, bbs):
            x = (width - (bb[2] - bb[0])) // 2 - bb[0]
            d.text((x, y - bb[1] - 1), s, fill=_shade(rgb(bottom), 0.6), font=f)  # letterpress goes up on a dark fill
            d.text((x, y - bb[1]), s, fill=(255, 255, 255), font=f)
            y += bb[3] - bb[1] + 4
        sheet.paste(face, (0, i * height), mask)
    sheet.save(out)
    n = Path(out).name
    print(f".{cls}{{display:block;width:{width}px;height:{height}px;overflow:hidden;text-indent:-999em;"
          f"background:url({n}) no-repeat 0 0}}\n.{cls}:hover{{background-position:0 -{height}px}}")
    return sheet


def sprite(out, inputs, gap=10, prefix=None):
    frames = [Image.open(p).convert("RGBA") for p in inputs]
    im = Image.new("RGBA", (max(f.width for f in frames), sum(f.height for f in frames) + gap * (len(frames) - 1)), (0, 0, 0, 0))
    y, rules = 0, []
    for p, f in zip(inputs, frames):
        im.paste(f, (0, y))
        name = f"{prefix}-{Path(p).stem}" if prefix else Path(p).stem
        rules.append(f".{name}{{width:{f.width}px;height:{f.height}px;background:url({Path(out).name}) no-repeat 0 {-y}px}}")
        y += f.height + gap  # the gap stops a neighbour bleeding in if a box is a few px too tall
    im.save(out)
    print("\n".join(rules))
    return rules


def window(out, width=640, height=400, title="", content=None, shadow=14):
    """Flat window: grey title bar, three flat dots, 1px border, then a baked soft drop shadow."""
    bar = 22
    win = Image.new("RGB", (width, height), (255, 255, 255))
    d = ImageDraw.Draw(win)
    for y in range(bar):
        v = round(236 - 26 * y / (bar - 1))
        d.line((0, y, width, y), fill=(v, v, v))
    d.line((0, bar, width, bar), fill=(160, 160, 160))
    for i, c in enumerate(("#ec6a5e", "#f4bf4f", "#61c554")):
        d.ellipse((8 + i * 20, 5, 20 + i * 20, 17), fill=rgb(c), outline=_shade(rgb(c), 0.8))
    if title:
        f = font("sans", 12)
        bb = d.textbbox((0, 0), title, font=f)
        d.text(((width - (bb[2] - bb[0])) // 2 - bb[0], (bar - (bb[3] - bb[1])) // 2 - bb[1]), title, fill=(60, 60, 60), font=f)
    if content:
        c = Image.open(content).convert("RGB")
        win.paste(c.crop((0, 0, width, height - bar - 1)), (0, bar + 1))
    d.rectangle((0, 0, width - 1, height - 1), outline=(140, 140, 140))
    m = shadow * 2
    out_im = Image.new("RGBA", (width + 2 * m, height + 2 * m), (0, 0, 0, 0))
    sh = Image.new("RGBA", out_im.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rectangle((m, m + shadow // 3, m + width, m + height + shadow // 3), fill=(0, 0, 0, 110))
    out_im = Image.alpha_composite(out_im, sh.filter(ImageFilter.GaussianBlur(shadow / 2)))
    out_im.paste(win, (m, m))
    out_im.save(out)
    print(f'{Path(out).name}: {out_im.width}x{out_im.height}; window at {m},{m}; content area {width}x{height - bar - 1} at {m},{m + bar + 1}')
    return out_im, m


def selftest():
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        spacer(d / "s.gif"); assert Image.open(d / "s.gif").size == (1, 1)
        g = gradient(d / "g.png", 40, "#fff", "#e0e0e0")
        assert g.size == (1, 40) and g.getpixel((0, 0)) == (255, 255, 255) and g.getpixel((0, 39)) == (224, 224, 224)
        ps = corners(str(d / "c"), 6, "#fff", "#d5d6d7"); assert all(Image.open(p).size == (6, 6) for p in ps)
        tl = Image.open(ps[0]).convert("RGB"); assert tl.getpixel((0, 0)) != (255, 255, 255) and tl.getpixel((5, 5)) == (255, 255, 255)
        noise(d / "n.png", "#e6e6e6"); assert Image.open(d / "n.png").size == (128, 128)
        button(d / "b.gif", "GET IT\\nNOW"); assert Image.open(d / "b.gif").size == (88, 31)
        # logo: two colours only (aliased), ink touches the padding on every side (no blank strip)
        logo(d / "l.gif", "Kessler & Sons", "serif", 26, "#900", "#fff", pad=2)
        lg = Image.open(d / "l.gif").convert("RGB")
        assert len(lg.getcolors()) == 2, lg.getcolors()
        ink = Image.eval(lg.convert("L"), lambda v: 255 if v < 200 else 0).getbbox()
        assert ink and ink[0] <= 3 and ink[1] <= 3 and lg.width - ink[2] <= 3 and lg.height - ink[3] <= 3, (ink, lg.size)
        # navmap: areas tile the whole width, no strip left over, few colours
        (w, h), areas = navmap(d / "nav.gif", ["Home", "Tools", "Paint", "Hours"])
        assert areas[0][0] == 0 and areas[-1][1] == w - 1 and h == 22 and len(Image.open(d / "nav.gif").convert("RGB").getcolors()) <= 8
        # appbutton: two states stacked, hover differs, corners transparent
        sh = appbutton(d / "ab.png", "Download", "v1.0")
        assert sh.size == (196, 112) and sh.getpixel((0, 0))[3] == 0 and sh.getpixel((98, 28)) != sh.getpixel((98, 84))
        # sprite: printed offsets land exactly on each frame, with a transparent gap between
        Image.new("RGBA", (48, 48), (255, 0, 0, 255)).save(d / "a.png"); Image.new("RGBA", (40, 40), (0, 0, 255, 255)).save(d / "b.png")
        rules = sprite(d / "sp.png", [d / "a.png", d / "b.png"], gap=10, prefix="icon")
        sp = Image.open(d / "sp.png")
        assert sp.size == (48, 98) and "0 -58px" in rules[1] and sp.getpixel((0, 58)) == (0, 0, 255, 255) and sp.getpixel((0, 50))[3] == 0
        # window: shadow margin is transparent at the corner, the window is opaque, the shadow sits below it
        Image.new("RGB", (300, 200), (10, 20, 30)).save(d / "shot.png")
        wi, m = window(d / "w.png", 300, 200, "Prefs", d / "shot.png")
        assert wi.size == (300 + 4 * 14, 200 + 4 * 14) and wi.getpixel((0, 0))[3] == 0 and wi.getpixel((m + 5, m + 100))[:3] == (10, 20, 30)
        assert 0 < wi.getpixel((m + 150, m + 200 + 6))[3] < 255
    print("selftest ok")


def main():
    if "--selftest" in sys.argv:
        return selftest()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("spacer"); s.add_argument("out")
    s = sub.add_parser("logo"); s.add_argument("out"); s.add_argument("--text", required=True); s.add_argument("--font", default="serif")
    s.add_argument("--size", type=int, default=26); s.add_argument("--fg", default="#000"); s.add_argument("--bg", default="#fff"); s.add_argument("--pad", type=int, default=2)
    s = sub.add_parser("navmap"); s.add_argument("out"); s.add_argument("--labels", required=True); s.add_argument("--href")
    s.add_argument("--font", default="sans"); s.add_argument("--size", type=int, default=12); s.add_argument("--fg", default="#fff")
    s.add_argument("--bg", default="#990000"); s.add_argument("--sep", default="#ffdd00"); s.add_argument("--padx", type=int, default=12); s.add_argument("--height", type=int, default=22)
    s = sub.add_parser("gradient"); s.add_argument("out"); s.add_argument("--height", type=int, required=True)
    s.add_argument("--top", required=True); s.add_argument("--bottom", required=True); s.add_argument("--width", type=int, default=1)
    s = sub.add_parser("corners"); s.add_argument("prefix"); s.add_argument("--radius", type=int, required=True)
    s.add_argument("--fg", required=True); s.add_argument("--bg", required=True)
    s = sub.add_parser("noise"); s.add_argument("out"); s.add_argument("--base", required=True)
    s.add_argument("--amount", type=int, default=6); s.add_argument("--size", type=int, default=128); s.add_argument("--seed", type=int, default=1)
    s = sub.add_parser("button"); s.add_argument("out"); s.add_argument("--text", required=True)
    s.add_argument("--bg", default="#336699"); s.add_argument("--fg", default="#ffffff"); s.add_argument("--font")
    s = sub.add_parser("appbutton"); s.add_argument("out"); s.add_argument("--text", required=True); s.add_argument("--sub")
    s.add_argument("--width", type=int, default=196); s.add_argument("--height", type=int, default=56)
    s.add_argument("--top", default="#6db33f"); s.add_argument("--bottom", default="#3f7f1f"); s.add_argument("--class", dest="cls", default="btn")
    s = sub.add_parser("sprite"); s.add_argument("out"); s.add_argument("inputs", nargs="+"); s.add_argument("--gap", type=int, default=10); s.add_argument("--prefix")
    s = sub.add_parser("window"); s.add_argument("out"); s.add_argument("--width", type=int, default=640); s.add_argument("--height", type=int, default=400)
    s.add_argument("--title", default=""); s.add_argument("--content"); s.add_argument("--shadow", type=int, default=14)
    a = ap.parse_args()
    if a.cmd == "spacer": spacer(a.out)
    elif a.cmd == "logo": logo(a.out, a.text, a.font, a.size, a.fg, a.bg, a.pad)
    elif a.cmd == "navmap": navmap(a.out, a.labels.split("|"), a.href.split("|") if a.href else None, a.font, a.size, a.fg, a.bg, a.sep, a.padx, a.height)
    elif a.cmd == "gradient": gradient(a.out, a.height, a.top, a.bottom, a.width)
    elif a.cmd == "corners": print("\n".join(corners(a.prefix, a.radius, a.fg, a.bg)))
    elif a.cmd == "noise": noise(a.out, a.base, a.amount, a.size, a.seed)
    elif a.cmd == "button": button(a.out, a.text, a.bg, a.fg, a.font)
    elif a.cmd == "appbutton": appbutton(a.out, a.text, a.sub, a.width, a.height, a.top, a.bottom, a.cls)
    elif a.cmd == "sprite": sprite(a.out, a.inputs, a.gap, a.prefix)
    elif a.cmd == "window": window(a.out, a.width, a.height, a.title, a.content, a.shadow)


if __name__ == "__main__":
    main()
