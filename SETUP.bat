@echo off
REM Get Better - Setup and Run Script for Windows
REM Run this script: SETUP.bat

echo.
echo 🚀 Get Better - Setup Script
echo ================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

echo ✅ Python found
python --version
echo.

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo 🔌 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📥 Installing dependencies...
pip install -r requirements.txt

REM Create database
echo 💾 Setting up database...
python app.py >nul 2>&1 &
timeout /t 2 /nobreak >nul 2>&1

echo.
echo ================================
echo ✅ Setup Complete!
echo ================================
echo.
echo 🎯 Next Steps:
echo.
echo 1. Activate virtual environment (if needed)
echo    venv\Scripts\activate.bat
echo.
echo 2. Run the application
echo    python app.py
echo.
echo 3. Open in browser
echo    http://localhost:5000
echo.
echo 4. Test it out!
echo    - Sign up with test@example.com / password123
echo    - Select multiple goals
echo    - View your personalized plans
echo.
echo 📚 For more info, read QUICKSTART.md
echo.
pause
