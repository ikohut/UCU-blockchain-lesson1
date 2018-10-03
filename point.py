# source - https://jeremykun.com/2014/02/24/elliptic-curves-as-python-objects/
from elliptic_curve import EllipticCurve


# This class is supposed to represent a point on an elliptic curve
class Point(object):
    def __init__(self, curve, x, y):
        self.curve = curve  # the curve containing this point
        self.x = x
        self.y = y

        if not curve.testPoint(x, y):
            raise Exception("The point %s is not on the given curve %s" % (self, curve))

    def __str__(self):
        return '(%G, %G)' % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Ideal):
            return self

        x_1, y_1, x_2, y_2 = self.x, self.y, other.x, other.y

        if (x_1, y_1) == (x_2, y_2):
            if y_1 == 0:
                return Ideal(self.curve)

            # slope of the tangent line
            m = (3 * x_1 * x_1 + self.curve.a) / (2 * y_1)
        else:
            if x_1 == x_2:
                return Ideal(self.curve)

            # slope of the secant line
            m = (y_2 - y_1) / (x_2 - x_1)

        x_3 = m * m - x_2 - x_1
        y_3 = m * (x_3 - x_1) + y_1

        return Point(self.curve, x_3, -y_3)


class Ideal(Point):
    """
    Ideal point is a point (0,0).
    """
    def __init__(self, curve):
        self.curve = curve

    def __str__(self):
        return "Ideal"

    def __add__(self, other):
        return other


curve = EllipticCurve(a=-2, b=4)
print(curve)
a = Point(curve, 3, 5)
b = Point(curve, -2, 0)
print(a + b)
print(a + a)
print(b + b)

