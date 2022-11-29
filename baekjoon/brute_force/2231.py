import sys

N: int = int(sys.stdin.readline())
result = 0
for n in range(N):
    if sum(map(int, str(n))) + n == N:
        result = n
        break
print(result)
