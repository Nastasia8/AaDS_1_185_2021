x = int(input('x = '))
y = int(input('y = '))


def nod(x, y):
    a, b = x, y
    while x != y:
        if y > x:
            y -= x
        else:
            x -= y
    print(f'НОД({a},{b}) = {x}')


nod(x, y)
