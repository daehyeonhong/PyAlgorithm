import sys

N: int = int(sys.stdin.readline())
base: int = 666
key: int = base
while True:
    if str(key).find(str(base)) != -1:
        N -= 1
        if N == 0:
            print(key)
            exit()
    key += 1
