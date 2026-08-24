# -*- coding: utf-8 -*-
import io, os, re, sys, collections
BASE = r"C:\Games\The Scroll of Taiwu\The Scroll of Taiwu_Data\StreamingAssets"
RU = os.path.join(BASE, "Language_RU")
CYR = re.compile(u"[\u0400-\u04FF]")
LAT = re.compile(u"[A-Za-z]")
TAG = re.compile(u"<[^<>]*>")
PH = re.compile(u"\\{\\d+\\}")
ESC = re.compile(u"\\\\[nv]")
SPLIT = re.compile(u"[_]")


def strip_markup(v):
    return ESC.sub(u" ", PH.sub(u" ", TAG.sub(u" ", v)))


fn = sys.argv[1] if len(sys.argv) > 1 else "ui_language.txt"
depth = int(sys.argv[2]) if len(sys.argv) > 2 else 2
lines = io.open(os.path.join(RU, fn), encoding="utf-8").read().split(u"\n")
cnt = collections.Counter()
for i in range(0, len(lines) - 1, 2):
    k, v = lines[i], lines[i + 1]
    if CYR.search(v):
        continue
    if not LAT.search(strip_markup(v)):
        continue
    parts = k.split(u"_")
    cnt[u"_".join(parts[:depth])] += 1
tot = sum(cnt.values())
sys.stdout.write(u"%s: %d untranslated\n" % (fn, tot))
for k, n in cnt.most_common(40):
    sys.stdout.write(u"%6d  %s\n" % (n, k))
