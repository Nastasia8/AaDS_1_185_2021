#1
n = int(input())
numbers = list(map(int, input().split(maxsplit=n)))
k = [i for i in numbers]
for i in range(n-1):
        for j in range(n-i-1):
            if k[j] > k[j+1]:
                k[j], k[j+1] = k[j+1], k[j]
                print(*k, sep = " ")
if k == numbers:
    print(0)

#2
n= int(input())
arr=[]
for i in range (n): 
    arr.append(input().split(" "))
arr=[[int(arr[i][j]) for j in range(2)] for i in range(n)]
for i in range(n-1):
    for j in range (n-1-i):
        if  arr[j][1]<arr[j+1][1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
        if  arr[j][1]==arr[j+1][1]:
            if arr[j][0]>arr[j+1][0]:
                arr[j],arr[j+1]=arr[j+1],arr[j]   
[print(i[0], i[1]) for i in arr]

#5
n = int(input())
k = list(map(int, input().split(maxsplit=n)))
s = 0
k.sort()
for l in range(n-1):
    if k[l] != k[l+1]:
        s += 1
print(s+1)

#6
from collections import Counter
n=input()
arr = list(map(int, input().split()))
k=input()
l = Counter(map(int, input().split()))
[print('yes' if arr[i - 1] - l[i] < 0 else 'no') for i in range(1, len(arr) + 1)]