# -*- coding: utf-8 -*-
import io, sys

BASE = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
f = u'ui_language.txt'
en = io.open(BASE + u'Language_EN/' + f, encoding='utf-8').read().split(u'\n')
ru = io.open(BASE + u'Language_RU/' + f, encoding='utf-8').read().split(u'\n')
pats = [p.lower() for p in sys.argv[1:]]
for i in range(0, min(len(en), len(ru)) - 1, 2):
    k = en[i]
    if any(p in k.lower() for p in pats):
        sys.stdout.write(u'%s\n  EN %s\n  RU %s\n' % (k, en[i + 1][:200], ru[i + 1][:200]))
