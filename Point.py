import gmpy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    # Equation: y^2 = x^3 + ax + b
    def add(self, other, curve, mod):


        if self.x == float("inf") and self.y == float("inf") and other.x == float("inf") and other.y == float("inf"):
            return (float("inf"), float("inf"))

        elif self.x == float("inf") and self.y == float("inf"):
            return other

        elif other.x == float("inf") and other.y == float("inf"):
            return self

        point1_on_curve = (self.y ** 2) % mod == (self.x ** 3 + curve[0] * self.x + curve[1]) % mod
        point2_on_curve = (other.y ** 2) % mod == (other.x ** 3 + curve[0] * other.x + curve[1]) % mod

        if not point1_on_curve or not point2_on_curve:
            return "One of the points is not on the curve"

        elif self.x == other.x and self.y == other.y:
            delta_upper = 3 * self.x**2 + curve[0]
            delta_lower = 2*self.y
        elif other.x == self.x:
            return (float('inf'), float('inf'))
        else:
            # slope (gradient) = (y2 - y1)/(x2 - x1)
            delta_upper = (other.y - self.y)
            delta_lower = (other.x - self.x)

        delta_lower_MI = gmpy.invert(delta_lower, mod)

        slope = (delta_upper*delta_lower_MI) % mod
        answer_x = (slope**2 - self.x - other.x) % mod
        answer_y = (slope*(self.x - answer_x) - self.y) % mod
        return Point(float(answer_x), float(answer_y))


point1 = Point(float("inf"), float("inf"))
point2 = Point(6, 0)

point = point1.add(point2, (3, 4), 17)

print(point.x, point.y)

