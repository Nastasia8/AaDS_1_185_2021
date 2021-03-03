def kortezh(numbers):
    return tuple(sorted(set(numbers)))

numbers = input("Numbers: ").split()
print(kortezh(numbers))