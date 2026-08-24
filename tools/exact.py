# -*- coding: utf-8 -*-
# Ищет пары, у которых английское значение точно равно заданному.
# Показывает файл, ключ и русское значение (или пометку, что не переведено).
import io, os, sys, re

BASE = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
CYR = re.compile(u'[\u0400-\u04FF]')
targets = [a for a in sys.argv[1:] if not a.startswith('--')]
only_bad = '--bad' in sys.argv

for f in sorted(os.listdir(BASE + u'Language_EN')):
    if not f.endswith(u'.txt'):
        continue
    pe, pr = BASE + u'Language_EN/' + f, BASE + u'Language_RU/' + f
    if not os.path.exists(pr):
        continue
    en = io.open(pe, encoding='utf-8').read().split(u'\n')
    ru = io.open(pr, encoding='utf-8').read().split(u'\n')
    for i in range(1, min(len(en), len(ru)) - 1, 2):
        if en[i] in targets:
            done = bool(CYR.search(ru[i]))
            if only_bad and done:
                continue
            sys.stdout.write(u'%-38s %-46s %s\n' % (f, en[i - 1], ru[i][:60]))
