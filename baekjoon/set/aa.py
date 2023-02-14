import sys
sysLine = sys.stdin.readline
N = int(sysLine().rstrip())
N_Dict = {}
for key in map(int, sysLine().rstrip().split()):
    N_Dict[key] = 1 if not key in N_Dict else N_Dict[key]+1
M = int(sysLine())
M_ = M
fin_str = []
for key in  map(int, sysLine().rstrip().split()):
    M_=M_-1
    if key in N_Dict:
        val = N_Dict[key]
        fin_str.append(str(N_Dict[key]))
        M = M-val
    else:
        fin_str.append('0')
    if M == 0:
        for key in range(M_):
            fin_str.append('0')
        break
print(' '.join(fin_str))