import sys

x, y = map(int, sys.stdin.readline().split())
print(' '.join(list(filter(lambda l: int(l) < y, list(sys.stdin.readline().split())))))
