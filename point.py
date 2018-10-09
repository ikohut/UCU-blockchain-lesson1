import gmpy

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other, curve, mod):
        if self.x == float("inf") and self.y == float("inf") and other.x == float("inf") and other.y == float("inf"):
            return (float("inf"), float("inf"))

        elif self.x == float("inf") and self.y == float("inf"):
            return other

        elif other.x == float("inf") and other.y == float("inf"):
            return self

        point1_curve = self.check_curve(self.x, self.y, curve[0], curve[1], mod)
        point2_curve = self.check_curve(other.x, other.y, curve[0], curve[1], mod)

        if not point1_curve or not point2_curve:
            return "One point is not on the curve"
	
        elif (self.x == other.x) and (self.y == other.y):
            d_up = 3 * self.x ** 2 + curve[0]
            d_low = 2 * self.y

        elif self.x == other.x:
            return (float('inf'), float('inf'))
        else:
            #(y2 - y1),(x2 - x1)
            d_up = other.y - self.y 
            d_low = other.x - self.x

        d_low_mi = gmpy.invert(d_low, mod)
        lmb = (d_up * d_low_mi) % mod

        fin_x = (lmb ** 2 - other.x - self.x) % mod
        fin_y = (lmb * (self.x - fin_x) - self.y) % mod

        return Point(fin_x, fin_y)

    def check_curve(self, x, y, a, b, mod):
        # Equation: y^2 = x^3 + ax + b

        first_side = y ** 2
        second_side = x ** 3 + a * x + b

        return first_side % mod == second_side % mod

#Test
point1 = Point(5, 5)
point2 = Point(6, 0)
point = point1.add(point2,(3,4),17)

print(point.x, point.y)