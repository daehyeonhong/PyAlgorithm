def merge_sort(arg):
    length = len(arg)
    if length <= 1:
        return arg
    cen = length // 2
    group1 = merge_sort(arg[:cen])
    group2 = merge_sort(arg[cen:])
    result = []
    while group1 and group2:
        print(f'group1 : {group1}, group2 : {group2}')
        if group1[0] > group2[0]:
            result.append(group1.pop(0))
        else:
            result.append(group2.pop(0))
    print(f'step1 : {result}')
    while group1:
        result.append(group1.pop(0))
    print(f'step2 : {result}')
    while group2:
        result.append(group2.pop(0))
    print(f'step3 : {result}')
    return result


arr = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(arr))
