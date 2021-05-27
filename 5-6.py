def build(v, l, r, do, a):#аналогично 4му заданию
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
    m = (r+l)//2#нахождение середины
    if do[2*v+1] >= k:#если есть левый потомок  >= k, то рекурсивно вызываем его
        return get_k_zero(2*v+1, l, m, do, k)
    else:#если есть правый потомок, то рекурсивно вызываем его
        return get_k_zero(2*v+2, m, r, do, k - do[2*v+1])

def get_sum(v, l, r, do, ql, qr):# аналогично 4му заданию
    if ql <= l and qr >= r:
        return do[v]
    if ql >= r or qr <= l:
        return 0
    m = (r+l)//2
    tl = get_sum(2*v+1, l, m, do, ql, qr)
    tr = get_sum(2*v+2, m, r, do, ql, qr)
    return tl + tr

def update(v, l, r, do, idx, value):#добавляем функцию для обновления элементов
    if r-l == 1:
        do[v] = value
        return
    m = (r+l)//2
    if idx < m:
        update(2*v+1, l, m, do, idx, value)
    else:
        update(2*v+2, m, r, do, idx, value)
    do[v] = do[2*v+1] + do[2*v+2]

n = int(input())
a = [0 if int(i) != 0 else 1 for i in input().split()]# аналогично 4му заданию
do = [0]*4*n
build(0, 0, n, do, a)
q = int(input())
index = []
while q != 0:
    input_ = input().split()
    if len(input_) == 4:#изменяем ввод, если длина 4 символа
        l, r, k = int(input_[1]), int(input_[2]), int(input_[3])#обозначаем ввод для нахождения К нуля
        sum_ = get_sum(0, 0, n, do, l-1, r)
        if sum_ >= k and l > 1:
            index.append(get_k_zero(0, 0, n, do, k+get_sum(0, 0, n, do, 0, l-1)))
        elif sum_ >= k and l == 1:
            index.append(get_k_zero(0, 0, n, do, k))
        else:
            index.append(-1)
    else:
        i, v = int(input_[1]), int(input_[2])# условие для обновления элементов
        if v == 0:#для нуля
            update(0, 0, n, do, i-1, 1)
        else:#для других чисел
            update(0, 0, n, do, i-1, 0)
    q -= 1
print(*index)