from tkinter import (
    Canvas,
    Tk,
)
import time

from input.CameraMovement import CameraMovement
from pipeline.renderer import Renderer

if __name__ == "__main__":
    print("3D engine written in Python3.6")
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
    time_diff = 1
    # Pack event handler
    camera_movement_handler = CameraMovement(ren.camera)
    top.bind("<KeyPress>", camera_movement_handler.handle_input)
    top.bind("<KeyRelease>", camera_movement_handler.clear_movement)

    # Main loop
    while True:
        # Set FPS
        top.title(f"Python Engine 3D - FPS: {(1 / time_diff):.0f}")

        # Render frame, display it and get update from GUI
        rendered_frame = ren.render_frame(window, time_diff)
        rendered_frame.update_idletasks()
        rendered_frame.update()

        # Calculate time difference used for keeping stuff in sync
        time_2 = time.time()
        time_diff = time_2 - time_1
        time_1 = time_2
