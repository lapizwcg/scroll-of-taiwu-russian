# -*- coding: utf-8 -*-
import io

p = u'C:/Games/taiwu-ru-progress.md'
t = io.open(p, encoding='utf-8').read()

old_state = u"""**Осталось по созданию персонажа:** длинные описания сект в `Organization_language.txt`
(`Desc_1…15`, `OrganizationExtraDesc_*`, `TaiwuVillageSteleDesc_*` — по 5–8 строк каждое),
описания шести путей перерождения `DestinyType Desc_0…5`, `ConsummateLevel Desc_*`,
`CharacterTableElement_language.txt` (107), `VillagerRole_language.txt` (37).
`CharacterFeature_language.txt` и `BehaviorType_language.txt` закрыты полностью.
В `ui_language.txt` осталось ~7520; крупных блоков там больше нет, дальше хвост по 40–110.
Основной объём — в других 206 файлах: `AdventureCore` 21 162, `Name` 19 778,
`SpecialEffect` 7 837, `CombatSkill` 3 194. Смотреть `taiwu-ru-byfile.py`."""

new_state = u"""Создание персонажа закрыто целиком: секты, свойства, одарённость, месяцы, внешность,
подробности мира, режим бездны.

**`CombatSkill_language.txt`:** все 946 имён и все 756 описаний готовы. Остались только
`BreakStart_*` / `BreakEnd_*` — 1492 строки, 986 уникальных названий узлов прорыва
(акупунктурные точки, части тела, гексаграммы). Это мелкие подписи в сетке прорыва,
низкий приоритет.

**`SkillBook_language.txt`:** все 879 имён готовы, описаний 733 из 879.
Осталось 146 описаний настоящих трактатов — `Desc_0`–`Desc_143` плюс два хвостовых.
Остальное перенеслось автоматически: описания книг дословно совпадают с описаниями искусств.

В `ui_language.txt` осталось ~7400; крупных блоков там больше нет, дальше хвост по 40–110.
Основной объём — в других файлах: `AdventureCore` 21 162, `Name` 19 778,
`SpecialEffect` 7 837, `Weapon` 1878. Смотреть `taiwu-ru-byfile.py`."""

assert old_state in t, 'старый абзац не найден'
t = t.replace(old_state, new_state)

# убрать устаревший подраздел про остаток описаний
i = t.find(u'### Где остановились в описаниях боевых искусств')
if i != -1:
    j = t.find(u'###', i + 10)
    t = t[:i] + (t[j:] if j != -1 else u'')

with open(p, 'wb') as out:
    out.write(t.encode('utf-8'))
print('журнал приведён в порядок')
