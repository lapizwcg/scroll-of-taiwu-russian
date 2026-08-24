# -*- coding: utf-8 -*-
import io, os, sys
BASE = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
w = sys.argv[1]
lim = int(sys.argv[2]) if len(sys.argv) > 2 else 30
n = 0
for name in sorted(os.listdir(BASE + u'Language_RU')):
    if not name.endswith(u'.txt'):
        continue
    try:
        el = io.open(BASE + u'Language_EN/' + name, encoding='utf-8').read().split(u'\n')
        rl = io.open(BASE + u'Language_RU/' + name, encoding='utf-8').read().split(u'\n')
    except Exception:
        continue
    for i in range(1, min(len(el), len(rl)) - 1, 2):
        if w in rl[i]:
            print(u'%s\t%s\t%s\t%s' % (name, el[i - 1], el[i][:90], rl[i][:110]))
            n += 1
            if n >= lim:
                sys.exit()
