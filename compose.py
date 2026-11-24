#!/usr/bin/env python3
"""THE UNIVERSAL LEDGER — compose.py (NI23 G3, akun18).

Renders the front page of a one-day world newspaper for Monday
23 November 2026 as a 1024x1024 PNG. All stories come from the locked
NI23 pool; the lead is pool story 32 (Tata Steel pipe sale).
Variants: A = cream/grape (house palette), B = white/oxblood,
C = parchment/teal. Usage: python3 compose.py [A|B|C] [out.png]
Map: dotted_map() draws an original dotted world from hand-made
continent polygons (no geojson file, no external assets).
"""
import sys
from PIL import Image, ImageDraw, ImageFont

FDIR = "/home/hatch/workspace/tools/bedah-19nov/news-image/fonts/"
W = 1024
M = 26
CW = W - 2 * M


def F(name, size):
    return ImageFont.truetype(FDIR + name, size)


def fb(n):   # headline serif (Playfair)
    return F("PlayfairDisplay-Bold.ttf", n)


def fblack(n):
    return F("PlayfairDisplay-Black.ttf", n)


def fr(n):   # body sans (Archivo)
    return F("Archivo.ttf", n)


def fbb(n):  # bold sans
    return F("Archivo-Bold.ttf", n)


def fsr(n):  # small sans (briefs / footer)
    return F("Archivo.ttf", n)


REGION_COLORS = {
    "MIDDLE EAST": (146, 64, 32),
    "NORTH AMERICA": (30, 84, 140),
    "EUROPE": (38, 110, 90),
    "SOUTH ASIA": (178, 92, 20),
    "SE ASIA": (120, 60, 150),
    "GLOBAL": (90, 90, 90),
    "AFRICA": (150, 120, 30),
}

# ---- the day in numbers: (value, label) --------------------------------
NUMS = [
    ("Rs 28,000 cr", "Tata Steel pipe sale"),
    ("258-173", "Democrats House win"),
    ("720/9d", "India Test record"),
    ("$3,538", "gold per ounce"),
    ("65.9%", "IndiGo domestic share"),
    ("700,000", "Rohingya fled Myanmar"),
    ("$5M", "Google IIT grant"),
    ("7 + 50", "Indonesia fire toll"),
]

# ---- timeline of the day (UTC) ------------------------------------------
TL = [
    ("00:02Z", "AI-weapons talks"),
    ("02:00Z", "Albanese reacts"),
    ("06:40Z", "Kyiv boy freed"),
    ("11:30Z", "House count set"),
    ("16:45Z", "Gold fix $3,538"),
    ("21:10Z", "Alcaraz triumph"),
]

# ---- also on the front page (briefs, numbered on the page) --------------
BRIEFS_L = [
    "15. IRGC claims 2 Patriot radars hit",
    "16. Houthi missile intercepted",
    "17. Swimmer crosses Hormuz strait",
    "18. UN talks on killer AI weapons",
    "19. US releases new UFO footage",
    "20. Albanese: COP31 a hard moment",
    "21. Towed ship: Gulf of Finland",
    "22. Drone blast in Benghazi port",
]
BRIEFS_R = [
    "23. Kyiv: 14 missing after strike",
    "24. UK-EU Brexit reset deal hailed",
    "25. Lisbon marches on living costs",
    "26. ASEAN ruling unfair: Myanmar",
    "27. Cameroon ex-rebels in limbo",
    "28. Escaped lion scares Turkiye town",
    "29. Nepal PM Shah meets Modi",
    "30. India, Bulgaria discuss IMEC",
]
BRIEFS = [
    "31. Guru Nanak Jayanti marked",
    "32. UP air-raid drill: 75 districts",
    "33. NZ 119/2 as India chase win",
    "34. India win ODI series 3-2 in NZ",
    "35. Anupama keeps IBSF snooker title",
    "36. World Chess draws big crowds",
    "37. MP Wadkute dies in Delhi",
    "38. Kota pilgrim bus crash: 9 dead",
    "39. SpiceJet audit call; IndiGo 65.9%",
    "40. IFFI hosts BRICS table in Goa",
    "41. Arunachal infra push Rs 4,000 cr",
]

