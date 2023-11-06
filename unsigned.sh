#! /bin/zsh

# Define the correct directory path
unsigned_dir="/Users/vinaykukke/Documents/Work/unsigned_py"
hython="/Applications/Houdini/Houdini19.5.716/Frameworks/Houdini.framework/Versions/19.5/Resources/bin/hython"

# The main unsigned CLI
function unsigned() {
  if [ "$#" -lt 1 ]; then
    echo "Error: At least one argument is required."
  fi

  if [ $1 = "init" ]; 
  then
    __init
  elif [ $1 = "install" ]; 
  then
    if [ $2 = "hpip" ]; then
      __check $2
      pip_exists=$?

      if [ $pip_exists -eq 1 ]; then
        echo "PIP already exists!"
        echo "You can use it with the following command: hpip install numpy"
      else
        __pip
      fi
    else
      echo "'$2' is not a known command" >&2
    fi
  else
    # Show a helpful error
    echo "'$1' is not a known command" >&2
  fi
}

# hpip is the houdini python package manager
function hpip() {
  $hython -m pip $@
}

function __init() {
  # Move to the parent dir
  cd ../
  echo 'Initializing your directory!'
  # Make a unsigned_project directory
  mkdir unsigned_projects
  # Call the PM script to initiate
  zsh ./unsigned_py/project_manager.sh
}

function __pip() {
   # Check if the user is in the correct directory
  if [ "$PWD" != "$unsigned_dir" ]; then
    echo "You are not in the correct directory. Please move to: $unsigned_dir and then install!"
    exit 1
  else
    echo "Installing PIP in the houdini environament..."
    curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    $hython ./get-pip.py
    echo "All set! You can now use PIP in houdini by calling: hpip"
  fi
}

function __check() {
  # Check if the "get-pip.py" file exists in the current directory
  if [ -e "get-pip.py" ]; then
    return 1
  else
    return 0
  fi
}

"$@"