from Curve import Curve

class Point:
    def __init__(self, x, y, curve):
        self._x = x
        self._y = y
        self._curve = curve

    def add(self, other):
        if self._x == other.get_x():
            # the result goes to infinity
            self._x = float("inf")
            self._y = float("inf")
            return

        if self._x == other.get_x() and self._y == other.y:
            lamb = (3 * self._x ** 2 + self._curve.get_a()) / 2 * self._y
        else:
            lamb = (other.get_y() - self._y) / (other.get_x() - self._x)

        v = self._y - lamb * self._x

        # finding new values(y is reflected)
        x3 = lamb ** 2 - self._x - other.get_x()
        y3 = lamb * x3 + v

        self._x = x3
        self._y = y3

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


def test_ctypto_scalar_operations():
    elipcurve = Curve(1, 2)
    p1 = Point(-1, 0, elipcurve)
    p2 = Point(0, 1.414, elipcurve)

    print("p1 is on curve: ", elipcurve.check_if_point_is_on_curve(p1))
    print("p2 is on curve: ", elipcurve.check_if_point_is_on_curve(p2))

    p1.add(p2)

    print("p3 is on curve: ", elipcurve.check_if_point_is_on_curve(p1))

    print("P1 + P2 = Point({}, {})".format(p1.get_x(), p1.get_y()))


if __name__ == "__main__":
    test_ctypto_scalar_operations()