# ---- date check: named rejects with their real dates --------------------
dc = ("DATE CHECK - checked and left out, NOT 23 Nov: "
      "Xi-Trump-Putin summit - 19 Nov 2026 · "
      "SpiceJet Rs 5,500 cr raise - 18 Nov 2026 · "
      "Paolo Bulgari died - told 22 Nov 2026 · "
      "24 civilians killed, S. Sudan - 22 Nov 2026 · "
      "Bolsonaro stable in ICU - 22 Nov 2026 · "
      "S. Korea minister quits - told 22 Nov 2026 · "
      "Indonesia candy-factory fire itself - 22 Nov 2026")

# ---- map pins: (story number, lon, lat) ----------------------------------
PINS = [
    (1, 73.0, 19.0), (2, -77.0, 39.0), (3, 31.6, 50.4),
    (4, 174.8, -41.3), (5, 0.0, 51.5), (6, 56.3, 26.6),
    (7, 30.7, 36.9), (8, 96.0, 21.9), (9, -98.0, 39.0),
    (10, 107.0, -6.8), (11, 7.7, 45.1), (12, 87.3, 22.3),
    (13, 24.9, 59.9),
]

# ---- mini cards: (num, region, topic, src, head, deck, kind) -------------
grid = [
    (2, "NORTH AMERICA", "US POLITICS", "BBC 23 Nov",
     "Democrats Take House, 258-173",
     "Largest Democratic majority since 1992; a North Carolina flip.",
     "capitol"),
    (3, "EUROPE", "UKRAINE", "BBC 23 Nov",
     "Boy of 7 Freed From Kyiv Rubble",
     "Freed after hours under debris; 6 died in the Russian strike.",
     "rescue"),
    (4, "SOUTH ASIA", "CRICKET", "ObserverVoice 23 Nov",
     "India Post Record 720/9 in NZ",
     "Highest Test total made in New Zealand; marks since 1930 fall.",
     "cricket"),
    (5, "GLOBAL", "MARKETS", "ObserverVoice 23 Nov",
     "Gold Falls to $3,538 an Ounce",
     "Down over $2,000 from the 2026 record $5,595; off 2.41% Friday.",
     "gold"),
    (6, "MIDDLE EAST", "GULF WAR", "AP live 23 Nov",
     "Tanker Burns in Hormuz Strait",
     "Iran-US war widens in the Gulf; IRGC claims US radar strikes.",
     "tanker"),
    (7, "EUROPE", "CLIMATE", "BBC / AP 23 Nov",
     "COP31 Ends With No Deal",
     "Final Turkish draft omits fossil fuels; 2 weeks of talks fail.",
     "summit"),
    (8, "SE ASIA", "WORLD COURT", "Guardian / NYT 23 Nov",
     "ICJ: Myanmar Guilty of Genocide",
     "Court cites the 2017 Rohingya campaign; 700,000 fled homes.",
     "scales"),
    (9, "NORTH AMERICA", "SECURITY", "AP wire 23 Nov",
     "FBI Probes Database Hack",
     "Agents probe a breach of the main US database in Washington.",
     "database"),
    (10, "SE ASIA", "DISASTER", "JagranJosh 23 Nov",
     "Indonesia Fire: 7 Found, 50 Lost",
     "The 23 November update from the candy-factory fire in Java.",
     "fire"),
    (11, "EUROPE", "TENNIS", "BBC 23 Nov",
     "Alcaraz Beats Zverev in Turin",
     "A first ATP Finals title for Alcaraz over Alexander Zverev.",
     "tennis"),
    (12, "SOUTH ASIA", "TECHNOLOGY", "JagranJosh 23 Nov",
     "Google Gives $5M to IIT",
     "Grant funds AI research at IIT Kharagpur; 1 of 5 awards.",
     "chip"),
    (13, "EUROPE", "BALTIC", "BBC / JagranJosh 23 Nov",
     "Russian Ship Burns Off Finland",
     "Freighter burns a 2nd day in the Gulf of Finland post-attack.",
     "ship"),
]

