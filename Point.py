class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.a = 1

    # a in curve y^2 = x^3 + ax + b
    def add(self, other):
        if other.x != self.x and other.y != self.y:
            # lambda λ = (y2−y1)/(x2−x1)
            lam = (other.y - self.y) / (other.x - self.x)

            # ν = y1 − λ*x1
            v = self.y - lam * self.x

            # x3 = λ^2 − x1 − x2
            x3 = lam ** 2 - self.x - other.x
            # y3 = λ*x3 + v
            y3 = lam * x3 + v

            self.x, self.y = x3, -y3
            return self.x, self.y
        else:
            self.add_equal()

    def add_equal(self):

            # lambda λ = (3 * x1^2 + a) / 2 * y1
            lam = (3 * (self.x**2) + self.a) / 2 * self.y

            # ν = y1 − λ*x1
            v = self.y - lam * self.x

            # x3 = λ^2 − 2 * x1
            x3 = lam ** 2 - 2 * self.x
            # y3 = λ*x3 + v
            y3 = lam * x3 + v

            self.x, self.y = x3, -y3
            return self.x, self.y


def test():
    a = Point(2, 4)
    b = Point(3, 1)

    c = a.add(b)
    d = b.add_equal()

    print("a + b = ", c)
    print("b + b = ", d)


if __name__ == "__main__":
    test()
