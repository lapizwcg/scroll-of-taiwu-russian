# -*- coding: utf-8 -*-
import io, json, collections

M = {
u'Strength': u'Сила', u'Agility': u'Проворство', u'Willpower': u'Сосредоточение',
u'Constitution': u'Телосложение', u'Root Bone': u'Костяк', u'Comprehension': u'Понимание',
u'Force': u'Напор', u'Precision': u'Искусность', u'Dexterity': u'Стремительность', u'Sway': u'Чарование',
u'Phy. Penetration': u'Физическое пробитие', u'Qi Penetration': u'Пробитие ци',
u'Resistance': u'Сопротивление', u'Parry': u'Парирование', u'Dodge': u'Уклонение', u'Poise': u'Твёрдость',
u'Phy. Defense': u'Физическая защита', u'Qi Defense': u'Защита ци',
u'Stance Recovery': u'Восстановление стойки', u'Inhale Recovery': u'Восстановление дыхания',
u'Movement Speed': u'Скорость перемещения', u'Footing Steadiness': u'Устойчивость',
u'Cast Speed': u'Скорость применения', u'Qi Burst': u'Всплеск ци',
u'Equipment Mastery': u'Владение снаряжением', u'Attack Speed': u'Скорость атаки',
u'Qi Art Efficacy': u'Действенность искусств ци', u'Breath Control': u'Владение дыханием',
u'Acritoxin Res.': u'Стойкость к жгучему', u'Umbritoxin Res.': u'Стойкость к теневому',
u'Cryotoxin Res.': u'Стойкость к морозному', u'Pyrotoxin Res.': u'Стойкость к огненному',
u'Necrotoxin Res.': u'Стойкость к гнилостному', u'Oneirotoxin Res.': u'Стойкость к дурманному',
u'Composure': u'Собранность', u'Wit': u'Смекалка', u'Enthusiasm': u'Пылкость', u'Valor': u'Отвага',
u'Fortitude': u'Упорство', u'Luck': u'Удача', u'Harmony': u'Согласие', u'Charm': u'Обаяние',
u'Fertility': u'Плодовитость', u'Preference Change Cycle': u'Срок смены пристрастий',
u'XP': u'Опыт', u'Lifespan': u'Срок жизни', u'Maximum Qi': u'Наибольшая ци',
u'Divine Art Attainment': u'Мастерство божественного искусства',
u'Divine Art': u'Божественное искусство',
u'Ghost Art Attainment': u'Мастерство призрачного искусства',
u'Ghost Art': u'Призрачное искусство',
u'Study Efficiency': u'Успешность изучения', u'Actual battle': u'Боевой опыт',
u'Cricket Affinity': u'Чутьё на сверчков',
u'Strength recovery': u'Восстановление силы', u'Agility recovery': u'Восстановление проворства',
u'Willpower recovery': u'Восстановление сосредоточения',
u'Constitution Recovery': u'Восстановление телосложения',
u'Root Bone recovery': u'Восстановление костяка', u'Comprehension recovery': u'Восстановление понимания',
u'Basic Resilience': u'Основная стойкость',
u'Love Confession Success Rate': u'Успех признания в любви',
u'Native Utility Slot': u'Своя вспомогательная ячейка', u'Attunement': u'Сродство',
u'Qi Art Power': u'Мощь искусств ци', u'Annihilation Power': u'Мощь Сокрушения',
u'Nimble Power': u'Мощь Ловкости', u'Protection Power': u'Мощь Защиты',
u'Acumen Power': u'Мощь Прозорливости',
u'Wound Resilience': u'Стойкость к увечьям', u'Mind Resilience': u'Стойкость разума',
u'Character Tactic': u'Расчёт персонажа',
u'True Qi Natural Recovery Speed': u'Естественное восстановление истинной ци',
u'True Qi Natural Decay Speed': u'Естественное убывание истинной ци',
u'Qi Arts Slot': u'Ячейка искусств ци', u'Annihilation Slot': u'Ячейка Сокрушения',
u'Nimble Slot': u'Ячейка Ловкости', u'Protection Slot': u'Ячейка Защиты',
u'Acumen Slot': u'Ячейка Прозорливости',
u'Toughness': u'Прочность', u'Armor Pierce': u'Пробитие брони', u'Blade Break': u'Слом клинка',
u'Weight': u'Вес', u'Durability': u'Долговечность', u'Attack': u'Нападение', u'Defense': u'Защита',
u'Follow-Up': u'Добивание', u'Pinpoint Strike': u'Прицельный удар',
u'External Injury Reduction': u'Снижение внешних ран',
u'Internal Injury Reduction': u'Снижение внутренних ран',
u'Reflection Power': u'Мощь отражения', u'Counter Power': u'Мощь контратаки',
u'Minimum Attack Range': u'Наименьшая дальность атаки',
u'Maximum Attack Range': u'Наибольшая дальность атаки',
u'Power Cap': u'Предел мощи', u'Usage Requirements': u'Требования к применению',
}

