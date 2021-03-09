n = int(input())
c = [int(a) for a in input().split()]
k = int(input())
p = [int(a) for a in input().split()]
mas = [0]*101
for i in p:
    mas[i] += 1
for i in range(n):
    if mas[i+1] > c[i]:
        print('yes')
    else:
        print('no')
