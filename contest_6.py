n = int(input())
c = [int(i) for i in input().split()]
k = int(input())
p = [int(j) for j in input().split()]
for i in range(0, n):
    if c[i] < p.count(i+1):
        print('yes')
    else:
        print('no')