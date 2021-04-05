def prefix(s):
    a = [0] * len(s)
    ind = 0
    for i in range(len(s)-1):
        j = a[i]
        while j > 0 and s[j] != s[i + 1]:
            j = a[j - 1]
        if s[j] == s[i + 1]:
            a[i+1] = j + 1
        else:
            a[i+1] = 0
        if a[i+1] < 2:
            ind = i+1
    return a, ind


def result(s):
    pref, ind = prefix(s)
    if len(s) == 2 and s[0] == s[1]:
        return 2
    if 2 in pref:
        t = s[:ind]
    else:
        return 1
    k = 0
    a, NULL = prefix((t+"$"+s))
    for i in range(len(a)):
        if a[i] == len(t):
            k += 1
    if k*t == s:
        return k
    return 1


def main():
    s = input()
    print(result(s))