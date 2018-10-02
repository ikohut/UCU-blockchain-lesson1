class Point:
    def __init__(self, x=float('inf'), y=float('inf')):
        self.x = x
        self.y = y

    def add(self, to_add_point):
        """
        This function add to different point on the elliptic curve
        :param to_add_point: coordinates of point to add
        :return: coordinates of the resulted point
        """
        if (to_add_point.x == self.x) and (to_add_point.y == self.y):
            return self.add_point_to_itself()
        try:
            s = (to_add_point.y - self.y) / (to_add_point.x - self.x)
        except ZeroDivisionError:
            return "X coordinate of the newly created point: inf" + '\n' \
                "Y coordinate of the newly created point: inf"
        else:
            created_point_x = s ** 2 - self.x - to_add_point.x
            created_point_y = self.y + s * (created_point_x - self.x)
            return Point(created_point_x, -created_point_y)

    def add_point_to_itself(self):
        """
        This function add point to itself
        :return: coordinates of the resulted point
        """
        try:
            s = (3*self.x**2) / (2*self.y)
        except ZeroDivisionError:
            return "X coordinate of the newly created point: inf" + '\n' \
                "Y coordinate of the newly created point: inf"
        else:
            created_point_x = s**2 - 2 * self.x
            created_point_y = self.y + s * (created_point_x - self.x)
            return Point(created_point_x, -created_point_y)

    def __str__(self):
        return "X coordinate of the newly created point: " + str(round(self.x, 3)) + '\n' \
               "Y coordinate of the newly created point: " + str(round(self.y, 3))


if __name__ == "__main__":

    A = Point(4, 7.912)
    B = Point(0.72, 1.501)
    print(A.add(B))
    print()
    C = Point(4, 5)
    D = Point(4, 5)
    print(D.add(C))
    print()
    E = Point(4, 8)
    F = Point(4, 5)
    print(E.add(F))