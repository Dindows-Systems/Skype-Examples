#define MyAppName "SkypeTalking"
#define MyAppVer "0.9.6"
#define MyAppPublisher "Hrvoje Katiæ"
#define MyAppExeName "SkypeTalking.exe"
#define MyAppDescription "Provides access to Skype using speech and refreshable braille"
#define MyAppURL "http://skypetalking.googlecode.com/"
#define MyAppCopyrightYear "2010"

[Setup]
AppCopyright=Copyright © {#MyAppCopyrightYear} {#MyAppPublisher}
AppName={#MyAppName}
AppVerName={#MyAppName} {#MyAppVer}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\{#MyAppName}
DefaultGroupName={#MyAppName}
OutputDir=..\src\SkypeTalkingBinary
OutputBaseFilename={#MyAppName}_{#MyAppVer}_Setup
SetupIconFile=..\src\{#MyAppName}.ico
Compression=lzma/ultra
SolidCompression=true
DisableStartupPrompt=true
AlwaysShowDirOnReadyPage=true
AlwaysShowGroupOnReadyPage=true
ShowLanguageDialog=yes
DirExistsWarning=no
DisableProgramGroupPage=true
DisableReadyPage=true
DisableFinishedPage=false
ArchitecturesAllowed=x86 x64
VersionInfoCompany={#MyAppPublisher}
VersionInfoCopyright=Copyright © {#MyAppCopyrightYear} {#MyAppPublisher}
VersionInfoDescription={#MyAppDescription}
VersionInfoProductName={#MyAppName}
VersionInfoProductVersion={#MyAppVer}
VersionInfoVersion={#MyAppVer}
AppVersion={#MyAppVer}
AppModifyPath={app}
AppContact=hrvojekatic@gmail.com
UninstallDisplayName={#MyAppName} {#MyAppVer}
UninstallDisplayIcon={app}\SkypeTalking.ico
MinVersion=,5.01.2600

[Languages]
Name: en; MessagesFile: compiler:Default.isl,Languages\DefaultCustom.isl; LicenseFile: ..\license.txt; InfoAfterFile: Languages\_InfoAfter_en.txt
Name: ar_EG; MessagesFile: Languages\Arabic.isl; LicenseFile: ..\license.txt; InfoAfterFile: Languages\_InfoAfter_en.txt
Name: be; MessagesFile: Languages\Belarusian.isl; LicenseFile: ..\license.txt; InfoAfterFile: Languages\_InfoAfter_en.txt
Name: bg; MessagesFile: Languages\Bulgarian.isl,Languages\BulgarianCustom.isl; LicenseFile: ..\license.txt; InfoAfterFile: Languages\_InfoAfter_bg.txt
Name: hr; MessagesFile: Languages\Croatian.isl,Languages\CroatianCustom.isl; LicenseFile: ..\license.txt; InfoAfterFile: Languages\_InfoAfter_hr.txt
Name: cs; MessagesFile: compiler:Languages\Czech.isl; LicenseFile: ..\license.txt; InfoAfterFile: Languages\_InfoAfter_en.txt
Name: da; MessagesFile: compiler:Languages\Danish.isl,Languages\DanishCustom.isl; LicenseFile: ..\license.txt; InfoAfterFile: Languages\_InfoAfter_da.txt
Name: fi; MessagesFile: compiler:Languages\Finnish.isl; LicenseFile: ..\license.txt; InfoAfterFile: Languages\_InfoAfter_en.txt
Name: fr; MessagesFile: compiler:Languages\French.isl,Languages\FrenchCustom.isl; LicenseFile: ..\help\fr\license.txt; InfoAfterFile: Languages\_InfoAfter_fr.txt
Name: de; MessagesFile: compiler:Languages\German.isl,Languages\GermanCustom.isl; LicenseFile: ..\help\de\license.txt; InfoAfterFile: Languages\_InfoAfter_de.txt
Name: he; MessagesFile: compiler:Languages\Hebrew.isl; LicenseFile: ..\license.txt; InfoAfterFile: Languages\_InfoAfter_en.txt
Name: hu; MessagesFile: compiler:Languages\Hungarian.isl; LicenseFile: ..\license.txt; InfoAfterFile: Languages\_InfoAfter_en.txt
Name: it; MessagesFile: compiler:Languages\Italian.isl; LicenseFile: ..\license.txt; InfoAfterFile: Languages\_InfoAfter_en.txt
Name: ja; MessagesFile: compiler:Languages\Japanese.isl; LicenseFile: ..\license.txt; InfoAfterFile: Languages\_InfoAfter_en.txt
Name: lv; MessagesFile: Languages\Latvian.isl; LicenseFile: ..\license.txt; InfoAfterFile: Languages\_InfoAfter_en.txt
Name: mk; MessagesFile: Languages\Macedonian.isl; LicenseFile: ..\license.txt; InfoAfterFile: Languages\_InfoAfter_en.txt
Name: ms; MessagesFile: Languages\Malaysian.isl; LicenseFile: ..\help\ms\license.txt; InfoAfterFile: Languages\_InfoAfter_en.txt
Name: pl; MessagesFile: compiler:Languages\Polish.isl; LicenseFile: ..\license.txt; InfoAfterFile: Languages\_InfoAfter_en.txt
Name: pt_PT; MessagesFile: compiler:Languages\Portuguese.isl; LicenseFile: ..\license.txt; InfoAfterFile: Languages\_InfoAfter_en.txt
Name: ru; MessagesFile: compiler:Languages\Russian.isl,Languages\RussianCustom.isl; LicenseFile: ..\license.txt; InfoAfterFile: Languages\_InfoAfter_ru.txt
Name: sr; MessagesFile: Languages\SerbianLatin.isl; LicenseFile: ..\license.txt; InfoAfterFile: Languages\_InfoAfter_en.txt
Name: sl; MessagesFile: compiler:Languages\Slovenian.isl,Languages\SlovenianCustom.isl; LicenseFile: ..\license.txt; InfoAfterFile: Languages\_InfoAfter_sl.txt
Name: es; MessagesFile: compiler:Languages\Spanish.isl; LicenseFile: ..\help\es\license.txt; InfoAfterFile: Languages\_InfoAfter_en.txt
Name: tr; MessagesFile: Languages\Turkish.isl; LicenseFile: ..\license.txt; InfoAfterFile: Languages\_InfoAfter_en.txt
Name: uk; MessagesFile: Languages\Ukrainian.isl; LicenseFile: ..\license.txt; InfoAfterFile: Languages\_InfoAfter_en.txt

[Files]
Source: ..\src\{#MyAppName}\{#MyAppExeName}; DestDir: {app}; Flags: ignoreversion
Source: ..\src\{#MyAppName}\*; DestDir: {app}; Excludes: ..\src\{#MyAppName}\lib\jfwapi.dll; Flags: ignoreversion recursesubdirs createallsubdirs
Source: ..\src\{#MyAppName}\lib\jfwapi.dll; DestDir: {app}\lib; Flags: regserver ignoreversion

[Icons]
Name: {group}\{cm:InstructionsManual,{#MyAppName}}; Filename: {app}\help\en\readme.html; Languages: en ar_EG be cs fi he ja mk pl pt_PT sr sl
Name: {group}\{cm:InstructionsManual,{#MyAppName}}; Filename: {app}\help\{language}\readme.html; Languages: bg de fr hu hr it lv ms ru
Name: {group}\{cm:InstructionsManual,{#MyAppName}}; Filename: {app}\help\{language}\readme.txt; Languages: da es
Name: {group}\{cm:WhatsNew,{#MyAppName}}; Filename: {app}\help\en\whatsnew.html; Languages: en ar_EG be bg cs da he ja mk pl pt_PT sr sl
Name: {group}\{cm:WhatsNew,{#MyAppName}}; Filename: {app}\help\{language}\whatsnew.html; Languages: de fr hu hr lv ms ru
Name: {group}\{cm:WhatsNew,{#MyAppName}}; Filename: {app}\help\{language}\whatsnew.txt; Languages: es fi it tr uk
Name: {group}\{cm:LaunchProgram,{#MyAppName}}; Filename: {app}\{#MyAppExeName}; HotKey: Alt+Ctrl+Shift+T; WorkingDir: {app}
Name: {group}\{cm:ProgramOnTheWeb, {#MyAppName}}; Filename: {#MyAppURL}
Name: {group}\{cm:UninstallProgram, {#MyAppName}}; Filename: {uninstallexe}
Name: {userdesktop}\{#MyAppName}; Filename: {app}\{#MyAppExeName}; WorkingDir: {app}

[Run]
Filename: {app}\help\en\readme.html; Description: {cm:ReadInstructionsManual,{#MyAppName}}; Flags: postinstall shellexec skipifsilent; Languages: en ar_EG be cs fi he ja mk pl pt_PT sr sl
Filename: {app}\help\{language}\readme.html; Description: {cm:ReadInstructionsManual,{#MyAppName}}; Flags: postinstall shellexec skipifsilent; Languages: bg de fr hu hr it lv ms ru
Filename: {app}\help\{language}\readme.txt; Description: {cm:ReadInstructionsManual,{#MyAppName}}; Flags: postinstall shellexec skipifsilent; Languages: da es
Filename: {app}\{#MyAppExeName}; Description: {cm:LaunchProgram,{#MyAppName}}; Flags: nowait postinstall skipifsilent
