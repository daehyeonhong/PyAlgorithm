import sys

N: int = int(sys.stdin.readline())
if N % 3 != 0:
    exit()


def recursion(n):
    if n == 1:
        return ['*']
    interval: int = n // 3
    stars: list[str] = recursion(interval)
    result = []

    for star in stars:
        result.append(star * 3)
    for star in stars:
        result.append(star + ' ' * interval + star)
    for star in stars:
        result.append(star * 3)
    return result


print('\n'.join(recursion(N)))
