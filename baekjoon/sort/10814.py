import sys

length = int(sys.stdin.readline())
funcSet = [[]] * 201
for i in range(length):
    x, y = sys.stdin.readline().split()
    int_x = int(x)
    if funcSet[int_x] == []:
        funcSet[int_x] = [y]
    else:
        x_ = funcSet[int_x]
        x_.append(y)
        funcSet[int_x] = x_

for idx in range(len(funcSet)):
    a = funcSet[idx]
    if a == {''}:
        continue
    else:
        semi_set = []
        while a:
            semi_set.append(a.pop())
        while semi_set:
            print(f'{idx} {semi_set.pop()}')
