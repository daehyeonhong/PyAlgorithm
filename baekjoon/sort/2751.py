import sys

length = int(input())
inp_list = []

for i in range(length):
    inp_list.append(int(sys.stdin.readline()))

for i in sorted(inp_list):
    print(i)
