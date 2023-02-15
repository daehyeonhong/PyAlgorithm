import sys

A, B = map(int, sys.stdin.readline().split())

SET_A = set(map(int, sys.stdin.readline().rstrip().split()))
SET_B = set(map(int, sys.stdin.readline().rstrip().split()))
RESULT_B=list()
for B in SET_B:
    if SET_A.__contains__(B):
        SET_A.remove(B)
    else:
        RESULT_B.append(B)

print(len(SET_A)+len(RESULT_B))