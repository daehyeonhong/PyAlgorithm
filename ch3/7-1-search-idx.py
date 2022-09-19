def search_first_idx(arg, target):
    result = []
    for i in range(len(arg)):
        if target == arg[i]:
            result.append(i)
    return result


number_list = [1, 3, 4, 1, 4, 5, 2, 5, 6, 6, 7, 8, 7, 43, 6, 63, 63, 63, 54]
print(search_first_idx(number_list, 1))
print(search_first_idx(number_list, 80))
