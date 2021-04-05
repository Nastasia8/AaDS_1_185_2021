n = int(input())
sort = []
for i in range (n):
    sort.append(input().split(" "))
sort = [[int(sort[i][j]) for j in range(2)] for i in range(n)]
for i in range(n - 1):
    for j in range (n - 1 - i):
        if sort[j][1] < sort[j + 1][1]:
            sort[j], sort[j + 1] = sort[j + 1],sort[j]
        if sort[j][1] == sort[j + 1][1] and sort[j][0] > sort[j + 1][0]:
            sort[j], sort[j + 1] = sort[j + 1],sort[j]
[print(i[0], i[1]) for i in sort]