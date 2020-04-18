"""
Camera class which is basically wrapper around a Vec3
"""
from math_3d.vec3 import Vec3


class Camera:
    def __init__(self, position: Vec3):
        self.position = position
        self.yaw = 0
        self.move_direction = None
