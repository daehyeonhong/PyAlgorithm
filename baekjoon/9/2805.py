import sys

readline = sys.stdin.readline
N, R = map(int, readline().split())
trees = sorted([int(i) for i in readline().split()])

start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    log = 0
    for tree in trees:
        if tree >= mid:
            log += tree - mid
    if log >= R:
        start = mid + 1
    else:
        end = mid - 1

print(end)
