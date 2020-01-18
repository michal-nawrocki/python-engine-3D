from typing import TypeVar


class Vec3:
    """
    Vec3 - Vector with 3 coordinates X, Y, Z.

    Supports all operations on a vector:
        Addition (+)
        Subtraction (-)
        Dot-product (*)
        Cross-product (//)
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

    def __mul__(self, other) -> float:
        """
        Dot-product of 2 vectors results to a float.
        Geometrically, this is can tell the relation between 2 vectors.
        If the result is equal to 0, the vectors are perpendicular.

        :param other: Vec3
        :return: float
        """

        return self.x*other.x + self.y*other.y + self.z*other.z

    def __floordiv__(self, other) -> Vec3:
        """
        Cross-product of 2 vectors results to a new vector.
        The result vector is at a right angle to both of the vectors.

        :param other: Vec3
        :return: Vec3
        """

        c_x = self.y*other.z - self.z*other.y
        c_y = self.z*other.x - self.x*other.z
        c_z = self.x*other.y - self.y*other.x

        return Vec3(c_x, c_y, c_z)

    def __eq__(self, other: Vec3) -> bool:
        """
        Comparing if 2 vectors are the same.

        :param other: Vec3
        :return: bool
        """
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False
