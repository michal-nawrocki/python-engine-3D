import unittest
from math_3d.vec3 import Vec3


class TestVec3(unittest.TestCase):
    """
    Unit test for Vec3
    """
    def test_addition(self):
        """ Testing + operator """
        vec_a = Vec3(1, 2, 3)
        vec_b = Vec3(0, 1, 3)
        vec_c = vec_a + vec_b

        self.assertEqual(1, vec_c.x, "Asserting vec3.x")
        self.assertEqual(3, vec_c.y, "Asserting vec3.y")
        self.assertEqual(6, vec_c.z, "Asserting vec3.z")

    def test_subtraction(self):
        """ Testing - operator """
        vec_a = Vec3(5, 4, 3)
        vec_b = Vec3(3, 4, 5)
        vec_c = vec_a - vec_b

        self.assertEqual(2, vec_c.x, "Asserting vec3.x")
        self.assertEqual(0, vec_c.y, "Asserting vec3.y")
        self.assertEqual(-2, vec_c.z, "Asserting vec3.z")

    def test_dot_product(self):
        """ Testing * operator for dot_product """
        vec_a = Vec3(1, 2, 3)
        vec_b = Vec3(0, 1, 3)
        dot_product = vec_a * vec_b

        self.assertEqual(11, dot_product, "Asserting dot_product")

    def test_scalar(self):
        """ Testing * operator for scalar multiplication """
        vec = Vec3(5, 2, 3)
        result = vec * 3

        self.assertEqual(15, result.x, "Asserting vec3.x")
        self.assertEqual(6, result.y, "Asserting vec3.y")
        self.assertEqual(9, result.z, "Asserting vec3.z")

        vec = Vec3(2, 3, 4)
        result = 5 * vec
        self.assertEqual(10, result.x, "Asserting vec3.x")
        self.assertEqual(15, result.y, "Asserting vec3.y")
        self.assertEqual(20, result.z, "Asserting vec3.z")

    def test_cross_product(self):
        """ Testing // operator """
        vec_a = Vec3(2, 3, 4)
        vec_b = Vec3(5, 6, 7)
        vec_c = vec_a // vec_b

        self.assertEqual(-3, vec_c.x, "Asserting vec3.x")
        self.assertEqual(6, vec_c.y, "Asserting vec3.y")
        self.assertEqual(-3, vec_c.z, "Asserting vec3.z")

    def test_equals(self):
        """ Testing == operator """
        vec_a = Vec3(2, 3, 4)
        vec_b = Vec3(5, 6, 7)

        self.assertTrue(vec_a == vec_a, "Asserting vec_a == vec_a")
        self.assertFalse(vec_a == vec_b, "Asserting vec_a == vec_b")

    def test_not_equals(self):
        """ Testing != operator """
        vec_a = Vec3(2, 3, 4)
        vec_b = Vec3(5, 6, 7)

        self.assertFalse(vec_a != vec_a, "Asserting vec_a == vec_a")
        self.assertTrue(vec_a != vec_b, "Asserting vec_a == vec_b")

    def test_normalize(self):
        """ Testing .normalize() """
        vec = Vec3(4, 3, 0).normalize()

        self.assertEqual(0.8, vec.x, "Asserting vec3.x")
        self.assertEqual(0.6, vec.y, "Asserting vec3.y")
        self.assertEqual(0, vec.z, "Asserting vec3.z")
