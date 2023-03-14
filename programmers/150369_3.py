def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries or pickups:
        delivery_count=0
        pickup_count=0
        delivery_length=0
        pickup_length=0
        isFirstDelivery = True
        isFirstPickup = True
        for delivery_index in reversed(range(len(deliveries))):
            delivery = deliveries[delivery_index]
            delivery_count += delivery
            if isFirstDelivery and delivery > 0 :
                delivery_length=delivery_index+1
                isFirstDelivery = False
            if delivery_count>=cap:
                deliveries[delivery_index]=delivery-cap
                break
            deliveries.pop(delivery_index)
        for pickup_index in reversed(range(len(pickups))):
            pickup = pickups[pickup_index]
            pickup_count+=pickup
            if isFirstPickup and pickup > 0:
                pickup_length=pickup_index+1
                isFirstPickup=False
            pickup_count+=pickup
            if pickup_count>=cap:
                pickups[pickup_index]=pickup-cap
                break
            pickups.pop(pickup_index)
        answer+=delivery_length if delivery_length>pickup_length else pickup_length
    return answer*2
# cap=3
# [1,1,1,1,1,4,0,0]
# [1,1,1,1,1,1,1,1]
# [0,0,1,1,1,0,0,0]
#print(solution(4, 2, [6,0,0], [0,0, 0]))
print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]), 16)
# print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]), 30)
# print(solution(4, 5, [8, 0, 8, 0, 4], [0, 0, 0, 0, 20]), 50)
# print(solution(2, 2, [0, 1], [0, 4]), 8)
# print(solution(2, 2, [0, 0], [0, 6]), 12)
# print(solution(2, 2, [0, 0], [4, 0]), 4)
# print(solution(2, 2, [5, 0], [0, 3]), 10)
# print(solution(5, 3, [5, 0, 5], [0, 1, 10]), 16)
# print(solution(5, 3, [5, 1, 5], [0, 1, 10]), 16)
# print(solution(2, 3, [0, 6, 13], [19, 0, 1]), 54)
# print(solution(2, 3, [4, 2, 1], [0, 4, 1]), 16)
# print(solution(4, 5, [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]), 12)
# print(solution(4, 4, [25, 24, 51, 0], [51, 0, 0, 49]), (13 * 4 + 6 * 2 + 6) * 2)
