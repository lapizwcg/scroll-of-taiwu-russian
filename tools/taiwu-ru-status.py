# -*- coding: utf-8 -*-
"""Статус перевода Language_RU. Запуск: python taiwu-ru-status.py [префикс_ключа]"""
import io, os, re, sys, collections

BASE = r"C:\Games\The Scroll of Taiwu\The Scroll of Taiwu_Data\StreamingAssets"
RU, EN = os.path.join(BASE, "Language_RU"), os.path.join(BASE, "Language_EN")
CYR = re.compile(u"[\u0400-\u04FF]")          # настоящая кириллица
LAT = re.compile(u"[A-Za-z]")

# Ключи, которых нет в английском файле, но которые игра запрашивает (баг игры:
# LK_MouseTip_Circket_Age_Content есть только в китайской локализации). Мы их
# дописываем в RU, поэтому строк там больше на указанное число.
EXTRA = {"ui_language.txt": 2}


def pairs(path):
    with io.open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    for i in range(0, len(lines) - 1, 2):
        yield lines[i].rstrip("\r"), lines[i + 1].rstrip("\r")


TAG = re.compile(u"<[^<>]*>")       # <color=#grey>, <NL>, <Character key=… />
PH = re.compile(u"\\{\\d+\\}")      # {0}, {1}
ESC = re.compile(u"\\\\[nv]")       # литеральные \n, \v


def strip_markup(val):
    """Убирает то, что переводить нельзя: теги, подстановки, escape-последовательности."""
    return ESC.sub(u" ", PH.sub(u" ", TAG.sub(u" ", val)))


def classify(val):
    if CYR.search(val):
        return "ru"
    if LAT.search(strip_markup(val)):
        return "en"
    return "neutral"            # {0}{1}, разметка, числа, пусто — переводить нечего


prefix = sys.argv[1] if len(sys.argv) > 1 else None
total = collections.Counter()
per_file, bad = [], []

for name in sorted(os.listdir(RU)):
    if not name.endswith(".txt"):
        continue
    ru_path, en_path = os.path.join(RU, name), os.path.join(EN, name)
    c = collections.Counter()
    for k, v in pairs(ru_path):
        if prefix and not k.startswith(prefix):
            continue
        c[classify(v)] += 1
    if not sum(c.values()):
        continue
    total.update(c)
    per_file.append((name, c))

    if os.path.exists(en_path) and not prefix:
        with io.open(ru_path, encoding="utf-8") as a, io.open(en_path, encoding="utf-8") as b:
            n_ru, n_en = len(a.read().split("\n")), len(b.read().split("\n"))
        if n_ru - n_en != EXTRA.get(name, 0):
            bad.append("%s: строк RU=%d EN=%d" % (name, n_ru, n_en))

if prefix:
    print(u"Префикс %s" % prefix)
todo = total["en"]
done = total["ru"]
pct = 100.0 * done / (done + todo) if done + todo else 100.0
print(u"переведено %d, осталось %d  (%.1f%%)  + %d без текста" % (done, todo, pct, total["neutral"]))

if bad:
    print(u"\nНЕСОВПАДЕНИЕ ЧИСЛА СТРОК:")
    for b in bad:
        print(u"  " + b)
elif not prefix:
    print(u"структура всех файлов цела")

if prefix or "-v" in sys.argv:
    for name, c in sorted(per_file, key=lambda x: -x[1]["en"])[:25]:
        if c["en"]:
            print(u"  %-48s осталось %5d" % (name, c["en"]))
