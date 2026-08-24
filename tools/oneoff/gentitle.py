# -*- coding: utf-8 -*-
u"""PartTitle_N_k в энциклопедии почти всегда дословно повторяет Name_N.

Общий xfer.py их не берёт: "Use", "Book", "Guard" стоят в чёрном списке или
слишком коротки. Но внутри одного файла совпадение английского значения
с Name_N однозначно, поэтому переносим здесь.

Что не совпало — печатаем, переводим руками.
"""
import io, json, re

BASE = (u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/'
        u'StreamingAssets/')
FN = u'GuidingChapter_language.txt'
CYR = re.compile(u'[\u0400-\u04ff]')

E = io.open(BASE + u'Language_EN/' + FN, encoding='utf-8').read().split(u'\n')
R = io.open(BASE + u'Language_RU/' + FN, encoding='utf-8').read().split(u'\n')

name_en, name_ru = {}, {}
for i in range(0, min(len(E), len(R)) - 1, 2):
    k = E[i].strip()
    if k.startswith(u'Name_'):
        n = k[5:]
        name_en[n] = E[i + 1]
        name_ru[n] = R[i + 1]

out, manual = {}, []
for i in range(0, min(len(E), len(R)) - 1, 2):
    k = E[i].strip()
    if not k.startswith(u'PartTitle_') or CYR.search(R[i + 1]) or not E[i + 1].strip():
        continue
    n = k[10:].rsplit(u'_', 1)[0]
    if name_en.get(n) == E[i + 1] and CYR.search(name_ru.get(n, u'')):
        out[k] = name_ru[n]
    else:
        manual.append((k, E[i + 1], name_en.get(n), name_ru.get(n)))

# Заголовки, которые не сводятся к названию статьи.
EXTRA = {
    u'PartTitle_36_0': u'Окно темницы',
    u'PartTitle_36_1': u'Окно темницы',
    u'PartTitle_294_0': u'О пиршественном зале',
    u'PartTitle_294_1': u'О пиршественном зале',
    u'PartTitle_294_2': u'О пиршественном зале',
    u'PartTitle_27_0': u'Раскопки',
    u'PartTitle_27_1': u'Раскопки',
    u'PartTitle_27_2': u'Раскопки',
}
out.update(EXTRA)

with io.open('b274.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps({FN: out}, ensure_ascii=False, indent=2))

print(u'перенесено: %d' % len(out))
for k, ev, ne, nr in manual:
    if k not in EXTRA:
        print(u'  РУЧНОЙ %-18s %-28s (Name: %s / %s)'
              % (k, ev[:28], (ne or u'-')[:20], (nr or u'-')[:20]))