crafts = [
 (u'Music', u'музыки', u'Музыка'), (u'Weiqi', u'вэйци', u'Вэйци'),
 (u'Literature', u'словесности', u'Словесность'), (u'Painting', u'живописи', u'Живопись'),
 (u'Astrology', u'звездочётства', u'Звездочётство'), (u'Appreciation', u'оценки', u'Оценка'),
 (u'Smithing', u'кузнечества', u'Кузнечество'), (u'Carpentry', u'плотничества', u'Плотничество'),
 (u'Medical Arts', u'врачевания', u'Врачевание'), (u'Medical Art', u'врачевания', u'Врачевание'),
 (u'Toxicology', u'ядоделия', u'Ядоделие'), (u'Weaving', u'ткачества', u'Ткачество'),
 (u'Jewelcrafting', u'ювелирного дела', u'Ювелирное дело'), (u'Taoism', u'даосизма', u'Даосизм'),
 (u'Buddhism', u'буддизма', u'Буддизм'), (u'Culinary Arts', u'стряпни', u'Стряпня'),
 (u'Unorthodox Arts', u'тайных искусств', u'Тайные искусства'),
]
arts = [
 (u'Qi Arts', u'искусств ци', u'Искусства ци'), (u'Qi Art', u'искусств ци', u'Искусства ци'),
 (u'Footwork Arts', u'искусств Ловкости', u'Искусства Ловкости'),
 (u'Unique Arts', u'уникальных приёмов', u'Уникальные приёмы'),
 (u'Fist Arts', u'кулачных искусств', u'Кулачные искусства'),
 (u'Finger Arts', u'искусств пальцев', u'Искусства пальцев'),
 (u'Kicking Arts', u'искусств ног', u'Искусства ног'),
 (u'Concealed Weapons', u'скрытого оружия', u'Скрытое оружие'),
 (u'Sword Arts', u'искусств меча', u'Искусства меча'),
 (u'Blade Arts', u'искусств сабли', u'Искусства сабли'),
 (u'Polearm Arts', u'искусств древкового оружия', u'Искусства древкового оружия'),
 (u'Exotic Weapons', u'необычного оружия', u'Необычное оружие'),
 (u'Whip Arts', u'искусств плети', u'Искусства плети'),
 (u'Ranged Weapons', u'стрелкового оружия', u'Стрелковое оружие'),
 (u'Instrument Arts', u'музыкальных искусств', u'Музыкальные искусства'),
]
for en, gen, nom in crafts + arts:
    M[en + u' Talent'] = u'Одарённость: ' + nom
    M[en + u' Attainment'] = u'Мастерство: ' + nom
    M[en + u' Capacity'] = u'Ёмкость: ' + nom
    M.setdefault(en, nom)

parts = [(u'Head', u'головы'), (u'Torso', u'торса'), (u'Arm', u'рук'),
         (u'Midsection', u'поясницы'), (u'Legs', u'ног')]
