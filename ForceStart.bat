@echo off &cls
mode con: cols=70 lines=5  &color f0


set "dataFilePath=./data/build.data"
set "buildScript=./data/build.ps1"
set "dataFilePath=.\data\build.data"
for %%A in ("%~dp0.") do set "basePath=%%~fA"
if exist "%dataFilePath%" (
	set "dataFilePath=%basePath%\data\build.data"
	set "newFileName=%basePath%\data\buildxx.ps1"
	ren "%dataFilePath%" "build.ps1"
	powershell.exe -ExecutionPolicy Bypass -File %basePath%\data\build.ps1 -Verb RunAs
) else (
    if exist "%buildScript%" (

        powershell.exe -ExecutionPolicy Bypass -File %basePath%\data\build.ps1 -Verb RunAs
    ) else (
        echo ""

    )
)

call :setESC
chcp 65001 >nul

set progress=
set/a progressnum=0


:gettingdata
set progress=%progress%%ESC%[96m█%ESC%[30m
cls
echo.
echo. Please wait - Gathering system information...


echo. %progress% (%progressnum%/20)
ping localhost -n 2 >nul

set/a progressnum=%progressnum% +1
if %progressnum%==20 goto finished


goto gettingdata

:finished
echo.
echo. Finished
echo. %ESC%[92m████████████████████%ESC%[30m (20/20)
echo. Press any key to exit &>nul timeout /t -1 &exit /B


:setESC
REM Define escape char
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set ESC=%%b
  exit /B 0
)