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

    @staticmethod
    def clip_against_plane(plane_point: Vec3, plane_normal: Vec3, triangle: Triangle):
        # Normalize the normal
        plane_normal.normalize()

        # Keep track of whether point is inside/outside
        points_inside = []
        points_outside = []

        for index in range(0, 3):
            point_distance = Vec3.point_to_plane_distance(
                triangle.p[index],
                plane_point,
                plane_normal
            )

            if point_distance >= 0:
                points_inside.append(triangle.p[index])
            else:
                points_outside.append(triangle.p[index])

        # Calculate triangles based on scenarios of points_inside/points_outside
        inside_count = len(points_inside)
        outside_count = len(points_outside)

        if inside_count == 0:
            # No points in view plane, return nothing
            return []
        elif inside_count == 3:
            # All points are inside
            return [triangle]
        elif inside_count == 1 and outside_count == 2:
            # Clip as 2 points are outside, results in a smaller triangle
            # 2 outside points will become intersection points with the view plane
            triangle_out = Triangle(
                points_inside[0],
                Vec3.intersect_plane(
                    plane_point,
                    plane_normal,
                    points_inside[0],
                    points_outside[0]
                ),
                Vec3.intersect_plane(
                    plane_point,
                    plane_normal,
                    points_inside[0],
                    points_outside[1]
                ),
                triangle.angle_to_light
            )

            return [triangle_out]
        elif inside_count == 2 and outside_count == 1:
            # Results in a quad that will be split into 2 triangles
            triangle_out_1 = Triangle(
                points_inside[0],
                points_inside[1],
                Vec3.intersect_plane(
                    plane_point,
                    plane_normal,
                    points_inside[0],
                    points_outside[0]
                ),
                triangle.angle_to_light
            )

            triangle_out_2 = Triangle(
                points_inside[1],
                triangle_out_1.p[2],
                Vec3.intersect_plane(
                    plane_point,
                    plane_normal,
                    points_inside[1],
                    points_outside[0]
                ),
                triangle.angle_to_light
            )

            return [triangle_out_1, triangle_out_2]
