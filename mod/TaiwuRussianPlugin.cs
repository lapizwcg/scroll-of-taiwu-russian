using System;
using System.Globalization;
using System.IO;
using System.Reflection;
using System.Text.RegularExpressions;
using TaiwuModdingLib.Core.Plugin;
using UnityEngine;

namespace TaiwuRussian
{
    /// <summary>
    /// Русская локализация The Scroll of Taiwu.
    ///
    /// Версия 0.2 делает ровно одно: переносит языковые файлы из папки мода
    /// в StreamingAssets. Обновление игры затирает StreamingAssets, а папку
    /// Mod не трогает — так перевод переживает обновления.
    ///
    /// Подгонки размера шрифта здесь намеренно нет. В версии 0.1 она вызывала
    /// Resources.FindObjectsOfTypeAll по таймеру, и это подвешивало запуск.
    /// Вернём отдельным шагом, когда будет видно, что мод грузится штатно.
    /// </summary>
    /// <remarks>
    /// Атрибут PluginConfig обязателен: его наличие проверяет конструктор
    /// TaiwuRemakePlugin, и без него загрузка падает ещё до Initialize(),
    /// а игра после этого зависает на экране загрузки.
    /// </remarks>
    [PluginConfig("TaiwuRussian", "WCG", "0.2.0.0")]
    public class TaiwuRussianPlugin : TaiwuRemakePlugin
    {
        private const string LanguageFolder = "Language_RU";

        /// <summary>
        /// Ничто здесь не должно бросать исключение наружу: если плагин не
        /// построится, игра не завершит загрузку главного меню.
        /// </summary>
        public override void Initialize()
        {
            try
            {
                Log("запуск, версия 0.2");

                string modDir = ResolveModDir();
                if (modDir == null)
                {
                    Log("не удалось определить папку мода — установка пропущена");
                    return;
                }
                Log("папка мода: " + modDir);

                if (!ReadInstallSetting(modDir))
                {
                    Log("установка языковых файлов выключена в настройках");
                    return;
                }

                InstallLanguageFiles(modDir);
            }
            catch (Exception e)
            {
                Log("сбой при загрузке: " + e);
            }
        }

        public override void Dispose()
        {
            try
            {
                Log("выгружен");
            }
            catch
            {
                // выгрузка не должна мешать игре закрываться
            }
        }

        public override void OnModSettingUpdate()
        {
            Log("настройки изменены; языковые файлы обновятся при следующем запуске");
        }

        /// <summary>
        /// Копирует *.txt из Mod/TaiwuRussian/Language_RU в
        /// StreamingAssets/Language_RU, трогая только устаревшие файлы.
        /// </summary>
        private static void InstallLanguageFiles(string modDir)
        {
            string src = Path.Combine(modDir, LanguageFolder);
            if (!Directory.Exists(src))
            {
                Log("в моде нет папки " + LanguageFolder + " — установка пропущена");
                return;
            }

            string dst = Path.Combine(Application.streamingAssetsPath, LanguageFolder);
            Directory.CreateDirectory(dst);

            string[] files = Directory.GetFiles(src, "*.txt");
            int copied = 0;
            int failed = 0;

            foreach (string file in files)
            {
                string target = Path.Combine(dst, Path.GetFileName(file));
                try
                {
                    if (File.Exists(target) &&
                        File.GetLastWriteTimeUtc(file) <= File.GetLastWriteTimeUtc(target))
                        continue;

                    File.Copy(file, target, true);
                    copied++;
                }
                catch (Exception e)
                {
                    failed++;
                    if (failed <= 3)
                        Log("не скопирован " + Path.GetFileName(file) + ": " + e.Message);
                }
            }

            Log(string.Format(CultureInfo.InvariantCulture,
                "языковых файлов в моде: {0}, обновлено: {1}, с ошибкой: {2}",
                files.Length, copied, failed));

            if (copied > 0)
                Log("новые тексты вступят в силу при следующем запуске игры");
        }

        /// <summary>
        /// Читает installLanguage из Settings.Lua — игра пишет туда значения,
        /// выставленные игроком в меню модов.
        /// </summary>
        private static bool ReadInstallSetting(string modDir)
        {
            string path = Path.Combine(modDir, "Settings.Lua");
            if (!File.Exists(path))
                return true;

            try
            {
                string text = File.ReadAllText(path);
                Match m = Regex.Match(text, @"\binstallLanguage\s*=\s*([^,\r\n}]+)");
                if (!m.Success)
                    return true;

                return m.Groups[1].Value.Trim()
                        .Equals("true", StringComparison.OrdinalIgnoreCase);
            }
            catch (Exception e)
            {
                Log("не удалось прочитать Settings.Lua: " + e.Message);
                return true;
            }
        }

        /// <summary>
        /// Находит папку мода.
        ///
        /// Через Assembly.Location это не работает: игра грузит плагин из байтов,
        /// и путь на диске у такой сборки пустой. Поэтому идём от папки игры:
        /// Application.dataPath = &lt;игра&gt;\The Scroll of Taiwu_Data, а моды
        /// лежат в &lt;игра&gt;\Mod\&lt;имя&gt;.
        /// </summary>
        private static string ResolveModDir()
        {
            try
            {
                DirectoryInfo root = Directory.GetParent(Application.dataPath);
                if (root == null)
                    return null;

                string modsRoot = Path.Combine(root.FullName, "Mod");
                if (!Directory.Exists(modsRoot))
                {
                    Log("папки модов нет: " + modsRoot);
                    return null;
                }

                string expected = Path.Combine(modsRoot, "TaiwuRussian");
                if (HasOurPlugin(expected))
                    return expected;

                // папку могли переименовать — ищем ту, где лежит наша DLL
                foreach (string dir in Directory.GetDirectories(modsRoot))
                    if (HasOurPlugin(dir))
                        return dir;

                Log("в " + modsRoot + " не нашлось папки с TaiwuRussian.dll");
                return null;
            }
            catch (Exception e)
            {
                Log("не удалось найти папку мода: " + e.Message);
                return null;
            }
        }

        private static bool HasOurPlugin(string dir)
        {
            return File.Exists(Path.Combine(dir, Path.Combine("Plugins", "TaiwuRussian.dll")));
        }

        private static void Log(string message)
        {
            try
            {
                Debug.Log("[TaiwuRussian] " + message);
            }
            catch
            {
                // логирование не должно ронять плагин
            }
        }
    }
}
