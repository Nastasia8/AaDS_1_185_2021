# find_k работает на всем дереве, не на отрезке. возвращает индекс к-той единицы
def find_k(v, ql, qr, do, k):
    if k > do[v]:
        return -1
    if qr - ql == 1:
        return qr
    m = (ql+qr)//2
    if do[v*2+1] >= k:
        return find_k(2*v+1, ql, m, do, k)
    return find_k(2*v+2, m, qr, do, k-do[2*v+1])

# работает на отрезке. возвращает сумму единиц, которые являются нулями. возвращает количество нулей
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

# начало. цикл for переводит 0 в 1, а другие числа в 0
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] == 0:
        a[i] = 1
    else:
        a[i] = 0
# конец 

do = [0]*4*n
build(0, 0, n, do, a)
q = int(input())
index = []

while q != 0:
    l, r, k = map(int, input().split())
    sum_zero = get_sum(0, 0, n, do, l-1, r)

    if sum_zero >= k:
        if l > 1:
            index.append(find_k(0, 0, n, do, k+get_sum(0, 0, n, do, 0, l-1))) # k+get_sum это добавление суммы единиц отрезка до отрезка, на котором надо найти
             # 10|101|01 надо найти на 101, но т.к find_k не работает на отрезках, надо прибавить 10 к К
        elif l == 1:
            index.append(find_k(0, 0, n, do, k))
    else:
        index.append(-1)
    q -= 1

print(*index)