N = int(input())
a = list(map(int, input().split(maxsplit=N)))
count=0
for i in range(N-1):
    for j in range(N-i-1):
        if a[j] > a[j+1]:
            count=1
            a[j], a[j+1] = a[j+1], a[j]
            print( " ".join( repr(e) for e in a ) )
            
if(count==0):
    print(0)
