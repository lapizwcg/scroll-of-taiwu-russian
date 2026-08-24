# -*- coding: utf-8 -*-
import io, sys
BASE = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
fn = sys.argv[1]
pref = sys.argv[2]
el = io.open(BASE + u'Language_EN/' + fn, encoding='utf-8').read().split(u'\n')
rl = io.open(BASE + u'Language_RU/' + fn, encoding='utf-8').read().split(u'\n')
out = []
for i in range(0, len(el) - 1, 2):
    k = el[i]
    if not k.startswith(pref):
        continue
    out.append(u'%s\t%s\t%s' % (k, el[i + 1], rl[i + 1]))
io.open(u'C:/Temp/claude/C--Games/15491550-6574-474d-9b03-ddc506e3c80f/scratchpad/pairs.txt', 'w', encoding='utf-8').write(u'\n'.join(out))
print(len(out))
