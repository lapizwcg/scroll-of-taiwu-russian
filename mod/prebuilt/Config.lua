return {
	Title = "Русская локализация",
	Version = "0.2.0.0",
	Author = "WCG",
	Description = "Перевод игры на русский язык. Переносит языковые файлы в StreamingAssets, чтобы перевод не пропадал при обновлении игры. Язык переключается в Настройки → Язык игры. Новые тексты вступают в силу при следующем запуске.",
	FrontendPlugins = {
		[1] = "TaiwuRussian.dll",
	},
	DefaultSettings = {
		[1] = {
			SettingType = "Toggle",
			Key = "installLanguage",
			DisplayName = "Устанавливать языковые файлы",
			GroupName = nil,
			DefaultValue = true,
		},
	},
	Source = 0,
	FileId = 1,
	GameVersion = "0.84.75",
	Visibility = 0,
	SettingGroups = {
		[1] = "Default",
	},
	UpdateLogList = { },
	ChangeConfig = false,
	HasArchive = false,
	NeedRestartWhenSettingChanged = false,
	Cover = nil,
	WorkshopCover = nil,
}
