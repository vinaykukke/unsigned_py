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

void add_points(
    vector p;
    vector dir;
    int pid;
    int ptnum;
    float scale;
    float ramp;
    float min;
    float max;
    int seed;
    float s;
    vector edge_dir;
    vector avg_n;
    vector dir;
    ) {

    /** Manually created attribues */
    
    /** Scaling Randomization */
    float random_number = pid + rand(pid*seed+11)*11;
    float random_scale = fit01(rand(ptnum+random_number), min, max);

	/** Control the scale fo the feather */
    scale = scale * ramp + random_scale;

	/** Creating the Geometry*/
	int prim = addprim(0, "polyline");

	/** Adds point and moves them along the desired direction */
	int new_point = addpoint(0, p+dir*scale);

	/** Creates a line between our current point and new point */
	addvertex(0, prim, ptnum);
	addvertex(0, prim, new_point);

    /** Add all the newly created primitives into their own group */
    setprimgroup(0, "barb_group", prim, 1);

    /** 
     * All the created attributes do not get transfered if geometry is created in code,
     * so they must be transfered manually.
     * ************************************************************
     * Transfer all the attributes to the newly created points.
     */
    setpointattrib(0, "s", new_point, s, "set");
    setpointattrib(0, "edge_dir", new_point, edge_dir, "set");
    setpointattrib(0, "dir", new_point, dir, "set");
    setpointattrib(0, "avg_n", new_point, avg_n, "set");
    setpointattrib(0, "pid", new_point, pid, "set");
}

vector ribbon_feather(
    float f[]; 
    float w[]; 
    int pid;
    float angle;
    float ramp;
    vector edge_dir;
    vector dir
    ) {
    float rand_freq = fit01(rand(pid*1111 + 11), f[1], f[2]);
    float rand_weight = fit01(rand(pid*2222 + 22), w[1], w[2]);
    angle *= w[0] * ramp;
    vector4 quat = quaternion(radians(angle), edge_dir);

	return qrotate(quat, dir);
}