import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

for i in reversed(str(y)):
    print(int(i) * x)
print(x * y)
