# -*- coding: utf-8 -*-
"""Проверка партий 193-200: запретные знаки, иероглифы, латиница внутри слов."""
import io, re

p = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/Language_RU/SkillBook_language.txt'
L = io.open(p, encoding='utf-8').read().split('\n')

BAD = u'\u00ab\u00bb\u201e\u201c\u201d\u2018\u2019\u2212'
CJK = re.compile(u'[\u3000-\u9fff]')
MIX = re.compile(u'[\u0400-\u04FF][A-Za-z]|[A-Za-z][\u0400-\u04FF]')

n = 0
for i in range(0, len(L) - 1, 2):
    k, v = L[i], L[i + 1]
    if not k.startswith('Desc_'):
        continue
    for ch in v:
        if ch in BAD:
            print('ЗАПРЕТНЫЙ ЗНАК', k, repr(ch))
            n += 1
    if CJK.search(v):
        print('ИЕРОГЛИФ', k, CJK.search(v).group())
        n += 1
    m = MIX.search(v)
    if m:
        print('СМЕСЬ АЛФАВИТОВ', k, m.group())
        n += 1
print('замечаний:', n)
