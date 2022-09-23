arr = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]


def merge_sort(arg, num):
    num+=1
    length = len(arg)
    if length <= 1:
        return arg
    center = length // 2
    print(f'num : {num}, arg : {arg}')
    group1 = merge_sort(arg[:center], num)
    group2 = merge_sort(arg[center:], num)

    result = []
    while group1 and group2:
        result.append(group1.pop(0) if group1[0] < group2[0] else group2.pop(0))
    while group1:
        result.append(group1.pop(0))
    while group2:
        result.append(group2.pop(0))
    return result


print(merge_sort(arr, 0))
