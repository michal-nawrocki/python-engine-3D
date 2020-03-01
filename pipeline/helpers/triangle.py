from typing import TypeVar

from math_3d.vec3 import Vec3


class Triangle:
    """
    Triangle - 3 vectors making up a triangle used for creating models

    """
    Triangle = TypeVar("Triangle")

    def __init__(
            self,
            p1: Vec3,
            p2: Vec3,
            p3: Vec3,
            angle_to_light=None,   # Used to determine intensity of color when drawn
    ):
        self.p = [p1, p2, p3]
        self.angle_to_light = angle_to_light
