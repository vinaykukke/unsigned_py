#include <feather_tool_types.h>

int create_attributes(int prim_num) {
    /** Stores all the points on a primitive and puts into an array */
    int prim_pts[] = primpoints(0, prim_num);
    /** Gets the root point (root_pt) from the array */
    return min(prim_pts);
}

/** Keep only the base point and remove all other points */
void keep_base_point(int ptnum; int root_pt) {
    if (ptnum != root_pt) {
        removepoint(0, ptnum);
    }
}

vector set_avg_n(int pid) {
    /** 
     * Take all the points from input 1 and
     * read the N attribute corresponding to the incoming pid
     */
    return point(1, "N", pid);
}

/** Setting the directions of the vectors */
vector set_direction_vector(int ptnum; vector avg_n; vector edge_dir) {
    vector dir = normalize(cross(normalize(avg_n), normalize(edge_dir)));

    if (ptnum %2 != 0) {
        dir *= -1; 
    }

    return dir;
}

vector rotate(float angle; float ramp; vector vector_to_rotate; vector second_vector) {
	angle *= ramp;

    vector rotation_axis = normalize(cross(normalize(vector_to_rotate), normalize(second_vector)));
	vector4 quat = quaternion(radians(angle), rotation_axis);

	return qrotate(quat, vector_to_rotate);
}

vector clump_feathers(ClumpInfo info) {
    /** Right Side */
    float u_pos;
    vector pos;
    vector dir = info.dir;
    float u_inc = (info.u_end - info.u_start) / info.clump_num; 
    float loop_inc = info.u_start + u_inc;
    float loop_start = info.u_start;

    /** Find the clump position */
    for (int i = 0; i < info.clump_num; i++)  {
        u_pos = fit01(rand(info.pid + info.random_number + info.seed), loop_start, loop_inc);
        append(info.u_pos, u_pos);
        loop_start += u_inc;
        loop_inc += u_inc;
    }

    /** Extract the 3D position from the u_pos */
    foreach (float val; info.u_pos) {
        int prev_pts = info.pts[len(info.pts) - 1];
        int pt = nearpoint(0, pos);
        int condition_right = prev_pts == pt || pt % 2 != 0;
        int condition_left = prev_pts == pt || pt % 2 == 0;
        /** Get the position from the primitive and store in pos */
        prim_attribute(0, pos , "P", info.primnum, val, 0);

        /** If our near point is the same as the prev point then add 1 */
        if (condition_right || condition_left) {
            pt += 1;
        }

        append(info.pts, pt);
    }

    /** Calculate the angle */
    foreach (int i; info.pts){
        if (info.ptnum > i) {
            info.sum_of_angles += info.angle;
            
            if (info.sum_of_angles >= 90) {
                info.angle = 0;
            }

            vector4 rotation = quaternion(radians(info.angle), info.rot_axis);
            dir = qrotate(rotation, dir);
        }
    }

    return dir;
}