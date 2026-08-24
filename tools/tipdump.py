# -*- coding: utf-8 -*-
import io, json, os, sys

ROOT = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/Language_RU/CommonTip'
KEYS = (u'title', u'content')

def walk(o, out):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in KEYS and isinstance(v, str):
                out.append(u'%s = %s' % (k, v))
            else:
                walk(v, out)
    elif isinstance(o, list):
        for i in o:
            walk(i, out)

for dp, dn, fn in os.walk(ROOT):
    for f in sorted(fn):
        p = os.path.join(dp, f).replace(os.sep, u'/')
        d = json.load(io.open(p, encoding='utf-8'))
        out = []
        walk(d, out)
        sys.stdout.write(u'##### %s\n' % p[len(ROOT) - 9:])
        for line in out:
            sys.stdout.write(line + u'\n')
