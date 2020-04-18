import unittest
from math import cos, sin

from math_3d.vec3 import Vec3
from math_3d.mat4x4 import Mat4x4


class TestMat4x4(unittest.TestCase):
    """
    Unit test of Mat4x4
    """
    def test_vector_multiplication(self):
        """ Testing * operator """
        vec = Vec3(1, 2, 3)
        matrix = Mat4x4()

        matrix.m[0] = [4, 3, 1, 0]
        matrix.m[2] = [2, 2, 2, 0]

        result = matrix * vec

        self.assertEqual(10, result.x, "Asserting vec.x from matrix-vector multiplication")
        self.assertEqual(9, result.y, "Asserting vec.y from matrix-vector multiplication")
        self.assertEqual(7, result.z, "Asserting vec.z from matrix-vector multiplication")

    def test_x_rotation_matrix(self):
        """ Test x_rotation_matrix """

        angle = 0.5
        x_rotation_matrix = Mat4x4.x_rotation_matrix(angle).m

        row_0 = [1.0, 0.0, 0.0, 0.0]
        row_1 = [0.0, cos(angle), sin(angle), 0.0]
        row_2 = [0.0, -sin(angle), cos(angle), 0.0]
        row_3 = [0.0, 0.0, 0.0, 1.0]

        self.assertEqual(row_0, x_rotation_matrix[0], "Asserting mat[0] row for x_rotation_matrix")
        self.assertEqual(row_1, x_rotation_matrix[1], "Asserting mat[1] row for x_rotation_matrix")
        self.assertEqual(row_2, x_rotation_matrix[2], "Asserting mat[2] row for x_rotation_matrix")
        self.assertEqual(row_3, x_rotation_matrix[3], "Asserting mat[3] row for x_rotation_matrix")

    def test_y_rotation_matrix(self):
        """ Test y_rotation_matrix """

        angle = 0.5
        y_rotation_matrix = Mat4x4.y_rotation_matrix(angle).m

        row_0 = [cos(angle), 0.0, sin(angle), 0.0]
        row_1 = [0.0, 1.0, 0.0, 0.0]
        row_2 = [-sin(angle), 0.0, cos(angle), 0.0]
        row_3 = [0.0, 0.0, 0.0, 1.0]

        self.assertEqual(row_0, y_rotation_matrix[0], "Asserting mat[0] row for y_rotation_matrix")
        self.assertEqual(row_1, y_rotation_matrix[1], "Asserting mat[1] row for y_rotation_matrix")
        self.assertEqual(row_2, y_rotation_matrix[2], "Asserting mat[2] row for y_rotation_matrix")
        self.assertEqual(row_3, y_rotation_matrix[3], "Asserting mat[3] row for y_rotation_matrix")

    def test_z_rotation_matrix(self):
        """ Test z_rotation_matrix """

        angle = 0.5
        z_rotation_matrix = Mat4x4.z_rotation_matrix(angle).m

        row_0 = [cos(angle), sin(angle), 0.0, 0.0]
        row_1 = [-sin(angle), cos(angle), 0.0, 0.0]
        row_2 = [0.0, 0.0, 1.0, 0.0]
        row_3 = [0.0, 0.0, 0.0, 1.0]

        self.assertEqual(row_0, z_rotation_matrix[0], "Asserting mat[0] row for z_rotation_matrix")
        self.assertEqual(row_1, z_rotation_matrix[1], "Asserting mat[1] row for z_rotation_matrix")
        self.assertEqual(row_2, z_rotation_matrix[2], "Asserting mat[2] row for z_rotation_matrix")
        self.assertEqual(row_3, z_rotation_matrix[3], "Asserting mat[3] row for z_rotation_matrix")
