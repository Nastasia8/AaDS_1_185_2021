def build(v,l,r,do,a):
    if r - l == 1:
        do[v]= a[l]
        return
    m=(r+l)//2
    build(2*v+1,l,m,do,a)
    build(2*v+2,m,r,do,a)
    do[v] = (do[2*v+1]+do[2*v+2])

def update(v,l,r,do,idx,value):
    if r-l==1:
        do[v]=value
        return
    m=(r+l)//2
    if idx < m:
        update (2*v+1,l,m,do,idx,value)
    else:
        update (2*v+2,m,r,do,idx,value)
    do[v] = (do[2*v+1]+do[2*v+2])
def get_summ(v,l,r,do,ql,qr):
    if ql<=l and qr>=r:
        return do[v]
    if ql >= r or qr<=l:
        return 0
    m = (r+l)//2
    tl = get_summ (2*v+1,l,m,do,ql,qr)
    tr = get_summ (2*v+2,m,r,do,ql,qr)
    return (tl+tr)
def find_kth(v, l, r, do, k):
    if k > do[v]:
        return -1
    if r - l == 1:
        return r
    m = (r+l)//2
    if do[2*v+1] >= k:
        return find_kth(2*v+1, l, m, do, k)
    else:
        return find_kth(2*v+2, m, r, do, k - do[2*v+1])
        
def main():
    n=int(input())
    a= [1 if int(i)==0 else 0 for i in input().split()]
    do= [0]*4*n
    build(0,0,n,do,a)
    q = int(input())
    index = []
    while q !=0:
        enter=[i for i in input().split()]
        if enter[0]=="s":
            l,r,k=enter[1:]
            l,r,k=int(l),int(r),int(k)
            sum = get_summ(0, 0, n, do, l-1, r)
            if sum >= k and l == 1:
                index.append(find_kth(0, 0, n, do, k))
            elif sum >= k and l > 1:
                index.append(find_kth(0, 0, n, do, k +(get_summ(0, 0, n, do, 0, l-1))))
            else:
                index.append(-1)
            
        else:
            l,r=enter[1:3]
            l,r=int(l),int(r)
            r=1 if r == 0 else 0
            update(0,0,n,do,int(l)-1,int(r))
        q-=1
    print(*index) 


main()

'''
5
0 0 3 0 2
4
u 1 5
u 1 0
s 1 5 3
s 1 4 2
'''