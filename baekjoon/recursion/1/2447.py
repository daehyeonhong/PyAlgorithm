import sys

readline = sys.stdin.readline
N: int = int(readline())
stars = [['*' for j in range(N)] for i in range(N)]

mid = 1 * 3 // 2
stars[1][1] = ' '

for star in stars:
    print(star)