# ---- hand-made continent polygons (lon, lat) for the dotted map ---------
CONTINENTS = [
    [(-168, 66), (-140, 70), (-125, 72), (-105, 73), (-95, 80), (-85, 70),
     (-80, 73), (-76, 62), (-65, 60), (-55, 52), (-65, 45), (-70, 42),
     (-74, 39), (-76, 35), (-80, 32), (-81, 26), (-84, 30), (-90, 29),
     (-97, 26), (-105, 23), (-110, 24), (-114, 30), (-121, 34), (-124, 41),
     (-124, 48), (-132, 56), (-152, 60), (-166, 60)],
    [(-79, 9), (-71, 12), (-62, 10), (-52, 5), (-44, -3), (-35, -8),
     (-40, -16), (-42, -23), (-49, -28), (-53, -34), (-58, -39), (-62, -42),
     (-65, -46), (-68, -51), (-69, -54), (-72, -54), (-74, -47), (-74, -38),
     (-72, -30), (-70, -19), (-76, -14), (-80, -6), (-77, 3)],
    [(-17, 15), (-10, 29), (-6, 35), (3, 37), (10, 37), (11, 34), (20, 32),
     (30, 31), (34, 28), (38, 21), (40, 15), (43, 12), (49, 11), (51, 12),
     (46, 5), (41, -4), (40, -14), (36, -22), (33, -27), (29, -32),
     (20, -35), (18, -33), (15, -27), (13, -18), (12, -10), (9, -2),
     (9, 4), (-8, 5), (-13, 8), (-17, 12)],
    [(-10, 37), (-9, 43), (-2, 44), (-1, 46), (-5, 48), (0, 50), (3, 52),
     (6, 54), (8, 56), (8, 58), (13, 56), (19, 56), (21, 59), (25, 60),
     (24, 66), (31, 70), (45, 68), (55, 68), (48, 64), (40, 62), (33, 59),
     (28, 56), (23, 54), (18, 56), (13, 54), (8, 54), (4, 52), (0, 46),
     (-2, 44), (-9, 38)],
    [(35, 36), (42, 38), (48, 30), (52, 28), (57, 26), (60, 25), (66, 25),
     (72, 21), (75, 16), (77, 8), (80, 13), (84, 19), (88, 22), (91, 23),
     (92, 20), (95, 17), (97, 15), (98, 9), (101, 3), (104, 8), (106, 12),
     (109, 14), (110, 20), (114, 22), (118, 25), (121, 28), (122, 32),
     (120, 35), (122, 38), (125, 40), (128, 41), (131, 43), (136, 45),
     (141, 47), (142, 51), (142, 56), (150, 60), (158, 63), (166, 65),
     (178, 66), (178, 63), (169, 60), (160, 57), (155, 51), (150, 45),
     (143, 44), (140, 40), (138, 36), (135, 34), (130, 33), (127, 35),
     (124, 33), (121, 29), (119, 25), (115, 22), (110, 19), (108, 12),
     (106, 8), (103, 2), (100, 8), (98, 14), (94, 17), (91, 16), (88, 22),
     (85, 20), (80, 15), (77, 8), (73, 19), (68, 23), (62, 25), (57, 26),
     (51, 28), (47, 30), (41, 31), (36, 34)],
    [(95, 5), (100, 0), (105, -5), (110, -7), (115, -8), (121, -9),
     (126, -10), (131, -3), (136, -2), (141, -3), (141, -8), (136, -7),
     (130, -4), (125, -1), (119, -1), (114, -2), (109, -3), (104, -6),
     (99, -3), (95, 2)],
    [(113, -22), (114, -29), (116, -34), (119, -35), (125, -33), (130, -32),
     (133, -32), (136, -35), (139, -37), (141, -39), (146, -39), (148, -38),
     (150, -37), (153, -31), (153, -25), (150, -22), (146, -19), (143, -15),
     (142, -11), (140, -14), (136, -12), (135, -15), (132, -11), (129, -14),
     (125, -14), (122, -17), (117, -20)],
    [(167, -45), (172, -41), (174, -38), (176, -38), (174, -41), (169, -46),
     (167, -46)],
    [(130, 31), (133, 34), (137, 35), (140, 36), (141, 40), (141, 44),
     (143, 44), (141, 39), (139, 35), (135, 34), (131, 32)],
    [(-5, 50), (-3, 53), (-5, 55), (-8, 55), (-6, 52), (-3, 50)],
]


