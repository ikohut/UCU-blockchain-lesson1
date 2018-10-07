from point import Point
import utils


class PointOnCryptoCurve(Point):
    crypto_curve = {"a": 0, "b": 7, "p": 131}

    def __init__(self, x, y):
        super().__init__(x, y)
        assert PointOnCryptoCurve.point_is_on_curve(x, y)

    def add(self, other):
        self._check_type(other)

        l_numerator = (other.y - self.y)
        l_denominator = (other.x - self.x)

        if self == other:
            l_denominator = (2 * self.y)
            l_numerator = 3 * (self.x ** 2)
        elif self.x == other.x:
            return "point at infinity"

        return self._add(other, l_numerator, l_denominator)

    def _add(self, other, l_numerator, l_denominator):
        mod = PointOnCryptoCurve.crypto_curve["p"]
        l_denominator_MI = utils.multiplicative_inverse(l_denominator, mod)
        l = (l_numerator * l_denominator_MI) % mod
        x_res = (l ** 2 - self.x - other.x) % mod
        y_res = (l * (self.x - x_res) - self.y) % mod
        self.x = x_res
        self.y = y_res
        return self

    @staticmethod
    def point_is_on_curve(x, y):
        a = PointOnCryptoCurve.crypto_curve["a"]
        b = PointOnCryptoCurve.crypto_curve["b"]
        p = PointOnCryptoCurve.crypto_curve["p"]
        lefths = y ** 2
        rigthhs = x ** 3 + a * x + b
        return lefths % p == rigthhs % p


if __name__ == "__main__":
    def test_addition(a, b):
        print("Adding 2 points on crypto curve")
        print(a, b)
        a.add(b)
        print("Result: %s" % a)
        print("It is on crypto curve as well: %s\n" % PointOnCryptoCurve.point_is_on_curve(*a.get_cords()))


    a = PointOnCryptoCurve(5, 1.0)
    b = PointOnCryptoCurve(9, 9.0)

    c = PointOnCryptoCurve(20, 4)
    d = PointOnCryptoCurve(38, 11)

    test_addition(a, b)
    test_addition(a, c)
    test_addition(b, b)
    test_addition(c, d)
