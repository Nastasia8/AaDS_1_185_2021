h = int(input('h = '))


def treug(h):
    a = [1, 1]
    b = [1, 1]
    print([1])
    print(a)
    k = 2
    for i in range(h-2):
        for j in range(1, k):
            b[j] = a[j]+a[j-1]
            if j == k-1:
                b.append(1)
        print(b)
        k += 1
        a = b[:]


treug(h)
#       [1]
#     [1, 1]
#    [1, 2, 1]
#   [1, 3, 3, 1]
#  [1, 4, 6, 4, 1]
# [1, 5, 10, 5, 1]
