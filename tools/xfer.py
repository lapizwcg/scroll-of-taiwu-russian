# -*- coding: utf-8 -*-
u"""Автоперенос перевода по совпадающей английской строке.

Игра держит один и тот же текст в разных файлах (описания частей зверей,
названия боевых искусств в книгах, повторы внутри файла). Если английское
значение уже где-то переведено — переносим готовый русский.

Строит словарь EN -> RU по всем переведённым парам; если для одной
английской строки нашлось несколько разных переводов, она объявляется
спорной и не переносится (иначе разнобой расползётся дальше).

  python xfer.py                 — показать, что можно перенести
  python xfer.py --apply         — перенести
  python xfer.py Armor_language.txt [...]  — только эти файлы
"""
import io, os, re, sys

CYR = re.compile(u'[\u0400-\u04ff]')

# \u0410\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0435 \u0441\u0442\u0440\u043e\u043a\u0438, \u0443 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0441\u043c\u044b\u0441\u043b \u0437\u0430\u0432\u0438\u0441\u0438\u0442 \u043e\u0442 \u043c\u0435\u0441\u0442\u0430. \u041f\u0435\u0440\u0435\u043d\u043e\u0441\u0438\u0442\u044c \u043d\u0435\u043b\u044c\u0437\u044f:
# "Back" \u0432 \u0431\u043e\u044e \u2014 "\u0421\u0437\u0430\u0434\u0438", \u0432 \u043f\u0440\u0438\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0438 \u2014 \u043a\u043d\u043e\u043f\u043a\u0430 "\u041d\u0430\u0437\u0430\u0434"; "Next" \u2014 \u0438 "\u0414\u0430\u043b\u0435\u0435",
# \u0438 "\u0445\u043e\u0434\u0438\u0442 \u0432\u0442\u043e\u0440\u044b\u043c". \u041e\u0434\u043d\u043e\u0431\u0443\u043a\u0432\u0435\u043d\u043d\u044b\u0435 \u0432\u043e\u043e\u0431\u0449\u0435 \u043d\u0435 \u0442\u0440\u043e\u0433\u0430\u0435\u043c (C, E, Li, Zi, You \u2014
# \u044d\u0442\u043e \u043a\u0438\u0442\u0430\u0439\u0441\u043a\u0438\u0435 \u0441\u043b\u043e\u0433\u0438, \u0430 \u043d\u0435 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0435 \u0441\u043b\u043e\u0432\u0430).
BLOCK = set([
    u'Back', u'Next', u'Use', u'On', u'Off', u'Escape', u'Ending ID',
    u'Aspiration', u'Low', u'Dire', u'Secret', u'Herb', u'Baby',
    u'Technique', u'Expand', u'Source', u'General', u'Default',
])
MINLEN = 3

ROOTS = [
    u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/Language_RU',
    u'C:/Games/The Scroll of Taiwu/Mod/TaiwuRussian/Language_RU',
    u'C:/Games/taiwu-ru-backup/Language_RU',
]
EN = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/Language_EN'


def read(path):
    return io.open(path, encoding='utf-8').read().split(u'\n')


def files(root):
    for fn in sorted(os.listdir(root)):
        if fn.endswith('.txt') and os.path.isfile(os.path.join(root, fn)) \
           and os.path.isfile(os.path.join(EN, fn)):
            yield fn


def build_dict(root):
    u"""EN -> RU по всем уже переведённым парам. Спорные выбрасываем."""
    good, bad = {}, set()
    for fn in files(root):
        e = read(os.path.join(EN, fn))
        r = read(os.path.join(root, fn))
        for i in range(0, min(len(e), len(r)) - 1, 2):
            ev, rv = e[i + 1], r[i + 1]
            if not ev.strip() or ev == rv or not CYR.search(rv):
                continue
            if ev in good and good[ev] != rv:
                bad.add(ev)
            good[ev] = rv
    for ev in bad:
        good.pop(ev, None)
    return good, bad


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    apply = '--apply' in sys.argv
    root0 = ROOTS[0]
    table, bad = build_dict(root0)
    print(u'словарь: %d строк, спорных отброшено: %d\n' % (len(table), len(bad)))

    plan = {}          # файл -> {номер строки: русский}
    for fn in files(root0):
        if args and fn not in args:
            continue
        e = read(os.path.join(EN, fn))
        r = read(os.path.join(root0, fn))
        hits = {}
        for i in range(0, min(len(e), len(r)) - 1, 2):
            if CYR.search(r[i + 1]):
                continue
            ev = e[i + 1]
            if len(ev.strip()) < MINLEN or ev.strip() in BLOCK:
                continue
            ru = table.get(ev)
            if ru:
                hits[i + 1] = ru
        if hits:
            plan[fn] = hits
            print(u'%-42s %d' % (fn, len(hits)))

    total = sum(len(v) for v in plan.values())
    print(u'\nвсего переносится: %d' % total)
    if not apply:
        return
    for root in ROOTS:
        if not os.path.isdir(root):
            continue
        for fn, hits in plan.items():
            path = os.path.join(root, fn)
            if not os.path.isfile(path):
                continue
            lines = read(path)
            for i, ru in hits.items():
                if i < len(lines) and not CYR.search(lines[i]):
                    lines[i] = ru
            with io.open(path, 'w', encoding='utf-8', newline='') as f:
                f.write(u'\n'.join(lines))
    print(u'записано в %d копий' % len(ROOTS))


main()
