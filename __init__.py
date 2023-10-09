"""
Unsigned Studios custom settings
"""

import hou

# Define geometry node name
NAME = 'MY_GEO'

def check_existing(geometry_name):
    """
    Checks for existing node's with the given name
    """
    node_exists = False
    # Check if "MY_GEO" exists
    if hou.node(f"/obj/{geometry_name}"):
        # Display fail message
        hou.ui.displayMessage(f"{geometry_name} already exists in the scene")
        node_exists = True
    return node_exists

def create_geo_node(geometry_name = "test"):
    """
    Creates a new node with a given name
    """
    # Get scene root node
    scene_root = hou.node('/obj/')
    # Create empty geometry node in scene root
    geometry = scene_root.createNode('geo', run_init_scripts=False)
    # Set geometry node name
    geometry.setName(geometry_name)
    # Display creation message
    hou.ui.displayMessage(f"{geometry_name} node created!")

# Execute node creation s
if check_existing(NAME) is not True:
    create_geo_node(NAME)
