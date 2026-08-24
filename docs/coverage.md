# Покрытие русского перевода

Файл собирается скриптом `C:\Games\coverage.py` — перезапускать после каждой
крупной партии, проценты обновятся сами. Строка считается переведённой, если
в значении есть кириллица.

## Итог

| Пласт | Переведено | Всего | % |
|---|---:|---:|---:|
| Интерфейс, предметы, события (`*_language.txt`) | 74263 | 112483 | **66.0%** |
| Сюжетные диалоги (`Event\EventLanguages`) | 1065 | 55752 | **1.9%** |
| Всплывающие подсказки (`CommonTip`, 15 json) | — | — | **100%** |
| Таблицы энциклопедии (`EncyclopediaAssets`, 238 tsv, 4.3 МБ) | 0 | — | **0%** |

Не в счёт: 9843 невидимых игроку строк (заметки редактора вылазок
`Parameters.N Name/Desc` и ярлыки точек сбора `MapPickups Name_N`).

## По категориям

| Категория | Переведено | Всего | % | |
|---|---:|---:|---:|---|
| Интерфейс, подсказки и обучение | 8029 | 14920 | **53.8%** | `███████████·········` |
| Боевые искусства, эффекты и бой | 9943 | 17020 | **58.4%** | `████████████········` |
| Предметы и снаряжение | 7232 | 9341 | **77.4%** | `███████████████·····` |
| Сверчки и гу | 787 | 980 | **80.3%** | `████████████████····` |
| Персонажи, мир и карта | 27905 | 28285 | **98.7%** | `████████████████████` |
| Вылазки и события | 13823 | 19380 | **71.3%** | `██████████████······` |
| Задания и сюжетные линии | 642 | 3653 | **17.6%** | `████················` |
| Деревня, постройки и жители | 1433 | 3338 | **42.9%** | `█████████···········` |
| Вести и тайные сведения | 157 | 4770 | **3.3%** | `█···················` |
| Летопись, уведомления и наследие | 1732 | 7696 | **22.5%** | `█████···············` |
| Ремёсла, диспут и энциклопедия | 2580 | 3100 | **83.2%** | `█████████████████···` |
| Сюжетные диалоги | 1065 | 55752 | **1.9%** | `····················` |

### Интерфейс, подсказки и обучение — 53.8% (осталось 6891)

| Файл | Осталось | Всего | % |
|---|---:|---:|---:|
| `ui` | 5240 | 12716 | 59% |
| `UpdateLog` | 278 | 285 | 2% |
| `StatInfo` | 224 | 229 | 2% |
| `TutorialVideo` | 206 | 246 | 16% |
| `EventOptionTipsInfo` | 206 | 236 | 13% |
| `InteractCheckTip` | 182 | 183 | 1% |
| `LoadingTips` | 110 | 124 | 11% |
| `PredefinedLog` | 96 | 96 | 0% |
| `DevelopmentTeam` | 78 | 78 | 0% |
| `TutorialChapters` | 50 | 50 | 0% |
| `BlockButton` | 40 | 46 | 13% |
| `NewFunctionUnlock` | 37 | 56 | 34% |
| `ImplementedDlc` | 30 | 32 | 6% |
| `ExtraNameText` | 29 | 31 | 6% |
| `MapLegend` | 27 | 41 | 34% |
| `MapBlockCharCustomInfo` | 16 | 27 | 41% |
| `MapElementDisplayRuleItem` | 14 | 44 | 68% |
| `MapBlockCharCustomButton` | 10 | 10 | 0% |
| `MapElementDisplayRuleGroup` | 8 | 8 | 0% |
| `CombatConfig` | 8 | 8 | 0% |
| `CharacterMapBlockButton` | 2 | 5 | 60% |
| `SortItem` | 0 | 224 | 100% |
| `ChallengeMode` | 0 | 52 | 100% |
| `HotKeyDisplay` | 0 | 40 | 100% |
| `MainMenuButton` | 0 | 28 | 100% |
| `MainUiCustomButton` | 0 | 25 | 100% |

### Боевые искусства, эффекты и бой — 58.4% (осталось 7077)

