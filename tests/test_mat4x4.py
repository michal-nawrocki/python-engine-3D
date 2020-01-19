import unittest

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
