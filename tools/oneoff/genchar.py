# -*- coding: utf-8 -*-
"""Character_language.txt: безымянные звания, особые звания и реплики немых.
Строки повторяются, поэтому переводим уникальные значения и раскатываем по ключам."""
import io, json, re, collections

base = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
CYR = re.compile(u'[\u0400-\u04FF]')
PREF = ('AnonymousTitle_', 'SpecialGradeName_', 'SpecialMuteBubbleSelf_', 'SpecialMuteBubbleEnemy_')

M = {
    # --- безымянные звания ---
    u'Demon': u'Демон',
    u'Young Girl': u'Девочка',
    u'Young Boy': u'Мальчик',
    u'Girl': u'Девушка',
    u'White-Robed Maiden': u'Дева в белом',
    u'Taoist': u'Даос',
    u'Strange Woman': u'Странная женщина',
    u'Strange Beast': u'Странный зверь',
    u'Sharp Claw Astragale': u'Астрагал с острым когтем',
    u'Night Watchman': u'Ночной сторож',
    u'Mysterious One': u'Таинственный незнакомец',
    u'Hall Master': u'Глава зала',
    u'Blind Assassin': u'Слепой убийца',
    u'Blackscale Serpent': u'Черночешуйчатый змей',
    u'Black-Robed Youth': u'Юноша в чёрном',
    u'Asura Maiden': u'Дева-асура',
    u'Wooden Dummy': u'Деревянный болван',
    u'Wretched Alchemist': u'Жалкий алхимик',
    u'Mirror Dweller': u'Обитатель зеркала',
    u'Woman': u'Женщина',
    u'Talking Dummy': u'Говорящий болван',
    u'Nameless Monster': u'Безымянное чудовище',
    u'Young Xiake': u'Молодой странствующий воин',
    u'Wrathful Elder': u'Гневный старец',
    u'White Robed Swordmaster': u'Мастер меча в белом',
    u'Western Damsel': u'Дева с запада',
    u'Unnamed Mother and Child': u'Безымянные мать и дитя',
    u'The Old': u'Старец',
    u'Red Robed Woman': u'Женщина в красном',
    u'Ranshan Spirit': u'Дух Жаньшань',
    u'Old Monk': u'Старый монах',
    u'Old Lady': u'Старуха',
    u'Oddity': u'Диковина',
    u'Nameless Woman': u'Безымянная женщина',
    u'Nameless Parents': u'Безымянные родители',
    u'Mysterious Youth': u'Таинственный юноша',
    u'Mysterious Monk': u'Таинственный монах',
    u'Muscular Young Man': u'Крепкий юноша',
    u'Mischievous Child': u'Озорной ребёнок',
    u'Middle-aged Man': u'Мужчина средних лет',
    u'Man': u'Мужчина',
    u'Liao Ancestry': u'Из рода Ляо',
    u'Languid Elder': u'Вялый старец',
    u'Kindly Elder': u'Добрый старец',
    u'Illusion in the Mirror': u'Морок в зеркале',
    u'Grave': u'Могила',
    u'Fuloong Envoy': u'Посланник Фулун',
    u'Crippled Elder': u'Увечный старец',
    u'Cold-Faced Elder': u'Хладноликий старец',
    u'Bronze Head': u'Бронзовая голова',
    u'Blind Lady': u'Слепая женщина',
    u'Black Robed One': u'Некто в чёрном',
    u'Automaton': u'Механический спутник',
    u'Alchemist': u'Алхимик',

    # --- особые звания ---
    u'Bamboo Incarnation': u'Воплощение бамбука',
    u'Bandit': u'Разбойник',
    u'Blade Path Demon': u'Демон пути клинка',
    u'Blood Path Demon': u'Демон пути крови',
    u'Blood Tomb Beauty': u'Красавица кровавой гробницы',
    u"Candelor's Tail Incarnation": u'Воплощение Хвоста Канделора',
    u'Chief Disciple of the Divine Sword School': u'Старший ученик школы Божественного меча',
    u'Chief Disciple of the Jade Seal School': u'Старший ученик школы Яшмовой печати',
    u'Chief Disciple of the Yin Yang School': u'Старший ученик школы инь и ян',
    u'Dark Flame': u'Тёмное пламя',
    u'Dark Frost Incarnation': u'Воплощение Тёмного инея',
    u'Demonbind Incarnation': u'Воплощение Оков демона',
    u'Divine Loong': u'Божественный лун',
    u'Divine Loong Incarnation': u'Воплощение божественного луна',
    u'Divine Sword School Founder': u'Основатель школы Божественного меча',
    u'Eight-Trigram Purple Ribbon Gown': u'Одеяние с пурпурной лентой восьми триграмм',
    u'Evil Flood Dragon': u'Злой цзяо',
    u'Evildoers': u'Злодеи',
    u'Exotic Fighter': u'Чужеземный боец',
    u'Fenghuang Cocoon Incarnation': u'Воплощение Кокона фэнхуана',
    u'Fire Path Demon': u'Демон пути огня',
    u'Five-Fire Seven-Bird Fan': u'Веер пяти огней и семи птиц',
    u'Flying Lion Hall Disciple': u'Ученик Зала летящего льва',
    u'Fuloong Fanatic': u'Изувер Фулун',
    u'Grimlord': u'Мрачный владыка',
    u'Hall Master of Flying Lion Hall': u'Глава Зала летящего льва',
    u'Heaven-Overturning Seal': u'Печать, опрокидывающая небо',
    u'Ignideus Blaze Incarnation': u'Воплощение Пламени Игнидея',
    u'Immortal Jade-Maiden': u'Бессмертная яшмовая дева',
    u'Immortal-Slaying Sword': u'Меч, разящий бессмертных',
    u'Jade Seal School Master': u'Наставник школы Яшмовой печати',
    u'Kongsang Traitor': u'Отступник Кунсан',
    u'Loong': u'Лун',
    u'Loong and Phoenix': u'Лун и фэнхуан',
    u'Loong-Binding Stake': u'Кол, вяжущий луна',
    u'Malevolent Mystic': u'Злокозненный тайновед',
    u'Monu Weave Incarnation': u'Воплощение Ткани Мону',
    u'Nameless Taoist': u'Безымянный даос',
    u'Nine-Loong Divine Flame Shroud': u'Плащ божественного пламени девяти лунов',
    u'Orphan of the Liao Family': u'Сирота из рода Ляо',
    u'Outland Raider': u'Налётчик из чужих земель',
    u'Outlandish Item': u'Диковинная вещь',
    u'Patriarch of the Earth Immortals': u'Патриарх земных бессмертных',
    u'Peculiar Serpent': u'Диковинный змей',
    u'Primordial True Elixir': u'Изначальный истинный эликсир',
    u'Pure Glazed Bottle': u'Чистый глазурный сосуд',
    u'Rainbow Ultima Incarnation': u'Воплощение Предела радуги',
    u'Reclusive Divine Maiden': u'Затворная божественная дева',
    u'Reclusive Divine Matron': u'Затворная божественная госпожа',
    u'Relics Searcher': u'Искатель реликвий',
    u'Retired Senior': u'Отошедший от дел старейшина',
    u'Seventh Generation of Taiwu': u'Тайу седьмого поколения',
    u'Shaolin Master': u'Наставник Шаолиня',
    u'Spiritsealer Incarnation': u'Воплощение Печати духов',
    u'The Mindless': u'Обезумевший',
    u'The Nine Offspring of the Loong': u'Девять сыновей луна',
    u'The Yufu Bloom': u'Цветок Юйфу',
    u'Three School Founders': u'Основатели трёх школ',
    u'Tomb Remains': u'Останки из гробницы',
    u'Trinity Treasure Mirror': u'Драгоценное зеркало триединства',
    u'Unknown Disciple': u'Неизвестный ученик',
    u'Valley of Flowers Master': u'Наставница Долины Сотни Цветов',
    u'Vanquisher': u'Победитель',
    u'Veil Scar Founder': u'Основатель Вуали-Шрама',
    u'Vitalos Incarnation': u'Воплощение Виталоса',
    u'White Ape Hermit': u'Отшельник-белая обезьяна',
    u'Xiangshu': u'Сяншу',
    u'Yin Yang School Founder': u'Основатель школы инь и ян',

    # --- бессловесные возгласы ---
    u'Wuuu... Gah...': u'У-у-у... Гх...',
    u'Gah gah gah gah...': u'Гх-гх-гх-гх...',
    u'Hoo... Hmph...': u'Ху... Хм...',
    u'Woooo\u2014': u'У-у-у-у\u2014',
    u'Moo... Hng...': u'Му-у... Хнг...',
    u'Hiss... Hiss...': u'Ш-ш-ш... Ш-ш-ш...',
    u'Woo... Ha! Hoo...': u'У-у... Ха! Ху...',
    u'Awoo\u2014woo...': u'А-у-у\u2014у-у...',
    u'Ha... Awoo!': u'Ха... А-у-у!',
    u'Hiss! Awoo\u2014': u'Ш-ш! А-у-у\u2014',
    u'Chirp... Chirp...': u'Чирик... Чирик...',
    u'Coo... Coo... Hum...': u'Ку... Ку... Гм...',
    u'Ha\u2014Awoo\u2014': u'Ха\u2014А-у-у\u2014',
    u'Hiss... Whoosh...': u'Ш-ш-ш... Вжух...',
    u'Moo\u2014': u'Му-у\u2014',
    u'Woo... Awoo!': u'У-у... А-у-у!',
    u'Woo... Whine...': u'У-у... И-и-и...',
    u'Awoo! Woo\u2014': u'А-у-у! У-у\u2014',

    # --- реплики ---
    u'A breeze sweeps away all demonic haze, pure air washes the spirit clean...':
        u'Ветер сметает всю демоническую мглу, чистый воздух омывает дух...',
    u'A just cause attracts abundant support. An unjust cause attracts little support.':
        u'У кого правда, у того и поддержки много. У кого её нет, тому помогать некому.',
    u'All the advantages and disadvantages are plain, Master. Let me assist you in this fight...':
        u'Все выгоды и слабости на виду, хозяин. Дай мне помочь тебе в этом бою...',
    u'All things that live and perish shall return to the void eventually...':
        u'Всё, что живёт и гибнет, в конце концов вернётся в пустоту...',
    u'Allow this old man to aid you in overcoming these foes...':
        u'Позволь старику помочь тебе одолеть этих врагов...',
    u'Betray me, deceive me, slander me.': u'Предай меня, обмани меня, оболги меня.',
    u'Blame me, accuse me, punish me...': u'Вини меня, обвиняй меня, карай меня...',
    u'Worry me, frighten me, torment me...': u'Тревожь меня, пугай меня, мучай меня...',
    u'God Trapper': u'Ловец богов',
    u'Calm yourself! With my divine needle, there is nothing to worry...':
        u'Успокойся! С моей божественной иглой тревожиться не о чем...',
    u'Do your best without regrets...': u'Сделай всё, что можешь, и не жалей ни о чём...',
    u"Don't harm Taiwu; I can fight too...": u'Не трогай Тайу, я тоже умею драться...',
    u"Heaven's way is merciless and runs forever!": u'Путь неба безжалостен и длится вечно!',
    u'Humans are the essence of the Five Elements\u2014how could Taiwu consort with demons?':
        u'Человек \u2014 суть пяти стихий; как может Тайу водиться с демонами?',
    u'Let me take the lead and clear a path for you against these foes...':
        u'Дай мне пойти первым и расчистить тебе дорогу через этих врагов...',
    u'Little do they know that we are also eternal, and will persist through all ages!':
        u'Невдомёк им, что и мы вечны и пребудем во все времена!',
    u'Move fast and finish strong; don\u2019t worry about taking damage\u2014my power will protect you...':
        u'Двигайся быстро и бей крепко; о ранах не думай \u2014 моя сила тебя защитит...',
    u"Move fast and finish strong; don't worry about taking damage\u2014my power will protect you...":
        u'Двигайся быстро и бей крепко; о ранах не думай \u2014 моя сила тебя защитит...',
    u'My Master is here, yield now before it\u2019s too late...':
        u'Мой хозяин здесь \u2014 сдавайся, пока не поздно...',
    u"My Master is here, yield now before it's too late...":
        u'Мой хозяин здесь \u2014 сдавайся, пока не поздно...',
    u'O Taiwu, I miss you so dearly...': u'О Тайу, как же я по тебе тоскую...',
    u'Since I have a moment free, Master, allow me to show you what I can do...':
        u'Раз выдалась свободная минута, хозяин, позволь показать, на что я гожусь...',
    u'The Star Fortune manifests; I shall aid you to shatter the enemies...':
        u'Звёздная судьба явила себя; я помогу тебе сокрушить врагов...',
    u'The Tao of Heaven has no favorites; it always aids the good man!':
        u'У небесного Дао нет любимцев: оно всегда помогает доброму человеку!',
    u'The earth bears all beneath its vast grace...':
        u'Земля несёт на себе всё под своей безмерной милостью...',
    u'The evil is purged\u2014never again shall you disturb the balance of the world!':
        u'Зло изгнано \u2014 больше ты не нарушишь равновесия мира!',
    u'The wise must understand the rise and fall of all things.':
        u'Мудрому должно понимать возвышение и упадок всего сущего.',
    u'To crave and to desire is human nature.': u'Алкать и желать \u2014 в природе человека.',
    u'Who are you pest to obstruct us? Move aside!':
        u'Что ты за букашка, чтобы нам мешать? Прочь с дороги!',
    u'You insolent thief, how dare you spoil our peaceful slumber...':
        u'Дерзкий вор, как ты смеешь тревожить наш покойный сон...',
}

E = io.open(base + 'Language_EN/Character_language.txt', encoding='utf-8').read().split('\n')
R = io.open(base + 'Language_RU/Character_language.txt', encoding='utf-8').read().split('\n')

d = collections.OrderedDict()
miss = collections.Counter()
for i in range(0, len(E) - 1, 2):
    k = E[i]
    if not k.startswith(PREF):
        continue
    if CYR.search(R[i + 1]):
        continue
    en = E[i + 1].strip()
    if not en:
        continue
    if en in M:
        d[k] = M[en]
    else:
        miss[en] += 1

io.open('bchar.json', 'w', encoding='utf-8').write(
    json.dumps({u'Character_language.txt': d}, ensure_ascii=False, indent=1))
print('переведено:', len(d), '| без пары:', sum(miss.values()))
for k, v in miss.most_common(20):
    print('   %3d  %s' % (v, k))
