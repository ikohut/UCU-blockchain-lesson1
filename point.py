

# x1 != x2
# x1 == x2
# x1 == -x2


class Point():
    def __init__(self, a, b, x, y):
        if all([x, y]): # check if it is not an infinity point
            if y ** 2 != x ** 3 + a * x + b:
                raise ValueError('Point ({},{}) is not on the curve'.format(x, y))
        self.a = a
        self.b = b
        self.x = x
        self.y = y

    def __str__(self):
        return 'a:{} b:{} x:{} y:{}'.format(self.a, self.b, self.x, self.y)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.x == other.x and self.y == other.y

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise RuntimeError('Points {}, {} are not on the same curve'.format(self, other))
        elif self == other:
            if self.y == 0:
                self.x = None
                self.y = None
            else:
                k = (3 * (self.x ** 2) + self.a) / (2 * self.y)
                s_x = k ** 2 - 2 * self.x
                s_y = k * (self.x - s_x) - self.y
                self.x = s_x
                self.y = s_y
        elif self.x is None:
            self.x = other.x
            self.y = other.y
        elif other.x is None:
            pass
        elif self.x == other.x:   # p1 == -p2
            self.x = None
            self.y = None
        else:  # p1 != p2
            k = (other.y - self.y) / (other.x - self.x)
            s_x = k ** 2 - self.x - other.x
            s_y = k * (self.x - s_x) - self.y
            self.x = s_x
            self.y = s_y





