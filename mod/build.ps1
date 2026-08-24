# Building the Russian localization mod.
# Usage:  powershell -File build.ps1
$ErrorActionPreference = "Stop"

$game    = "C:\Games\The Scroll of Taiwu"
$managed = Join-Path $game "The Scroll of Taiwu_Data\Managed"
$src     = "C:\Games\taiwu-ru-mod\TaiwuRussianPlugin.cs"
# Build into staging, never straight into the game folder: a half-assembled mod
# left in Mod\ wedges the game's startup.
$outDir  = "C:\Games\taiwu-ru-mod\staging\TaiwuRussian\Plugins"
$outDll  = Join-Path $outDir "TaiwuRussian.dll"
$csc     = "C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe"

$refs = @(
    "TaiwuModdingLib.dll",
    "Assembly-CSharp.dll",
    "Assembly-CSharp-firstpass.dll",
    "GameData.Shared.dll",
    "Unity.TextMeshPro.dll",
    "UnityEngine.dll",
    "UnityEngine.CoreModule.dll",
    "UnityEngine.UI.dll",
    "UnityEngine.TextRenderingModule.dll",
    "netstandard.dll"
)

foreach ($r in $refs) {
    $p = Join-Path $managed $r
    if (-not (Test-Path $p)) { Write-Host "MISSING reference: $r" }
}

New-Item -ItemType Directory -Force -Path $outDir | Out-Null

$refArgs = $refs | Where-Object { Test-Path (Join-Path $managed $_) } |
           ForEach-Object { "/r:`"" + (Join-Path $managed $_) + "`"" }

$args = @("/target:library", "/optimize+", "/nologo", "/warn:2",
          "/out:`"$outDll`"") + $refArgs + @("`"$src`"")

Write-Host "csc -> $outDll"
& $csc $args
if ($LASTEXITCODE -ne 0) { Write-Host "BUILD FAILED (exit $LASTEXITCODE)"; exit $LASTEXITCODE }

Write-Host "OK:" (Get-Item $outDll).Length "bytes"
