# -*- coding: utf-8 -*-
import io, os, sys, re
BASE = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
w = sys.argv[1].lower()
lim = int(sys.argv[2]) if len(sys.argv) > 2 else 15
n = 0
for name in sorted(os.listdir(BASE + u'Language_EN')):
    if not name.endswith(u'.txt'):
        continue
    try:
        el = io.open(BASE + u'Language_EN/' + name, encoding='utf-8').read().split(u'\n')
        rl = io.open(BASE + u'Language_RU/' + name, encoding='utf-8').read().split(u'\n')
    except Exception:
        continue
    for i in range(1, min(len(el), len(rl)) - 1, 2):
        if w in el[i].lower():
            print(u'%s\t%s\t%s\t%s' % (name, el[i-1], el[i][:150], rl[i][:150]))
            n += 1
            if n >= lim:
                sys.exit()
