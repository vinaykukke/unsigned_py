import os
import hou


def __process_folder(folder_path):
    file_names = []
    # Get all files with .vfl extension in the folder
    files = [f for f in os.listdir(folder_path) if f.endswith(".vfl")]
    # Define a custom sorting key function to extract the numeric part of the filename
    def get_numeric_part(file_name):
        return int(''.join(filter(str.isdigit, file_name)))

    # Sort files based on the numeric part of the filename
    files.sort(key=get_numeric_part)

    if len(files) == 0:
        hou.ui.displayMessage(
            "The code you are looking for doesn't exist!")  # type: ignore
    else:
        for file in files:
            # Use the file name (excluding extension) as the Wrangle node name
            file_names.append(file)
            file_names.append(file.split(".")[1])

    return file_names


def get():
    nodes = []
    # Get all items in the directory
    vex_path = os.environ.get("UNSIGNED_VEX_PATH")
    selected_nodes = hou.selectedNodes()

    if vex_path is None:
        hou.ui.displayMessage("No directories available!")  # type: ignore
    else:
        if len(selected_nodes) > 0:
            current_node = selected_nodes[0]
            node_parm = current_node.parm("tool_name")
            
            if node_parm:
                tool_name = node_parm.rawValue()
                directory_path = os.path.join(vex_path, tool_name, "nodes")
                nodes = __process_folder(directory_path)

    return nodes
