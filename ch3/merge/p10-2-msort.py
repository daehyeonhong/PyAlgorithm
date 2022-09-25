def merge_sort(arg, n, st):
    n += 1
    length = len(arg)
    if length <= 1:
        return

    center = length // 2
    group1 = arg[:center]
    group2 = arg[center:]
    merge_sort(group1, n, 'g1')
    merge_sort(group2, n, 'g2')
    i1 = 0
    i2 = 0
    ia = 0
    print(f'case0 idx: {n}, arg : {arg}, group1 : {group1}, group2 : {group2}')
    while i1 < len(group1) and i2 < len(group2):
        if group1[i1] < group2[i2]:
            arg[ia] = group1[i1]
            arg[ia] = group1[i1]
            i1 += 1
            ia += 1
            print(f'case1 idx: {n}, arg : {arg}, group1 : {group1}, group2 : {group2}')
        else:
            arg[ia] = group2[i2]
            ia += 1
            i2 += 1
            print(f'case2 idx: {n}, arg : {arg}, group1 : {group1}, group2 : {group2}')
    while i1 < len(group1):
        arg[ia] = group1[i1]
        i1 += 1
        ia += 1
        print(f'case3 idx: {n}, arg : {arg}, group1 : {group1}, group2 : {group2}')
    while i2 < len(group2):
        arg[ia] = group2[i2]
        ia += 1
        i2 += 1
        print(f'case4 idx: {n}, arg : {arg}, group1 : {group1}, group2 : {group2}')


arr = [11, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(arr, -1, 'root')
print(f'result : {arr}')
