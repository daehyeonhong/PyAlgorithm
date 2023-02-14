import sys
from collections import Counter
from operator import itemgetter

N = int(sys.stdin.readline().rstrip())

numcard = sys.stdin.readline().rstrip().split()

counter = Counter(numcard)

M = int(sys.stdin.readline().rstrip())

candidate = sys.stdin.readline().rstrip().split()

result = str(itemgetter(*candidate)(counter))
result = result.replace(',', '')
        
print(result[1:-1])