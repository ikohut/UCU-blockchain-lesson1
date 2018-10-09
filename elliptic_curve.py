class Point():
    """
    Class Point implements the point on
    elliptic curve: mod p(y^2) = (x^3 + ax + b)mod p
    """

    def __init__(self, x, y, a, b, mod):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.mod = mod

        if self.x == float("inf") or self.y == float("inf"):
            pass
        elif self.y**2 % self.mod != (self.x**3 + self.a*self.x + self.b) % self.mod:
            print('Point ({},{}) does not belong to the curve'.format(self.x, self.y))

        if not self.is_prime(self.mod):
            print("P number must be prime!")

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            print('Points {}, {} does not belong to the same curve'.format(self, other))

        # The points at infinity
        if self.x == float("inf"): return other
        elif other.x == float("inf"): return self

        # The points are in a vertical line
        elif self.x == other.x and self.y == -other.y: return float('inf')

        # The points where x_1 != x_2
        elif self.x != other.x:
            alpha_num = other.y - self.y
            alpha_den = other.x - self.x

        # The two points are the same
        else:
            if self.y == 0:
                return float("inf")
            else:
                alpha_num = 3*self.x**2 + self.a
                alpha_den = 2*self.y

        alpha_den_mi = self.multiplicative_inverse(alpha_den, self.mod)
        alpha = (alpha_num * alpha_den_mi) % self.mod
        x_3 = (alpha**2 - self.x - other.x)
        y_3 = (alpha * (self.x - x_3) - self.y ) % self.mod

        return Point(x_3, y_3, self.a, self.b, self.mod)

    def __str__(self):
        return "Point ({}, {})".format(self.x, self.y)

    @staticmethod
    def is_prime(p):
        return all(p % i for i in range(2, p))

    @staticmethod
    def multiplicative_inverse(num, mod):
        NUM, MOD = num, mod
        x, x_old = 0, 1
        y, y_old = 1, 0

        while mod:
            q = num // mod
            num, mod = mod, num % mod
            x, x_old = x_old - q * x, x
            y, y_old = y_old - q * y, y

        if num != 1:
            return "NO MI. However, the GCD of %d and %d is %u" % (NUM, MOD, num)
        else:
            MI = (x_old + MOD) % MOD
        return MI


if __name__ == '__main__':

    p1 = Point(-1, 1, 5, 7, 3)
    p2 = Point(-1, 1, 5, 7, 3)
    inf = Point(float("inf"), float("inf"), 5, 7, 3)

    print(p1 + inf)
    print(p1 + p2)
    print(p2 + inf)