def in_poly(lon, lat, poly):
    inside = False
    j = len(poly) - 1
    for i in range(len(poly)):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if ((yi > lat) != (yj > lat)) and \
           (lon < (xj - xi) * (lat - yi) / (yj - yi) + xi):
            inside = not inside
        j = i
    return inside


def dotted_map(d, x, y, w, h, ink, accent, bg):
    """Original dotted world map from hand-made polygons + numbered pins."""
    d.rectangle([x, y, x + w, y + h], outline=ink, width=1)
    step = 5
    yy = y + 3
    while yy < y + h - 2:
        lat = 82 - (yy - y) / h * 152
        xx = x + 3
        while xx < x + w - 2:
            lon = -180 + (xx - x) / w * 360
            if any(in_poly(lon, lat, p) for p in CONTINENTS):
                d.ellipse([xx - 1, yy - 1, xx + 1, yy + 1], fill=ink)
            xx += step
        yy += step
    for num, lon, lat in PINS:
        px = x + (lon + 180) / 360 * w
        py = y + (82 - lat) / 152 * h
        r = 8
        d.ellipse([px - r, py - r, px + r, py + r], fill=accent)
        t = str(num)
        fnt = fbb(10)
        tw = d.textlength(t, font=fnt)
        d.text((px - tw / 2, py - 6), t, font=fnt, fill=bg)


def wrap(d, text, font, maxw, maxlines=3):
    words = text.split()
    lines, cur = [], ""
    for wd in words:
        trial = (cur + " " + wd).strip()
        if d.textlength(trial, font=font) <= maxw or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    if len(lines) > maxlines:
        lines = lines[:maxlines]
        last = lines[-1]
        while last and d.textlength(last + "...", font=font) > maxw:
            last = last[:-1]
        lines[-1] = last.rstrip() + "..."
    return lines


