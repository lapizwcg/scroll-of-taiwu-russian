# -*- coding: utf-8 -*-
u"""Свести названия семи торговых товариществ к одному варианту.

Разъехались, потому что переводились в разных файлах и в разное время.
Канон выбран по смыслу китайского названия, а не по кальке с английского.
"""
import io, os, sys

REPL = [
    (u'Караван Оксбэк',      u'Караван Воловьей спины'),
    (u'Оружие поборника',    u'Оружейная витязя'),
    (u'Аптекарь воскрешения', u'Аптека Возрождения'),
    (u'Павильон чудес',      u'Павильон диковин'),
]

ROOTS = [
    u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/Language_RU',
    u'C:/Games/The Scroll of Taiwu/Mod/TaiwuRussian/Language_RU',
    u'C:/Games/taiwu-ru-backup/Language_RU',
]


def main():
    apply = '--apply' in sys.argv
    for root in ROOTS:
        if not os.path.isdir(root):
            continue
        total = 0
        for fn in sorted(os.listdir(root)):
            path = os.path.join(root, fn)
            if not os.path.isfile(path) or not fn.endswith('.txt'):
                continue
            lines = io.open(path, encoding='utf-8').read().split(u'\n')
            hits = 0
            for i in range(1, len(lines), 2):
                new = lines[i]
                for a, b in REPL:
                    new = new.replace(a, b)
                if new != lines[i]:
                    lines[i] = new
                    hits += 1
            if hits:
                total += hits
                print(u'%-42s %d' % (fn, hits))
                if apply:
                    with io.open(path, 'w', encoding='utf-8', newline='') as f:
                        f.write(u'\n'.join(lines))
        print(u'%s -> %d строк\n' % (root.split('/')[-2], total))


main()
