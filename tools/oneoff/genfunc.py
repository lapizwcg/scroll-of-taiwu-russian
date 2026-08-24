# -*- coding: utf-8 -*-
u"""FunctionDesc в Material_language.txt: 53 уникальные строки на 347 мест.

Это подсказка «на что годится припас». Текст шаблонный, поэтому переводим
каждую строку один раз и разворачиваем по всем ключам.

Цветовые теги переносятся дословно вместе с их странностями: в кулинарных
строках точка стоит ЗА закрывающим </color>, и так и должно остаться.

Свойства сведены по парам «основное свойство -> вид попадания + вид отклонения»
(см. CLAUDE.md): английская локализация зовёт их вразнобой — Accuracy это
искусность (Precision), Drive это чарование (Sway), Integrity это твёрдость
(Poise). Идём по паре, а не по слову.
"""
import io, json, re

P = u'<color=#pinkyellow>'
R_ = u'<color=#brightred>'
C = u'</color>'

MAP = {
    # припасы для ремесла
    u'Used to craft wooden equipment and vehicles, ':
        u'Идёт на деревянное снаряжение и средства передвижения, ',
    u'but not seals.': u'но не на печати.',
    u'Used to craft vine equipment and vehicles,':
        u'Идёт на лозовое снаряжение и средства передвижения,',
    u'but not mechanisms or seals.': u'но не на механизмы и печати.',
    u'Used to craft iron equipment, ': u'Идёт на железное снаряжение, ',
    u'but not seals or whips.': u'но не на печати и плети.',
    u'Used to craft gold/silver equipment and vehicles, ':
        u'Идёт на золотое и серебряное снаряжение и средства передвижения, ',
    u'but not mechanisms, seals, or whips.':
        u'но не на механизмы, печати и плети.',
    u'Used to craft stone equipment and vehicles, ':
        u'Идёт на каменное снаряжение и средства передвижения, ',
    u'Used to craft jade equipment, ': u'Идёт на яшмовое снаряжение, ',
    u'but not mechanisms or whips.': u'но не на механизмы и плети.',
    u'Used to craft fur equipment, clothing, pouches, and ropes, ':
        u'Идёт на меховое снаряжение, одежду, сумки и верёвки, ',
    u'but not weapons other than gloves and whips.':
        u'но из оружия — только на перчатки и плети.',
    u'Used to craft fabric equipment, clothing, pouches, and ropes, ':
        u'Идёт на тканое снаряжение, одежду, сумки и верёвки, ',
    u'but not weapons other than seals, gloves, or whips.':
        u'но из оружия — только на печати, перчатки и плети.',
    # перековка и цзяо
    u'Used to refine weapons, armor, and relics to enhance equipment attributes.':
        u'Идёт на перековку оружия, доспехов и реликвий — поднимает их свойства.',
    u'Used to hatch young Jiao in the Jiao Pool of Taiwu Village.':
        u'Идёт на выведение молодых цзяо в пруду цзяо деревни Тайу.',
    u'Used to raise Jiao in the Jiao Pool of Taiwu Village.':
        u'Идёт на выращивание цзяо в пруду цзяо деревни Тайу.',
}

# Яды: шесть токсинов.
TOX = [(u'Acritoxin', u'жгучий'), (u'Umbritoxin', u'теневой'),
       (u'Cryotoxin', u'морозный'), (u'Pyrotoxin', u'огненный'),
       (u'Necrotoxin', u'гнилостный'), (u'Oneirotoxin', u'дурманный')]
for en, ru in TOX:
    for verb in (u'make %s poison', u'make %s Poison'):
        MAP[u'Used to %s, or craft Arsenopyrite containing %s.'
            % (verb % en, en)] = (
            u'Идёт на %s яд, а также на мышьяковую руду с %s токсином.'
            % (ru, ru))

