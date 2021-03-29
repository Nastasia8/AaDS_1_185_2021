def prefix(s):
    n = len(s)
    pi = [0]*n
    for i in range(1, n):
        j = pi[i-1]
        while (j > 0) and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            pi[i] = j + 1
        else:
            pi[i] = j
        k = 0
    if pi == [0]*len(s):
        return len(s)
    else:
        while pi[k] == 0:
            k += 1
        if len(s) > k+1:
            return k+1 if pi[k] == pi[k+1] else k
        else:
            return k


s = str(input())
print(len(s)//prefix(s))
