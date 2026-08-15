#!/usr/bin/env python3
"""Generate a wildflower-meadow-at-dawn hero background as a self-contained SVG."""

import math
import random

random.seed(11)

W, H = 1600, 900
out = []
a = out.append


def r(v, n=1):
    return round(v, n)


def ridge(y0, amp, seg, jitter=0.35, base=H):
    """Smooth-ish mountain silhouette path across the full width."""
    pts = []
    x = -160
    while x < W + 200:
        peak = y0 - amp * (0.45 + random.random())
        pts.append((x, peak if random.random() > jitter else y0 + amp * 0.25 * random.random()))
        x += seg * (0.6 + 0.8 * random.random())
    pts.append((W + 260, y0 - amp * (0.3 + 0.5 * random.random())))
    d = [f"M{pts[0][0]:.0f},{pts[0][1]:.0f}"]
    for i in range(1, len(pts)):
        px, py = pts[i - 1]
        cx, cy = pts[i]
        mx = (px + cx) / 2
        d.append(f"Q{px + (mx - px) * 0.5:.0f},{py:.0f} {mx:.0f},{(py + cy) / 2:.0f}")
        d.append(f"Q{cx - (cx - mx) * 0.5:.0f},{cy:.0f} {cx:.0f},{cy:.0f}")
    d.append(f"L{W + 260},{base} L-160,{base} Z")
    return " ".join(d)


def hill(y_left, y_ctrl, y_right, base=H):
    return (f"M-60,{y_left:.0f} Q{W * 0.3:.0f},{y_ctrl:.0f} {W * 0.6:.0f},{(y_ctrl + y_right) / 2:.0f} "
            f"T{W + 120},{y_right:.0f} L{W + 120},{base} L-60,{base} Z")


a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice" '
  f'role="img" aria-label="Wildflower meadow overlooking misty mountains at dawn">')

# ---------------------------------------------------------------- definitions
a('<defs>')
a('<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%" stop-color="#E4E2EE"/>'
  '<stop offset="26%" stop-color="#EAE4EE"/>'
  '<stop offset="52%" stop-color="#F1E6E9"/>'
  '<stop offset="74%" stop-color="#F7E9E0"/>'
  '<stop offset="100%" stop-color="#FAEFE6"/></linearGradient>')
a('<radialGradient id="dawnglow" cx="0.42" cy="0.92" r="0.75">'
  '<stop offset="0%" stop-color="#FFE9CE" stop-opacity="0.95"/>'
  '<stop offset="55%" stop-color="#FFE3D2" stop-opacity="0.35"/>'
  '<stop offset="100%" stop-color="#FFE3D2" stop-opacity="0"/></radialGradient>')
a('<linearGradient id="far" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%" stop-color="#B9BFD6"/><stop offset="100%" stop-color="#CFD3E4"/></linearGradient>')
a('<linearGradient id="mid" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%" stop-color="#9AA6C2"/><stop offset="100%" stop-color="#B4BDD4"/></linearGradient>')
a('<linearGradient id="near" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%" stop-color="#77879F" stop-opacity="0.95"/>'
  '<stop offset="100%" stop-color="#93A2B4" stop-opacity="0.9"/></linearGradient>')
a('<linearGradient id="valley" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%" stop-color="#E9C99A"/><stop offset="100%" stop-color="#D9BC92"/></linearGradient>')
a('<linearGradient id="ridgeGreen" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%" stop-color="#7C8F72"/><stop offset="100%" stop-color="#6B8064"/></linearGradient>')
a('<linearGradient id="meadow1" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%" stop-color="#A3AC80"/><stop offset="100%" stop-color="#8B9769"/></linearGradient>')
a('<linearGradient id="meadow2" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%" stop-color="#96A473"/><stop offset="100%" stop-color="#7B8B5C"/></linearGradient>')
a('<linearGradient id="meadow3" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%" stop-color="#87975F" stop-opacity="0.98"/>'
  '<stop offset="100%" stop-color="#6C7E4C"/></linearGradient>')
