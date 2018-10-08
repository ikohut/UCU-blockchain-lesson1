from point_on_crypto_curve import PointOnCryptoCurve

def addition(a, b):
    print("Adding 2 points on crypto curve")
    print(a, b)
    a.add(b)
    print("Result: %s" % a)
    print("It is on crypto curve as well: %s\n" % PointOnCryptoCurve.point_is_on_curve(*a.get_cords()))


def main():
    a = PointOnCryptoCurve(5, 1.0)
    b = PointOnCryptoCurve(9, 9.0)

    c = PointOnCryptoCurve(20, 4)
    d = PointOnCryptoCurve(38, 11)

    addition(a, b)
    addition(a, c)
    addition(b, b)
    addition(c, d)


if __name__ == "__main__":
    main()