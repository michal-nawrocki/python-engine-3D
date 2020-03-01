"""
Color representation stored in an object.
Can cast color to RGB and HLS representations.

For  calculating shadows, RGB doesn't have a `intensity` parameter allowing for
brighter or darker colors. One solution to this problem is using HLS
(Hue, Luminance, Saturation) representation of RGB color space.
"""
import colorsys
from typing import Union


class Color:
    """
    Simple color class to keep color values and allow for conversion
    between color spaces [RGB, HLS]
    """
    RGB = "rgb"
    HLS = "hls"

    def __init__(self, space: Union[RGB, HLS], *args):
        if len(args) != 3:
            raise ValueError("There can be only 3 values for a color space")

        # Validate that values are correct
        Color.__validate_values(space, args)

        self.space = space
        self.color_values = args

    def to_rgb(self):
        values = list(self.color_values)

        # Check if we're already RGB
        if self.space == Color.RGB:
            return values

        # Convert Hue to float value
        values[0] = values[0]/360

        # Get converted colors from HLS to RGB as floats
        converted = colorsys.hls_to_rgb(*values)

        # Convert those floats to ints in range [0, 255]
        converted = list(map(lambda value: round(value*255), converted))
        return converted

    def to_hls(self):
        # Check if we're already hls
        if self.space == Color.HLS:
            return list(self.color_values)

        # Convert RGB ints to floats
        as_floats = list(map(lambda value: round(value/255), self.color_values))

        # Convert to HLS
        converted = list(colorsys.rgb_to_hls(*as_floats))

        # Represent Hue as degrees
        converted[0] = round(converted[0]*360)

        return converted

    def to_hex(self):
        # Get RGB representation
        as_rgb = self.to_rgb()

        # To hex
        as_hex = "#%02x%02x%02x" % tuple(as_rgb)
        return as_hex

    @staticmethod
    def __validate_values(space, args):
        if space == Color.RGB:
            Color.__check_rgb_values(args)
        elif space == Color.HLS:
            Color.__check_hls_values(args)
        else:
            raise ValueError(f"Wrong value: {space} - Value of color space has"
                             f"to be {Color.HLS}, {Color.RGB}")

    @staticmethod
    def __check_rgb_values(values):
        # RGB values have to be between 0 and 255
        for value in values:
            if isinstance(value, int) and 0 <= value <= 255:
                continue
            else:
                raise ValueError(f"Wrong value: {value} - Values for RGB have"
                                 "to be between 0 and 255.")

    @staticmethod
    def __check_hls_values(values):
        hue = values[0]
        # Hue has to be between [0, 360]
        if not (isinstance(hue, int) and 0 <= hue <= 360):
            raise ValueError(f"Wrong value for Hue: {hue} - Hue has to be"
                             "between 0 and 360")

        # Check Luminance and Saturation
        for index in range(1, 3):
            val = values[index]
            if not 0 <= val <= 1:
                raise ValueError(f"Wrong value: {val} - Luminance and "
                                 "Saturation have to be between 0 and 1")
