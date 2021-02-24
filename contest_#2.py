n = int(input())
s = []
for x in range(n):
    s.append([int(x) for x in input().split()])
for i in range(0, n-1):
    for j in range(0, n-i-1):
        if s[j][1] < s[j+1][1]:
            s[j], s[j+1] = s[j+1], s[j]
        elif s[j][1] == s[j+1][1] and s[j][0] > s[j+1][0]:
            s[j], s[j + 1] = s[j + 1], s[j]
[print(m[0], m[1]) for m in s]