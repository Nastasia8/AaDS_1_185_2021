

def build(v, l, r, do, a):
    if r-l == 1:
        do[v] = a[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, do, a)
    build(2*v+2, m, r, do, a)
    do[v] = do[2*v+1] + do[2*v+2]
    print(*do)

def get_k_zero(v, l, r, do, k):
    if k > do[v]:
        return -1
    if l == r:
        return l
    m = (r+l)//2
    if do[2*v+1] >= k:
        return get_k_zero(2*v+1, l, m, do, k)
    else:
        return get_k_zero(2*v+2, m+1, r, do, k - do[2*v+1])

n = int(input())
a = input().split()
a = [int(a[i])*0 if int(a[i]) != 0 else int(a[i]) + 1 for i in range(n)]
do = [0]*4*n
build(0, 0, n, do, a, n)
q = int(input())
index = []
while q != 0:
    l, r, k = map(int, input().split())
    index.append(get_k_zero(0, 0, n, do, k))
    q -= 1
print(*index)