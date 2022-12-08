import sys

N: int = int(sys.stdin.readline())
base: int = 666
interval: int = 10
start: int = base
while True:
    end: int = start * interval
    for i in range(start, end):
        if str(i).find(str(base)) != -1:
            N -= 1
            if N == 0:
                print(i)
                exit()
    start = end
