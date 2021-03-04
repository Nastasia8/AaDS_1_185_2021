n = int(input('n: '))
k = set([int(i) for i in input().split()])
print(len(k))

#2
n = int(input('n: '))
k = sorted([int(i) for i in input().split()])
k2 = []
for i in k:
    if i not in k2:
        k2.append(i)
print(len(k2))
