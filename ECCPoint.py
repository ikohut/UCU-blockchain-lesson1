import numpy as np


def equation(x, a=3, b=7):
    return x ** 3 + a * x + b


class Point:
    def __init__(self, x):
        self.x = x
        self.y = np.sqrt(equation(x))

    def add(self, other):
        second_point = Point(other)

        k = (second_point.y - self.y) / (second_point.x - self.x)   # Slope

        third_point_x = k**2 - second_point.x - self.x
        third_point_y = second_point.y + k + (third_point_x - second_point.x)

        self.x = third_point_x
        self.y = third_point_y
