
def build(v,l,r,do,a):
    if r - l == 1:
        do[v]= a[l]
        return
    m=(r+l)//2
    build(2*v+1,l,m,do,a)
    build(2*v+2,m,r,do,a)
    do[v] = min(do[2*v+1],do[2*v+2])

def get_min(v,l,r,do,ql,qr):
    if ql<=l and qr>=r:
        return do[v]
    if ql >= r or qr<=l:
        return 1e9
    m = (r+l)//2
    tl = get_min (2*v+1,l,m,do,ql,qr)
    tr = get_min (2*v+2,m,r,do,ql,qr)
    return min(tl,tr)

def main():
    n,k=list(map(int,input().split(maxsplit=2)))
    a= list(map(int, input().split(maxsplit=n)))
    do= [0]*4*n
    build(0,0,n,do,a)
    
    
    for i in range(n-k+1):
        l,r = [i,i+k]
        print(get_min(0,0,n,do,l,r))
        
   


main()