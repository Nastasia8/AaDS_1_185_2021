#многие функции были написаны на паре, я не стал их коментить
def build(v, l, r, do, a):
    if r - l == 1:
        do[v] = a[l]
        return
    m = (r + l) // 2
    build(2*v+1, l, m, do, a)
    build(2*v+2, m, r, do, a)
    do[v] = do[2*v+1] + do[2*v+2]

def get_zero(v, l, r, do, k):
    if k > do[v]:
        return -1
    if r - l == 1:
        return r
    m = (r+l)//2
    if do[2*v+1] >= k:
        return get_zero(2*v+1, l, m, do, k)
    else:
        return get_zero(2*v+2, m, r, do, k - do[2*v+1])

def get_sum(v, l, r, do, ql, qr):
    if ql <= l and qr >= r:
        return do[v]
    if ql >= r or qr <= 1:
        return 0
    m = (r+l)//2
    tl = get_sum(2*v+1, l, m, do, ql, qr)
    tr = get_sum(2*v+2, m, r, do, ql, qr)
    return tl + tr

def main():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    do = [0] * 4 * n
    q = int(input())
    build(0, 0, n, do, a)
    index = []
    
    while q != 0:
        l, r, k = map(int, input().split())
        sum = get_sum(0,0, n, do, l-1, r)
        if sum >= k and l > 1: #если сумма больше или равна К и левая граница не 1
            index.append(get_zero(0, 0, n, do, k + get_sum(0, 0, n, do, 0, l-1)))
        elif sum >= k and l == 1: #если сумма больше или равна К и левая граница равна 1
            index.append(get_zero(0, 0, n, do, k))
        else:
            index.append(-1)
        q -= 1
    print(*index)
main()