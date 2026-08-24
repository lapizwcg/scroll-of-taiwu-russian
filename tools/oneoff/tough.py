# -*- coding: utf-8 -*-
"""Durability -> прочность, Toughness -> крепость.
Долговечность (13 знаков) не влезала в шапку предмета; прочность освобождается
переносом Toughness на «крепость». Порядок проходов важен: сперва Toughness."""
import io, os, sys

ROOTS = [
    u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets',
    u'C:/Games/The Scroll of Taiwu/Mod/TaiwuRussian',
    u'C:/Games/taiwu-ru-backup',
]
EN = ROOTS[0] + u'/Language_EN'

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
        e, r = el[i], rl[i]
        new = r
        if u'Toughness' in e:
            new = new.replace(u'Прочност', u'Крепост').replace(u'прочност', u'крепост')
        if u'Durability' in e:
            new = new.replace(u'Долговечност', u'Прочност').replace(u'долговечност', u'прочност')
        if new != r:
            if hits < 2:
                sys.stdout.write(u'%s %s\n  - %s\n  + %s\n' % (fn, el[i - 1], r[:90], new[:90]))
            rl[i] = new
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
