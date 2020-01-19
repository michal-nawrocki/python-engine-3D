from typing import TypeVar

from math_3d.vec3 import Vec3


class Triangle:
    """
    Triangle - 3 vectors making up a triangle used for creating models

    """
    Triangle = TypeVar("Triangle")

    def __init__(self, p1: Vec3, p2: Vec3, p3: Vec3):
        self.p = [p1, p2, p3]
