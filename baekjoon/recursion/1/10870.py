import sys

n = int(sys.stdin.readline())
dp = [0] * (n + 1)


def fibonacci(arg):
    if arg == 0:
        return 0
    elif arg == 1:
        return 1
    else:
        if dp[arg - 2]:
            return dp[arg - 1] + dp[arg - 2]
        fibonacci_result = fibonacci(arg - 1) + fibonacci(arg - 2)
        dp[arg] = fibonacci_result
        return fibonacci_result


print(fibonacci(n))
