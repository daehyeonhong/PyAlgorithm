import sys
sysLine = sys.stdin.readline
N, M = map(int, sysLine().rstrip().split())

S = {}
RS = {}

for i in range(N):
   input = sysLine().rstrip()
   S[input] = i
   RS[i] = input

l = []

for i in range(M):
    input = sysLine().rstrip()
    l.append( RS[int(input)-1]if input.isdigit() else S[input]+1)

for item in l:
    print(item)
