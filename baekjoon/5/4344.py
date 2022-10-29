import sys

readline = sys.stdin.readline
N = int(readline())
arr1 = []
for i in range(N):
    inp = list(map(int, readline().split()))
    arr1.append(inp)
for inp in arr1:
    cnt = inp.pop(0)
    avg = sum(inp) // cnt
    over_cnt = 0
    for item in inp:
        if item > avg:
            over_cnt += 1
    print("{:.3f}%".format(round(over_cnt / cnt * 100, 3)))

# 5
# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91
