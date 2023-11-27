struct Vector3 {
    float x, y, z;
};

function vector[] set_vectors() {
	// Assume forward vector is normalized
	vector up = {0, 1, 0};
	vector N = {0, 0, 1};

    return array(up, N);
}

vector set_side(int ptnum; vector N) {
	vector res = N;

	if (ptnum %2 != 0) {
		res *= -1;
	}

	return res;
}