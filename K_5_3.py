def build(v, l, r, do, a):
    if r - l == 1:
        do[v] = a[l]
        return
    m = (r + l) // 2
    build(2*v+1, l, m, do, a)
    build(2*v+2, m, r, do, a)
    do[v] = nod(do[2*v+1], do[2*v+2])

def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b

def nod_k(v, l, r, do, ql, qr):
    if ql <= l and qr >= r:
        return do[v]
    if ql >= r or qr <= l:
        return 0
    m = (r+l)//2
    tl = nod_k(2*v+1, l, m, do, ql, qr)
    tr = nod_k(2*v+2, m, r, do, ql, qr)
    return nod(tl, tr)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    do = [0] * 4 * n
    q = int(input())
    build(0, 0, n, do, a)
    index = []
    while q != 0:
        l, r = map(int, input().split())
        index.append(nod_k(0,0, n, do, l-1, r))
        q -= 1
    print(*index)
main()