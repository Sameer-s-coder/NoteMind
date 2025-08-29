@echo off
echo NoteMind Token Manager - Installation Script
echo ===========================================
echo.

echo Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

echo.
echo Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo Testing installation...
python -c "from token_manager import TokenManager; print('Token Manager imported successfully!')"
if %errorlevel% neq 0 (
    echo ERROR: Token Manager import failed
    pause
    exit /b 1
)

echo.
echo Installation successful!
echo.
echo Available commands:
echo   python quick_start.py     - Interactive tutorial
echo   python examples.py        - Usage examples
echo   python token_cli.py       - Command line interface
echo   python test_token_manager.py - Run tests
echo.
echo Run 'python quick_start.py' to get started!
pause
