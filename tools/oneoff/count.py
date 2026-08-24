# -*- coding: utf-8 -*-
"""Сколько строк затронет каждое переименование."""
import io, os, re, sys, collections

base = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/Language_RU/'
words = [u'словесност', u'красноречи', u'необычн', u'стряпн', u'звездочёт',
         u'сосредоточени', u'костяк', u'понимани', u'проворств', u'ловкост',
         u'срок жизни', u'долголети', u'восприяти']
cnt = collections.Counter()
files = collections.defaultdict(set)
for fn in sorted(os.listdir(base)):
    if not fn.endswith('.txt'):
        continue
    L = io.open(base + fn, encoding='utf-8').read().split('\n')
    for i in range(1, len(L), 2):
        low = L[i].lower()
        for w in words:
            if w in low:
                cnt[w] += 1
                files[w].add(fn)
for w in words:
    print(u'%5d строк, %2d файлов  %s' % (cnt[w], len(files[w]), w))
