from tkinter import (
    Canvas,
    Tk,
    NW,
    W,
    N,
)
import time

from input.CameraMovement import CameraMovement
from helpers.loggers import get_a_logger
from pipeline.renderer import Renderer


_LOGGER = get_a_logger(__name__)


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
        try:
            top.title(f"Python Engine 3D - FPS: {(1 / time_diff):.0f}")
        except ZeroDivisionError:
            top.title(f"Python Engine 3D - FPS: 0")

        # Render frame, display it and get update from GUI
        rendered_frame = ren.render_frame(window, time_diff)

        # Add text to it

        # Add debug info to window
        camera_text = (
            f"Camera:\n"
            f" X: {ren.camera.position.x}\n"
            f" Y: {ren.camera.position.y}\n"
            f" Z: {ren.camera.position.z}\n"
            f" Yaw: {ren.camera.yaw}"
        )

        rendered_frame.create_text(5, 5, anchor=NW, text=camera_text, fill="red")

        rendered_frame.update_idletasks()
        rendered_frame.update()

        # Calculate time difference used for keeping stuff in sync
        time_2 = time.time()
        time_diff = time_2 - time_1
        time_1 = time_2
