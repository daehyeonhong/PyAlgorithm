import sys

length = int(sys.stdin.readline())
arr = []
for i in range(length):
    arr.append(sys.stdin.readline().rstrip())
l = list(set(arr))
l.sort()
l.sort(key=len)
for i in l:
    print(i)
