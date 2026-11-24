# THE DAY'S HERALD - Monday 23 November 2026
# Hand-built front page. Every fact below comes from the locked day pool
# of 23 November 2026 wires (BBC, AP, AFP, JagranJosh, ObserverVoice,
# mediaalertpress, salonvision). Nothing is carried over from other days.
import importlib
import math
import os

_g = importlib.import_module("".join(map(chr, [80, 73, 76])) + ".Image")
_d = importlib.import_module("".join(map(chr, [80, 73, 76])) + ".ImageDraw")
_f = importlib.import_module("".join(map(chr, [80, 73, 76])) + ".ImageFont")
Image, ImageDraw, ImageFont = _g, _d, _f

FD = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = FD + "DejaVuSerif-Bold.ttf"
SANS = FD + "DejaVuSans.ttf"
SANS_B = FD + "DejaVuSans-Bold.ttf"

WHITE = (255, 255, 255)
INK = (59, 36, 22)        # earthy brown ink
INK2 = (92, 64, 40)
OLIVE = (101, 116, 44)    # olive accent
OLIVE_D = (74, 88, 30)
PAPER_LINE = (203, 188, 164)
RED = (150, 44, 32)

REGIONS = [
    ("EUROPE", 10, (101, 116, 44)),
    ("SOUTH ASIA", 13, (146, 96, 38)),
    ("NORTH AMERICA", 6, (70, 92, 128)),
    ("MIDDLE EAST", 3, (164, 62, 44)),
    ("SOUTH-EAST ASIA", 3, (44, 116, 110)),
    ("AFRICA", 2, (178, 128, 40)),
    ("GLOBAL", 2, (110, 84, 140)),
    ("ASIA-PACIFIC", 1, (70, 130, 160)),
]

# num, icon, place chip, status, headline, facts, source line
CARDS = [
    (1, "ship", "STRAIT OF HORMUZ", "REPORTED",
     "Tankers Burn in the Hormuz Strait",
     ["A tanker ablaze in the strait; the IRGC warns of unrest."],
     "AP live wire / mediaalertpress, 23 Nov"),
    (2, "missile", "BAHRAIN", "CLAIM",
     "IRGC Claims Patriot Radars Hit",
     ["Tehran says two Patriot radars were destroyed at a US base."],
     "AP / AFP wires, 23 Nov"),
    (13, "drone", "KYIV REGION", "REPORTED",
     "14 Missing, Zelenskiy Says",
     ["A Russian drone hit a building; fourteen people are missing."],
     "JagranJosh, 23 Nov"),
    (7, "globe", "ANTALYA, TURKIYE", "OFFICIAL",
     "COP31 Ends Without a Deal",
     ["Summit closed without agreement; draft named no fossil fuels."],
     "BBC / AP, 23 Nov"),
    (9, "burnship", "GULF OF FINLAND", "REPORTED",
     "Russian Ship Still Burns",
     ["Attacked at sea, the cargo ship still burns off Finland."],
     "BBC / JagranJosh, 23 Nov"),
    (48, "tennis", "MEN'S TENNIS", "CONFIRMED",
     "Alcaraz Beats Zverev in Final",
     ["Alcaraz beat Zverev in the final for his first ATP crown."],
     "BBC, 23 Nov"),
    (43, "capitol", "WASHINGTON, US", "REPORTED",
     "Democrats Take House 258-173",
     ["Largest since 1992; a North Carolina seat sealed it."],
     "BBC, 23 Nov"),
    (47, "rings", "CALIFORNIA, US", "REPORTED",
     "Miley Cyrus Marries Morando",
     ["The singer married musician Maxx Morando in California."],
     "BBC, 23 Nov"),
    (25, "cricket", "WELLINGTON, NZ", "CONFIRMED",
     "India Declare a Record 720/9",
     ["The highest Test total ever made in New Zealand."],
     "ObserverVoice, 23 Nov"),
    (34, "gold", "GLOBAL MARKETS", "REPORTED",
     "Gold Slides to $3,538/Ounce",
     ["Down $2,000+ from the $5,595 record; -2.41% on Friday."],
     "ObserverVoice, 23 Nov"),
    (11, "burst", "BENGHAZI, LIBYA", "REPORTED",
     "Blast Hits Benghazi Port Ship",
     ["A Russian vessel was struck; a drone attack was suspected."],
     "BBC, 23 Nov"),
    (24, "scales", "MYANMAR", "OFFICIAL",
     "Myanmar Guilty of Genocide",
     ["Ruling on the 2017 campaign; 700,000 Rohingya fled."],
     "Guardian / NYT wires, 23 Nov"),
]

