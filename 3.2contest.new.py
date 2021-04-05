def get_hesh(s, n, p, x):
    res = 0
    for i in range(n):
        res = (res*x+ord(s[i])) % p
    return res


def robin_karp(s, string2, p, x):
    ht = get_hesh(string2, len(string2), p, x)
    hs = get_hesh(s, len(s), p, x)
    xt = 1
    for i in range(len(string2)):
        xt = (xt*x) % p
    for i in range(len(s)):
        if (ht == hs):
            return i
        ht = (ht*x-ord(string2[i])*xt+ord(string2[i])) % p
    return -1

string = input()
string2 = input()
p = 1e9 + 7
x = 26
print(robin_karp(string, string2, p, x))
