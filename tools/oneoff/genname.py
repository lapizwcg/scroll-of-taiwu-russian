# -*- coding: utf-8 -*-
"""Name_language.txt: слоги имён, фамилии, монашеские имена, тибетские имена, топонимы."""
import io, json, re, collections
from palladius import translit

base = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
CYR = re.compile(u'[\u0400-\u04FF]')

# английские слова, которыми локализация заменила смысл иероглифа
WORDS = {
    u"A'": u'А', u'Bear': u'Медведь', u'Break': u'Разлом', u'Child': u'Дитя',
    u'Fangs': u'Клыки', u'Fight': u'Бой', u'Image': u'Образ', u'Okay': u'Ладный',
    u'Place': u'Место',
    # опечатка английской локализации: Zigui (秭归) + kou
    u'Zigruikou': u'Цзыгуйкоу',
}

# тип поселения ставим впереди, как принято в русских картах
KIND = {
    u'Town': u'городок', u'Village': u'деревня', u'Township': u'волость',
    u'Fort': u'крепость', u'Post': u'станция', u'Pass': u'застава',
    u'Mountain': u'гора',
}

ZANG = {
 u'Ajia': u'Аджа', u'Baizong': u'Байцзун', u'Bapa': u'Бапа', u'Buchi': u'Бучи',
 u'Changchub': u'Чанчуб', u'Chijia': u'Чицзя', u'Chodak': u'Чодак',
 u'Choephel': u'Чопхел', u'Chogyal': u'Чогьял', u'Choli': u'Чоли',
 u'Chudron': u'Чудрон', u'Chungda': u'Чунда', u'Dargye': u'Даргье',
 u'Dawa': u'Дава', u'Dekyi': u'Декьи', u'Delek': u'Делек', u'Dhondup': u'Дондуб',
 u'Doren': u'Дорен', u'Dorje': u'Дордже', u'Dorjin': u'Дорджин',
 u'Drokar': u'Дрокар', u'Drugyal': u'Другьял', u'Duoji': u'Дуоцзи',
 u'Garong': u'Гарон', u'Gelek': u'Гелек', u'Geli': u'Гели', u'Gonpo': u'Гонпо',
 u'Gyantsen': u'Гьянцен', u'Gyatso': u'Гьяцо', u'Gyelpo': u'Гьелпо',
 u'Heiba': u'Хэйба', u'Jamba': u'Джамба', u'Jamyang': u'Джамьян',
 u'Janan': u'Джанан', u'Jare': u'Джаре', u'Jashi': u'Джаши', u'Jiahei': u'Цзяхэй',
 u'Jigme': u'Джигме', u'Jinpa': u'Джинпа', u'Karma': u'Карма',
 u'Kelsang': u'Келсан', u'Kunsang': u'Кунсан', u'Laba': u'Лаба',
 u'Ladron': u'Ладрон', u'Lakyi': u'Лакьи', u'Langdi': u'Ланди',
 u'Langri': u'Ланри', u'Latse': u'Лаце', u'Lhamo': u'Лхамо',
 u'Lhundrup': u'Лхундруб', u'Lobsang': u'Лобсан', u'Loden': u'Лоден',
 u'Lodro': u'Лодро', u'Lodroe': u'Лодрё', u'Maqung': u'Мачун', u'Metok': u'Меток',
 u'Mima': u'Мима', u'Namgyal': u'Намгьял', u'Namkha': u'Намкха', u'Nari': u'Нари',
 u'Nasen': u'Насен', u'Ngawang': u'Нгаван', u'Ngodup': u'Нгодуб',
 u'Norbu': u'Норбу', u'Nyima': u'Ньима', u'Oser': u'Осер', u'Pachou': u'Пачоу',
 u'Pasang': u'Пасан', u'Pawo': u'Паво', u'Pema': u'Пема', u'Pemba': u'Пемба',
 u'Phajia': u'Пхацзя', u'Phajo': u'Пхаджо', u'Phuntsok': u'Пхунцок',
 u'Phurbu': u'Пхурбу', u'Rangjung': u'Ранджун', u'Rangzu': u'Ранцзу',
 u'Rinchen': u'Ринчен', u'Samdup': u'Самдуб', u'Sangmo': u'Сангмо',
 u'Sangye': u'Сангье', u'Senge': u'Сенге', u'Shamba': u'Шамба',
 u'Solang': u'Солан', u'Sona': u'Сона', u'Sonam': u'Сонам', u'Tashi': u'Таши',
 u'Tendu': u'Тенду', u'Tenpa': u'Тенпа', u'Tenzhu': u'Тэнчжу', u'Tenzin': u'Тензин',
 u'Thubten': u'Тхубтен', u'Trinley': u'Тринлей', u'Tsangjo': u'Цанджо',
 u'Tsangla': u'Цангла', u'Tsedan': u'Цедан', u'Tserang': u'Цэран',
 u'Tsering': u'Цэрин', u'Tseringchung': u'Цэринчун', u'Tseringdon': u'Цэриндон',
 u'Tseringdruk': u'Цэриндрук', u'Tseringgyel': u'Цэрингьел',
 u'Tseringkyi': u'Цэринкьи', u'Tseringnyima': u'Цэриньима',
 u'Tseringsung': u'Цэринсун', u'Tseringxi': u'Цэринси', u'Tsewang': u'Цэван',
 u'Tsomu': u'Цому', u'Tsultrim': u'Цултрим', u'Wangdu': u'Ванду',
 u'Wanggyel': u'Вангьел', u'Wangmo': u'Ванмо', u'Wengding': u'Вэндин',
 u'Yangchen': u'Янчен', u'Yangla': u'Янла', u'Yangzom': u'Янцзом',
 u'Yeshe': u'Еше', u'Yeshi': u'Еши', u'Zhuoma': u'Чжома',
}


def pinyin(w):
    """Транслитерация с учётом апострофа как границы слогов."""
    if u"'" in w:
        parts = [translit(p) for p in w.split(u"'")]
        if any(p is None for p in parts):
            return None
        return parts[0] + u''.join(p.lower() for p in parts[1:])
    return translit(w)


def render(key, en):
    if en in WORDS:
        return WORDS[en]
    if key.startswith('Zang_'):
        return ZANG.get(en)
    if key.startswith('TownName_'):
        bits = en.split()
        if len(bits) == 2 and bits[1] in KIND:
            p = pinyin(bits[0])
            return None if p is None else u'%s %s' % (KIND[bits[1]], p)
        if len(bits) == 1:
            return pinyin(en)
        return None
    return pinyin(en)


E = io.open(base + 'Language_EN/Name_language.txt', encoding='utf-8').read().split('\n')
R = io.open(base + 'Language_RU/Name_language.txt', encoding='utf-8').read().split('\n')

d = collections.OrderedDict()
miss = collections.Counter()
for i in range(0, len(E) - 1, 2):
    k = E[i]
    if CYR.search(R[i + 1]):
        continue
    en = E[i + 1].strip()
    if not en:
        continue
    ru = render(k, en)
    if ru:
        d[k] = ru
    else:
        miss[en] += 1

io.open('bname.json', 'w', encoding='utf-8').write(
    json.dumps({u'Name_language.txt': d}, ensure_ascii=False, indent=1))
print('переведено:', len(d), '| без пары:', sum(miss.values()), 'уникальных:', len(miss))
for k, v in sorted(miss.items())[:40]:
    print('   %3d  %s' % (v, k))
