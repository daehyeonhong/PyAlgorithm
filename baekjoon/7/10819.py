from itertools import permutations

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

ans = 0
result_item = []
for item in permutations(a):
    s = 0
    for job in range(len(item) - 1):
        s += abs(item[job] - item[job + 1])
    if s > ans:
        result_item = item
        ans = s

print(result_item)
print(ans)
