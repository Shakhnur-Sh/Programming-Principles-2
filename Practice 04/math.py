# math.py
# Python Math library tasks

import math as m

def degree_to_radian(deg: float) -> float:
    return deg * m.pi / 180.0


def trapezoid_area(height: float, base1: float, base2: float) -> float:
    return (base1 + base2) * height / 2.0


def regular_polygon_area(n_sides: int, side_length: float) -> float:
    # Area = (n * s^2) / (4 * tan(pi/n))
    return (n_sides * (side_length ** 2)) / (4.0 * m.tan(m.pi / n_sides))


def parallelogram_area(base: float, height: float) -> float:
    return base * height


def main():
    # 1) degree to radian
    deg = float(input("Input degree: "))
    print("Output radian:", round(degree_to_radian(deg), 6))

    # 2) area of trapezoid
    h = float(input("\nHeight: "))
    b1 = float(input("Base, first value: "))
    b2 = float(input("Base, second value: "))
    print("Expected Output:", trapezoid_area(h, b1, b2))

    # 3) area of regular polygon
    n = int(input("\nInput number of sides: "))
    s = float(input("Input the length of a side: "))
    print("The area of the polygon is:", regular_polygon_area(n, s))

    # 4) area of parallelogram
    base = float(input("\nLength of base: "))
    ph = float(input("Height of parallelogram: "))
    print("Expected Output:", parallelogram_area(base, ph))


if __name__ == "__main__":
    main()