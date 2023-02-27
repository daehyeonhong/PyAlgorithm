import math


def solution(k, m, score):
    score_len = len(score)
    box_count = math.floor(score_len / m)
    score.sort(reverse=True)
    count = 0
    answer = 0
    print(score)
    for score_item in score:
        count += 1
        if count > box_count * m:
            break
        if count % m == 0:
            answer += (score_item * m)
    return answer


print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))
