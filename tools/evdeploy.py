# -*- coding: utf-8 -*-
# Игра НЕ читает суффикс _Language_RU: её загрузчик знает только CN/EN/KO/CNH/JP
# и при русском языке берёт _Language_EN. Поэтому перевод разворачивается так:
#   1) evru.py делает *_Language_RU.txt — это наш исходник, его и правим;
#   2) evdeploy.py кладёт его поверх *_Language_EN.txt — это то, что читает игра.
# Нетронутые английские оригиналы лежат в
#   C:\Games\taiwu-ru-backup\EventLanguages_EN_original\
# Скрипт откажется работать, если резервной копии для файла там нет.
import io, os, sys, shutil

DIR = u'C:/Games/The Scroll of Taiwu/Event/EventLanguages/'
BAK = u'C:/Games/taiwu-ru-backup/EventLanguages_EN_original/'

apply = '--apply' in sys.argv
restore = '--restore' in sys.argv
names = [a for a in sys.argv[1:] if not a.startswith('--')]

ru_files = sorted(f for f in os.listdir(DIR) if f.endswith(u'_Language_RU.txt'))
if names:
    ru_files = [f for f in ru_files if any(n in f for n in names)]

done = 0
for f in ru_files:
    en = f.replace(u'_Language_RU.txt', u'_Language_EN.txt')
    if not os.path.exists(BAK + en):
        sys.stdout.write(u'НЕТ РЕЗЕРВА, пропуск: %s\n' % en)
        continue
    if restore:
        sys.stdout.write(u'восстановить %s\n' % en)
        if apply:
            shutil.copyfile(BAK + en, DIR + en)
        done += 1
        continue
    src = io.open(DIR + f, encoding='utf-8').read()
    sys.stdout.write(u'%-64s -> %s\n' % (f, en))
    if apply:
        with io.open(DIR + en, 'w', encoding='utf-8', newline='') as h:
            h.write(src)
    done += 1
sys.stdout.write(u'файлов: %d%s\n' % (done, u'' if apply else u'  (пробный прогон, добавь --apply)'))
