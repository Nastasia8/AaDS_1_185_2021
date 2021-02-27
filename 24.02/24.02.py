#1
n= int(input())
sort=input().split(" ")
sort = [int(i) for i in sort]
proveka=[i for i in sort]
k=0

for i in range(n-1):
    for j in range (n-1-i):
        if sort[j]>sort[j+1]:
            sort[j],sort[j+1]=sort[j+1],sort[j]
            k+=5
            print(*sort,sep=" ")
        
if k == 0:
    print(0)
#2
n= int(input())
sort=[]
for i in range (n): 
    sort.append(input().split(" "))
sort=[[int(sort[i][j]) for j in range(2)] for i in range(n)]
for i in range(n-1):
    for j in range (n-1-i):
        if  sort[j][1]<sort[j+1][1]:
            sort[j],sort[j+1]=sort[j+1],sort[j]
        if  sort[j][1]==sort[j+1][1]:
            if sort[j][0]>sort[j+1][0]:
                sort[j],sort[j+1]=sort[j+1],sort[j]   
[print(i[0], i[1]) for i in sort]