def merge_sort(arg):
    length = len(arg)
    if length <= 1:
        return

    center = length // 2
    group1 = arg[:center]
    group2 = arg[center:]
    merge_sort(group1)
    merge_sort(group2)
    i1 = 0
    i2 = 0
    ia = 0
    print(f'group1 : {group1}, group2 : {group2}')
    while i1 < len(group1) and i2 < len(group2):
        if group1[i1] > group2[i2]:
            arg[ia] = group1[i1]
            i1 += 1
            ia += 1
        else:
            arg[ia] = group2[i2]
            ia += 1
            i2 += 1
    sort_left_args(arg, group1, i1, ia)
    sort_left_args(arg, group2, i2, ia)


def sort_left_args(arg, group, idx, base):
    while idx < len(group):
        arg[base] = group[idx]
        idx += 1
        base += 1


arr = [11, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(arr)
print(f'result : {arr}')
