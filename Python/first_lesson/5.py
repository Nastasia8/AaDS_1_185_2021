y = int(input("y="))
z = int(input("z="))


def function(y, z):
    arr = []
    for item in range(1, 21):
        if item % 2 == 1:
            arr.append(item**y**z)
    return arr


print(function(y, z))
print( [number **y**z if number%2==1 else number for number in range(1, 21)])