def icon(d, kind, x, y, s, ink, accent):
    """Tiny original line drawings, one per story kind."""
    cx, cy = x + s / 2, y + s / 2
    if kind == "pipes":
        for r in (s * 0.30, s * 0.19):
            d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=accent, width=3)
        d.line([x + 4, y + s - 6, x + s - 4, y + s - 6], fill=ink, width=3)
    elif kind == "capitol":
        d.arc([cx - s * 0.3, cy - s * 0.42, cx + s * 0.3, cy + s * 0.1], 180, 360, fill=accent, width=3)
        for i in range(-2, 3):
            xx = cx + i * s * 0.13
            d.line([xx, cy + s * 0.02, xx, cy + s * 0.3], fill=ink, width=3)
        d.line([x + 5, y + s - 5, x + s - 5, y + s - 5], fill=ink, width=3)
    elif kind == "rescue":
        d.polygon([(x + 4, y + s - 6), (cx, y + 8), (x + s - 4, y + s - 6)], outline=accent, width=3)
        d.ellipse([cx - 4, cy - 2, cx + 4, cy + 6], outline=ink, width=3)
    elif kind == "cricket":
        d.line([x + 10, y + s - 8, x + s * 0.55, y + 10], fill=accent, width=5)
        d.ellipse([x + s * 0.62, y + s * 0.55, x + s * 0.62 + 13, y + s * 0.55 + 13], fill=ink)
    elif kind == "gold":
        d.polygon([(cx - s * 0.34, cy + s * 0.22), (cx - s * 0.2, cy - s * 0.02),
                   (cx + s * 0.2, cy - s * 0.02), (cx + s * 0.34, cy + s * 0.22)], outline=accent, width=3)
        d.polygon([(cx - s * 0.24, cy - s * 0.1), (cx - s * 0.12, cy - s * 0.3),
                   (cx + s * 0.12, cy - s * 0.3), (cx + s * 0.24, cy - s * 0.1)], outline=ink, width=3)
    elif kind == "tanker":
        d.polygon([(x + 5, cy), (x + s - 8, cy), (x + s - 15, cy + s * 0.25),
                   (x + 11, cy + s * 0.25)], outline=accent, width=3)
        d.rectangle([cx - 8, cy - s * 0.22, cx + 8, cy], outline=ink, width=3)
        d.line([x + 4, y + s - 6, x + s - 4, y + s - 6], fill=ink, width=2)
    elif kind == "summit":
        d.ellipse([cx - s * 0.32, cy - s * 0.32, cx + s * 0.32, cy + s * 0.32], outline=accent, width=3)
        d.arc([cx - s * 0.32, cy - s * 0.32, cx + s * 0.32, cy + s * 0.32], 300, 120, fill=ink, width=2)
    elif kind == "scales":
        d.line([cx, y + 7, cx, y + s - 10], fill=ink, width=3)
        d.line([x + 7, y + 13, x + s - 7, y + 13], fill=accent, width=3)
        d.arc([x + 3, y + 13, x + 19, y + 30], 0, 180, fill=ink, width=2)
        d.arc([x + s - 19, y + 13, x + s - 3, y + 30], 0, 180, fill=ink, width=2)
        d.line([x + 6, y + s - 6, x + s - 6, y + s - 6], fill=ink, width=3)
    elif kind == "database":
        d.ellipse([cx - s * 0.28, y + 8, cx + s * 0.28, y + 20], outline=accent, width=3)
        d.line([cx - s * 0.28, y + 14, cx - s * 0.28, y + s - 12], fill=accent, width=3)
        d.line([cx + s * 0.28, y + 14, cx + s * 0.28, y + s - 12], fill=accent, width=3)
        d.arc([cx - s * 0.28, y + s - 24, cx + s * 0.28, y + s - 6], 0, 180, fill=accent, width=3)
        d.polygon([(cx + 3, y + s * 0.3), (cx - 5, y + s * 0.55), (cx, y + s * 0.55),
                   (cx - 3, y + s * 0.78)], fill=ink)
    elif kind == "fire":
        d.polygon([(cx, y + 6), (cx + s * 0.26, cy + s * 0.1), (cx + s * 0.16, y + s - 7),
                   (cx - s * 0.16, y + s - 7), (cx - s * 0.26, cy + s * 0.1)], outline=accent, width=3)
        d.ellipse([cx - 5, cy + 4, cx + 5, cy + s * 0.32], fill=ink)
    elif kind == "tennis":
        d.ellipse([x + 8, y + 8, x + s - 8, y + s - 8], outline=accent, width=3)
        d.arc([x - 2, y + 8, x + s * 0.5, y + s - 8], 270, 90, fill=ink, width=2)
        d.arc([x + s * 0.5, y + 8, x + s + 2, y + s - 8], 90, 270, fill=ink, width=2)
    elif kind == "chip":
        d.rectangle([cx - s * 0.26, cy - s * 0.26, cx + s * 0.26, cy + s * 0.26], outline=accent, width=3)
        for i in range(-1, 2):
            off = i * s * 0.18
            d.line([cx + off, y + 5, cx + off, cy - s * 0.26], fill=ink, width=2)
            d.line([cx + off, cy + s * 0.26, cx + off, y + s - 5], fill=ink, width=2)
    elif kind == "ship":
        d.polygon([(x + 5, cy + 4), (x + s - 6, cy + 4), (x + s - 13, cy + s * 0.28),
                   (x + 12, cy + s * 0.28)], outline=ink, width=3)
        d.rectangle([x + s * 0.3, cy - s * 0.2, x + s * 0.42, cy + 4], outline=accent, width=3)
        d.ellipse([x + s * 0.28, cy - s * 0.42, x + s * 0.46, cy - s * 0.24], outline=accent, width=2)
    else:  # generic star
        d.polygon([(cx, y + 6), (cx + 5, cy - 2), (x + s - 7, cy - 2), (cx + 7, cy + 6),
                   (cx + 10, y + s - 7), (cx, cy + 12), (cx - 10, y + s - 7),
                   (cx - 7, cy + 6), (x + 7, cy - 2), (cx - 5, cy - 2)], outline=accent, width=2)


