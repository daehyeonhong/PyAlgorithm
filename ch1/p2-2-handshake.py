arg1 = ["Kim", "Woo", "Park", "Han"]
arg2 = ["AKAK", "ALAL", "AJAJ", "AHAH"]


def print_handshake(arg):
    arg_len = len(arg)
    for i in range(arg_len):
        for j in range(i + 1, arg_len):
            print(arg[i], '-', arg[j])


print_handshake(arg1)
print_handshake(arg2)
