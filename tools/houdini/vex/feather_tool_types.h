struct AddPointVector {
	vector p;
    vector dir;
	vector edge_dir;
    vector avg_n;
};

struct AddPointFloat {
	float scale;
    float scale_ramp;
	float random_scale_ramp;
    float min;
    float max;
	float s;
    float painted_scale;
    float random_painted_scale;
};

struct AddPointInt {
	int pid;
    int ptnum;
    int seed;
};

struct AddPoints {
	AddPointVector v;
	AddPointFloat f;
	AddPointInt i;
};

struct ClumpInfo {
    float u_start;
    float u_end;
    float random_number;
    float seed;
    float u_pos[];
    float clump_num;
    float angle;
    float sum_of_angles;
    int pts[];
    int pid;
    int primnum;
    int ptnum;
    vector dir;
    vector rot_axis;
}