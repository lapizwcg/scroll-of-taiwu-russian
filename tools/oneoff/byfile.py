# -*- coding: utf-8 -*-
import io, os, re, sys
BASE = r"C:\Games\The Scroll of Taiwu\The Scroll of Taiwu_Data\StreamingAssets"
RU = os.path.join(BASE, "Language_RU")
CYR = re.compile(u"[\u0400-\u04FF]")
LAT = re.compile(u"[A-Za-z]")
TAG = re.compile(u"<[^<>]*>")
PH = re.compile(u"\\{\\d+\\}")
ESC = re.compile(u"\\\\[nv]")


def strip_markup(v):
    return ESC.sub(u" ", PH.sub(u" ", TAG.sub(u" ", v)))


rows = []
for fn in sorted(os.listdir(RU)):
    if not fn.endswith(".txt"):
        continue
    lines = io.open(os.path.join(RU, fn), encoding="utf-8").read().split(u"\n")
    n = 0
    for i in range(0, len(lines) - 1, 2):
        v = lines[i + 1]
        if CYR.search(v):
            continue
        if not LAT.search(strip_markup(v)):
            continue
        n += 1
    if n:
        rows.append((n, fn))
rows.sort(reverse=True)
sys.stdout.write(u"файлов с остатком: %d, всего строк: %d\n" % (len(rows), sum(r[0] for r in rows)))
for n, fn in rows[:30]:
    sys.stdout.write(u"%7d  %s\n" % (n, fn))
