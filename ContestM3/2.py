
def hash_(string, x, p):
    result = 0
    for i in range(len(string)):
        result = (result*x + ord(string[i])) % p
    return result 


def cyclic_shift(string_s, string_t, x, p):
    shift_power = 0
    string_t = " ".join(string_t)
    string_s = " ".join(string_s)
    hs = hash_(string_s, x, p)
    ht = hash_(string_t, x, p)
    for i in range(len(string_s)+1):
        if string_t != string_s:
            part = string_t.partition(' ')
            string_t = part[-1] + part[1] + part[0]
            shift_power += 1
            ht = hash_(string_t, x, p)
            if shift_power == len(string_s):
                return -1
        else:
            return shift_power

string_s = input()
string_t = input()
x = 27
p = 1e9 + 7
print(cyclic_shift(string_s, string_t, x, p))