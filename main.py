import math

from Point import Point
from EllipticCurve import EllipticCurve
import unittest


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.curve_1 = EllipticCurve(5, 2, 7)

    def test_two_diff_points(self):
        point_1 = Point(0, 3, self.curve_1)
        point_2 = Point(3, 3, self.curve_1)
        point_1.add(point_2)
        self.assertTrue(point_1 == Point(4, 4, self.curve_1))

    def test_add_to_itself(self):
        self.curve_1 = EllipticCurve(5, 2, 7)
        point_1 = Point(1, 1, self.curve_1)
        point_1.add(point_1)
        self.assertTrue(point_1 == Point(0, 3, self.curve_1))

    def test_add_point_to_inf(self):
        self.curve_1 = EllipticCurve(5, 2, 7)
        point_1 = Point(math.inf, math.inf, self.curve_1)
        point_2 = Point(0, 3, self.curve_1)
        point_1.add(point_2)
        self.assertTrue(point_1 == Point(0, 3, self.curve_1))

    def test_add_inf_to_point(self):
        self.curve_1 = EllipticCurve(5, 2, 7)
        point_1 = Point(math.inf, math.inf, self.curve_1)
        point_2 = Point(0, 4, self.curve_1)
        point_2.add(point_1)
        self.assertTrue(point_2 == Point(0, 4, self.curve_1))

    def test_add__two_inf(self):
        self.curve_1 = EllipticCurve(5, 2, 7)
        point_1 = Point(math.inf, math.inf, self.curve_1)
        point_2 = Point(math.inf, math.inf, self.curve_1)
        point_1.add(point_2)
        self.assertTrue(point_2 == Point(math.inf, math.inf, self.curve_1))


if __name__ == '__main__':
    unittest.main()
