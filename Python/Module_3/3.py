# def main():
#     s = input()
#     t = input()
#     p = prefix(t+'#'+s)
#     for i in range(len(p)):
#         if p[i] == len(t):
#             print(i-2*len(t), end=" ")


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
    s = str(input())
    p = prefix(s)
    n = len(p)
    flag = True
    k_zero = p.count(0)
    print(p)
    if n*[0] == p:
        k = n
    else:
        k = 1
        while p[k] == 0:
            k += 1
        if k_zero == k:
            if p.count(1) == 2:
                k += 1
            elif p.count(1) > 2:
                a = p[k:k+p.count(1)]
                b = [1]*p.count(1)
                if a == b:
                    k += p.count(1)-1
                else:
                    k = n

        elif p[-1] == 0:
            k = n
        else:
            while p[k] != 0:
                k += 1
            while p[k] == 0:
                k += 1
    if n % k == 0:
        print(n//k)
    else:
        print(1)


main()
