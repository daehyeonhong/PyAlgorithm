# input : {arg : 배열}
# output: 최댓값 위치

def find_max(arg):
    max_idx = 0
    for i in range(1, len(arg)):
        max_idx = i if arg[i] > arg[max_idx] else max_idx
    return max_idx


fst = [1, 92, 18, 33, 58, 7, 33, 42]
snd = [101, 1, 41, 377, 11, 235, 62]
trd = [11, 23, 134, 123, 26, 65, 77, 132]

fstValue = find_max(fst)
sndValue = find_max(snd)
trdValue = find_max(trd)
print(fstValue)
print(sndValue)
print(trdValue)
