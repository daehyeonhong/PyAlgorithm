# input : {n : 배열}
# output: 최댓값 위치

def find_max(a):
    max_v: Int = a[0]
    max_v_ind = 0
    for i in range(len(a)):
        max_v_ind = i if a[i] > max_v else max_v_ind
        max_v = a[i] if a[i] > max_v else max_v
    return max_v_ind


fst = [1, 92, 18, 33, 58, 7, 33, 42]
snd = [101, 1, 41, 377, 11, 235, 62]
trd = [11, 23, 134, 123, 26, 65, 77, 132]

fstValue = find_max(fst)
sndValue = find_max(snd)
trdValue = find_max(trd)
print(fstValue)
print(sndValue)
print(trdValue)
