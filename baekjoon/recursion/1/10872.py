import sys

N = int(sys.stdin.readline())


def factorial(arg):
    if arg > 0:
        return arg * factorial(arg - 1)
    else:
        return 1


print(factorial(N))