| Файл | Осталось | Всего | % |
|---|---:|---:|---:|
| `SpecialEffect` | 2794 | 7837 | 64% |
| `CombatSkill` | 1441 | 3194 | 55% |
| `TeammateBubble` | 1141 | 1261 | 10% |
| `CombatState` | 280 | 442 | 37% |
| `SkillBreakPlateGridBonusType` | 235 | 266 | 12% |
| `AiCondition` | 232 | 254 | 9% |
| `TeammateCommand` | 227 | 413 | 45% |
| `LegendaryBookSlot` | 168 | 168 | 0% |
| `AiAction` | 122 | 134 | 9% |
| `QiArtStrategy` | 122 | 123 | 1% |
| `CombatEvaluation` | 96 | 102 | 6% |
| `AiParam` | 61 | 84 | 27% |
| `DemonSlayerTrialRestrict` | 35 | 35 | 0% |
| `DemonSlayerTrial` | 21 | 21 | 0% |
| `MixPoisonEffect` | 20 | 20 | 0% |
| `CombatScene` | 19 | 57 | 67% |
| `NeiliAllocationStatus` | 17 | 20 | 15% |
| `WeaponUnlockEffect` | 11 | 11 | 0% |
| `DemonSlayerTrialLevel` | 9 | 9 | 0% |
| `SpecialEffectDataField` | 7 | 37 | 81% |
| `BodyPart` | 7 | 14 | 50% |
| `Poison` | 5 | 18 | 72% |
| `AiNode` | 5 | 8 | 38% |
| `SkillBreakPageEffectImplement` | 2 | 2 | 0% |
| `SkillBook` | 0 | 1758 | 100% |
| `NeiliType` | 0 | 190 | 100% |
| `EquipmentEffect` | 0 | 136 | 100% |
| `SkillBreakBonusEffect` | 0 | 96 | 100% |
| `SkillBreakEffectDisplay` | 0 | 92 | 100% |
| `CombatSkillProperty` | 0 | 74 | 100% |
| `SkillBreakGridType` | 0 | 48 | 100% |
| `TrickType` | 0 | 44 | 100% |
| `CombatSkillType` | 0 | 28 | 100% |
| `SkillBreakOutlineEffect` | 0 | 10 | 100% |
| `QiDisorderEffect` | 0 | 10 | 100% |
| `CombatDifficulty` | 0 | 4 | 100% |

### Предметы и снаряжение — 77.4% (осталось 2109)

| Файл | Осталось | Всего | % |
|---|---:|---:|---:|
| `Medicine` | 617 | 1065 | 42% |
| `Accessory` | 300 | 599 | 50% |
| `MakeItemSubType` | 288 | 476 | 39% |
| `Chicken` | 189 | 191 | 1% |
| `CraftTool` | 162 | 163 | 1% |
| `MakeItemType` | 141 | 366 | 61% |
| `Music` | 122 | 141 | 13% |
| `Clothing` | 95 | 238 | 60% |
| `Carrier` | 92 | 181 | 49% |
| `TeaWine` | 71 | 72 | 1% |
| `Puppet` | 32 | 33 | 3% |
| `Weapon` | 0 | 1878 | 100% |
| `Misc` | 0 | 1355 | 100% |
| `Armor` | 0 | 1166 | 100% |
| `Material` | 0 | 1047 | 100% |
| `Food` | 0 | 354 | 100% |
| `ResourceType` | 0 | 16 | 100% |

### Сверчки и гу — 80.3% (осталось 193)

| Файл | Осталось | Всего | % |
|---|---:|---:|---:|
| `JiaoRecord` | 69 | 70 | 1% |
| `WugKing` | 32 | 32 | 0% |
| `JiaoProperty` | 26 | 33 | 21% |
| `CricketPolymorphEvent` | 23 | 244 | 91% |
| `JiaoNurturance` | 20 | 20 | 0% |
| `Luohan` | 18 | 18 | 0% |
| `Loong` | 5 | 5 | 0% |
| `CricketParts` | 0 | 399 | 100% |
| `CricketSkill` | 0 | 66 | 100% |
| `CricketAffixes` | 0 | 44 | 100% |
| `Jiao` | 0 | 40 | 100% |
| `Cricket` | 0 | 9 | 100% |

### Персонажи, мир и карта — 98.7% (осталось 380)

