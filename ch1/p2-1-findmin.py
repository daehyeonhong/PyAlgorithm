def find_min(arg):
    min_val = arg[0]
    for i in range(1, len(arg)):
        min_val = min_val if min_val < arg[i] else arg[i]
    return min_val


arg = [7, 442, 5553, 4125, 5515, 56, 3, 4, 2, 4, 5, 6, -1, 44, 5262, 6262, 114]
min1 = find_min(arg)
print(min1)
