import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))

for i in arr:
    print(arr2.index(i), end = ' ')