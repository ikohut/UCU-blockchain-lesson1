class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, other):
        assert type(other) == type(self)
        self.x += other.x
        self.y += other.y
        return self  # for chaining

    def __repr__(self):
        return "Point at (%d, %d)" % (self.x, self.y)


if __name__ == "__main__":
    a = Point(2, 3)
    b = 5
    b = Point(3, 5)
    print(a.add(b))
