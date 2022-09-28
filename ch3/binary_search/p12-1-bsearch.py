def binary_search(arg, target):
    start = 0
    end = len(arg) - 1

    while start <= end:
        center = (start + end) // 2
        if target == arg[center]:
            return center
        elif target > arg[center]:
            start = center + 1
        else:
            end = center - 1
    return -1


arr = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(arr, 36))
print(binary_search(arr, 50))
