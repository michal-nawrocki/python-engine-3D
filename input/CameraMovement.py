"""
Handling of moving a camera
"""

import copy
import platform
from pipeline.camera import Camera
from helpers.loggers import get_a_logger

_LOGGER = get_a_logger(__name__)


class CameraMovement:

    up_controls = ['w', 'Up']
    down_controls = ['s', 'Down']
    left_controls = ['a', 'Left']
    right_controls = ['d', 'Right']

    forward_controls = ["8", "z"]
    backward_controls = ["2", "x"]
    turn_left_controls = ["4", "q"]
    turn_right_controls = ["6", "e"]

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

        if event.keysym in ["space"]:
            self.camera.move_direction = None

        # Reset to original value
        if event.keysym in ["r"]:
            self.camera.move_direction = None
            self.camera.yaw = 0
            self.camera.position = copy.deepcopy(self.camera.origin)

    def clear_movement(self, event):
        _LOGGER.info(f"Key released: {event}")

        if "Windows" in platform.platform():
            self.camera.move_direction = None
