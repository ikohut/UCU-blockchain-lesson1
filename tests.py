import copy

from elliptic_curve import EllipticCurve
from helpers import plot
from point import Point

C = EllipticCurve(a=-2, b=4)
print(C)

# case where P + Q + r = 0 ( tree points on curve)
P = Point(C, 3, 5)
P_copy = copy.copy(P)
Q = Point(C, -2, 0)
U = P+Q
print(U)
plot(C, P_copy, Q, U)

# case where P + P + 0 = 0 (only one point on curve)
P = Point(C, -2, 0)
P_copy = copy.copy(P)
Q = Point(C, -2, 0)
U = P+Q
print(U)
plot(C, P_copy, Q, U)

# case where P + Q + 0 = 0 (vertical line)
P = Point(C, 0, 2)
P_copy = copy.copy(P)
Q = Point(C, 0, -2)
U = P+Q
print(U)
plot(C, P_copy, Q, U)

# case where P + P + Q = 0 (two points on curve)
P = Point(C, 3, 5)
P_copy = copy.copy(P)
Q = Point(C, 3, 5)
U = P+Q
print(U)
plot(C, P_copy, Q, U)