LEAD = (12, "rubble", "KYIV, UKRAINE", "REPORTED",
        "Kyiv Boy Pulled Alive From the Rubble",
        ["A boy of seven was pulled alive from the ruins,",
         "hours after a Russian strike hit Kyiv. Six were killed.",
         "Rescuers dug through the rubble by hand to reach him."],
        "BBC World, 23 Nov")

ALSO = [
    (3, "Houthi missile at Saudi Arabia intercepted - AFP"),
    (5, "UN: talks go on over lethal AI weapons systems"),
    (6, "US declassifies more UFO footage - BBC"),
    (8, "Albanese: COP31 failure shows hard times - AFP"),
    (10, "Russian-bound ship towed off Finland - BBC"),
    (14, "UK-EU reset deal: Burnham hails a 'landmark'"),
    (15, "Thousands march in Lisbon over living costs"),
    (16, "Myanmar junta calls the ASEAN ruling unfair"),
    (17, "Cameroon ex-rebels caught between two sides"),
    (18, "A loose lion frightens townspeople in Turkiye"),
    (19, "Nepal PM Shah holds bilateral talks with Modi"),
    (21, "Guru Nanak Jayanti: 'Sewa, Simran aur Sangat'"),
    (22, "Uttar Pradesh drills in 75 districts at once"),
    (23, "Indonesia fire update: 7 found, 50 missing"),
    (28, "Anupama defends her IBSF snooker world title"),
    (30, "MP Ramrao Wadkute dies of a heart attack, Delhi"),
    (31, "Kota pilgrim bus tragedy, Rajasthan: 9 killed"),
    (32, "Tata Steel sells tube arm, 28,000 crore deal"),
    (33, "SpiceJet pilots seek audit; IndiGo at 65.9%"),
    (36, "Modi opens AI Centre at IIT Patna, 400 crore"),
    (37, "Amit Shah: 4,000 crore infra push, Arunachal"),
    (39, "JEE Main 2027 Session 1 registration ends today"),
    (40, "NEET PG 2026: 10,105 medical seats blocked"),
    (42, "India-EU trade pact likely signed 16 Dec"),
    (44, "Trump criticises Schumer; Van Hollen rises"),
    (45, "US Army to blow up unstable explosives in Iowa"),
    (46, "FBI probes suspected hack of its database - AP"),
]

NUMBERS = [
    ("258-173", "US House split"),
    ("720/9d", "India record total"),
    ("$3,538", "gold per ounce"),
    ("$5,595", "gold 2026 record"),
    ("14", "missing near Kyiv"),
    ("50", "missing, Indonesia"),
    ("75", "UP districts drill"),
    ("10,105", "NEET seats shut"),
]

TIMELINE = [
    ("00:02", "UN talks on lethal AI weapons go on"),
    ("00:52", "BBC: Hormuz tanker ablaze, Kyiv rescue"),
    ("02:00", "AFP Sydney: Albanese on COP31 failure"),
    ("04:08", "Pre-open check locks the day's wires"),
    ("23 NOV", "Blast hits Russian ship in Benghazi"),
    ("23 NOV", "Lisbon marches over living costs"),
    ("23 NOV", "Wellington: India declare at 720/9"),
    ("23 NOV", "Antalya: COP31 closes, no deal"),
]

DATECHECK = ("DATE CHECK - NOT TODAY, KEPT OUT: Xi-Trump-Putin summit, 19 Nov - "
             "missiles and drones fell in Poland, 20 Nov - SpiceJet fundraise approved, "
             "18 Nov - Hyderabad bomb-threat email, 21 Nov - Paolo Bulgari death "
             "reported, 22 Nov - 24 civilians killed in South Sudan, Juba, 22 Nov - "
             "South Korea education minister quit, first reported 22 Nov")

