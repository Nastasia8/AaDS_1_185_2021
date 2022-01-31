def build(v, l, r, do, a):
    if r-l == 1:
        do[v] = [a[l], 1] 
        return

    m = (l+r)//2
    build(2*v + 1, l, m, do, a)
    build(2*v + 2, m, r, do, a)
    tl = do[2*v + 1]
    tr = do[2*v + 2]
    if tl[0] > tr[0]:
        do[v] = tl
    if tl[0] < tr[0]:
        do[v] = tr
    else:
        do[v] = [tl[0], tl[1] + tr[1]]

def get_max(v, l, r, do, ql, qr):
    if ql <= l and qr >= r: 
        return do[v]
    if ql >= r or qr <= l:
        return [-1e9, -1]
    m = (l+r)//2
    tl = get_max(2*v + 1, l, m, do, ql, qr)
    tr = get_max(2*v + 2, m, r, do, ql, qr)
    if tl[0] > tr[0]:
        return tl
    if tl[0] < tr[0]:
        return tr
    else:
        return [tl[0], tl[1] + tr[1]]

def update(v, l, r, do, idx, value):
    if r-l == 1:
        do[v][0] = value
        return
    m = (r+l)//2
    if idx < m:
        update(2*v+1, l, m, do, idx, value)
    else:
        update(2*v+2, m, r, do, idx, value)
    tl = do[2*v + 1]
    tr = do[2*v + 2]
    if tl[0] > tr[0]:
        return tl
    if tl[0] < tr[0]:
        return tr
    else:
        return [tl[0], tl[1] + tr[1]]
    
def main():
    n = int(input())
    do = [[0,0]]*4*n
    a = list(map(int, input().split()))[:n]
    build(0, 0, n, do, a)
    q = int(input())
    res = []
    while q !=0:
        que, l, r = map(str, input().split())
        if que=="s":
            res.append(get_max(0, 0, n, do, int(l)-1, int(r)))
        else:
            update(0, 0, n, do, int(l)-1, int(r))
        q-=1
    for e, i in res:
        print(i, end=" ")
main()