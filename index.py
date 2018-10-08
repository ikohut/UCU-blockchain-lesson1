import MI


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mod = 29

    def add(self, P):
        numerator = 3 * (self.x ** 2)
        denominator = 2 * self.y
        if P.x != self.x and P.y != self.y:
            numerator = P.y - self.y
            denominator = P.x - self.x
        s = self.slope(numerator, denominator)
        x = (s ** 2 - self.x - P.x) % self.mod
        y = (self.y + s * (x - self.x)) % self.mod
        return Point(x, -y)

    def slope(self, numerator, denominator):
        _denominator = MI.multiplicative_inverse(denominator, self.mod)
        s = (numerator / _denominator) % self.mod
        return s

    def __str__(self):
        return "({:.3f}, {:.3f})".format(self.x, self.y)


P = Point(18, 1.0)
R = Point(2, 9.5)
print('2P =', P.add(P))
print('2R =', R.add(R))
print('P + R =', P.add(R))
