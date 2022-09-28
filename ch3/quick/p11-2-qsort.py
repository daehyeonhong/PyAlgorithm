def quick_sort_sub(arg, start, end):
    if end - start <= 0:
        return
    pivot = arg[end]
    i = start
    for j in range(start, end):
        if arg[j] <= pivot:
            arg[i], arg[j] = arg[j], arg[i]
            i += 1
    arg[i], arg[end] = arg[end], arg[i]
    quick_sort_sub(arg, start, i - 1)
    quick_sort_sub(arg, i + 1, end)


def quick_sort(arg):
    quick_sort_sub(arg, 0, len(arg) - 1)


arr = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
quick_sort(arr)
print(arr)
