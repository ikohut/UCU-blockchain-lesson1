from ECCPoint import Point

if __name__ == "__main__":
    point = Point(2)

    for i in range(10):
        print("x:", point.x, "y:", point.y)
        point.add(i)
