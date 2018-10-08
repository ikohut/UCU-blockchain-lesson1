class Point():
    """
    Implementation of the point on elliptic curve : y^2=x^3+ax+b
    """
    def __init__(self, x, y, a, b):
        self.y = y
        self.x = x
        self.a = a
        self.b = b
        self.__check_point_on_curve__()

    def __check_point_on_curve__(self):
        if self.x is None and self.y is None:
            return
        if int((self.y ** 2)%3) != int((self.x ** 3 + self.a * self.x + self.b)%3):   # mod3
            raise ValueError('Point ({},{}) is not on the curve'.format(self.x, self.y))

    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        """
        For any two points addition process:
            1) draw a line through the two points
            2) find the point intersects the elliptic curve a third time
            2) reflect this point over the x-axis
        :return:
        """
        if self.x is None:
            return other
        if other.x is None:
            return self

        if self.a != other.a or self.b != other.b:
            raise TypeError('Points {}, {} are not on the same curve'.format(self, other))

        if self.x != other.x:
            s = (other.y - self.y) / (other.x - self.x)
            x_new = s**2 - self.x - other.x
            y_new = s*(self.x - x_new) - self.y
            return Point(x=x_new, y=y_new, a=self.a, b=self.b)

        if self == other:
            s = (3*self.x**2 + self.a) / (2*self.y)
            x_new = s**2 - 2*self.x
            y_new = s*(self.x - x_new) - self.y
            return Point(x=x_new, y=y_new, a=self.a, b=self.b)


def test():
    # Test 1
    assert Point(-30, -1, 5, 7), ValueError

    # Test 2
    p1 = Point(-1, -1, 5, 7)
    p2 = Point(-1, 1, 5, 7)
    inf = Point(None, None, 5, 7)
    assert p1 + inf, Point(-1, -1, 5, 7)
    assert inf + p2, Point(-1, 1, 5, 7)

    # Test 3
    a = Point(x=3, y=7, a=5, b=7)
    b = Point(x=-1, y=-1, a=5, b=7)
    assert a + b, Point(x=2, y=-5, a=5, b=7)
    # print(a+b)

    # Test 4
    a = Point(x=-1, y=1, a=5, b=7)
    assert a + a, Point(x=18, y=-77, a=5, b=7)

test()
