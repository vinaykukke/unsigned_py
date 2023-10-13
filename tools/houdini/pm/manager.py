#pylint: disable=W0311

"""
Creates the correct folder structure for a new Unsigned Studio project
"""

def create_project():
	"Test"
	print("This is working => New comment")

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
