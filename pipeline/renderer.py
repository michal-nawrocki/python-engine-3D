from math import sin, cos, tan, pi
from tkinter import Canvas

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
        self.theta = 0.0

        self.camera = Vec3(0, 0, 0)

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
    def _calculate_shade_of_triangle(tri: Triangle):
        """
        Calculate the shade of a color based on triangles angle to light

        As we draw only white for now, I use hardcoded values of shades of white
        """
        dot_value = tri.angle_to_light

        if dot_value <= 0.1:
            shade_of_triangle = "#191919"
        elif dot_value <= 0.2:
            shade_of_triangle = "#323232"
        elif dot_value <= 0.3:
            shade_of_triangle = "#4c4c4c"
        elif dot_value <= 0.4:
            shade_of_triangle = "#666666"
        elif dot_value <= 0.5:
            shade_of_triangle = "#7f7f7f"
        elif dot_value <= 0.6:
            shade_of_triangle = "#999999"
        elif dot_value <= 0.7:
            shade_of_triangle = "#b2b2b2"
        elif dot_value <= 0.8:
            shade_of_triangle = "#cccccc"
        elif dot_value <= 0.9:
            shade_of_triangle = "#e5e5e5"
        else:
            shade_of_triangle = "#ffffff"

        return shade_of_triangle

    @staticmethod
    def _draw_triangle(tri: Triangle, window: Canvas) -> None:
        """
        Draw triangle to screen

        :param tri: Triangle to be drawn
        """
        points = [tri.p[0].x, tri.p[0].y, tri.p[1].x, tri.p[1].y, tri.p[2].x, tri.p[2].y]
        shade_of_triangle = Renderer._calculate_shade_of_triangle(tri)

        window.create_polygon(points, outline="red", fill=shade_of_triangle)

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

        tri_scaled.p[0].x *= 0.6 * self.screen_width
        tri_scaled.p[0].y *= 0.6 * self.screen_height

        tri_scaled.p[1].x *= 0.6 * self.screen_width
        tri_scaled.p[1].y *= 0.6 * self.screen_height

        tri_scaled.p[2].x *= 0.6 * self.screen_width
        tri_scaled.p[2].y *= 0.6 * self.screen_height

        return tri_scaled

    def render_frame(self, window: Canvas, time_diff: float) -> Canvas:
        # Clear screen
        window.delete("all")

        # Get objects in scene
        objects = get_objects_for_scene()

        # Angle for rotation
        self.theta += time_diff * 1.0

        # Setup Z-Rotation matrix
        z_rotate = Mat4x4()
        z_rotate.m[0][0] = cos(self.theta)
        z_rotate.m[0][1] = sin(self.theta)
        z_rotate.m[1][0] = -sin(self.theta)
        z_rotate.m[1][1] = cos(self.theta)
        z_rotate.m[2][2] = 1
        z_rotate.m[3][3] = 1

        # Setup X-Rotation matrix
        x_rotate = Mat4x4()
        x_rotate.m[0][0] = 1
        x_rotate.m[1][1] = cos(self.theta * 0.5)
        x_rotate.m[1][2] = sin(self.theta * 0.5)
        x_rotate.m[2][1] = -sin(self.theta * 0.5)
        x_rotate.m[2][2] = cos(self.theta * 0.5)
        x_rotate.m[3][3] = 1

        # Loop on objects in scene
        for obj in objects:
            # Loop on triangles in an object
            for tri in obj:
                # Rotate about Z-axis
                tri_rotated_z = tri
                tri_rotated_z.p[0] = z_rotate * tri.p[0]
                tri_rotated_z.p[1] = z_rotate * tri.p[1]
                tri_rotated_z.p[2] = z_rotate * tri.p[2]

                # Rotate about X-axis
                tri_rotated_x = tri_rotated_z
                tri_rotated_x.p[0] = x_rotate * tri_rotated_x.p[0]
                tri_rotated_x.p[1] = x_rotate * tri_rotated_x.p[1]
                tri_rotated_x.p[2] = x_rotate * tri_rotated_x.p[2]

                # Offset into Z-direction
                tri_translated = tri_rotated_x
                tri_translated.p[0].z += 3.0
                tri_translated.p[1].z += 3.0
                tri_translated.p[2].z += 3.0

                # Get normal of triangle
                line_a = tri_translated.p[1] - tri_translated.p[0]
                line_b = tri_translated.p[2] - tri_translated.p[0]
                normal = line_a // line_b

                # Normalize the normal
                normal.normalize()

                if normal * (tri_translated.p[0] - self.camera) < 0.0:
                    # Illuminate triangle
                    light_direction = Vec3(0.0, 0.0, -1.0).normalize()  # towards the camera
                    dot_product = light_direction * normal
                    tri_translated.angle_to_light = dot_product

                    # Project triangles
                    tri_projected = self._project_triangle(tri_translated)

                    # Scale triangle into view
                    tri_scaled = self._scale_triangle(tri_projected)

                    # Draw triangle to screen
                    self._draw_triangle(tri_scaled, window)

        return window
