import sys

readline = sys.stdin.readline
N, T = map(int, readline().split())

X = [int(readline()) for i in range(N)]

start = min(X)
end = start + T

result = 0

while start <= end:
    mid = (start + end) // 2

    s = 0
    for level in X:
        if mid > level:
            s += (mid - level)

    if s <= T:
        start = mid + 1
        result = max(mid, result)
    else:
        end = mid - 1

print(result)
