q = int(input())
a = list(map(int, input().split(maxsplit = q)))
_a = [i for i in a]
for i in range(q - 1):
    for j in range(q - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            for i in a:
                print(i, end=" ")
            print()
if _a == a:
    print(0)