class Curve(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Y^2 = X^3 + {}X + {}".format(self.a, self.b)

    __repr__ = __str__


class Point(object):
    def __init__(self, x, y, curve):
        self.x = x
        self.y = y
        assert type(curve) == Curve, "Should be {Curve} object"
        self.curve = curve

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __iadd__(self, other):
        lambda_up = other.y - self.y
        lambda_down = other.x - self.x
        if lambda_down == 0:
            if lambda_up == 0:
                lambda_up = 3 * (self.x ** 2) + self.curve.a
                lambda_down = 2 * self.y
            else:
                raise ValueError("infinity point")

        lambda_ = lambda_up / float(lambda_down)
        x = lambda_ ** 2 - self.x - other.x
        y = lambda_ * (self.x - x) - self.y
        self.x = x
        self.y = y
        return self

    def __str__(self):
        return "x:{}; y:{}".format(self.x, self.y)


if __name__ == "__main__":
    curve = Curve(*[1, 1])
    print(curve)
    p1 = Point(0, 1, curve)
    print(p1)

    p2 = Point(1, 3**0.5, curve)
    print(p2)

    p1 += p2
    print(p1)