a('<linearGradient id="mist" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0%" stop-color="#FFFFFF" stop-opacity="0"/>'
  '<stop offset="45%" stop-color="#FFFBF7" stop-opacity="0.9"/>'
  '<stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>')
a('<filter id="blurL" x="-25%" y="-140%" width="150%" height="380%"><feGaussianBlur stdDeviation="30"/></filter>')
a('<filter id="blurS" x="-25%" y="-140%" width="150%" height="380%"><feGaussianBlur stdDeviation="14"/></filter>')
a('<filter id="soften" x="-8%" y="-8%" width="116%" height="116%"><feGaussianBlur stdDeviation="1.1"/></filter>')
a('</defs>')

# ------------------------------------------------------------------- backdrop
a(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
a(f'<rect width="{W}" height="{H}" fill="url(#dawnglow)"/>')

# thin cloud streaks
for i in range(9):
    cy = 120 + i * 34 + random.random() * 22
    cw = 320 + random.random() * 760
    cx = random.random() * W
    a(f'<ellipse cx="{r(cx)}" cy="{r(cy)}" rx="{r(cw / 2)}" ry="{r(7 + random.random() * 11)}" '
      f'fill="#FFFFFF" opacity="{r(0.16 + random.random() * 0.2, 2)}" filter="url(#blurS)"/>')

# ------------------------------------------------------------- mountain bands
a(f'<path d="{ridge(452, 46, 165)}" fill="url(#far)" opacity="0.55"/>')
a(f'<rect x="-40" y="436" width="{W + 80}" height="70" fill="url(#mist)" filter="url(#blurL)"/>')

a(f'<path d="{ridge(484, 58, 190)}" fill="url(#mid)" opacity="0.7"/>')
a(f'<rect x="-40" y="470" width="{W + 80}" height="76" fill="url(#mist)" filter="url(#blurL)"/>')

# sunlit valley floor glimpsed between the ranges
a(f'<path d="{hill(536, 520, 546, 620)}" fill="url(#valley)" opacity="0.85"/>')
a(f'<rect x="-40" y="506" width="{W + 80}" height="72" fill="url(#mist)" filter="url(#blurL)"/>')

a(f'<path d="{ridge(524, 52, 210)}" fill="url(#near)" opacity="0.9"/>')
a(f'<rect x="-40" y="520" width="{W + 80}" height="66" fill="url(#mist)" filter="url(#blurL)"/>')

# green shoulder ridges that frame the meadow
a(f'<path d="{hill(556, 590, 512, 760)}" fill="url(#ridgeGreen)" opacity="0.92"/>')
a(f'<path d="M-60,566 Q220,512 470,560 T1010,556 Q1290,512 1660,540 L1660,760 L-60,760 Z" '
  f'fill="#6E8262" opacity="0.55"/>')
a(f'<rect x="-40" y="548" width="{W + 80}" height="58" fill="url(#mist)" filter="url(#blurL)" opacity="0.75"/>')

# ------------------------------------------------------------------- meadow
def crest(y_base, amp, phase, wobble=1.0):
    """Rolling meadow crest: smooth sinusoidal ridge with light irregularity."""
    pts = []
    steps = 14
    for i in range(steps + 1):
        t = i / steps
        x = -160 + t * (W + 420)
        y = (y_base
             - amp * math.sin(t * math.pi * wobble + phase)
             - amp * 0.28 * math.sin(t * math.pi * 2.7 + phase * 1.7))
        pts.append((x, y))
    d = [f"M{pts[0][0]:.0f},{pts[0][1]:.0f}"]
    for i in range(1, len(pts)):
        px, py = pts[i - 1]
        cx, cy = pts[i]
        d.append(f"C{px + (cx - px) / 2:.0f},{py:.0f} {px + (cx - px) / 2:.0f},{cy:.0f} {cx:.0f},{cy:.0f}")
    d.append(f"L{W + 260},{H} L-160,{H} Z")
    return " ".join(d), pts


PALETTE = [
    "#F3BFD6", "#EAA6C6", "#F8D8E6", "#FFFFFF", "#FCF5E7",
    "#C9AEE2", "#AB90D4", "#DECCEF", "#F4DF95", "#F1CC6B",
    "#F7F1DE", "#EA8CA3", "#C3DDF2", "#FBE9F2",
]

bands = [
    # fill,           y_base, amp, phase, wobble, clusters, per, spread, size,        alpha
    ("url(#meadow1)", 606, 22, 0.4, 1.6, 64, 22, (150, 20), (1.1, 2.3), 0.62),
    ("url(#meadow2)", 690, 30, 2.1, 1.2, 78, 36, (140, 30), (1.8, 3.8), 0.82),
    ("url(#meadow3)", 792, 26, 4.2, 0.9, 88, 52, (130, 36), (2.6, 6.0), 0.97),
]

for fill, y_base, amp, phase, wobble, clusters, per, spread, size, alpha in bands:
    path, pts = crest(y_base, amp, phase, wobble)
    a(f'<path d="{path}" fill="{fill}"/>')

    # sunlit rim along the crest
    rim = " ".join(
        [f"M{pts[0][0]:.0f},{pts[0][1]:.0f}"] +
        [f"L{p[0]:.0f},{p[1]:.0f}" for p in pts[1:]]
    )
    a(f'<path d="{rim}" fill="none" stroke="#E8E3B4" stroke-width="7" opacity="0.3" filter="url(#blurS)"/>')

    lo = min(p[1] for p in pts)
    span = max(60.0, H - lo)

    # grass texture: soft horizontal streaks following the slope
    for _ in range(int(clusters * per * 0.22)):
        gx = random.random() * (W + 320) - 160
        t = max(0.0, min(1.0, (gx + 160) / (W + 420)))
        top = y_base - amp * math.sin(t * math.pi * wobble + phase)
        gy = top + random.random() * (H - top)
        depth = (gy - top) / max(1.0, H - top)
        a(f'<ellipse cx="{r(gx)}" cy="{r(gy)}" rx="{r(16 + depth * 52)}" ry="{r(1.5 + depth * 3.6)}" '
          f'fill="#FCF3DF" opacity="{r(0.04 + random.random() * 0.1, 2)}"/>')

    # flowers, scattered in drifts rather than evenly
    a('<g filter="url(#soften)">')
    for _ in range(clusters):
        cx0 = random.random() * (W + 320) - 160
        t = max(0.0, min(1.0, (cx0 + 160) / (W + 420)))
        top = y_base - amp * math.sin(t * math.pi * wobble + phase)
        cy0 = top + random.random() * (H - top)
        drift = random.sample(PALETTE, 3)
        for _ in range(per):
            fx = cx0 + random.gauss(0, spread[0] * 0.34)
            fy = cy0 + random.gauss(0, spread[1])
            if fy < top - 2 or fy > H + 12:
                continue
            depth = max(0.0, min(1.0, (fy - lo) / span))
            rad = size[0] + (size[1] - size[0]) * (0.3 + 0.7 * depth) * (0.55 + random.random() * 0.9)
            col = random.choice(drift) if random.random() > 0.25 else random.choice(PALETTE)
            op = alpha * (0.5 + 0.5 * random.random())
            a(f'<circle cx="{fx:.0f}" cy="{fy:.0f}" r="{rad:.1f}" fill="{col}" opacity="{op:.2f}"/>')
            if depth > 0.5 and rad > size[1] * 0.55 and random.random() > 0.7:
                a(f'<rect x="{r(fx - 0.5)}" y="{r(fy)}" width="1" height="{r(4 + random.random() * 10)}" '
                  f'fill="#5C7046" opacity="{r(0.3 + random.random() * 0.3, 2)}"/>')
    a('</g>')

# warm light wash from the horizon over the meadow edge
a(f'<rect x="0" y="540" width="{W}" height="150" fill="#FFE6C8" opacity="0.18" filter="url(#blurL)"/>')

a('</svg>')

svg = "\n".join(out)
with open("/Users/feniljikadara/Documents/Projects/hero-bg.svg", "w") as f:
    f.write(svg + "\n")

print(f"{len(svg) / 1024:.1f} KB")
