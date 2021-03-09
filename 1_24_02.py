# сортировка пузырьком
n=int(input())
a=input().split()[:n]
k=0
for i in range(n-1):
    for j in range (n-i-1):
        if a[j]>a[j+1]:
            a[j], a[j+1]=a[j+1], a[j]
            k=k+1
            print(*a, sep=" ")
if k==0:
    print(0)