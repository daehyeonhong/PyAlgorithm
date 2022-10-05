def bubble_sort(arg):
    length = len(arg)
    flag = True
    while flag:
        flag = False
        for i in range(0, length - 1):
            j = i + 1
            i_val = arg[i]
            j_val = arg[j]
            if i_val > j_val:
                print(f'before : {arg}')
                print(f'change arg[i] : {i_val}, arg[j] : {j_val}')
                arg[i], arg[j] = arg[j], arg[i]
                flag = True
                print(f'after : {arg}')
            else:
                print(f'not change arg[i] : {i_val}, arg[j] : {j_val}')


arr = [2, 4, 5, 1, 3]
arr2 = [3, 4, 5, 2, 1]
arr3 = [5, 4, 3, 2, 1]
bubble_sort(arr)
print(arr)
bubble_sort(arr2)
print(arr2)
bubble_sort(arr3)
print(arr3)
