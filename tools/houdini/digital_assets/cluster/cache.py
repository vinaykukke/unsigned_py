import hou

asset = hou.node(".").path()

def destroy_readers():
    children = hou.node("/obj").children()

    for c in children:
        if ("cluster_reader" in c.name()):
            c.destroy()

def create_reader_nodes():
    # Destroy all previous reader nodes
    destroy_readers()

    # Then create new nodes
    # asset_name = hou.node(asset).name()
    clusters = int(hou.parm(f"{asset}/cluster_core").rawValue())
    reader_node = hou.node("/obj").createNode("geo", "cluster_reader")
    out_null = reader_node.createNode("null", "OUT_READER")
    merge_node = reader_node.createNode("merge", "reader_merge")
    reader_node.moveToGoodPosition()
    out_null.setFirstInput(merge_node)

    for i in range(clusters):
        file_node = reader_node.createNode("file", f"file_cluster_{i+1}")
        file_node.parm("file").set(f"$HIP/geo/$HIPNAME.cluster.{i+1}.$F4.bgeo.sc")
        # If file is not found dont show the geometry
        file_node.parm("missingframe").set(1)
        merge_node.setInput(i+1, file_node)
    
    # Layout all the children
    reader_node.layoutChildren()
    # Set the flags
    out_null.setDisplayFlag(True)
    out_null.setRenderFlag(True)

def write_to_disk():
    c_range_min = hou.parm(f"{asset}/c_rangemin").eval()
    c_range_max = hou.parm(f"{asset}/c_rangemax").eval()
    rop_geo_path = hou.parm(f"{asset}/rop_geo").eval()
    frame_range = hou.parmTuple(f"{rop_geo_path}/f")
    t_range = hou.parm(f"{rop_geo_path}/trange")
    output_node = hou.parm(f"{rop_geo_path}/sopoutput")
    output_path = output_node.rawValue()
    clusters = int(hou.parm(f"{asset}/cluster_core").rawValue())
    select_cluster = hou.parm(f"{asset}/select_cluster")
    save = hou.parm(f"{rop_geo_path}/execute")

    # Set all the frame to be cached
    frame_range.set((c_range_min, c_range_max, 1))
    t_range.set(1)

    for i in range(clusters):
        split_output_path = output_path.split(".")
        split_output_path.insert(1, f"cluster.{str(i+1)}")
        final_path = ".".join(split_output_path)
        output_node.set(final_path)

        # Move to the next cluster
        select_cluster.set(i)

        # Save the cache
        save.pressButton()

    # Set clusters to 0
    select_cluster.set(0)
    # Set the output path back to its original value
    output_node.set(output_path)

    # Create all the reader nodes
    create_reader_nodes()
