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