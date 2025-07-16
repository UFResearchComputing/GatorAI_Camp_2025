@echo off
REM Batch script to set up the conda environment
REM Run this script from the project root directory

setlocal enabledelayedexpansion

echo.
echo ===========================================
echo  GatorAI Camp 2025 - Conda Environment Setup
echo ===========================================
echo.

REM Check if conda is installed
where conda >nul 2>nul
if %errorlevel% neq 0 (
    echo [WARNING] Conda is not found in PATH
    echo.
    echo Attempting to find conda in common installation locations...
    
    REM Check common miniconda locations
    set "conda_found="
    
    REM Check each path individually
    if exist "%USERPROFILE%\AppData\Local\miniconda3\Scripts\conda.exe" (
        set "conda_found=%USERPROFILE%\AppData\Local\miniconda3\Scripts\conda.exe"
        echo [INFO] Found conda at: !conda_found!
        goto :conda_found
    )
    
    if exist "%USERPROFILE%\miniconda3\Scripts\conda.exe" (
        set "conda_found=%USERPROFILE%\miniconda3\Scripts\conda.exe"
        echo [INFO] Found conda at: !conda_found!
        goto :conda_found
    )
    
    if exist "%USERPROFILE%\Miniconda3\Scripts\conda.exe" (
        set "conda_found=%USERPROFILE%\Miniconda3\Scripts\conda.exe"
        echo [INFO] Found conda at: !conda_found!
        goto :conda_found
    )
    
    if exist "C:\miniconda3\Scripts\conda.exe" (
        set "conda_found=C:\miniconda3\Scripts\conda.exe"
        echo [INFO] Found conda at: !conda_found!
        goto :conda_found
    )
    
    if exist "C:\Miniconda3\Scripts\conda.exe" (
        set "conda_found=C:\Miniconda3\Scripts\conda.exe"
        echo [INFO] Found conda at: !conda_found!
        goto :conda_found
    )
    
    if exist "%USERPROFILE%\anaconda3\Scripts\conda.exe" (
        set "conda_found=%USERPROFILE%\anaconda3\Scripts\conda.exe"
        echo [INFO] Found conda at: !conda_found!
        goto :conda_found
    )
    
    if exist "%USERPROFILE%\Anaconda3\Scripts\conda.exe" (
        set "conda_found=%USERPROFILE%\Anaconda3\Scripts\conda.exe"
        echo [INFO] Found conda at: !conda_found!
        goto :conda_found
    )
    
    if exist "C:\anaconda3\Scripts\conda.exe" (
        set "conda_found=C:\anaconda3\Scripts\conda.exe"
        echo [INFO] Found conda at: !conda_found!
        goto :conda_found
    )
    
    if exist "C:\Anaconda3\Scripts\conda.exe" (
        set "conda_found=C:\Anaconda3\Scripts\conda.exe"
        echo [INFO] Found conda at: !conda_found!
        goto :conda_found
    )
    
    echo [ERROR] Conda not found in common locations
    echo.
    echo Please ensure conda is installed and either:
    echo 1. Add conda to your PATH environment variable
    echo 2. Run this script from the Anaconda/Miniconda prompt
    echo 3. Install Miniconda from: https://docs.conda.io/en/latest/miniconda.html
    echo.
    echo Common installation locations checked:
    echo    %USERPROFILE%\AppData\Local\miniconda3\Scripts\conda.exe
    echo    %USERPROFILE%\miniconda3\Scripts\conda.exe
    echo    %USERPROFILE%\Miniconda3\Scripts\conda.exe
    echo    C:\miniconda3\Scripts\conda.exe
    echo    C:\Miniconda3\Scripts\conda.exe
    echo    %USERPROFILE%\anaconda3\Scripts\conda.exe
    echo    %USERPROFILE%\Anaconda3\Scripts\conda.exe
    echo    C:\anaconda3\Scripts\conda.exe
    echo    C:\Anaconda3\Scripts\conda.exe
    pause
    exit /b 1
    
    :conda_found
    echo [DEBUG] conda_found variable: !conda_found!
    
    REM Extract the base conda directory
    for %%i in ("!conda_found!") do set "conda_base=%%~dpi"
    set "conda_base=!conda_base:~0,-9!"
    echo [DEBUG] conda_base directory: !conda_base!
    
    REM Try conda.bat first (more reliable)
    if exist "!conda_base!Scripts\conda.bat" (
        set "conda_cmd="!conda_base!Scripts\conda.bat""
        echo [DEBUG] Using conda.bat: !conda_cmd!
    ) else (
        set "conda_cmd="!conda_found!""
        echo [DEBUG] Using conda.exe: !conda_cmd!
    )
    
    REM Add conda Scripts to PATH temporarily
    set "PATH=!conda_base!Scripts;!conda_base!;!PATH!"
    echo [DEBUG] Updated PATH with conda directories
    
    REM Initialize conda first before using it
    echo [INFO] Running conda init...
    "!conda_found!" init >nul 2>&1
    if %errorlevel% neq 0 (
        echo [WARNING] conda init failed, but continuing...
    ) else (
        echo [DEBUG] conda init successful
    )
) else (
    set "conda_cmd=conda"
)

