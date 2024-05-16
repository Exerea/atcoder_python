@echo off

rem ****************************************
rem yyyymmddフォルダの作成
rem ****************************************

rem 日付をyyyyMMdd形式で取得
for /f "tokens=2 delims==" %%i in ('"wmic os get localdatetime /value"') do set datetime=%%i
set today=%datetime:~0,8%

rem フォルダ名の重複を確認し、重複があれば語尾に数字を付ける
set foldername=%today%
set count=1

:checkFolder
if exist "%foldername%" (
    set /a count+=1
    set foldername=%today%_%count%
    goto checkFolder
)

rem 最終的なフォルダ名でフォルダを作成
mkdir "%foldername%"

rem defaultFolderの中身を新しいフォルダにコピー
xcopy /s "defaultFolder" "%foldername%"