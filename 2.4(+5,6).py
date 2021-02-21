def Nod(x, y):
    while x != y:
        if x < y:
            y = y - x
        else:
            x = x - y
    return x

def Nod2(numbers):
    nods = list()
    for i in numbers:
        for j in numbers:
            nods.append(Nod(int(i),int(j)))
    return min(nods)


def Nok(x, y):
    return int((x*y)/Nod(x,y))

x = int(input("X= "))
y = int(input("Y= "))
print("НОД= " + str(Nod(x, y)))
print("НОК= " + str(Nok(x, y)))
numbers = input("Числа: ").split()
print("НОД чисел: " + str(Nod2(numbers)))