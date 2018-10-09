from sympy import mod_inverse


class Point(object):
    def __init__(self, curve, x, y):
        self.curve = curve
        self.x = x
        self.y = y
        self.mod = 6
        if not self.on_curve(curve):
            raise Exception("The point is not on curve")

    def on_curve(self, curve):
        return pow(self.y, 2) % self.mod == (pow(self.x, 3) + curve.a * self.x + curve.b) % self.mod

    def __str__(self):
        return "Resulting point: (%d, %d)" % (self.x, self.y)

    def __add__(self, Q):
        x_1, y_1, x_2, y_2 = self.x, self.y, Q.x, Q.y
        if (x_1, y_1) == (x_2, y_2):

            # case where P + P + 0 = 0 (only one point on curve)
            if y_1 == 0:
                return Point(self.curve, x_1, y_1)

            # case where P + P + Q = 0 (two points on curve)
            s = ((3 * pow(x_1, 2) + self.curve.a) / (mod_inverse(2 * y_1, self.mod))) % self.mod
        else:

            # case where P + Q + 0 = 0 (vertical line)
            if x_1 == x_2:
                return Point(self.curve, self.x, self.y)
            # case where P + Q + r = 0 (tree points on curve)

            s = ((y_2 - y_1) / (mod_inverse(x_2 - x_1, self.mod))) % self.mod
        self.x = (pow(s, 2) - x_2 - x_1) % self.mod
        self.y = ((s * (self.x - x_1)) + y_1) % self.mod

        print(self.x, self.y)
        # return for drawing the resulting point
        return Point(self.curve, self.x, -self.y)













