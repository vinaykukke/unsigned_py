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
    attributes_created = hou.parm(f"{Paths.ASSET.value}/attributes_created").eval()
    has_attr_in_session = hasattr(hou.session, 'un_ft_attributes_created') # type: ignore
    check_condition = attributes_created and has_attr_in_session

    if (check_condition):
        if (has_attr_in_session):
            hou.ui.displayMessage("All the attributes have already been created!!")  # type: ignore
            sys.exit()
    else:
        eagle = hou.node(Parameters.SKIN.value).parent()
        for child in eagle.children():
            if (child.name() == "OUT_eagle"):
                hou.ui.displayMessage(
                    "All the attributes have already been created!!")  # type: ignore
                sys.exit()

def set_expressions():
    # Unlock the asset to edit it
    asset = hou.node(Paths.ASSET.value)
    asset.allowEditingOfContents()

    # Set the expressions
    box_s = ["sx", "sy", "sz"]
    box_t = ["tx", "ty", "tz"]
    size = hou.parmTuple("/obj/feather_tool_dev/feather_tool/delete_group_box/size")
    translate = hou.parmTuple("/obj/feather_tool_dev/feather_tool/delete_group_box/t")

    for i, s in enumerate(size):
        s.setExpression(f"ch('../../../{asset.name()}__group_box/{box_s[i]}')")

    for i, t in enumerate(translate):
        t.setExpression(f"ch('../../../{asset.name()}__group_box/{box_t[i]}')")

def create_group_box():
    root_node = hou.node("/obj")
    children = root_node.children()
    group_box_name = f"{hou.node(Paths.ASSET.value)}__group_box"
    group_exists = [c for c in children if c.name() == group_box_name]

    # Add if no other bounding box for the feather tool exists
    if (len(group_exists) == 0):
        tool_position = hou.node(Paths.ASSET.value).position()
        geo = root_node.createNode("geo", group_box_name)
        geo.createNode("box")
        # Set the position in the network editior
        geo.setPosition(hou.Vector2(tool_position[0], tool_position[1] - 2.5))
        # Set position in the viewport
        geo.parmTuple("t").set((0,1,0))
        # Set the display to be bounding box
        geo.parm("viewportlod").set(2)
        geo.setDisplayFlag(True)
    
    # Once the box is created set expressions
    set_expressions()

def create():
    # Check if all the attributes have been created and only then proceed
    check()
    # Create the group box
    create_group_box()

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

        # Attributes to set to zero
        zero_attributes = ["painted_tilt", "painted_concave"]

        # Set the parameteres
        value = 0 if attribute in zero_attributes else 1
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
    # Add to the created_attributes paramater
    hou.parm(f"{Paths.ASSET.value}/attributes_created").set(1)
