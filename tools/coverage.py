# -*- coding: utf-8 -*-
"""Покрытие перевода по категориям. Пишет C:\\Games\\taiwu-ru-coverage.md.

    set PYTHONIOENCODING=utf-8
    python C:\\Games\\coverage.py

Считает три пласта:
  1. StreamingAssets\\Language_RU\\*_language.txt   — интерфейс, предметы, события
  2. Event\\EventLanguages\\*_Language_RU.txt        — сюжетные диалоги
  3. Language_RU\\CommonTip\\*.json, EncyclopediaAssets\\*.tsv — отдельным итогом

Строка считается переведённой, если в значении есть кириллица; непереведённой —
если после снятия разметки остаются латинские буквы. Пустые значения, числа и
голая разметка в счёт не идут.
"""
import io, os, re, sys, collections

GAME = r"C:\Games\The Scroll of Taiwu"
RU = os.path.join(GAME, r"The Scroll of Taiwu_Data\StreamingAssets\Language_RU")
EN = os.path.join(GAME, r"The Scroll of Taiwu_Data\StreamingAssets\Language_EN")
EVR = os.path.join(GAME, r"Event\EventLanguages")
EVBAK = r"C:\Games\taiwu-ru-backup\EventLanguages_EN_original"
OUT = r"C:\Games\taiwu-ru-coverage.md"

CYR = re.compile(u"[\u0400-\u04FF]")
LAT = re.compile(u"[A-Za-z]")
TAG = re.compile(u"<[^<>]*>")
PH = re.compile(u"[{]\\d+[}]")
ESC = re.compile(u"[\\\\][nv]")
NUM = re.compile(u"\\d+")

# Ключи, которых игрок не видит: заметки редактора вылазок и ярлыки точек сбора.
SKIP = {
    "AdventureCore_language.txt": re.compile(u" Parameters[.]\\d+ (Name|Desc)$"),
    "MapPickups_language.txt": re.compile(u"^Name_\\d+$"),
}

