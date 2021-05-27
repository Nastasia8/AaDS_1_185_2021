from math import gcd
def build(v,g,r,do,a):
    if r - g == 1:
        do[v]= a[g]
        return
    m=(r+g)//2
    build(2*v+1,g,m,do,a)
    build(2*v+2,m,r,do,a)
    do[v] = gcd(do[2*v+1],do[2*v+2])
def update(v,l,r,do,idx,value):
    if r-l==1:
        do[v]=value
        return
    m=(r+l)//2
    if idx < m:
        update (2*v+1,l,m,do,idx,value)
    else:
        update (2*v+2,m,r,do,idx,value)
    do[v]= gcd (do[2*v+1],do[2*v+2])
def get_max(v,l,r,do,ql,qr):
    if ql<=l and qr>=r:
        return do[v]
    if ql >= r or qr<=l:
        return 0
    m = (r+l)//2
    tl = get_max (2*v+1,l,m,do,ql,qr)
    tr = get_max (2*v+2,m,r,do,ql,qr)
    return gcd(tl,tr)
def main():
    n=int(input())
    a= list(map(int, input().split(maxsplit=n)))
    do= [0]*4*n
    build(0,0,n,do,a)
    q = int(input())
    index = []
    while q !=0:
        que,l,r = map(str,input().split())
        if que=="s":
            index.append(get_max(0,0,n,do,int(l)-1,int(r)))
        else:
            update(0,0,n,do,int(l)-1,int(r))
        q-=1
    print(*index)
main()