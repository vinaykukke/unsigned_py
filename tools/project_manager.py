# Wrapper to run Houdini with custom environment
import os, subprocess, sys

def run_houdini():
  # Set path to Houdini executable
  houdini = '/Applications/Houdini/Houdini19.5.716/Houdini Apprentice 19.5.716.app/Contents/MacOS/happrentice'

  # SETUP PROJECT ENVIRONMENT
  # Get the path to PIPELINE folder
  rootPipeline = os.path.dirname(__file__).replace('\\','/')
  # Add path to custom python tools
  os.environ['PYTHONPATH'] = '{}/tools;&'.format(rootPipeline)
  # Create environment variable pointing to a pipeline folder
  os.environ['ROOT_PIPELINE'] = rootPipeline
  # Set root of houdini project
  os.environ['JOB'] = '{}/3D/'.format(os.path.dirname(os.path.dirname(__file__)))

  # Run Houdini
  process = subprocess.Popen(houdini)
  process.wait()
  print("Houdini has finished running. Exiting the script.")
  sys.exit(0)  # Exit the script with a successful status code

def build_folder_structure(self, ASSETS, SHOTS):
  """
    Create list for project folder structure

    @param ASSETS: list of Asset folders ['characters', ['roma', []]]
    @param SHOTS:  list of Sequences/Shot folders
    @return: Returns a list representing the folder structure.
  """

  # PROJECT FOLDER STRUCTURE

  # Types structure
  TYPES = [
    ['ASSETS', ASSETS],
    ['SHOTS', SHOTS]
  ]

  # Folders structure
  FOLDERS = [
    ['EDIT', [
      ['OUT', []],
      ['PROJECT', []]
    ]],
    ['PREP', [
      ['ART', []],
      ['SRC', []],
      ['PIPELINE', []],
    ]],
    ['PROD', [
      ['2D', [
        ['COMP', SHOTS],
        ['RENDER', SHOTS]
      ]],
      ['3D', [
        ['lib', [
          ['ANIMATION', []],
          ['MATERIALS', [
              ['MANTRA', []]
          ]]
        ]],
        ['fx', TYPES],
        ['caches', TYPES],
        ['hda', [
          ['ASSETS', ASSETS],
          ['FX', TYPES],
        ]],
        ['render', SHOTS],
        ['scenes', [
          ['ASSETS', ASSETS],
          ['SHOTS', [
            ['ANIMATION', SHOTS],
            ['RENDER', SHOTS]
          ]]
        ]],
        ['textures', TYPES],
      ]],
    ]]
  ]

  return FOLDERS

# Run our custom houdini instance
# Executed when invoked directly
if __name__ == "__main__":
  run_houdini()