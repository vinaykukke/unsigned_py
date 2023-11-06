@echo off
SETLOCAL

:: Define the correct directory path
set "unsigned_dir=C:\Users\vinaykukke\Documents\Work\unsigned_py"
set "hython=C:\Program Files\Side Effects Software\Houdini 19.5.368\bin\hython.exe"


:: Function to display usage information
:show_help
echo Usage: %~nx0 [command] [options]
echo Commands:
echo   init        Initialize the directory
echo   install     Install packages (e.g., "install hpip")
echo.
echo Options:
echo   -h, --help  Show this help message
goto :eof

:: The main unsigned CLI
:unsigned
if "%~1" == "" (
  echo Error: At least one argument is required.
  call :show_help
  exit /b 1
)

if /i "%~1" equ "-h" goto show_help
if /i "%~1" equ "--help" goto show_help
if /i "%~1" equ "init" call :init
if /i "%~1" equ "install" (
  if "%~2" == "" (
    echo Subcommand 'install' requires a package name (e.g., "install hpip")
    call :show_help
    exit /b 1
  )
  if /i "%~2" equ "hpip" (
    call :install_hpip %*
  ) else (
    echo "'%~2' is not a known subcommand" >&2
    call :show_help
    exit /b 1
  )
) else (
  echo "'%~1' is not a known command" >&2
  call :show_help
  exit /b 1
)
goto :eof

if "%~1"=="init" (
  call :init
) else (
  echo '%~1' is not a known command
  exit /b 1
)

exit /b 0

:: hpip is the Houdini Python package manager
:hpip
"%hython%" -m pip %*
goto :eof

:check
:: Check if the file exists in the current directory
if exist "%~1" (
  exit /b 1
) else (
  exit /b 0
)
goto :eof

:: The improved __install_hpip function
:install_hpip
call :check "get-pip.py"

if %errorlevel% equ 1 (
  echo PIP already exists!
  echo You can use it with the following command: hpip install numpy
) else (
  :: Check if the user is in the correct directory
  if "%CD%" neq "%unsigned_dir%" (
    echo You are not in the correct directory. Please move to: %unsigned_dir% and then install.
    exit /b 1
  ) else (
    echo Installing PIP in the Houdini environment...
    bitsadmin /transfer mydownload /download /priority normal https://bootstrap.pypa.io/get-pip.py "%~dp0get-pip.py"
    "%hython%" "%~dp0get-pip.py"
    echo All set! You can now use PIP in Houdini by calling: hpip
  )
)
goto :eof

:init
:: Move to the parent dir
cd ..
echo Initializing your directory!
:: Make an unsigned_projects directory
mkdir unsigned_projects
:: Call the PM script to initiate
zsh ./unsigned_py/project_manager.sh
goto :eof

endlocal
