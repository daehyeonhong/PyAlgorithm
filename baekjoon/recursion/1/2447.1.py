import sys

N: int = int(sys.stdin.readline())

stars = []


def recursion(n, interval):
    row = n % N
    column = n % N
    print(column, row)
    global stars
    mid = interval // 2
    if mid == N:
        return
    if (row - mid) % 3 == 0:
        stars.append(' ')
    elif (column - mid) % 3 == 0:
        stars.append(' ')
    else:
        stars.append('*')


recursion(1, 3)
print(stars)
