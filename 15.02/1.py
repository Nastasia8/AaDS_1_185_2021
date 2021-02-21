x = int(input('x = '))


def proverka(x):
    a = []
    while x != 1:
        if x % 2 == 0:
            x = x // 2
            a.append(x)
        else:
            x = (x*3+1)//2
            a.append(x)
    return a


print(proverka(x))
