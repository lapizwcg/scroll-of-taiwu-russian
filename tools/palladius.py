# -*- coding: utf-8 -*-
"""Транслитерация пиньиня в кириллицу по системе Палладия."""
import re

INIT = [
    ('zh', u'чж'), ('ch', u'ч'), ('sh', u'ш'),
    ('b', u'б'), ('p', u'п'), ('m', u'м'), ('f', u'ф'),
    ('d', u'д'), ('t', u'т'), ('n', u'н'), ('l', u'л'),
    ('g', u'г'), ('k', u'к'), ('h', u'х'),
    ('j', u'цз'), ('q', u'ц'), ('x', u'с'),
    ('r', u'ж'), ('z', u'цз'), ('c', u'ц'), ('s', u'с'),
]

# финали после согласной (обычный ряд)
FIN = {
    'a': u'а', 'o': u'о', 'e': u'э', 'i': u'и', 'u': u'у', 'v': u'юй',
    'ai': u'ай', 'ei': u'эй', 'ao': u'ао', 'ou': u'оу',
    'an': u'ань', 'en': u'энь', 'ang': u'ан', 'eng': u'эн', 'ong': u'ун',
    'er': u'эр',
    'ia': u'я', 'ie': u'е', 'iao': u'яо', 'iu': u'ю', 'iou': u'ю',
    'ian': u'янь', 'in': u'инь', 'iang': u'ян', 'ing': u'ин', 'iong': u'юн',
    'ua': u'уа', 'uo': u'о', 'uai': u'уай', 'ui': u'уй', 'uei': u'уй',
    'uan': u'уань', 'un': u'унь', 'uen': u'унь', 'uang': u'уан', 'ueng': u'уэн',
    've': u'юэ', 'van': u'юань', 'vn': u'юнь',
}

# нулевая инициаль
ZERO = {
    'a': u'а', 'ai': u'ай', 'an': u'ань', 'ang': u'ан', 'ao': u'ао',
    'e': u'э', 'ei': u'эй', 'en': u'энь', 'eng': u'эн', 'er': u'эр',
    'o': u'о', 'ou': u'оу',
    'yi': u'и', 'ya': u'я', 'yo': u'йо', 'ye': u'е', 'yao': u'яо', 'you': u'ю',
    'yan': u'янь', 'yin': u'инь', 'yang': u'ян', 'ying': u'ин', 'yong': u'юн',
    'yu': u'юй', 'yue': u'юэ', 'yuan': u'юань', 'yun': u'юнь',
    'wu': u'у', 'wa': u'ва', 'wo': u'во', 'wai': u'вай', 'wei': u'вэй',
    'wan': u'вань', 'wen': u'вэнь', 'wang': u'ван', 'weng': u'вэн',
}

# слоги-исключения целиком
EXC = {
    'zi': u'цзы', 'ci': u'цы', 'si': u'сы',
    'zhi': u'чжи', 'chi': u'чи', 'shi': u'ши', 'ri': u'жи',
    'me': u'мэ', 'lo': u'ло', 'hui': u'хуэй',
    'jue': u'цзюэ', 'que': u'цюэ', 'xue': u'сюэ',
    'juan': u'цзюань', 'quan': u'цюань', 'xuan': u'сюань',
    'jun': u'цзюнь', 'qun': u'цюнь', 'xun': u'сюнь',
    'ju': u'цзюй', 'qu': u'цюй', 'xu': u'сюй',
    'yai': u'яй',
}

VALID = set(EXC) | set(ZERO)
for ini, _ in INIT:
    for fin in FIN:
        VALID.add(ini + fin)
# уберём заведомо несуществующие сочетания не станем — лишние варианты
# отсекает жадный разбор по фактическим данным


def syllable(s):
    if s in EXC:
        return EXC[s]
    if s in ZERO:
        return ZERO[s]
    for ini, cyr in INIT:
        if s.startswith(ini):
            fin = s[len(ini):]
            if ini in ('j', 'q', 'x'):
                fin = fin.replace('u', 'v', 1) if fin.startswith('u') else fin
            if fin in FIN:
                return cyr + FIN[fin]
    return None


def split_syllables(w, i=0):
    """Разбор слова на слоги с откатом: сначала пробуем самый длинный."""
    w = w.lower()
    if i == len(w):
        return []
    for n in range(min(6, len(w) - i), 0, -1):
        part = w[i:i + n]
        if syllable(part) is None:
            continue
        rest = split_syllables(w, i + n)
        if rest is not None:
            return [part] + rest
    return None


YOT = u'яеюё'


def translit(word):
    """Пиньинь -> кириллица. Первая буква прописная."""
    parts = split_syllables(word)
    if parts is None:
        return None
    res = u''
    for p in parts:
        c = syllable(p)
        # слог на -ng даёт "н"; перед я/е/ю/ё нужен разделительный ъ
        if res.endswith(u'н') and c[0] in YOT:
            res += u'ъ'
        res += c
    return res[0].upper() + res[1:]


if __name__ == '__main__':
    import io, sys
    for line in io.open(sys.argv[1], encoding='utf-8'):
        w = line.strip()
        if w:
            print(u'%-14s %s' % (w, translit(w)))
