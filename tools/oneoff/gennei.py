# -*- coding: utf-8 -*-
"""NeiliType_language.txt: стихии истинной ци (окно Судьбы).

Условия и эффекты разбираем из английского по образцу и собираем заново,
чтобы не потерять цветовые теги. Названия и стихи — вручную.
"""
import io, json, re, collections

base = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
CYR = re.compile(u'[\u0400-\u04FF]')

# стихия -> (код цвета, родительный, прилагательное во мн. род., прил. во мн. им.)
EL = {
    'Metal': (u'fiveelementtype_jingang', u'Металла', u'металлических', u'Металлические'),
    'Wood':  (u'fiveelementtype_zixia',   u'Дерева',  u'деревянных',   u'Деревянные'),
    'Water': (u'fiveelementtype_xuanyin', u'Воды',    u'водных',       u'Водные'),
    'Fire':  (u'fiveelementtype_chunyang', u'Огня',   u'огненных',     u'Огненные'),
    'Earth': (u'fiveelementtype_guiyuan', u'Земли',   u'земляных',     u'Земляные'),
}
TAG = re.compile(r'</?color[^>]*>')


def c(el, word):
    return u'<color=#%s>%s</color>' % (EL[el][0], word)


# ---------- условия ----------
COND = [
    (re.compile(r'^(\w+) Qi is the highest\.\\nAll the other Qi is below 40% of \1 Qi\.$'),
     lambda m: u'Ци %s наибольшая.\\nВся прочая ци ниже 40%% от ци %s.'
               % (c(m.group(1), EL[m.group(1)][1]), c(m.group(1), EL[m.group(1)][1]))),
    (re.compile(r'^The lowest Qi exceeds 80% of the highest Qi\.$'),
     lambda m: u'Наименьшая ци превышает 80% от наибольшей.'),
    (re.compile(r'^(\w+) Qi is the highest, followed by (\w+) Qi\.'
                r'\\n\2 Qi is not below 80% of \1 Qi\.$'),
     lambda m: u'Ци %s наибольшая, за ней идёт ци %s.\\nЦи %s не ниже 80%% от ци %s.'
               % (c(m.group(1), EL[m.group(1)][1]), c(m.group(2), EL[m.group(2)][1]),
                  c(m.group(2), EL[m.group(2)][1]), c(m.group(1), EL[m.group(1)][1]))),
    (re.compile(r'^(\w+) Qi is the highest, followed by (\w+) Qi\.'
                r'\\n\2 Qi is between 40% and 80% of \1 Qi\.$'),
     lambda m: u'Ци %s наибольшая, за ней идёт ци %s.'
               u'\\nЦи %s составляет от 40%% до 80%% от ци %s.'
               % (c(m.group(1), EL[m.group(1)][1]), c(m.group(2), EL[m.group(2)][1]),
                  c(m.group(2), EL[m.group(2)][1]), c(m.group(1), EL[m.group(1)][1]))),
]

# ---------- эффекты с цветом ----------
EFF = [
    (re.compile(r"^(\w+) and (\w+) [Mm]artial [Aa]rts' Power Cap increases by (\d+)%\.$"),
     lambda m: u'Предел мощи %s и %s боевых искусств <color=#brightblue>выше на %s%%</color>.'
               % (c(m.group(1), EL[m.group(1)][2]), c(m.group(2), EL[m.group(2)][2]), m.group(3))),
    (re.compile(r"^(\w+) and (\w+) [Mm]artial [Aa]rts' Power Cap decreases by (\d+)%\.$"),
     lambda m: u'Предел мощи %s и %s боевых искусств <color=#brightred>ниже на %s%%</color>.'
               % (c(m.group(1), EL[m.group(1)][2]), c(m.group(2), EL[m.group(2)][2]), m.group(3))),
    (re.compile(r"^(\w+) [Mm]artial [Aa]rts' Power Cap increases by (\d+)%\.$"),
     lambda m: u'Предел мощи %s боевых искусств <color=#brightblue>выше на %s%%</color>.'
               % (c(m.group(1), EL[m.group(1)][2]), m.group(2))),
    (re.compile(r"^(\w+) [Mm]artial [Aa]rts' Power Cap decreases by (\d+)%\.$"),
     lambda m: u'Предел мощи %s боевых искусств <color=#brightred>ниже на %s%%</color>.'
               % (c(m.group(1), EL[m.group(1)][2]), m.group(2))),
    (re.compile(r"^Each time using (\w+) [Mm]artial [Aa]rts causes Recoil Damage and Inner Breath Chaos\.$"),
     lambda m: u'Всякое применение %s боевых искусств <color=#brightred>наносит отдачу '
               u'и вызывает смятение внутреннего дыхания</color>.'
               % c(m.group(1), EL[m.group(1)][2])),
]

