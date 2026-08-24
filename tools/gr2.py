# -*- coding: utf-8 -*-
import io, os, sys, re
BASE = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
CYR = re.compile(u'[\u0400-\u04FF]')
w = sys.argv[1].lower()
lim = int(sys.argv[2]) if len(sys.argv) > 2 else 8
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
        if w in el[i].lower() and CYR.search(rl[i]):
            print(u'%s|%s|%s' % (name[:20], el[i][:110], rl[i][:110]))
            n += 1
            if n >= lim:
                sys.exit()
