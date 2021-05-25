def prefix(s):
    v = [0]*len(s)
    count = 1
    for i in range(1,len(s)):
        k = v[i-1]
        while k > 0 and s[k] != s[i]:
            k = v[k-1]
        if s[k] == s[i]:
            k = k + 1
        else:
            k = 0
        v[i] = k
        if v[i] < 2:
            count = i
    return count
s = input()
print(prefix(s))