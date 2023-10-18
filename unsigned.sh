#! /bin/zsh

function unsigned() {
  if [ "$#" -lt 1 ]; then
    echo "Error: At least one argument is required."
    exit 1
  fi

  if [ $1 = "init" ]; 
  then
    __init
  else
    # Show a helpful error
    echo "'$1' is not a known command" >&2
    exit 1
  fi
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

"$@"