CATS = [
 (u"Интерфейс, подсказки и обучение", [
    "ui", "InteractCheckTip", "LoadingTips", "HotKeyDisplay", "MainMenuButton",
    "MainUiCustomButton", "BlockButton", "SortItem", "StatInfo", "TutorialVideo",
    "TutorialChapters", "NewFunctionUnlock", "UpdateLog", "DevelopmentTeam",
    "ImplementedDlc", "MapLegend", "MapElementDisplayRuleItem",
    "MapElementDisplayRuleGroup", "CharacterMapBlockButton",
    "MapBlockCharCustomButton", "MapBlockCharCustomInfo", "ExtraNameText",
    "PredefinedLog", "EventOptionTipsInfo", "ChallengeMode", "CombatConfig",
 ]),
 (u"Боевые искусства, эффекты и бой", [
    "SpecialEffect", "SpecialEffectDataField", "CombatSkill", "CombatSkillType",
    "CombatSkillProperty", "SkillBook", "SkillBreakBonusEffect",
    "SkillBreakEffectDisplay", "SkillBreakGridType", "SkillBreakOutlineEffect",
    "SkillBreakPageEffectImplement", "SkillBreakPlateGridBonusType", "TrickType",
    "QiArtStrategy", "QiDisorderEffect", "NeiliType", "NeiliAllocationStatus",
    "WeaponUnlockEffect", "EquipmentEffect", "CombatState", "CombatScene",
    "CombatEvaluation", "CombatDifficulty", "TeammateCommand", "TeammateBubble",
    "AiCondition", "AiAction", "AiParam", "AiNode", "BodyPart", "Poison",
    "MixPoisonEffect", "LegendaryBookSlot", "DemonSlayerTrial",
    "DemonSlayerTrialLevel", "DemonSlayerTrialRestrict",
 ]),
 (u"Предметы и снаряжение", [
    "Weapon", "Armor", "Clothing", "Accessory", "Medicine", "Material", "Food",
    "TeaWine", "Misc", "CraftTool", "Carrier", "Puppet", "MakeItemType",
    "MakeItemSubType", "ResourceType", "Chicken", "Music",
 ]),
 (u"Сверчки и гу", [
    "Cricket", "CricketParts", "CricketSkill", "CricketAffixes",
    "CricketPolymorphEvent", "Jiao", "JiaoProperty", "JiaoRecord",
    "JiaoNurturance", "WugKing", "Loong", "Luohan",
 ]),
 (u"Персонажи, мир и карта", [
    "Name", "Character", "CharacterFeature", "CharacterPropertyDisplay",
    "CharacterTitle", "CharacterTable", "CharacterTableElement",
    "CharacterDeathType", "ProtagonistFeature", "Organization",
    "OrganizationMember", "MapArea", "MapBlock", "MapState", "WorldCreation",
    "WorldCreationGroup", "WorldState", "LandFormType", "Month", "SolarTerm",
    "DestinyType", "ConsummateLevel", "BehaviorType", "RelationDisplayType",
    "AvatarHead", "AvatarSkinColors", "AvatarHairColors", "AvatarEyeballColors",
    "AvatarClothColors", "WesternRegion", "TwelveImmortals", "NpcRandomWords",
    "AdventureTerrain", "AdventureRemakeMapBlock", "AdventureRemakeBlockEffect",
    "AdventureRemakePerformanceEffect",
 ]),
 (u"Вылазки и события", [
    "AdventureCore", "Adventure", "AdventureType", "EventFunction",
    "EventArgument", "EventActors", "EventValue", "EventCommonOption",
    "EventBoolState", "EventScriptType", "MapPickups", "TravelingEvent",
    "TaiwuBeHuntedEvent", "MonthlyEvent", "ShopEvent", "Feast",
    "TeaHorseCaravanEvent", "TeaHorseCaravanWeather", "TeaHorseCaravanTerrain",
    "EnemyNest", "InteractionEventOption", "NormalInteraction",
    "DemandInteraction", "MiniGameYuanshan", "MonthlyActions",
    "AdvancingMonthState", "CharacterAlertnessRecord",
 ]),
 (u"Задания и сюжетные линии", [
    "TaskInfo", "TaskChain", "TaskHint", "CharacterMission",
    "MainStoryLineProgress", "SectMainStory", "StoryScroll", "ExchangeTask",
    "PlanningGoal", "PlanningAction", "PrioritizedActions",
 ]),
 (u"Деревня, постройки и жители", [
    "BuildingBlock", "BuildingScale", "VillagerRole", "VillagerRoleArrangement",
    "VillagerRoleAutoAction", "VillagerRoleActionRecord", "VillagerRoleFormula",
    "Profession", "ProfessionSkill", "PersonalNeed", "SettlementTreasuryRecord",
    "SettlementPrisonRecord", "TaiwuVillageStoragesRecord", "MerchantType",
    "Merchant", "PunishmentType", "PunishmentSeverity", "CatchThiefLevel",
    "SectApprovingEffect",
 ]),
 (u"Вести и тайные сведения", [
    "InformationInfo", "InformationType", "SecretInformation",
    "SecretInformationAppliedContent", "SecretInformationAppliedResult",
    "SecretInformationAppliedSelection", "SecretInformationAppliedRelation",
    "SecretInformationDetailedFilter", "SecretInformationGeneralFilter",
    "SecretInformationEffect", "SecretInformationParameterType",
    "SecretInformationSpecialCondition",
 ]),
 (u"Летопись, уведомления и наследие", [
    "LifeRecord", "Legacy", "LegacyPoint", "LegacyPointType",
    "TaiwuLifeSummaryGroup", "TaiwuLifeSummaryType", "AchievementInfo",
    "InstantNotification", "MonthlyNotification",
    "MonthlyNotificationSortingGroup", "FameAction", "BecomeEnemyType",
    "SamsaraPlatformRecord",
 ]),
 (u"Ремёсла, диспут и энциклопедия", [
    "LifeSkill", "LifeSkillType", "LifeSkillCombatTalk", "LifeSkillCombatEffect",
    "DebateStrategy", "DebateStrategyTarget", "DebateRecord", "DebateComment",
    "DebateEvaluation", "DebateNodeEffect", "ReadingStrategy", "GuidingChapter",
    "GuidingChapterClass",
 ]),
]


