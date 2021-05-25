
def find_k(v, ql, qr, do, k):
    if k > do[v]:
        return -1
    if qr - ql == 1:
        return qr
    m = (ql+qr)//2
    if do[v*2+1] >= k:
        return find_k(2*v+1, ql, m, do, k)
    return find_k(2*v+2, m, qr, do, k-do[2*v+1])


def get_sum(v, l, r, do, ql, qr):
    if ql <= l and qr >= r:
        return do[v]
    if ql >= r or qr <= l:
        return 0
    m = (r+l)//2
    tl = get_sum(2*v+1, l, m, do, ql, qr)
    tr = get_sum(2*v+2, m, r, do, ql, qr)
    return tl + tr


def build(v, l, r, do, a):
    if r-l == 1:
        do[v] = a[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, do, a)
    build(2*v+2, m, r, do, a)
    do[v] = do[2*v+1]+do[2*v+2]


def update(v, l, r, do, idx, value):
    if r-l == 1:
        do[v] = value
        return
    m = (r+l)//2
    if idx < m:
        update(2*v+1, l, m, do, idx, value)
    else:
        update(2*v+2, m, r, do, idx, value)
    do[v] = do[2*v + 1] + do[2*v + 2]


n = int(input())
a = list(map(int, input().split()))
q = int(input())
for i in range(n):
    if a[i] == 0:
        a[i] = 1
    else:
        a[i] = 0
do = [0]*4*n
build(0, 0, n, do, a)

index = []
while q != 0:
    requests = list(map(str, input().split()))
    if requests[0] == 's':
        # l, r, k = map(int, input().split())
        sum_zero = get_sum(0, 0, n, do, int(requests[1])-1, int(requests[2]))
        if sum_zero >= int(requests[3]) and int(requests[1]) > 1:
            index.append(
                find_k(0, 0, n, do, int(requests[3])+get_sum(0, 0, n, do, 0, int(requests[1])-1)))
        elif sum_zero >= int(requests[3]) and int(requests[1]) == 1:
            index.append(find_k(0, 0, n, do, int(requests[3])))
        else:
            index.append(-1)
    elif requests[0] == 'u':
        if int(requests[2]) == 0:
            requests[2] = 1
        else:
            requests[2] = 0

        update(0, 0, n, do, int(requests[1])-1, requests[2])
    q -= 1
print(*index)
#
