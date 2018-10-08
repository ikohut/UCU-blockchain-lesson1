import gmpy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    # Equation: y^2 = x^3 + ax + b
    def add(self, other, curve, mod):
        point1_on_curve = (self.y**2) % mod == (self.x**3 + curve[0]*self.x + curve[1]) % mod
        point2_on_curve = (other.y**2) % mod == (other.x**3 + curve[0]*other.x + curve[1]) % mod

        if not point1_on_curve and not point2_on_curve:
            return "One of the points is not on the curve"

        if isinstance(self, str) and isinstance(other, str):
            return (float("inf"), float("inf"))
        elif isinstance(self, str):
            return other
        elif isinstance(other, str):
            return self
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
        return float(answer_x), float(answer_y)


a = Point(0, 3)
b = Point(0, 2)
result = a.add(b, (1, 4), 17)
print(result)


