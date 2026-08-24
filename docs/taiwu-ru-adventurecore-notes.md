# AdventureCore_language.txt — журнал параллельного сеанса

Сеанс работает **только** с `AdventureCore_language.txt`. Другие файлы не трогались.
Дата среза: 2026-08-17.

## Где мы сейчас

| Показатель | В начале | Сейчас |
|---|---|---|
| Непереведённых пар в файле | 20 109 | **9 846** |
| Из них `Parameters` (не переводим) | 8 790 | 8 741 |
| **Реально осталось к переводу** | 11 319 | **1 101** |

Готовность файла по «живому» тексту — **90 %**.
По проекту: `taiwu-ru-status.py` — 49.8 %, «структура всех файлов цела».
`fixquotes.py AdventureCore_language.txt --apply` — 0 находок.

### Закрыто целиком

| Раздел | Было | Осталось |
|---|---|---|
| `Adv.N Name` / `Desc` / `DescTarget` / `DescReward` | 658 | 3 (заглушки `XXXXXXXX` в оригинале) |
| `AdvElement.N Name` / `Desc` | 6 194 | 8 (служебный мусор) |
| `Adv.N Actions.N Name` / `Desc` | 1 924 | 0 |
| `MajorEvent.N Name` / `Desc` / `Nodes.N Name` / `Nodes.N Desc` | 1 034 | 0 |

Служебный мусор, который переводить нечего: `BWZQ_HIDDEN`, `ycys1`, `ycys2`,
`0`, `1`, `222`, `adventure_element_character_meta`.

### ТОЧКА ВОЗОБНОВЛЕНИЯ

Остался **один раздел: `Adv.N CustomTexts.N Text` — 1 091 строка.**
Это реплики в облачках и подсказки на клетках вылазок.

Работа идёт частотным словарём (см. ниже). Уже пройдены две порции — 362 и 140
ключей. Следующая порция начинается с самых частых из оставшихся:

```
"Feast hasn't started yet..."
'Waiter, one "Poultry Dish"...'
'There seems to be someone ahead...'
'"Absolutely stunning! I can't look away!"'
```

Готовые словари лежат в scratchpad: `map10.json`, `map11.json` — продолжать
в том же формате `{"английская строка": "перевод"}` и раздавать через `bulk.py`.

## Приём, на котором держится скорость

В файле очень много **дословных повторов**: одна английская строка встречается
до 50 раз под разными ключами. Порядок такой:

1. Считаем частоту уникальных английских значений внутри своей группы ключей.
2. Пишем словарь `{"английская строка": "перевод"}`.
3. `bulk.py` раздаёт его всем непереведённым ключам с **дословным** совпадением
   и печатает отчёт: сколько попало и какие строки словаря не нашлись.

Партии выходили по 1150, 757, 485, 436, 362 строки за раз. Это не `xfer.py`:
словарь пишется вручную и только по своему файлу, чужие партии не затрагиваются.

## Три ловушки, на которые напоролся

**1. Один и тот же персонаж в двух файлах.** `Character_language.txt` уже
переведён: `Wicked Beggar` → «Злой нищий». Я же в описаниях писал «злобный
попрошайка» — имя элемента и его описание в одном экране расходились.
Исправлено скопом, 19 строк (`fixbeg.py` в scratchpad).
Мораль: **прежде чем переводить имя существа или предмета, гнать `look.py`.**

Оттуда же взяты 9 ступеней прислужников Сяншу: Wicked · Evil · Sinister ·
Demonic · Calamitous · Vengeful · Faceless · Reaper · Soultaker →
Злой · Зло · Зловещий · Демонический · Гибельный · Мстительный · Безликий ·
Жнец · Похититель душ.

**2. Английский врёт про 月.** В вылазке «Дали, Юньнань» четыре элемента
风花雪月: Wind, Flower, Snow и… **Month**. Это луна, а не месяц — соседнее
описание прямо говорит «wind, flower, snow, and moon». Переведено как «Луна».

**3. Soulcatcher ≠ Soultaker.** Поправлено по твоей подсказке: где было
«Ловец душ» для Soultaker, теперь «Похититель душ». `Soulcatcher Banner`
в моём файле встречается **только** под ключом `Adv.294710198 Parameters.15 Name`,
то есть это заметка редактора — по правилу не переводим. Если он всплывёт
где-то в игровом тексте, ставим «Стяг ловца душ».

## Что поправил по твоей сводке терминов

- `Refining Materials` → «припасы для **очистки**» (`Adv.268182972 DescReward`).
  Единственное вхождение в файле.
