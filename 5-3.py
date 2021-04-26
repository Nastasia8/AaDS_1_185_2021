def build_tree(v, l, r, ts, a):
    if r - l == 1:
        ts[v] = a[l]
        return
    m = (r+l)//2
    build_tree(2*v+1, l, m, ts, a)
    build_tree(2*v+2, m, r, ts, a)
    ts[v] = nod(ts[2*v+1], ts[2*v+2])

def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b

def something(v, l, r, ts, ql, qr):
    if ql <= l and qr >= r:
        return ts[v]
    if ql >= r or qr <= l:
        return 0
    m = (r+l)//2
    tl = something(2*v+1, l, m, ts, ql, qr)
    tr = something(2*v+2, m, r, ts, ql, qr)
    return nod(tl, tr)

def main():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    ts = [0]*4*n
    build_tree(0, 0, n, ts, a)
    q = int(input())
    indexes = []
    while q != 0:
        l, r = map(int, input().split())
        indexes.append(something(0, 0, n, ts, l-1, r))
        q -= 1
    print(*indexes)

main()