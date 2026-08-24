# -*- coding: utf-8 -*-
"""Перенос описаний боевых искусств в описания книг-трактатов.

733 из 879 описаний в SkillBook_language.txt дословно совпадают с описаниями
в CombatSkill_language.txt. Сопоставляем по английской строке.
"""
import io, json, re, collections

base = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
CYR = re.compile(u'[\u0400-\u04FF]')

CE = io.open(base + 'Language_EN/CombatSkill_language.txt', encoding='utf-8').read().split('\n')
CR = io.open(base + 'Language_RU/CombatSkill_language.txt', encoding='utf-8').read().split('\n')
M = {}
for i in range(0, len(CE) - 1, 2):
    if not CE[i].startswith('Desc_'):
        continue
    en, ru = CE[i + 1].strip(), CR[i + 1].strip()
    if en and CYR.search(ru):
        M.setdefault(en, ru)

BE = io.open(base + 'Language_EN/SkillBook_language.txt', encoding='utf-8').read().split('\n')
BR = io.open(base + 'Language_RU/SkillBook_language.txt', encoding='utf-8').read().split('\n')
d = collections.OrderedDict()
miss = 0
for i in range(0, len(BE) - 1, 2):
    if not BE[i].startswith('Desc_'):
        continue
    en = BE[i + 1].strip()
    if not en or CYR.search(BR[i + 1]):
        continue
    if en in M:
        d[BE[i]] = M[en]
    else:
        miss += 1

io.open('b192.json', 'w', encoding='utf-8').write(
    json.dumps({u'SkillBook_language.txt': d}, ensure_ascii=False, indent=1))
print('перенесено:', len(d), '| осталось переводить вручную:', miss)
