class Curve(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Y^2 = X^3 + {}X + {}".format(self.a, self.b)

    __repr__ = __str__

    def __contains__(self, item):
        assert isinstance(item, Point), "Should be {Point} object"
        return item.y ** 2 == item.x ** 3 + item.x * self.a + self.b


class Point(object):
    def __init__(self, x, y, curve):
        self.x = x
        self.y = y
        assert isinstance(curve, Curve), "Should be {Curve} object"
        self.curve = curve
        assert self in self.curve

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        if isinstance(other, Ideal):
            return self

        lambda_up = other.y - self.y
        lambda_down = other.x - self.x
        if lambda_down == 0:
            if lambda_up == 0:
                if self.y == 0:
                    return Ideal(self.curve)
                lambda_up = 3 * (self.x ** 2) + self.curve.a
                lambda_down = 2 * self.y
            else:
                return Ideal(self.curve)

        lambda_ = lambda_up / lambda_down
        x = lambda_ ** 2 - self.x - other.x
        y = lambda_ * (self.x - x) - self.y
        return Point(x, y, self.curve)

    def __str__(self):
        return "x:{}; y:{}".format(self.x, self.y)


class Ideal(Point):
    def __init__(self, curve):
        super(Ideal, self).__init__(0, 0, curve)

    def __str__(self):
        return "Ideal"

    def __add__(self, other):
        return other


if __name__ == "__main__":
    import fractions
    frac = fractions.Fraction
    curve = Curve(*[frac(1), frac(1)])
    print(curve)
    p1 = Point(frac(0), frac(1), curve)
    print(p1)

    p2 = Point(frac(0), frac(1), curve)
    print(p2)

    p1 += p2
    print(p1)
