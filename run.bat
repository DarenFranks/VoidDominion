@echo off
REM Void Dominion - Quick Launch
REM Simple launcher for the game

echo ================================================
echo           VOID DOMINION
echo ================================================
echo.
echo Starting game...
echo.

cd /d %~dp0

REM Try python first, then python3
python gui.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Trying python3...
    python3 gui.py
)

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Failed to launch game!
    echo.
    echo Please run install.bat first if you haven't already
    echo.
    pause
)
