# -*- coding: utf-8 -*-
"""Названия эффектов, совпадающие с названиями боевых искусств.
SpecialEffect зовёт их во множественном числе ("Sword Arts"), CombatSkill —
в единственном ("Sword Art"), поэтому ищем и так, и так.
Запуск: python gensa.py <выход.json>"""
import io, os, re, json, sys, collections, unicodedata

BASE = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
CYR = re.compile(u'[\u0400-\u04ff]')
FN = u'SpecialEffect_language.txt'
PRIO = [u'CombatSkill_language.txt', u'SkillBook_language.txt', FN]


def norm(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii').lower()


D = {}
files = sorted(os.listdir(BASE + u'Language_EN'))
files = [f for f in files if f.endswith(u'.txt') and f not in PRIO] + PRIO
for name in files:
    try:
        el = io.open(BASE + u'Language_EN/' + name, encoding='utf-8').read().split(u'\n')
        rl = io.open(BASE + u'Language_RU/' + name, encoding='utf-8').read().split(u'\n')
    except Exception:
        continue
    for i in range(1, min(len(el), len(rl)) - 1, 2):
        if el[i].strip() and CYR.search(rl[i]):
            D[norm(el[i])] = rl[i]

VARIANTS = [lambda s: s,
            lambda s: s.replace(u' Arts', u' Art'),
            lambda s: s.replace(u' Art', u' Arts')]

el = io.open(BASE + u'Language_EN/' + FN, encoding='utf-8').read().split(u'\n')
rl = io.open(BASE + u'Language_RU/' + FN, encoding='utf-8').read().split(u'\n')
out = collections.OrderedDict()
miss = []
for i in range(1, len(el) - 1, 2):
    k, en, ru = el[i - 1], el[i], rl[i]
    if not k.startswith(u'Name_') or not en.strip() or CYR.search(ru):
        continue
    hit = None
    for v in VARIANTS:
        hit = D.get(norm(v(en)))
        if hit:
            break
    if hit:
        out[k] = hit
    else:
        miss.append(en)

io.open(sys.argv[1], 'w', encoding='utf-8').write(
    json.dumps({FN: out}, ensure_ascii=False, indent=1))
sys.stdout.write(u'собрано %d, не нашлось %d\n' % (len(out), len(miss)))
for m in sorted(set(miss)):
    sys.stdout.write(u'  НЕТ: %s\n' % m)
