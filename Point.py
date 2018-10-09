import math

class Point:
    def __init__(self, point):
        self.x = point[0]
        self.y = point[1]

    def check_on_curve(self, point, curve, p):
        a, b = curve
        y = point.y ** 2
        x = point.x ** 3 + a * point.x + b
        return x % p == y % p

    def inversion_mod_p(self, x, p):
        if x % p == 0:
           return None
        return pow(x, p - 2, p)

    def add(self, other, curve, p):
        if (self.x == math.inf or self.y == math.inf) and (other.x == math.inf or other.y == math.inf):
            return math.inf, math.inf
        elif self.x == math.inf or self.y == math.inf:
            return other
        elif other.x == math.inf or other.y == math.inf:
            return self
        elif not self.check_on_curve(self, curve, p) and not self.check_on_curve(other, curve, p):
            return "Points are not on the curve"
        elif (self.x == other.x) and (self.y == other.y):
            slope_up = 3 * self.x ** 2 + curve[0]
            slope_down = 2 * self.y
        elif self.x == other.x:
            return math.inf, math.inf
        else:
            slope_up = other.y - self.y
            slope_down = other.x - self.x
        slope_down_inv = self.inversion_mod_p(slope_down, p)

        if not slope_down_inv:
            return "Can't be inversed"

        slope = (slope_up * slope_down_inv) % p
        rx = (slope ** 2 - self.x - other.x) % p
        ry = (slope * (self.x - rx) - self.y) % p

        return rx, ry


point1 = Point((5, 10))
point2 = Point((0, 2))
print(point1.add(point2, (1, 4), 17))