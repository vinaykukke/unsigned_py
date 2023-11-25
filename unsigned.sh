#!/bin/bash

# Define the correct directory path
unsigned_dir="/Users/vinaykukke/Documents/Work/unsigned_py"
hython="/Applications/Houdini/Houdini20.0.506/Frameworks/Houdini.framework/Versions/20.0/Resources/bin/hython"

# Function to display usage information
show_help() {
  echo "Usage: unsigned [command] [options]"
  echo "Commands:"
  echo "  init        Initialize the directory"
  echo "  install     Install packages (e.g., 'install hpip')"
  echo ""
  echo "HPIP Commands:"
  echo "  NOTE:       You can use 'hpip' exactly like you would use regular pip"
  echo "  install     Install packages inside the houdini environment (e.g., 'hpip install numpy')"
  echo ""
  echo "Options:"
  echo "  -h, --help  Show this help message"
}

# The main unsigned CLI
unsigned() {
  if [ "$#" -lt 1 ]; then
    echo "Error: At least one argument is required."
    echo -e "\033[1;31mError: At least one argument is required.033[0m"
    show_help
    # exit 1
  fi

  case "$1" in
    -h|--help)
      show_help
      ;;
    init)
      __init
      ;;
    install)
      if [ -n "$2" ]; then
        case "$2" in
          hpip)
            __install_hpip
            ;;
          *)
            echo -e "\033[1;31m'$2' is not a known subcommand\033[0m" >&2
            show_help
            # exit 1
            ;;
        esac
      else
        echo -e "\033[1;31mSubcommand 'install' requires a package name (e.g., 'install hpip')\033[0m" >&2
        show_help
        # exit 1
      fi
      ;;
    *)
      echo -e "\033[1;31m'$1' is not a known command\033[0m" >&2
      show_help
      # exit 1
      ;;
  esac
}


# hpip is the Houdini Python package manager
hpip() {
  $hython -m pip "$@"
}

# Check if the "get-pip.py" file exists in the current directory
__check() {
  if [ -e "$1" ]; then
    return 1
  else
    return 0
  fi
}

# hpip is the Houdini Python package manager
function __install_hpip() {
  __check "get-pip.py"

  if [ $? -eq 1 ]; then
    echo "PIP already exists!"
    echo -e "\033[1;32mYou can use it with the following command: hpip install numpy\033[0m"
    # exit 0
  else
    # Check if the user is in the correct directory
    if [ "$PWD" != "$unsigned_dir" ]; then
      echo -e "\033[1;31mYou are not in the correct directory. Please move to: $unsigned_dir and then install.\033[0m"
      # exit 1
    else
      echo "Installing PIP in the Houdini environment..."
      curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py
      $hython ./get-pip.py
      echo -e "\033[1;32mAll set! You can now use PIP in Houdini by calling: hpip\033[0m"
    fi
  fi
}

function __init() {
  # Move to the parent dir
  cd ..
  echo 'Initializing your directory!'
  # Make an unsigned_projects directory
  mkdir unsigned_projects
  # Call the PM script to initiate
  zsh ./unsigned_py/project_manager.sh
}

# Call the main unsigned function with command line arguments
"$@"
