"""
Custom scripts to create basic lighting setup
"""

import hou
# from houdini import helper
# from packages.scipy import constants

def setup():
    """
    Sets up the scene with predetermined requiremnets
    """
    # if helper.check_existing("un_light") is not True:
    #     create_threepoint_light()
    # print(constants.acre)

def create_threepoint_light():
    """
    Creates a three point light that always faces the object of interest
    """
    root_node: hou.Node = hou.node("/obj")
    light: hou.Node = root_node.createNode("hlight::2.0", "un_light")
    light.parm("light_type").set(2)
    light.parmTuple("t").set((0, 2, 2))
    # print(light.evalParmTuple("t"))
    # /Applications/Houdini/Houdini19.5.716/Houdini FX 19.5.716.app/Contents/MacOS/houdinifx -m pip install
