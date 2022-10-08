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


input_number = int(input())
input_val_arr = []
for i in range(input_number):
    input_val_arr.append(int(input()))
merge_sort(input_val_arr)
for idx in range(len(input_val_arr)):
    print(input_val_arr[idx])
