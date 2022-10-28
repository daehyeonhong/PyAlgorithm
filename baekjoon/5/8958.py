import sys

N = int(sys.stdin.readline())

arr = []
for i in range(N):
    arr.append(sys.stdin.readline().rstrip())

for idx in range(N):
    sum_ = 0
    result = 0
    for item in arr[idx]:
        if item == 'X':
            result + sum_
            sum_ = 0
        else:
            sum_ = sum_ + 1
        result = result + sum_
    print(result)
# 5
# OOXXOXXOOO
# OOXXOOXXOO
# OXOXOXOXOXOXOX
# OOOOOOOOOO
# OOOOXOOOOXOOOOX
