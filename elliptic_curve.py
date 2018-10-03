class EllipticCurve(object):
    def __init__(self, a, b):
        # assume we're already in the Weierstrass form
        self.a = a
        self.b = b

        self.discriminant = -16 * (4 * a * a * a + 27 * b * b)
        if not self.isSmooth():
            raise Exception("The curve %s is not smooth!" % self)

    def isSmooth(self):
        return self.discriminant != 0

    def testPoint(self, x, y):
        return y * y == x * x * x + self.a * x + self.b

    def __str__(self):
        return 'y^2 = x^3 + %Gx + %G' % (self.a, self.b)

    def __eq__(self, other):
        return (self.a, self.b) == (other.a, other.b)
