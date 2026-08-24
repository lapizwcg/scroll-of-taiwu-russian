# -*- coding: utf-8 -*-
# Непереведённые пары ui_language.txt по подстроке ключа, полностью.
import io, re, sys

BASE = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
CYR = re.compile(u'[\u0400-\u04FF]')
f = u'ui_language.txt'
en = io.open(BASE + u'Language_EN/' + f, encoding='utf-8').read().split(u'\n')
ru = io.open(BASE + u'Language_RU/' + f, encoding='utf-8').read().split(u'\n')
pats = [p.lower() for p in sys.argv[1:]]
n = 0
for i in range(0, min(len(en), len(ru)) - 1, 2):
    k = en[i]
    if not any(p in k.lower() for p in pats):
        continue
    if not en[i + 1].strip() or CYR.search(ru[i + 1]):
        continue
    n += 1
    sys.stdout.write(u'%s\t%s\n' % (k, en[i + 1]))
sys.stdout.write(u'--- всего %d\n' % n)
