@echo off
setlocal EnableDelayedExpansion
set "ROOT=%~dp0"
cd /d "%ROOT%sample"

rem 1) Lokales bun.exe  2) bun im PATH  3) einmalig per curl  4) Node-Fallback
set "RUNNER="
set "MODE="

if exist "%ROOT%bun.exe" (
    set "RUNNER=%ROOT%bun.exe"
    set "MODE=bun"
)

if not defined RUNNER (
    where bun >nul 2>&1
    if !ERRORLEVEL!==0 (
        set "RUNNER=bun"
        set "MODE=bun"
    )
)

if not defined RUNNER (
    call :ensure_bun
    if exist "%ROOT%bun.exe" (
        set "RUNNER=%ROOT%bun.exe"
        set "MODE=bun"
    )
)

cd /d "%ROOT%sample"

if defined RUNNER if "!MODE!"=="bun" (
    "!RUNNER!" test orderCalculator.test.js
    exit /b !ERRORLEVEL!
)

where node >nul 2>&1
if %ERRORLEVEL%==0 (
    node --test orderCalculator.test.js
    exit /b %ERRORLEVEL%
)

echo [optional] Kein Bun/Node — Tests ueberspringen. Uebung geht ohne Testlauf weiter.
exit /b 0

:ensure_bun
cd /d "%ROOT%"
if exist "%ROOT%bun.exe" exit /b 0

set "BUN_VERSION=bun-v1.2.18"
set "BUN_ZIP=bun-windows-x64.zip"
set "BUN_URL=https://github.com/oven-sh/bun/releases/download/%BUN_VERSION%/%BUN_ZIP%"

echo Lade Bun einmalig per curl ...
curl -fsSL -o "%BUN_ZIP%" "%BUN_URL%"
if errorlevel 1 exit /b 1

tar -xf "%BUN_ZIP%"
if exist "bun-windows-x64\bun.exe" move /Y "bun-windows-x64\bun.exe" "%ROOT%bun.exe" >nul
if exist "bun.exe" move /Y "bun.exe" "%ROOT%bun.exe" >nul
rmdir /s /q "bun-windows-x64" 2>nul
del "%BUN_ZIP%" 2>nul
exit /b 0
