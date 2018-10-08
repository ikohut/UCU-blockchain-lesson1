class Point:
    """
    Class Point represents a point on crypto curve y^2 = x^3 + ax + b
    """

    def __init__(self, x, y, a, b, mod):
        if (y ** 2 - x ** 3 - a * x - b) % mod != 0:
            raise ValueError('Incorrect values')

        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.mod = mod

    def __add__(self, other):
        """
        A method should modify the self-instance.
        :param other:
        :return:
        """

        if self.x == other.x and self.y == other.y:
            return self.__prod2()

        elif self.x == other.x:
            return "Point is at infinity"

        # slope = (other.y - self.y) * self.__inv(other.x - self.x)
        slope = (other.y - self.y) * self.__inv2(other.x - self.x)

        x_res = (slope ** 2 - self.x - other.x) % self.mod
        y_res = (slope * (self.x - x_res) - self.y) % self.mod
        return Point(x_res, y_res, self.a, self.b, self.mod)

    def __inv(self, num):
        for i in range(self.mod):
            if num * i % self.mod == 1:
                return i

    def __inv2(self, num):
        return pow(num, self.mod - 2, self.mod)

    def __prod2(self):
        slope = (3 * (self.x ** 2) + self.a) / (2 * self.y)
        x_res = (slope ** 2 - 2 * self.x) % self.mod
        y_res = (slope * (self.x - x_res) - self.y) % self.mod

        return Point(x_res, y_res, self.a, self.b, self.mod)

    def __str__(self):
        return "Point: x: {0}, y: {1}".format(self.x, self.y)


if __name__ == "__main__":
    q = Point(0, 1, 1, 1, 7)
    p = Point(2, 2, 1, 1, 7)
    print(p + q)
    print("Hooray. Test 1 passed")

    q = Point(195, 652, 1, 1, 997)
    p = Point(995, 514, 1, 1, 997)
    print(p + q)
    print("Hooray. Test 2 passed")
