def prefix_func(k, n):
    s_res = [0]*n
    s_res[0] = 0
    for i in range(n-1):
        j = s_res[i]
        while (j > 0 and k[i+1] != k[j]):
            j = s_res[j-1]
        if (k[i+1] == k[j]):
            s_res[i+1] = j + 1
        else:
            s_res[i+1] = 0
    return s_res

S = input()
k = prefix_func(S, len(S))
print(len(S) - k[len(k)-1])