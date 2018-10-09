class Point:
    # curve y^2 = x^3 + ax + b
    # with a,b = 1 and mod = 3
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.a = 2
        self.b = 2
        self.mod = 17

    def add(self, other):
        if other.x != self.x and other.y != self.y:
            # lambda λ = (y2−y1)*(x2−x1)**(-1)mod p , mod inverse
            lam = (other.y - self.y) * pow(other.x - self.x, self.mod - 2, self.mod)

            x3 = (lam ** 2 - self.x - other.x) % self.mod   # x3 = λ^2 − x1 − x2 mod p
            y3 = (lam * (self.x - x3) - self.y) % self.mod  # y3 = λ*(x1−x3)−y1 mod p
            self.x, self.y = int(x3), int(y3)
        else:
            # lambda λ = (3 * x1^2 + a) * (2*y1)**(-1) mod p , mod inverse
            lam = (3 * (self.x ** 2) + self.a) * pow(2 * self.y, self.mod - 2, self.mod)

            x3 = (lam ** 2 - 2 * self.x) % self.mod     # x3 = λ^2 − 2*x1 mod p
            y3 = (lam*(self.x - x3) - self.y) % self.mod    # y3 = λ*(x1−x3)−y1 mod p
            self.x, self.y = int(x3), int(y3)
        return self.x, self.y


def test():
    a = Point(5, 1)
    b = Point(16, 13)

    c = a.add(b)    # (0, 6)
    d = b.add(b)    # (0, 11)
    print("a + b =", c)
    print("b + b =", d)


if __name__ == "__main__":
    test()
