import math

class Point:
    """
    Class Point represents a point on crypto curve y^2 = x^3 + ax + b
    """

    ALLOWED_ERROR = 0.0001

    def __init__(self, x, y, a, b):
        if abs(y ** 2 - x ** 3 - a * x - b) > Point.ALLOWED_ERROR:
            raise ValueError('Incorrect values')

        self.x = x
        self.y = y
        self.a = a
        self.b = b

    def __add__(self, other):
        """
        A method should modify the self-instance.
        :param other:
        :return:
        """
        if self.x == other.x and self.y == other.y:
            return self.__prod2()
        try:
            slope = (other.y - self.y) / (other.x - self.x)
        except ZeroDivisionError:
            return 'points are not on the same line'

        x_res = slope ** 2 - self.x - other.x
        y_res = slope * (self.x - x_res) - self.y
        return Point(x_res, y_res, self.a, self.b)

    def __prod2(self):
        slope = (3 * (self.x ** 2) + self.a) / (2 * self.y)
        x_res = slope ** 2 - 2 * self.x
        y_res = slope * (self.x - x_res) - self.y

        return Point(x_res, y_res, self.a, self.b)

    def __str__(self):
        return "Point: {0},{1}".format(self.x, self.y)


p = Point(1, math.sqrt(3), 1, 1)
q = Point(2, math.sqrt(11), 1, 1)
print(p+q)
