# -*- coding: utf-8 -*-
u"""Уникальные короткие строки, которые перенесёт xfer.py — для вычитки."""
import io, os, re, collections, sys

CYR = re.compile(u'[\u0400-\u04ff]')
ROOT = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/Language_RU'
EN = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/Language_EN'
MAXLEN = int(sys.argv[1]) if len(sys.argv) > 1 else 16
MINCNT = int(sys.argv[2]) if len(sys.argv) > 2 else 2


def read(p):
    return io.open(p, encoding='utf-8').read().split(u'\n')


def files():
    for fn in sorted(os.listdir(ROOT)):
        if fn.endswith('.txt') and os.path.isfile(os.path.join(ROOT, fn)) \
           and os.path.isfile(os.path.join(EN, fn)):
            yield fn


good, bad = {}, set()
for fn in files():
    e = read(os.path.join(EN, fn))
    r = read(os.path.join(ROOT, fn))
    for i in range(0, min(len(e), len(r)) - 1, 2):
        ev, rv = e[i + 1], r[i + 1]
        if not ev.strip() or ev == rv or not CYR.search(rv):
            continue
        if ev in good and good[ev] != rv:
            bad.add(ev)
        good[ev] = rv
for ev in bad:
    good.pop(ev, None)

cnt = collections.Counter()
for fn in files():
    e = read(os.path.join(EN, fn))
    r = read(os.path.join(ROOT, fn))
    for i in range(0, min(len(e), len(r)) - 1, 2):
        if CYR.search(r[i + 1]):
            continue
        if e[i + 1] in good and len(e[i + 1]) <= MAXLEN:
            cnt[e[i + 1]] += 1

sel = [(n, ev) for ev, n in cnt.items() if n >= MINCNT]
sel.sort(key=lambda t: -t[0])
print(u'уникальных: %d, строк: %d' % (len(sel), sum(n for n, _ in sel)))
for n, ev in sel:
    print(u'%3d %-22s %s' % (n, ev, good[ev]))
