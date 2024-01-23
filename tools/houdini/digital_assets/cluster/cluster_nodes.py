import hou
from enum import Enum

class Paths(Enum):
    ASSET = hou.node(".").path()

def powers_of_2(n):
    powers = [2**i for i in range(n+1) if i > 0]
    return powers

def get_sizes():
    sizes = [0, 0]
    depth = 8

    for i in powers_of_2(depth):
        sizes.append(i)
        sizes.append(i)

    return sizes

def check_clusters():
    cluster_sizes = 2**int(hou.parm(f"{Paths.ASSET.value}/cluster_core").eval())
    in_cluster = hou.node(f"{Paths.ASSET.value}/IN_CLUSTER")
    children = hou.node(f"{Paths.ASSET.value}").children()
    cluster_switch = hou.node(f"{Paths.ASSET.value}/cluster_switch")
    cluster_inputs = cluster_switch.inputs()

    for c in children:
        if ("delete_cluster" in c.name()):
            c.destroy()

    for _ in cluster_inputs:
        cluster_switch.setFirstInput(None)
    
    # Since 2^0 = 1 we need to check for 1 here
    if (cluster_sizes == 1):
        cluster_switch.setFirstInput(in_cluster)

def create():
    asset = hou.node(Paths.ASSET.value)
    cluster_sizes = 2**int(hou.parm(f"{Paths.ASSET.value}/cluster_core").eval())
    in_cluster = hou.node(f"{Paths.ASSET.value}/IN_CLUSTER")
    cluster_switch = hou.node(f"{Paths.ASSET.value}/cluster_switch")
    loop_range = (cluster_sizes * 2) - 2

    # Unlock the asset
    asset.allowEditingOfContents()
    # Check for existing cluster and destroy them
    check_clusters()

    # After all the clusters are destroyed then add new ones
    # Since 2^0 = 1 we need to check for 1 here
    if (cluster_sizes != 1):
        cluster_switch.setFirstInput(None)

    for i in range(loop_range):
        delete_node = hou.node(f"{Paths.ASSET.value}").createNode("delete", f"delete_cluster_{i}")
        delete_node.parm("groupop").set(1)

        if (i%2 != 0):
            delete_node.parm("rangestart").set(1)

        if (i < 2):
            delete_node.setNextInput(in_cluster)
        else:
            parent_node = hou.node(f"{Paths.ASSET.value}/delete_cluster_{int(i/2) - 1}")
            delete_node.setNextInput(parent_node)
        
        if (i >= (loop_range/2) - 1):
            cluster_switch.setNextInput(delete_node)
        
        delete_node.moveToGoodPosition()

def select():
    cluster_sizes = 2**int(hou.parm(f"{Paths.ASSET.value}/cluster_core").eval())
    select_cluster = hou.parm(f"{Paths.ASSET.value}/select_cluster")
    list = []

    # Since 2^0 = 1 we need to check for 1 here
    if (cluster_sizes == 1):
        list = [0, 0]
        select_cluster.set(0)
    else:
        for c in range(cluster_sizes):
            list.append(c+1)
            list.append(c+1)

    return list