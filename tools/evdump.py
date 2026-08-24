# -*- coding: utf-8 -*-
# Непереведённые реплики в *_Language_RU.txt из Event/EventLanguages.
# Уникальные значения, по одному в строке.
import io, os, re, sys

DIR = u'C:/Games/The Scroll of Taiwu/Event/EventLanguages/'
CYR = re.compile(u'[\u0400-\u04FF]')
pkg = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else None
p = DIR + u'Taiwu_EventPackage_%s_Language_RU.txt' % pkg
if not os.path.exists(p):
    p = DIR + u'Taiwu_EventPackage_%s_Language_EN.txt' % pkg
seen, res = set(), []
for ln in io.open(p, encoding='utf-8').read().split(u'\n'):
    s = ln.lstrip(u'\t')
    if not s.startswith(u'--') or u' : ' not in ln:
        continue
    val = ln.split(u' : ', 1)[1]
    if not val.strip() or val == u'nan' or CYR.search(val) or val in seen:
        continue
    seen.add(val)
    res.append(val)
sys.stdout.write(u'уникальных непереведённых: %d\n' % len(res))
if out:
    with io.open(out, 'w', encoding='utf-8', newline='') as f:
        f.write(u'\n'.join(res))
else:
    for r in res:
        sys.stdout.write(r + u'\n')
