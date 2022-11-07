import sys

stdin_readline = sys.stdin.readline
N = int(stdin_readline())
arr = list(map(int, stdin_readline().split()))

arr.sort(reverse=True)
mid = len(arr) // 2
left = arr[:mid]
right = arr[mid:]
left.sort()
right.sort(reverse=True)
result = []
aa = []
print(right)
print(left)
while right or left:
    if left:
        result.append(left.pop())
    if right:
        result.append(right.pop())
print(result)
for i in range(len(result) - 1):
    res = abs(result[i] - result[i + 1])
    print(f'{result[i]} - {result[i + 1]} = {res}')
    aa.append(res)

print(aa)
print(sum(aa))
