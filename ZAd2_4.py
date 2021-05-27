l = int(input())
s = list(map(int, input().split()))
a = [0] 
b = [0] 
for i in range(l):
    while a[-1] == b[-1] + 1:
        b.append(a[-1])
        a.pop()
    if s[i] == b[-1] + 1:
        b.append(s[i])
    else:
        a.append(s[i])
 
while a[-1] == b[-1] + 1:
    b.append(a[-1])
    a.pop()
 
if b[-1] == l:
    print('YES')
else:
    print('NO')