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

void add_points(AddPoints pt) {
    /** Manually created attribues */
    /** Scaling Randomization */
    float random_number = pt.i.pid + rand(pt.i.pid*pt.i.seed+11)*11;
    float random_scale = fit01(rand(pt.i.ptnum+random_number), pt.f.min, pt.f.max) * pt.f.random_painted_scale;

	/** Control the scale fo the feather */
    pt.f.scale = pt.f.scale * pt.f.ramp + random_scale;
    /** Multiply the weighted attribute `painted_scale` to the actual scale of the object */
    pt.f.scale *= pt.f.painted_scale;

	/** Creating the Geometry*/
	int prim = addprim(0, "polyline");

	/** Adds point and moves them along the desired direction */
	int new_point = addpoint(0, pt.v.p+pt.v.dir*pt.f.scale);

	/** Creates a line between our current point and new point */
	addvertex(0, prim, pt.i.ptnum);
	addvertex(0, prim, new_point);

    /** Add all the newly created primitives into their own group */
    setprimgroup(0, "barb_group", prim, 1);

    /** 
     * All the created attributes do not get transfered if geometry is created in code,
     * so they must be transfered manually.
     * ************************************************************
     * Transfer all the attributes to the newly created points.
     */
    setpointattrib(0, "s", new_point, pt.f.s, "set");
    setpointattrib(0, "edge_dir", new_point, pt.v.edge_dir, "set");
    setpointattrib(0, "dir", new_point, pt.v.dir, "set");
    setpointattrib(0, "avg_n", new_point, pt.v.avg_n, "set");
    setpointattrib(0, "pid", new_point, pt.i.pid, "set");
}