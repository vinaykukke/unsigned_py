import hou

def write_to_disk():
    asset = hou.node(".").path()
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

        
