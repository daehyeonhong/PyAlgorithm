import sys

length = int(sys.stdin.readline())
funcSet = [{}] * 51
for i in range(length):
    inp = sys.stdin.readline().rstrip()
    len1 = len(inp)
    len_ = funcSet[len1]
    if len_ == {}:
        funcSet[len1] = {inp}
    else:
        len_.add(inp)
        funcSet[len1] = len_
for a in funcSet:
    a_len = len(a)
    if a == {}:
        continue
    elif a_len == 1:
        print(a.pop())
    else:
        semi_set = []
        while a:
            semi_set.append(a.pop())
        semi_set.sort(reverse=True)
        while semi_set:
            print(semi_set.pop())
