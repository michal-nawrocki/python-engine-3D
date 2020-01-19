from math_3d.mat4x4 import Mat4x4


if __name__ == "__main__":
    print("3D engine written in Python3.6")

    matrix = Mat4x4()
    matrix.m[0] = [1, 2, 3, 4]
    matrix.m[3] = [5, 4, 3, 2]

    matrix.print_matrix()

