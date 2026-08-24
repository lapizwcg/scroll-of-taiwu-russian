# -*- coding: utf-8 -*-
import io, json, re

BASE = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
FN = u'MapBlock_language.txt'
el = io.open(BASE + u'Language_EN/' + FN, encoding='utf-8').read().split(u'\n')
rl = io.open(BASE + u'Language_RU/' + FN, encoding='utf-8').read().split(u'\n')
CYR = re.compile(u'[\u0400-\u04FF]')

# русские названия городов/сект — берём из уже переведённых Name_* этого же файла
RU_NAME = {}
for i in range(1, len(el) - 1, 2):
    if el[i - 1].startswith(u'Name_') and CYR.search(rl[i]):
        RU_NAME[el[i]] = rl[i]

DIRS = [u'северо-запад', u'север', u'северо-восток',
        u'запад', u'центр', u'восток',
        u'юго-запад', u'юг', u'юго-восток']

out = {}
missing = set()
for i in range(1, len(el) - 1, 2):
    k = el[i - 1]
    if not k.startswith(u'BlockNames_') or CYR.search(rl[i]):
        continue
    v = el[i]
    # "Northwest of the Capital" / "Central Capital"
    m = re.match(u'^(Northwest|North|Northeast|West|Central|East|Southwest|South|Southeast) of (?:the )?(.+)$', v)
    if m:
        city = m.group(2)
    elif v.startswith(u'Central '):
        city = v[len(u'Central '):]
    else:
        missing.add(v)
        continue
    idx = int(k.rsplit(u'_', 1)[1])
    ru_city = RU_NAME.get(city)
    if ru_city is None:
        missing.add(city)
        continue
    out[k] = u'%s, %s' % (ru_city, DIRS[idx])

io.open(u'C:/Temp/claude/C--Games/15491550-6574-474d-9b03-ddc506e3c80f/scratchpad/b516.json', 'w', encoding='utf-8').write(
    json.dumps({FN: out}, ensure_ascii=False, indent=1))
print(u'готово: %d' % len(out))
for m in sorted(missing):
    print(u'НЕТ: ' + m)
