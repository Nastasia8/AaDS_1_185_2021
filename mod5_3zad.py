from math import gcd
def build(v,l,r,do,a):
    if r - l == 1:
        do[v]= a[l]
        return
    m=(r+l)//2
    build(2*v+1,l,m,do,a)
    build(2*v+2,m,r,do,a)
    do[v] = gcd(do[2*v+1],do[2*v+2])

def nod(v,l,r,do,ql,qr):
    if ql<=l and qr>=r:
        return do[v]
    if ql >= r or qr<=l:
        return 0
    m = (r+l)//2
    tl = nod (2*v+1,l,m,do,ql,qr)
    tr = nod (2*v+2,m,r,do,ql,qr)

    return gcd(tl,tr)

def main():
    n=int(input())
    a= list(map(int, input().split(maxsplit=n)))
    do= [0]*4*n
    build(0,0,n,do,a)
    q = int(input())
    index = []
    while q !=0:
        l,r = map(int,input().split())
        index.append(nod(0,0,n,do,l-1,r))
        q-=1
    print(*index)


main()