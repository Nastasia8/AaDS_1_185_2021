n= int(input())
f=[]
for i in range (n): 
    sort.append(input().split(" "))
sort=[[int(f[i][j]) for j in range(2)] for i in range(n)]
for i in range(n-1):
    for j in range (n-1-i):
        if  f[j][1]<f[j+1][1]:
            f[j],f[j+1]=f[j+1],f[j]
        if  f[j][1]==f[j+1][1]:
            if f[j][0]>f[j+1][0]:
                f[j],f[j+1]=f[j+1],f[j]   
[print(i[0], i[1]) for i in f]
a="b"
b=int(a)
print (b)