- `Durability`, `Toughness`, `Phy. Penetration/Defense`, `Inner Breath Chaos`,
  `Attack Interval` — в моём файле встречаются **только под `Parameters`**,
  то есть в непереводимой части. Править нечего.
- 24 сельскохозяйственных срока сверены с закрытым `SolarTerm_language.txt` —
  совпали все, расхождений нет.

## Новые термины — на сведение с глоссарием

### Тайные трактаты (`Secret Tome`)

| Оригинал | Перевод |
|---|---|
| Collection of Fleeting Flare | Собрание мимолётного цвета |
| Nameless Swordcraft | Безымянное искусство меча |
| Record of Lethal Mara | Записи смертоносной мары |
| Mind's Eye | Око разума |
| Thousand Method Compendium | Свод тысячи приёмов |
| Sky Divider | Рассекающий небо |
| Novem-resembler | Девятиподобный |
| Book of the Primordial | Книга изначального |
| Celestial Melodist | Небесный музыкант |
| Tome of Shadowcraft Marvel | Трактат о дивном искусстве теней |
| Classics of the Unfettered | Канон беспечного странствия |
| Chant of Wordless Mind | Напев бессловесного сердца |
| Volatile Loong Depiction | Изображение изменчивого луна |

### Имена и существа

| Оригинал | Перевод |
|---|---|
| Xiangshu / Xiangshu Incarnation | Сяншу / воплощение Сяншу |
| Dayue Yaochang · Yi Yihou · Yi Xiang · Jiu Han · Jin Huang'er · Wei Qi · Monu | Даюэ Яочан · И Ихоу · И Сян · Цзю Хань · Цзинь Хуанъэр · Вэй Ци · Мону |
| Blood Maple · Spellwright | Кровавый клён · Заклинатель |
| Tainted (даос) · Huanxin · Immortal Xu · Ruler Mara | Осквернённый · Хуаньсинь · Бессмертный Сюй · Владыка Мара |
| Ou Yezi · Pangu · Fuxi · Nüwa · King Pan | Оу Ецзы · Паньгу · Фуси · Нюйва · царь Пань |
| Situ Huanyue · A'niu · Susu · Xu Xiaomao · Zi Wuxiao · Guo Yan · Jixi · Shi Houjiu | Ситу Хуаньюэ · А-ню · Сусу · Сюй Сяомао · Цзы Усяо · Го Янь · Цзиси · Ши Хоуцзю |
| Burnt Dust · White Ape | Жжёный прах · Белая обезьяна |
| Outlander Cult · Foreign Freak | Культ иноверцев · Чужеземный изувер |
| Toxin Wielder · Heretic · Unaging Elder | Владеющий ядом · Еретик · Нестареющий старейшина |
| Jade Belle · Dashing Beau · Paragon | Нефритовая красавица · Щёголь · первая красавица |
| enchantress / enchanter | чаровница / чаровник |
| Book Spirit / Book Soul | дух книги / душа книги |
| Nine-Headed Serpent · Starry Centipede · Chasm/Abyssal Wyrm · Ink Jiao | Девятиглавый змей · Звёздная сколопендра · змей бездны · тушевый цзяо |
| Mountain Fire Turtle · Lord of Black Mountain | горная огненная черепаха · Владыка Чёрной горы |
| Great Vajra Dharma King · Tomb Immortal | Великий царь Дхармы Ваджры · Бессмертный из гробницы |

### Места

| Оригинал | Перевод |
|---|---|
| Bashu · Jingbei · Jingnan · Jingji · Jiangbei · Jiangnan · Guangnan · Guangdong · Huainan · Liaodong · Shandong · Shanxi · Fujian | Башу · Цзинбэй · Цзиннань · Цзинцзи · Цзянбэй · Цзяннань · Гуаннань · Гуандун · Хуайнань · Ляодун · Шаньдун · Шаньси · Фуцзянь |
| Mass Grave · Enthralling Trap · Pandemonium | Братская могила · Обольстительная ловушка · Обитель демонов |
| Villains' Valley · House of Eccentrics · Hall of Xiake | Долина злодеев · Дом чудаков · Зал странствующих воинов |
| Killing Field · Land of Death · Demise Abyss | Поле смерти · Мёртвая земля · Бездна погибели |
| Ten Thousand Buddhas Cave · Library Cave · Scripture Vault | Пещера десяти тысяч будд · Пещера сутр · Хранилище сутр |
| Jinding Temple · Cave of Reincarnation · Qinglang Pavilion | храм Золотой вершины · Пещера перерождений · Павильон Цинлан |
| Egarim (зеркало на Пике Нефритовой Девы) | Эгарим |
| Bridge of Detachment · Heishui | Мост отрешения · Хэйшуй |

