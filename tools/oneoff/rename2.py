# -*- coding: utf-8 -*-
"""Уточнение терминов: кулинария, астрология, экзотическое оружие, воля, долголетие.

Меняем только значения (чётные строки). Пишем во все три копии.
"""
import io, os, re, sys

ROOTS = [
    u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/Language_RU/',
    u'C:/Games/The Scroll of Taiwu/Mod/TaiwuRussian/Language_RU/',
    u'C:/Games/taiwu-ru-backup/Language_RU/',
]
APPLY = '--apply' in sys.argv

# --- замены по всему тексту (склонения перечислены явно) ---
PLAIN = [
    # стряпня -> кулинария
    (u'Стряпня', u'Кулинария'), (u'стряпня', u'кулинария'),
    (u'Стряпни', u'Кулинарии'), (u'стряпни', u'кулинарии'),
    (u'Стряпне', u'Кулинарии'), (u'стряпне', u'кулинарии'),
    (u'Стряпню', u'Кулинарию'), (u'стряпню', u'кулинарию'),
    (u'Стряпнёй', u'Кулинарией'), (u'стряпнёй', u'кулинарией'),
    # звездочётство -> астрология (звездочёт-человек и терраса остаются)
    (u'Звездочётство', u'Астрология'), (u'звездочётство', u'астрология'),
    (u'Звездочётства', u'Астрологии'), (u'звездочётства', u'астрологии'),
    (u'Звездочётству', u'Астрологии'), (u'звездочётству', u'астрологии'),
    (u'Звездочётстве', u'Астрологии'), (u'звездочётстве', u'астрологии'),
    (u'Звездочётством', u'Астрологией'), (u'звездочётством', u'астрологией'),
    # необычное оружие -> экзотическое оружие
    (u'Необычное оружие', u'Экзотическое оружие'),
    (u'необычное оружие', u'экзотическое оружие'),
    (u'Необычного оружия', u'Экзотического оружия'),
    (u'необычного оружия', u'экзотического оружия'),
    (u'Необычному оружию', u'Экзотическому оружию'),
    (u'необычному оружию', u'экзотическому оружию'),
    (u'Необычном оружии', u'Экзотическом оружии'),
    (u'необычном оружии', u'экзотическом оружии'),
    (u'Необычным оружием', u'Экзотическим оружием'),
    (u'необычным оружием', u'экзотическим оружием'),
    # срок жизни -> долголетие
    (u'Срок жизни', u'Долголетие'), (u'срок жизни', u'долголетие'),
    (u'Срока жизни', u'Долголетия'), (u'срока жизни', u'долголетия'),
    (u'Сроку жизни', u'Долголетию'), (u'сроку жизни', u'долголетию'),
]

# --- «сосредоточение» -> «воля» только там, где это основное свойство ---
WILL_KEYS = {
    'CharacterPropertyDisplay_language.txt': ['Name_2', 'ShortName_2', 'Desc_2',
                                              'Name_115', 'ShortName_115'],
    'CharacterTableElement_language.txt': ['Name_13'],
    'EventArgument_language.txt': ['CustomEnumText_19_2'],
    'SortItem_language.txt': ['Names_62_0'],
    'ProtagonistFeature_language.txt': ['Desc_8', 'EffectDesc_8'],
    'ui_language.txt': ['LK_Main_Attribute_Concentration',
                        'GM_EditBaseMainAttributes_Arg3_Name',
                        'GM_EditCurrMainAttributes_Arg3_Name',
                        'MonthlyEvent_MainAttributeType2',
                        'LK_MouseTip_Concentration_Recovery',
                        'LK_MouseTip_Concentration_Regen',
                        'LK_LegendaryBook_GiveUp_Desc_Corpse3',
                        'LK_LegendaryBook_GiveUp_Tips_Corpse3'],
}
WILL = [
    (u'Сосредоточение', u'Воля'), (u'сосредоточение', u'воля'),
    (u'Сосредоточения', u'Воли'), (u'сосредоточения', u'воли'),
    (u'Сосредоточению', u'Воле'), (u'сосредоточению', u'воле'),
    (u'Сосредоточении', u'Воле'), (u'сосредоточении', u'воле'),
    (u'Сосредоточением', u'Волей'), (u'сосредоточением', u'волей'),
]

# --- строки, которые после замены читались бы коряво ---
EXACT = {
    ('CharacterPropertyDisplay_language.txt', 'Desc_2'):
        u'Воля — это умение человека держать себя в руках и судить здраво...'
        u'\\n\\n<color=#pinkyellow>Она повышает <SpName=ui9_icon_attribute_hit_small_3> '
        u'чарование и <SpName=ui9_icon_attribute_avoid_small_3> твёрдость.\\n'
        u'Повышает мощь боевых искусств, оружия и брони, которым нужна '
        u'<SpName=ui9_icon_attribute_major_small_2> воля.\\n'
        u'Чем старше человек, тем легче восстанавливать волю.</color>',
    ('ui_language.txt', 'LK_LegendaryBook_GiveUp_Desc_Corpse3'):
        u'Искусен в том, чтобы страстями соблазнять и испытывать чужие '
        u'<SpName=ui9_icon_attribute_major_big_2>волю и '
        u'<SpName=ui9_icon_attribute_major_big_4>костяк',
    ('ui_language.txt', 'LK_LegendaryBook_GiveUp_Tips_Corpse3'):
        u'Ин Цзяо: <color=#pinkyellow>искусен в том, чтобы страстями соблазнять и '
        u'испытывать чужие <SpName=mousetip_zhuyao_2>волю и '
        u'<SpName=mousetip_zhuyao_4>костяк.</color>',
    ('ui_language.txt', 'LK_VillagerRole_EffectTip_Farmer_Extra'):
        u'Вероятность повторной готовки',
}

total = 0
for root in ROOTS:
    n_root = 0
    for fn in sorted(os.listdir(root)):
        if not fn.endswith('.txt'):
            continue
        L = io.open(root + fn, encoding='utf-8').read().split('\n')
        hit = 0
        for i in range(1, len(L), 2):
            key, old = L[i - 1], L[i]
            new = old
            if (fn, key) in EXACT:
                new = EXACT[(fn, key)]
            else:
                for a, b in PLAIN:
                    new = new.replace(a, b)
                if key in WILL_KEYS.get(fn, ()):
                    for a, b in WILL:
                        new = new.replace(a, b)
            if new != old:
                L[i] = new
                hit += 1
        if hit:
            n_root += hit
            if APPLY:
                with open(root + fn, 'wb') as out:
                    out.write(u'\n'.join(L).encode('utf-8'))
    print(u'%-24s строк: %d' % (root.split('/')[-3][:24], n_root))
    total += n_root
print(u'ИТОГО: %d | РЕЖИМ: %s' % (total, u'ЗАПИСЬ' if APPLY else u'проверка'))
