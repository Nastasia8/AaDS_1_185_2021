def hashing(arr):
    global q, h
    p = 0
    for i in range(len(arr)):
        p = (p*h+ord(arr[i]))%q
    return p

def finding(s, t):
    global q, h
    indexes = []
    ls = len(s)
    lt = len(t)
    hf = 1
    hs = hashing(s[0:lt])
    ht = hashing(t)
    for i in range(lt):
        hf = (h*hf)%q
    for i in range(ls-lt+1):
        if ht == hs:
            indexes.append(i)
        if (i + lt) < ls:
            hs = ((hs * h) - ord(s[i])*hf + ord(s[i+lt])) % q
            hs = (hs+q)%q

    print(*indexes)

q = 1e9 + 7
h = 26
s = input()
t = input()
finding(s, t)