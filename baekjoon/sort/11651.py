import sys

length = int(sys.stdin.readline())
funcSet = []
for i in range(length):
    x, y = map(int, sys.stdin.readline().split())
    funcSet.append([y, x])

funcSet.sort()
for i in range(length):
    print(f'{funcSet[i][1]} {funcSet[i][0]}')
