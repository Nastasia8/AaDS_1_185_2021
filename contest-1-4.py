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
    p_arr, ind, k = prefix(s)
    l = len(s)
    t = s[:k - 1]
    if l <= 1:
        return l
    elif p_arr[-1] == l-len(p_arr[:ind+1]) and p_arr[-1] != 0:
        return l//len(p_arr[:ind+1])
    else:
        return 1

s = input()
print(fun(s))

