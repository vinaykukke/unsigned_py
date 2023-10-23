@echo off
SETLOCAL

:: Define the correct directory path
set "unsigned_dir=C:\Users\vinaykukke\Documents\Work\unsigned_py"

:: The main unsigned CLI
:unsigned
if "%~1"=="" (
  echo Error: At least one argument is required.
  exit /b 1
)

if "%~1"=="init" (
  call :init
) else if "%~1"=="install" (
  call :check %2
  if !errorlevel! == 1 (
    echo PIP already exists!
    echo You can use it with the following command: hpip install numpy
    exit /b 0
  ) else (
    call :pip
  )
) else (
  echo '%~1' is not a known command
  exit /b 1
)
exit /b 0

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


:: hpip is the houdini python package manager
:hpip
C:\Program Files\Side Effects Software\Houdini 19.5.368\bin\hython.exe -m pip %*
exit /b 0

:pip
:: Check if the user is in the correct directory
if "%CD%" neq "!unsigned_dir!" (
  echo You are not in the correct directory. Please move to: !unsigned_dir! and then install!
  exit /b 1
) else (
  echo Installing PIP in the houdini environment...
  curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  C:\Applications\Houdini\Houdini19.5.716\Frameworks\Houdini.framework\Versions\19.5\Resources\bin\hython get-pip.py
  echo All set! You can now use PIP in Houdini by calling: hpip
  exit /b 0
)

:check
:: Check if the file exists in the current directory
if exist "%~1" (
  exit /b 1
) else (
  exit /b 0
)
