n = int(input())
a = []  
for i in range(0, n):  
    _str = input()  
    _split = _str.split(' ')  
    pair = (int(_split[0])), int(_split[1])  
    a.append(pair) 
for i in range(n-1):
    for j in range(n-i-1):
        if a[j][1] < a[j+1][1]:
            a[j], a[j+1] = a[j+1], a[j]
        if a[j][1] == a[j+1][1]:
            if a[j][0] > a[j+1][0]:
                a[j], a[j+1] = a[j+1], a[j]
[print(i[0], i[1]) for i in a]  