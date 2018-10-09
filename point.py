class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def m_inverse(self, number, mod):
        for i in range(1, mod):
            if (mod * i + 1) % number == 0:
                return (mod * i + 1) // number
        return 1

    def check_on_curve(self, curve, mod):
        return (self.y ** 2) % mod == (self.x ** 3 + curve[0] * self.x + curve[1]) % mod

    def add(self, other, curve, mod):
        if self.check_on_curve(curve, mod) and other.check_on_curve(curve, mod):
            if isinstance(self, str) and isinstance(other, str):
                return "Point's at infinity"
            elif isinstance(self, str):
                return other
            elif isinstance(other, str):
                return self
            elif self.x == other.x and self.y == other.y:
                alpha_numerator = 3 * self.x ** 2 + curve[0]
                alpha_denominator = 2 * self.y
            elif self.x == other.x:
                return "Point's at infinity"
            else:
                alpha_numerator = other.y - self.y
                alpha_denominator = other.x - self.x
            alpha_denominator_m_i = self.m_inverse(alpha_denominator, mod)
            alpha = (alpha_numerator * alpha_denominator_m_i) % mod

            result_x = (alpha ** 2 - self.x - other.x) % mod
            result_y = (alpha * (self.x - result_x) - self.y) % mod
            return result_x, result_y
        else:
            return "Point isn't on curve"


point1 = Point(0, 2)
point2 = Point(3, 0)
point3 = point1.add(point2, (1, 4), 17)
print(point3)