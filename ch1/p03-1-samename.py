# input : {arg : 배열}
# output: 중복된 이름 배열
def find_same_name(arg):
    result = set()
    length = len(arg)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if arg[i] == arg[j]:
                result.add(arg[i])
    return result


list = ['Tom', 'Jerry', 'Mike', 'Tom']
list2 = ['Tom', 'Jerry', 'Mike', 'Tom', 'Mike']

print(find_same_name(list))
print(find_same_name(list2))
