a, b = map(int, input().split())

A = list(input().split())
B = list(input().split())

print(2 * len(set(A + B)) - a - b)