def strip_markup(v):
    return ESC.sub(u" ", PH.sub(u" ", TAG.sub(u" ", v)))


def scan_file(path, name):
    skip = SKIP.get(name)
    lines = io.open(path, encoding="utf-8").read().split(u"\n")
    done = todo = hidden = 0
    for i in range(0, len(lines) - 1, 2):
        k, v = lines[i], lines[i + 1]
        cyr = bool(CYR.search(v))
        lat = bool(LAT.search(strip_markup(v)))
        if not cyr and not lat:
            continue
        if skip and skip.search(k):
            hidden += 1
            continue
        if cyr:
            done += 1
        else:
            todo += 1
    return done, todo, hidden


def bar(pct, width=20):
    n = int(round(pct / 100.0 * width))
    return u"█" * n + u"·" * (width - n)


def pct(done, total):
    return 100.0 * done / total if total else 100.0


# ---- пласт 1: *_language.txt ------------------------------------------------
stat = {}
for fn in sorted(os.listdir(RU)):
    if fn.endswith(".txt"):
        stat[fn] = scan_file(os.path.join(RU, fn), fn)

known = set()
cats = []
for title, files in CATS:
    rows = []
    for base in files:
        fn = base + "_language.txt"
        known.add(fn)
        if fn in stat:
            d, t, h = stat[fn]
            if d + t:
                rows.append((t, d, h, fn))
    rows.sort(key=lambda r: (-r[0], -r[1]))
    cats.append((title, rows))

other = [(t, d, h, fn) for fn, (d, t, h) in stat.items()
         if fn not in known and d + t]
if other:
    other.sort(key=lambda r: -r[0])
    cats.append((u"Прочее (не разнесено по категориям)", other))

# ---- пласт 2: сюжетные диалоги ---------------------------------------------
LINE = re.compile(u"^\\s*-- (?:EventContent|Option_\\d+) : (.*)$")


def ev_lines(path):
    out = []
    for ln in io.open(path, encoding="utf-8", errors="replace"):
        m = LINE.match(ln.rstrip(u"\r\n"))
        if m and m.group(1).strip() and m.group(1).strip() != u"nan":
            out.append(m.group(1))
    return out


ev_rows = []
if os.path.isdir(EVBAK):
    for fn in sorted(os.listdir(EVBAK)):
        if not fn.endswith(u"_Language_EN.txt"):
            continue
        pkg = fn[:-len(u"_Language_EN.txt")]
        en = set(x for x in ev_lines(os.path.join(EVBAK, fn))
                 if LAT.search(strip_markup(x)))
        rupath = os.path.join(EVR, pkg + u"_Language_RU.txt")
        done = 0
        if os.path.exists(rupath):
            ru = set(ev_lines(rupath))
            done = len([x for x in ru if CYR.search(x)])
            if done > len(en):
                done = len(en)
        if en:
            ev_rows.append((len(en) - done, done, len(en), pkg))
ev_rows.sort(key=lambda r: -r[0])

# ---- пласт 3: прочие форматы -----------------------------------------------
def count_files(path, ext):
    if not os.path.isdir(path):
        return 0, 0
    n = s = 0
    for root, _, fs in os.walk(path):
        for f in fs:
            if f.lower().endswith(ext):
                n += 1
                s += os.path.getsize(os.path.join(root, f))
    return n, s


tip_n, tip_s = count_files(os.path.join(RU, "CommonTip"), ".json")
enc_n, enc_s = count_files(os.path.join(RU, "EncyclopediaAssets"), ".tsv")

# ---- отчёт ------------------------------------------------------------------
o = io.StringIO()
w = o.write

tot_d = sum(r[1] for c in cats for r in c[1])
tot_t = sum(r[0] for c in cats for r in c[1])
tot_h = sum(r[2] for c in cats for r in c[1])
ev_d = sum(r[1] for r in ev_rows)
ev_all = sum(r[2] for r in ev_rows)

w(u"# Покрытие русского перевода\n\n")
w(u"Файл собирается скриптом `C:\\Games\\coverage.py` — перезапускать после каждой\n"
  u"крупной партии, проценты обновятся сами. Строка считается переведённой, если\n"
  u"в значении есть кириллица.\n\n")
