def build(v, l, r, do, a):
    if r-l == 1:
        do[v] = a[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, do, a)
    build(2*v+2, m, r, do, a)
    do[v] = do[2*v+1] + do[2*v+2]

def get_k_zero(v, l, r, do, k):#функция для получения к-го нуля
    if k > do[v]:
        return -1#если К больше родительского элемента возвращаем -1
    if r - l == 1:#если длина =1, возвращаем r
        return r
    m = (r+l)//2#
    if do[2*v+1] >= k:#если левый потомок  >= k, то рекурсивно вызываем его
        return get_k_zero(2*v+1, l, m, do, k)
    else:#если правый потомок, то рекурсивно вызываем его
        return get_k_zero(2*v+2, m, r, do, k - do[2*v+1])

def get_sum(v, l, r, do, ql, qr):
    if ql <= l and qr >= r:
        return do[v]
    if ql >= r or qr <= l:
        return 0
    m = (r+l)//2
    tl = get_sum(2*v+1, l, m, do, ql, qr)
    tr = get_sum(2*v+2, m, r, do, ql, qr)
    return tl + tr

n = int(input())
a = [0 if int(i) != 0 else 1 for i in input().split()]
do = [0]*4*n
build(0, 0, n, do, a)
q = int(input())
index = []
while q != 0:
    l, r, k = map(int, input().split())
    sum_ = get_sum(0, 0, n, do, l-1, r)
    if sum_ >= k and l > 1:
        index.append(get_k_zero(0, 0, n, do, k+get_sum(0, 0, n, do, 0, l-1)))
    elif sum_ >= k and l == 1:
        index.append(get_k_zero(0, 0, n, do, k))
    else:
        index.append(-1)
    q -= 1
print(*index)
