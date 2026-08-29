@echo off
setlocal
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0verify_order9_two_bad_no_hit.ps1" %*
exit /b %ERRORLEVEL%
