import sys
sysLine = sys.stdin.readline
N = int(sysLine().rstrip())
N_Dict = {}
for key in map(int, sysLine().rstrip().split()):
    N_Dict[key] = 1 if not key in N_Dict else N_Dict[key]+1
M = int(sysLine())
fin_str = []
for key in  map(int, sysLine().rstrip().split()):
    if key in N_Dict:
        val = N_Dict[key]
        fin_str.append(str(N_Dict[key]))
    else:
        fin_str.append('0')
print(' '.join(fin_str))