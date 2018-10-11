class Curve:
    def __init__(self, a, b):
        self._a = a
        self._b = b

        if self.discriminant() == 0:
            raise DiscriminantEqualsToZero(
                "The discriminant of this curve with params A={}, B={} equals to 0".format(a, b))

    def discriminant(self):
        return 4 * self._a ** 3 + 27 * self._b ** 2

    def check_if_point_is_on_curve(self, point):
        left = point.get_y() ** 2
        right = point.get_x() ** 3 + self._a * point.get_x() + self._b
        if abs(left - right) < 0.01:
            return True

        return False

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b


class DiscriminantEqualsToZero(Exception):
    pass
