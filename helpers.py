import matplotlib.pyplot as plt
import numpy as np



def plot(curve, P, Q, U):
    a = curve.a
    b = curve.b
    y, x = np.ogrid[-10:10:100j, -10:10:100j]
    x_1, y_1, x_2, y_2, x_3, y_3 = P.x, P.y, Q.x, Q.y, U.x, U.y
    plt.scatter([x_1, x_2, x_3], [y_1, y_2, y_3])
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0])
    plt.grid()
    plt.show()