input_val = int(input())
input_val_arr = []
for i in range(input_val):
    input_val_arr.append(int(input()))
result_val_arr = sorted(input_val_arr)
for r_idx in range(len(result_val_arr)):
    print(result_val_arr[r_idx])


def 산술평균(arr):
    length = len(arr)
    sum = 0
    for i in range(length):
        sum += arr[i]
    return round(sum / length)
