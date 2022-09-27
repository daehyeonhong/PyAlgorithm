def quick_sort(arg):
    length = len(arg)
    if length <= 1:
        return arg

    pivot = arg[-1]
    group1 = []
    group2 = []

    for i in range(0, length - 1):
        if arg[i] < pivot:
            group1.append(arg[i])
        else:
            group2.append(arg[i])

    return quick_sort(group1) + [pivot] + quick_sort(group2)


arr = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]

print(quick_sort(arr))
