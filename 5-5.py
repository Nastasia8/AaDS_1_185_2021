from math import gcd
def build_tree(v, l, r, ts, a):
    if r - l == 1:
        ts[v] = a[l]
        return
    m = (r+l)//2
    build_tree(2*v+1, l, m, ts, a)
    build_tree(2*v+2, m, r, ts, a)
    ts[v] = gcd(ts[2*v+1], ts[2*v+2])


def update(v, l, r, do, idx, value):
    if r-l == 1:
        do[v] = value
        return
    m = (r+l)//2
    if idx < m:
        update(2*v+1, l, m, do, idx, value)
    else:
        update(2*v+2, m, r, do, idx, value)
    do[v] = gcd(do[2*v + 1], do[2*v + 2])



def something(v, l, r, ts, ql, qr):
    if ql <= l and qr >= r:
        return ts[v]
    if ql >= r or qr <= l:
        return 0
    m = (r+l)//2
    tl = something(2*v+1, l, m, ts, ql, qr)
    tr = something(2*v+2, m, r, ts, ql, qr)
    return gcd(tl, tr)


def main():
    n = int(input())
    do = [0]*4*n
    a = list(map(int, input().split()))[:n]
    build_tree(0, 0, n, do, a)
    q = int(input())
    res = []
    while q !=0:
        que, l, r = map(str, input().split())
        if que=="s":
            res.append(something(0, 0, n, do, int(l)-1, int(r)))
        else:
            update(0, 0, n, do, int(l)-1, int(r))
        q-=1
    print(*res)


main()