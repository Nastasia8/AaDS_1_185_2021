def prefix(s):
    p = [0] * len(s)
    index_ = 1
    for i in range(len(s) - 1):
        j = p[i]
        while j > 0 and s[j] != s[i + 1]:
            j = p[j - 1]
        if s[j] == s[i + 1]:
            p[i + 1] = j + 1
        else:
            p[i + 1] = 0
        if p[i + 1] < 2:
            index_ = i + 1
    return index_


s = input()
print(prefix(s))