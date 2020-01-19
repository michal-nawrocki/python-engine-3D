from math_3d.mat4x4 import Mat4x4
from pipeline.renderer import Renderer

if __name__ == "__main__":
    print("3D engine written in Python3.6")

    matrix = Mat4x4()
    matrix.m[0] = [1, 2, 3, 4]
    matrix.m[3] = [5, 4, 3, 2]

    matrix.print_matrix()

    ren = Renderer(
        near=0.1,
        far=100.,
        fov=90.,
        screen_height=256,
        screen_width=240,
    )

    ren.run()

