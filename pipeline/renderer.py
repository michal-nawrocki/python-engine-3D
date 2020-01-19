from math import tan, pi

from graphics import *
from math_3d.mat4x4 import Mat4x4
from math_3d.vec3 import Vec3
from pipeline.helpers.triangle import Triangle


def get_objects_for_scene() -> [[Triangle]]:
    # For now return a list with the points of a cube
    objects = []

    cube = [
        # SOUTH
        Triangle(Vec3(0.0, 0.0, 0.0), Vec3(0.0, 1.0, 0.0), Vec3(1.0, 1.0, 0.0)),
        Triangle(Vec3(0.0, 0.0, 0.0), Vec3(1.0, 1.0, 0.0), Vec3(1.0, 0.0, 0.0)),

        # EAST
        Triangle(Vec3(1.0, 0.0, 0.0), Vec3(1.0, 1.0, 0.0), Vec3(1.0, 1.0, 1.0)),
        Triangle(Vec3(1.0, 0.0, 0.0), Vec3(1.0, 1.0, 1.0), Vec3(1.0, 0.0, 1.0)),

        # NORTH
        Triangle(Vec3(1.0, 0.0, 1.0), Vec3(1.0, 1.0, 1.0), Vec3(0.0, 1.0, 1.0)),
        Triangle(Vec3(1.0, 0.0, 1.0), Vec3(0.0, 1.0, 1.0), Vec3(0.0, 0.0, 1.0)),

        # WEST
        Triangle(Vec3(0.0, 0.0, 1.0), Vec3(0.0, 1.0, 1.0), Vec3(0.0, 1.0, 0.0)),
        Triangle(Vec3(0.0, 0.0, 1.0), Vec3(0.0, 1.0, 0.0), Vec3(0.0, 0.0, 0.0)),

        # TOP
        Triangle(Vec3(0.0, 1.0, 0.0), Vec3(0.0, 1.0, 1.0), Vec3(1.0, 1.0, 1.0)),
        Triangle(Vec3(0.0, 1.0, 0.0), Vec3(1.0, 1.0, 1.0), Vec3(1.0, 1.0, 0.0)),

        # BOTTOM
        Triangle(Vec3(1.0, 0.0, 1.0), Vec3(0.0, 0.0, 1.0), Vec3(0.0, 0.0, 0.0)),
        Triangle(Vec3(1.0, 0.0, 1.0), Vec3(0.0, 0.0, 0.0), Vec3(1.0, 0.0, 0.0)),
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
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.aspect_ration = float(screen_height / screen_width)
        self.fov_rad = 1.0 / tan(fov * 0.5 / 180.0 * pi)

        # Set projection matrix
        proj_mat = Mat4x4()
        proj_mat.m[0][0] = self.aspect_ration * self.fov_rad
        proj_mat.m[1][1] = self.fov_rad
        proj_mat.m[2][2] = far // (far - near)
        proj_mat.m[3][2] = (-far * near) / (far - near)
        proj_mat.m[2][3] = 1.0
        proj_mat.m[3][3] = 0.0

        self.projection_matrix = proj_mat

    def _project_triangle(self, tri: Triangle) -> Triangle:
        """
        Project triangle from 3D to 2D using Renderer's projection matrix

        :param tri: Triangle to be projected
        :return: Projected triangle
        """

        tri_projected = tri
        tri_projected.p[0] = self.projection_matrix * tri.p[0]
        tri_projected.p[1] = self.projection_matrix * tri.p[1]
        tri_projected.p[2] = self.projection_matrix * tri.p[2]

        return tri_projected

    @staticmethod
    def _draw_triangle(tri: Triangle) -> None:
        """
        Draw triangle to screen

        :param tri: Triangle to be drawn
        """

        # For now just print the vectors
        for vec in tri.p:
            print(vec.x)
            print(vec.y)
            print(vec.z)

    def _scale_triangle(self, tri: Triangle) -> Triangle:
        """
        Scale triangle for the view

        :param tri: Triangle to be scaled
        :return: Scaled triangle
        """

        tri_scaled = tri

        tri_scaled.p[0].x += 1.0
        tri_scaled.p[1].x += 1.0
        tri_scaled.p[2].x += 1.0

        tri_scaled.p[0].y += 1.0
        tri_scaled.p[1].y += 1.0
        tri_scaled.p[2].y += 1.0

        tri_scaled.p[0].x *= 0.5 * self.screen_width
        tri_scaled.p[0].y *= 1.0 * self.screen_height

        tri_scaled.p[1].x *= 0.5 * self.screen_width
        tri_scaled.p[1].y *= 1.0 * self.screen_height

        tri_scaled.p[2].x *= 0.5 * self.screen_width
        tri_scaled.p[2].y *= 1.0 * self.screen_height

        return tri_scaled

    def run(self):
        # Clear screen
        # TODO: Implement this

        # Get objects in scene
        objects = get_objects_for_scene()

        # Loop on objects in scene
        for obj in objects:
            # Loop on triangles in an object
            for tri in obj:
                tri_translated = tri

                # Offset into Z-direction
                tri_translated.p[0].z += 3.0
                tri_translated.p[1].z += 3.0
                tri_translated.p[2].z += 3.0

                # Project triangles
                tri_projected = self._project_triangle(tri_translated)

                # Scale triangle into view
                tri_scaled = self._scale_triangle(tri_projected)

                # Draw triangle to screen
                self._draw_triangle(tri_scaled)
