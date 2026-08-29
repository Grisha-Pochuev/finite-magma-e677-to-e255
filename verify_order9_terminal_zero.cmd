@echo off
setlocal
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0verify_order9_terminal_zero.ps1" %*
exit /b %ERRORLEVEL%
