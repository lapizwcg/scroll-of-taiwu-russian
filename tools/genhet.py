# -*- coding: utf-8 -*-
"""Названия вида "Heterodox - <искусство>" собираются из уже переведённого
названия самого искусства: ищем его по всем файлам и ставим впереди
"Обратный путь — ". Что не нашлось — печатается списком.
Запуск: python genhet.py <выход.json>"""
import io, os, re, json, sys, collections

BASE = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
CYR = re.compile(u'[\u0400-\u04ff]')
FN = u'SpecialEffect_language.txt'
PREF = u'Heterodox - '

# словарь EN -> RU по всем переведённым парам
D = {}
bad = set()
for name in sorted(os.listdir(BASE + u'Language_EN')):
    if not name.endswith(u'.txt'):
        continue
    try:
        el = io.open(BASE + u'Language_EN/' + name, encoding='utf-8').read().split(u'\n')
        rl = io.open(BASE + u'Language_RU/' + name, encoding='utf-8').read().split(u'\n')
    except Exception:
        continue
    for i in range(1, min(len(el), len(rl)) - 1, 2):
        en, ru = el[i], rl[i]
        if not en.strip() or not CYR.search(ru):
            continue
        if en in D and D[en] != ru:
            bad.add(en)
        D[en] = ru

el = io.open(BASE + u'Language_EN/' + FN, encoding='utf-8').read().split(u'\n')
rl = io.open(BASE + u'Language_RU/' + FN, encoding='utf-8').read().split(u'\n')
out = collections.OrderedDict()
miss = []
for i in range(1, len(el) - 1, 2):
    en, ru = el[i], rl[i]
    if not en.startswith(PREF) or CYR.search(ru):
        continue
    base = en[len(PREF):]
    t = D.get(base)
    if t and base not in bad:
        out[el[i - 1]] = u'Обратный путь — ' + t
    else:
        miss.append(base)

io.open(sys.argv[1], 'w', encoding='utf-8').write(
    json.dumps({FN: out}, ensure_ascii=False, indent=1))
sys.stdout.write(u'собрано %d, не нашлось %d\n' % (len(out), len(miss)))
for m in sorted(set(miss)):
    sys.stdout.write(u'  НЕТ: %s\n' % m)