REM Show conda version
echo [INFO] Testing conda at: !conda_cmd!
call !conda_cmd! --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Found conda but cannot execute it
    echo [DEBUG] Tried to execute: !conda_cmd!
    echo [DEBUG] Attempting alternative execution methods...
    
    REM Try different execution methods if conda_found is set
    if defined conda_found (
        REM Method 1: Try with python -m conda
        "!conda_base!python.exe" -m conda --version >nul 2>&1
        if %errorlevel% equ 0 (
            set "conda_cmd="!conda_base!python.exe" -m conda"
            echo [DEBUG] Success with python -m conda method
            goto :conda_working
        )
        
        REM Method 2: Try with cmd /c
        cmd /c "!conda_found!" --version >nul 2>&1
        if %errorlevel% equ 0 (
            set "conda_cmd=cmd /c "!conda_found!""
            echo [DEBUG] Success with cmd /c method
            goto :conda_working
        )
        
        REM Method 3: Try conda.bat directly
        for %%i in ("!conda_found!") do set "conda_base=%%~dpi"
        set "conda_base=!conda_base:~0,-9!"
        if exist "!conda_base!Scripts\conda.bat" (
            call "!conda_base!Scripts\conda.bat" --version >nul 2>&1
            if %errorlevel% equ 0 (
                set "conda_cmd="!conda_base!Scripts\conda.bat""
                echo [DEBUG] Success with conda.bat method
                goto :conda_working
            )
        )
        
        REM Method 4: Try from conda base directory
        pushd "!conda_base!"
        call Scripts\conda.bat --version >nul 2>&1
        if %errorlevel% equ 0 (
            set "conda_cmd=!conda_base!Scripts\conda.bat"
            popd
            echo [DEBUG] Success with base directory method
            goto :conda_working
        )
        popd
        
        echo [ERROR] All execution methods failed
        echo [DEBUG] Conda found at: !conda_found!
        echo [DEBUG] Conda base: !conda_base!
        echo.
        echo [SOLUTION] Please try one of these alternatives:
        echo 1. Run this script from the Anaconda/Miniconda prompt
        echo 2. Or manually run: conda init cmd.exe
        echo 3. Or restart your command prompt after conda installation
        pause
        exit /b 1
    ) else (
        pause
        exit /b 1
    )
)

:conda_working
for /f "tokens=*" %%i in ('call !conda_cmd! --version') do set conda_version=%%i
echo [INFO] Found conda: !conda_version!

REM Check if environment.yml exists
if not exist "environment.yml" (
    echo [ERROR] environment.yml not found in current directory
    pause
    exit /b 1
)

REM Check if environment already exists
call !conda_cmd! env list | findstr /C:"gaic" >nul
if %errorlevel% equ 0 (
    echo [WARNING] Environment 'gaic' already exists
    set /p choice="Do you want to remove and recreate it? (y/N): "
    if /i "!choice!"=="y" (
        echo [INFO] Removing existing environment...
        call !conda_cmd! env remove -n gaic -y
        if %errorlevel% neq 0 (
            echo [ERROR] Failed to remove environment
            pause
            exit /b 1
        )
    ) else (
        echo [INFO] Environment setup cancelled
        pause
        exit /b 0
    )
)

REM Create the environment
echo [INFO] Creating conda environment from environment.yml...
call !conda_cmd! env create -f environment.yml

if %errorlevel% neq 0 (
    echo [ERROR] Failed to create environment
    pause
    exit /b 1
)

echo.
echo [SUCCESS] Environment created successfully!
echo.
echo Next steps:
echo 1. Run the game: python main.py (using environment Python)
echo 2. Or use direct path: "C:\Users\magitz\AppData\Local\miniconda3\envs\gaic\python.exe" main.py
echo 3. Or use conda run: !conda_cmd! run -n gaic python main.py
echo 4. Or use activation script: .\activate-env.ps1
echo.
echo Note: conda activate requires 'conda init' - see CONDA_ACTIVATION_GUIDE.md
echo.
pause
