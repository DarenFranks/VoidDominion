@echo off
REM Void Dominion - Quick Launch
REM Simple launcher for the game

cd /d %~dp0

REM Try python first, then python3
python gui.py 2>NUL
if %ERRORLEVEL% NEQ 0 (
    python3 gui.py
)

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Python not found or dependencies not installed!
    echo.
    echo Please run install.bat first
    echo.
    pause
)
