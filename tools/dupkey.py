# -*- coding: utf-8 -*-
# Правка пар с дублирующимся ключом "0" в AdventureCore — по номеру строки,
# потому что apply-ru.ps1 ищет по ключу и на дубликате промахнётся.
import io, os

FN = u'AdventureCore_language.txt'
COPIES = [
    u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/Language_RU/' + FN,
    u'C:/Games/The Scroll of Taiwu/Mod/TaiwuRussian/Language_RU/' + FN,
    u'C:/Games/taiwu-ru-backup/Language_RU/' + FN,
]
EN_PATH = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/Language_EN/' + FN

FIX = {
    u'Blocking the wedding party': u'Преграждает путь свадебному шествию',
    u'Blocking the groom...': u'Преграждает путь жениху…',
}

el = io.open(EN_PATH, encoding='utf-8').read().split(u'\n')
targets = []
for i in range(1, len(el) - 1, 2):
    if el[i - 1] == u'0' and el[i] in FIX:
        targets.append((i, el[i]))
print(u'найдено строк: %d' % len(targets))

for path in COPIES:
    if not os.path.exists(path):
        print(u'НЕТ: ' + path)
        continue
    rl = io.open(path, encoding='utf-8').read().split(u'\n')
    n = 0
    for i, en in targets:
        if rl[i] == en:           # ещё английская — правим
            rl[i] = FIX[en]
            n += 1
    io.open(path, 'w', encoding='utf-8', newline='').write(u'\n'.join(rl))
    print(u'%s: правок %d' % (path.split(u'/')[-3], n))
