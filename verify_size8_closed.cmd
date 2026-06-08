@echo off
cd /d "%~dp0"
powershell.exe -ExecutionPolicy Bypass -File "%~dp0verify_size8_closed.ps1"
set "status=%ERRORLEVEL%"
echo.
if not "%status%"=="0" echo Size-8 verification failed. Review the error above.
echo Press any key to close this window.
pause > nul
exit /b %status%