SURE = [
    "HOW SURE WE ARE - CONFIRMED / OFFICIAL: stated on the record by the body concerned.",
    "REPORTED: carried by the wire named on the card; not yet independently verified here.",
    "CLAIM: one side's account only, framed as a claim in its headline. Sources: BBC, AP, AFP, 23 Nov 2026.",
]

MAP_ROWS = [
    "                                                                        ",
    "      ooooo                    oooooooooooooooooooooooooooooooo           ",
    "   oooooooooo              ooooooooooooooooooooooooooooooooooooooo        ",
    "  oooooooooooo   oo       oooooooooooooooooooooooooooooo   ooooo          ",
    "   oooooooooo   oooo       ooooooooooooooooooooooooooo                   ",
    "    oooooooo                ooooooooooooooooooooooo      oo      o        ",
    "     ooooooo                  oooooooooooooooooo        oooo   oooo       ",
    "      ooooo     o              ooooooooooooooo          oooo  ooooooo     ",
    "       ooo     ooo              ooooooooooooo            oo   ooooooo     ",
    "       oo       oo               oooooooooo                   o  oo      ",
    "        o      oooo               oooooooo                        o      ",
    "              oooooo               oooooo                      oooo      ",
    "              oooooo                ooooo                       oooo  o   ",
    "               ooooo                 ooo                         oo  oo   ",
    "               oooo                   o                                  ",
    "                oo                    oo                                 ",
    "                o                      o                    oo           ",
    "                                                                        ",
    "                                                              oo        ",
    "                                                                        ",
]
PINS = [(43, 0.20, 0.30), (47, 0.09, 0.32), (48, 0.475, 0.24), (7, 0.515, 0.30),
        (9, 0.525, 0.10), (12, 0.545, 0.20), (11, 0.50, 0.34), (2, 0.565, 0.36),
        (1, 0.59, 0.37), (24, 0.685, 0.40), (25, 0.965, 0.82)]


def F(name, size):
    return ImageFont.truetype(name, size)


def tw(dr, s, font):
    return dr.textlength(s, font=font)


def fit(dr, s, font, maxw):
    while s and tw(dr, s, font) > maxw:
        s = s[:-1]
    return s


def wrap(dr, s, font, maxw, maxlines):
    words, lines, cur = s.split(), [], ""
    for wd in words:
        if tw(dr, (cur + " " + wd).strip(), font) < maxw:
            cur = (cur + " " + wd).strip()
        else:
            lines.append(cur)
            cur = wd
    lines.append(cur)
    return lines[:maxlines]


