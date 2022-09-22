def insert_sort(arg):
    length = len(arg)
    for i in range(1, length):
        key = arg[i]
        j = i - 1
        print(f'out({arg}, {key}, {i})')
        while j >= 0 and arg[j] > key:
            arg[j + 1] = arg[j]
            j -= 1
            print(f'in({arg}, {key})')
        arg[j + 1] = key


arr = [2, 4, 5, 1, 3]

insert_sort(arr)
print(arr)

