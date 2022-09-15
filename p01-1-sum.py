def sum_n(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s


def print_cute():
    name = '감자'
    age = 14
    phone = 1
    print("Hi {}, you are {}".format(name, age))
    print("Hi {name}, you are {age}".format(age=age, name=name))
    print("Hi {0}, you are {1}".format(name, age))
    print('{} + {} = {}'.format(1, 1, '귀요미'))
    print(f'{name:10}==>{phone:10d}')


print(sum_n(10))
print(sum_n(100))
print_cute()
