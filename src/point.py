class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def _check_type(self, other):
        assert type(other) == type(self)

    def add(self, other):
        self._check_type(other)
        self.x = self.x + other.x
        self.y = self.y + other.y
        return self  # for chaining

    def get_cords(self):
        return (self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Point at (%f, %f)" % (self.x, self.y)



if __name__ == "__main__":
    a = Point(2, 3)
    b = 5
    b = Point(3, 5)
    print(a.add(b))