| Файл | Осталось | Всего | % |
|---|---:|---:|---:|
| `WorldState` | 125 | 142 | 12% |
| `OrganizationMember` | 105 | 314 | 67% |
| `AdventureRemakeBlockEffect` | 48 | 56 | 14% |
| `TwelveImmortals` | 36 | 48 | 25% |
| `AdventureTerrain` | 33 | 46 | 28% |
| `CharacterTitle` | 20 | 43 | 53% |
| `DestinyType` | 6 | 18 | 67% |
| `AdventureRemakePerformanceEffect` | 6 | 7 | 14% |
| `Organization` | 1 | 115 | 99% |
| `Name` | 0 | 19778 | 100% |
| `Character` | 0 | 2072 | 100% |
| `CharacterFeature` | 0 | 1950 | 100% |
| `NpcRandomWords` | 0 | 1289 | 100% |
| `MapBlock` | 0 | 685 | 100% |
| `CharacterPropertyDisplay` | 0 | 463 | 100% |
| `MapArea` | 0 | 422 | 100% |
| `ProtagonistFeature` | 0 | 160 | 100% |
| `CharacterTableElement` | 0 | 107 | 100% |
| `WorldCreation` | 0 | 86 | 100% |
| `SolarTerm` | 0 | 72 | 100% |
| `AvatarSkinColors` | 0 | 48 | 100% |
| `AvatarHairColors` | 0 | 48 | 100% |
| `AvatarEyeballColors` | 0 | 48 | 100% |
| `AvatarClothColors` | 0 | 48 | 100% |
| `AdventureRemakeMapBlock` | 0 | 41 | 100% |
| `BehaviorType` | 0 | 25 | 100% |
| `Month` | 0 | 24 | 100% |
| `AvatarHead` | 0 | 22 | 100% |
| `RelationDisplayType` | 0 | 19 | 100% |
| `CharacterDeathType` | 0 | 18 | 100% |
| `ConsummateLevel` | 0 | 18 | 100% |
| `MapState` | 0 | 16 | 100% |
| `CharacterTable` | 0 | 12 | 100% |
| `LandFormType` | 0 | 12 | 100% |
| `WesternRegion` | 0 | 9 | 100% |
| `WorldCreationGroup` | 0 | 4 | 100% |

### Вылазки и события — 71.3% (осталось 5557)

| Файл | Осталось | Всего | % |
|---|---:|---:|---:|
| `EventFunction` | 2302 | 2414 | 5% |
| `MonthlyEvent` | 875 | 960 | 9% |
| `MapPickups` *(+542 невидимых)* | 351 | 1533 | 77% |
| `TravelingEvent` | 329 | 332 | 1% |
| `EventArgument` | 247 | 364 | 32% |
| `ShopEvent` | 211 | 211 | 0% |
| `TaiwuBeHuntedEvent` | 210 | 225 | 7% |
| `EventActors` | 209 | 336 | 38% |
| `Adventure` | 181 | 393 | 54% |
| `CharacterAlertnessRecord` | 110 | 118 | 7% |
| `InteractionEventOption` | 103 | 141 | 27% |
| `MonthlyActions` | 85 | 85 | 0% |
| `NormalInteraction` | 84 | 84 | 0% |
| `DemandInteraction` | 64 | 64 | 0% |
| `EventValue` | 39 | 70 | 44% |
| `EnemyNest` | 30 | 30 | 0% |
| `TeaHorseCaravanEvent` | 27 | 42 | 36% |
| `Feast` | 27 | 28 | 4% |
| `EventBoolState` | 21 | 21 | 0% |
| `AdvancingMonthState` | 13 | 13 | 0% |
| `AdventureCore` *(+9301 невидимых)* | 11 | 11861 | 100% |
| `EventScriptType` | 10 | 10 | 0% |
| `TeaHorseCaravanWeather` | 10 | 10 | 0% |
| `MiniGameYuanshan` | 4 | 4 | 0% |
| `EventCommonOption` | 2 | 8 | 75% |
| `TeaHorseCaravanTerrain` | 2 | 6 | 67% |
| `AdventureType` | 0 | 17 | 100% |

### Задания и сюжетные линии — 17.6% (осталось 3011)

