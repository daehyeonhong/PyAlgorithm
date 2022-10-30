import math
import sys


def prime_number(arg):
    if arg < 2:
        return False
    for i in range(2, int(math.sqrt(arg) + 1)):
        if arg % i == 0:
            return False
    return True


N = int(sys.stdin.readline())
arr = list(sys.stdin.readline().split())
result = 0
for item in arr:
    result += 1 if prime_number(int(item)) else 0
print(result)
