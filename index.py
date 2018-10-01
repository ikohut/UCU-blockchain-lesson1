class Point:
    def __init__(self, x, y):
        # elliptic curve equation:  y^2 = x^3 + ax + b
        self.x = x
        self.y = y

    def add(self, P):
        if P.x == self.x and P.y == self.y:
            # build slope to the curve in point P
            return self.double()
        try:
            s = (P.y - self.y) / (P.x - self.x)
        except ZeroDivisionError:
            return Point(float('inf'), float('inf'))
        x = s ** 2 - self.x - P.x
        y = self.y + s * (x - self.x)
        return Point(x, -y)

    def double(self):
        # s = (3x^2 + a) / 2y
        try:
            s = (3 * (self.x ** 2)) / (2 * self.y)
        except ZeroDivisionError:
            return Point(float('inf'), float('inf'))
        x = s ** 2 - 2 * self.x
        y = self.y + s * (x - self.x)
        return Point(x, -y)

    def __str__(self):
        return "({:.3f}, {:.3f})".format(self.x, self.y)


P = Point(1, 3)
R = Point(0.8, 2)
print('2P =', P.add(P))
print('2R =', R.add(R))
print('P + R =', P.add(R))
