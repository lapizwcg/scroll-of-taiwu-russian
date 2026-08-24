# -*- coding: utf-8 -*-
"""Проверка словаря для bulk.py: какие английские строки не найдены в файле.
Запуск: python dcheck.py <файл.txt> <словарь.json>"""
import io, json, sys, re
BASE = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
CYR = re.compile(u'[\u0400-\u04ff]')
fn, dic = sys.argv[1], sys.argv[2]
el = io.open(BASE + u'Language_EN/' + fn, encoding='utf-8').read().split(u'\n')
rl = io.open(BASE + u'Language_RU/' + fn, encoding='utf-8').read().split(u'\n')
todo = set()
for i in range(1, len(el) - 1, 2):
    if el[i].strip() and not CYR.search(rl[i]):
        todo.add(el[i])
D = json.load(io.open(dic, encoding='utf-8'))
miss = [k for k in D if k not in todo]
sys.stdout.write(u'в словаре %d, из них не найдено среди непереведённых: %d\n' % (len(D), len(miss)))
for k in miss:
    sys.stdout.write(u'  НЕТ: %s\n' % k)
