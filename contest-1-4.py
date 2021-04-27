def p_c(s):
    p = [0]*len(s)
    for i in range(len(s)-1):
        j = p[i]
        while j > 0 and s[j] != s[i+1]:
            j = p[j-1]
        if s[j] == s[i+1]:
            p[i+1] = j+1
        else:
            p[i+1] = 0
    return p

st = input()
pc = p_c(st)
index = []
if 1 in pc:
    for i in range(len(st)):
        if pc[i] == 1:
            index.append(i)
    pattern = st[:index[-1]]
else:
    pattern = st
if st == pattern*(len(st)//len(pattern)):
    print(len(st) // len(pattern))
else:
    print(1)

