
"""
5
0 0 2 0 1
5
1 5 2
2 4 2
3 5 3
1 1 1
3 4 1
"""
def build(v, l, r, do, a):
    if r-l == 1:
        do[v] = a[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, do, a)
    build(2*v+2, m, r, do, a)
    do[v] = do[2*v+1] + do[2*v+2]

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
a = [0 if int(i) != 0 else 1 for i in input().split()]
do = [0]*4*n
build(0, 0, n, do, a)
q = int(input())
index = []
while q != 0:
    l, r, k = map(int, input().split())
    index.append(get_k_zero(0, l, r, do, k))
    q -= 1
print(*index)