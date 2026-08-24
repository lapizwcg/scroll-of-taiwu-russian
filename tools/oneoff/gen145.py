# -*- coding: utf-8 -*-
import io, json, collections

base = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
out = collections.OrderedDict()
miss = []


def do(fname, mapping):
    E = io.open(base + 'Language_EN/' + fname, encoding='utf-8').read().split('\n')
    d = collections.OrderedDict()
    for i in range(0, len(E) - 1, 2):
        v = E[i + 1].strip()
        if not v:
            continue
        if v in mapping:
            d[E[i]] = mapping[v]
        else:
            miss.append((fname, E[i], v))
    if d:
        out[fname] = d


# --- размер/сложение головы и тела
do('AvatarHead_language.txt', {
    u'Tiny': u'Крошечное', u'Small': u'Небольшое', u'Medium': u'Среднее', u'Apt': u'Ладное',
    u'Sturdy': u'Крепкое', u'Plump': u'Полное', u'Wiry': u'Жилистое', u'Slim': u'Худощавое',
    u'Chubby': u'Пухлое', u'Round': u'Круглое',
})

do('AvatarHairColors_language.txt', {
    u'Rose Violet': u'Розово-лиловый', u'Sandy Red': u'Песчано-рыжий', u'Dark Black': u'Смоляной',
    u'Cerise': u'Вишнёвый', u'Tawny': u'Рыжевато-бурый', u'Brown': u'Каштановый',
    u'Ivory': u'Слоновая кость', u'Antler': u'Олений рог', u'Chestnut': u'Каштановый тёмный',
    u'Amber Black': u'Янтарно-чёрный', u'Aquamarine': u'Аквамариновый', u'Cypress': u'Кипарисовый',
    u'Jasper': u'Яшмовый', u'Azure': u'Лазурный', u'Raven': u'Вороново крыло',
    u'Sea Green': u'Морская зелень', u'Moon': u'Лунный', u'Dark Blue': u'Тёмно-синий',
    u'Indigo': u'Индиго', u'Lavender': u'Лавандовый', u'Dark': u'Тёмный', u'Hazel': u'Ореховый',
    u'White': u'Белый', u'Gray': u'Седой', u'Black': u'Чёрный',
})

do('AvatarSkinColors_language.txt', {
    u'Whitish': u'Светлая', u'Medium': u'Обычная', u'Apt': u'Ровная', u'Darker': u'Смуглая',
})

eye = {u'Red': u'Красные', u'Brown': u'Карие', u'Gold': u'Золотые', u'Green': u'Зелёные',
       u'Cyan': u'Бирюзовые', u'Blue': u'Синие', u'Purple': u'Лиловые', u'White': u'Белые',
       u'Gray': u'Серые', u'Black': u'Чёрные'}
do('AvatarEyeballColors_language.txt', eye)

cloth = {u'Red': u'Красный', u'Brown': u'Бурый', u'Yellow': u'Жёлтый', u'Green': u'Зелёный',
         u'Cyan': u'Бирюзовый', u'Blue': u'Синий', u'Purple': u'Лиловый', u'White': u'Белый',
         u'Gray': u'Серый', u'Black': u'Чёрный'}
do('AvatarClothColors_language.txt', cloth)

io.open('b145.json', 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
print('файлов:', len(out), 'ключей:', sum(len(v) for v in out.values()))
for m in miss:
    print('НЕ ПОКРЫТО', m)
