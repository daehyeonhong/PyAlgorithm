import sys

T = int(sys.stdin.readline())
for idx in range(T):
    A_SIZE, B_SIZE = map(int, sys.stdin.readline().split())
    A =sorted( list(map(int, sys.stdin.readline().split())))
    B =sorted( list(map(int, sys.stdin.readline().split())))
    res = 0
    for a in range(A_SIZE):
        for b in range(B_SIZE):
            if A[a] > B[b]:
                res += 1
    print(res)
