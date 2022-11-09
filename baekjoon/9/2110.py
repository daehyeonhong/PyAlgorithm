import sys

readline = sys.stdin.readline
N, C = map(int, readline().split())
homes = list((int(readline()) for i in range(N)))

homes.sort()

start = 1
end = homes[-1] - homes[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    current = homes[0]
    count = 1
    for i in range(1, len(homes)):
        if homes[i] >= current + mid:
            count += 1
            current = homes[i]
    if count >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)
