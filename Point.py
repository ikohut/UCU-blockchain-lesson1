# the class for addition operation on elliptic curve
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    # Equation: y^2 = x^3 + ax + b
    def add(self, other, a):
        if self.x == other.x and self.y == other.y:
            return self.double(a)
        if (other.x - self.x) == 0:
            return (float('inf'), float('inf'))
        # slope (gradient) = (y2 - y1)/{x2 - x1}
        slope = (other.y - self.y)/(other.x - self.x)

        answer_x = slope**2 - self.x - other.x
        answer_y = slope*(self.x - answer_x) - self.y
        return answer_x, answer_y

    def double(self, a):
        if self.y == 0:
            return (float('inf'), float('inf'))
        # slope (gradient) =(3x2 + a)/(2y)
        slope = 3 * (self.x**2 + a)/(2*self.y)
        answer_x = slope**2 - 2*self.x
        answer_y = slope*(self.x - answer_x)
        return answer_x, answer_y


a = Point(2, 2)
b = Point(1, 3)
print(a.add(b, 1))