def chip(d, x, y, text, color, bg):
    fnt = fbb(11)
    tw = d.textlength(text, font=fnt)
    d.rectangle([x, y, x + tw + 12, y + 16], fill=color)
    d.text((x + 6, y + 2), text, font=fnt, fill=bg)
    return x + tw + 12


def lead(d, x, y, w, h, num, region, src, head, deck, kind, pal):
    ink, accent, bg, cardbg = pal["ink"], pal["accent"], pal["bg"], pal["card"]
    d.rectangle([x, y, x + w, y + h], fill=cardbg, outline=ink, width=2)
    icon(d, kind, x + 12, y + 16, 84, ink, accent)
    tx = x + 112
    nx = chip(d, tx, y + 10, "No %s" % num, accent, bg)
    chip(d, nx + 6, y + 10, region, REGION_COLORS[region], bg)
    sw = d.textlength(src, font=fbb(11))
    d.text((x + w - sw - 10, y + 12), src, font=fbb(11), fill=ink)
    yy = y + 29
    for ln in wrap(d, head, fb(30), w - 128, 2):
        d.text((tx, yy), ln, font=fb(30), fill=ink)
        yy += 32
    for ln in wrap(d, deck, fr(15), w - 128, 2):
        d.text((tx, yy + 2), ln, font=fr(15), fill=ink)
        yy += 19


def mini(d, x, y, w, h, num, region, topic, src, head, deck, kind, pal):
    ink, accent, bg, cardbg = pal["ink"], pal["accent"], pal["bg"], pal["card"]
    d.rectangle([x, y, x + w, y + h], fill=cardbg, outline=ink, width=1)
    d.rectangle([x, y, x + 54, y + h], fill=pal["tint"])
    icon(d, kind, x + 6, y + h / 2 - 21, 42, ink, accent)
    tx = x + 64
    nx = chip(d, tx, y + 7, "No %s" % num, accent, bg)
    chip(d, nx + 5, y + 7, region, REGION_COLORS[region], bg)
    sw = d.textlength(src, font=fbb(10))
    d.text((x + w - sw - 7, y + 9), src, font=fbb(10), fill=ink)
    yy = y + 25
    for ln in wrap(d, head, fb(24), w - 74, 2):
        d.text((tx, yy), ln, font=fb(24), fill=ink)
        yy += 24
    for ln in wrap(d, deck, fr(14), w - 74, 2):
        d.text((tx, yy + 1), ln, font=fr(14), fill=ink)
        yy += 15


