input_val = int(input())
input_val_arr = []
for i in range(input_val):
    input_val_arr.append(int(input()))
result_val_arr = sorted(input_val_arr)
for r_idx in range(len(result_val_arr)):
    print(result_val_arr[r_idx])
