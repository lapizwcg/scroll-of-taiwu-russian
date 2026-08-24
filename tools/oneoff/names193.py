# -*- coding: utf-8 -*-
"""Показать русские названия книг Name_0..Name_150 для сверки с описаниями."""
import io

base = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
E = io.open(base + 'Language_EN/SkillBook_language.txt', encoding='utf-8').read().split('\n')
R = io.open(base + 'Language_RU/SkillBook_language.txt', encoding='utf-8').read().split('\n')

out = []
for i in range(0, len(E) - 1, 2):
    k = E[i]
    if not k.startswith('Name_'):
        continue
    try:
        n = int(k[5:])
    except ValueError:
        continue
    if n > 150:
        continue
    out.append(u'%s\t%s\t%s' % (k, E[i + 1], R[i + 1]))

io.open('names193.txt', 'w', encoding='utf-8').write(u'\n'.join(out))
print('строк:', len(out))
