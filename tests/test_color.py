import unittest
from pipeline.helpers.color import Color


class TestColor(unittest.TestCase):
    """
    Unit tests for Color
    """

    def test_color(self):
        """Test color constructor on happy path"""
        temp_rgb = Color(Color.RGB, 0, 255, 0)
        temp_hls = Color(Color.HLS, 0, 1, 1)

        self.assertIsInstance(temp_rgb, Color)
        self.assertIsInstance(temp_hls, Color)

    def test_raises_args_length(self):
        """Test constructor raises if there aren't 3 values"""
        with self.assertRaises(ValueError):
            Color(Color.RGB, 0)

    def test_raises_wrong_space(self):
        """Test constructor raises if wrong color space used"""
        with self.assertRaises(ValueError):
            Color("wrong value", 0, 0, 0)

    def test_raises_rgb_beyond_range(self):
        """Test constructor raises if RGB values beyond range[0,255]"""
        with self.assertRaises(ValueError):
            Color(Color.RGB, 0, 0, -1)
            Color(Color.RGB, 0, 0, 256)

    def test_raises_hue_wrong_value(self):
        """Test constructor raises if Hue beyond range[0, 360]"""
        with self.assertRaises(ValueError):
            Color(Color.HLS, -2, 0, 0)
            Color(Color.HLS, 361, 0, 0)

    def test_rgb_to_hls(self):
        """Test green rgb conversion to hls"""
        green_as_rgb = Color(Color.RGB, 0, 255, 0)
        self.assertEqual([120, 0.5, 1.0], green_as_rgb.to_hls())

    def test_hls_to_rgb(self):
        """Test hls conversion to rgb"""
        green_as_hls = Color(Color.HLS, 120, 0.5, 1.0)
        self.assertEqual([0, 255, 0], green_as_hls.to_rgb())

        red_as_hls = Color(Color.HLS, 0, 0.5, 1.0)
        self.assertEqual([255, 0, 0], red_as_hls.to_rgb())

        black_as_hls = Color(Color.HLS, 360, 0, 0)
        self.assertEqual([0, 0, 0], black_as_hls.to_rgb())

        black_as_hls_2 = Color(Color.HLS, 34, 0, 0)
        self.assertEqual([0, 0, 0], black_as_hls_2.to_rgb())

        white_as_hls = Color(Color.HLS, 357, 1, 0.21)
        self.assertEqual([255, 255, 255], white_as_hls.to_rgb())
