import sys

str = sys.stdin.readline().strip()

def sumFn(gap):
    return len({str[i:i+gap] for i in range(len(str)+1-gap)})

print(sum(sumFn(gap) for gap in range(1, len(str)+1)))
