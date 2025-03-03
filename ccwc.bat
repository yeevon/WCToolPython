@echo off
setlocal enabledelayedexpansion

REM Initialize variables
set FILE_PATH=""
set ARGUMENTS=""

REM Loop through all provided arguments
for %%A in (%*) do (
    if exist "%%A" (
        set "FILE_PATH=%%~fA"  REM Convert file path to absolute
    ) else (
        if "ARGUMENTS"=="" (
            set "ARGUMENTS=%%A"
        ) else (
            set "ARGUMENTS=!ARGUMENTS! %%A"
        )
    )
)

REM Debugging output (uncomment to check values)
REM echo !ARGUMENTS!

REM Change to the script directory
cd /d "%~dp0"

REM Run Python script with correctly formatted arguments
if not "!FILE_PATH!"=="" (
    "venv\Scripts\python.exe" "ccwc.py" !ARGUMENTS! "!FILE_PATH!"
) else (
    "venv\Scripts\python.exe" "ccwc.py" !ARGUMENTS!
)

endlocal
