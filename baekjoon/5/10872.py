import sys


def factorial(arg):
    if arg > 1:
        return arg * factorial(arg - 1)
    else:
        return 1


print(factorial(int(sys.stdin.readline())))
