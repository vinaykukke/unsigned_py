import hou

# Define geometry node name
name = 'MY_GEO'

def checkExisting(geometryName):
  # Check if "MY_GEO" exists
  if hou.node('/obj/{}'.format(geometryName)):
    # Display fail message
    hou.ui.displayMessage('{} already exists in the scene'.format(geometryName))
    return True
    

def createGeoNode(geometryName = "test"):
  # Get scene root node
  sceneRoot = hou.node('/obj/')
  # Create empty geometry node in scene root
  geometry = sceneRoot.createNode('geo', run_init_scripts=False)
  # Set geometry node name
  geometry.setName(geometryName)
  # Display creation message
  hou.ui.displayMessage('{} node created!'.format(geometryName))

# Execute node creation 
if checkExisting(name) != True:
  createGeoNode(name)