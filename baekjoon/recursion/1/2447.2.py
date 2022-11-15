import math
import sys

N: int = int(sys.stdin.readline())


def print_star(row, column, interval):
    print(row,math.sqrt(row), float(math.sqrt(row)).is_integer())
    if row == 1 or row == N or column == 1 or column == N or interval == N or float(
            math.sqrt(row)).is_integer() or float(math.sqrt(column)).is_integer():
        return '*'
    if (row == interval or row % 3 == interval) and (column == interval or column % 3 == interval):
        return ' '
    else:
        return print_star(row, column, interval + 1)


for starRow in range(1, N + 1):
    for starColumn in range(1, N + 1):
        print(print_star(starRow, starColumn, 1), end=('\n' if starColumn == N else ''))

#                *********
#                * ** ** *
#                *********
#                ***   ***
#                * *   * *
#                ***   ***
#                *********
#                * ** ** *
#                *********
