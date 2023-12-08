struct AddPointVector {
	vector p;
    vector dir;
	vector edge_dir;
    vector avg_n;
};

struct AddPointFloat {
	float scale;
    float ramp;
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