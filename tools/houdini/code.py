import os
import hou

def force_compile(node):
    children = node.children()
    wrangle_node = [c for c in children if c.name() == "unsigned_wrangle"].pop()
    children_wr = wrangle_node.allSubChildren()

    if len(children_wr) > 0:
        compile_btn = children_wr[0].parm("vop_forcecompile")
        compile_btn.pressButton()
        print(f"Force compiled node: {node.name()}")

def get_file_name(tool_name, file_name):
    children = hou.node(f"/obj/{tool_name}").children()
    node_name = f"un__{file_name.split('.')[1]}"

    def __filter(c):
        if node_name in c.name():
            return c
    
    node_list = list(filter(__filter, children))
    if len(node_list) >= 1:
        node_name = f"{node_name}__{len(node_list)+1}"
    
    return node_name
            

def get_code(file_path, node, name):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        file_contents = file.read()

    # Set the VEX code in the Wrangle node
    node.parm("snippet").set(file_contents)
    # Set the name of the node on restore
    if name != node.name():
        node.setName(name)
    
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
        get_code(file_path, current_node, get_file_name(tool_name, file_name))

def clear():
    selected_nodes = hou.selectedNodes()
    node = selected_nodes[0]
    node.parm("snippet").set("")