# ---------- описания в квадратных скобках ----------
DSC = [
    (re.compile(r'^Increases the Power Cap of \[(\w+)-type\] and \[(\w+)-type\] Martial Arts by (\d+)%\.$'),
     lambda m: u'Предел мощи боевых искусств [стихии %s] и [стихии %s] выше на %s%%.'
               % (EL[m.group(1)][1], EL[m.group(2)][1], m.group(3))),
    (re.compile(r'^Reduces the (?:Power Cap|maximum Power) of \[(\w+)-type\] and \[(\w+)-type\] Martial Arts by (\d+)%\.$'),
     lambda m: u'Предел мощи боевых искусств [стихии %s] и [стихии %s] ниже на %s%%.'
               % (EL[m.group(1)][1], EL[m.group(2)][1], m.group(3))),
    (re.compile(r'^Increases the Power Cap of \[(\w+)-type\] Martial Arts by (\d+)%\.$'),
     lambda m: u'Предел мощи боевых искусств [стихии %s] выше на %s%%.'
               % (EL[m.group(1)][1], m.group(2))),
    (re.compile(r'^Reduces the Power Cap of \[(\w+)-type\] Martial Arts by (\d+)%\.$'),
     lambda m: u'Предел мощи боевых искусств [стихии %s] ниже на <color=#brightred>%s%%</color>.'
               % (EL[m.group(1)][1], m.group(2))),
    (re.compile(r"^\[(\w+)-type\] Martial Arts deal Recoil damage to the user and cause "
                r"Inner Breath Chaos each time they're used\.$"),
     lambda m: u'Боевые искусства [стихии %s] при каждом применении наносят отдачу владельцу '
               u'и вызывают смятение внутреннего дыхания.' % EL[m.group(1)][1]),
]


def apply(rules, s):
    for rx, fn in rules:
        m = rx.match(s)
        if m:
            return fn(m)
    return None


