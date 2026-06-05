@echo off
cd /d "%~dp0"
powershell.exe -ExecutionPolicy Bypass -File "%~dp0verify_size8_closed.ps1"
echo.
echo Press any key to close this window.
pause > nul
