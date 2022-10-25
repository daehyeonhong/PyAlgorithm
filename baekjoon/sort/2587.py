import sys

input_ = sys.stdin.readline

n = 5
arr = []
for item in range(n):
    arr.append(int(input_()))

arr.sort()
avg = sum(arr) // n
mid = arr[n // 2]

print(avg)
print(mid)
