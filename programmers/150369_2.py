from collections import deque

def solution(cap, n, deliveries, pickups):
    answer = 0
    del_dq = deque([])
    pic_dq = deque([])
    for (ind, d_count), p_count in zip(enumerate(deliveries),pickups):
        del_dq += [ind+1]*d_count
        pic_dq += [ind+1]*p_count
    while del_dq or pic_dq:
        del_dist, pic_dist = 0, 0
        if del_dq:
            del_dist = del_dq.pop()
        if pic_dq:
            pic_dist = pic_dq.pop()
        answer += max(del_dist,pic_dist)*2
        for _ in range(cap-1):
            if del_dq:
                del_dq.pop()
            if pic_dq:
                pic_dq.pop()
    return answer
    
# cap=3
# [1,1,1,1,0,0,0,0,1,1,1,1]
# [0,0,0,0,1,1,1,1,0,0,0,0]
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
