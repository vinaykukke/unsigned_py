#pylint: disable=W0311

"""
Wrapper to run Houdini with custom environment
"""

import os
import subprocess
import sys

def run_houdini():
	"""
	Runs the custom instance of houdini defined for Unsigned Studios
	"""

	# Set path to Houdini executable
	houdini = '/Applications/Houdini/Houdini19.5.716/Houdini Apprentice 19.5.716.app/Contents/MacOS/happrentice'
	# Get the path to PIPELINE folder
	root_pipe_line = os.path.dirname(__file__).replace('\\','/')
	# Add path to custom python tools
	os.environ['PYTHONPATH'] = f"{root_pipe_line}/tools;&"
	# Create environment variable pointing to a pipeline folder
	os.environ['ROOT_PIPELINE'] = root_pipe_line
	# Set root of houdini project
	os.environ['JOB'] = f"{os.path.dirname(os.path.dirname(__file__))}/3D/"

	# Run Houdini
	with subprocess.Popen(houdini) as process:
		process.wait()
	print("Houdini has finished running. Exiting the script.")
	# Exit the script with a successful status code
	sys.exit(0)

def build_folder_structure(assets, shots):
	"""
	Create list for project folder structure

	@param ASSETS: list of Asset folders ['characters', ['roma', []]]
	@param SHOTS:  list of Sequences/Shot folders
	@return: Returns a list representing the folder structure.
	"""

    # Types structure
	types = [
		['ASSETS', assets],
		['SHOTS', shots]
	]

	# Folders structure
	folders = [
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
			['COMP', shots],
			['RENDER', shots]
		]],
		['3D', [
			['lib', [
			['ANIMATION', []],
			['MATERIALS', [
				['MANTRA', []]
			]]
			]],
			['fx', types],
			['caches', types],
			['hda', [
			['ASSETS', assets],
			['FX', types],
			]],
			['render', shots],
			['scenes', [
			['ASSETS', assets],
			['SHOTS', [
				['ANIMATION', shots],
				['RENDER', shots]
			]]
			]],
			['textures', types],
		]],
		]]
	]

	return folders

# Run our custom houdini instance
# Executed when invoked directly
if __name__ == "__main__":
	run_houdini()
