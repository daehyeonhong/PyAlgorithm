import sys

arr = []
for i in range(9):
    arr.append(int(sys.stdin.readline()))

arr.sort()
sum_val = sum(arr)
diff = sum_val - 100
target = []


def method_name(arg):
    length = len(arg)
    for idx in range(length):
        for j in range(idx + 1, length):
            i_ = arr[idx]
            j_ = arr[j]
            if i_ + j_ == diff:
                arr.pop(arr.index(i_))
                arr.pop(arr.index(j_))
                return arr
            elif i_ + j_ > diff:
                continue


for item in method_name(arr):
    print(item)