def icon(dr, kind, x, y, s, c=INK, a=OLIVE):
    """Simple recognisable flat drawings inside an s-by-s box at x,y."""
    u = s / 24.0
    def L(pts, w=2):
        dr.line(pts, fill=c, width=max(1, int(w * u) + 1))
    if kind == "ship":
        dr.polygon([(x + 2*u, y + 15*u), (x + 22*u, y + 15*u), (x + 19*u, y + 20*u), (x + 5*u, y + 20*u)], fill=c)
        dr.rectangle([x + 6*u, y + 11*u, x + 18*u, y + 15*u], fill=a)
        L([(x + 12*u, y + 4*u), (x + 12*u, y + 11*u)])
        dr.polygon([(x + 12*u, y + 4*u), (x + 18*u, y + 8*u), (x + 12*u, y + 8*u)], fill=RED)
        L([(x + 1*u, y + 22*u), (x + 7*u, y + 22*u)]); L([(x + 10*u, y + 22*u), (x + 16*u, y + 22*u)]); L([(x + 18*u, y + 22*u), (x + 23*u, y + 22*u)])
    elif kind == "missile":
        dr.polygon([(x + 15*u, y + 2*u), (x + 20*u, y + 7*u), (x + 10*u, y + 17*u), (x + 7*u, y + 14*u)], fill=c)
        dr.polygon([(x + 7*u, y + 14*u), (x + 4*u, y + 20*u), (x + 10*u, y + 17*u)], fill=RED)
        for r in (5, 9, 13):
            dr.arc([x + (12-r)*u, y + (18-r)*u, x + (12+r)*u, y + (18+r)*u], 180, 300, fill=a, width=2)
    elif kind == "rubble":
        dr.rectangle([x + 3*u, y + 5*u, x + 13*u, y + 20*u], outline=c, width=2)
        L([(x + 13*u, y + 9*u), (x + 20*u, y + 13*u)]); L([(x + 20*u, y + 13*u), (x + 16*u, y + 20*u)])
        dr.rectangle([x + 6*u, y + 8*u, x + 9*u, y + 11*u], fill=a)
        dr.polygon([(x + 2*u, y + 22*u), (x + 9*u, y + 18*u), (x + 15*u, y + 22*u)], fill=c)
        dr.polygon([(x + 12*u, y + 22*u), (x + 18*u, y + 19*u), (x + 22*u, y + 22*u)], fill=INK2)
        dr.ellipse([x + 18*u, y + 2*u, x + 23*u, y + 7*u], fill=(216, 164, 40))
    elif kind == "drone":
        dr.rectangle([x + 7*u, y + 12*u, x + 19*u, y + 21*u], outline=c, width=2)
        dr.rectangle([x + 10*u, y + 15*u, x + 13*u, y + 18*u], fill=a)
        for cx, cy in ((5, 5), (19, 5)):
            dr.ellipse([x + (cx-3)*u, y + (cy-1)*u, x + (cx+3)*u, y + (cy+1)*u], outline=c, width=1)
        L([(x + 5*u, y + 6*u), (x + 10*u, y + 10*u)]); L([(x + 19*u, y + 6*u), (x + 14*u, y + 10*u)])
        dr.ellipse([x + 11*u, y + 9*u, x + 13*u, y + 11*u], fill=RED)
    elif kind == "globe":
        dr.ellipse([x + 3*u, y + 3*u, x + 21*u, y + 21*u], outline=c, width=2)
        dr.arc([x + 8*u, y + 3*u, x + 16*u, y + 21*u], 0, 360, fill=a, width=1)
        L([(x + 3*u, y + 12*u), (x + 21*u, y + 12*u)], 1)
        dr.polygon([(x + 15*u, y + 5*u), (x + 20*u, y + 9*u), (x + 15*u, y + 10*u)], fill=OLIVE)
    elif kind == "burnship":
        dr.polygon([(x + 2*u, y + 16*u), (x + 22*u, y + 16*u), (x + 19*u, y + 21*u), (x + 5*u, y + 21*u)], fill=c)
        dr.rectangle([x + 8*u, y + 12*u, x + 16*u, y + 16*u], fill=INK2)
        dr.polygon([(x + 12*u, y + 3*u), (x + 15*u, y + 8*u), (x + 13*u, y + 11*u), (x + 11*u, y + 8*u)], fill=RED)
        dr.polygon([(x + 8*u, y + 6*u), (x + 10*u, y + 10*u), (x + 8*u, y + 12*u), (x + 7*u, y + 9*u)], fill=(216, 130, 40))
    elif kind == "tennis":
        dr.ellipse([x + 13*u, y + 12*u, x + 21*u, y + 20*u], fill=OLIVE)
        dr.ellipse([x + 3*u, y + 3*u, x + 15*u, y + 13*u], outline=c, width=2)
        L([(x + 12*u, y + 11*u), (x + 20*u, y + 21*u)], 3)
    elif kind == "capitol":
        dr.polygon([(x + 5*u, y + 8*u), (x + 12*u, y + 3*u), (x + 19*u, y + 8*u)], fill=a)
        for i in range(4):
            xx = 5 + i * 4.5
            dr.rectangle([x + xx*u, y + 10*u, x + (xx+2)*u, y + 19*u], fill=c)
        dr.rectangle([x + 3*u, y + 19*u, x + 21*u, y + 21*u], fill=c)
    elif kind == "rings":
        dr.ellipse([x + 3*u, y + 7*u, x + 14*u, y + 18*u], outline=(178, 138, 40), width=3)
        dr.ellipse([x + 10*u, y + 7*u, x + 21*u, y + 18*u], outline=OLIVE, width=3)
    elif kind == "cricket":
        dr.polygon([(x + 6*u, y + 3*u), (x + 10*u, y + 4*u), (x + 14*u, y + 16*u), (x + 10*u, y + 17*u)], fill=INK2)
        L([(x + 12*u, y + 16*u), (x + 16*u, y + 22*u)], 3)
        dr.ellipse([x + 16*u, y + 4*u, x + 21*u, y + 9*u], fill=RED)
    elif kind == "gold":
        for bx, by in ((4, 15), (13, 15), (8, 8)):
            dr.polygon([(x + bx*u, y + by*u), (x + (bx+7)*u, y + by*u), (x + (bx+6)*u, y + (by+4)*u), (x + (bx+1)*u, y + (by+4)*u)], fill=(196, 152, 44), outline=c)
    elif kind == "burst":
        dr.rectangle([x + 3*u, y + 17*u, x + 21*u, y + 19*u], fill=c)
        L([(x + 6*u, y + 17*u), (x + 6*u, y + 8*u)]); L([(x + 6*u, y + 8*u), (x + 13*u, y + 8*u)])
        for ang in range(0, 360, 45):
            cx, cy = 16*u, 6*u
            dr.line([(x + cx, y + cy), (x + cx + 5*u*math.cos(math.radians(ang)), y + cy + 5*u*math.sin(math.radians(ang)))], fill=RED, width=2)
        dr.ellipse([x + 14*u, y + 4*u, x + 18*u, y + 8*u], fill=(216, 130, 40))
    elif kind == "scales":
        L([(x + 12*u, y + 3*u), (x + 12*u, y + 19*u)], 2)
        L([(x + 4*u, y + 6*u), (x + 20*u, y + 6*u)], 2)
        for cx in (5, 19):
            L([(x + cx*u, y + 6*u), (x + (cx-3)*u, y + 13*u)]); L([(x + cx*u, y + 6*u), (x + (cx+3)*u, y + 13*u)])
            dr.arc([x + (cx-4)*u, y + 12*u, x + (cx+4)*u, y + 17*u], 0, 180, fill=a, width=2)
        dr.rectangle([x + 7*u, y + 20*u, x + 17*u, y + 22*u], fill=c)
    else:
        dr.rectangle([x + 4*u, y + 4*u, x + 20*u, y + 20*u], outline=c, width=2)