| Файл | Осталось | Всего | % |
|---|---:|---:|---:|
| `TaskInfo` | 2258 | 2785 | 19% |
| `CharacterMission` | 234 | 245 | 4% |
| `PlanningGoal` | 233 | 273 | 15% |
| `TaskChain` | 96 | 153 | 37% |
| `StoryScroll` | 84 | 84 | 0% |
| `MainStoryLineProgress` | 32 | 33 | 3% |
| `SectMainStory` | 24 | 30 | 20% |
| `PrioritizedActions` | 15 | 15 | 0% |
| `TaskHint` | 13 | 13 | 0% |
| `PlanningAction` | 13 | 13 | 0% |
| `ExchangeTask` | 9 | 9 | 0% |

### Деревня, постройки и жители — 42.9% (осталось 1905)

| Файл | Осталось | Всего | % |
|---|---:|---:|---:|
| `PunishmentType` | 494 | 506 | 2% |
| `BuildingScale` | 449 | 496 | 9% |
| `ProfessionSkill` | 356 | 360 | 1% |
| `Profession` | 162 | 180 | 10% |
| `MerchantType` | 105 | 112 | 6% |
| `TaiwuVillageStoragesRecord` | 64 | 86 | 26% |
| `VillagerRoleArrangement` | 60 | 64 | 6% |
| `Merchant` | 53 | 54 | 2% |
| `SettlementTreasuryRecord` | 48 | 50 | 4% |
| `VillagerRoleAutoAction` | 38 | 40 | 5% |
| `SectApprovingEffect` | 28 | 30 | 7% |
| `SettlementPrisonRecord` | 24 | 24 | 0% |
| `VillagerRoleActionRecord` | 22 | 30 | 27% |
| `VillagerRoleFormula` | 2 | 24 | 92% |
| `BuildingBlock` | 0 | 1201 | 100% |
| `VillagerRole` | 0 | 37 | 100% |
| `PersonalNeed` | 0 | 27 | 100% |
| `PunishmentSeverity` | 0 | 10 | 100% |
| `CatchThiefLevel` | 0 | 7 | 100% |

### Вести и тайные сведения — 3.3% (осталось 4613)

| Файл | Осталось | Всего | % |
|---|---:|---:|---:|
| `InformationInfo` | 2909 | 2918 | 0% |
| `SecretInformation` | 649 | 729 | 11% |
| `SecretInformationAppliedResult` | 291 | 291 | 0% |
| `SecretInformationAppliedContent` | 280 | 280 | 0% |
| `SecretInformationSpecialCondition` | 184 | 188 | 2% |
| `SecretInformationEffect` | 107 | 137 | 22% |
| `SecretInformationAppliedSelection` | 90 | 94 | 4% |
| `SecretInformationDetailedFilter` | 43 | 58 | 26% |
| `InformationType` | 32 | 38 | 16% |
| `SecretInformationAppliedRelation` | 20 | 20 | 0% |
| `SecretInformationGeneralFilter` | 8 | 10 | 20% |
| `SecretInformationParameterType` | 0 | 7 | 100% |

### Летопись, уведомления и наследие — 22.5% (осталось 5964)

| Файл | Осталось | Всего | % |
|---|---:|---:|---:|
| `LifeRecord` | 2532 | 2802 | 10% |
| `Legacy` | 1298 | 1498 | 13% |
| `InstantNotification` | 977 | 999 | 2% |
| `AchievementInfo` | 531 | 594 | 11% |
| `MonthlyNotificationSortingGroup` | 240 | 420 | 43% |
| `TaiwuLifeSummaryType` | 112 | 113 | 1% |
| `FameAction` | 93 | 93 | 0% |
| `LegacyPoint` | 91 | 101 | 10% |
| `TaiwuLifeSummaryGroup` | 86 | 113 | 24% |
| `MonthlyNotification` | 2 | 943 | 100% |
| `SamsaraPlatformRecord` | 2 | 2 | 0% |
| `BecomeEnemyType` | 0 | 10 | 100% |
| `LegacyPointType` | 0 | 8 | 100% |

### Ремёсла, диспут и энциклопедия — 83.2% (осталось 520)

