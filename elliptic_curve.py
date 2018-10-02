

class Point():
    """
    Class Point implements the point on
    elliptic curve: y^2 = x^3 + ax + b
    """

    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b

        if self.x == float("inf") or self.y == float("inf"):
            pass
        elif self.y**2 != self.x**3 + self.a*self.x + self.b:
            print('Point ({},{}) does not belong to the curve'.format(self.x, self.y))


    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            print('Points {}, {} does not belong to the same curve'.format(self, other))

        # The points at infinity
        if self.x == float("inf"): return other
        elif other.x == float("inf"): return self

        # The points are in a vertical line
        elif self.x == other.x and self.y == -other.y:  return float('inf')

        # The points where x_1 != x_2
        elif self.x != other.x:
            s = (other.y - self.y)/(other.x - self.x)
            x_3 = s**2 - self.x - other.x
            y_3 = s*(self.x - x_3) - self.y
            return Point(x_3, y_3, self.a, self.b)

        # The two points are the same
        if self.x == other.x and self.y == other.y:
            if self.y == 0:
                x_3, y_3 = float("inf"), float("inf")
            else:
                s = (3*self.x**2 + self.a)/2*self.y
                x_3 = s**2 - 2*self.x
                y_3 = s*(self.x - x_3) - self.y
            return Point(x_3, y_3, self.a, self.b)

    def __str__(self):
        return "Point ({}, {})".format(self.x, self.y)


p1 = Point(-1, 1, 5, 7)
p2 = Point(-1, 1, 5, 7)
inf = Point(float("inf"), float("inf"), 5, 7)

print(p1 + inf)
print(p1 + p2)
