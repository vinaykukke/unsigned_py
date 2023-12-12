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
    # Get all nodes in the "/obj" context
    obj_context = hou.node("/obj")

    # Get all cameras in the scene
    cameras = [node for node in obj_context.children() if node.type().name() == "cam"]

    # if there is no camera add one
    if len(cameras) == 0:    
        node = hou.node("/obj").createNode("cam", "cam_1080")
        node.setParms({"resx": 1920, "resy": 1080})
        node.setDisplayFlag(False)

# Create Mantra - PBR driver
def mantra_driver():
    """
    Check and place drivers
    """
    node = hou.node("/out/idf")

    if node is None:
        node = hou.node("/out").createNode("ifd")
        node.setParms({"vm_renderengine": "pbrraytrace",
                "override_camerares": True, "camera": "/obj/cam_1080"})

def organize_layout():
    # Get the OBJ level
    obj_level = hou.node("/obj")

    # Get all nodes at the OBJ level
    all_nodes = obj_level.children()

    if not all_nodes:
        print("No nodes found at the OBJ level.")
        return

    # Separate connected and unconnected nodes
    connected_nodes = []
    unconnected_nodes = []

    for node in all_nodes:
        if node.inputConnections() or node.outputConnections():
            connected_nodes.append(node)
        else:
            unconnected_nodes.append(node)

    # Function to arrange nodes vertically and then horizontally
    def arrange_unconnected_nodes(nodes, num_columns, start_position):
        # Set the initial position
        x_position = start_position[0]
        y_position = start_position[1]

        # Iterate through nodes and set their positions
        for i, node in enumerate(nodes):
            node.setPosition(hou.Vector2(x_position, y_position))

            # Update the position for the next node
            y_position -= 2.5  # Move down by 2 units for the next row

            # If we reach the end of a column, reset the y-position and move to the next column
            if (i + 1) % num_columns == 0:
                y_position = start_position[1]
                x_position += 2.5  # Move right by 2 units for the next column

    # Specify the number of columns and rows (both set to n)
    # Square root to get a square layout, you can adjust this based on your preference
    n = int(len(all_nodes)**0.5)
    num_columns = n

    # Arrange unconnected nodes on the right
    start_position_unconnected = (4 * num_columns, 0)
    arrange_unconnected_nodes(unconnected_nodes, num_columns, start_position_unconnected)

def main():
    """
    Main function
    """
    create_camera()
    mantra_driver()
    organize_layout()

if __name__ == '__main__':
    main()