for en, ru in parts:
    M[en + u' External Injury Resilience'] = u'Стойкость %s к внешним ранам' % ru
    M[en + u' Internal Injury Resilience'] = u'Стойкость %s к внутренним ранам' % ru

base = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
E = io.open(base + 'Language_EN/CharacterPropertyDisplay_language.txt', encoding='utf-8').read().split('\n')
d = collections.OrderedDict()
miss = set()
for i in range(0, len(E) - 1, 2):
    k = E[i]
    v = E[i + 1].strip()
    if not v:
        continue
    if not (k.startswith('Name_') or k.startswith('ShortName_')):
        continue
    if v in M:
        d[k] = M[v]
    else:
        miss.add(v)

# описания свойств
NL = chr(92) + 'n'
SP = lambda s: u'<SpName=%s>' % s
PY = u'<color=#pinkyellow>'
C = u'</color>'
d[u'Desc_0'] = (u'Сила — это способность человека применять грубую мощь...' + NL + NL + PY
    + u'Она повышает ' + SP('ui9_icon_attribute_hit_small_0') + u' напор и '
    + SP('ui9_icon_attribute_avoid_small_0') + u' сопротивление.' + NL
    + u'Повышает мощь боевых искусств, оружия и брони, которым нужна '
    + SP('ui9_icon_attribute_major_small_0') + u' сила.' + NL
    + u'Повышает наибольший вес снаряжения.' + NL
    + u'Чем старше человек, тем труднее восстанавливать силу.' + C)
d[u'Desc_1'] = (u'Проворство — это способность человека двигаться легко и ловко...' + NL + NL + PY
    + u'Оно повышает ' + SP('ui9_icon_attribute_hit_small_2') + u' стремительность и '
    + SP('ui9_icon_attribute_avoid_small_2') + u' уклонение.' + NL
    + u'Повышает мощь боевых искусств, оружия и брони, которым нужно '
    + SP('ui9_icon_attribute_major_small_1') + u' проворство.' + NL
    + u'Чем старше человек, тем труднее восстанавливать проворство.' + C)
d[u'Desc_2'] = (u'Сосредоточение — это способность человека владеть своей волей и судить здраво...' + NL + NL + PY
    + u'Оно повышает ' + SP('ui9_icon_attribute_hit_small_3') + u' чарование и '
    + SP('ui9_icon_attribute_avoid_small_3') + u' твёрдость.' + NL
    + u'Повышает мощь боевых искусств, оружия и брони, которым нужно '
    + SP('ui9_icon_attribute_major_small_2') + u' сосредоточение.' + NL
    + u'Чем старше человек, тем легче восстанавливать сосредоточение.' + C)
d[u'Desc_3'] = (u'Телосложение — это стойкость и выносливость человека...' + NL + NL + PY
    + u'Оно повышает ' + SP('ui9_icon_attribute_attack_small_0') + u'физическое пробитие и '
    + SP('ui9_icon_attribute_defence_small_0') + u' физическую защиту.' + NL
    + u'Повышает мощь боевых искусств, оружия и брони, которым нужно '
    + SP('ui9_icon_attribute_major_small_3') + u'телосложение.' + NL
    + u'Повышает число вещей, которые человек может потребить за месяц.' + NL
    + u'Чем старше человек, тем труднее восстанавливать телосложение.' + C)
d[u'Desc_4'] = (u'Костяк — это врождённое качество человека, добротность его костей и крови...' + NL + NL + PY
    + u'Он повышает ' + SP('ui9_icon_attribute_attack_small_1') + u' пробитие ци и '
    + SP('ui9_icon_attribute_defence_small_1') + u' защиту ци.' + NL
    + u'Повышает мощь боевых искусств, оружия и брони, которым нужен '
    + SP('ui9_icon_attribute_major_small_4') + u' костяк.' + NL
    + u'С возрастом костяк восстанавливать легче.' + C)
