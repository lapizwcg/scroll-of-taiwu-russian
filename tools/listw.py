# -*- coding: utf-8 -*-
"""Непереведённое в произвольном файле локализации."""
import io, re, sys, collections

base = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
CYR = re.compile(u'[\u0400-\u04FF]')
name = sys.argv[1]

E = io.open(base + 'Language_EN/' + name, encoding='utf-8').read().split('\n')
R = io.open(base + 'Language_RU/' + name, encoding='utf-8').read().split('\n')

pref = collections.Counter()
out = []
for i in range(0, len(E) - 1, 2):
    if CYR.search(R[i + 1]) or not E[i + 1].strip():
        continue
    out.append(u'%s\t%s' % (E[i], E[i + 1]))
    pref[re.sub(u'[0-9]+$', u'#', E[i]).strip()] += 1

io.open('listw.txt', 'w', encoding='utf-8').write(u'\n'.join(out))
print('непереведённых:', len(out))
for k, v in pref.most_common(40):
    print('%6d  %s' % (v, k))
