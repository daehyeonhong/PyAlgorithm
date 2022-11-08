import itertools

array = [int(input()) for _ in range(9)]

combinations = itertools.combinations(array, 7)
for i in combinations:
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break
