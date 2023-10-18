#! /bin/zsh

# prints the input
function init() {
  # Move to the parent dir
  cd ../
  echo 'Initializing your directory!'
  # Make a unsigned_project directory
  mkdir unsigned_projects
  # Call the PM script to initiate
  zsh ./unsigned_py/project_manager.sh
}

# Check if the function exists (bash specific)
if declare -f "$1" > /dev/null
then
  # call arguments verbatim
  "$@"
else
  # Show a helpful error
  echo "'$1' is not a known function name" >&2
  exit 1
fi