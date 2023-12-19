import os
import hou

def force_compile(node):
    children = node.children()
    wrangle_node = [c for c in children if c.name() == "unsigned_wrangle"].pop()
    children_wr = wrangle_node.allSubChildren()
    compile_btn = children_wr[0].parm("vop_forcecompile")
    compile_btn.pressButton()
    print(f"Force compiled node: {node.name()}")

def get_code(file_path, node, name):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        file_contents = file.read()

    # Set the VEX code in the Wrangle node
    node.parm("snippet").set(file_contents)
    # Set the name of the node on restore
    if "un__" not in node.name():
        node.setName(f"un__{name.split('.')[1]}")
    
    # Force the compile on update
    force_compile(node)

def restore(tool_name: str):
    # Get all items in the directory
    vex_path = os.environ.get("UNSIGNED_VEX_PATH")

    if vex_path is None:
        hou.ui.displayMessage("No directories available!") # type: ignore

    if vex_path is not None:
        selected_nodes = hou.selectedNodes()
        current_node = selected_nodes[0]
        file_name = current_node.parm("file_name").rawValue()
        file_path = os.path.join(vex_path, tool_name, "nodes", file_name);
        get_code(file_path,current_node, file_name)

def clear():
    selected_nodes = hou.selectedNodes()
    node = selected_nodes[0]
    node.parm("snippet").set("")