### Вылазки, собрания, обряды

| Оригинал | Перевод |
|---|---|
| Soaring Escape (私奔) | Побег на крыльях |
| Matrimonial Rites · Bowing Ceremony · Intimate | свадебный обряд · обряд поклонов · близкий |
| Betrothal Contest | состязание за руку |
| Sect Tournament · Major Contest | турнир секты · большое состязание |
| Martial World Tournament · Chief of Martial World | Турнир вольного света · глава вольного света |
| Summer Martial Contest · Winter Debate | Летнее ратное состязание · Зимний диспут |
| Manor / Tavern / Family Tea Gathering | чайное собрание в усадьбе / в трактире / семейное |
| Small Marketplace · Topic Week · Honored Guest | Малый торг · Неделя бесед · почётный гость |
| Panwang Festival · Drum Festival · Starry Festival | Праздник царя Паня · Барабанный праздник · Звёздный праздник |
| Contemplation Arc / Torment Arc | Часть раздумий / Часть мучений |
| Divine Fire Recollection Story | Воспоминание божественного огня |
| Demon-Sealing Light | Свет, запирающий демонов |

Жетоны товариществ: Book Tickets · Merchant Tickets · Iron Tokens · Iron Orders ·
Herb Notes · Ancient Coins · Luban Rulers → книжные жетоны · купеческие жетоны ·
железные жетоны · железные грамоты · травяные грамоты · древние монеты ·
линейки Лу Баня.

### Механика и предметы

| Оригинал | Перевод |
|---|---|
| Trait · Combat Efficiency · Favorability | особенность · боевая выучка · расположение |
| Relic · Concoction · Medicine & Poison Reagents | реликвия · снадобье · лекарские и ядовитые составы |
| Loong Spittle · Fragmented Texts | слюна луна · обрывки текста |
| Residual Wood / Water / Fire / Earth / Metal | Остаточное дерево / вода / огонь / земля / металл |
| Demonic Tower · Hellstone | демоническая башня · адский камень |
| Soul-Guiding Lamp · Ever-Burning Lamp Stand | душеводный светильник · неугасимый светильник |
| Five-Spirit Seal Stone · Four-Beast Suppression Stone | Камень печати пяти духов · Камень, усмиряющий четырёх зверей |
| Life-/Earth-/Heaven-Soul Lamp | светильник души жизни / земли / неба |
| Wandering Loong Force · Great Void | сила блуждающего луна · Великая пустота |
| tangyuan · Tanghulu · qingtuan · Kumis | танъюань · танхулу · цинтуань · кумыс |

Мечевые печати (`… Sword Seal`): лёгкого · твёрдого · гибкого · тяжёлого ·
короткого · деревянного · нефритового меча.

Восемь врат цимэнь дуньцзя: Rest · Life · Harm · Obstruction · Scenery · Death ·
Fright · Opening → врата покоя · жизни · вреда · преграды · вида · смерти ·
испуга · открытия. Дворцы — Кань · Кунь · Чжэнь · Сюнь · средоточие · Цянь ·
Дуй · Гэнь · Ли.

Пять нот: гун · шан · цзюэ · чжи · юй.
Четыре символа: Azure Loong · White Tiger · Vermilion Bird · Black Tortoise →
Лазурный лун · Белый тигр · Красная птица · Чёрная черепаха.

Тестовые вылазки `Drill-NNNNN` → `Проба-NNNNN`, `Demo`/`Deo` → `Демо`,
`Acceptance Element N` → `Элемент приёмки N`.

## Как работает этот сеанс

1. `python C:\Games\listw.py AdventureCore_language.txt` — свежий остаток в `listw.txt`.
2. `pick.py <регексп ключа> <смещение> <сколько>` — выборка (scratchpad).
3. `look.py <подстрока EN>` — ищет термин по **всем** файлам, печатает EN → RU
   и помечает непереведённое. Гонять до того, как придумывать свой вариант.
4. `bulk.py <словарь.json> <выход.json> <регексп ключа>` — раздача по дословным повторам.
5. Партия в JSON → `powershell C:\Games\apply-ru.ps1 -Batch <файл>`.
6. После крупной порции — `python C:\Games\fixquotes.py AdventureCore_language.txt --apply`
   (обязательно с именем файла).

`xfer.py` этот сеанс не запускает.

## Известная заноза: дубликат ключа `0`

В файле два ключа `0` подряд: `Blocking the wedding party` и `Blocking the groom...`.
`apply-ru.ps1` патчит **только первое вхождение** ключа, поэтому вторую строку
через скрипт не достать. Обе оставлены непереведёнными.
