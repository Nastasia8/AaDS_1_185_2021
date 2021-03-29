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
        if n > 2:
            if p[-1]-1 == p[-2]:
                while p[k] == 0:
                    k += 1
                    flag = False
                if k > p[-1]:
                    k = n
                elif max(p) != p[-1]:
                    k = n
                elif p[k] == p[k+1]:
                    k += 1
                elif k == k_zero and p[-1] % k_zero != 0:
                    k = n
                elif k_zero != k:
                    if flag == False:
                        k = n
                    else:
                        k = 1
                        while p[k] != 0:
                            k += 1
                        while p[k] == 0:
                            k += 1
                        for i in range(k, n-1):
                            if p[i] == p[i+1]:
                                k += 1
                        if n % k != 0:
                            k = n
                        elif p[-1] % k != 0:
                            k = 1
            else:
                k = n
    print(n//k)


main()
