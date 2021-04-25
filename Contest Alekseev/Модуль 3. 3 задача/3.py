def prefix(A, n):
    res = [0]*n
    res[0] = 0
    for i in range(n-1):
        j = res[i]
        while (j > 0 and A[i+1] != A[j]):
            j = res[j-1]
        if (A[i+1] == A[j]):
            res[i+1] = j + 1
        else:
            res[i+1] = 0
    return res

A = input()
res = prefix(A, len(A))
k = len(A) - res[len(A)-1]
if (len(A) % k == 0):
    print(len(A)//k)
else:
    print(1)
