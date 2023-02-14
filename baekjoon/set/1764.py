import sys

듣, 보 = map(int, sys.stdin.readline().rstrip().split())
듣보_목록 = {}
결과_목록 = []
for i in range(듣):
    value = sys.stdin.readline().rstrip()
    듣보_목록[value] = value

for i in range(보):
    try:
        듣보 = 듣보_목록.pop(sys.stdin.readline().rstrip())
        결과_목록.append(듣보)
    except:
        continue
print(len(결과_목록))
for item in sorted(결과_목록):
    print(item)