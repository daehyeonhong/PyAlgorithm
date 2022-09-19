def search_list(arg, target):
    for i in range(len(arg)):
        if arg[i] == target:
            return i
    return -1


items = [17, 92, 18, 33, 58, 7, 33, 42]

print(search_list(items, 18))
print(search_list(items, 33))
print(search_list(items, 900))
