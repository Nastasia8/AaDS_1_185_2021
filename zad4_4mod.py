#7 3
#1 3 2 4 5 3 1
def min(n, k, a):
    stak = []
    for i in range(k):
        while stak and a[i] <=a[stak[-1]]:
            stak.pop()
        stak.append(i)
    for i in range(k, n):
        print(a[stak[0]])
        while stak and i - k >= stak[0]:
            stak.pop(0)
        while stak and a[i] <= a[stak[-1]]:
            stak.pop()
        stak.append(i)
    print(a[stak[0]])
n, k = map(int, input().split())
a = list(map(int, input().split()))
min(n, k, a)