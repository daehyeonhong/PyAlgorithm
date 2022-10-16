from collections import Counter
import math


def 산술평균(arr):
    length = len(arr)
    sum = 0
    for i in range(length):
        sum += arr[i]
    return round(sum / length)


def 중앙값(arr):
    return arr[math.floor(len(arr) / 2)]


def 범위(arr):
    return arr[len(arr)] - arr[0]


def 최빈값(arr):
    ctn = Counter(arr)
    print(ctn)
    mcnt = ctn.most_common(1)
    if (mcnt[0][0]):
        return mcnt[0][0]


input_val = int(input())
input_val_arr = []
for i in range(input_val):
    input_val_arr.append(int(input()))
result_val_arr = sorted(input_val_arr)
print(result_val_arr)
print(산술평균(result_val_arr))
print(중앙값(result_val_arr))
print(최빈값(result_val_arr))
print(범위(result_val_arr))
