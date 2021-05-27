
def build(v, l, r, do, a):
    if r-l == 1:
        do[v] = a[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, do, a)
    build(2*v+2, m, r, do, a)
    do[v] = do[2*v+1] + do[2*v+2]

def get_sum(v, l, r, do, ql, qr):
    if ql <= l and qr >= r:
        return do[v]
    if ql >= r or qr <= l:
        return 0
    m = (r+l)//2
    tl = get_sum(2*v+1, l, m, do, ql, qr)
    tr = get_sum(2*v+2, m, r, do, ql, qr)
    return tl + tr
def zero(num):
    for i in range(len(num)):
        if num[i] == 0:
            num[i] = 1
        else:
            num[i] = 0
    return num

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

def update(v, l, r, do, idx, value):
    if r-l == 1:
        do[v] = value
        return
    m = (r+l)//2
    if idx < m:
        update(2*v+1, l, m, do, idx, value)
    else:
        update(2*v+2, m, r, do, idx, value)
    do[v] = do[2*v+1] + do[2*v+2]


def main():
    n = int(input())
    num = list(map(int, input().split()))
    a = zero(num)
    do = [0] * 4 * n
    q = int(input())
    build(0, 0, n, do, a)
    index = []
    
    while q != 0:
        
        operation = list(map(str, input().split()))
        l, r = int(operation[1]), int(operation[2])
        if operation[0] == "s":
            k = int(operation[3])
            sum = get_sum(0, 0, n, do, l-1, r)
            if sum >= k and l > 1:
                index.append(get_zero(0, 0, n, do, k+get_sum(0, 0, n, do, 0, l-1)))
            elif sum >= k and l == 1:
                index.append(get_zero(0, 0, n, do, k))
            else:
                index.append(-1)
        else:
            if r == 0:
                update(0, 0, n, do, l-1, 1)
            else:
                update(0, 0, n, do, l-1, 0)

        q -= 1
    print(*index)
main()