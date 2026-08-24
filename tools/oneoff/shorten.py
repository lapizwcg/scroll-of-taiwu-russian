# -*- coding: utf-8 -*-
"""Укорачивает подписи, которые не влезают в поля.
Правит только пары с точным совпадением английского значения."""
import io, os, sys

ROOTS = [
    u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets',
    u'C:/Games/The Scroll of Taiwu/Mod/TaiwuRussian',
    u'C:/Games/taiwu-ru-backup',
]
EN = ROOTS[0] + u'/Language_EN'

# английское значение -> (что было, чем заменить)
RULES = {
    u'Phy. Penetration': (u'Физическое пробитие', u'Физ. пробитие'),
    u'Phy. Defense': (u'Физическая защита', u'Физ. защита'),
    u'Inner Breath Chaos': (u'Смятение внутреннего дыхания', u'Смятение дыхания'),
    u'Attack Interval': (u'Промежуток между атаками', u'Промежуток атак'),
}

apply = '--apply' in sys.argv
total = 0
for fn in sorted(os.listdir(EN)):
    if not fn.endswith('.txt') or fn == 'AdventureCore_language.txt':
        continue
    el = io.open(EN + u'/' + fn, encoding='utf-8').read().split(u'\n')
    src = ROOTS[0] + u'/Language_RU/' + fn
    if not os.path.exists(src):
        continue
    rl = io.open(src, encoding='utf-8').read().split(u'\n')
    if len(rl) != len(el):
        continue
    hits = 0
    for i in range(1, len(el) - 1, 2):
        r = RULES.get(el[i])
        if r and rl[i] == r[0]:
            rl[i] = r[1]
            hits += 1
    if hits:
        total += hits
        sys.stdout.write(u'%-42s %d\n' % (fn, hits))
        if apply:
            data = u'\n'.join(rl)
            for root in ROOTS:
                p = root + u'/Language_RU/' + fn
                if os.path.exists(os.path.dirname(p)):
                    f = io.open(p, 'w', encoding='utf-8', newline='')
                    f.write(data)
                    f.close()
sys.stdout.write(u'ВСЕГО: %d  %s\n' % (total, u'ЗАПИСАНО' if apply else u'проба'))