w(u"## Итог\n\n")
w(u"| Пласт | Переведено | Всего | % |\n|---|---:|---:|---:|\n")
w(u"| Интерфейс, предметы, события (`*_language.txt`) | %d | %d | **%.1f%%** |\n"
  % (tot_d, tot_d + tot_t, pct(tot_d, tot_d + tot_t)))
w(u"| Сюжетные диалоги (`Event\\EventLanguages`) | %d | %d | **%.1f%%** |\n"
  % (ev_d, ev_all, pct(ev_d, ev_all)))
w(u"| Всплывающие подсказки (`CommonTip`, %d json) | — | — | **100%%** |\n" % tip_n)
w(u"| Таблицы энциклопедии (`EncyclopediaAssets`, %d tsv, %.1f МБ) | 0 | — | **0%%** |\n"
  % (enc_n, enc_s / 1048576.0))
w(u"\nНе в счёт: %d невидимых игроку строк (заметки редактора вылазок\n"
  u"`Parameters.N Name/Desc` и ярлыки точек сбора `MapPickups Name_N`).\n\n" % tot_h)

w(u"## По категориям\n\n")
w(u"| Категория | Переведено | Всего | % | |\n|---|---:|---:|---:|---|\n")
for title, rows in cats:
    d = sum(r[1] for r in rows)
    t = sum(r[0] for r in rows)
    w(u"| %s | %d | %d | **%.1f%%** | `%s` |\n"
      % (title, d, d + t, pct(d, d + t), bar(pct(d, d + t))))
d = ev_d
w(u"| Сюжетные диалоги | %d | %d | **%.1f%%** | `%s` |\n"
  % (ev_d, ev_all, pct(ev_d, ev_all), bar(pct(ev_d, ev_all))))
w(u"\n")

for title, rows in cats:
    d = sum(r[1] for r in rows)
    t = sum(r[0] for r in rows)
    w(u"### %s — %.1f%% (осталось %d)\n\n" % (title, pct(d, d + t), t))
    w(u"| Файл | Осталось | Всего | % |\n|---|---:|---:|---:|\n")
    for t_, d_, h_, fn in rows:
        mark = u" *(+%d невидимых)*" % h_ if h_ else u""
        w(u"| `%s`%s | %d | %d | %.0f%% |\n"
          % (fn.replace(u"_language.txt", u""), mark, t_, d_ + t_, pct(d_, d_ + t_)))
    w(u"\n")

w(u"### Сюжетные диалоги — %.1f%% (осталось %d реплик)\n\n"
  % (pct(ev_d, ev_all), ev_all - ev_d))
w(u"Уникальные реплики пакета. Одна и та же реплика в разных пакетах считается\n"
  u"отдельно, поэтому итог по папке больше числа уникальных строк (около 50 тыс.).\n"
  u"Пакеты, где не переведено ни строки, свёрнуты в\n"
  u"последнюю строку таблицы.\n\n")
w(u"| Пакет | Осталось | Всего | % |\n|---|---:|---:|---:|\n")
untouched_all = [r for r in ev_rows if r[1] == 0]
touched = [r for r in ev_rows if r[1] > 0]
untouched_all.sort(key=lambda r: -r[2])
big, untouched = untouched_all[:25], untouched_all[25:]
for t_, d_, all_, pkg in touched + big:
    w(u"| `%s` | %d | %d | %.0f%% |\n" % (pkg, t_, all_, pct(d_, all_)))
if untouched:
    w(u"| *не начато: %d пакетов* | %d | %d | 0%% |\n"
      % (len(untouched), sum(r[0] for r in untouched),
         sum(r[2] for r in untouched)))
w(u"\n")

io.open(OUT, "w", encoding="utf-8", newline="\n").write(o.getvalue())
sys.stdout.write(u"записано %s\n" % OUT)
sys.stdout.write(u"тексты: %d/%d (%.1f%%), диалоги: %d/%d (%.1f%%)\n"
                 % (tot_d, tot_d + tot_t, pct(tot_d, tot_d + tot_t),
                    ev_d, ev_all, pct(ev_d, ev_all)))
if other:
    sys.stdout.write(u"не разнесено по категориям: %d файлов\n" % len(other))
