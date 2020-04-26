import copy
from math import sin, cos, tan, pi
from tkinter import Canvas, NW, SW, NE, SE

from math_3d.mat4x4 import Mat4x4
from math_3d.vec3 import Vec3

from pipeline.camera import Camera

from pipeline.helpers.color import Color
from pipeline.helpers.triangle import Triangle

from pipeline.helpers.model_reader import ModelReader


def get_objects_for_scene() -> [[Triangle]]:
    # For now return a list with the points of a cube
    objects = []
    #
    # cube = [
    #     # SOUTH
    #     Triangle(Vec3(0.0, 0.0, 0.0), Vec3(0.0, 1.0, 0.0), Vec3(1.0, 1.0, 0.0)),
    #     Triangle(Vec3(0.0, 0.0, 0.0), Vec3(1.0, 1.0, 0.0), Vec3(1.0, 0.0, 0.0)),
    #
    #     # EAST
    #     Triangle(Vec3(1.0, 0.0, 0.0), Vec3(1.0, 1.0, 0.0), Vec3(1.0, 1.0, 1.0)),
    #     Triangle(Vec3(1.0, 0.0, 0.0), Vec3(1.0, 1.0, 1.0), Vec3(1.0, 0.0, 1.0)),
    #
    #     # NORTH
    #     Triangle(Vec3(1.0, 0.0, 1.0), Vec3(1.0, 1.0, 1.0), Vec3(0.0, 1.0, 1.0)),
    #     Triangle(Vec3(1.0, 0.0, 1.0), Vec3(0.0, 1.0, 1.0), Vec3(0.0, 0.0, 1.0)),
    #
    #     # WEST
    #     Triangle(Vec3(0.0, 0.0, 1.0), Vec3(0.0, 1.0, 1.0), Vec3(0.0, 1.0, 0.0)),
    #     Triangle(Vec3(0.0, 0.0, 1.0), Vec3(0.0, 1.0, 0.0), Vec3(0.0, 0.0, 0.0)),
    #
    #     # TOP
    #     Triangle(Vec3(0.0, 1.0, 0.0), Vec3(0.0, 1.0, 1.0), Vec3(1.0, 1.0, 1.0)),
    #     Triangle(Vec3(0.0, 1.0, 0.0), Vec3(1.0, 1.0, 1.0), Vec3(1.0, 1.0, 0.0)),
    #
    #     # BOTTOM
    #     Triangle(Vec3(1.0, 0.0, 1.0), Vec3(0.0, 0.0, 1.0), Vec3(0.0, 0.0, 0.0)),
    #     Triangle(Vec3(1.0, 0.0, 1.0), Vec3(0.0, 0.0, 0.0), Vec3(1.0, 0.0, 0.0)),
    # ]
    #
    # objects.append(cube)

    axis = ModelReader.read_obj_model(r"models/axis.obj")
    objects.append(axis)

    # spaceship = ModelReader.read_obj_model(r"models/ship.obj")
    # objects.append(spaceship)

    # teapot = ModelReader.read_obj_model(r"models/teapot.obj")
    # objects.append(teapot)

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
        self.theta = pi/4
        self.time_diff = 1

        self.camera = Camera(Vec3(0, 0, -10))
        self.projection_matrix = self._make_projection_matrix(far, near)

        # Get objects for the scene
        self.objects = get_objects_for_scene()

    def update_camera_position(self):
        if self.camera.move_direction == "UP":
            self.camera.position.y -= 8.0 * self.time_diff

        if self.camera.move_direction == "DOWN":
            self.camera.position.y += 8.0 * self.time_diff

        if self.camera.move_direction == "LEFT":
            self.camera.position.x -= 8.0 * self.time_diff

        if self.camera.move_direction == "RIGHT":
            self.camera.position.x += 8.0 * self.time_diff

        forward_vector = self.camera.look_direction * (8.0 * self.time_diff)

        if self.camera.move_direction == "FORWARDS":
            self.camera.position += forward_vector

        if self.camera.move_direction == "BACKWARDS":
            self.camera.position -= forward_vector

        if self.camera.move_direction == "TURN_LEFT":
            self.camera.yaw -= 2.0 * self.time_diff

        if self.camera.move_direction == "TURN_RIGHT":
            self.camera.yaw += 2.0 * self.time_diff

    def _make_projection_matrix(self, far, near):
        """ Create matrix for projection with parameters defined in object """
        proj_mat = Mat4x4()
        proj_mat.m[0][0] = self.aspect_ration * self.fov_rad
        proj_mat.m[1][1] = self.fov_rad
        proj_mat.m[2][2] = far // (far - near)
        proj_mat.m[3][2] = (-far * near) / (far - near)
        proj_mat.m[2][3] = 1.0
        proj_mat.m[3][3] = 0.0

        return proj_mat

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
    def _point_at_matrix(position: Vec3, target: Vec3, up: Vec3) -> Mat4x4:
        # Calculate forward direction
        new_forward = target - position
        new_forward.normalize()

        # Calculate new Up direction
        a = new_forward * (up * new_forward)
        new_up = up - a
        new_up.normalize()

        # New right
        new_right = new_up // new_forward

        # Construct Dimensioning and translation matrix
        matrix = Mat4x4()
        matrix.m[0] = [new_right.x, new_right.y, new_right.z, 0.0]
        matrix.m[1] = [new_up.x, new_up.y, new_up.z, 0.0]
        matrix.m[2] = [new_forward.x, new_forward.y, new_forward.z, 0.0]
        matrix.m[3] = [position.x, position.y, position.z, 1.0]

        return matrix

    @staticmethod
    def _quick_inverse_matrix(original: Mat4x4) -> Mat4x4:
        matrix = Mat4x4()
        matrix.m[0][0] = original.m[0][0]
        matrix.m[0][1] = original.m[1][0]
        matrix.m[0][2] = original.m[2][0]
        matrix.m[0][3] = 0.0

        matrix.m[1][0] = original.m[0][1]
        matrix.m[1][1] = original.m[1][1]
        matrix.m[1][2] = original.m[2][1]
        matrix.m[1][3] = 0.0

        matrix.m[2][0] = original.m[0][2]
        matrix.m[2][1] = original.m[1][2]
        matrix.m[2][2] = original.m[2][2]
        matrix.m[2][3] = 0.0

        matrix.m[3][0] = -(
                original.m[3][0] * original.m[0][0] + original.m[3][1] * original.m[1][0] + original.m[3][2] *
                original.m[2][0])
        matrix.m[3][1] = -(
                original.m[3][0] * original.m[0][1] + original.m[3][1] * original.m[1][1] + original.m[3][2] *
                original.m[2][1])
        matrix.m[3][2] = -(
                original.m[3][0] * original.m[0][2] + original.m[3][1] * original.m[1][2] + original.m[3][2] *
                original.m[2][2])
        matrix.m[3][3] = 1.0

        return matrix

    @staticmethod
    def _calculate_shade_of_triangle(tri: Triangle) -> Color:
        """
        Calculate the shade of a color based on triangles angle to light

        Using color in HLS color space we can manipulate the illumination
        """
        dot_value = tri.angle_to_light
        base_color = Color(Color.RGB, 0, 255, 0)  # Use Green for now

        # Change illumination of triangle based on angle
        color_hls_form = base_color.to_hls()
        # color_hls_form[1] *= dot_value

        shade_of_triangle = Color(Color.HLS, *color_hls_form)

        return shade_of_triangle

    @staticmethod
    def _draw_triangle(tri: Triangle, window: Canvas) -> None:
        """
        Draw triangle to screen

        :param tri: Triangle to be drawn
        """
        points = [tri.p[0].x, tri.p[0].y, tri.p[1].x, tri.p[1].y, tri.p[2].x, tri.p[2].y]
        shade_of_triangle = Renderer._calculate_shade_of_triangle(tri)

        # With wireframe
        window.create_polygon(points, outline="red", fill=shade_of_triangle.to_hex())

        # window.create_polygon(points, fill=shade_of_triangle.to_hex())

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

        # update time_diff
        self.time_diff = time_diff

        # update camera position
        self.update_camera_position()

        # Get objects in scene
        objects = copy.deepcopy(self.objects)

        # Angle for rotation
        # self.theta += time_diff * 1.0

        # Setup Z and X rotation matrices
        z_rotate = Mat4x4.z_rotation_matrix(0)
        x_rotate = Mat4x4.x_rotation_matrix(0)

        # Setup Translation matrix
        translation_matrix = Mat4x4.translation_matrix(0.0, 0.0, 0.0)

        # Setup World matrix
        world_matrix = Mat4x4.multiply_matrix(z_rotate, x_rotate)
        world_matrix = Mat4x4.multiply_matrix(world_matrix, translation_matrix)

        # Make point_at matrix
        up_vector = Vec3(0, 1, 0)
        target_vector = Vec3(0, 0, 1)
        camera_rotation = Mat4x4.y_rotation_matrix(self.camera.yaw)
        self.camera.look_direction = camera_rotation * target_vector
        target_vector = self.camera.position + self.camera.look_direction

        camera_matrix = self._point_at_matrix(self.camera.position, target_vector, up_vector)
        camera_view = self._quick_inverse_matrix(camera_matrix)

        # Triangle to be drawn
        triangles_to_raster = []
        triangles_to_draw = []

        # Loop on objects in scene
        for obj in objects:
            # Loop on triangles in an object
            for tri in obj:

                # Perform Translate-Rotate-Scale matrix multiplication on triangle
                tri_transformed = tri
                tri_transformed.p[0] = world_matrix * tri.p[0]
                tri_transformed.p[1] = world_matrix * tri.p[1]
                tri_transformed.p[2] = world_matrix * tri.p[2]

                # Get normal of triangle
                line_a = tri_transformed.p[1] - tri_transformed.p[0]
                line_b = tri_transformed.p[2] - tri_transformed.p[0]
                normal = line_a // line_b
                normal.normalize()

                camera_ray = tri_transformed.p[0] - self.camera.position

                if normal * camera_ray <= 0.0:
                    # Illuminate triangle
                    light_direction = Vec3(0.0, 0.0, -1.0).normalize()  # towards the camera
                    dot_product = max(0.1, light_direction * normal)
                    tri_transformed.angle_to_light = dot_product

                    # Convert World Space into View Space
                    tri_viewed = tri_transformed
                    tri_viewed.p[0] = camera_view * tri_transformed.p[0]
                    tri_viewed.p[1] = camera_view * tri_transformed.p[1]
                    tri_viewed.p[2] = camera_view * tri_transformed.p[2]

                    # Check if triangle needs to be clipped
                    tris_clipped = Triangle.clip_against_plane(Vec3(0.0, 0.0, 0.1), Vec3(0.0, 0.0, 1.0), tri_viewed)

                    for tri_clipped in tris_clipped:
                        # Project triangles
                        tri_projected = self._project_triangle(tri_clipped)

                        # Scale triangle into view
                        tri_scaled = self._scale_triangle(tri_projected)

                        # Store triangle
                        triangles_to_raster.append(tri_scaled)

        # Sort the triangles using *z-buffer*
        triangles_to_raster.sort(key=lambda x: (x.p[0].z + x.p[1].z + x.p[2].z) / 3.0, reverse=True)

        # Clip triangle against screen edges
        triangles_to_clip = []
        for triangle in triangles_to_raster:
            new_triangles = 1
            triangles_to_clip.append(triangle)

            for p in range(0, 4):
                tris_to_add = []

                while new_triangles > 0:
                    test = triangles_to_clip.pop(0)
                    new_triangles -= 1

                    if p == 0:
                        tris_to_add = Triangle.clip_against_plane(Vec3(0, 0, 0,), Vec3(0, 1, 0), test)
                    elif p == 1:
                        tris_to_add = Triangle.clip_against_plane(Vec3(0, self.screen_height - 1, 0,), Vec3(0, -1, 0), test)
                    elif p == 2:
                        tris_to_add = Triangle.clip_against_plane(Vec3(0, 0, 0,), Vec3(1, 0, 0), test)
                    elif p == 3:
                        tris_to_add = Triangle.clip_against_plane(Vec3(self.screen_width - 1, 0, 0,), Vec3(-1, 0, 0), test)

                    triangles_to_clip += tris_to_add
                new_triangles = len(triangles_to_clip)

            # Draw triangles to screen
            for triangle in triangles_to_clip:
                self._draw_triangle(triangle, window)

        # Add debug info to window
        camera_text = (
            f"Camera:\n"
            f" X: {self.camera.position.x}\n"
            f" Y: {self.camera.position.y}\n"
            f" Z: {self.camera.position.z}\n"
            f" Yaw: {self.camera.yaw}"
        )

        triangle_count = 0
        for obj in objects:
            triangle_count = triangle_count + len(obj)

        triangle_text = (
            "Triangles:\n"
            f" Total: {triangle_count}\n"
            f" Drawn: {len(triangles_to_draw)}"
        )

        window.create_text(5, 5, anchor=NW, text=camera_text, fill="red")
        window.create_text(5, 100, anchor=NW, text=triangle_text, fill="red")

        return window
