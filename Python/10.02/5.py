x = int(input('x = '))
y = int(input('y = '))


def nok(x, y):
    if x >= y:
        k = x
    else:
        k = y
    while 1:
        if k % x == 0 and k % y == 0:
            print(f'НОК({x},{y}) = {k}')
            break
        k += 1


nok(12, 10)
