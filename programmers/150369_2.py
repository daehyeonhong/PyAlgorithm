def solution(cap, n, deliveries, pickups):
    answer = 0
    while True:
        a = 0
        b = 0
        length = len(deliveries)
        is_first_not_zero = True
        while pickups and (cap >= a and cap >= b):
            a += deliveries.pop()
            b += pickups.pop()
            if is_first_not_zero and (a == 0 and b == 0):
                length -= 1
            else:
                is_first_not_zero = False
        if a > cap or b > cap:
            deliveries.append(max(a - cap, 0))
            pickups.append(max(b - cap, 0))
        answer += length * 2
        if length <= 0:
            return answer


print(solution(2, 2, [0, 0], [0, 4]))
