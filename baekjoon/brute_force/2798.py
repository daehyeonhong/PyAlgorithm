from itertools import permutations
import sys

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

max_v: int = 0
for items in permutations(cards, 3):
    sum_v = sum(items)
    if N == 3 or M == sum_v:
        max_v = sum_v
        break
    elif max_v < sum_v <= M:
        max_v = sum_v

print(max_v)
