import sys


def hanoi(val, fst, mid, lst):
    if val == 1:
        print(fst, lst, sep=" ")
    else:
        hanoi(val - 1, fst, lst, mid)
        hanoi(1, fst, mid, lst)
        hanoi(val - 1, mid, fst, lst)


N = int(sys.stdin.readline())
print(2 ** N - 1)
if N <= 20:
    hanoi(N, 1, 2, 3)
