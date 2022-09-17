# input : {arg : 배열}
# output: 최댓값
def find_max(arg):
    max_v = arg[0]
    for i in range(1, len(arg)):
        max_v = arg[i] if arg[i] > max_v else max_v
    return max_v


def find_max_with_sort(a):
    a.sort()
    return a[-1]


fst = [17, 92, 18, 33, 58, 7, 33, 42]
snd = [101, 1, 41, 525, 11, 235, 62]
trd = [11, 23, 13, 83, 26, 65, 77, 132]

fstValue = find_max(fst)
sndValue = find_max(snd)
trdValue = find_max(trd)
print(fstValue)
print(sndValue)
print(trdValue)

fstSortValue = find_max_with_sort(fst)
scdSortValue = find_max_with_sort(snd)
trdSortValue = find_max_with_sort(trd)
print(fstSortValue)
print(scdSortValue)
print(trdSortValue)

print(f'fstResult: {fstValue.__eq__(fstSortValue)}')
print(f'sndResult: {sndValue == scdSortValue}')
print(f'thrResult: {trdValue == trdSortValue}')
