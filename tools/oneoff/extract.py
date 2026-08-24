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


pref = sys.argv[1]
start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
cnt = int(sys.argv[3]) if len(sys.argv) > 3 else 10000
fn = sys.argv[4] if len(sys.argv) > 4 else "ui_language.txt"
lines = io.open(os.path.join(RU, fn), encoding="utf-8").read().split(u"\n")
out = []
for i in range(0, len(lines) - 1, 2):
    k, v = lines[i], lines[i + 1]
    if not k.startswith(pref):
        continue
    if CYR.search(v):
        continue
    if not LAT.search(strip_markup(v)):
        continue
    out.append((k, v))
sys.stdout.write(u"ALL %d\n" % len(out))
for k, v in out[start:start + cnt]:
    sys.stdout.write(k + u"\t" + v + u"\n")
