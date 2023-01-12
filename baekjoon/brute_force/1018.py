import sys

sysLine = sys.stdin.readline
N, M = map(int, sysLine().split())
totalArry = []
for i in range(N):
    totalArry.append(sysLine())


min_count = 64


def judgeRaceCheck(arr):
    check_split = list(
        'WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW')
    result = 0

    for i in range(len(check_split)):
        if check_split[i] != arr[i]:
           result += 1
    return 64 - result if 32 <= result else result


for i in range(0, N-7):
    for j in range(0, M-7):  
        fin_str = ''
        for m in range(8):

            fin_str += ''.join(totalArry[i+m][0+j:8+j])

        res = judgeRaceCheck(list(fin_str))
        min_count = min_count if min_count < res else res

print(min_count)
