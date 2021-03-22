def prefix(s):
    p = [0] * len(s)
    for i in range(len(s)-1):
        j = p[i]
        while j > 0 and s[j] != s[i+1]:
            j = p[j-1]
        if s[j] == s[i+1]:
            p[i+1] = j + 1
        else:
            p[i+1] = 0
    return p

def fun(s):
    i = 0
    while prefix(s)[i] == 0:
        i += 1
    t = s[:i]
    return len(s) // len(t)

s = input()
print(fun(s))

