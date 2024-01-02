import hou

asset = hou.node(".").path()

def create_reader_nodes():
    asset_name = hou.node(asset).name()
    clusters = int(hou.parm(f"{asset}/cluster_core").rawValue())
    reader_node = hou.node("/obj").createNode("geo", "cluster_reader")
    out_null = reader_node.createNode("null", "OUT_READER")
    merge_node = reader_node.createNode("merge", "reader_merge")
    r_position = hou.node(asset).position()
    reader_node.setPosition(hou.Vector2(r_position[0]+ 3.5, r_position[1]))
    out_null.setFirstInput(merge_node)

    for i in range(clusters):
        file_node = reader_node.createNode("file", f"file_cluster_{i+1}")
        file_node.parm("file").set(f"$HIP/geo/feather_tool.{asset_name}.cluster.{i+1}.$F4.bgeo.sc")
        merge_node.setInput(i+1, file_node)
    
    # Layout all the children
    reader_node.layoutChildren()
    # Set the flags
    out_null.setDisplayFlag(True)
    out_null.setRenderFlag(True)

def write_to_disk():
    c_range_min = hou.parm(f"{asset}/c_rangemin").eval()
    c_range_max = hou.parm(f"{asset}/c_rangemax").eval()
    frame_range = hou.parmTuple(f"{asset}/f")
    t_range = hou.parm(f"{asset}/trange")
    output_node = hou.parm(f"{asset}/sopoutput")
    output_path = output_node.rawValue()
    clusters = int(hou.parm(f"{asset}/cluster_core").rawValue())
    select_cluster = hou.parm(f"{asset}/select_cluster")
    save = hou.parm(f"{asset}/execute")

    # Set all the frame to be cached
    frame_range.set((c_range_min, c_range_max, 1))
    t_range.set(1)

    for i in range(clusters):
        split_output_path = output_path.split(".")
        split_output_path.insert(2, f"cluster.{i+1}")
        final_path = ".".join(split_output_path)
        output_node.set(final_path)

        # Move to the next cluster
        select_cluster.set(i)

        # Save the cache
        save.pressButton()

    # Set the output path back to its original value
    output_node.set(output_path)

    # Create all the reader nodes
    create_reader_nodes()

        
