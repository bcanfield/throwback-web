# throwback-web

An agent skill that makes your AI build a website like it's 1999. On purpose.

Every AI-built site now has the same rounded cards, the same gradient, the same Inter. This skill tells the agent to go the other way and commit: table layouts, `<font>` tags, rounded corners cut from GIFs, an 88x31 badge or two. A real person from that year should take the result for a real site.

## Install

It's a Claude Code skill (Agent Skills format). Copy or symlink the inner folder into your skills directory:

```sh
git clone https://github.com/bcanfield/throwback-web
ln -s "$PWD/throwback-web/throwback-web" ~/.claude/skills/throwback-web
```

## Use it

```
Build a landing page for my bike repair shop. Make it look like 2001.
```

It picks the era from what the site does, so "make it look old" works too.

## Eras

- **1996-2003:** tables, spacer GIFs, a `<font>` tag on every line, the whole nav as one image map.
- **2004-2009:** Web 2.0. A centred 760px column, tag clouds, corners cut from GIFs, Prototype.js.
- **2010-2013:** skeuomorphic and early CSS3. Noise textures, Typekit, Bootstrap 2, vendor prefixes applied unevenly.

What it won't do is the cartoon. No starbursts, no reflections, no linen. We checked: real sites mostly didn't either.

## Two modes

- **Costume** (default): the look is faithful, but it's safe to ship today. No fake tracking IDs, no dead scripts, no Flash.
- **Artifact:** every period fingerprint kept. For art pieces and museum recreations.

## What's in the box

- `scripts/lint_era.py` checks a page for anachronisms that give the game away.
- `scripts/make_assets.py` makes spacer GIFs, 88x31 buttons, sprites and similar.
- `research/` is the homework behind it, checked against real Wayback captures and test builds.

Best viewed in Netscape Navigator 4 at 800x600. (Any browser works.)