# Пилюли: «увеличить X или усилить Y».
EFF = {
    u'healing external injuries': u'лечения внешних ран',
    u'healing internal injuries': u'лечения внутренних ран',
    u'regulating Inner Breath': u'выправления внутреннего дыхания',
    u'restoring health': u'возвращения здоровья',
    u'increasing Force': u'напора',
    u'enhancing Force': u'напора',
    u'increasing Phy. Defense': u'физической защиты',
    u'enhancing Phy. Defense': u'физической защиты',
    u'increasing Attack Speed and Equipment Mastery':
        u'скорости атаки и владения снаряжением',
    u'increasing Qi Defense': u'защиты ци',
    u'enhancing Qi Defense': u'защиты ци',
    u'increasing Accuracy': u'искусности',
    u'enhancing Accuracy': u'искусности',
    u'increasing Resistance': u'сопротивления',
    u'enhancing Resistance': u'сопротивления',
    u'increasing Movement Speed and Steadiness':
        u'скорости перемещения и устойчивости',
    u'increasing Parry': u'парирования',
    u'enhancing Parry': u'парирования',
    u'increasing Inhale and Stance Speed':
        u'восстановления дыхания и стойки',
    u'increasing Dodge': u'уклонения',
    u'enhancing Dodge': u'уклонения',
    u'increasing Dexterity': u'стремительности',
    u'enhancing Dexterity': u'стремительности',
    u'increasing Qi Penetration': u'пробития ци',
    u'enhancing Qi Penetration': u'пробития ци',
    u'increasing Phy. Penetration': u'физического пробития',
    u'enhancing Phy. Penetration': u'физического пробития',
    u'increasing Casting Speed and Qi Burst':
        u'скорости применения и всплеска ци',
    u'enhancing Casting Speed and Qi Burst':
        u'скорости применения и всплеска ци',
}
for en, ru in TOX:
    EFF[u'neutralizing %s' % en] = u'снятия %s токсина' % ru

PILL = re.compile(u'^Used to make Pills for (.+?) or (.+?), '
                  u'also used to craft Poison Creams\\.$')
COOK = re.compile(u'^Used to cook (Meat|Vegetarian) Dishes for '
                  u'recovering (\\w[\\w. ]*?) and increasing ([\\w. ]+?) ?$')

ATTR = {u'Strength': u'силу', u'Agility': u'проворство',
        u'Willpower': u'волю', u'Constitution': u'телосложение',
        u'Root Bone': u'костяк', u'Comprehension': u'понимание'}
BOOST = {u'Phy. Defense': u'физическую защиту',
         u'Phy. Penetration': u'физическое пробитие',
         u'Qi Defense': u'защиту ци', u'Qi Penetration': u'пробитие ци',
         u'Resistance': u'сопротивление', u'Dodge': u'уклонение',
         u'Dexterity': u'стремительность', u'Force': u'напор',
         u'Integrity': u'твёрдость', u'Parry': u'парирование',
         u'Accuracy': u'искусность', u'Drive': u'чарование'}

BASE = (u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/'
        u'StreamingAssets/')
FN = u'Material_language.txt'
CYR = re.compile(u'[\u0400-\u04ff]')

E = io.open(BASE + u'Language_EN/' + FN, encoding='utf-8').read().split(u'\n')
RU = io.open(BASE + u'Language_RU/' + FN, encoding='utf-8').read().split(u'\n')

out, unknown = {}, set()
for i in range(0, min(len(E), len(RU)) - 1, 2):
    k = E[i].strip()
    if not k.startswith(u'FunctionDesc') or CYR.search(RU[i + 1]):
        continue
    v = E[i + 1]
    plain = re.sub(u'</?color[^>]*>', u'', v).strip()

    m = PILL.match(plain)
    if m and m.group(1) in EFF and m.group(2) in EFF:
        out[k] = (P + u'Идёт на пилюли для %s или %s, а также на ядовитые мази.'
                  % (EFF[m.group(1)], EFF[m.group(2)]) + C)
        continue
    m = COOK.match(plain.rstrip(u'.').strip())
    if m and m.group(2) in ATTR and m.group(3).strip() in BOOST:
        kind = u'мясные' if m.group(1) == u'Meat' else u'постные'
        out[k] = (P + u'Идёт на %s блюда, что возвращают %s и поднимают %s'
                  % (kind, ATTR[m.group(2)], BOOST[m.group(3).strip()]) + C + u'.')
        continue
    # составные строки из двух кусков (ремесло)
    parts = re.findall(u'<color=#(\\w+)>([^<]*)</color>', v)
    if parts and all(t in MAP for _, t in parts):
        out[k] = u''.join(u'<color=#%s>%s</color>' % (c, MAP[t])
                          for c, t in parts)
        continue
    if plain in MAP:
        out[k] = P + MAP[plain] + C
        continue
    unknown.add(v)

with io.open('b339.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps({FN: out}, ensure_ascii=False, indent=2))

print(u'собрано: %d' % len(out))
for v in sorted(unknown):
    print(u'  НЕ РАЗОБРАНО: %s' % v[:160])
