def solution(cap, n, deliveries, pickups):
    answer = 0
    while True:
        length = len(deliveries)
        A = 0
        B = 0
        while length != 0 and (cap >= A and cap >= B) and (pickups or deliveries):
            del_pop = deliveries.pop()
            pick_pop = pickups.pop()
            A += del_pop
            B += pick_pop
        if A > cap or B > cap:
            deliveries.append(max(A - cap, 0))
            pickups.append(max(B - cap, 0))
        answer += length * 2
        if length <= 0:
            return answer


print(solution(2, 2, [0, 0], [0, 4]))