d[u'Desc_5'] = (u'Понимание — это способность человека постигать и чувствовать...' + NL + NL + PY
    + u'Оно повышает ' + SP('ui9_icon_attribute_hit_small_1') + u' искусность и '
    + SP('ui9_icon_attribute_avoid_small_1') + u' парирование.' + NL
    + u'Повышает мощь боевых искусств, оружия и брони, которым нужно '
    + SP('ui9_icon_attribute_major_small_5') + u' понимание.' + NL
    + u'Помогает в изучении книг и в прорывах боевых искусств.' + C)
d[u'Desc_6'] = (u'Умение сокрушить врага грубой силой и нанести ему урон...' + NL + NL + PY
    + u'На нём держатся удар кулаком, рубящий удар, бросок и прочее.' + C)
d[u'Desc_7'] = (u'Умение сбить врага с толку хитрым приёмом и нанести ему урон...' + NL + NL + PY
    + u'На нём держатся захват, подсечка снизу, толчок и прочее.' + C)
d[u'Desc_8'] = (u'Умение достать врага ошеломляющей быстротой и нанести ему урон...' + NL + NL + PY
    + u'На нём держатся тычок, укол, щелчок и прочее.' + C)
d[u'Desc_9'] = (u'Умение смутить врага чарующими звуками и нанести ему урон...' + NL + NL + PY
    + u'На нём держатся напев, заклятие и прочее.' + C)
d[u'Desc_10'] = u'Умение пробить физическую защиту врага и увеличить наносимые ему внешние раны...'
d[u'Desc_11'] = u'Умение пробить защиту ци врага и увеличить наносимые ему внутренние раны...'
d[u'Desc_12'] = u'Умение выдержать удар врага и не пострадать от атак напора...'
d[u'Desc_13'] = u'Умение отбить приём врага и не пострадать от атак искусности...'
d[u'Desc_14'] = u'Умение уйти от удара врага и не пострадать от атак стремительности...'
d[u'Desc_15'] = u'Умение устоять перед чарующими звуками врага и не пострадать от атак чарования...'
d[u'Desc_16'] = u'Умение сохранять телесную крепость и уменьшать внешние раны...'
d[u'Desc_17'] = u'Умение удерживать ци в равновесии и уменьшать внутренние раны...'
d[u'Desc_18'] = (u'Чем выше восстановление стойки, тем больше стойки человек получает всякий раз, '
    u'когда наносит оружейный удар или получает его.')
d[u'Desc_19'] = (u'Чем выше восстановление дыхания, тем быстрее оно восполняется. '
    u'Дыхание в основном тратится на боевые искусства ци.')
d[u'Desc_20'] = u'Чем выше скорость перемещения, тем быстрее человек движется в бою.'
d[u'Desc_21'] = u'Чем выше устойчивость, тем быстрее исчезают уязвимости человека в бою.'
d[u'Desc_22'] = u'Чем выше скорость применения, тем быстрее человек применяет боевые искусства в бою.'
d[u'Desc_23'] = u'Чем выше всплеск ци, тем быстрее раскрываются запечатанные точки человека в бою.'
d[u'Desc_24'] = (u'Чем выше владение снаряжением, тем короче перерыв при смене оружия в бою и тем '
    u'выше вероятность, что сработают действия оружия и брони.')
d[u'Desc_25'] = u'Чем выше скорость атаки, тем короче время исполнения оружейных ударов в бою.'
d[u'Desc_26'] = (u'Чем выше действенность искусств ци, тем шире можно менять соотношение ци и телесной '
    u'силы у боевых искусств и оружия.')
d[u'Desc_27'] = (u'Чем выше владение дыханием, тем быстрее сходит смятение внутреннего дыхания и тем меньше '
    u'его набирается. К тому же излишек истинной ци рассеивается в бою медленнее, а утраченная '
    u'истинная ци восполняется быстрее.')
