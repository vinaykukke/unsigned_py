#pylint: disable=W0311

"""
Creates the correct folder structure for a new Unsigned Studio project
"""
import os
import hou

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

# def build_shot_folders(project):
# 	"""
# 	Build sequences/shots folder structure list
# 	:return:
# 	"""

# 	shots = []

# 	# Get sequences
# 	eve_data.get_project_sequences(project)

# 	for sequence in eve_data.project_sequences:

# 		# Get shots
# 		eve_data.get_sequence_shots(sequence.id)
# 		if eve_data.sequence_shots:
# 			for shot in eve_data.sequence_shots:
# 				folder = [sequence.name, [[shot.name, []]]]
# 				shots.append(folder)
# 		else:
# 			# If there is no shots in the sequence
# 			shots.append([sequence.name, []])

# 	return shots
def create_folder(path):
	"""
	Create folder at input path
	:param path: Path to create folder (C:/TEMP)
	"""

	if not os.path.exists(path):
		os.makedirs(path)

def create_folders(folders_template, root = hou.getenv('JOB')):
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

def build_folder_structure(assets):
	"""
	Create list for project folder structure

	@param ASSETS: list of Asset folders ['characters', ['roma', []]]
	@param SHOTS:  list of Sequences/Shot folders
	@return: Returns a list representing the folder structure.
	"""

    # Types structure
	types = [
		['ASSETS', assets],
		# ['SHOTS', shots]
	]

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
			['render', []],
			['scenes', [
			['ASSETS', assets],
			['SHOTS', [
				['ANIMATION', []],
				['RENDER', []]
			]]
			]],
			['textures', types],
		]],
		]]
	]

	return folders

def create_project():
	"""
	Create folder structure on HDD
	@param project: project object
	@return None
	"""
	# Build lists for assets and sequences/shots
	asset_folders = build_asset_folders(["Characters"])
	# cwd = os.path.dirname(os.path.realpath(__file__))
	# shot_folders = build_shot_folders(project)
	# Build folders list
	folders = build_folder_structure(asset_folders)
	# Create folders on HDD
	create_folders(folders)
