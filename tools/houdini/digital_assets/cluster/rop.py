import sys
import hou

def select():
    asset = hou.node('.').path()
    selected_node = hou.parm(f"{asset}/rop_geo").eval()
    rop_selected = hou.parm(f"{asset}/rop_geo_selected")
    node = hou.node(selected_node)
    
    if (node is None):
        rop_selected.set(0)
        hou.ui.displayMessage("Field cannot be empty!") #type: ignore
        sys.exit()
    
    node_type = node.type().name()
    if (node_type != "rop_geometry"):
        rop_selected.set(0)
        hou.ui.displayMessage("Please select a valid ROP Geometry node!") #type: ignore
        sys.exit()
    
    rop_selected.set(1)