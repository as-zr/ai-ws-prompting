@echo off
call "%~dp0exercises\run-tests.bat" %*
exit /b %ERRORLEVEL%
