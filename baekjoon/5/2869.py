import math
import sys

A, B, V = map(int, sys.stdin.readline().split())
end = (V - B) / (A - B)
print(math.ceil(end))
