# -*- coding: utf-8 -*-
import io, sys
ZH = u'C:/Games/taiwu-language-files-zh-hans-main/zh-hans/'
BASE = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
fn = sys.argv[1]
lo, hi = int(sys.argv[2]), int(sys.argv[3])
kind = sys.argv[4] if len(sys.argv) > 4 else u'Name'
zl = io.open(ZH + fn, encoding='utf-8').read().split(u'\n')
el = io.open(BASE + u'Language_EN/' + fn, encoding='utf-8').read().split(u'\n')
EN = {}
for i in range(1, len(el) - 1, 2):
    EN[el[i - 1]] = el[i]
off = 0 if kind == u'Name' else 1
for n in range(lo, hi + 1):
    idx = 2 * n + off
    zh = zl[idx] if idx < len(zl) else u'?'
    print(u'%d\t%s\t%s' % (n, EN.get(u'%s_%d' % (kind, n), u'-'), zh))
