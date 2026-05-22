@echo off
setlocal
cd /d "%~dp0sample"

if exist "%~dp0node.exe" (
    set "NODE=%~dp0node.exe"
) else (
    set "NODE=node"
)

"%NODE%" --test orderCalculator.test.js
exit /b %ERRORLEVEL%
