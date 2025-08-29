@echo off
echo NoteMind Token Manager - Demo Runner
echo ===================================
echo.
echo Choose an option:
echo.
echo 1. Quick Start (Interactive Tutorial)
echo 2. Examples (All Features Demo)
echo 3. Command Line Interface
echo 4. Run Tests
echo 5. Exit
echo.
set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" (
    echo.
    echo Starting Quick Start Tutorial...
    python quick_start.py
) else if "%choice%"=="2" (
    echo.
    echo Running Examples...
    python examples.py
) else if "%choice%"=="3" (
    echo.
    echo Starting CLI...
    echo Type 'python token_cli.py --help' for usage information
    python token_cli.py --help
    echo.
    echo Example commands:
    echo   python token_cli.py --text "Hello world" --action analyze
    echo   python token_cli.py --action models
    echo   python token_cli.py --text "Your text here" --action check
) else if "%choice%"=="4" (
    echo.
    echo Running Tests...
    python -m unittest test_token_manager.py
) else if "%choice%"=="5" (
    echo Goodbye!
    exit /b 0
) else (
    echo Invalid choice. Please run the script again.
    pause
    exit /b 1
)

echo.
echo Demo completed!
pause
