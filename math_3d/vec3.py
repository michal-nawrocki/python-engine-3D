from typing import (
    Union,
    TypeVar,
)
from math import sqrt


class Vec3:
    """
    Vec3 - Vector with 3 coordinates X, Y, Z.

    Supports all operations on a vector:
        Addition (+) \n
        Subtraction (-) \n
        Scalar multiplication (*) \n
        Dot-product (*) \n
        Cross-product (//) \n

    Can also compare if vectors are equal
    """
    Vec3 = TypeVar("Vec3")

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: Vec3):
        """
        Addition of vectors results to a new vector

        :param other: Vec3
        :return: Vec3
        """
        return Vec3(
            x=self.x + other.x,
            y=self.y + other.y,
            z=self.z + other.z
        )

    def __sub__(self, other: Vec3) -> Vec3:
        """
        Subtraction of 2 vectors results to a new vector.

        :param other: Vec3
        :return: Vec3
        """

        return Vec3(
            x=self.x - other.x,
            y=self.y - other.y,
            z=self.z - other.z
        )

    def __mul__(self, other: Union[float, Vec3]) -> Union[float, Vec3]:
        """
        Dot-product of 2 vectors results to a float.
        Geometrically, this is can tell the relation between 2 vectors.
        If the result is equal to 0, the vectors are perpendicular.

        Scalar multiplication results in a new Vec3.

        :param other: Number or Vec3
        :return: float or Vec3
        """

        if isinstance(other, self.__class__):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return Vec3(
                x=self.x * other,
                y=self.y * other,
                z=self.z * other
            )

    def __rmul__(self, other: Union[float, Vec3]):
        """
        Returns the exact same values as __mul__

        :param other: Number or Vec3
        :return: float or Vec3
        """
        return self.__mul__(other)

    def __floordiv__(self, other: Vec3) -> Vec3:
        """
        Cross-product of 2 vectors results to a new vector.
        The result vector is at a right angle to both of the vectors.

        :param other: Vec3
        :return: Vec3
        """

        c_x = self.y*other.z - self.z*other.y
        c_y = self.z*other.x - self.x*other.z
        c_z = self.x*other.y - self.y*other.x

        return Vec3(
            x=c_x,
            y=c_y,
            z=c_z
        )

    def __eq__(self, other: Vec3) -> bool:
        """
        Comparing if 2 vectors are the same.

        :param other: Vec3
        :return: bool
        """
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other: Vec3) -> bool:
        """
        Compare if 2 vectors are not equal

        :param other: Vec3
        :return: bool
        """

        return not self.__eq__(other)

    def normalize(self) -> Vec3:
        """
        Normalize a vector to the unit vector

        :return: None
        """

        length = sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        if length != 0:
            self.x /= length
            self.y /= length
            self.z /= length

        return self

    @staticmethod
    def intersect_plane(
        plane_point: Vec3,
        plane_normal: Vec3,
        line_start: Vec3,
        line_end: Vec3
    ):
        plane_normal.normalize()

        plane_normal_dot = -(plane_normal * plane_point)
        start_plane_dot = line_start * plane_normal
        end_plane_dot = line_end * plane_normal
        t = (-plane_normal_dot - start_plane_dot) / (end_plane_dot - start_plane_dot)
        line_start_end = line_end - line_start
        line_intersect = line_start_end * t

        return line_start + line_intersect

    @staticmethod
    def point_to_plane_distance(
        point: Vec3,
        plane_point: Vec3,
        plane_normal: Vec3
    ):
        point = point.normalize()

        return plane_normal.x * point.x + plane_normal.y * point.y \
            + plane_normal.z * point.z - (plane_normal * plane_point)

