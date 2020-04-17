"""
Handling of moving a camera
"""

from math_3d.vec3 import Vec3
from pipeline.camera import Camera


class CameraMovement:

    up_controls = ['w', 'Up', 100]
    down_controls = ['s', 'Down']
    left_controls = ['a', 'Left']
    right_controls = ['d', 'Right']
    forward_controls = ["z"]
    backward_controls = ["x"]

    def __init__(self, camera: Camera):
        self.camera = camera

    def handle_input(self, event):
        print(f"Pressed key: {event}")
        if event.keysym in self.up_controls:
            self.camera.move_direction = "UP"

        if event.keysym in self.down_controls:
            self.camera.move_direction = "DOWN"

        if event.keysym in self.left_controls:
            self.camera.move_direction = "LEFT"

        if event.keysym in self.right_controls:
            self.camera.move_direction = "RIGHT"

        if event.keysym in self.forward_controls:
            self.camera.move_direction = "FORWARDS"

        if event.keysym in self.backward_controls:
            self.camera.move_direction = "BACKWARDS"

    def clear_movement(self, event):
        print(f"Key released: {event}")
        self.camera.move_direction = None
