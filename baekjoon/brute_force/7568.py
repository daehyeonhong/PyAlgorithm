import sys

N: int = int(sys.stdin.readline())
student_list = []
for i in range(N):
    weight, height = map(int, sys.stdin.readline().split())
    student_list.append((weight, height))
for i in student_list:
    rank = 1
    for j in student_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")
