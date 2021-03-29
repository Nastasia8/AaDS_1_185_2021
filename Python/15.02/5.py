n = int(input('n = '))
a = []
for i in range(n):
    a.append(int(input('')))


def tup(a):
    a_set = set(a)
    return tuple(sorted(a_set))


print(tup(a))
