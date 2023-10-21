"""
Default set of helper methods
"""

import hou

def check_existing(geometry_name: str):
    """
    Checks for existing node's with the given name
    """
    node_exists = False
    # Check if exists
    if hou.node(f"/obj/{geometry_name}"):
        # Display fail message
        hou.ui.displayMessage(f"{geometry_name} already exists in the scene") # type: ignore
        node_exists = True

    return node_exists