def render(variant, out):
    if variant == "B":
        pal = {"bg": (252, 250, 243), "ink": (18, 18, 18), "accent": (122, 31, 31),
               "card": (255, 255, 255), "tint": (244, 230, 222)}
    elif variant == "C":
        pal = {"bg": (243, 233, 200), "ink": (24, 22, 18), "accent": (15, 94, 92),
               "card": (250, 244, 224), "tint": (226, 236, 228)}
    else:
        pal = {"bg": (247, 241, 222), "ink": (18, 16, 12), "accent": (91, 42, 110),
               "card": (252, 248, 236), "tint": (238, 228, 205)}
    ink, accent, bg = pal["ink"], pal["accent"], pal["bg"]
    img = Image.new("RGB", (W, W), bg)
    d = ImageDraw.Draw(img)

    # kicker
    kick = "40 STORIES · 7 REGIONS · EVERY ONE FROM 23 NOVEMBER 2026"
    kw = d.textlength(kick, font=fbb(13))
    d.text(((W - kw) / 2, 14), kick, font=fbb(13), fill=accent)
    d.line([M, 36, W - M, 36], fill=ink, width=2)

    # masthead (PlayfairDisplay-Black), auto-fit
    name = "THE UNIVERSAL LEDGER"
    size = 84
    while d.textlength(name, font=fblack(size)) > CW and size > 40:
        size -= 2
    nw = d.textlength(name, font=fblack(size))
    d.text(((W - nw) / 2, 42), name, font=fblack(size), fill=ink)
    my = 42 + size + 8
    d.line([M, my, W - M, my], fill=ink, width=3)
    date = "Monday 23 November 2026"
    dw = d.textlength(date, font=fb(30))
    d.text(((W - dw) / 2, my + 6), date, font=fb(30), fill=accent)
    dy = my + 42
    d.line([M, dy, W - M, dy], fill=ink, width=1)

    # numbers strip: 2 rows x 4
    ny = dy + 8
    chw = CW // 4
    for i, (val, lab) in enumerate(NUMS):
        cx = M + (i % 4) * chw
        cy = ny + (i // 4) * 27
        d.text((cx + 4, cy), val, font=fbb(23), fill=accent)
        vw = d.textlength(val, font=fbb(23))
        for j, ln in enumerate(wrap(d, lab, fsr(10), chw - vw - 12, 2)):
            d.text((cx + vw + 10, cy + 1 + j * 11), ln, font=fsr(10), fill=ink)
    sy = ny + 58
    d.line([M, sy, W - M, sy], fill=ink, width=2)

    # lead card (left) + dotted map (right)
    ly = sy + 8
    lead(d, M, ly, 596, 112, "1", "SOUTH ASIA", "ObserverVoice 23 Nov",
         "Tata Steel Sells Pipe Arm for Rs 28,000 Crore",
         "APL Apollo buys the pipe unit for Rs 28,000 crore.",
         "pipes", pal)
    mx = M + 608
    dotted_map(d, mx, ly, CW - 608, 112, ink, accent, bg)
    leg = "Dotted map: numbered marks = stories 1-13"
    d.text((mx + 4, ly + 112 - 14), leg, font=fsr(10), fill=ink)

    # mini grid: 4 rows x 3
    gy = ly + 122
    cw3 = (CW - 12) // 3
    for i, c in enumerate(grid):
        cx = M + (i % 3) * (cw3 + 6)
        cy = gy + (i // 3) * 112
        mini(d, cx, cy, cw3, 108, *c, pal)
    ty = gy + 4 * 112 + 2

    # timeline strip
    d.rectangle([M, ty, W - M, ty + 26], outline=ink, width=1)
    tx = M + 8
    d.text((tx, ty + 6), "THE DAY (UTC)", font=fbb(12), fill=accent)
    tx += d.textlength("THE DAY (UTC)", font=fbb(12)) + 12
    for t, ev in TL:
        seg = "%s %s" % (t, ev)
        d.text((tx, ty + 7), seg, font=fsr(11), fill=ink)
        tx += d.textlength(seg, font=fsr(11)) + 12

    # ALSO ON: 4 columns
    ay = ty + 32
    d.text((M, ay), "ALSO ON THE FRONT PAGE", font=fbb(14), fill=accent)
    allb = BRIEFS_L + BRIEFS_R + BRIEFS
    cols = [allb[0:7], allb[7:14], allb[14:21], allb[21:27]]
    colw = CW // 4
    for ci, col in enumerate(cols):
        for ri, b in enumerate(col):
            d.text((M + ci * colw, ay + 18 + ri * 14), b, font=fsr(13), fill=ink)

    # date check strip (red)
    dcy = ay + 18 + 7 * 14 + 6
    red = (168, 30, 30)
    d.rectangle([M, dcy, W - M, dcy + 32], outline=red, width=2)
    for i, ln in enumerate(wrap(d, dc, fsr(11), CW - 16, 2)):
        d.text((M + 8, dcy + 4 + i * 13), ln, font=fsr(11), fill=red)

    # footer
    foot = ("Every story happened, or was first reported, on Monday 23 November 2026. "
            "Contested claims are attributed. · Original drawings.")
    fw = d.textlength(foot, font=fsr(11))
    d.text(((W - fw) / 2, dcy + 38), foot, font=fsr(11), fill=ink)

    img.save(out)
    print("saved", out, variant)


if __name__ == "__main__":
    v = sys.argv[1] if len(sys.argv) > 1 else "A"
    o = sys.argv[2] if len(sys.argv) > 2 else "/tmp/ni23g3-akun18-%s.png" % v
    render(v, o)
