from itertools import permutations

import sys

# 주어진 값 입력
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

# permutation 저장(per: reference of permutation tuples)
per = permutations(a)
ans = 0

# 순열마다 차이를 더해(s), ans 보다 크면 ans를 update
for item in per:
    s = 0
    for job in range(len(item) - 1):
        s += abs(item[job] - item[job + 1])
    if s > ans:
        ans = s

print(ans)
