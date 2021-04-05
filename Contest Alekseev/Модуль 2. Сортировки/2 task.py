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