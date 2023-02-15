import sys
add = sys.stdin.readline().rstrip()
set_var = set()
var_str = add
for first in range(len(add)):
    for end in range(first ,len(add)):
        set_var.add(var_str[first:end+1])
print(len(set_var))
#0
#'a,b,a,b,c
#1
#'ab'ab' ab bc