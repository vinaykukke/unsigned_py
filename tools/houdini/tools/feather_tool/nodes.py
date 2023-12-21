from enum import Enum
import hou

class Paths(Enum):
    ASSET = hou.node(".").path()

class Parameters(Enum):
    SKIN = hou.parm(f"{Paths.ASSET.value}/merge_skin").eval()
    CURVES = hou.parm(f"{Paths.ASSET.value}/merge_curves").eval()
    ANIMATED_SKIN = hou.parm(f"{Paths.ASSET.value}/merge_animated_skin").eval()

def create():
    skin_path = hou.node(Parameters.SKIN.value).parent().path()
    # painted_attributes = ["painted_scale"]
    painted_attributes = ["painted_density", "painted_scale", "random_painted_scale", "painted_ribbon", "painted_tilt", "painted_rotation", "painted_concave"]

    for i, attribute in enumerate(painted_attributes):
        # Create all the attribute nodes
        attribute_create = hou.node(skin_path).createNode("attribcreate::2.0", f"attribcreate_{attribute}")
        attribute_paint = hou.node(skin_path).createNode("attribpaint", attribute)

        # Set the parameteres
        attribute_create.parm("name1").set(attribute)
        attribute_create.parm("value1v1").set(1)
        attribute_paint.parm("attribname1").set(attribute)

        # Set the output of prev attribut_paint to the next attribute_create
        if (i > 0):
            prev_attribute_paint = hou.node(f"{skin_path}/{painted_attributes[i-1]}")
            attribute_create.setNextInput(prev_attribute_paint)
        else:
            tranform_node = hou.node(f"{skin_path}/transform")
            attribute_create.setNextInput(tranform_node)

        # Connect the last node to the output/null node
        if (i == len(painted_attributes) - 1):
            null_node = hou.node(f"{skin_path}/null")
            null_node.setNextInput(attribute_paint)
