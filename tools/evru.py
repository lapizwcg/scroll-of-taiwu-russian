# -*- coding: utf-8 -*-
# Делает русскую версию файла из Event/EventLanguages: копирует *_Language_EN.txt
# в *_Language_RU.txt и подменяет английские реплики по словарю.
# Словарь: JSON {"английская строка": "перевод"}. Совпадение точное, по хвосту
# строки после " : ", поэтому теги <NL>, <Character .../> и скобки не страдают.
import io, json, os, sys

DIR = u'C:/Games/The Scroll of Taiwu/Event/EventLanguages/'
MARKS = (u'-- EventContent : ', u'-- Option_')


def load(p):
    return json.load(io.open(p, encoding='utf-8'))


def run(pkg, dict_path, apply):
    src = DIR + u'Taiwu_EventPackage_%s_Language_EN.txt' % pkg
    dst = DIR + u'Taiwu_EventPackage_%s_Language_RU.txt' % pkg
    if not os.path.exists(src):
        sys.stdout.write(u'нет файла: %s\n' % src)
        return
    ru = load(dict_path) if dict_path else {}
    # Настоящий перевод строки внутри реплики разорвал бы файл событий:
    # переносить строку можно только тегом <NL>.
    broken = [k for k, v in ru.items() if u'\n' in v or u'\r' in v]
    if broken:
        for k in broken:
            sys.stdout.write(u'ОТКАЗ: в переводе настоящий перенос строки, нужен <NL>\n  %s\n' % k[:90])
        sys.stdout.write(u'ничего не записано\n')
        return
    base = io.open(dst if os.path.exists(dst) else src, encoding='utf-8').read()
    lines = base.split(u'\n')
    hit = 0
    miss = set(ru.keys())
    for i, ln in enumerate(lines):
        s = ln.lstrip(u'\t')
        if not s.startswith(u'--'):
            continue
        if u' : ' not in ln:
            continue
        head, val = ln.split(u' : ', 1)
        if val in ru:
            lines[i] = head + u' : ' + ru[val]
            hit += 1
            miss.discard(val)
    sys.stdout.write(u'%s: заменено %d, не найдено %d\n' % (pkg, hit, len(miss)))
    for m in sorted(miss):
        sys.stdout.write(u'  НЕ НАЙДЕНО: %s\n' % m[:90])
    if apply:
        with io.open(dst, 'w', encoding='utf-8', newline='') as f:
            f.write(u'\n'.join(lines))
        sys.stdout.write(u'записано: %s\n' % dst)


if __name__ == '__main__':
    pkg = sys.argv[1]
    dict_path = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] != '-' else None
    run(pkg, dict_path, '--apply' in sys.argv)
