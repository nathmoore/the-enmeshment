#!/usr/bin/env python3
"""Regenerate the 11 per-archetype OG share cards (1200x630 PNG).

    python3 site/tools/build-cards.py

Reads `archetype` and `status` from each site/files/<slug>.md front matter, writes an
SVG per archetype from the template below, and rasterises it with macOS Quick Look
(/usr/bin/qlmanage) — this machine has no imagemagick/rsvg/inkscape.

qlmanage only ever emits a SQUARE thumbnail: hand it a 1200x630 document and it
scales-to-fit and clips. So the card is drawn into a 1200x1200 canvas, vertically
centred (285px letterbox top and bottom), rasterised 1:1, then centre-cropped back to
1200x630 with `sips -c 630 1200`. That round-trip is exact — verified pixel-for-pixel.

SVGs are written to a temp dir; only the PNGs land in site/assets/files/ (they are
committed, because GitHub Pages serves them and the build does not run this script).

No third-party assets or fonts: system monospace only, same leaked-file visual
language as assets/css/site.css.
"""

import html
import pathlib
import re
import shutil
import subprocess
import tempfile

SITE = pathlib.Path(__file__).resolve().parent.parent   # site/
FILES = SITE / "files"
HERE = SITE / "assets" / "files"                         # where the PNGs land

W, H = 1200, 630
PAD = (W - H) // 2                            # letterbox for the square rasteriser
PAPER, FORM = "#f4f1e9", "#fbf9f4"
INK, INK_SOFT, RULE_HARD, RULE, STAMP = "#1b1917", "#5d564c", "#9d9483", "#cdc5b4", "#93392c"
MONO = "ui-monospace, 'SF Mono', Menlo, Monaco, Consolas, monospace"

MARGIN = 96
COL = W - 2 * MARGIN                          # usable text width


def mono_width(text, size, tracking=0.0):
    """Monospace advance is ~0.6em; add letter-spacing."""
    return len(text) * (size * 0.6 + tracking)


def card_svg(archetype, status):
    name = archetype.upper()
    size = 86.0
    while mono_width(name, size, 2.0) > COL and size > 40:
        size -= 1

    stamp_text = f"FILE STATUS: {status.upper()}"
    stamp_size, stamp_track = 26.0, 3.0
    stamp_w = mono_width(stamp_text, stamp_size, stamp_track) + 52
    stamp_h = 60

    e = html.escape
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{W}"
     viewBox="0 0 {W} {W}" font-family="{e(MONO)}">
  <rect width="{W}" height="{W}" fill="{PAPER}"/>
  <g transform="translate(0 {PAD})">
  <rect width="{W}" height="{H}" fill="{PAPER}"/>
  <rect x="40" y="40" width="{W - 80}" height="{H - 80}" fill="{FORM}"
        stroke="{RULE_HARD}" stroke-width="2"/>

  <text x="{MARGIN}" y="140" font-size="21" letter-spacing="3.4" fill="{INK_SOFT}"
        >ENMESHMENT DIRECTORATE &#8212; UNOFFICIAL EXTRACT</text>
  <line x1="{MARGIN}" y1="166" x2="{W - MARGIN}" y2="166" stroke="{RULE}" stroke-width="2"/>

  <text x="{MARGIN}" y="250" font-size="27" letter-spacing="1.5" fill="{INK_SOFT}"
        >Subject classification:</text>
  <text x="{MARGIN}" y="{250 + size + 22:.0f}" font-size="{size:.0f}" letter-spacing="2"
        font-weight="700" fill="{INK}">{e(name)}</text>

  <g transform="translate({MARGIN} 440) rotate(-1.25)">
    <rect x="0" y="0" width="{stamp_w:.0f}" height="{stamp_h}" fill="none"
          stroke="{STAMP}" stroke-width="3"/>
    <text x="26" y="39" font-size="{stamp_size:.0f}" letter-spacing="{stamp_track}"
          fill="{STAMP}">{e(stamp_text)}</text>
  </g>

  <line x1="{MARGIN}" y1="520" x2="{W - MARGIN}" y2="520" stroke="{RULE}" stroke-width="2"/>
  <text x="{MARGIN}" y="558" font-size="26" letter-spacing="2.5" fill="{INK}"
        >The Enmeshment</text>
  </g>
</svg>
"""


def front_matter(path):
    text = path.read_text()
    block = text.split("---", 2)[1]
    grab = lambda k: re.search(rf'^{k}:\s*"?(.*?)"?\s*$', block, re.M).group(1)
    return grab("archetype"), grab("status")


def main():
    ql = "/usr/bin/qlmanage"
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="enmeshment-cards-"))
    made = []
    for md in sorted(FILES.glob("*.md")):
        slug = md.stem
        archetype, status = front_matter(md)
        svg = tmp / f"{slug}.svg"
        svg.write_text(card_svg(archetype, status))
        subprocess.run([ql, "-t", "-s", str(W), "-o", str(tmp), str(svg)],
                       check=True, capture_output=True)
        png = tmp / f"{slug}.svg.png"
        if not png.exists():
            raise SystemExit(f"qlmanage produced no PNG for {slug}")
        out = HERE / f"{slug}.png"
        subprocess.run(["sips", "-c", str(H), str(W), str(png), "--out", str(out)],
                       check=True, capture_output=True)
        made.append(slug)
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"wrote {len(made)} cards -> {HERE}")
    for slug in made:
        out = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight",
                              str(HERE / f"{slug}.png")], capture_output=True, text=True)
        dims = " ".join(l.split(": ")[-1] for l in out.stdout.splitlines() if ":" in l and "pixel" in l)
        print(f"  {slug:18s} {dims}")


if __name__ == "__main__":
    main()
