# -*- coding: utf-8 -*-
"""Выгрузить непереведённые ключи ui_language.txt по списку префиксов."""
import io, re, sys

base = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
CYR = re.compile(u'[\u0400-\u04FF]')
pref = tuple(a.decode('utf-8') if isinstance(a, bytes) else a for a in sys.argv[1:])

E = io.open(base + 'Language_EN/ui_language.txt', encoding='utf-8').read().split('\n')
R = io.open(base + 'Language_RU/ui_language.txt', encoding='utf-8').read().split('\n')
out, n = [], 0
for i in range(0, len(E) - 1, 2):
    k = E[i]
    if k.startswith(pref) and not CYR.search(R[i + 1]) and E[i + 1].strip():
        out.append(u'%s\t%s' % (k, E[i + 1]))
        n += 1
io.open('uiblock.txt', 'w', encoding='utf-8').write(u'\n'.join(out))
print('непереведённых:', n)
