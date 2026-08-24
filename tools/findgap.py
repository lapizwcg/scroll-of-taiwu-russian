# -*- coding: utf-8 -*-
"""Найти непереведённые ключи, чьё английское значение равно заданной строке."""
import io, os, re, sys

base = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
CYR = re.compile(u'[\u0400-\u04FF]')
targets = set(a.decode('utf-8') if isinstance(a, bytes) else a for a in sys.argv[1:])

for fn in sorted(os.listdir(base + 'Language_EN')):
    if not fn.endswith('.txt'):
        continue
    try:
        E = io.open(base + 'Language_EN/' + fn, encoding='utf-8').read().split('\n')
        R = io.open(base + 'Language_RU/' + fn, encoding='utf-8').read().split('\n')
    except IOError:
        continue
    for i in range(0, min(len(E), len(R)) - 1, 2):
        v = E[i + 1].strip()
        if v in targets and not CYR.search(R[i + 1]):
            print(u'%-42s %-40s %s' % (fn, E[i], v))
