class EllipticCurve(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

        self.discriminant = -16 * (4 * pow(a, 3) + 27 * pow(b, 2))
        if self.discriminant == 0:
            raise Exception("The discriminant is not equal to zero. The definition of the elliptic "
                            "curve requires that the curve be non-singular." % self)

    def __str__(self):
        return 'EllipticCurve: y^2 = x^3 + %dx + %d' % (self.a, self.b)
