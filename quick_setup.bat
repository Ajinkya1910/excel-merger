@echo off
REM Quick Setup Script for Windows
REM Run: quick_setup.bat

echo 🚀 Excel Merger - Quick Setup
echo ================================

REM Check Python
echo ✓ Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install from python.org
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo   Python %PYTHON_VERSION% found ✓

REM Create virtual environment
echo.
echo ✓ Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo ✓ Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo.
echo ✓ Upgrading pip...
python -m pip install --upgrade pip >nul 2>&1

REM Install dependencies
echo ✓ Installing dependencies...
pip install -r requirements.txt >nul 2>&1

echo.
echo ================================
echo ✅ Setup Complete!
echo ================================
echo.
echo To start the app, run:
echo.
echo   venv\Scripts\activate
echo   streamlit run app.py
echo.
echo Then open: http://localhost:8501
echo.
pause
