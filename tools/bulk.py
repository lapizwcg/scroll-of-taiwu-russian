# -*- coding: utf-8 -*-
"""Раздача перевода по дословным повторам внутри одного файла.
Запуск: python bulk.py <файл.txt> <словарь.json> <выход.json>
Словарь: {"английская строка": "перевод"} — раздаётся всем непереведённым ключам
с точным совпадением значения."""
import io, json, sys, collections, re

BASE = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
CYR = re.compile(u'[\u0400-\u04ff]')

fn, dic_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
el = io.open(BASE + u'Language_EN/' + fn, encoding='utf-8').read().split(u'\n')
rl = io.open(BASE + u'Language_RU/' + fn, encoding='utf-8').read().split(u'\n')
D = json.load(io.open(dic_path, encoding='utf-8'))

out = collections.OrderedDict()
miss = collections.Counter()
for i in range(1, len(el) - 1, 2):
    if not el[i].strip() or CYR.search(rl[i]):
        continue
    v = D.get(el[i])
    if v is not None:
        out[el[i - 1]] = v
    else:
        miss[el[i]] += 1

io.open(out_path, 'w', encoding='utf-8').write(
    json.dumps({fn: out}, ensure_ascii=False, indent=1))
sys.stdout.write(u'раздано %d ключей по %d строкам словаря; без перевода осталось %d\n'
                 % (len(out), len(D), sum(miss.values())))
