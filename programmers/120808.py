import math


def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    num1 = numer1 * denom2
    num2 = numer2 * denom1
    num = num1 + num2
    a = math.floor(denom / num)

    answer = [num % a, denom / a]
    return answer

