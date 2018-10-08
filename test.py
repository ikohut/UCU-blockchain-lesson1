import unittest
from point import Point


class TestPoint(unittest.TestCase):

    def setUp(self):
        pass

    def test_eq(self):
        a = Point(a=5, b=7, x=3, y=-7)
        b = Point(a=5, b=7, x=18, y=77)
        self.assertFalse(a == b)
        self.assertTrue(a == a)

    def test_add_opposite(self):
        b = Point(a=5, b=7, x=2, y=5)
        c = Point(a=5, b=7, x=2, y=-5)
        b + c
        self.assertEqual(b, Point(a=5, b=7, x=None, y=None))

    def test_add_infinity_point(self):
        a = Point(a=5, b=7, x=None, y=None)
        b = Point(a=5, b=7, x=2, y=5)
        a + b
        self.assertEqual(a, b)

    def test_add_infinity_point_2(self):
        a = Point(a=5, b=7, x=None, y=None)
        b = Point(a=5, b=7, x=2, y=5)
        b + a
        self.assertEqual(b, Point(a=5, b=7, x=2, y=5))

    def test_add_self(self):
        a = Point(a=5, b=7, x=-1, y=1)
        a + a
        self.assertEqual(a, Point(a=5, b=7, x=18, y=-77))

    def test_add_p1_not_equal_p2(self):
        a = Point(a=5, b=7, x=3, y=7)
        b = Point(a=5, b=7, x=-1, y=-1)
        a + b
        self.assertEqual(a, Point(a=5, b=7, x=2, y=-5))


if __name__ == '__main__':
    unittest.main()


