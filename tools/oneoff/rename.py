# -*- coding: utf-8 -*-
"""Глобальное переименование терминов в уже переведённых файлах.

  Sect              «школа»            -> «секта»
  Valley of Flowers «Долина Ста Цветов» -> «Долина Сотни Цветов»

Трогает только чётные строки (значения); ключи ASCII, но так надёжнее.
Пишет UTF-8 без BOM с переводами строк LF, число строк не меняется.
"""
import io, os, re, sys, codecs

# все падежные формы: «школ» + окончание -> «сект» + то же окончание
ENDINGS = [u'ами', u'ах', u'ам', u'ой', u'ою', u'а', u'ы', u'е', u'у', u'']
FORMS = []
for e in sorted(ENDINGS, key=len, reverse=True):
    FORMS.append((u'школ' + e, u'сект' + e))
    FORMS.append((u'Школ' + e, u'Сект' + e))
# «школ» как основа слова: граница справа обязательна, чтобы не задеть
# «школьный», «дошкольный» и т.п.
PAT = re.compile(u'(?<![А-Яа-яЁё])([ШШш]кол(?:ами|ах|ам|ой|ою|а|ы|е|у)?)(?![А-Яа-яЁё])')
MAP = dict(FORMS)

VALLEY = ((u'Долина Ста Цветов', u'Долина Сотни Цветов'),
          (u'Долины Ста Цветов', u'Долины Сотни Цветов'),
          (u'Долине Ста Цветов', u'Долине Сотни Цветов'),
          (u'Долину Ста Цветов', u'Долину Сотни Цветов'),
          (u'Долиной Ста Цветов', u'Долиной Сотни Цветов'))


def fix(v):
    n = 0
    def sub(m):
        w = m.group(1)
        return MAP.get(w, w)
    v2 = PAT.sub(sub, v)
    if v2 != v:
        n += 1
    v = v2
    for a, b in VALLEY:
        if a in v:
            v = v.replace(a, b)
            n += 1
    return v, n


def run(root, dry):
    total_files = 0
    total_lines = 0
    for f in sorted(os.listdir(root)):
        if not f.endswith('.txt'):
            continue
        path = os.path.join(root, f)
        lines = io.open(path, encoding='utf-8').read().split('\n')
        hits = 0
        for i in range(1, len(lines), 2):
            v, n = fix(lines[i])
            if n:
                lines[i] = v
                hits += 1
        if hits:
            total_files += 1
            total_lines += hits
            print('%6d  %s' % (hits, f))
            if not dry:
                text = '\n'.join(lines)
                with open(path, 'wb') as out:
                    out.write(text.encode('utf-8'))
    print('---')
    print('%s: файлов %d, строк %d' % (root, total_files, total_lines))


if __name__ == '__main__':
    dry = '--apply' not in sys.argv
    roots = [
        u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/Language_RU',
        u'C:/Games/The Scroll of Taiwu/Mod/TaiwuRussian/Language_RU',
        u'C:/Games/taiwu-ru-backup/Language_RU',
    ]
    for r in roots:
        if os.path.isdir(r):
            run(r, dry)
        else:
            print('нет папки:', r)
    print('РЕЖИМ:', 'проверка (без записи)' if dry else 'ЗАПИСЬ')
