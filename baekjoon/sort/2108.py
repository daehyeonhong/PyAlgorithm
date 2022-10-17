from collections import Counter
import math
import sys


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


def 최빈값(arr, n):
    n = int(sys.stdin.readline())
    nums = []
    for i in range(n):
        nums.append(int(sys.stdin.readline()))
    nums.sort()
    nums_s = Counter(nums).most_common()
    print(round(sum(nums) / n))
    print(nums[n // 2])
    if len(nums_s) > 1:
        if nums_s[0][1] == nums_s[1][1]:
            print(nums_s[1][0])
        else:
            print(nums_s[0][0])
    else:
        print(nums_s[0][0])
    print(nums[-1] - nums[0])


input_val = int(input())
input_val_arr = []
for i in range(input_val):
    input_val_arr.append(int(input()))
result_val_arr = sorted(input_val_arr)
print(산술평균(result_val_arr))
print(중앙값(result_val_arr))
print(최빈값(result_val_arr, input_val))
print(범위(result_val_arr))
