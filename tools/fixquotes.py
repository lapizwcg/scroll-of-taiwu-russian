# -*- coding: utf-8 -*-
u"""Замена знаков, которых нет в шрифте игры.

В английских файлах эти символы не встречаются ни разу — значит, шрифт их
не тянет, и вместо них игра рисует пустой квадрат. Проверено на скриншоте:
кавычки-ёлочки «» выводятся как □.

Заменяем на то, чем пользуется сама игра (ASCII-кавычки и дефис).

  python fixquotes.py                          — показать, что найдено
  python fixquotes.py --apply                  — исправить
  python fixquotes.py AdventureCore_language.txt --apply
                                               — только этот файл

**Указывайте файл, если работаете параллельно со вторым сеансом:**
без имени файла скрипт переписывает все 227 файлов и может затереть
партию соседнего сеанса.
"""
import io, os, sys

REPL = [
    (u'\u00ab', u'"'),   # «
    (u'\u00bb', u'"'),   # »
    (u'\u201e', u'"'),   # „
    (u'\u201c', u'"'),   # “
    (u'\u201d', u'"'),   # ”
    (u'\u2018', u"'"),   # ‘
    (u'\u2019', u"'"),   # ’
    (u'\u2212', u'-'),   # − минус
]

ROOTS = [
    (u'StreamingAssets',
     u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/Language_RU'),
    (u'TaiwuRussian',
     u'C:/Games/The Scroll of Taiwu/Mod/TaiwuRussian/Language_RU'),
    (u'taiwu-ru-backup',
     u'C:/Games/taiwu-ru-backup/Language_RU'),
]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    only = set(args)
    apply = '--apply' in sys.argv
    for label, root in ROOTS:
        if not os.path.isdir(root):
            continue
        files = lines = 0
        for fn in sorted(os.listdir(root)):
            path = os.path.join(root, fn)
            if not os.path.isfile(path) or not fn.endswith('.txt'):
                continue
            if only and fn not in only:
                continue
            src = io.open(path, encoding='utf-8').read().split(u'\n')
            hits = 0
            for i in range(1, len(src), 2):        # только значения
                new = src[i]
                for a, b in REPL:
                    new = new.replace(a, b)
                if new != src[i]:
                    src[i] = new
                    hits += 1
            if hits:
                files += 1
                lines += hits
                print(u'    %-42s %d' % (fn, hits))
                if apply:
                    with io.open(path, 'w', encoding='utf-8', newline='') as f:
                        f.write(u'\n'.join(src))
        print(u'--- %s: файлов %d, строк %d' % (label, files, lines))
    print(u'РЕЖИМ: %s' % (u'ЗАПИСЬ' if apply else u'только показ'))


main()
