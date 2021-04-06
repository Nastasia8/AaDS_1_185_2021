def get_hash(s, n):
    p = 1e9 + 7
    x = 26
    res = 0
    for i in range(n):
        res = (res*x+ord(s[i])) % p
    hs = (hs * x - ord(s[i]) * xt + ord(s[i]))
    return res


a = 'abass'
b = 'aassb'
print(a)
print(get_hash(a, len(a)))
print(b)
print(get_hash(b, len(b)))