| Файл | Осталось | Всего | % |
|---|---:|---:|---:|
| `DebateStrategy` | 215 | 222 | 3% |
| `LifeSkillCombatTalk` | 80 | 84 | 5% |
| `DebateRecord` | 69 | 69 | 0% |
| `LifeSkillCombatEffect` | 51 | 54 | 6% |
| `DebateComment` | 40 | 40 | 0% |
| `LifeSkill` | 19 | 288 | 93% |
| `DebateStrategyTarget` | 18 | 18 | 0% |
| `DebateNodeEffect` | 15 | 15 | 0% |
| `DebateEvaluation` | 10 | 10 | 0% |
| `GuidingChapterClass` | 3 | 11 | 73% |
| `GuidingChapter` | 0 | 2177 | 100% |
| `ReadingStrategy` | 0 | 57 | 100% |
| `LifeSkillType` | 0 | 55 | 100% |

### Сюжетные диалоги — 1.9% (осталось 54687 реплик)

Уникальные реплики пакета. Одна и та же реплика в разных пакетах считается
отдельно, поэтому итог по папке больше числа уникальных строк (около 50 тыс.).
Пакеты, где не переведено ни строки, свёрнуты в
последнюю строку таблицы.

| Пакет | Осталось | Всего | % |
|---|---:|---:|---:|
| `Taiwu_EventPackage_MainStory_DeepValley` | 72 | 170 | 58% |
| `Taiwu_EventPackage_MainStory_FirstTaiWu` | 2 | 338 | 99% |
| `Taiwu_EventPackage_MainStory_SmallVilliage` | 1 | 420 | 100% |
| `Taiwu_EventPackage_DeepValleyExit` | 0 | 47 | 100% |
| `Taiwu_EventPackage_NewMainStory_DeepValley` | 0 | 165 | 100% |
| `Taiwu_EventPackage_SectMainStoryWudang` | 998 | 998 | 0% |
| `Taiwu_EventPackage_SectMainStoryShixiang` | 910 | 910 | 0% |
| `Taiwu_EventPackage_SectMainStoryEmei` | 883 | 883 | 0% |
| `Taiwu_EventPackage_SectMainStoryRanshanExtra` | 870 | 870 | 0% |
| `Taiwu_EventPackage_WorldKungfuMeeting` | 865 | 865 | 0% |
| `Taiwu_EventPackage_SectMainStoryWuxian` | 746 | 746 | 0% |
| `Taiwu_EventPackage_SectMainStoryYuanshanEpitasis` | 718 | 718 | 0% |
| `Taiwu_EventPackage_SectMainStoryXuehou` | 690 | 690 | 0% |
| `Taiwu_EventPackage_MainStory_SwordGraveProgress` | 689 | 689 | 0% |
| `Taiwu_EventPackage_SectMainStoryRanshan` | 637 | 637 | 0% |
| `Taiwu_EventPackage_SectMainStoryShaolin` | 579 | 579 | 0% |
| `Taiwu_EventPackage_SectMainStoryFulong2` | 578 | 578 | 0% |
| `Taiwu_EventPackage_SameBlockNpcMonthAdvanceEvents` | 550 | 550 | 0% |
| `Taiwu_EventPackage_SectMainStoryKongsang` | 537 | 537 | 0% |
| `Taiwu_EventPackage_SectMainStoryXuannv_Part3` | 514 | 514 | 0% |
| `Taiwu_EventPackage_SectMainStoryJingang` | 506 | 506 | 0% |
| `Taiwu_EventPackage_CharacterInteraction_LoveDlC_UnmarriedDate` | 501 | 501 | 0% |
| `Taiwu_EventPackage_Story_Jouenry` | 499 | 499 | 0% |
| `Taiwu_EventPackage_SectMainStoryJingang2` | 470 | 470 | 0% |
| `Taiwu_EventPackage_SectCombatMatch` | 427 | 427 | 0% |
| `Taiwu_EventPackage_MainStory_VisitSect` | 393 | 393 | 0% |
| `Taiwu_EventPackage_SectStoryZhujianEpitasis` | 385 | 385 | 0% |
| `Taiwu_EventPackage_LoongDLC` | 380 | 380 | 0% |
| `Taiwu_EventPackage_CharacterInteraction_Main` | 365 | 365 | 0% |
| `Taiwu_EventPackage_NewMainStory_PreIronPlate` | 356 | 356 | 0% |
| *не начато: 410 пакетов* | 39566 | 39566 | 0% |

