def solution(cap, n, deliveries, pickups):
    answer = 0
    while True:
        a = 0
        b = 0
        length = n
        isFirst = True
        for i in reversed(range(length)):
            deliveries[i] 
            pickups[i]
        while pickups and (cap >= a and cap >= b):
            del_var = deliveries.pop()
            pic_var = pickups.pop()
            a += del_var
            b += pic_var
            if isFirst:
                if del_var+pic_var == 0:
                    length-=1
                else:
                    isFirst=False
        if a > cap or b > cap:
            deliveries.append(max(a - cap, 0))
            pickups.append(max(b - cap, 0))
        answer += length * 2
        if length <= 0:
            return answer

print(solution(4, 2, [6,0,0], [0,0, 0]))
print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]), 16)
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]), 30)
print(solution(4, 5, [8, 0, 8, 0, 4], [0, 0, 0, 0, 20]), 50)
print(solution(2, 2, [0, 1], [0, 4]), 8)
print(solution(2, 2, [0, 0], [0, 6]), 12)
print(solution(2, 2, [0, 0], [4, 0]), 4)
print(solution(2, 2, [5, 0], [0, 3]), 10)
print(solution(5, 3, [5, 0, 5], [0, 1, 10]), 16)
print(solution(5, 3, [5, 1, 5], [0, 1, 10]), 16)
print(solution(2, 3, [0, 6, 13], [19, 0, 1]), 54)
print(solution(2, 3, [4, 2, 1], [0, 4, 1]), 16)
print(solution(4, 5, [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]), 12)
print(solution(4, 4, [25, 24, 51, 0], [51, 0, 0, 49]), (13 * 4 + 6 * 2 + 6) * 2)
