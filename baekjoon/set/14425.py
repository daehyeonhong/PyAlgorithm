import sys
sysLine = sys.stdin.readline
N, M = map(int, sysLine().rstrip().split())

S = set([ sysLine().rstrip() for i in range(N)])

count = 0

for i in range(M):
    input = str( sysLine().rstrip())
    count += 1 if S.__contains__(input) else 0

print(count)