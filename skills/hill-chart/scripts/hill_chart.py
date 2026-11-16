#!/usr/bin/env python3
"""Render a Shape Up hill chart as SVG and flag stuck or backsliding scopes.

Usage:
  hill_chart.py scopes.json out.svg [--previous older.json]

scopes.json:
  {"title": "Holder v2", "date": "2026-11-20",
   "scopes": [{"name": "Snap clips", "position": 35}, ...]}

position runs 0-100: 0-50 is uphill (figuring it out), 50 is the top (approach
known, all work visible), 50-100 is downhill (executing), 100 is done.

With --previous, prints a warning for each scope that hasn't moved (stuck) or
moved back after passing the top (backslid). Exits 0 either way.
"""
import json
import math
import sys
from xml.sax.saxutils import escape

W, H = 960, 420
LEFT, RIGHT, BASE, PEAK = 60, 900, 330, 110
PALETTE = ["#E07A2E", "#3B82C4", "#2E8B57", "#8E44AD", "#C0392B", "#B8860B", "#16A085", "#7F8C8D"]


def curve_y(pos):
    x = (pos - 50) / 50  # -1..1
    return BASE - (BASE - PEAK) * math.exp(-4.5 * x * x)


def curve_x(pos):
    return LEFT + (RIGHT - LEFT) * pos / 100


def load(path):
    with open(path) as f:
        data = json.load(f)
    for s in data.get("scopes", []):
        p = s.get("position")
        if not isinstance(p, (int, float)) or not 0 <= p <= 100:
            raise SystemExit(f"{path}: scope '{s.get('name')}' needs a position from 0 to 100")
    return data


def render(data):
    pts = " ".join(f"{curve_x(p):.1f},{curve_y(p):.1f}" for p in range(0, 101))
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
        f'aria-label="Hill chart: {escape(data.get("title", ""))}" font-family="Arial, sans-serif">',
        f'<rect width="{W}" height="{H}" fill="#F6F4EE"/>',
        f'<text x="{LEFT}" y="40" font-size="22" font-weight="700" fill="#161B26">'
        f'{escape(data.get("title", "Hill chart"))}</text>',
        f'<text x="{RIGHT}" y="40" font-size="16" fill="#4A5568" text-anchor="end">{escape(data.get("date", ""))}</text>',
        f'<polyline points="{pts}" fill="none" stroke="#161B26" stroke-width="3"/>',
        f'<line x1="{curve_x(50):.1f}" y1="{PEAK - 20}" x2="{curve_x(50):.1f}" y2="{BASE + 10}" '
        f'stroke="#9AA3B2" stroke-dasharray="6 6"/>',
        f'<text x="{curve_x(25):.1f}" y="{BASE + 45}" font-size="16" fill="#4A5568" text-anchor="middle">'
        f'Figuring things out</text>',
        f'<text x="{curve_x(75):.1f}" y="{BASE + 45}" font-size="16" fill="#4A5568" text-anchor="middle">'
        f'Making it happen</text>',
    ]
    scopes = sorted(data.get("scopes", []), key=lambda s: s["position"])
    for i, s in enumerate(scopes):
        p = s["position"]
        x, y = curve_x(p), curve_y(p)
        color = s.get("color") or PALETTE[i % len(PALETTE)]
        ly = y - 22 - (i % 3) * 22
        anchor = "end" if p > 50 else "start"
        lx = x - 10 if p > 50 else x + 10
        out.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{lx:.1f}" y2="{ly + 4:.1f}" stroke="{color}" stroke-width="1.5"/>')
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" fill="{color}" stroke="#F6F4EE" stroke-width="3"/>')
        out.append(f'<text x="{lx:.1f}" y="{ly:.1f}" font-size="16" fill="#161B26" text-anchor="{anchor}" '
                   f'stroke="#F6F4EE" stroke-width="5" paint-order="stroke">'
                   f'{escape(s["name"])}</text>')
    out.append("</svg>")
    return "\n".join(out)


def compare(old, new):
    before = {s["name"]: s["position"] for s in old.get("scopes", [])}
    for s in new.get("scopes", []):
        prev = before.get(s["name"])
        if prev is None:
            continue
        if s["position"] == prev and s["position"] < 100:
            print(f"STUCK: '{s['name']}' hasn't moved from {prev}. Ask what's unknown.")
        elif prev >= 50 and s["position"] < prev:
            print(f"BACKSLID: '{s['name']}' moved back from {prev} to {s['position']}. "
                  "Work was solved in the head, not by building; split or re-shape it.")
    for s in new.get("scopes", []):
        if 40 <= s["position"] <= 60 and " and " in s["name"]:
            print(f"MIXED?: '{s['name']}' may hide parts at different stages; consider splitting.")


def main(argv):
    if len(argv) < 3:
        raise SystemExit(__doc__)
    data = load(argv[1])
    with open(argv[2], "w") as f:
        f.write(render(data))
    if "--previous" in argv:
        compare(load(argv[argv.index("--previous") + 1]), data)


if __name__ == "__main__":
    main(sys.argv)
