import sys
from collections import Counter


def 평균(arg, leng):
    return round(sum(arg) / leng)


def 중앙값(arg, leng):
    return arg[leng // 2]


def 최빈값(arg):
    args = Counter(arg).most_common()
    print(args)
    print(Counter(arg))
    if len(args) > 1:
        return args[1][0] if args[0][1] == args[1][1] else args[0][0]
    else:
        return args[0][0]


def 범위(arg):
    return arg[-1] - arg[0]


length = int(sys.stdin.readline())
array = []
for i in range(length):
    array.append(int(sys.stdin.readline()))
array.sort()
print(f'평균{평균(array, length)}')
print(f'중앙값{중앙값(array, length)}')
print(f'최빈값{최빈값(array)}')
print(f'범위{범위(array)}')
