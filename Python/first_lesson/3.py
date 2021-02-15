k = int(input("введи k"))


def proiz(k):
    n = 1
    pr = 1
    for i in range(n, k):
        pr *= (2**i) - 1
    print(pr)


proiz(k)
