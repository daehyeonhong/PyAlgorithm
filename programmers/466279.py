def solution(arr):
    if len(arr) == 1:
        return [-1]
    answer = []
    for item in range(len(arr)):
        if sorted(arr)[0] != arr[item]:
            answer.append(arr[item])
    return answer
