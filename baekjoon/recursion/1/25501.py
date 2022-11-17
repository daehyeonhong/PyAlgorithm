import sys


def recursion(s, l, r, cnt):
    if l >= r:
        return {1, cnt}
    elif s[l] != s[r]:
        return {0, cnt}
    else:
        return recursion(s, l + 1, r - 1, cnt + 1)


def is_palindrome(s):
    return recursion(s, 0, len(s) - 1, 1)


readline = sys.stdin.readline
T: int = int(readline())

S = [readline().rstrip() for i in range(T)]
for s in S:
    print(*is_palindrome(s))