d[u'Desc_28'] = u'Умение уберечь сердечные меридианы и противостоять жгучему токсину...'
d[u'Desc_29'] = u'Умение противостоять теневому токсину...'
d[u'Desc_30'] = u'Умение противостоять морозному токсину...'
d[u'Desc_31'] = u'Умение противостоять огненному токсину...'
d[u'Desc_32'] = u'Умение противостоять гнилостному токсину...'
d[u'Desc_33'] = u'Умение противостоять дурманному токсину...'
talent_order = [c[1] for c in crafts if c[0] != u'Medical Art']
for n, gen in zip(range(34, 50), talent_order):
    d[u'Desc_%d' % n] = u'Способность человека изучать и постигать %s...' % gen
for n, gen in zip(range(50, 66), talent_order):
    d[u'Desc_%d' % n] = u'Понимание, применение и достижения человека в области %s...' % gen
art_order = [a[1] for a in arts if a[0] != u'Qi Art']
for n, gen in zip(range(66, 80), art_order):
    d[u'Desc_%d' % n] = u'Способность человека изучать и постигать %s...' % gen
for n, gen in zip(range(80, 94), art_order):
    d[u'Desc_%d' % n] = u'Понимание, применение и достижения человека в области %s...' % gen
d[u'Desc_94'] = u'Умение человека справляться с запутанными обстоятельствами...'
d[u'Desc_95'] = u'Умение человека понимать и усваивать новое...'
d[u'Desc_96'] = u'Страсть человека к новизне, открытиям и общению...'
d[u'Desc_97'] = u'Умение человека смело встречать невзгоды...'
d[u'Desc_98'] = u'Сила воли человека, позволяющая терпеть крайние условия...'
d[u'Desc_99'] = u'Особый дар, данный человеку небом...'
d[u'Desc_100'] = u'Особое качество, данное человеку землёй...'
d[u'Desc_101'] = (u'Обаяние — это внешность человека и его личное очарование...' + NL + NL + PY
    + u'- К детям обаяние не применяется.' + NL
    + u'- Неопрятный вид резко снижает обаяние.' + NL
    + u'- Уровни обаяния (от низшего к высшему):' + NL + NL
    + SP('ui9_icon_charm_small_0') + u'<color=#AttractionType_NonHuman>Чудовищный</color>' + NL
    + SP('ui9_icon_charm_small_0') + u'<color=#AttractionType_Odious>Отвратительный</color>' + NL
    + SP('ui9_icon_charm_small_0') + u'<color=#AttractionType_Ugly>Уродливый</color>' + NL
    + SP('ui9_icon_charm_small_1') + u'<color=#AttractionType_Normal>Обычный</color>' + NL
    + SP('ui9_icon_charm_small_2') + u'<color=#AttractionType_Outstanding>Привлекательный</color>' + NL
    + SP('ui9_icon_charm_small_3') + u'<color=#AttractionType_Beautiful>Пригожий (муж.) / Изящная (жен.)</color>' + NL
    + SP('ui9_icon_charm_small_4') + u'<color=#AttractionType_Brilliant>Величавый (муж.) / Грациозная (жен.)</color>' + NL
    + SP('ui9_icon_charm_small_5') + u'<color=#AttractionType_Stunning>Несравненный</color>' + NL
    + SP('ui9_icon_charm_small_6') + u'<color=#AttractionType_Godlike>Неземной</color>' + C)
d[u'Desc_104'] = (u'Опыт — это всё пережитое человеком, его прозрения и понимание...' + NL + NL + PY
    + u'Опыт тратится на совершенствование в боевых искусствах.' + C)
d[u'Desc_111'] = u'Может заменить наименьшее из требований боевого искусства'
d[u'Desc_136'] = u'Заменяет наименьшее требование к применению.'

io.open('b142.json', 'w', encoding='utf-8').write(
    json.dumps({u'CharacterPropertyDisplay_language.txt': d}, ensure_ascii=False, indent=1))
print('ключей:', len(d))
print('не покрыто:', sorted(miss))
