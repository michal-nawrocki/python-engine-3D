from tkinter import *
import time

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
        screen_height=600,
        screen_width=600,
    )

    top = Tk()
    top.title("Python Engine 3D")
    window = Canvas(top, bg="black", width=600, height=600)
    window.pack()
    time_1 = time.time()
    time_2 = time.time()

    # Main loop
    while True:
        # Calculating time difference used for keeping stuff in sync
        time_2 = time.time()
        time_diff = time_2 - time_1
        time_1 = time_2

        # Set FPS
        top.title(f"Python Engine 3D - FPS: { 1 / time_diff}")

        # Render frame, display it and get update from GUI
        rendered_frame = ren.render_frame(window, time_diff)
        rendered_frame.update_idletasks()
        rendered_frame.update()
