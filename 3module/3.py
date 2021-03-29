def prefix(s):
    p = [0] * len(s)
    ind = 0
    for i in range(len(s)-1):
        j = p[i]
        while j > 0 and s[j] != s[i + 1]:
            j = p[j - 1]
        if s[j] == s[i + 1]:
            p[i+1] = j + 1
        else:
            p[i+1] = 0
        if p[i+1] < 2:
            ind = i+1
    return p, ind


def result(s):
    pref, ind = prefix(s)
    if len(s) == 2 and s[0] == s[1]:
        return 2
    print(ind)
    if 2 in pref:
        t = s[:ind]
    else:
        return 1
    k = 0
    p, NULL = prefix((t+"$"+s))
    for i in range(len(p)):
        if p[i] == len(t):
            k += 1
    if k*t == s:
        return k
    return 1


def main():
    s = input()
    print(result(s))


main()
