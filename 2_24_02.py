n = int(input())
a = []
for i in range(n):
    t = input().split()
    a.append(t)
a = [[int(a[i][j]) for j in range(2)] for i in range(n)]
for i in range(n-1):
    for j in range(n-1):
        if a[j][1] < a[j+1][1]:
            a, a[j+1] = a[j+1], a[j]
        if (a[j][1] == a[j+1][1]) and (a[j][0] > a[j+1][0]):
            a[j], a[j+1] = a[j+1], a[j]
for i in range(n):
    print(*a, sep=" ")