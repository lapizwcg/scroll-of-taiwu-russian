# -*- coding: utf-8 -*-
"""Показать непереведённые описания книг в SkillBook_language.txt."""
import io, re, sys

base = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
CYR = re.compile(u'[\u0400-\u04FF]')

E = io.open(base + 'Language_EN/SkillBook_language.txt', encoding='utf-8').read().split('\n')
R = io.open(base + 'Language_RU/SkillBook_language.txt', encoding='utf-8').read().split('\n')

n = 0
out = []
for i in range(0, len(E) - 1, 2):
    if CYR.search(R[i + 1]):
        continue
    if not E[i + 1].strip():
        continue
    n += 1
    out.append(u'%s\t%s\t%s' % (E[i], E[i + 1], R[i + 1]))

io.open('list193.txt', 'w', encoding='utf-8').write(u'\n'.join(out))
print('непереведённых:', n)
