import sys

N: int = int(sys.stdin.readline())

start: int = 666
count: int = 0
temp = start
flag: bool = True
result = 0
while flag:
    if "666" in str(temp):
        count += 1
    elif count == N:
        print( temp - 1)
        break
    temp += 1
