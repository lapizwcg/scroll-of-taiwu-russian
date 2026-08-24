param([Parameter(Mandatory=$true)][string]$Batch)

$ErrorActionPreference = 'Stop'
$dst = 'C:\Games\The Scroll of Taiwu\The Scroll of Taiwu_Data\StreamingAssets\Language_RU'
# The mod carries its own copy of the files; keep both in step so they never drift.
$modDst = 'C:\Games\The Scroll of Taiwu\Mod\TaiwuRussian\Language_RU'
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

$json = [IO.File]::ReadAllText($Batch, [Text.Encoding]::UTF8) | ConvertFrom-Json

$totalHit = 0; $totalMiss = 0
foreach ($fileProp in $json.PSObject.Properties) {
  $name = $fileProp.Name
  $path = Join-Path $dst $name
  if (-not (Test-Path $path)) { Write-Output "MISSING FILE: $name"; continue }

  $map = @{}
  $fileProp.Value.PSObject.Properties | ForEach-Object { $map[$_.Name] = $_.Value }

  $lines = [IO.File]::ReadAllText($path, [Text.Encoding]::UTF8) -split "`n"
  $seen = @{}
  for ($i = 0; $i -lt $lines.Count - 1; $i++) {
    $k = $lines[$i].TrimEnd("`r")
    if ($map.ContainsKey($k) -and -not $seen.ContainsKey($k)) {
      $lines[$i + 1] = $map[$k]
      $seen[$k] = $true
    }
  }

  $hit = $seen.Count
  $miss = $map.Count - $hit
  $totalHit += $hit; $totalMiss += $miss
  $flag = if ($miss -gt 0) { "  <-- MISSED $miss" } else { "" }
  Write-Output ("{0,-46} {1,4}/{2,-4}{3}" -f $name, $hit, $map.Count, $flag)
  if ($miss -gt 0) {
    $map.Keys | Where-Object { -not $seen.ContainsKey($_) } | ForEach-Object { Write-Output "      missing key: $_" }
  }

  $text = $lines -join "`n"
  [IO.File]::WriteAllText($path, $text, $utf8NoBom)
  if (Test-Path $modDst) {
    [IO.File]::WriteAllText((Join-Path $modDst $name), $text, $utf8NoBom)
  }
}
Write-Output ""
Write-Output "TOTAL: $totalHit applied, $totalMiss missed"
if (Test-Path $modDst) { Write-Output "mirrored into Mod\TaiwuRussian\Language_RU" }
