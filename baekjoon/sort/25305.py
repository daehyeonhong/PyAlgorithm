total, target = map(int, input().split())
scores = map(int, input().split())
print(sorted(scores, reverse=True)[target - 1])