def proiz(k):
    p = 1
    for i in range(1,k+1):
        p *= 2**i-1
    return p

k = int(input("K: "))
print(proiz(k))