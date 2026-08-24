# -*- coding: utf-8 -*-
import io, re, sys
BASE = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
CYR = re.compile(u'[\u0400-\u04FF]')
fn = sys.argv[1]
pref = sys.argv[2] if len(sys.argv) > 2 else u''
out_path = sys.argv[3] if len(sys.argv) > 3 else u'C:/Temp/claude/C--Games/15491550-6574-474d-9b03-ddc506e3c80f/scratchpad/dump.txt'
el = io.open(BASE + u'Language_EN/' + fn, encoding='utf-8').read().split(u'\n')
rl = io.open(BASE + u'Language_RU/' + fn, encoding='utf-8').read().split(u'\n')
out = []
for i in range(1, min(len(el), len(rl)) - 1, 2):
    if not el[i].strip() or CYR.search(rl[i]):
        continue
    if pref and not el[i - 1].startswith(pref):
        continue
    out.append(u'%s\t%s' % (el[i - 1], el[i]))
io.open(out_path, 'w', encoding='utf-8').write(u'\n'.join(out))
print(len(out))
