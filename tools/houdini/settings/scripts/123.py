# pylint disable: C0103:invalid-name

"""
Houdini Startup scripts
"""

import hou

# Create Camera - 1080
def create_camera():
    """
    Creates a basic camera object
    """
    node = hou.node("/obj").createNode("cam", "cam_1080")
    node.setParms({"resx": 1920, "resy": 1080})
    node.setDisplayFlag(False)

# Create Mantra - PBR driver
def mantra_driver():
  node = hou.node("/out")
  out = node.createNode("ifd")
  out.setParms({"vm_renderengine": "pbrraytrace", "override_camerares": True, "camera": "/obj/cam_1080"})

def create_geo():
    """
    Creates the basic geometry nodes required
    """
    geo = hou.node("/obj").createNode("geo", "GEO")
    # geo.moveToGoodPosition()
    geo.setDisplayFlag(True)


def organize_layout():
    # Get the OBJ level
    obj_level = hou.node("/obj")

    # Get all nodes at the OBJ level
    all_nodes = obj_level.children()

    if not all_nodes:
        print("No nodes found at the OBJ level.")
        return

    # Get the number of nodes to arrange
    num_nodes = len(all_nodes)

    # Specify the number of columns and rows (both set to n)
    # Square root to get a square layout, you can adjust this based on your preference
    n = int(num_nodes**0.5)
    num_columns = n
    # num_rows = n

    # Set the initial position
    x_position = 0
    y_position = 0

    # Iterate through all nodes at the OBJ level and set their positions
    for i, node in enumerate(all_nodes):
        node.setPosition(hou.Vector2(x_position, y_position))

        # Update the position for the next node
        x_position += 4  # Move by 4 units for the next column

        # If we reach the end of a row, reset the x-position and move to the next row
        if (i + 1) % num_columns == 0:
            x_position = 0
            y_position -= 4  # Move down by 4 units for the next row


def main():
    """
    Main function
    """
    create_camera()
    create_geo()
    mantra_driver()
    organize_layout()

if __name__ == '__main__':
    main()
