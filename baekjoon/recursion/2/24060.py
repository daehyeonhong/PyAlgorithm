import sys

K, N = map(int, sys.stdin.readline().split())
result_array = []


def merge_sort(arg, num):
    num += 1
    length = len(arg)
    if length <= 1:
        return arg
    center = length // 2
    group1 = merge_sort(arg[:center], num)
    group2 = merge_sort(arg[center:], num)

    result = []
    while group1 and group2:
        pop_ = group1.pop(0) if group1[0] < group2[0] else group2.pop(0)
        result_array.append(pop_)
        result.append(pop_)
    while group1:
        pop = group1.pop(0)
        result_array.append(pop)
        result.append(pop)
    while group2:
        pop = group2.pop(0)
        result_array.append(pop)
        result.append(pop)
    return result


merge_sort(list(map(int, sys.stdin.readline().split())), 0)
print(-1 if len(result_array) <= N else result_array[N - 1])