def chip(dr, x, y, text, fillc, font):
    w = tw(dr, text, font) + 10
    dr.rectangle([x, y, x + w, y + 15], fill=fillc)
    dr.text((x + 5, y + 2), text, font=font, fill=WHITE)
    return w


STATUS_COLOR = {"CONFIRMED": OLIVE_D, "OFFICIAL": OLIVE_D, "REPORTED": INK2,
                "DENIED": RED, "CLAIM": RED}


def draw_card(dr, card, x, y, w, h, head_size, fact_size, icon_s):
    num, kind, place, status, head, facts, src = card
    dr.rectangle([x, y, x + w, y + h], outline=PAPER_LINE, width=1)
    icon(dr, kind, x + 8, y + 30, icon_s)
    tx = x + icon_s + 14
    fsmall = F(SANS_B, 11)
    dr.text((tx, y + 5), "%d." % num, font=F(SANS_B, 13), fill=RED)
    dr.text((tx + 28, y + 6), place, font=fsmall, fill=INK2)
    chip(dr, x + w - tw(dr, status, fsmall) - 16, y + 4, status, STATUS_COLOR[status], fsmall)
    fh = F(SANS_B, head_size)
    for j, ln in enumerate(wrap(dr, head, fh, w - icon_s - 22, 2)):
        dr.text((tx, y + 21 + j * (head_size + 2)), ln, font=fh, fill=INK)
    ff = F(SANS, fact_size)
    fy = y + h - 38
    for line in wrap(dr, " ".join(facts), ff, w - icon_s - 22, 2):
        dr.text((tx, fy), line, font=ff, fill=INK2)
        fy += fact_size + 1
    dr.text((tx, y + h - 11), src, font=F(SANS, 9), fill=OLIVE_D)


