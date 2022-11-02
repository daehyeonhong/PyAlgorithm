import sys


def det(num):
    for v in range(num):
        if arr[num] == arr[v] or abs(arr[num] - arr[v]) == num - v:
            return False
    return True


def func(num):
    global cnt

    if num == N:
        cnt += 1
        return

    for i in range(N):
        arr[num] = i
        if det(num):
            func(num + 1)


N = int(sys.stdin.readline())
arr = [0] * N
cnt = 0

func(0)
print(cnt)
