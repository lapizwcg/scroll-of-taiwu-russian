# -*- coding: utf-8 -*-
import io, os, sys
BASE = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
words = [w.strip().lower() for w in io.open(sys.argv[1], encoding='utf-8').read().split(u'\n') if w.strip()]
seen = {}
for name in sorted(os.listdir(BASE + u'Language_EN')):
    if not name.endswith(u'.txt'):
        continue
    el = io.open(BASE + u'Language_EN/' + name, encoding='utf-8').read().split(u'\n')
    rl = io.open(BASE + u'Language_RU/' + name, encoding='utf-8').read().split(u'\n')
    for i in range(1, min(len(el), len(rl)) - 1, 2):
        v = el[i].strip().lower()
        if v in seen:
            continue
        if v in words:
            seen[v] = (name, el[i - 1], rl[i])
for w in words:
    if w in seen:
        print(u'%-30s %-22s %s' % (w, seen[w][1], seen[w][2]))
    else:
        print(u'%-30s ---' % w)
