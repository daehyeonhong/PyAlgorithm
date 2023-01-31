import sys

N = int(sys.stdin.readline())
N_List = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_List = list(map(int, sys.stdin.readline().split()))

result = []
for M_Item in M_List:
    result.append(str(1 if (N_List.__contains__(M_Item)) else 0))
print(" ".join(result))
