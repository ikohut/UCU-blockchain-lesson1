from point import Point
import utils
from crypto_curve import CryptoCurve


class PointOnCryptoCurve(Point):
    crypto_curve = CryptoCurve(**{"a": 0, "b": 7, "p": 131})

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
        mod = PointOnCryptoCurve.crypto_curve.p
        l_denominator_MI = utils.multiplicative_inverse(l_denominator, mod)
        l = (l_numerator * l_denominator_MI) % mod
        x_res = (l ** 2 - self.x - other.x) % mod
        y_res = (l * (self.x - x_res) - self.y) % mod
        self.x = x_res
        self.y = y_res
        return self

    @staticmethod
    def point_is_on_curve(x, y):
        a, b, p = PointOnCryptoCurve.crypto_curve.get_params()
        lefths = y ** 2
        rigthhs = x ** 3 + a * x + b
        return lefths % p == rigthhs % p

