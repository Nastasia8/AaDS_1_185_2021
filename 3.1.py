def one(x):
    numbers = list()
    while x > 1:
        if x % 2 == 0:
            x /= 2
            numbers.append(int(x))
        else:
            x = (x * 3 + 1) / 2
            numbers.append(int(x))
    print(numbers)

x = int(input("Число: "))
one(x)


