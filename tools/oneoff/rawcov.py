# -*- coding: utf-8 -*-
import io, os, re, sys
BASE = r"C:\Games\The Scroll of Taiwu\The Scroll of Taiwu_Data\StreamingAssets"
RU = os.path.join(BASE, "Language_RU")
CYR = re.compile(u"[\u0400-\u04FF]"); LAT = re.compile(u"[A-Za-z]")
TAG = re.compile(u"<[^<>]*>"); PH = re.compile(u"\{\d+\}"); ESC = re.compile(u"\\[nv]")
def sm(v): return ESC.sub(u" ", PH.sub(u" ", TAG.sub(u" ", v)))
rows=[]
for fn in sorted(os.listdir(RU)):
    if not fn.endswith(".txt"): continue
    lines = io.open(os.path.join(RU, fn), encoding="utf-8").read().split(u"\n")
    ru=en=0
    for i in range(0, len(lines)-1, 2):
        v = lines[i+1]
        if CYR.search(v): ru+=1
        elif LAT.search(sm(v)): en+=1
    rows.append((ru+en, ru, en, fn))
rows.sort(reverse=True)
for t,r,e,fn in rows:
    if t: sys.stdout.write(u"%6d %6d %6d  %s\n" % (t,r,e,fn))
