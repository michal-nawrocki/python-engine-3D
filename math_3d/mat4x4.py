from typing import TypeVar
from math import cos, sin

from math_3d.vec3 import Vec3


class Mat4x4:
    """
    Mat4x4 - Matrix with 4 rows and 4 columns.

    Supported operations on a matrix:
        TODO Addition (+) \n
        Matrix-Vector Multiplication (*) \n
        TODO Scalar (**) \n
        TODO Transposition (//) \n
    """
    Mat4x4 = TypeVar("Mat4x4")

    def __init__(self):
        self.m = [[0] * 4 for _ in range(4)]

    def __mul__(self, other: Vec3) -> Vec3:
        """
        Multiplication of a matrix and vector results in a vector.
        :param other: Vec3
        :return: Vec3
        """

        x = other.x * self.m[0][0] + other.y * self.m[1][0] + other.z * self.m[2][0] + self.m[3][0]
        y = other.x * self.m[0][1] + other.y * self.m[1][1] + other.z * self.m[2][1] + self.m[3][1]
        z = other.x * self.m[0][2] + other.y * self.m[1][2] + other.z * self.m[2][2] + self.m[3][2]
        w = other.x * self.m[0][3] + other.y * self.m[1][3] + other.z * self.m[2][3] + self.m[3][3]

        if w != 0.:
            x /= w
            y /= w
            z /= w

        return Vec3(x, y, z)

    @staticmethod
    def x_rotation_matrix(radians: float):
        matrix = Mat4x4()
        matrix.m[0][0] = 1.0
        matrix.m[1][1] = cos(radians)
        matrix.m[1][2] = sin(radians)
        matrix.m[2][1] = -sin(radians)
        matrix.m[2][2] = cos(radians)
        matrix.m[3][3] = 1.0

        return matrix

    @staticmethod
    def y_rotation_matrix(radians: float):
        matrix = Mat4x4()
        matrix.m[0][0] = cos(radians)
        matrix.m[0][2] = sin(radians)
        matrix.m[2][0] = -sin(radians)
        matrix.m[1][1] = 1.0
        matrix.m[2][2] = cos(radians)
        matrix.m[3][3] = 1.0

        return matrix

    @staticmethod
    def z_rotation_matrix(radians: float):
        matrix = Mat4x4()
        matrix.m[0][0] = cos(radians)
        matrix.m[0][1] = sin(radians)
        matrix.m[1][0] = -sin(radians)
        matrix.m[1][1] = cos(radians)
        matrix.m[2][2] = 1.0
        matrix.m[3][3] = 1.0

        return matrix

    def print_matrix(self):
        """
        Print matrix for visual representation
        :return: None
        """
        for x in self.m:
            print(x)

        print()
