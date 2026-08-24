# -*- coding: utf-8 -*-
import io, json, re

BASE = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
FN = u'MapBlock_language.txt'
el = io.open(BASE + u'Language_EN/' + FN, encoding='utf-8').read().split(u'\n')
rl = io.open(BASE + u'Language_RU/' + FN, encoding='utf-8').read().split(u'\n')
CYR = re.compile(u'[\u0400-\u04FF]')

TERRAIN = {
    u'Bamboo Hut': u'Бамбуковая хижина',
    u'Farmland': u'Пашня',
    u'Landscape Garden': u'Парк',
    u'Stone Forests': u'Каменный лес',
    u'Mulberry Garden': u'Тутовый сад',
    u'Herb Garden': u'Аптекарский огород',
    u'Emerald Peak': u'Изумрудная вершина',
    u'Mountains': u'Горы',
    u'Mountain Ranges': u'Горные кряжи',
    u'Canyons': u'Ущелье',
    u'Natural Strongholds': u'Природные твердыни',
    u'Hills': u'Холмы',
    u'Highland Expanse': u'Нагорье',
    u'Fields': u'Поля',
    u'Plains': u'Равнины',
    u'Woodlands': u'Перелески',
    u'Forest': u'Лес',
    u'Riverbanks': u'Берега реки',
    u'River Valley': u'Речная долина',
    u'Thick Woods': u'Чаща',
    u'Cave': u'Пещера',
    u'Swamp': u'Болото',
    u'Havens': u'Приюты',
    u'Stream Valley': u'Долина ручья',
    u'Wilderness': u'Глушь',
    u'Ravaged Plot': u'Разорённый участок',
}

out = {}
missing = set()
for i in range(1, len(el) - 1, 2):
    k = el[i - 1]
    if not k.startswith(u'AdventureEditorName_') or CYR.search(rl[i]):
        continue
    m = re.match(u'^(.+?) (\\d+)$', el[i])
    if not m:
        missing.add(el[i])
        continue
    base, num = m.group(1), m.group(2)
    ru = TERRAIN.get(base)
    if ru is None:
        missing.add(base)
        continue
    out[k] = u'%s %s' % (ru, num)

io.open(u'C:/Temp/claude/C--Games/15491550-6574-474d-9b03-ddc506e3c80f/scratchpad/b521.json', 'w', encoding='utf-8').write(
    json.dumps({FN: out}, ensure_ascii=False, indent=1))
print(u'готово: %d' % len(out))
for m in sorted(missing):
    print(u'НЕТ: ' + m)
