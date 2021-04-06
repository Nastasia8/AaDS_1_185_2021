a_i= int (input())
a= list (map(int,input().split()))[:a_i]
n_i= int(input())
n= list (map(int,input().split()))[:n_i]

q=[0] * 101
for i in n:
    q[i]+=1
for i in range(a_i):
    if q[i+1]> a[i]:
        print('yes')
    else:
        print('no')