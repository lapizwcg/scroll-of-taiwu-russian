# -*- coding: utf-8 -*-
import io, re
BASE = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
CYR = re.compile(u'[\u0400-\u04FF]')
fn = u'AdventureCore_language.txt'
el = io.open(BASE + u'Language_EN/' + fn, encoding='utf-8').read().split(u'\n')
rl = io.open(BASE + u'Language_RU/' + fn, encoding='utf-8').read().split(u'\n')
out = []
for i in range(1, min(len(el), len(rl)) - 1, 2):
    k = el[i - 1]
    if not el[i].strip() or CYR.search(rl[i]):
        continue
    if u' Parameters.' in k:
        continue
    out.append(u'%s\t%s' % (k, el[i]))
io.open(u'C:/Temp/claude/C--Games/15491550-6574-474d-9b03-ddc506e3c80f/scratchpad/adv.txt', 'w', encoding='utf-8').write(u'\n'.join(out))
print(len(out))
