from random import randint as rand
n = int(input("n = "))
m = int(input('m = '))
arr = [[0]*m]*n
arr = [[arr[i][j] + rand(1, 10) for j in range(m)]for i in range(n)]
print(arr)
print('---------')
# 1
for i in range(n):
    for j in range(m//2):
        arr[i][j], arr[i][-(j+1)] = arr[i][-(j+1)], arr[i][j]
# 2
for i in range(n):
    arr[i] = arr[i][::-1]
print(arr)
