# 입력: 리스트 a
# 출력: 정렬된 새 리스트
def find_insert_idx(r, v):
    for i in range(0, len(r)):
        if v < r[i]:
            return i
    return len(r)


def insert_sort(arg):
    result = []
    while arg:
        value = arg.pop(0)
        ins_idx = find_insert_idx(result, value)
        result.insert(ins_idx, value)
        print(f'insert_sort({arg}, {result})')
    return result


d = [2, 4, 5, 1, 3]
print(insert_sort(d))
