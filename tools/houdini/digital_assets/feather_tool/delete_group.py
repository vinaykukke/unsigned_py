import hou

def toggle():
    asset_path = hou.node('.').path()
    toggle = hou.parm(f"{asset_path}/toggle_delete_group").eval()
    range_switch = hou.parm(f"{asset_path}/range_switch")
    box = hou.node(f"{asset_path}__group_box")
    range_switch.set(toggle)
    box.setDisplayFlag(toggle)