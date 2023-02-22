def solution(cap, n, deliveries, pickups):
    answer = 0
    devliverCount  = cap # 4
    pickupCount = cap
    lengtN = n
    while lengtN >= 1:
       lastDeliver = deliveries.pop()
       lastPickup = pickups.pop()
       if lastDeliver == 0 and lastPickup == 0:
           lengtN -= 1
           lastDeliver = deliveries.pop()
           lastPickup = pickups.pop()

       devliverCount = devliverCount - lastDeliver # 2
       pickupCount = pickupCount -  lastPickup  # 0
       if devliverCount < 1 or pickupCount < 1:
            answer += lengtN
            lengtN = len(deliveries)

       if  devliverCount < 0:
           deliveries.append(lastDeliver)
           lengtN += 1

       if  pickupCount < 0:
           pickups.append(lastPickup)
           lengtN += 1

    return answer


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))


def solution(cap, n, deliveries, pickups):
    answer = 0
    while True:
        A = 0
        B = 0
        length = 0
        isFirstNotZero = True
        while pickups and (cap >= A and cap >= B):
            A += deliveries.pop()
            B += pickups.pop()
            if isFirstNotZero and (A != 0 or B != 0):
                isFirstNotZero = False
                length = len(deliveries) + 1
        if A > cap or B > cap:
            deliveries.append(max(A - cap, 0))
            pickups.append(max(B - cap, 0))
        answer += length * 2
        if length <= 0:
            return answer


print(solution(2, 2, [0, 0], [0, 4]))
