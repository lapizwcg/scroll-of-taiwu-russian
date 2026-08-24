# -*- coding: utf-8 -*-
import io, os

COPIES = [
    u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/Language_RU/',
    u'C:/Games/The Scroll of Taiwu/Mod/TaiwuRussian/Language_RU/',
    u'C:/Games/taiwu-ru-backup/Language_RU/',
]
EN_DIR = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/Language_EN/'

RULES = [
    (u'Дальность атаки', u'Дистанция'),
    (u'дальность атаки', u'дистанция'),
    (u'Дальность искусств', u'Дистанция искусств'),
    (u'дальность искусств', u'дистанция искусств'),
]

for base in COPIES:
    if not os.path.isdir(base):
        print(u'НЕТ: ' + base)
        continue
    total = 0
    for name in sorted(os.listdir(base)):
        if not name.endswith(u'.txt') or not os.path.exists(EN_DIR + name):
            continue
        el = io.open(EN_DIR + name, encoding='utf-8').read().split(u'\n')
        rl = io.open(base + name, encoding='utf-8').read().split(u'\n')
        n = 0
        for i in range(1, min(len(el), len(rl)) - 1, 2):
            # правим только там, где в английском действительно Attack Range / attack range
            if u'ttack range' not in el[i] and u'ttack Range' not in el[i]:
                continue
            new = rl[i]
            for a, b in RULES:
                new = new.replace(a, b)
            if new != rl[i]:
                rl[i] = new
                n += 1
        if n:
            io.open(base + name, 'w', encoding='utf-8', newline='').write(u'\n'.join(rl))
            total += n
            print(u'  %-45s %d' % (name, n))
    print(u'%s: правок %d' % (base.split(u'/')[-3], total))
