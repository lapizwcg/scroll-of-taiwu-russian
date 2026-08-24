# -*- coding: utf-8 -*-
import io, json, re, collections

D = {
 u"Dullard": u"Тупица", u"Tailor's Needle": u"Портновская игла",
 u"Twin Spike": u"Двойной шип", u"Blaring Bell": u"Гремучий колокол",
 u"Sandy Stallion": u"Песчаный жеребец", u"Jade Pickaxe": u"Яшмовая кирка",
 u"Tabarded General": u"Полководец в накидке", u"Deathdealer": u"Смертонос",
 u"Cinnabar Champion": u"Киноварный чемпион", u"Dhutanga": u"Дхутанга",
 u"Iron Bullet": u"Железное ядро", u"Crimson Bullwhip": u"Багровый кнут",
 u"Jade Tail": u"Яшмовый хвост", u"Paper Lantern": u"Бумажный фонарь",
 u"Tricolor Tyrant": u"Трёхцветный тиран", u"Grasslurker": u"Затаившийся в траве",
 u"Imperial Gold": u"Императорское золото", u"Plum Wings": u"Сливовые крылья",
 u"Skyglow": u"Небесное зарево",
 u"Three-Color Segment Brocade": u"Трёхцветная узорная парча",
 u"Third Prince": u"Третий принц", u"The Eight-Failure": u"Восемь неудач",
 u"Flawless Blue": u"Безупречный синий", u"Flawless Yellow": u"Безупречный жёлтый",
 u"Flawless Purple": u"Безупречный лиловый", u"Flawless Red": u"Безупречный красный",
 u"Flawless Black": u"Безупречный чёрный", u"Flawless White": u"Безупречный белый",
 # головы
 u"Pumpkin Head": u"Тыквоголовый", u"Flathead": u"Плоскоголовый",
 u"Roundhead": u"Круглоголовый", u"Sharphead": u"Остроголовый",
 u"Squarehead": u"Квадратноголовый", u"Bighead": u"Большеголовый",
 u"Stripyhead": u"Полосатоголовый", u"Charcoalic": u"Углистый",
 u"Crimson Brow": u"Багровобровый", u"Golden Brow": u"Золотобровый",
 u"Cricket Angularis": u"Угловатый", u"Gemstonehead": u"Самоцветноголовый",
 u"Amberhead": u"Янтарноголовый", u"Butterflyhead": u"Бабочкоголовый",
 u"Jade Cauldron": u"Яшмовый котёл", u"Dragonflyhead": u"Стрекозоголовый",
 u"Buddhahead": u"Буддоголовый", u"Domedhead": u"Купологоловый",
 # крылья и спина
 u"Roundwing": u"Круглокрылый", u"Squarewing": u"Квадратнокрылый",
 u"Sharpwing": u"Острокрылый", u"Widewing": u"Ширококрылый",
 u"Shaleback": u"Сланцеспинный", u"Curlywing": u"Кудрявокрылый",
 u"Yin-Yang Wing": u"Крыло инь и ян", u"Raggedwing": u"Рванокрылый",
 u"Longwing": u"Длиннокрылый", u"Iriswing": u"Радужнокрылый",
 u"Argentback": u"Сереброспинный", u"Glasswing": u"Стеклокрылый",
 u"Inklightwing": u"Тушекрылый", u"Lapiswing": u"Лазуритокрылый",
 u"Lutewing": u"Лютнекрылый", u"Crosswing": u"Крестокрылый",
 u"Brocade": u"Парчовый",
 # челюсти
 u"Softtooth": u"Мягкозубый", u"Mottletooth": u"Пестрозубый",
 u"Ambertooth": u"Янтарнозубый", u"Iristooth": u"Радужнозубый",
 u"Ashentooth": u"Пепельнозубый", u"Scarlettooth": u"Алозубый",
 u"Dottooth": u"Точечнозубый", u"Textured Jaw": u"Узорчаточелюстный",
 u"Embossed Tooth": u"Чеканнозубый", u"Guillotine Tooth": u"Топорозубый",
 u"Speckled Tooth": u"Крапчатозубый", u"Twintooth": u"Двузубый",
 u"Crimsonjaw": u"Багровочелюстный", u"Coraljaw": u"Кораллочелюстный",
 u"Nailjaw": u"Гвоздечелюстный", u"Bonetooth": u"Костезубый",
 u"Bricktooth": u"Кирпичнозубый", u"Steeljaw": u"Стальночелюстный",
 u"Hugetooth": u"Огромнозубый",
 # глаза, усы, прочее
 u"Darkened Eye": u"Темноглазый", u"Unpaired Eye": u"Разноглазый",
 u"Yin-Yang Eye": u"Глаз инь и ян", u"Tristrand": u"Трёхжильный",
 u"Monostrand": u"Одножильный", u"Octostrand": u"Восьмижильный",
 u"Turtle-shell": u"Черепаховый", u"Champion Belt": u"Пояс чемпиона",
 u"Loongscale": u"Луночешуйчатый", u"Unpaired Antenna": u"Одноусый",
 u"Joint Antenna": u"Сдвоенноусый", u"Butterfly Antenna": u"Бабочкоусый",
 u"Iron Thorax": u"Железногрудый", u"Snowflake": u"Снежинка",
 u"Marble Thorax": u"Мраморногрудый", u"Spiked Claw": u"Шипастолапый",
 u"Loose Leg": u"Вольноногий", u"Octoleg": u"Восьминогий",
 u"Serpentine": u"Змеевидный", u"Scarlet Tail": u"Алохвостый",
 u"Blood Speckle": u"Кровекрапчатый", u"Tight Torso": u"Туготелый",
 u"Spindle": u"Веретёнчатый", u"Octomolt": u"Восьмилинный",
 u"Six-winged": u"Шестикрылый", u"Crimson Claw": u"Багровокогтый",
 # цвета
 u"Blue": u"Синий", u"Cyan": u"Голубой", u"Teal": u"Бирюзовый",
 u"Stonewash": u"Сизый", u"Cerulean": u"Лазурный", u"Cornflower": u"Васильковый",
 u"Cobalt": u"Кобальтовый", u"Celadon": u"Селадоновый", u"Ochre": u"Охристый",
 u"Buttercup": u"Лютиковый", u"Citrine": u"Цитриновый", u"Flaxen": u"Льняной",
 u"Brown": u"Бурый", u"Bronze": u"Бронзовый", u"Purple": u"Лиловый",
 u"Zi": u"Лиловый", u"Heather": u"Вересковый", u"Nightshade": u"Паслёновый",
 u"Heliotrope": u"Гелиотроповый", u"Magenta": u"Пурпурный", u"Lilac": u"Сиреневый",
 u"Red": u"Красный", u"Scarlet": u"Алый", u"Coral": u"Коралловый",
 u"Cerice": u"Вишнёвый", u"Vermilion": u"Киноварный", u"Crimson": u"Багровый",
 u"Sanguine": u"Кровавый", u"Garnet": u"Гранатовый", u"Black": u"Чёрный",
 u"Obsidian": u"Обсидиановый", u"Gray": u"Серый", u"Dusk": u"Сумеречный",
 u"Murk": u"Мглистый", u"Slate": u"Аспидный", u"Soot": u"Сажевый",
 u"Charcoal": u"Угольный", u"White": u"Белый", u"Ice": u"Ледяной",
 u"Beige": u"Бежевый", u"Mottled": u"Пёстрый", u"Peridot": u"Хризолитовый",
}

BASE = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
CYR = re.compile(u'[\u0400-\u04ff]')
el = io.open(BASE + u'Language_EN/CricketParts_language.txt', encoding='utf-8').read().split(u'\n')
rl = io.open(BASE + u'Language_RU/CricketParts_language.txt', encoding='utf-8').read().split(u'\n')

out = collections.OrderedDict()
missing = set()
for i in range(1, len(el) - 1, 2):
    k = el[i - 1]
    if not el[i].strip() or CYR.search(rl[i]) or k.startswith(u'Desc'):
        continue
    v = D.get(el[i])
    if v is None:
        missing.add(el[i])
    else:
        out[k] = v

if missing:
    for m in sorted(missing):
        print(u'НЕТ ПЕРЕВОДА: ' + m)
io.open('b374.json', 'w', encoding='utf-8').write(
    json.dumps({u'CricketParts_language.txt': out}, ensure_ascii=False, indent=1))
print(len(out))
