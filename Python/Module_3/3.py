# def main():
#     s = input()
#     t = input()
#     p = prefix(t+'#'+s)
#     for i in range(len(p)):
#         if p[i] == len(t):
#             print(i-2*len(t), end=" ")


def prefix(s):
    p = [0]*len(s)
    for i in range(len(s)-1):
        j = p[i]
        while j > 0 and s[j] != s[i+1]:
            j = p[j-1]
        if s[j] == s[i+1]:
            p[i+1] = j+1
        else:
            p[i+1] = j
    return p


def main():
    s = str(input())
    p = prefix(s)
    print(p)
    if len(p) == 0:
        print('')
    elif len(p) == 1:
        print(1)

    elif p[-1] == 0:
        print(1)
    else:
        k = 0
        while p[k] == 0:
            k += 1
        if k == 1 and p.count(0) > 1:
            if p[k+1] == 0:
                print(len(s)//(k+2))
            else:
                print(1)
        # elif k <=len(p):
        elif 2*k <= len(p):
            if p[k+1] == 1:
                k += 1
            print(len(s)//k)
        else:
            print(len(s)//k)


main()
