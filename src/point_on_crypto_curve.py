from point import Point


class PointOnCryptoCurve(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
        assert PointOnCryptoCurve.point_is_on_curve(x, y)

    def add(self, other):
        self._check_type(other)

        if self == other:
            l = 3 * (self.x ** 2) / (2 * self.y)
        else:
            assert self.x != other.x
            l = (other.y - self.y) / (other.x - self.x)

        return self._add(other, l)

    def _add(self, other, l):
        x_res = l ** 2 - self.x - other.x
        y_res = l * (self.x - x_res) - self.y
        self.x = x_res
        self.y = y_res
        return self

    @staticmethod
    def point_is_on_curve(x, y, a=0, b=7):
        epsilon = 1e-7  # due to floating point operations
        crypto_curve = abs(y ** 2 - (x ** 3 + a * x + b))
        return crypto_curve < epsilon


if __name__ == "__main__":
    def test_addition(a, b):
        print("Adding 2 points on crypto curve")
        print(a, b)
        a.add(b)
        print("Result is on crypto curve as well: %s\n" % PointOnCryptoCurve.point_is_on_curve(*a.get_cords()))


    a = PointOnCryptoCurve(3, 5.830951894845301)
    b = PointOnCryptoCurve(2, 3.872983346207417)

    c = PointOnCryptoCurve(-1.62, 1.65785162)
    d = PointOnCryptoCurve(2.62, 4.9984725666)

    e = PointOnCryptoCurve(2.62, 4.9984725666)
    f = PointOnCryptoCurve(2.62, 4.9984725666)
    test_addition(a, b)
    test_addition(c, d)
    test_addition(e, f)
