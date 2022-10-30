import math
import sys

A, B, V = map(int, sys.stdin.readline().split())

if A == V:
    print(1)
else:
    C = A - B
    D = math.ceil((V - A) / C)
    print(D + 1 if D * C + A >= V else D)
