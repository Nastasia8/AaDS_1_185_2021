def hashing(arr):
    global q, h
    p = 0
    for i in range(len(arr)):
        p = (p*h+ord(arr[i]))%q
    return p

def finding(s, t):
    global q, h
    l = len(s)
    c = 0
    hf = 1
    hs = hashing(s)
    ht = hashing(t)
    if ht == hs:
        return 0
    else:
        for i in range(l):
            hf = (h * hf) % q
        for i in range(l):
            if ht != hs:
                ht = ((ht * h) - ord(t[i])*hf + ord(t[i])) % q
                ht = (ht+q)%q
                c += 1
        if ht == hs:
            return c
        else:
            return -1


q = 1e9 + 7
h = 26
s = input()
t = input()
print(finding(s, t))