import random


def get_point_on_curve(curve):
    a = curve["a"]
    b = curve["b"]
    p = curve["p"]

    trial = 0

    while trial < 2 * p:
        x = random.randint(1, p - 1)
        trial += 1
        if trial >= (2 * p): break
        righths = (x ** 3 + x * a + b) % p

        sq_y = righths ** 0.5
        if int(sq_y) == sq_y:
            y = sq_y
            return (x, y)

    print("no points found")


def multiplicative_inverse(num, mod):
    n = num
    m = mod
    x, x_old = 0, 1
    y, y_old = 1, 0
    while mod:
        q = num // mod
        num, mod = mod, num % mod
        x, x_old = x_old - q * x, x
        y, y_old = y_old - q * y, y

    if num != 1:
        return "NO MI. However, the GCD of %d and %d is %u" % (n, m, num)
    else:
        return (x_old + m) % m


def is_prime(n):
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    # curve = {"a": 0, "b": 7, "p": 100000000003}
    curve = {"a": 0, "b": 7, "p": 131}

    res = get_point_on_curve(curve)


    print(res)
