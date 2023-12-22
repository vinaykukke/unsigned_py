import hou
import sys
from enum import Enum

class Paths(Enum):
    ASSET = hou.node(".").path()

class Parameters(Enum):
    SKIN = hou.parm(f"{Paths.ASSET.value}/merge_skin").eval()
    CURVES = hou.parm(f"{Paths.ASSET.value}/merge_curves").eval()
    ANIMATED_SKIN = hou.parm(f"{Paths.ASSET.value}/merge_animated_skin").eval()

def check():
    if (hasattr(hou.session, 'un_ft_attributes_created')): # type: ignore
        created = hou.session.un_ft_attributes_created  # type: ignore
        if (created):
            hou.ui.displayMessage("All the attributes have already been created!!")  # type: ignore
            sys.exit()
    else:
        eagle = hou.node(Parameters.SKIN.value).parent()
        for child in eagle.children():
            if (child.name() == "OUT_eagle"):
                hou.ui.displayMessage(
                    "All the attributes have already been created!!")  # type: ignore
                sys.exit()

def create():
    # Check if all the attributes have been created and only then proceed
    check()

    # Create attributes
    skin_path = hou.node(Parameters.SKIN.value).parent().path()
    # Create a null node
    null_node = hou.node(skin_path).createNode("null", "OUT_eagle")
    # Attributes
    painted_attributes = ["painted_density", "painted_scale", "random_painted_scale", "painted_ribbon", "painted_tilt", "painted_rotation", "painted_concave"]

    for i, attribute in enumerate(painted_attributes):
        # Create all the attribute nodes
        attribute_create = hou.node(skin_path).createNode("attribcreate::2.0", f"attribcreate_{attribute}")
        attribute_paint = hou.node(skin_path).createNode("attribpaint", attribute)

        # Set the parameteres
        value = 0 if attribute == "painted_concave" else 1
        attribute_create.parm("name1").set(attribute)
        attribute_create.parm("value1v1").set(value)
        attribute_paint.parm("attribname1").set(attribute)

        # Connect the creat to the paint node
        attribute_paint.setNextInput(attribute_create)

        # Set the output of prev attribut_paint to the next attribute_create
        if (i > 0):
            prev_attribute_paint = hou.node(f"{skin_path}/{painted_attributes[i-1]}")
            attribute_create.setNextInput(prev_attribute_paint)
        else:
            tranform_node = hou.node(f"{skin_path}/OUT_transform")
            attribute_create.setNextInput(tranform_node)

        # Connect the last node to the output/null node
        if (i == len(painted_attributes) - 1):
            null_node.setNextInput(attribute_paint)
        
    # Layout children and set render flag for null
    hou.node(skin_path).layoutChildren()
    null_node.setDisplayFlag(True)
    null_node.setRenderFlag(True)

    # Change the merge_skin parameter to point to the new NULL
    hou.parm(f"{Paths.ASSET.value}/merge_skin").set(null_node.path())

    # Add to the session
    hou.setSessionModuleSource("un_ft_attributes_created = True")
