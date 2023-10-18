@echo off
SETLOCAL

:unsigned
if "%~1"=="" (
  echo Error: At least one argument is required.
  exit /b 1
)

if "%~1"=="init" (
  call :init
) else (
  echo '%~1' is not a known command
  exit /b 1
)

exit /b 0

:init
cd ..
echo Initializing your directory!
mkdir unsigned_projects
call "%CD%\unsigned_py\project_manager.bat"
exit /b
