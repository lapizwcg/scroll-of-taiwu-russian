# -*- coding: utf-8 -*-
"""Доля повторов в остатке по файлам: где выгоден автоперенос."""
import io, os, re

base = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
CYR = re.compile(u'[\u0400-\u04FF]')
rows = []
for fn in sorted(os.listdir(base + 'Language_EN')):
    if not fn.endswith('.txt'):
        continue
    try:
        E = io.open(base + 'Language_EN/' + fn, encoding='utf-8').read().split('\n')
        R = io.open(base + 'Language_RU/' + fn, encoding='utf-8').read().split('\n')
    except IOError:
        continue
    vals = []
    for i in range(0, min(len(E), len(R)) - 1, 2):
        if CYR.search(R[i + 1]):
            continue
        v = E[i + 1].strip()
        if v:
            vals.append(v)
    if len(vals) < 200:
        continue
    u = len(set(vals))
    rows.append((len(vals), u, 100.0 * u / len(vals), fn))

rows.sort(reverse=True)
print('%7s %7s %6s  %s' % ('всего', 'уник.', 'уник%', 'файл'))
for n, u, p, fn in rows[:22]:
    print('%7d %7d %5.0f%%  %s' % (n, u, p, fn))
