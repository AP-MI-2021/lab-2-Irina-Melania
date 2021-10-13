# 12
import math


def get_perfect_squares(start: int, end: int):
    perfect_squares = []

    for i in range(start, end+1):
        r = math.sqrt(i)
        if i % r == 0:
            perfect_squares.append(i)

    return perfect_squares


def main():
    start = int(input("start = "))
    end = int(input("end = "))

    perfect_squares = get_perfect_squares(start, end)
    for ps in perfect_squares:
        print(ps)


main()