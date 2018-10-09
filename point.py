from crypto import CryptoCurve


class Point:

    def __init__(self, crypto_curve, x=-1, y=-1):
        self.x = x
        self.y = y
        self.a = crypto_curve.a
        self.b = crypto_curve.b
        self.p = crypto_curve.p
        self.coordinates_list = []

    def generate_points(self):
        for i in range(1, self.p):
            right_side = (i ** 3 + i * self.a + self.b) % self.p
            y = right_side ** 0.5
            if int(y) == y:
                self.coordinates_list.append([i, int(y)])
        print(self.coordinates_list)
        if self.coordinates_list:
            self.x = self.coordinates_list[0][0]
            self.y = self.coordinates_list[0][1]
        return self.coordinates_list

    def is_on_curve(self):
        print(self.x, self.y)
        return (self.x**3 + self.x * self.a + self.b) % self.p == self.y ** 2 % self.p

    def multiplicative_inverse(self, num, mod):
        n = num
        m = mod
        x, x_old = 0, 1
        y, y_old = 1, 0
        while mod:
            q = num // mod
            num, mod = mod, num % mod
            x, x_old = x_old - q * x, x
            y, y_old = y_old - q * y, y

        if num != 1:
            return "NO MI. However, the GCD of %d and %d is %u" % (n, m, num)
        else:
            return (x_old + m) % m

    def add(self, other):
        numerator = (other.y - self.y)
        denominator = (other.x - self.x)

        if self.x == other.x and self.y == other.y:
            denominator = (2 * self.y)
            numerator = 3 * (self.x ** 2)
        elif self.x == other.x:
            return "point at infinity"

        mod = self.p
        denominator_inverse = self.multiplicative_inverse(denominator, mod)
        l = (numerator * denominator_inverse) % mod
        x_new = (l ** 2 - self.x - other.x) % mod
        y_new = (l * (self.x - x_new) - self.y) % mod
        self.x = x_new
        self.y = y_new
        print(x_new, y_new)
        return self


c = CryptoCurve(0, 7, 101)
p1 = Point(c)
p1.generate_points()
p2 = Point(c, 15, 7)
p1.add(p2)
print(p1.is_on_curve())

