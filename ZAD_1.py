a=int(input())
f=input().split(" ")
f= [int(i) for i in f]
p=[i for i in f]
k=0
for i in range(a-1):
    for j in range (a-1-i):
        if f[j]>f[j+1]:
            f[j],f[j+1]=f[j+1],f[j]
            k+=2
            print(*f,sep=" ")

if k == 0:
    print(0)