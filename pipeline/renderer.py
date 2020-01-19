import math

from graphics import *

from math_3d.mat4x4 import Mat4x4
from math_3d.vec3 import Vec3


def get_objects_in_scene() -> [[[Vec3]]]:
    # For now return a list with the points of a cube
    objects = []

    cube = [
        # SOUTH
        [Vec3(0.0, 0.0, 0.0), Vec3(0.0, 1.0, 0.0), Vec3(1.0, 1.0, 0.0)],
        [Vec3(0.0, 0.0, 0.0), Vec3(1.0, 1.0, 0.0), Vec3(1.0, 0.0, 0.0)],

        # EAST
        [Vec3(1.0, 0.0, 0.0), Vec3(1.0, 1.0, 0.0), Vec3(1.0, 1.0, 1.0)],
        [Vec3(1.0, 0.0, 0.0), Vec3(1.0, 1.0, 1.0), Vec3(1.0, 0.0, 1.0)],

        # NORTH
        [Vec3(1.0, 0.0, 1.0), Vec3(1.0, 1.0, 1.0), Vec3(0.0, 1.0, 1.0)],
        [Vec3(1.0, 0.0, 1.0), Vec3(0.0, 1.0, 1.0), Vec3(0.0, 0.0, 1.0)],

        # WEST
        [Vec3(0.0, 0.0, 1.0), Vec3(0.0, 1.0, 1.0), Vec3(0.0, 1.0, 0.0)],
        [Vec3(0.0, 0.0, 1.0), Vec3(0.0, 1.0, 0.0), Vec3(0.0, 0.0, 0.0)],

        # TOP
        [Vec3(0.0, 1.0, 0.0), Vec3(0.0, 1.0, 1.0), Vec3(1.0, 1.0, 1.0)],
        [Vec3(0.0, 1.0, 0.0), Vec3(1.0, 1.0, 1.0), Vec3(1.0, 1.0, 0.0)],

        # BOTTOM
        [Vec3(1.0, 0.0, 1.0), Vec3(0.0, 0.0, 1.0), Vec3(0.0, 0.0, 0.0)],
        [Vec3(1.0, 0.0, 1.0), Vec3(0.0, 0.0, 0.0), Vec3(1.0, 0.0, 0.0)],
    ]

    objects.append(cube)

    return objects


class Renderer:
    """
    Renderer - Compute the frame of a scene
    """

    def __init__(
            self,
            *,
            near: float,
            far: float,
            fov: float,
            screen_height: int,
            screen_width: int
    ):
        """
        Set up all variables needed for the projection matrix

        :param near: float representing distance to near plane
        :param far: float representing distance to far plane
        :param fov: float representing field-of-view
        :param screen_height: int representing height of the screen
        :param screen_width: int representing width of the screen
        """
        self.near = near,
        self.far = far,
        self.fov = fov,
        self.aspect_ration = float(screen_height / screen_width)
        self.fov_rad = 1.0 / math.tan(fov * 0.5 / 180.0 * math.pi)

        # Initiate projection matrix
        proj_mat = Mat4x4()
        proj_mat.m[0][0] = self.aspect_ration * self.fov_rad
        proj_mat.m[1][1] = self.fov_rad
        proj_mat.m[2][2] = self.far / (self.far - self.near)
        proj_mat.m[3][2] = (-self.far * self.near) / (self.far - self.near)
        proj_mat.m[2][3] = 1.0
        proj_mat.m[3][3] = 0.0

    def run(self, window: GraphWin):

        # Clear screen
        window.setBackground(color_rgb(0, 0, 0))

        # Get objects in scene
        objects = get_objects_in_scene()

        # Loop on objects in scene
        for obj in objects:
            # Loop on triangles in an object
            for triangle in obj:
                pass