# ---------- названия и стихи ----------
NAMES = [
 u'Металл: Изгнание зол', u'Дерево: Благовещая ци', u'Вода: Студёное инь',
 u'Огонь: Палящее ян', u'Земля: Небесная мощь', u'Хуньюань: Божественное единение',
 u'Металл: Осевший поток', u'Металл: Закалённое лезвие', u'Металл: Убывающая крепость',
 u'Металл: Раскол надвое', u'Металл: Горные жилы', u'Металл: Зарытые сокровища',
 u'Дерево: Горящий гнев', u'Дерево: Меняющиеся облики', u'Дерево: Расщеплённый ствол',
 u'Дерево: Осыпающееся разрушение', u'Дерево: Зелёная природа', u'Дерево: Пышный рост',
 u'Вода: Истинная текучесть', u'Вода: Ревущий разлив', u'Вода: Уходящая влага',
 u'Вода: Погашенное пламя', u'Вода: Металлические наносы', u'Вода: Металлические токи',
 u'Огонь: Вечное пламя', u'Огонь: Неугасимая ярость', u'Огонь: Погасшее пламя',
 u'Огонь: Расплавленный металл', u'Огонь: Раздутая ярость', u'Огонь: Лесной пожар',
 u'Земля: Непробиваемая твердь', u'Земля: Насыщенная плотность', u'Земля: Полное размывание',
 u'Земля: Запертые потоки', u'Земля: Подсека и пал', u'Земля: Выжженная крепость',
]
SIMPLE = [
 u'"Ваджра изгоняет зло и рушит постройки".',
 u'"Дуновение благовещей ци идёт с востока — знак, что отвращает беды".',
 u'"Студёное инь: могучий Кунь уходит в северные моря".',
 u'"Палящее ян, от которого разум делается твёрдым".',
 u'"Небесная мощь: земля несёт на себе всё сущее".',
 u'"Хуньюань объемлет всё: пять стихий сходятся воедино".',
 u'"Металл вновь обретает крепость, когда лишняя вода уходит".',
 u'"Закалка в воде даёт лезвию его остроту".',
 u'"Вода точит металл, и крепость его убывает".',
 u'"Металл рассекает дерево, и ствол распадается надвое".',
 u'"Горные жилы родят металл: земля питает клинок".',
 u'"Зарытые сокровища ждут в земле того, кто их отыщет".',
 u'"Дерево кормит огонь, и гнев его разгорается".',
 u'"Огонь пожирает дерево, и облик его вечно меняется".',
 u'"Металл рубит дерево, и ствол идёт в щепу".',
 u'"Дерево, лишённое влаги, осыпается прахом".',
 u'"Вода питает дерево, и зелёная природа его крепнет".',
 u'"Вода поит корни, и рост становится пышным".',
 u'"Истинная текучесть: вода не спорит и оттого сильна".',
 u'"Ревущий разлив: вода вбирает дерево и катится валом".',
 u'"Дерево пьёт воду, и влага уходит".',
 u'"Вода гасит огонь, и пламя исчезает".',
 u'"Металл родит воду, и в потоке оседают металлические наносы".',
 u'"Металлические токи: вода несёт в себе крепость металла".',
 u'"Вечное пламя: огонь не гаснет, покуда есть чем гореть".',
 u'"Неугасимая ярость: огонь берёт своё у земли".',
 u'"Вода встречает огонь, и пламя гаснет".',
 u'"Огонь плавит металл, и тот течёт расплавом".',
 u'"Дерево раздувает огонь, и ярость его растёт".',
 u'"Лесной пожар: огонь идёт по дереву и не знает удержу".',
 u'"Непробиваемая твердь: земля не поддаётся".',
 u'"Огонь родит золу, и земля становится плотнее".',
 u'"Вода размывает землю без остатка".',
 u'"Земля запирает воду, и потоки останавливаются".',
 u'"Подсека и пал: дерево сводят, чтобы поднять землю".',
 u'"Огонь выжигает землю, и крепость её уходит".',
]

E = io.open(base + 'Language_EN/NeiliType_language.txt', encoding='utf-8').read().split('\n')
R = io.open(base + 'Language_RU/NeiliType_language.txt', encoding='utf-8').read().split('\n')

d = collections.OrderedDict()
miss = []
for i in range(0, len(E) - 1, 2):
    k, en = E[i], E[i + 1]
    if CYR.search(R[i + 1]) or not en.strip():
        continue
    ru = None
    # Хуньюань стоит особняком: он не меняет предел мощи, а снижает требования
    if k == 'Desc_5':
        ru = SIMPLE[5] + u'\\n\\nТребования к применению всех боевых искусств ниже на 20%.'
    elif k == 'EffectDesc_5':
        ru = (u'Требования к применению всех боевых искусств '
              u'<color=#brightblue>ниже на 20%.</color>')
    elif k.startswith('Name_'):
        ru = NAMES[int(k[5:])]
    elif k.startswith('SimpleDesc_'):
        ru = SIMPLE[int(k[11:])]
    elif k.startswith('NeiliTypeConditionText_'):
        ru = apply(COND, TAG.sub('', en))
    elif k.startswith('EffectDesc_'):
        parts = [apply(EFF, p) for p in TAG.sub('', en).split('\\n')]
        ru = u'\\n'.join(parts) if all(parts) else None
    elif k.startswith('Desc_'):
        head, _, tail = en.partition('\\n\\n')
        parts = [apply(DSC, p) for p in TAG.sub('', tail).split('\\n')]
        if all(parts):
            ru = SIMPLE[int(k[5:])] + u'\\n\\n' + u'\\n'.join(parts)
    if ru:
        d[k] = ru
    else:
        miss.append((k, en[:100]))

io.open('bnei.json', 'w', encoding='utf-8').write(
    json.dumps({u'NeiliType_language.txt': d}, ensure_ascii=False, indent=1))
print('готово:', len(d), '| не разобрано:', len(miss))
for k, v in miss[:10]:
    print('   ', k, '|', v)
