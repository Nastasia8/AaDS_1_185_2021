def prefix(s):
    v = [0]*len(s)
    for i in range(1, len(s)):
        k = v[i-1]
        while k > 0 and s[k] != s[i]:
            k = v[k-1]
        if s[k] == s[i]:
            k = k + 1
        v[i] = k
    return v


def main():
    s = input()
    p = prefix(s)
    print(p)
    n = len(p)
    res = 0
    if 1 not in p:
        k = s
    else:
        k = s[0:len(s) - p[::-1].index(1) - 1]
    if s == k*(n//len(k)):
        res = n//len(k)
    else:
        res = 1

    print(res)
    if res > 1:
        print(n)
    elif n % (n - p[-1]) != 0 and p[-2] <= p[-1]:
        x = n - p[-1]
        while n % x != 0:
            n += 1
        print(n)
    else:
        print(n)


main()
