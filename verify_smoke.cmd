@echo off
cd /d "%~dp0"
powershell.exe -ExecutionPolicy Bypass -File "%~dp0verify_smoke.ps1"
echo.
echo Press any key to close this window.
pause > nul
