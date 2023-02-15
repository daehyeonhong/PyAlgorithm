import sys

T = int(sys.stdin.readline().rstrip())
for idx in range(T):
    A_SIZE, B_SIZE = map(int, sys.stdin.readline().rstrip().split())
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    B = list(map(int, sys.stdin.readline().rstrip().split()))
    res = 0
    for a in A:
        for b in B:
            if a > b:
                res += 1
    print(res)
