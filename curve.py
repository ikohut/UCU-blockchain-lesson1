class EllipticCurve(object):
    """
    This class represents Elliptic Curve of the form:
    y^2 = x^3 + ax + b

    >>> print(EllipticCurve(a=17, b=1))
    y^2 = x^3 + 17x + 1

    >>> EllipticCurve(a=0, b=0)
    Traceback (most recent call last):
        ...
    Exception: The curve y^2 = x^3 + 0x + 0 is not smooth!
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b

        self.discriminant = -16 * (4 * a*a*a + 27 * b * b)
        if not self.isSmooth():
            raise Exception("The curve %s is not smooth!" % self)

    def isSmooth(self):
        return self.discriminant != 0

    def testPoint(self, x, y):
        """
        This function checks if a Point belongs to the given Elliptic Curve.
        
        >>> EllipticCurve(a=0, b=3).testPoint(1, 2)
        True
        >>> EllipticCurve(a=3, b=2).testPoint(1, 1)
        False
        """
        return y**2 == x**3 + self.a * x + self.b

    def __str__(self):
        return "y^2 = x^3 + {0}x + {1}".format(self.a, self.b)

    def __eq__(self, other):
        return (self.a, self.b) == (other.a, other.b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()