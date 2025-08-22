@echo off
REM Windows registration script for Qwen-Image MCP Server

echo ======================================
echo 🎨 Qwen-Image MCP Registration
echo ======================================

REM Get the directory where this script is located
set SCRIPT_DIR=%~dp0
set SERVER_PATH=%SCRIPT_DIR%qwen_image_mcp\server.py

REM Find Python executable
where python >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set PYTHON_CMD=python
) else (
    where python3 >nul 2>&1
    if %ERRORLEVEL% EQU 0 (
        set PYTHON_CMD=python3
    ) else (
        echo ❌ Python not found. Please install Python 3.10+
        pause
        exit /b 1
    )
)

echo ✅ Using Python: %PYTHON_CMD%
echo ✅ Server path: %SERVER_PATH%

REM Check if claude command exists
where claude >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ❌ 'claude' command not found.
    echo    Please ensure Claude Code is installed and in PATH
    pause
    exit /b 1
)

REM Remove existing registration if present
echo.
echo 📝 Removing any existing registration...
claude mcp remove qwen-image 2>nul

REM Register the server
echo 📝 Registering Qwen-Image server...
claude mcp add --scope user qwen-image "%PYTHON_CMD%" -- "%SERVER_PATH%"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✅ Successfully registered!
    echo.
    echo Next steps:
    echo 1. Restart Claude Code or run '/mcp' command
    echo 2. Generate images by asking Claude
    echo.
    echo Example prompts:
    echo   "Generate an image of a sunset"
    echo   "Create a portrait of a cat"
) else (
    echo ❌ Registration failed
    echo.
    echo Try manual registration:
    echo   claude mcp add --scope user qwen-image %PYTHON_CMD% -- %SERVER_PATH%
    pause
    exit /b 1
)

pause