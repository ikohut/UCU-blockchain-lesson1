class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.a = 1

    def add(self,other):
        #if point 1 equal to point 2
        if self.x == other.x and self.y == other.y:
            lamda = (3 * self.x ** 2 + self.a) / (2 * other.y)
        else:
            lamda = (other.y - self.y) / (other.x - self.x)
        nu = self.y - lamda * self.x
        x3 = lamda ** 2 - self.x - other.x
        y3 = -(lamda * x3 + nu)
        return (x3, y3)


# a = Point(3, 2)
# b = Point(4, 1)
# print(a.add(b))
