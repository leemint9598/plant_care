"""Draws the landing page's timelapse strip: one plant in the same pot, from
seedling to fruiting, in seven frames.

Uses the app's painted-icon helpers (../flutter_plant_id/tool/design/painted.py)
so the pot, leaves and colored-pencil texture match the app exactly.

    python3 tools/growth_frames.py   # writes assets/growth/frame-1.svg … frame-7.svg
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "flutter_plant_id", "tool", "design"))
from painted import DEFS, LEAF2, LEAF_D, SUN, LIME, leaf, line, pot, sparkle, tomato  # noqa: E402

FILTER = re.search(r"<filter.*</filter>", DEFS).group(0)
W, H = 90, 160          # a 9:16 frame, like the exported video
CX, POT_TOP = 45, 116   # the pot never moves — that is the point of the ghost overlay
BG = "#EDEFE4"          # a paper-coloured "photo"


def stage(n):
    """The plant at week n (1–7): taller stem, more leaves, then fruit."""
    top = POT_TOP
    h = [10, 20, 32, 44, 56, 68, 78][n - 1]
    out = line(f"M{CX} {top}c-1-{h * 0.4} 2-{h * 0.7} 0-{h}", LEAF_D, 2 + n * 0.25)
    # leaves alternate up the stem, growing with the plant
    for i in range(min(2 + n, 8)):
        frac = (i + 1) / (min(2 + n, 8) + 0.6)
        y = top - h * frac
        left = i % 2 == 0
        s = 0.5 + 0.07 * n - 0.03 * (i if n > 3 else 0)
        out += leaf(CX, y, -70 + i * 6 if left else 25 - i * 4, max(s, 0.42), LEAF2 if not left else "#6E9A45")
    if n >= 4:  # side branch
        out += line(f"M{CX} {top - h * 0.55}c6-3 11-8 13-15", LEAF_D, 1.8)
        out += leaf(CX + 13, top - h * 0.55 - 15, 10, 0.55 + 0.05 * n, LEAF2)
    if n >= 6:
        out += tomato(CX - 9, top - h * 0.45, 4.2 + (n - 6) * 1.4)
    if n >= 7:
        out += tomato(CX + 11, top - h * 0.62, 4.6) + tomato(CX - 4, top - h * 0.78, 3.8)
    if n == 7:
        out += sparkle(16, 22, 5, SUN) + sparkle(76, 34, 4, LIME)
    return out


def frame(n):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W * 2}" height="{H * 2}">'
            f'<defs>{FILTER}</defs>'
            f'<rect width="{W}" height="{H}" fill="{BG}"/>'
            f'<ellipse cx="{CX}" cy="{POT_TOP + 38}" rx="30" ry="4" fill="#D9DCCB"/>'
            f'<g filter="url(#paint)">{stage(n)}{pot(CX, POT_TOP, 50, 36)}</g></svg>')


if __name__ == "__main__":
    out = os.path.join(HERE, "..", "assets", "growth")
    os.makedirs(out, exist_ok=True)
    for n in range(1, 8):
        with open(os.path.join(out, f"frame-{n}.svg"), "w") as f:
            f.write(frame(n))
    print("wrote 7 frames")
