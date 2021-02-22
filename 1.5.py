def xyz(y, z):
    numbers = []
    for x in range(1, 21):
        if x % 2 != 0:
            numbers.append(x**y**z)
        else:
            numbers.append(x)
    return numbers

y = int(input("y= "))
z = int(input("z= "))
print(xyz(y,z))
        