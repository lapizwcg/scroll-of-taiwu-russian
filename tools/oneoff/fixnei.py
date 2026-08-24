# -*- coding: utf-8 -*-
"""Свести названия стихий в NeiliType с теми, что давно стоят в ui_language.

ui: Изгнание скверны · Благодатная ци · Тёмная инь · Чистый ян · Небесная мощь.
"""
import io, json, collections

FIX = {
    u'Name_0': u'Металл: Изгнание скверны',
    u'Name_1': u'Дерево: Благодатная ци',
    u'Name_2': u'Вода: Тёмная инь',
    u'Name_3': u'Огонь: Чистый ян',
    u'Name_4': u'Земля: Небесная мощь',
    u'SimpleDesc_0': u'"Ваджра изгоняет скверну и рушит постройки".',
    u'SimpleDesc_1': u'"Дуновение благодатной ци идёт с востока — знак, что отвращает беды".',
    u'SimpleDesc_2': u'"Тёмная инь: могучий Кунь уходит в северные моря".',
    u'SimpleDesc_3': u'"Чистый ян, от которого разум делается твёрдым".',
}
d = collections.OrderedDict(FIX)
# описания начинаются с той же строки — пересобираем начало
base = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/Language_RU/'
L = io.open(base + 'NeiliType_language.txt', encoding='utf-8').read().split('\n')
OLD = {
    u'Desc_0': (u'"Ваджра изгоняет зло и рушит постройки".', FIX[u'SimpleDesc_0']),
    u'Desc_1': (u'"Дуновение благовещей ци идёт с востока — знак, что отвращает беды".',
                FIX[u'SimpleDesc_1']),
    u'Desc_2': (u'"Студёное инь: могучий Кунь уходит в северные моря".', FIX[u'SimpleDesc_2']),
    u'Desc_3': (u'"Палящее ян, от которого разум делается твёрдым".', FIX[u'SimpleDesc_3']),
}
for i in range(0, len(L) - 1, 2):
    k = L[i]
    if k in OLD:
        a, b = OLD[k]
        assert a in L[i + 1], k
        d[k] = L[i + 1].replace(a, b)

io.open('bnei2.json', 'w', encoding='utf-8').write(
    json.dumps({u'NeiliType_language.txt': d}, ensure_ascii=False, indent=1))
print('строк:', len(d))
