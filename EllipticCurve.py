class EllipticCurve:
    """
    y^2 = x^3 + ax + b

    """

    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def get_params(self):
        return self.a, self.b, self.p

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.p == other.p

    def __str__(self):
        return "a: {}, b: {}, p: {}".format(self.a, self.b, self.p)
