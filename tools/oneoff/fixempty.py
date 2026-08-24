# -*- coding: utf-8 -*-
import io, os

FN = u'BuildingBlock_language.txt'
COPIES = [
    u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/Language_RU/' + FN,
    u'C:/Games/The Scroll of Taiwu/Mod/TaiwuRussian/Language_RU/' + FN,
    u'C:/Games/taiwu-ru-backup/Language_RU/' + FN,
]
EN_PATH = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/Language_EN/' + FN
el = io.open(EN_PATH, encoding='utf-8').read().split(u'\n')

for path in COPIES:
    if not os.path.exists(path):
        print(u'НЕТ: ' + path)
        continue
    rl = io.open(path, encoding='utf-8').read().split(u'\n')
    n = 0
    for i in range(1, min(len(el), len(rl)) - 1, 2):
        k = el[i - 1]
        if (k.startswith(u'LeaderName_') or k.startswith(u'MemberName_')) \
                and not el[i].strip() and rl[i].strip():
            rl[i] = el[i]
            n += 1
    io.open(path, 'w', encoding='utf-8', newline='').write(u'\n'.join(rl))
    print(u'%s: очищено %d' % (path.split(u'/')[-3], n))
