# -*- coding: utf-8 -*-
# Подсказки CommonTip игра берёт из Language_EN, а не из Language_RU
# (её загрузчик знает только CN/EN/KO/CNH/JP). Поэтому русские .json надо
# положить поверх английских — как и с диалогами в Event\EventLanguages.
# Оригиналы: C:\Games\taiwu-ru-backup\Language_EN_original\CommonTip\
import io, os, sys, shutil

SA = u'C:/Games/The Scroll of Taiwu/The Scroll of Taiwu_Data/StreamingAssets/'
SRC = SA + u'Language_RU/CommonTip/'
DST = SA + u'Language_EN/CommonTip/'
BAK = u'C:/Games/taiwu-ru-backup/Language_EN_original/CommonTip/'

apply = '--apply' in sys.argv
restore = '--restore' in sys.argv
n = 0
for dp, dn, fn in os.walk(SRC):
    for f in sorted(fn):
        rel = os.path.join(dp, f).replace(os.sep, u'/')[len(SRC):]
        if not os.path.exists(BAK + rel):
            sys.stdout.write(u'НЕТ РЕЗЕРВА, пропуск: %s\n' % rel)
            continue
        src = (BAK if restore else SRC) + rel
        sys.stdout.write(u'%s %s\n' % (u'восстановить' if restore else u'разложить', rel))
        if apply:
            d = os.path.dirname(DST + rel)
            if not os.path.isdir(d):
                os.makedirs(d)
            shutil.copyfile(src, DST + rel)
        n += 1
sys.stdout.write(u'файлов: %d%s\n' % (n, u'' if apply else u'  (пробный прогон, добавь --apply)'))
