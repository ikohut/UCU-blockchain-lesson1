from point import Point


class PointOnCryptoCurve(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
        assert PointOnCryptoCurve.point_is_on_curve(x, y)

    @staticmethod
    def point_is_on_curve(x, y):
        epsilon = 1e-14  # due to floating point operations
        crypto_curve = abs(y ** 2 - (x ** 3 + 7))
        return crypto_curve < epsilon


if __name__ == "__main__":
    a = PointOnCryptoCurve(3, 5.830951894845301)
    a = PointOnCryptoCurve(2, 3.872983346207417)
