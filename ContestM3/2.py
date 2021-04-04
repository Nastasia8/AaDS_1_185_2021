def hash_(string, x, p):
    result = 0
    for i in range(len(string)):
        result = (result*x + ord(string[i])) % p
    return result 

def cyclic_shift(s, t, x, p):
    shift_power = 0 
    hs = hash_(s, x, p)
    ht = hash_(t, x, p)
    xt = 1
    for i in range(len(t)):
        xt = (xt*x) % p
    for i in range(len(s)):
        if hs == ht:
            return shift_power
        else:
            shift_power += 1
            ht = (ht*x - ord(t[i])*xt + ord(t[i]) + p) % p
    return -1


def main():
    p = 1e9 + 7
    x = 27
    s = input()
    t = input()
    if len(t) == 1 and len(s) == 1:
        if s == t:
            print(0)
        else:
            print(-1)
    else:
        print(cyclic_shift(s, t, x, p))

main()