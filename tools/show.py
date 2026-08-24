# -*- coding: utf-8 -*-
"""Показать ключ и значение для строк, содержащих слово."""
import io, os, sys

base = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/Language_RU/'
w = sys.argv[1].decode('utf-8') if isinstance(sys.argv[1], bytes) else sys.argv[1]
w = w.lower()
lim = int(sys.argv[2]) if len(sys.argv) > 2 else 40
n = 0
for fn in sorted(os.listdir(base)):
    if not fn.endswith('.txt'):
        continue
    L = io.open(base + fn, encoding='utf-8').read().split('\n')
    for i in range(1, len(L), 2):
        if w in L[i].lower():
            n += 1
            if n > lim:
                sys.exit()
            v = L[i]
            if len(v) > 110:
                v = v[:110] + u'...'
            print(u'%-32s %-38s %s' % (fn[:-13], L[i - 1][:38], v))
