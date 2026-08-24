# -*- coding: utf-8 -*-
import io, os, re, sys, collections
BASE = r"C:\Games\The Scroll of Taiwu\The Scroll of Taiwu_Data\StreamingAssets\Language_RU"
CYR = re.compile(u"[\u0400-\u04FF]"); LAT = re.compile(u"[A-Za-z]")
TAG = re.compile(u"<[^<>]*>"); PH = re.compile(u"\{\d+\}"); ESC = re.compile(u"\\[nv]")
def sm(v): return ESC.sub(u" ", PH.sub(u" ", TAG.sub(u" ", v)))
fn = sys.argv[1]
lines = io.open(os.path.join(BASE, fn), encoding="utf-8").read().split(u"\n")
c = collections.Counter(); d = collections.Counter()
for i in range(0, len(lines)-1, 2):
    k = re.sub(u"\d+", u"N", lines[i]); v = lines[i+1]
    if CYR.search(v): d[k] += 1
    elif LAT.search(sm(v)): c[k] += 1
for k, n in c.most_common(15):
    sys.stdout.write(u"%6d остаток / %6d готово  %s\n" % (n, d[k], k))
