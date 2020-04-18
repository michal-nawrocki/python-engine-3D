"""
Handling of moving a camera
"""

from pipeline.camera import Camera
from helpers.loggers import get_a_logger

_LOGGER = get_a_logger(__name__)


class CameraMovement:

    up_controls = ['w', 'Up']
    down_controls = ['s', 'Down']
    left_controls = ['a', 'Left']
    right_controls = ['d', 'Right']

    forward_controls = ["8"]
    backward_controls = ["2"]
    turn_left_controls = ["4"]
    turn_right_controls = ["6"]

    def __init__(self, camera: Camera):
        self.camera = camera

    def handle_input(self, event):
        _LOGGER.info(f"Pressed key: {event}")

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

        if event.keysym in self.turn_left_controls:
            self.camera.move_direction = "TURN_LEFT"

        if event.keysym in self.turn_right_controls:
            self.camera.move_direction = "TURN_RIGHT"

    def clear_movement(self, event):
        _LOGGER.info(f"Key released: {event}")
        self.camera.move_direction = None
