from enum import Enum
import hou

asset = hou.node(".").path()
master_resolution = hou.parm(f"{asset}/un_feather_resolution")
feather_resolution = hou.parm(f"{asset}/feather_resolution")
poly_feather_resolution = hou.parm(f"{asset}/poly_feather_resolution")
poly_switch = hou.parm(f"{asset}/poly_vis_switch")

class Resolutions(Enum):
    POLY = "poly"
    NORMAL = "normal"

def set(res_type: str):    
    if (res_type == Resolutions.POLY.value):
        master_resolution.set(poly_feather_resolution.eval())

    if (res_type == Resolutions.NORMAL.value):
        master_resolution.set(feather_resolution.eval())

def apply_res():
    if (poly_switch.eval() == 0):
        master_resolution.set(feather_resolution.eval())

    if (poly_switch.eval() == 1):
        master_resolution.set(poly_feather_resolution.eval())