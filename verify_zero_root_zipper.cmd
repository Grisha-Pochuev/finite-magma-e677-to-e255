@echo off
setlocal
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0verify_zero_root_zipper.ps1" %*
exit /b %ERRORLEVEL%
