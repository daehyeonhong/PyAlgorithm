import sys


def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)


cnt: int = 0


def is_palindrome(s):
    global cnt
    cnt = 0
    return recursion(s, 0, len(s) - 1)


readline = sys.stdin.readline
T: int = int(readline())

S = [readline().rstrip() for i in range(T)]
for s in S:
    print(is_palindrome(s), cnt)
