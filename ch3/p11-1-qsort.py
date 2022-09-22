def quick_sort(arg):
    length = len(arg)
    if length <= 1:
        return arg
    pivot = arg[-1]
    group1 = []
    group2 = []
    for i in range(length - 1):
        print(f'arg : {arg}, pivot : {pivot}, group : {group1}, group2 : {group2}')
        if arg[i] < pivot:
            group1.append(arg[i])
        else:
            group2.append(arg[i])
    return quick_sort(group1) + [pivot] + quick_sort(group2)


arr = [88, 7, 65, 4, 6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort(arr))
arr = [6, 8, 3, 9, 19, 1, 2, 4, 7, 5]
print(quick_sort(arr))
