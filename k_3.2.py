def get_hesh(s, n, p, x):
    res = 0
    for i in range(n):
        res = (res*x+ord(s[i])) % p
    return res


def rk(s, st, p, x):
    ht = get_hesh(st, len(st), p, x)
    hs = get_hesh(s, len(s), p, x)
    xt = 1
    for i in range(len(st)):
        xt = (xt*x) % p
    for i in range(len(s)):
        if (ht == hs):
            return i
        ht = (ht*x-ord(st[i])*xt+ord(st[i])) % p
    return -1

s = input()
st = input()
p = 1e9 + 7
x = 26
print(rk(s, st, p, x))
#Делали в универе