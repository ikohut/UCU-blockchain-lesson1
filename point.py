from curve import EllipticCurve
# from zero import Zero

class Point(object):
  """
  This class represents a point on the given Elliptic Curve

  >>> print(Point(EllipticCurve(0, 3), 1, 2))
  (1, 2)

  >>> Point(EllipticCurve(0, 3), 2, 2)
  Traceback (most recent call last):
      ...
  Exception: The point (2, 2) doesn't belong to the given curve y^2 = x^3 + 0x + 3

  >>> print(Point(EllipticCurve(0, 3), 1, 2) + Zero(EllipticCurve(0, 3)))
  (1, 2)
  """
  def __init__(self, curve, x, y):
    self.curve = curve
    self.x = x
    self.y = y

    if not curve.testPoint(x, y):
          raise Exception("The point %s doesn't belong to the given curve %s" % (self, curve))

  def __str__(self):
      return "({}, {})".format(self.x, self.y)
        
  def __add__(self, other):
      if isinstance(other, Zero):
          return self

      x_1, y_1, x_2, y_2 = self.x, self.y, other.x, other.y

      if (x_1, y_1) == (x_2, y_2):
          if y_1 == 0:
            return Zero(self.curve)

          # slope of the tangent line 
          m = (3 * x_1 * x_1 + self.curve.a) / (2 * y_1)
      else:
          if x_1 == x_2:
            return Zero(self.curve)

          # slope of the secant line
          m = (y_2 - y_1) / (x_2 - x_1)

      x_3 = m*m - x_2 - x_1
      y_3 = m*(x_3 - x_1) + y_1

      return Point(self.curve, x_3, -y_3)


class Zero(Point):
    """
    This class represents a zero == (0, 0) point
   
    >>> print(Zero(EllipticCurve(a=1, b=1)))
    Zero

    >>> print(Zero(EllipticCurve(a=1, b=1)) + Point(EllipticCurve(0, 3), 1, 2))
    (1, 2)
    """
    def __init__(self, curve):
        self.curve = curve

    def __str__(self):
        return "Zero"

    def __add__(self, other_point):
        return other_point

    def __neg__(self):
      return self

if __name__ == "__main__":
    import doctest
    doctest.testmod()


