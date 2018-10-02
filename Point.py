class Point:
    def __init__(self, x, y):
        self.x = x,
        self.y = y

    def add(self, other):
        if other.x[0] != self.x[0] and other.y != self.y:
            # lambda λ = (y2−y1)/(x2−x1)
            lam = (other.y - self.y) / (other.x[0] - self.x[0])

            # ν = y1 − λ*x1
            v = self.y - lam * self.x[0]

            # x3 = λ^2 − x1 − x2
            x3 = lam ** 2 - self.x[0] - other.x[0]
            # y3 = λ*x3 + v
            y3 = lam * x3 + v

            self.x = x3
            self.y = y3
            return self.x, self.y
        else:
            self.add_equal(other)

    def add_equal(self, a):

            # lambda λ = (3 * x1^2 + a) / 2 * y1
            lam = (3 * (self.x[0]**2) + a) / 2 * self.y

            # ν = y1 − λ*x1
            v = self.y - lam * self.x[0]

            # x3 = λ^2 − 2 * x1
            x3 = lam ** 2 - 2 * self.x[0]
            # y3 = λ*x3 + v
            y3 = lam * x3 + v

            self.x = x3
            self.y = y3
            return self.x, self.y


def test():
    a = Point(2, 4)
    b = Point(3, 1)

    c = a.add(b)
    # need a in curve y^2 = x^3 + ax + b
    d = b.add_equal(0)

    print("a + b = ", c)
    print("b + b = ", d)


if __name__ == "__main__":
    test()
