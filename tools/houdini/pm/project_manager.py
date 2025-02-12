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
	houdini = "/Applications/Houdini/Houdini19.5.716/Houdini Apprentice 19.5.716.app/Contents/MacOS/happrentice"
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

def build_asset_folders(project_assets):
	"""
	Build sequences/shots folder structure list
	:return:
	"""
	assets = []

	for asset in project_assets:
		folder = [f"{asset}s", [[asset, []]]]
		assets.append(folder)

	return assets

def create_folder(path):
	"""
	Create folder at input path
	:param path: Path to create folder (C:/TEMP)
	"""

	if not os.path.exists(path):
		os.makedirs(path)

def create_folders(folders_template, root = os.environ["UN_ROOT"]):
	"""
	Recursively build folder structure based on template
	:param root: Root directory to create folder structure
	:param folders_template: List of lists, folder structure template
	:return:
	"""

	if folders_template:
		for folder in folders_template:
			folder_name = folder[0]
			path = f"{root}/{folder_name}"
			create_folder(path)
			create_folders(folder[1], path)

def build_folder_structure():
	"""
	Create list for project folder structure

	@param ASSETS: list of Asset folders ['characters', ['roma', []]]
	@param SHOTS:  list of Sequences/Shot folders
	@return: Returns a list representing the folder structure.
	"""

	print("Building the folder structure...")

	# Folders structure
	folders = [
		['PREP', [
		['ART', []],
		['SRC', []],
		['PIPELINE', []],
		]],
		['PROD', [
		['2D', [
			['COMP', []],
			['RENDER', []]
		]],
		['3D', [
			['lib', [
			['Animation', []],
			['Materials', []]
			]],
			['fx', []],
			['caches', []],
			['Assets', []],
			['hda', []],
			['render', []],
			['scenes', [
			['Assets', []],
			['Shots', [
				['Animation', []],
				['Render', []]
			]]
			]],
			['textures', []],
		]],
		]]
	]

	return folders

def create_project_template():
	"""
	Create folder structure on HDD
	@param project: project object
	@return None
	"""
	# Build folders list
	folders = build_folder_structure()
	# Create folders on HDD
	print("Creating the folders...")
	create_folders(folders)
	print("You are all set!")

# Run our custom houdini instance
# Executed when invoked directly
if __name__ == "__main__":
	create_project_template()
