import math


class Point:
    def __init__(self, x, y, curve):
        self.x = x
        self.y = y
        self.p = curve.p
        self.curve = curve

    @staticmethod
    def __check_on_curve(point, curve):
        if math.inf in point.get_parameters():
            return True
        return (point.y ** 2) % curve.p == (point.x ** 3 + curve.a * point.x + curve.b) % curve.p

    def __eq__(self, other):
        return self.get_parameters() == other.get_parameters() and self.curve == other.curve

    def __str__(self):
        return "x: {}, y: {} p:{}".format(self.x, self.y, self.p)

    def get_parameters(self):
        return self.x, self.y

    @staticmethod
    def mod_inv(number, p):
        return pow(number, p - 2, p) if number % p != 0 else None

    def add(self, other):
        if not (self.__check_on_curve(self, self.curve) and self.__check_on_curve(other, other.curve)
                and self.curve == other.curve):
            print(self, other)
            print(self.__check_on_curve(self, self.curve), self.__check_on_curve(other, other.curve),
                  self.curve == other.curve)
            raise RuntimeError("Points are not on the same curve")

        if math.inf in self.get_parameters() and math.inf in other.get_parameters():
            return math.inf, math.inf

        elif math.inf in self.get_parameters():
            self.x = other.x
            self.y = other.y
            return other

        elif math.inf in other.get_parameters():
            return self

        elif self.get_parameters() == other.get_parameters():
            numerator = 3 * self.x ** 2 + self.curve.a
            denominator = 2 * self.x

        elif self.x == other.x:
            self.x = math.inf
            self.y = math.inf
            return self.x, self.y

        else:
            numerator = other.y - self.y
            denominator = other.x - self.x
        denominator_inverse = self.mod_inv(denominator, self.p)

        if not denominator_inverse:
            print("Can't inverse")
            return None

        a = (numerator * denominator_inverse) % self.p
        x3 = (a ** 2 - self.x - other.x) % self.p
        y3 = (a * (self.x - x3) - self.y) % self.p
        self.x = x3
        self.y = y3
        return self.x, self.y
