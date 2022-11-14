import sys

readline = sys.stdin.readline
N: int = int(readline())
stars = [['*' for j in range(N)] for i in range(N)]

mid = 1 * 3 // 2
rows = mid
columns = mid
for row in range(rows, N, 3):
    for column in range(columns, N, 3):
        stars[row][column] = ' '

for star in stars:
    print(star)
