#include <types.h>

function vector[] set_vectors() {
	// Assume forward vector is normalized
	vector up = {0, 1, 0};
	vector N = {0, 0, 1};
	vector aim = normalize(cross(normalize(up), normalize(N)));

    return array(up, N, aim);
}

Side set_side(int ptnum; vector N) {
	/** 
	 * Its much easier to return a vector with values than 
	 * to return one vector and one array 
	 */
	Side result;

	if (ptnum % 2 != 0) {
		result.N = N * -1;
		result.side = -1;
	} else {
		result.N = N;
	}

	return result;
}

vector rotate(float angle; float ramp; int side; vector aim; vector N) {
	float ang;

	if (side == 1) {
		ang = angle;
	} else {
		ang = -angle;
	}

	ang *= ramp; 
	vector4 quat = quaternion(radians(ang), aim);
	vector q_rot = qrotate(quat, N);

	return q_rot;
}

int add_points(vector p; vector N; int ptnum; float scale; float min; float max) {
	// Returns bw 0-1
	float random = fit01(rand(ptnum*11+11), min, max);
	scale += random;

	/** Creating the Geometry*/
	int prim = addprim(0, "polyline");

	/** Adds point and moves them along the normals */
	int new_point = addpoint(0, p+N*scale);

	/** Creates a line between our current point and new point */
	addvertex(0, prim, ptnum);
	addvertex(0, prim, new_point);
}