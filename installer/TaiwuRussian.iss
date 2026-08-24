; Установщик русской локализации The Scroll of Taiwu
; Собирается компилятором Inno Setup 6:  ISCC.exe TaiwuRussian.iss

#define AppName "Русская локализация The Scroll of Taiwu"
#define AppShortName "TaiwuRussian"
#define AppVersion "0.3.0"
#define AppPublisher "WCG"
#define GameExe "The Scroll of Taiwu.exe"
#define GameVersion "0.84.75"

[Setup]
AppId={{8F3C1A54-2E7B-4D9A-9C21-5A7E4B0C3D19}
AppName={#AppName}
AppVersion={#AppVersion}
AppVerName={#AppName} {#AppVersion}
AppPublisher={#AppPublisher}
VersionInfoVersion=0.3.0.0
DefaultDirName={code:DetectGameDir}
DirExistsWarning=no
UsePreviousAppDir=yes
AppendDefaultDirName=no
DisableProgramGroupPage=yes
AllowNoIcons=yes
OutputDir=.
OutputBaseFilename=TaiwuRussian-{#AppVersion}-setup
Compression=lzma2/max
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
UninstallFilesDir={app}\TaiwuRussian_uninstall
UninstallDisplayName={#AppName}
UninstallDisplayIcon={app}\{#GameExe}

[Languages]
Name: "ru"; MessagesFile: "compiler:Languages\Russian.isl"

[Messages]
ru.WelcomeLabel2=Программа установит русскую локализацию для игры The Scroll of Taiwu версии {#GameVersion}.%n%nПеред установкой закройте игру.
ru.SelectDirLabel3=Укажите папку, в которую установлена игра The Scroll of Taiwu.
ru.SelectDirBrowseLabel=Нажмите «Обзор», чтобы выбрать папку вручную, или «Найти игру на дисках» — программа поищет её сама.

[CustomMessages]
ru.DirHint=Нужна папка с файлом «{#GameExe}» — рядом с ним лежат «The Scroll of Taiwu_Data», «Event» и «Mod».
ru.BtnSearch=Найти игру на дисках
ru.Searching=Идёт поиск, подождите…
ru.FoundAt=Игра найдена:%n%n%1%n%nИспользовать эту папку?
ru.NotFound=Автоматически найти игру не удалось.%n%nУкажите папку вручную кнопкой «Обзор». Это папка, в которой лежит «{#GameExe}» — например:%n%nD:\Games\The Scroll of Taiwu%nD:\SteamLibrary\steamapps\common\The Scroll of Taiwu
ru.NotGameDir=В этой папке нет файла «{#GameExe}».%n%nУкажите папку с установленной игрой — ту, где лежит сам исполняемый файл игры.
ru.TaskMod=Установить мод (восстанавливает перевод после обновления игры)
ru.TaskEvents=Перевести сюжетные диалоги (пролог, приход в деревню Тайу, деревушка за долиной)
ru.FinishNote=Перевод установлен.%n%nВключите его в игре: Настройки → Язык игры → Русский, затем перезапустите игру.%n%nЕсли понадобится зайти в раздел модов, сначала переключите язык на английский: с русским языком этот раздел зависает — это ограничение самой игры.

[Tasks]
Name: "modfiles"; Description: "{cm:TaskMod}"; GroupDescription: "Дополнительно:"
Name: "events"; Description: "{cm:TaskEvents}"; GroupDescription: "Дополнительно:"

[Files]
; Основные языковые файлы — игра читает их отсюда
Source: "payload\Language_RU\*"; DestDir: "{app}\The Scroll of Taiwu_Data\StreamingAssets\Language_RU"; Flags: recursesubdirs createallsubdirs ignoreversion

; Всплывающие подсказки: игра берёт их только из Language_EN, поэтому кладём поверх
Source: "payload\Language_RU\CommonTip\*"; DestDir: "{app}\The Scroll of Taiwu_Data\StreamingAssets\Language_EN\CommonTip"; Flags: recursesubdirs createallsubdirs ignoreversion

; Мод: держит свою копию и восстанавливает её после обновления игры
Source: "payload\Mod\TaiwuRussian\*"; DestDir: "{app}\Mod\TaiwuRussian"; Flags: recursesubdirs createallsubdirs ignoreversion; Tasks: modfiles
Source: "payload\Language_RU\*"; DestDir: "{app}\Mod\TaiwuRussian\Language_RU"; Flags: recursesubdirs createallsubdirs ignoreversion; Tasks: modfiles

; Сюжетные диалоги. Русский файл — наш исходник, копия поверх английского — то, что читает игра
Source: "payload\EventLanguages\*_Language_RU.txt"; DestDir: "{app}\Event\EventLanguages"; Flags: ignoreversion; Tasks: events
Source: "payload\EventLanguages\Taiwu_EventPackage_NewMainStory_DeepValley_Language_RU.txt"; DestDir: "{app}\Event\EventLanguages"; DestName: "Taiwu_EventPackage_NewMainStory_DeepValley_Language_EN.txt"; Flags: ignoreversion; Tasks: events
Source: "payload\EventLanguages\Taiwu_EventPackage_MainStory_DeepValley_Language_RU.txt"; DestDir: "{app}\Event\EventLanguages"; DestName: "Taiwu_EventPackage_MainStory_DeepValley_Language_EN.txt"; Flags: ignoreversion; Tasks: events
Source: "payload\EventLanguages\Taiwu_EventPackage_DeepValleyExit_Language_RU.txt"; DestDir: "{app}\Event\EventLanguages"; DestName: "Taiwu_EventPackage_DeepValleyExit_Language_EN.txt"; Flags: ignoreversion; Tasks: events
Source: "payload\EventLanguages\Taiwu_EventPackage_MainStory_FirstTaiWu_Language_RU.txt"; DestDir: "{app}\Event\EventLanguages"; DestName: "Taiwu_EventPackage_MainStory_FirstTaiWu_Language_EN.txt"; Flags: ignoreversion; Tasks: events
Source: "payload\EventLanguages\Taiwu_EventPackage_MainStory_SmallVilliage_Language_RU.txt"; DestDir: "{app}\Event\EventLanguages"; DestName: "Taiwu_EventPackage_MainStory_SmallVilliage_Language_EN.txt"; Flags: ignoreversion; Tasks: events

[UninstallDelete]
Type: filesandordirs; Name: "{app}\The Scroll of Taiwu_Data\StreamingAssets\Language_RU"
Type: filesandordirs; Name: "{app}\Mod\TaiwuRussian"
Type: files; Name: "{app}\Event\EventLanguages\Taiwu_EventPackage_NewMainStory_DeepValley_Language_RU.txt"
Type: files; Name: "{app}\Event\EventLanguages\Taiwu_EventPackage_MainStory_DeepValley_Language_RU.txt"
Type: files; Name: "{app}\Event\EventLanguages\Taiwu_EventPackage_DeepValleyExit_Language_RU.txt"
Type: files; Name: "{app}\Event\EventLanguages\Taiwu_EventPackage_MainStory_FirstTaiWu_Language_RU.txt"
Type: files; Name: "{app}\Event\EventLanguages\Taiwu_EventPackage_MainStory_SmallVilliage_Language_RU.txt"

[Code]
const
  BackupRoot = 'TaiwuRussian_backup';

var
  SearchButton: TNewButton;
  HintLabel: TNewStaticText;

// ---- что мы кладём поверх английских файлов -------------------------------
function CommonTipFiles(Index: Integer): String;
begin
  case Index of
    0: Result := 'Character\Charm.json';
    1: Result := 'Character\Feature.json';
    2: Result := 'Character\Guard.json';
    3: Result := 'Character\SecretInformation.json';
    4: Result := 'Combat\CombatChangeTrickConfirmTip.json';
    5: Result := 'Combat\CombatChangeTrickTrickTip.json';
    6: Result := 'Combat\CombatPartialFlaw.json';
    7: Result := 'Combat\CostClearDefend.json';
    8: Result := 'Combat\CostNeiliAllocation.json';
    9: Result := 'Combat\CostWugKing.json';
   10: Result := 'Cricket\CricketSkillReplace.json';
   11: Result := 'Debug\DebugTip.json';
   12: Result := 'Event\CustomSectLaw.json';
   13: Result := 'Event\EventOption.json';
   14: Result := 'LegendaryBook\LegendaryBookBonus_1.json';
  else
    Result := '';
  end;
end;

function EventFiles(Index: Integer): String;
begin
  case Index of
    0: Result := 'Taiwu_EventPackage_NewMainStory_DeepValley_Language_EN.txt';
    1: Result := 'Taiwu_EventPackage_MainStory_DeepValley_Language_EN.txt';
    2: Result := 'Taiwu_EventPackage_DeepValleyExit_Language_EN.txt';
    3: Result := 'Taiwu_EventPackage_MainStory_FirstTaiWu_Language_EN.txt';
    4: Result := 'Taiwu_EventPackage_MainStory_SmallVilliage_Language_EN.txt';
  else
    Result := '';
  end;
end;

// ---- поиск папки с игрой --------------------------------------------------
function IsGameDir(Dir: String): Boolean;
begin
  Result := (Dir <> '') and FileExists(AddBackslash(Dir) + '{#GameExe}');
end;

function IsSkippedDir(Name: String): Boolean;
var
  L: String;
begin
  L := Lowercase(Name);
  Result := (L = 'windows') or (L = '$recycle.bin') or (L = 'system volume information') or
            (L = 'programdata') or (L = 'appdata') or (L = 'perflogs') or
            (L = 'msocache') or (L = 'recovery') or (L = 'boot') or (L = 'config.msi');
end;

// Ищет вглубь на Depth уровней. Depth=0 — смотрим только саму папку.
function ScanDir(Root: String; Depth: Integer): String;
var
  FR: TFindRec;
  Sub: String;
begin
  Result := '';
  if Root = '' then Exit;
  if IsGameDir(Root) then begin Result := Root; Exit; end;
  if Depth <= 0 then Exit;
  if not DirExists(Root) then Exit;

  if FindFirst(AddBackslash(Root) + '*', FR) then
  try
    repeat
      if (FR.Attributes and FILE_ATTRIBUTE_DIRECTORY <> 0) and
         (FR.Name <> '.') and (FR.Name <> '..') and (not IsSkippedDir(FR.Name)) then
      begin
        Sub := AddBackslash(Root) + FR.Name;
        Result := ScanDir(Sub, Depth - 1);
        if Result <> '' then Exit;
      end;
    until not FindNext(FR);
  finally
    FindClose(FR);
  end;
end;

function SteamLibraryGuess(SteamPath: String): String;
var
  Vdf, Line: String;
  Lines: TArrayOfString;
  I, P1, P2: Integer;
  Cand: String;
begin
  Result := '';
  if SteamPath = '' then Exit;
  Cand := AddBackslash(SteamPath) + 'steamapps\common\The Scroll of Taiwu';
  if IsGameDir(Cand) then begin Result := Cand; Exit; end;

  Vdf := AddBackslash(SteamPath) + 'steamapps\libraryfolders.vdf';
  if not FileExists(Vdf) then Exit;
  if not LoadStringsFromFile(Vdf, Lines) then Exit;
  for I := 0 to GetArrayLength(Lines) - 1 do
  begin
    Line := Lines[I];
    P1 := Pos('"path"', Line);
    if P1 > 0 then
    begin
      Line := Copy(Line, P1 + 6, Length(Line));
      P1 := Pos('"', Line);
      if P1 > 0 then
      begin
        Line := Copy(Line, P1 + 1, Length(Line));
        P2 := Pos('"', Line);
        if P2 > 1 then
        begin
          Cand := Copy(Line, 1, P2 - 1);
          StringChangeEx(Cand, '\\', '\', True);
          Cand := AddBackslash(Cand) + 'steamapps\common\The Scroll of Taiwu';
          if IsGameDir(Cand) then begin Result := Cand; Exit; end;
        end;
      end;
    end;
  end;
end;

// Быстрая проверка привычных мест: без обхода всего диска.
function QuickGuess: String;
var
  S, Drive, Cand: String;
  D, I: Integer;
  FreeMB, TotalMB: Cardinal;
  Roots: array[0..9] of String;
begin
  Result := '';

  // 1. Steam из реестра
  if RegQueryStringValue(HKLM, 'SOFTWARE\WOW6432Node\Valve\Steam', 'InstallPath', S) or
     RegQueryStringValue(HKLM, 'SOFTWARE\Valve\Steam', 'InstallPath', S) or
     RegQueryStringValue(HKCU, 'Software\Valve\Steam', 'SteamPath', S) then
  begin
    StringChangeEx(S, '/', '\', True);
    Result := SteamLibraryGuess(S);
    if Result <> '' then Exit;
  end;

  // 2. Привычные папки на всех дисках, на два уровня вглубь
  for D := 0 to 25 do
  begin
    Drive := Chr(Ord('A') + D) + ':';
    if GetSpaceOnDisk(Drive + '\', True, FreeMB, TotalMB) then
    begin
      Roots[0] := Drive + '\Games';
      Roots[1] := Drive + '\Игры';
      Roots[2] := Drive + '\SteamLibrary\steamapps\common';
      Roots[3] := Drive + '\Steam\steamapps\common';
      Roots[4] := Drive + '\Program Files (x86)\Steam\steamapps\common';
      Roots[5] := Drive + '\Program Files\Steam\steamapps\common';
      Roots[6] := Drive + '\GOG Games';
      Roots[7] := Drive + '\Repack';
      Roots[8] := Drive + '\Repacks';
      Roots[9] := Drive + '\';
      for I := 0 to 9 do
      begin
        if I = 9 then
          Cand := ScanDir(Roots[I], 1)
        else
          Cand := ScanDir(Roots[I], 2);
        if Cand <> '' then begin Result := Cand; Exit; end;
      end;
    end;
  end;
end;

// Долгий поиск: обход дисков вглубь, запускается кнопкой.
function DeepSearch: String;
var
  Drive: String;
  D: Integer;
  FreeMB, TotalMB: Cardinal;
begin
  Result := QuickGuess;
  if Result <> '' then Exit;
  for D := 0 to 25 do
  begin
    Drive := Chr(Ord('A') + D) + ':';
    if GetSpaceOnDisk(Drive + '\', True, FreeMB, TotalMB) then
    begin
      Result := ScanDir(Drive + '\', 4);
      if Result <> '' then Exit;
    end;
  end;
end;

function DetectGameDir(Param: String): String;
begin
  Result := QuickGuess;
  if Result = '' then
    Result := ExpandConstant('{autopf}\The Scroll of Taiwu');
end;

// ---- резервные копии английских файлов ------------------------------------
procedure BackupOne(Src, Dst: String);
begin
  if FileExists(Src) and (not FileExists(Dst)) then
  begin
    ForceDirectories(ExtractFileDir(Dst));
    CopyFile(Src, Dst, True);
  end;
end;

procedure MakeBackups;
var
  Game, Bak, Rel: String;
  I: Integer;
begin
  Game := AddBackslash(ExpandConstant('{app}'));
  Bak := Game + BackupRoot + '\';

  for I := 0 to 14 do
  begin
    Rel := CommonTipFiles(I);
    BackupOne(Game + 'The Scroll of Taiwu_Data\StreamingAssets\Language_EN\CommonTip\' + Rel,
              Bak + 'CommonTip\' + Rel);
  end;

  if WizardIsTaskSelected('events') then
    for I := 0 to 4 do
    begin
      Rel := EventFiles(I);
      BackupOne(Game + 'Event\EventLanguages\' + Rel, Bak + 'EventLanguages\' + Rel);
    end;
end;

// Возврат оригиналов. Вызывается ПОСЛЕ удаления файлов, иначе Inno
// сотрёт только что восстановленные английские файлы.
procedure RestoreBackups;
var
  Game, Bak, Rel, Dst: String;
  I: Integer;
begin
  Game := AddBackslash(ExpandConstant('{app}'));
  Bak := Game + BackupRoot + '\';

  for I := 0 to 14 do
  begin
    Rel := CommonTipFiles(I);
    if FileExists(Bak + 'CommonTip\' + Rel) then
    begin
      Dst := Game + 'The Scroll of Taiwu_Data\StreamingAssets\Language_EN\CommonTip\' + Rel;
      ForceDirectories(ExtractFileDir(Dst));
      CopyFile(Bak + 'CommonTip\' + Rel, Dst, False);
    end;
  end;

  for I := 0 to 4 do
  begin
    Rel := EventFiles(I);
    if FileExists(Bak + 'EventLanguages\' + Rel) then
    begin
      Dst := Game + 'Event\EventLanguages\' + Rel;
      ForceDirectories(ExtractFileDir(Dst));
      CopyFile(Bak + 'EventLanguages\' + Rel, Dst, False);
    end;
  end;

  DelTree(Game + BackupRoot, True, True, True);
end;

// ---- страница выбора папки ------------------------------------------------
procedure SearchButtonClick(Sender: TObject);
var
  Found: String;
begin
  SearchButton.Enabled := False;
  HintLabel.Caption := ExpandConstant('{cm:Searching}');
  WizardForm.Refresh;
  try
    Found := DeepSearch;
  finally
    SearchButton.Enabled := True;
    HintLabel.Caption := ExpandConstant('{cm:DirHint}');
  end;

  if Found <> '' then
  begin
    if MsgBox(FmtMessage(ExpandConstant('{cm:FoundAt}'), [Found]), mbConfirmation, MB_YESNO) = IDYES then
      WizardForm.DirEdit.Text := Found;
  end
  else
    MsgBox(ExpandConstant('{cm:NotFound}'), mbInformation, MB_OK);
end;

procedure InitializeWizard;
begin
  HintLabel := TNewStaticText.Create(WizardForm);
  HintLabel.Parent := WizardForm.SelectDirPage;
  HintLabel.Left := WizardForm.DirEdit.Left;
  HintLabel.Top := WizardForm.DirEdit.Top + WizardForm.DirEdit.Height + ScaleY(14);
  HintLabel.Width := WizardForm.SelectDirPage.Width - WizardForm.DirEdit.Left;
  HintLabel.AutoSize := False;
  HintLabel.Height := ScaleY(34);
  HintLabel.WordWrap := True;
  HintLabel.Caption := ExpandConstant('{cm:DirHint}');

  SearchButton := TNewButton.Create(WizardForm);
  SearchButton.Parent := WizardForm.SelectDirPage;
  SearchButton.Left := WizardForm.DirEdit.Left;
  SearchButton.Top := HintLabel.Top + HintLabel.Height + ScaleY(6);
  SearchButton.Width := ScaleX(190);
  SearchButton.Height := WizardForm.DirBrowseButton.Height;
  SearchButton.Caption := ExpandConstant('{cm:BtnSearch}');
  SearchButton.OnClick := @SearchButtonClick;
end;

function NextButtonClick(CurPageID: Integer): Boolean;
begin
  Result := True;
  if CurPageID = wpSelectDir then
    if not IsGameDir(WizardDirValue) then
    begin
      MsgBox(ExpandConstant('{cm:NotGameDir}'), mbError, MB_OK);
      Result := False;
    end;
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssInstall then
    MakeBackups;
end;

procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);
begin
  if CurUninstallStep = usPostUninstall then
    RestoreBackups;
end;

procedure CurPageChanged(CurPageID: Integer);
begin
  if CurPageID = wpFinished then
    WizardForm.FinishedLabel.Caption := ExpandConstant('{cm:FinishNote}');
end;