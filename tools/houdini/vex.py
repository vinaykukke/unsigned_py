"""
Saves all the vex code written in houdini into .vex files in the repository
"""

import hou
import os

def node_setup():
    """
    Makes the node setup necessary for saving vex files
    """
    root_node: hou.Node = hou.node("/obj")
    geo: hou.Node = root_node.createNode("geo", "SPHERE")
    # Sphere
    sphere: hou.Node = geo.createNode("sphere")
    sphere.parm("type").set(1)
    sphere.moveToGoodPosition()
    # Arrtibute Wrangle
    attrib_wrangle: hou.Node = geo.createNode("attribwrangle", "WRANGLER")
    attrib_wrangle.setNextInput(sphere)
    attrib_wrangle.moveToGoodPosition()
    # Python Node
    script: hou.Node = geo.createNode("python")
    script.setNextInput(sphere)
    script.moveToGoodPosition()
    script.parm("python").set("from houdini import vex \nvex.text()")
    # get existing list of parameters for the specified node
    g = script.parmTemplateGroup()

    # define new float parameter ("id", "Label", components/input fields, default values)
    p = hou.StringParmTemplate("myParm", "My Parameter", 3, default_value="Test")

    # append the new parameter to the list
    g.append(p)

    # apply changes
    script.setParmTemplateGroup(g)
 

def save():
    """
    Saves to a .vex file and recomplies all the changes in any vex code
    """
    node_setup()
    # node: hou.Node = hou.node("/obj")
    # fileparm = node.parm("script_filepath")
    # filename = fileparm.eval()
    # geo = node.geometry()
    # print(filename)

def text():
    """
    te
    """
    print("This is working")
