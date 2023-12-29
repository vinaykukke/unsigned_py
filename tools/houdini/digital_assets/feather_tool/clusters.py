import inspect
import math
import sys
import hou

def powers_of_2(n):
    powers = [2**i for i in range(n+1) if i > 0]
    return powers

def get_sizes():
    sizes = []
    depth = 8

    for i in powers_of_2(depth):
        sizes.append(i)
        sizes.append(i)

    return sizes

def find_power_of_2(number):
    if number <= 0 or not isinstance(number, int):
        hou.ui.displayMessage(
            f"Error in function: {inspect.currentframe().f_code.co_name} in module: {__name__}! Please check the console.")  # type: ignore
        print("Invalid input. Please provide a positive integer.")
        sys.exit()

    return int(math.log2(number))

def check_clusters():
    children = hou.node("./feather_tool").children()
    cluster_switch = hou.node("./feather_tool/cluster_switch")

    for c in children:
        if ("delete_cluster" in c.name()):
            c.destroy()

    for i in cluster_switch.inputs():
        cluster_switch.setFirstInput(None)

def create():
    # Check for existing cluster and destroy them
    check_clusters()

    # After all the clusters are destroyed then add new ones
    asset = hou.node(".").path()
    cluster_sizes = hou.parm(f"{asset}/cluster_core").rawValue()
    loop_range = (int(cluster_sizes) * 2) - 2
    in_cluster = hou.node(f"{asset}/feather_tool/IN_CLUSTER")
    cluster_switch = hou.node(f"{asset}/feather_tool/cluster_switch")
    cluster_switch.setFirstInput(None)

    for i in range(loop_range):
        delete_node = hou.node(f"{asset}/feather_tool").createNode("delete", f"delete_cluster_{i}")
        delete_node.parm("groupop").set(1)

        if (i%2 != 0):
            delete_node.parm("rangestart").set(1)

        if (i < 2):
            delete_node.setNextInput(in_cluster)
        else:
            parent_node = hou.node(f"{asset}/feather_tool/delete_cluster_{int(i/2) - 1}")
            delete_node.setNextInput(parent_node)
        
        if (i >= (loop_range/2) - 1):
            cluster_switch.setNextInput(delete_node)
        
        delete_node.moveToGoodPosition()