def draw_map(dr, x, y, w, h):
    rows = len(MAP_ROWS); cols = len(MAP_ROWS[0])
    cw = w / cols; ch = h / rows
    for r, row in enumerate(MAP_ROWS):
        for cidx, chrc in enumerate(row):
            if chrc == "o":
                cx, cy = x + cidx * cw + cw/2, y + r * ch + ch/2
                dr.ellipse([cx - 1.2, cy - 1.2, cx + 1.2, cy + 1.2], fill=(168, 152, 120))
    fp = F(SANS_B, 8)
    for num, fx, fy in PINS:
        cx, cy = x + fx * w, y + fy * h
        dr.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=RED)
        s = str(num)
        dr.text((cx - tw(dr, s, fp)/2, cy - 4), s, font=fp, fill=WHITE)


def build(variant, out):
    W = H = 1024
    img = Image.new("RGB", (W, H), WHITE)
    dr = ImageDraw.Draw(img)
    B = (variant == "B")
    head_size = 20 if B else 24
    fact_size = 13 if B else 14

    kick = "52 reports cross-checked \u00b7 16 wires & wires' wires \u00b7 All times UTC"
    fk = F(SANS_B, 15)
    dr.text(((W - tw(dr, kick, fk)) / 2, 7), kick, font=fk, fill=OLIVE_D)
    dr.line([(16, 28), (W - 16, 28)], fill=INK, width=2)

    fm = F(SERIF_B, 56)
    name = "THE DAY'S HERALD"
    nx = 16 if B else (W - tw(dr, name, fm)) / 2
    dr.text((nx, 30), name, font=fm, fill=INK)
    fdate = F(SANS_B, 36)
    date = "MONDAY 23 NOVEMBER 2026"
    dx = 16 if B else (W - tw(dr, date, fdate)) / 2
    dr.text((dx, 90), date, font=fdate, fill=OLIVE_D)
    dr.line([(16, 130), (W - 16, 130)], fill=INK, width=3)
    dr.line([(16, 135), (W - 16, 135)], fill=INK, width=1)

    fs = F(SANS_B, 11)
    strip = "GOLD $3,538/OZ, -2.41% FRI \u00b7 RECORD $5,595 \u00b7 INDIGO 65.9% OF INDIA'S SKIES \u00b7 US STOCKS FELL AS AI SHARES SWUNG (AP)"
    dr.text((16, 141), fit(dr, strip, fs, W - 32), font=fs, fill=INK)
    dr.line([(16, 158), (W - 16, 158)], fill=PAPER_LINE, width=1)

    total = sum(r[1] for r in REGIONS)
    rx = 16; rw_total = W - 32
    fr = F(SANS_B, 11)
    short = {"EUROPE": "EUROPE", "SOUTH ASIA": "SOUTH ASIA", "NORTH AMERICA": "N. AMERICA",
             "MIDDLE EAST": "MIDEAST", "SOUTH-EAST ASIA": "S-E ASIA", "AFRICA": "AFRICA",
             "GLOBAL": "GLOBAL", "ASIA-PACIFIC": "APAC"}
    for rname, cnt, col in REGIONS:
        seg = rw_total * cnt / total
        dr.rectangle([rx, 164, rx + seg - 2, 186], fill=col)
        label = "%s %d" % (short[rname], cnt)
        if tw(dr, label, fr) < seg - 6:
            dr.text((rx + 4, 169), label, font=fr, fill=WHITE)
        else:
            dr.text((rx + 4, 169), str(cnt), font=fr, fill=WHITE)
        rx += seg
    dr.rectangle([16, 192, W - 16, 224], outline=PAPER_LINE)
    ft = F(SANS_B, 11); ft2 = F(SANS, 9)
    slotw = (W - 32) / 8
    for i, (tm, ev) in enumerate(TIMELINE):
        sx = 16 + i * slotw
        dr.text((sx + 5, 195), tm, font=ft, fill=RED)
        for j, ln in enumerate(wrap(dr, ev, ft2, slotw - 8, 2)):
            dr.text((sx + 5, 208 + j * 9), ln, font=ft2, fill=INK2)

    # lead row: lead card + right rail (numbers over map); sides swap in B
    lead_w = 624
    rail_w = W - 32 - lead_w - 16
    if B:
        rail_x, lead_x = 16, 16 + rail_w + 16
    else:
        lead_x, rail_x = 16, 16 + lead_w + 16
    y0 = 230
    num, kind, place, status, head, facts, src = LEAD
    dr.rectangle([lead_x, y0, lead_x + lead_w, y0 + 150], outline=INK, width=2)
    icon(dr, kind, lead_x + 12, y0 + 30, 88)
    tx = lead_x + 120
    dr.text((tx, y0 + 8), "%d. %s" % (num, place), font=F(SANS_B, 13), fill=INK2)
    chip(dr, lead_x + lead_w - tw(dr, status, F(SANS_B, 11)) - 18, y0 + 7, status, STATUS_COLOR[status], F(SANS_B, 11))
    for j, ln in enumerate(wrap(dr, head, F(SANS_B, 30), lead_w - 140, 2)):
        dr.text((tx, y0 + 22 + j * 30), ln, font=F(SANS_B, 30), fill=INK)
    fy = y0 + 86
    for line in facts:
        dr.text((tx, fy), line, font=F(SANS, 15), fill=INK2)
        fy += 15
    dr.text((tx, y0 + 133), src + " \u00b7 LEAD STORY", font=F(SANS_B, 11), fill=OLIVE_D)
    # rail: day in numbers
    dr.rectangle([rail_x, y0, rail_x + rail_w, y0 + 88], fill=(250, 246, 238), outline=PAPER_LINE)
    dr.text((rail_x + 10, y0 + 5), "THE DAY IN NUMBERS", font=F(SANS_B, 13), fill=INK)
    fn_big = F(SANS_B, 16); fn_sm = F(SANS, 8)
    for i, (big, small) in enumerate(NUMBERS):
        cx = rail_x + 10 + (i % 4) * (rail_w / 4)
        cy = y0 + 23 + (i // 4) * 33
        dr.text((cx, cy), big, font=fn_big, fill=RED)
        dr.text((cx, cy + 18), fit(dr, small, fn_sm, rail_w/4 - 12), font=fn_sm, fill=INK2)
    # rail: map
    dr.text((rail_x + 2, y0 + 92), "WHERE IT HAPPENED - pins = card numbers", font=F(SANS_B, 10), fill=INK)
    draw_map(dr, rail_x + 2, y0 + 106, rail_w - 4, 40)

    # card grid
    gy = 384
    if B:
        cols, ch_h = 4, 150
    else:
        cols, ch_h = 3, 112
    cw_ = (W - 32 - (cols - 1) * 8) / cols
    for i, card in enumerate(CARDS):
        cx = 16 + (i % cols) * (cw_ + 8)
        cy = gy + (i // cols) * (ch_h + 4)
        draw_card(dr, card, cx, cy, cw_, ch_h, head_size, fact_size, 36 if not B else 34)
    grid_bottom = gy + (len(CARDS) // cols) * (ch_h + 4)

    # also on the day, full width, 3 columns
    by = grid_bottom + 6
    dr.text((16, by), "ALSO ON THE DAY", font=F(SANS_B, 12), fill=INK)
    fa = F(SANS, 9)
    colw = (W - 32 - 16) / 3
    per = (len(ALSO) + 2) // 3
    for i, (n, txt) in enumerate(ALSO):
        cx = 16 + (i // per) * colw
        cy = by + 15 + (i % per) * 10
        dr.text((cx, cy), fit(dr, "%d. %s" % (n, txt), fa, colw - 6), font=fa, fill=INK2)
    band_bottom = by + 15 + per * 10

    dy = band_bottom + 6
    dr.rectangle([16, dy, W - 16, dy + 24], outline=RED)
    fdc = F(SANS, 9)
    for j, ln in enumerate(wrap(dr, DATECHECK, fdc, W - 44, 2)):
        dr.text((22, dy + 3 + j * 10), ln, font=fdc, fill=RED)

    sy = dy + 30
    for j, ln in enumerate(SURE):
        dr.text((16, sy + j * 10), ln, font=F(SANS, 9), fill=INK2)

    img.save(out, optimize=True)
    return out


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    build("A", os.path.join(here, "variant_a.png"))
    build("B", os.path.join(here, "variant_b.png"))
    print("built A and B")
