#!/bin/bash

# Define the correct directory path
unsigned_dir="/Users/vinaykukke/Documents/Work/unsigned_py"
hython="/Applications/Houdini/Houdini19.5.716/Frameworks/Houdini.framework/Versions/19.5/Resources/bin/hython"

# Function to display usage information
show_help() {
  echo "Usage: $0 [command] [options]"
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
    show_help
    exit 1
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
            echo "'$2' is not a known subcommand" >&2
            show_help
            exit 1
            ;;
        esac
      else
        echo "Subcommand 'install' requires a package name (e.g., 'install hpip')" >&2
        show_help
        exit 1
      fi
      ;;
    *)
      echo "'$1' is not a known command" >&2
      show_help
      exit 1
      ;;
  esac
}

# hpip is the Houdini Python package manager
function __install_hpip() {
  # Check if the user is in the correct directory
  if [ "$PWD" != "$unsigned_dir" ]; then
    echo "You are not in the correct directory. Please move to: $unsigned_dir and then install."
    exit 1
  else
    echo "Installing PIP in the Houdini environment..."
    curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    $hython ./get-pip.py
    echo "All set! You can now use PIP in Houdini by calling: hpip"
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
