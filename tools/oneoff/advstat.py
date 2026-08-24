# -*- coding: utf-8 -*-
import io, re, sys, collections
BASE = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
CYR = re.compile(u'[\u0400-\u04FF]')
fn = sys.argv[1]
el = io.open(BASE + u'Language_EN/' + fn, encoding='utf-8').read().split(u'\n')
rl = io.open(BASE + u'Language_RU/' + fn, encoding='utf-8').read().split(u'\n')
c = collections.Counter()
for i in range(1, min(len(el), len(rl)) - 1, 2):
    if not el[i].strip() or CYR.search(rl[i]):
        continue
    k = el[i - 1]
    # обобщаем: Adv.123 Parameters.4 Desc -> Adv.# Parameters.# Desc
    g = re.sub(u'\\d+', u'#', k)
    c[g] += 1
for g, n in c.most_common(40):
    print(u'%6d  %s' % (n, g))
