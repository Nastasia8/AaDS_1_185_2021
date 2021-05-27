n = int(input())
k = list(map(int, input().split(maxsplit=n)))
s = 0
k.sort()
for l in range(n-1):
    if k[l] != k[l+1]:
        s += 1
print(s+1)