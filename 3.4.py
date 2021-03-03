def mn(a):
    b = set()
    for i in a:
        c = i
        for j in range(a.count(i)):
            b.add(c)
            c = c*10+i
    return b

a = [5, 6, 9, 6, 3, 5, 2, 5, 1]
print(mn(a))