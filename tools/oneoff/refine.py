# -*- coding: utf-8 -*-
"""Refine/Refinement (炼化) -> очистка; Reforge (重铸) остаётся перековкой.
Правит только те пары, где в английском есть Refin* и нет Reforg*."""
import io, os, sys, re

ROOTS = [
    u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets',
    u'C:/Games/The Scroll of Taiwu/Mod/TaiwuRussian',
    u'C:/Games/taiwu-ru-backup',
]
EN = ROOTS[0] + u'/Language_EN'

SUB = [
    (u'Перековк', u'Очистк'), (u'перековк', u'очистк'),
    (u'Перековат', u'Очистит'), (u'перековат', u'очистит'),
    (u'Перековыва', u'Очища'), (u'перековыва', u'очища'),
    (u'Перекован', u'Очищен'), (u'перекован', u'очищен'),
]
RE_REFIN = re.compile(r'[Rr]efin')
RE_REFORG = re.compile(r'[Rr]eforg')

apply = '--apply' in sys.argv
total = 0
for fn in sorted(os.listdir(EN)):
    if not fn.endswith('.txt') or fn == 'AdventureCore_language.txt':
        continue  # файл второго сеанса — не трогать
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
        if not RE_REFIN.search(e) or RE_REFORG.search(e):
            continue
        new = r
        for a, b in SUB:
            new = new.replace(a, b)
        if new != r:
            if hits < 3:
                sys.stdout.write(u'%s %s\n  - %s\n  + %s\n' % (fn, el[i - 1], r[:100], new[:100]))
            rl[i] = new
            hits += 1
    if hits:
        total += hits
        sys.stdout.write(u'%-40s %d\n' % (fn, hits))
        if apply:
            data = u'\n'.join(rl)
            for root in ROOTS:
                p = root + u'/Language_RU/' + fn
                if os.path.exists(os.path.dirname(p)):
                    f = io.open(p, 'w', encoding='utf-8', newline='')
                    f.write(data)
                    f.close()
sys.stdout.write(u'ВСЕГО: %d  %s\n' % (total, u'ЗАПИСАНО' if apply else u'проба'))
