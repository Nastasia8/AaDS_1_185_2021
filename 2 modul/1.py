n=int(input())
a=list(map(int,input().split(maxsplit=n)))
_a = [i for i in a]
for i in range(n-1):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            print(*a, sep = " ")
if _a == a:
    print(0)